import json
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.analyze_results.function_analyze import FunctionClassifyResponse
from prompts.function_classifier import system_prompting_en
from prompts.summary_prompt import function_classify_final_prompt_en as SUMMARY_PROMPT
import os
import time
import asyncio
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, get_analyzed_json_log
from utils.ai_log_manager import ai_log_manager
import config.globs as globs

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

# Set up MCP client
client = MultiServerMCPClient(
    {
        # using connection
        # "lcmhal_collector": {
        #     # make sure you start your weather server on port 8000
        #     "url": "http://localhost:8112/mcp/",
        #     "transport": "streamable_http",
        # },
        "lcmhal_collector": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [
                "-m",
                "tools.collector.mcp_server",
                "--db-path",
                globs.db_path,
                "--transport",
                "stdio"
            ],
            # "cwd": "/home/haojie/workspace/lcmhalmcp",
            "transport": "stdio"
        },

        # using stdio
    }
)

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: FunctionClassifyResponse
    # Function name being classified
    function_name: str

# 全局变量存储graph实例
_graph = None

async def build_graph():
    global _graph
    # 如果graph已经构建过，直接返回
    if _graph is not None:
        return _graph
    
    # 异步获取工具
    tools = await client.get_tools()

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(FunctionClassifyResponse)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Create a wrapper for tool_node to add logging
    async def tools_with_logging(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "tools"
        function_name = state.get("function_name", "unknown")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        result = await tool_node.ainvoke(state)
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "respond"
        function_name = state.get("function_name", "unknown")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        # Use the imported summary prompt to ensure LLM only summarizes and doesn't call tools
        response = model_with_structured_output.invoke(
            state["messages"] + [HumanMessage(content=SUMMARY_PROMPT)]
        )
        # We return the final answer
        result = {"final_response": response}
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
            # 记录精炼对话记录
            ai_log_manager.log_agent_refined_memory(
                agent_name=agent_name,
                state=updated_state,
                function_name=function_name
            )
        
        return result

    def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        else:
            return "respond"

    # Define call_model function
    async def call_model(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "unknown")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        
        result = {"messages": [response]}
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    # Build the graph
    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tools_with_logging)

    builder.add_edge(START, "agent")
    builder.add_conditional_edges(
        "agent",
        should_continue,
    )
    builder.add_edge("tools", "agent")
    builder.add_edge("respond", END)

    # Compile the graph and存储到全局变量
    _graph = builder.compile()
    return _graph

async def function_classify(func_name : str, overwrite: bool = False) -> FunctionClassifyResponse:
    # 检查函数是否已经分析过
    if check_analyzed(func_name) and not overwrite:
        # print(f"Function {func_name} has been analyzed, skip.")
        return function_classify_from_log(func_name)
    # 构建graph
    graph = await build_graph()
    # llm 调用
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompting_en},
            {"role": "user", "content": f"Classify the function : {func_name}"}
        ],
        "function_name": func_name
        # 移除自定义计数器，直接使用LangGraph的错误处理
    }
    
    try:
        result = await graph.ainvoke(initial_state, config={"recursion_limit": 50})  # 添加recursion_limit配置
        # log ai memory
        if globs.ai_log_enable:
            dump_message_json_log("function_classify", result)
        return result["final_response"]
    except Exception as e:
        from langgraph.errors import GraphRecursionError
        if isinstance(e, GraphRecursionError):
            # 捕获LangGraph的递归错误，触发failcheck分析
            from utils.failcheck import analyze_failed_conversation
            analyze_failed_conversation(initial_state["messages"], "analyzer_agent", 50)  # 50次agent调用
        else:
            # 其他错误直接抛出
            raise

def check_analyzed(func_name: str) -> bool:
    """
    检查函数是否已经分析过
    """
    return check_analyzed_json_log("function_classify", func_name)

def get_analyzed(func_name: str) -> str:
    """
    获取函数分析日志
    """
    return get_analyzed_json_log("function_classify", func_name)

def function_classify_from_log(func_name: str) -> FunctionClassifyResponse:
    """
    从JSON日志中获取函数分析结果
    """
    infos = get_analyzed(func_name)
    json_data = json.loads(infos)
    return FunctionClassifyResponse(**json_data["final_response"])

async def analyze_functions(function_list):
    mmio_info_list = {}
    max_retries = 3
    retry_delay = 1  # 秒
    
    async def classify_with_retry(func_name):
        """带重试机制的函数分类"""
        for attempt in range(max_retries):
            try:
                result = await function_classify(func_name)
                if result:
                    return result
                else:
                    print(f"Warning: Empty result for {func_name}, retrying ({attempt + 1}/{max_retries})...")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(retry_delay)
            except Exception as e:
                print(f"Error analyzing {func_name} (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
        return None
    
    tasks = []
    for func_name in function_list:
        tasks.append(classify_with_retry(func_name))
    
    results = await asyncio.gather(*tasks)
    
    for func_name, result in zip(function_list, results):
        if result:
            mmio_info_list[func_name] = result
        else:
            print(f"Error: Failed to analyze {func_name} after {max_retries} attempts")
            mmio_info_list[func_name] = None
    
    return mmio_info_list

@tool(
    "Analyzer",
    description="Sub Agent `Analyzer`, analyze the driver source code and classify the functions into MMIO and non-MMIO functions"
)
async def analyzer_agent(func_name : str) -> FunctionClassifyResponse:
    return await function_classify(func_name, False)

async def main():
    # Test the graph
    classify_response = await function_classify("HAL_ETH_ReadData", True)
    print(f"Classify response: {classify_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())