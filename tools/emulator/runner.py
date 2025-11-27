# 运行并动态修复

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.emulate_results.emulate_result import EmulateResult
from prompts.project_emulator import system_prompting_en
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_message_raw_log
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
        "lcmhal_emulator": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [
                "-m",
                "tools.emulator.mcp_server",
                "--script-dir",
                globs.script_path
                # "--transport",
                # "stdio"
            ],
            # "cwd": "/home/haojie/workspace/lcmhalmcp",
            "transport": "stdio"
        },
        "lcmhal_builder": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [
                "-m",
                "tools.builder.mcp_server",
                "--script-dir",
                globs.script_path
                # "--transport",
                # "stdio"
            ],
            # "cwd": "/home/haojie/workspace/lcmhalmcp",
            "transport": "stdio"
        },
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

class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: EmulateResult

    # @DeprecationWarning("use log.dump_message instead")
    def dump_message(self):
        model_list =  [i.model_dump() for i in self["messages"]]
        return {
            "messages": model_list,
            "final_response": self["final_response"].model_dump()
        }
    
    # @DeprecationWarning("use log.dump_message_json instead")
    def dump_message_json(self):
        import json
        return json.dumps(self.dump_message(), ensure_ascii=False, indent=2)
    
    # @DeprecationWarning("use log.dump_message_json_log instead")    
    def dump_message_json_log(self, file_path: str = ""):
        if file_path == "":
            # 当前项目执行路径
            work_dir = os.path.dirname(os.path.abspath(__file__))
            tmp_dir = os.path.join(work_dir, "tmp")
            if not os.path.exists(tmp_dir):
                os.makedirs(tmp_dir)
            file_path = os.path.join(tmp_dir, f"builder_tool_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.dump_message_json())

def dump_message_state(state):
    model_list =  [i.model_dump() for i in state["messages"]]
    return {
        "messages": model_list
    }

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
    model_with_structured_output = model.with_structured_output(EmulateResult)

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
        import json
        dump_message_raw_log("emulator_state", json.dumps(dump_message_state(state), ensure_ascii=False, indent=2), overwrite=True)
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

async def run_emulator() -> EmulateResult:
    graph = await build_graph()
    result = await graph.ainvoke({"messages": [
        {"role": "system", "content": system_prompting_en},
        {"role": "user", "content": f"emulate the project, rerun-fix-rebuild the project until the project is successfully run."}
    ]}, config={"recursion_limit": 50})
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("run_emulator", result)
    return result["final_response"]

def check_analyzed() -> bool:
    """
    检查函数是否已经分析过
    """
    return check_analyzed_json_log(msg_type="build_project")

async def main():
    # Test the graph
    emulate_response = await run_emulator()
    print(f"Emulate response: {emulate_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    # 编译脚本路径
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    # codeql的DB路径
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    # 项目路径, DB中记录的项目路径
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"

    import asyncio
    asyncio.run(main())