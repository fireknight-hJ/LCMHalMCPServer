from langchain.agents import create_agent
from langgraph_supervisor import create_supervisor
from langchain_deepseek import ChatDeepSeek
from langgraph.graph import END, START, StateGraph, MessagesState
from config.llm_config import llm_deepseek_config
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
import time

from utils.db_cache import dump_message_json_log, check_analyzed_json_log, dump_message_raw_log
from models.emulate_results.emulate_result import EmulateResult
from prompts.emulator_multiagent import project_builder_prompt, supervisor_prompt, function_fixer_prompt
import config.globs as globs

# TODO: 测试完成后，移除下面的硬编码路径设置
# 编译脚本路径
globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
# codeql的DB路径
globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
# 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
# 项目路径, DB中记录的项目路径
globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"

# brain + emulate
supervisor_mcpclient = MultiServerMCPClient(
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
        }
    }
)

# 编译agent
builder_mcpclient = MultiServerMCPClient(
    {
        "lcmhal_builder": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [
                "-m",
                "tools.builder.mcp_server",
                "--script-dir",
                globs.script_path
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

        # using stdio
    }
)


fixer_mcpclient = MultiServerMCPClient(
    {
        "lcmhal_builder": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": [
                "-m",
                "tools.builder.mcp_server",
                "--script-dir",
                globs.script_path
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

# Initialize the model
model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

builder_tools = builder_mcpclient.get_tools()
builder_agent = create_agent(
    model=model,
    tools=builder_tools,
    prompt=(
        project_builder_prompt
    ),
    name="builder_agent",
)

fixer_tools = fixer_mcpclient.get_tools()
fixer_agent = create_agent(
    model=model,
    tools=fixer_tools,
    prompt=(
        function_fixer_prompt
    ),
    name="fixer_agent",
)

supervisor_agent = create_supervisor(
    model=model,
    tools= supervisor_mcpclient.get_tools(),
    agents=[builder_agent, fixer_agent],
    prompt=(
        supervisor_prompt
    ),
    add_handoff_back_messages=True,
    output_mode="full_history",
).compile()

from langgraph.graph import END

# Define the multi-agent supervisor graph
supervisor = (
    StateGraph(MessagesState)
    # NOTE: `destinations` is only needed for visualization and doesn't affect runtime behavior
    .add_node(supervisor_agent, destinations=("research_agent", "math_agent", END))
    .add_node(builder_agent)
    .add_node(fixer_agent)
    .add_edge(START, "supervisor")
    # always return back to the supervisor
    .add_edge("research_agent", "supervisor")
    .add_edge("math_agent", "supervisor")
    .compile()
)

async def run_emulator() -> EmulateResult:
    graph = supervisor
    result = await graph.ainvoke({"messages": [
        {"role": "user", "content": f"emulate the project, rerun-fix-rebuild the project until the project is successfully run."}
    ]}, config={"recursion_limit": 50})
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("run_emulator", result)
    return result["final_response"]

async def main():
    # Test the graph
    emulate_response = await run_emulator()
    print(f"Emulate response: {emulate_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())