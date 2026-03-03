"""BuilderFixer sub-agent: fix a single function given function name and build error snippet. Exposed as a tool to Builder."""

from langchain_core.tools import tool
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from config.model_singleton import get_model
from models.build_results.builder_fixer_result import BuilderFixerResult
from prompts.builder_fixer import system_prompt_en
from prompts.summary_prompt import builder_fixer_summary_prompt_en as SUMMARY_PROMPT
from utils.ai_log_manager import ai_log_manager
import config.globs as globs
from tools.builder.core import init_builder, build_project as core_build_project
from tools.builder.tool import (
    build_project,
    get_replace_func_details_by_file,
    update_function_replacement,
    get_function_analysis_and_replacement,
)

model = get_model()

BUILDER_FIXER_RECURSION_LIMIT = 20


class AgentState(MessagesState):
    final_response: BuilderFixerResult
    function_name: str


_graph = None


async def build_graph():
    global _graph
    if _graph is not None:
        return _graph

    await init_builder()

    tools = [
        build_project,
        get_replace_func_details_by_file,
        update_function_replacement,
        get_function_analysis_and_replacement,
    ]
    model_with_tools = model.bind_tools(tools)
    model_with_structured_output = model.with_structured_output(
        BuilderFixerResult, method="json_mode"
    )
    tool_node = ToolNode(tools)

    async def tools_with_logging(state: AgentState):
        agent_name = "builder_fixer_agent"
        node_name = "tools"
        function_name = state.get("function_name", "builder_fix")
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(
                agent_name, node_name, state, function_name
            )
        result = await tool_node.ainvoke(state)
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(
                agent_name, node_name, updated_state, function_name
            )
        return result

    def respond(state: AgentState):
        agent_name = "builder_fixer_agent"
        node_name = "respond"
        function_name = state.get("function_name", "builder_fix")
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(
                agent_name, node_name, state, function_name
            )
        max_retries = 3
        response = None
        for _ in range(max_retries):
            try:
                response = model_with_structured_output.invoke(
                    state["messages"] + [HumanMessage(content=SUMMARY_PROMPT)]
                )
                break
            except Exception as e:
                continue
        if response is None:
            response = BuilderFixerResult(
                success=False,
                reason="Failed to generate structured response after retries",
                modifications="",
            )
        result = {"final_response": response}
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(
                agent_name, node_name, updated_state, function_name
            )
        return result

    def should_continue(state: AgentState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return "respond"

    async def call_model(state: AgentState):
        agent_name = "builder_fixer_agent"
        node_name = "call_model"
        function_name = state.get("function_name", "builder_fix")
        if globs.ai_log_enable:
            ai_log_manager.log_langgraph_node_start(
                agent_name, node_name, state, function_name
            )
        messages = state["messages"]
        response = await model_with_tools.ainvoke(messages)
        result = {"messages": [response]}
        if globs.ai_log_enable:
            updated_state = {**state, **result}
            ai_log_manager.log_langgraph_node_end(
                agent_name, node_name, updated_state, function_name
            )
        return result

    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tools_with_logging)
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", should_continue)
    builder.add_edge("tools", "agent")
    builder.add_edge("respond", END)
    _graph = builder.compile()
    return _graph


async def run_builder_fix(
    function_name: str, error_info: str, replace_code: str | None = None
) -> BuilderFixerResult:
    graph = await build_graph()
    user_content = (
        f"Fix the following function so that the given errors are resolved.\n"
        f"function_name: {function_name}\n"
        f"error_info:\n{error_info}\n\n"
    )
    if replace_code and replace_code.strip():
        user_content += (
            "Current replacement code (failed verification; fix this code):\n"
            "```c\n" + replace_code.strip() + "\n```\n\n"
        )
    user_content += (
        "Use tools to get context (GetFunctionAnalysisAndReplacement or GetReplaceFuncDetailsByFile) if needed, "
        "then UpdateFunctionReplacement with the fixed code, then BuildProject. "
        "If build succeeds or the given error_info no longer appears in stderr, return success with reason; otherwise return failure with reason."
    )
    initial_state = {
        "messages": [
            {"role": "system", "content": system_prompt_en},
            {"role": "user", "content": user_content},
        ],
        "function_name": function_name,
    }
    result = await graph.ainvoke(
        initial_state, config={"recursion_limit": BUILDER_FIXER_RECURSION_LIMIT}
    )
    return result["final_response"]


@tool(
    "FixFunctionBuildErrors",
    description="Fix build errors for a single function: given function_name and the stderr/error snippet (error_info). "
    "Optionally pass replace_code (the current replacement that failed verification) so the fixer has full context. "
    "Returns success/failure, reason, and modifications. Use when VerifyReplacement returns pass=false with build_stderr.",
)
async def builder_fixer_agent(
    function_name: str, error_info: str, replace_code: str | None = None
) -> dict:
    """Invoke BuilderFixer to fix one function. Returns dict with success, reason, modifications."""
    result = await run_builder_fix(function_name, error_info, replace_code=replace_code)
    # Optional programmatic check: if agent said success but error_info still in stderr, override to failure
    if result.success and error_info and error_info.strip():
        build_out = core_build_project()
        stderr = build_out.get("std_err") or ""
        if error_info.strip() in stderr:
            result = BuilderFixerResult(
                success=False,
                reason=result.reason + "; Programmatic check: error still present in stderr.",
                modifications=result.modifications,
            )
    return result.model_dump()
