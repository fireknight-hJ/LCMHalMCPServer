from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode

# Initialize the model
model = init_chat_model("anthropic:claude-3-5-sonnet-latest")

# Set up MCP client
client = MultiServerMCPClient(
    {
        "lcmhal_info_collector": {
            "command": "python",
            # Make sure to update to the full absolute path to your mcp_server.py file
            "args": ["./tools/collector/mcp_server.py"],
            "transport": "stdio",
        },
    }
)
tools = client.get_tools()

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

async def test_graph():
    """测试图功能的异步函数"""
    # Test the graph
    math_response = await graph.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    weather_response = await graph.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print(f"Math response: {math_response}")
    print(f"Weather response: {weather_response}")

# 在文件末尾添加运行代码
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_graph())