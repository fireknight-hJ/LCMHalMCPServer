from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.analyze_results.function_analyze import FixedFunctionInfo
from models.analyze_results.function_analyze import ReplacementUpdate
from prompts.function_fixer import system_prompt_en
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_json_log
import config.globs as globs
from tools.fixer.replacement_update import update_function_replacement

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: ReplacementUpdate


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
            # Collector 获取数据结构信息
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
        }
    )
    # 异步获取工具
    tools = await client.get_tools()
    # 添加函数替换工具
    tools.append(update_function_replacement)

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model_with_tools.with_structured_output(ReplacementUpdate)

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
    """
    fix the problematic functions based on error feedback
    """
    graph = await build_graph()
    result = await graph.ainvoke({"messages": [
        {"role": "system", "content": system_prompt_en},
        {"role": "user", "content": f"Analyze the emulator error feedback and fix the problematic functions in the driver source code accordingly."}
    ]}, config={"recursion_limit": 50})
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("function_fix", result)
    resp = result["final_response"]
    dump_json_log("replacement_update", resp.model_dump())
    return result["final_response"]

async def main():
    # Test the graph
    locate_response = await dump_message_json_log()
    print(f"Driver dir locate response: {locate_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())