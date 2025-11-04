from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from config import globs 
import os

# Initialize the model
# model = init_chat_model("anthropic:claude-3-5-sonnet-latest")

# TODO: remove mock config
llm_deepseek_config = {
    "base_url" : "https://api.deepseek.com",
    "model_name" : "deepseek-chat",
    "api_key" : "sk-6bf25f3820ee4d69a56b42ffaf8bab84"
}

model = ChatOpenAI(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    base_url=llm_deepseek_config["base_url"]
)

# Set up MCP client
client = MultiServerMCPClient(
    {
        # using connection
        # "lcmhal_collector": {
        #     # make sure you start your weather server on port 8000
        #     "url": "http://localhost:8112/mcp/",
        #     "transport": "streamable_http",
        # }

        # using stdio
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

async def main():
    # 异步获取工具
    tools = await client.get_tools()

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)

    # Create ToolNode
    tool_node = ToolNode(tools)

    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END

    # Define call_model function
    async def call_model(state: MessagesState):
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        return {"messages": [response]}

    # Build the graph
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", tool_node)

    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        should_continue,
    )
    builder.add_edge("tools", "call_model")

    # Compile the graph
    graph = builder.compile()

    # Test the graph
    # analyze_response = await graph.ainvoke(
    #     {"messages": [{"role": "user", "content": "Analyze the database : /home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer, then get the mmio function list"}]}
    # )
    # analyze_response = await graph.ainvoke(
    #     {"messages": [{"role": "user", "content": "Register Database : /home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer, then Analyze the mmio function : HAL_I2C_Mem_Read"}]}
    # )
    analyze_response = await graph.ainvoke(
        {"messages": [{"role": "user", "content": "Get all the mmio file paths"}]}
    )
    print(f"Analyze response: {analyze_response}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())