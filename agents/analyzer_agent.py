import json
from langchain_core.tools import tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from config.model_singleton import get_model
from models.analyze_results.function_analyze import FunctionClassifyResponse
from prompts.function_classifier import system_prompting_en
from prompts.summary_prompt import function_classify_final_prompt_en as SUMMARY_PROMPT
import os
import time
import asyncio
from utils.db_cache import dump_message_json_log, check_analyzed_json_log, get_analyzed_json_log
from utils.ai_log_manager import ai_log_manager
from utils.replacement_rubric import check_replacement_rubric
from tools.collector.collector import get_function_source
import config.globs as globs

# 使用统一的模型实例
model = get_model()

# MCP client 不再在模块加载时创建，否则会用到 import 时的默认 globs.db_path（main 尚未 globs_init）。
# 改为在 build_graph() 内用当前 globs.db_path 创建，保证 GetFunctionInfo 等工具连到正确 DB。
_client = None


class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: FunctionClassifyResponse
    # Function name being classified
    function_name: str

# 全局变量存储graph实例及创建时使用的 db_path（切换 testcase 时需重建）
_graph = None
_graph_db_path = None

async def build_graph():
    global _graph, _client, _graph_db_path
    db_path = getattr(globs, "db_path", None) or ""
    # 若已构建过但 db_path 已变（例如换了 testcase），则失效缓存，用新 DB 重建
    if _graph is not None and _graph_db_path != db_path:
        _graph = None
        _graph_db_path = None
    # 如果graph已经构建过，直接返回
    if _graph is not None:
        return _graph

    # 用当前 globs.db_path 创建 MCP client，保证 GetFunctionInfo 等连到当前 testcase 的 DB（非默认）
    _client = MultiServerMCPClient(
        {
            "lcmhal_collector": {
                "command": "python",
                "args": [
                    "-m",
                    "tools.collector.mcp_server",
                    "--db-path",
                    db_path,
                    "--transport",
                    "stdio"
                ],
                "transport": "stdio"
            },
        }
    )

    # 异步获取工具（Collector MCP + 验证与修复委托）；延迟导入避免与 data_manager 循环依赖
    from tools.builder.tool import verify_replacement as verify_replacement_tool
    from agents.builder_fixer_agent import builder_fixer_agent
    tools = await _client.get_tools()
    tools = tools + [verify_replacement_tool, builder_fixer_agent]

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)
    # Set up model with structured output
    model_with_structured_output = model.with_structured_output(FunctionClassifyResponse)

    # Create ToolNode
    tool_node = ToolNode(tools)

    # Create a wrapper for tool_node to add logging
    async def tools_with_logging(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "tools"
        function_name = state.get("function_name", "unknown")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        result = await tool_node.ainvoke(state)
        
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(agent_name, node_name, updated_state, function_name)
        
        return result

    def _get_last_verified_replace_code(messages):
        """从对话中解析最后一次 VerifyReplacement 且 pass=true 的 replace_code。"""
        id_to_call = {}
        for msg in messages:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    tid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", None)
                    name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
                    args = tc.get("args") if isinstance(tc, dict) else getattr(tc, "args", {}) or {}
                    if tid:
                        id_to_call[tid] = (name, args)
        last_verified_code = None
        for msg in messages:
            if getattr(msg, "tool_call_id", None) and getattr(msg, "content", None):
                name, args = id_to_call.get(msg.tool_call_id, (None, {}))
                if name == "VerifyReplacement":
                    try:
                        content = msg.content
                        data = json.loads(content) if isinstance(content, str) else content
                        if data.get("pass") is True:
                            last_verified_code = (args or {}).get("replace_code") or last_verified_code
                    except Exception:
                        pass
        return last_verified_code

    def _has_fix_function_build_errors_success(messages, function_name: str) -> bool:
        """True 若对话中存在针对当前 function_name 的 FixFunctionBuildErrors 且返回 success。"""
        id_to_call = {}
        for msg in messages:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    tid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", None)
                    name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
                    args = tc.get("args") if isinstance(tc, dict) else getattr(tc, "args", {}) or {}
                    if tid:
                        id_to_call[tid] = (name, args)
        for msg in messages:
            if getattr(msg, "tool_call_id", None) and getattr(msg, "content", None):
                name, args = id_to_call.get(msg.tool_call_id, (None, {}))
                if name == "FixFunctionBuildErrors":
                    try:
                        fn = (args or {}).get("function_name") or ""
                        if fn != function_name:
                            continue
                        content = msg.content
                        data = json.loads(content) if isinstance(content, str) else content
                        if data.get("success") is True:
                            return True
                    except Exception:
                        pass
        return False

    # Define the function that responds to the user
    def respond(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "respond"
        function_name = state.get("function_name", "unknown")
        
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(agent_name, node_name, state, function_name)
        
        # Use the imported summary prompt to ensure LLM only summarizes and doesn't call tools
        response = model_with_structured_output.invoke(
            state["messages"] + [HumanMessage(content=SUMMARY_PROMPT)]
        )
        # 替换采纳优先级：VerifyReplacement pass > FixFunctionBuildErrors 成功 > 否则清空未验证替换
        verified_code = _get_last_verified_replace_code(state["messages"])
        current_fn = state.get("function_name", "")
        fixer_success = _has_fix_function_build_errors_success(state["messages"], current_fn)

        if verified_code is not None and verified_code.strip():
            # 有 VerifyReplacement pass=true，直接采用
            response = response.model_copy(update={"function_replacement": verified_code})
        elif fixer_success:
            # FixFunctionBuildErrors 成功：直接采纳 fixer 已落盘的替换，无需再 VerifyReplacement
            from core.data_manager import data_manager
            ru = data_manager.get_replacement_updates().get(current_fn)
            if ru and getattr(ru, "replacement_code", "").strip():
                response = response.model_copy(update={"function_replacement": ru.replacement_code, "has_replacement": True})
        else:
            # 既无 VerifyReplacement 通过，又无 FixFunctionBuildErrors 成功：有替换内容则清空（未验证不采纳）
            if getattr(response, "has_replacement", False) and (getattr(response, "function_replacement") or "").strip():
                response = response.model_copy(update={"has_replacement": False, "function_replacement": ""})
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
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        else:
            return "respond"

    # Define call_model function
    async def call_model(state: AgentState):
        agent_name = "analyzer_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "unknown")
        
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
    _graph_db_path = db_path
    return _graph

async def function_classify(func_name : str, overwrite: bool = False) -> FunctionClassifyResponse:
    # 检查函数是否已经分析过
    if check_analyzed(func_name) and not overwrite:
        # print(f"Function {func_name} has been analyzed, skip.")
        return function_classify_from_log(func_name)
    # 构建graph
    graph = await build_graph()
    # llm 调用
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompting_en},
            {"role": "user", "content": f"Classify the function : {func_name}"}
        ],
        "function_name": func_name
        # 移除自定义计数器，直接使用LangGraph的错误处理
    }
    
    try:
        result = await graph.ainvoke(initial_state, config={"recursion_limit": 50})  # 添加recursion_limit配置
        # log ai memory
        if globs.ai_log_enable:
            dump_message_json_log("function_classify", result)
        final_response = result["final_response"]
        # Rubric check: if classifier produced a replacement, validate it before use
        if getattr(final_response, "has_replacement", False) and getattr(final_response, "function_replacement", "").strip():
            original_code = get_function_source(globs.db_path, func_name) if globs.db_path else None
            check_result = check_replacement_rubric(
                func_name,
                final_response.function_replacement,
                original_code=original_code,
            )
            if not check_result["pass"]:
                # Attach failure reason to response for logging / retry
                d = final_response.model_dump()
                d["replacement_check_reason"] = check_result["reason"]
                final_response = FunctionClassifyResponse(**d)
        return final_response
    except Exception as e:
        from langgraph.errors import GraphRecursionError
        if isinstance(e, GraphRecursionError):
            # 捕获LangGraph的递归错误，触发failcheck分析
            from utils.failcheck import analyze_failed_conversation
            analyze_failed_conversation(
                initial_state["messages"], 
                "analyzer_agent", 
                50,
                db_path=globs.db_path
            )  # 50次agent调用
        else:
            # 其他错误直接抛出
            raise

