from langchain.chat_models import init_chat_model
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
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_json_log
import config.globs as globs
from tools.builder.core import init_builder
from tools.builder.tool import build_project, get_replace_func_details_by_file, update_function_replacement
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
    # Counter to prevent infinite loops
    iteration_count: int = 0


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
            # Emulator 执行模拟器，获取错误反馈
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
    init_builder()
    
    from tools.fixer.replacement_update import update_function_replacement
    # 异步获取工具
    tools = await client.get_tools()
    # 定义工具列表
    tools = tools + [
        # emulator工具
        emulate_proj,
        mmio_function_emulate_info,
        function_calls_emulate_info,
        # builder工具
        get_replace_func_details_by_file,
        update_function_replacement
    ]

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(ReplacementUpdate)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Define the function that responds to the user
    def respond(state: AgentState):
        response = model_with_structured_output.invoke(
            # [HumanMessage(content=state["messages"][-1].content)]
            state["messages"]
        )
        # We return the final answer
        return {"final_response": response}

    def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        else:
            return "respond"

    # Define call_model function
    async def call_model(state: AgentState):
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        return {"messages": [response]}

    # Build the graph
    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tool_node)

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
    result = await graph.ainvoke({"messages": [
        {"role": "system", "content": system_prompt_en},
        {"role": "user", "content": f"Analyze the emulator error feedback and fix the problematic functions in the driver source code accordingly."}
    ]}, config={"recursion_limit": 50})
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("function_fix", result)
    return result["final_response"]

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