from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from models.analyze_results.driverdir_locate import DriverDirLocatorResponse
from prompts.driverdir_locator import system_prompting_en
from prompts.summary_prompt import summary_prompt_en as SUMMARY_PROMPT
import os
import time
from utils.db_cache import dump_message_json_log, check_analyzed_json_log
from utils.ai_log_manager import ai_log_manager
from utils.failcheck import check_iteration_limit
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
    final_response: DriverDirLocatorResponse
    # Function name being located
    function_name: str
    # Counter to prevent infinite loops
    iteration_count: int = 0

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
            file_path = os.path.join(tmp_dir, f"driver_dir_locate_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.dump_message_json())

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
    model_with_structured_output = model.with_structured_output(DriverDirLocatorResponse)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Create a wrapper for tool_node to add logging
    async def tools_with_logging(state: AgentState):
        agent_name = "driver_locator_agent"
        node_name = "tools"
        function_name = state.get("function_name", "driver_dir_locate")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        result = await tool_node.ainvoke(state)
        
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

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "driver_locator_agent"
        node_name = "respond"
        function_name = state.get("function_name", "driver_dir_locate")
        
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
        agent_name = "driver_locator_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "driver_dir_locate")
        
        # 检查迭代次数限制
        current_iteration = state.get("iteration_count", 0)
        new_iteration = check_iteration_limit(state, max_iterations=100, agent_name=agent_name)
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        
        result = {"messages": [response], "iteration_count": new_iteration}
        
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

async def driver_dir_locate() -> DriverDirLocatorResponse:
    graph = await build_graph()
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompting_en},
            {"role": "user", "content": f"Find the driver directory and kernel support directory of the project"}
        ],
        "function_name": "driver_dir_locate",
        "iteration_count": 0  # 显式设置初始迭代次数
    }
    result = await graph.ainvoke(initial_state, config={"recursion_limit": 100})  # 添加recursion_limit配置
    # log ai memory
    if globs.ai_log_enable:
        dump_message_json_log("driver_dir_locate", result)
    return result["final_response"]

def check_analyzed() -> bool:
    """
    检查函数是否已经分析过
    """
    return check_analyzed_json_log(msg_type="driver_dir_locate")

async def main():
    # Test the graph
    locate_response = await driver_dir_locate()
    print(f"Driver dir locate response: {locate_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())