def check_analyzed(func_name: str) -> bool:
    """
    检查函数是否已经分析过
    """
    return check_analyzed_json_log("function_classify", func_name)

def get_analyzed(func_name: str) -> str:
    """
    获取函数分析日志
    """
    return get_analyzed_json_log("function_classify", func_name)

def function_classify_from_log(func_name: str) -> FunctionClassifyResponse:
    """
    从JSON日志中获取函数分析结果
    """
    infos = get_analyzed(func_name)
    json_data = json.loads(infos)
    return FunctionClassifyResponse(**json_data["final_response"])

async def analyze_functions(function_list):
    mmio_info_list = {}
    tasks = []
    for func_name in function_list:
        tasks.append(function_classify(func_name))
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for func_name, result in zip(function_list, results):
        if isinstance(result, Exception):
            print(f"Error analyzing function {func_name}: {result}")
            continue
        if result is None:
            print(f"Warning: function_classify returned None for {func_name}, skip.")
            continue
        if not isinstance(result, FunctionClassifyResponse):
            print(f"Warning: function_classify returned non-Response for {func_name}: type={type(result)}, skip.")
            continue
        mmio_info_list[func_name] = result
    
    return mmio_info_list

@tool(
    "Analyzer",
    description="Sub Agent `Analyzer`, analyze the driver source code and classify the functions into MMIO and non-MMIO functions"
)
async def analyzer_agent(func_name : str) -> FunctionClassifyResponse:
    return await function_classify(func_name, False)

async def main():
    # Test the graph
    classify_response = await function_classify("HAL_ETH_ReadData", True)
    print(f"Classify response: {classify_response.model_dump_json()}")

# 运行主函数
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())