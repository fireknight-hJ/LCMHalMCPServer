from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from config.llm_config import llm_deepseek_config
from models.analyze_results.function_analyze import FixedFunctionInfo
from models.analyze_results.function_analyze import ReplacementUpdate
from prompts.function_fixer import system_prompt_en
from prompts.summary_prompt import fixer_summary_prompt_en as SUMMARY_PROMPT
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_json_log
from utils.ai_log_manager import ai_log_manager
import config.globs as globs
from tools.builder.core import init_builder
from tools.builder.tool import build_project, get_replace_func_details_by_file, update_function_replacement, get_function_analysis_and_replacement
from tools.emulator.tool import emulate_proj, mmio_function_emulate_info, function_calls_emulate_info

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: ReplacementUpdate
    # Function name being fixed
    function_name: str


# 全局变量存储graph实例
_graph = None



async def build_graph():
    # global _graph
    # # 如果graph已经构建过，直接返回
    # if _graph is not None:
    #     return _graph
    # Set up MCP client
    client = MultiServerMCPClient(
        {
            # # Emulator 执行模拟器，获取错误反馈
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
            # "lcmhal_emulator": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": [
            #         "-m",
            #         "tools.emulator.mcp_server",
            #         "--script-dir",
            #         globs.script_path,
            #         # "--transport",
            #         # "stdio"
            #     ],
            #     # "cwd": "/home/haojie/workspace/lcmhalmcp",
            #     "transport": "stdio"
            # },
            # # Builder 执行构建命令，检查是否通过
            # "lcmhal_builder": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": [
            #         "-m",
            #         "tools.builder.mcp_server",
            #         "--script-dir",
            #         globs.script_path,
            #         # "--transport",
            #         # "stdio"
            #     ],
            #     # "cwd": "/home/haojie/workspace/lcmhalmcp",
            #     "transport": "stdio"
            # },

            # using stdio
        }
    )
    global _graph
    # 如果graph已经构建过，直接返回
    if _graph is not None:
        return _graph
    
    # 初始化builder工具
    await init_builder()
    
    # 异步获取工具
    tools = await client.get_tools()
    # 定义工具列表
    tools = tools + [
        # emulator工具
        # emulate_proj,
        mmio_function_emulate_info,
        function_calls_emulate_info,
        # builder工具
        get_replace_func_details_by_file,
        update_function_replacement,
        get_function_analysis_and_replacement
    ]

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(ReplacementUpdate)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Create a wrapper for tool_node to add logging
    async def tools_with_logging(state: AgentState):
        agent_name = "fixer_agent"
        node_name = "tools"
        function_name = state.get("function_name", "function_fix")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        result = await tool_node.ainvoke(state)
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "fixer_agent"
        node_name = "respond"
        function_name = state.get("function_name", "function_fix")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        # Use the imported summary prompt to ensure LLM only summarizes and doesn't call tools
        max_retries = 5
        retry_count = 0
        response = None
        
        while retry_count < max_retries and response is None:
            try:
                response = model_with_structured_output.invoke(
                    state["messages"] + [HumanMessage(content=SUMMARY_PROMPT)]
                )
                # We return the final answer
                result = {"final_response": response}
            except Exception as e:
                retry_count += 1
                print(f"[ERROR] Failed to generate structured response (attempt {retry_count}/{max_retries}): {e}")
                
        # 如果所有重试都失败，使用回退方案
        if response is None:
            print(f"[ERROR] All {max_retries} attempts failed, using fallback")
            result = {"final_response": ReplacementUpdate(
                function_name=function_name,
                replacement_code="",
                reason="Failed to generate replacement code after multiple attempts"
            )}
        
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
        agent_name = "fixer_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "function_fix")
        
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

async def function_fix() -> ReplacementUpdate:
    graph = await build_graph()
    
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompt_en},
            {"role": "user", "content": f"Analyze the emulator error feedback and fix the problematic functions in the driver source code accordingly."}
        ],
        "function_name": "function_fix"
        # 移除自定义计数器，直接使用LangGraph的错误处理
    }
    
    try:
        result = await graph.ainvoke(initial_state, config={"recursion_limit": 50})
        # log ai memory
        if globs.ai_log_enable:
            dump_message_json_log("function_fix", result)
        return result["final_response"]
    except Exception as e:
        from langgraph.errors import GraphRecursionError
        if isinstance(e, GraphRecursionError):
            # 捕获LangGraph的递归错误，触发failcheck分析
            from utils.failcheck import analyze_failed_conversation
            analyze_failed_conversation(initial_state["messages"], "fixer_agent", 50)  # 50次agent调用
        else:
            # 其他错误直接抛出
            raise

@tool(
    "Fixer",
    description="Sub Agent `Fixer`, analyze the emulator error feedback and fix the problematic functions in the driver source code accordingly"
)
async def fixer_agent() -> ReplacementUpdate:
    result = await function_fix()
    return result

async def main():
    # Test the graph
    fixer_response = await function_fix()
    print(f"Fixer response: {fixer_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    # 导入argparse模块（如果尚未导入）
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='LCMHal Fixer')
    # 添加--script-dir选项参数，设置help信息
    parser.add_argument('--script-dir', dest='script_path', help='Path to the compilation script directory', required=True)
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 从命令行参数设置script_path
    globs.script_path = args.script_path
    # 从配置文件加载配置
    config = globs.load_config_from_yaml(globs.script_path)
    
    # 设置全局变量
    globs.globs_init(config)
    
    # 输出配置信息
    print(f"Configuration:")
    print(f"  script_path: {globs.script_path}")
    print(f"  db_path: {globs.db_path}")
    print(f"  src_path: {globs.src_path}")
    print(f"  proj_path: {globs.proj_path}")
    
    import asyncio
    asyncio.run(main())