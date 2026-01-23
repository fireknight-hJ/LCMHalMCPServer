# 运行并动态修复
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.emulate_results.emulate_result import EmulateResult
from models.build_results.build_output import BuildOutput
from models.analyze_results.function_analyze import ReplacementUpdate
from prompts.project_emulator import system_prompting_en
from prompts.summary_prompt import summary_prompt_en as SUMMARY_PROMPT
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_message_raw_log
from utils.ai_log_manager import ai_log_manager
import config.globs as globs
from agents.builder_agent import builder_agent
from agents.fixer_agent import fixer_agent

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: EmulateResult
    # Function name being emulated
    function_name: str


# 全局变量存储graph实例
_graph = None

_overwrite = False

async def build_graph():
    client = MultiServerMCPClient(
        {
            # "lcmhal_collector": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": [
            #         "-m",
            #         "tools.collector.mcp_server",
            #         "--db-path",
            #         globs.db_path,
            #         "--transport",
            #         "stdio"
            #     ],
            #     # "cwd": "/home/haojie/workspace/lcmhalmcp",
            #     "transport": "stdio"
            # },
            "lcmhal_emulator": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": [
                    "-m",
                    "tools.emulator.mcp_server",
                    "--script-dir",
                    globs.script_path,
                    # "--transport",
                    # "stdio"
                ],
                # "cwd": "/home/haojie/workspace/lcmhalmcp",
                "transport": "stdio"
            },
            # using stdio
        }
    )
    global _graph
    # 如果graph已经构建过，直接返回
    if _graph is not None:
        return _graph
    
    # 异步获取工具
    tools = await client.get_tools()
    tools.append(builder_agent)
    tools.append(fixer_agent)

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(EmulateResult)

    # 创建自定义工具调用函数，避免使用ToolNode
    async def tools_with_logging(state: AgentState):
        agent_name = "emulator_runner_agent"
        node_name = "tools"
        function_name = state.get("function_name", "run_emulator")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        # 直接调用工具，避免使用ToolNode
        messages = state["messages"]
        last_message = messages[-1]
        
        result_messages = []
        
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            for tool_call in last_message.tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call['args']
                
                # 查找对应的工具
                tool = None
                for t in tools:
                    if t.name == tool_name:
                        tool = t
                        break
                
                if tool:
                    try:
                        # 调用工具
                        tool_output = await tool.ainvoke(tool_args)
                        result_messages.append({
                            "role": "tool",
                            "content": str(tool_output),
                            "tool_call_id": tool_call['id'],
                            "name": tool_name
                        })
                    except Exception as e:
                        result_messages.append({
                            "role": "tool",
                            "content": f"Error: {str(e)}",
                            "tool_call_id": tool_call['id'],
                            "name": tool_name
                        })
        
        result = {"messages": result_messages}
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "emulator_runner_agent"
        node_name = "respond"
        function_name = state.get("function_name", "run_emulator")
        
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
        import json
        global _overwrite
        dump_message_raw_log("emulator_state", json.dumps(dump_message_state(state), ensure_ascii=False, indent=2), overwrite=_overwrite)
        if _overwrite == False:
            _overwrite = True
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        else:
            return "respond"

    # Define call_model function
    async def call_model(state: AgentState):
        agent_name = "emulator_runner_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "run_emulator")
        
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

async def run_emulator() -> EmulateResult:
    graph = await build_graph()
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompting_en},
            {"role": "user", "content": f"Emulate the project, rerun-fix-rebuild the project until the project is successfully run."}
        ],
        "function_name": "run_emulator"
        # 移除自定义计数器，直接使用LangGraph的错误处理
    }
    
    try:
        result = await graph.ainvoke(initial_state, config={"recursion_limit": 50})
        # log ai memory
        if globs.ai_log_enable:
            dump_message_json_log("run_emulator", result)
        return result["final_response"]
    except Exception as e:
        from langgraph.errors import GraphRecursionError
        if isinstance(e, GraphRecursionError):
            # 捕获LangGraph的递归错误，触发failcheck分析
            from utils.failcheck import analyze_failed_conversation
            analyze_failed_conversation(initial_state["messages"], "emulator_runner_agent", 50)  # 50次agent调用
        else:
            # 其他错误直接抛出
            raise


def dump_message_state(state):
    model_list =  [i.model_dump() for i in state["messages"]]
    return {
        "messages": model_list
    }

async def main():
    # 导入argparse模块
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='LCMHal Emulator Runner')
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
    
    # Test the graph
    emulate_response = await run_emulator()
    print(f"Emulate response: {emulate_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
