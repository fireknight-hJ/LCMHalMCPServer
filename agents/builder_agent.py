from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.build_results.build_output import BuildOutput
from prompts.project_builder import system_prompting_en
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log
from utils.ai_log_manager import ai_log_manager
import config.globs as globs
from tools.builder.core import init_builder
from tools.builder.tool import build_project, get_replace_func_details_by_file, update_function_replacement

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: BuildOutput
    # Function name being built
    function_name: str

# 全局变量存储graph实例
_graph = None



async def build_graph():
    # 确保script_path不为空
    if not globs.script_path:
        globs.script_path = globs.default_config["script_path"]
        print(f"builder.py: script_path为空，使用默认值: {globs.script_path}")
    
    # Set up MCP client
    client = MultiServerMCPClient(
        {
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
            # "lcmhal_builder": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your math_server.py file
            #     "args": [
            #         "-m",
            #         "tools.builder.mcp_server",
            #         "--script-dir",
            #         globs.script_path
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
    
    # 异步获取工具
    tools = await client.get_tools()
    # 初始化builder工具
    init_builder()
    
    # 定义工具列表
    tools = tools + [
        build_project,
        get_replace_func_details_by_file,
        update_function_replacement
    ]
    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(BuildOutput)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Create a wrapper for tool_node to add logging
    async def tools_with_logging(state: AgentState):
        agent_name = "builder_agent"
        node_name = "tools"
        function_name = state.get("function_name", "build_project")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        result = await tool_node.ainvoke(state)
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "builder_agent"
        node_name = "respond"
        function_name = state.get("function_name", "build_project")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        response = model_with_structured_output.invoke(
            # [HumanMessage(content=state["messages"][-1].content)]
            state["messages"]
        )
        # We return the final answer
        result = {"final_response": response}
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
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
        agent_name = "builder_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "build_project")
        
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

async def run_build_project() -> BuildOutput:
    graph = await build_graph()
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompting_en},
            {"role": "user", "content": f"Build the project and fix the errors recursively, until the build is successful."}
        ],
        "function_name": "build_project"
    }
    result = await graph.ainvoke(initial_state, config={"recursion_limit": 50})
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("build_project", result)
    return result["final_response"]

@tool(
    "Builder",
    description="Sub Agent `Builder`, build the project and return the build result (call this tool after calling Fixer, fixed the source code)"
)
async def builder_agent() -> BuildOutput:
    result = await run_build_project()
    return result

def check_analyzed() -> bool:
    """
    检查函数是否已经分析过
    """
    return check_analyzed_json_log(msg_type="build_project")

async def main():
    # Test the graph
    build_response = await run_build_project()
    print(f"Build project response: {build_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    # 导入argparse模块（如果尚未导入）
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='LCMHal Builder')
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