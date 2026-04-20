# 动态测试反馈闭环模块：从 emulator_runner_agent 开始的多智能体架构与协同工作流

**日期**: 2026-03-19  
**适用范围**: LCMHalMCP 主工作流 `run` 命令、所有配置了 `lcmhal_config.yml` 的 testcase  
**证据范围**: 仓库当前实现（main 分支 / test/server_test 分支）

---

## 1. 背景与目标

### 1.1 问题定义

在 HAL 驱动函数替换场景中，替换后的固件需通过**动态仿真**验证正确性。若仿真失败（死循环、UNMAPPED 访问、异常等），需要根据执行日志诊断问题、修改替换代码、重新编译并回归验证，直到稳定或达到终止条件。

### 1.2 目标

实现一个**动态测试反馈闭环**（dynamic test feedback loop），闭环包括：

1. **运行**：执行固件仿真
2. **采集输出/诊断**：收集 stdout/stderr、函数调用栈、MMIO 调用日志
3. **生成改动/修复建议**：由 Fixer 分析并生成 `ReplacementUpdate`
4. **回归验证**：重新编译并再次仿真
5. **终止条件**：`success: true` 或达到最大迭代/递归限制

---

## 2. 整体架构

### 2.1 入口与编排

```
main.py (run 命令)
    └── run_workflow()
            ├── build_proj_dbgen, register_db, init_builder
            ├── build_project()  [首次构建，失败则 Builder Agent 递归修复]
            ├── generate_emulator_configs()
            ├── run_emulator()   ← agents/emulator_runner_agent.run_emulator()
            └── fault 恢复循环 (max 3 轮): get_fault_function → analyze_functions → replace → build → emulate
```

**证据**: `main.py:99-164`（`run_workflow` 函数）

### 2.2 多智能体拓扑

```
                    ┌─────────────────────────────────────────────────────────┐
                    │              emulator_runner_agent                      │
                    │  (LangGraph: agent ↔ tools 循环，recursion_limit=50)    │
                    └─────────────────────────┬─────────────────────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         │                                    │                                    │
         ▼                                    ▼                                    ▼
┌─────────────────┐              ┌─────────────────────┐              ┌─────────────────────┐
│ MCP Emulator    │              │ fixer_agent (tool)   │              │ builder_agent (tool) │
│ EmulateProject  │              │ 子图: Fixer         │              │ 子图: Builder        │
│ GetMMIOFuncInfo │              │ 输出: ReplacementUpdate│           │ 输出: BuildOutput    │
│ GetFuncCallsInfo│              │ 内部: update_func_replacement│      │ 内部: replace_funcs │
└─────────────────┘              └─────────────────────┘              │       build_project │
                                                                       └─────────────────────┘
```

**证据**: `agents/emulator_runner_agent.py:76-78`（tools 绑定）、`agents/emulator_runner_agent.py:168-179`（图结构）

---

## 3. Agent 分工与职责

### 3.1 emulator_runner_agent 主控 Agent

| 属性 | 说明 |
|------|------|
| **入口** | `agents/emulator_runner_agent.run_emulator()` |
| **职责** | 驱动「仿真 → 诊断 → 修复 → 构建 → 回归」闭环，直至 `success: true` 或达到 recursion_limit |
| **输入** | `initial_state`: `messages`（system + user prompt）、`function_name: "run_emulator"` |
| **输出** | `EmulateResult`（std_err, std_out, exit_code, success, reason） |
| **工具** | EmulateProject, GetMMIOFunctionEmulateInfo, GetFunctionCallsEmulateInfo, Fixer, Builder |

**证据**: `agents/emulator_runner_agent.py:185-201`（`run_emulator`）、`models/emulate_results/emulate_result.py`（EmulateResult 定义）

### 3.2 Fixer 子 Agent（function_fixer_agent）

| 属性 | 说明 |
|------|------|
| **触发** | emulator_runner_agent 在 `success: false` 时调用 Fixer 工具 |
| **职责** | 分析仿真日志，定位问题函数，生成替换代码并调用 `update_function_replacement` |
| **输入** | 通过 messages 传递：Emulator 的 stdout/stderr、MMIO/函数调用日志 |
| **输出** | `ReplacementUpdate`（function_name, replacement_code, reason） |
| **工具** | mmio_function_emulate_info, function_calls_emulate_info, get_replace_func_details_by_file, update_function_replacement, get_function_analysis_and_replacement |

**证据**: `agents/fixer_agent.py:267-273`（fixer_agent 工具定义）、`agents/fixer_agent.py:104-114`（工具列表）

### 3.3 Builder 子 Agent（builder_agent）

| 属性 | 说明 |
|------|------|
| **触发** | emulator_runner_agent 在 Fixer 返回后调用 Builder 工具 |
| **职责** | 执行 `replace_funcs` + `build_project`，编译固件 |
| **输入** | 无显式参数；`replace_funcs` 从 `data_manager.replacement_updates` 读取 Fixer 写入的替换 |
| **输出** | `BuildOutput`（exit_code, stderr 等） |
| **工具** | build_project, get_replace_func_details_by_file, update_function_replacement, get_function_analysis_and_replacement, builder_fixer_agent |

**证据**: `agents/builder_agent.py:241-245`（builder_agent 工具定义）、`tools/builder/core.py:25-41`（replace_funcs 使用 replacement_updates）

### 3.4 MCP Emulator 工具（非 Agent）

| 工具名 | 说明 | 返回 |
|--------|------|------|
| EmulateProject | 运行 fuzzemu 仿真 | `{std_out, std_err, exit_code, success, has_exceptional_loop}` |
| GetMMIOFunctionEmulateInfo | 读取 lcmhal.txt | MMIO 函数调用信息 |
| GetFunctionCallsEmulateInfo | 读取 function.txt（压缩循环） | 函数调用栈信息 |

**证据**: `tools/emulator/tool.py`、`tools/emulator/core.py:10-49`（emulate_proj 实现）

---

## 4. 闭环状态机与协同流程

### 4.1 Sequence Diagram 风格流程

```
User/main.py          emulator_runner_agent        Emulator(MCP)      Fixer           Builder
     |                         |                        |              |                |
     |-- run_workflow() ------->|                        |              |                |
     |                         |-- EmulateProject() ---->|              |                |
     |                         |<-- {success:false} -----|              |                |
     |                         |                        |              |                |
     |                         |-- Fixer() -------------|------------->|                |
     |                         |                        |              |-- update_func  |
     |                         |                        |              |   _replacement |
     |                         |<-- ReplacementUpdate --|--------------|                |
     |                         |                        |              |                |
     |                         |-- Builder() -----------|--------------|-------------->|
     |                         |                        |              |   replace_funcs|
     |                         |                        |              |   build_project|
     |                         |<-- BuildOutput --------|--------------|----------------|
     |                         |                        |              |                |
     |                         |-- EmulateProject() ---->|              |                |
     |                         |<-- {success:true} ------|              |                |
     |                         |                        |              |                |
     |                         |-- respond() -> EmulateResult          |                |
     |<-- emulate_output ------|                        |              |                |
```

### 4.2 伪码：emulator_runner_agent 主循环

```python
# 伪码：emulator_runner_agent 内部逻辑（由 LangGraph 实现）
# 证据：agents/emulator_runner_agent.py:168-179, prompts/project_emulator.py:17-51

async def run_emulator():
    graph = await build_graph()  # StateGraph: agent <-> tools <-> respond
    state = {
        "messages": [system_prompt, user_prompt],
        "function_name": "run_emulator"
    }
    result = await graph.ainvoke(state, config={"recursion_limit": 50})
    return result["final_response"]  # EmulateResult

# LangGraph 节点流转（由 should_continue 控制）:
# START -> agent(call_model) -> [tool_calls?] -> tools(ToolNode) -> agent -> ... -> respond -> END
# 当 last_message 无 tool_calls 时 -> respond -> 生成 EmulateResult
```

### 4.3 伪码：主工作流中的 fault 恢复循环

```python
# 证据：main.py:127-164

emulate_output = await run_emulator()

for _ in range(max_emulate_fault_rounds):  # max_emulate_fault_rounds = 3
    if emulate_output.success:
        break
    fault_func = get_fault_function_from_emulate_output()  # 解析 UNMAPPED/fault PC
    if not fault_func or fault_func in mmio_info_list:
        break
    # 对新发现的 fault 函数做一次 analyze + 替换 + 构建 + 仿真
    result_map = await analyze_functions([fault_func])
    if result_map and fault_func in result_map and has_replacement:
        data_manager.mmio_info_list[fault_func] = result_map[fault_func]
        replace_funcs()
        build_output = core_build_project()
        if build_output["exit_code"] == 0:
            generate_emulator_configs()
            emulate_output = await run_emulator()
```

### 4.4 关键数据在 Agent 之间的传递

| 数据 | 来源 | 去向 | 传递方式 |
|------|------|------|----------|
| Emulator 输出 | EmulateProject | emulator_runner_agent messages | Tool 返回 → messages |
| ReplacementUpdate | Fixer | data_manager.replacement_updates | Fixer 内部调用 update_function_replacement |
| 替换代码 | data_manager.replacement_updates | Builder.replace_funcs | 全局 data_manager 单例 |
| BuildOutput | Builder | emulator_runner_agent messages | Tool 返回 → messages |
| EmulateResult | respond 节点 | run_workflow 返回值 | model_with_structured_output(SUMMARY_PROMPT) |

**证据**: `core/data_manager.py:49-59`（update_function_replacement）、`tools/builder/core.py:25-41`（replace_funcs 读取 replacement_updates）

---

## 5. 终止条件与回归策略

### 5.1 成功终止

- **条件**: Emulator 返回 `success: true`（即 `exit_code == 0` 且无 `exceptional loop`）
- **证据**: `tools/emulator/core.py:40-41`（success 判断）、`prompts/project_emulator.py:33`（"If success: true, stop"）

### 5.2 失败终止

| 类型 | 条件 | 行为 |
|------|------|------|
| GraphRecursionError | LangGraph 达到 recursion_limit=50 | 调用 `analyze_failed_conversation`，写 failcheck 报告，`sys.exit(1)` |
| fault 恢复耗尽 | max_emulate_fault_rounds=3 且仍失败 | 退出 fault 循环，不再重试 |
| 无 fault 函数 | UNMAPPED/fault PC 无法解析为函数名 | 跳过 fault 恢复 |

**证据**: `agents/emulator_runner_agent.py:203-215`（GraphRecursionError 处理）、`main.py:130-137`（fault 循环条件）

### 5.3 回归策略

- **主闭环**: Emulator → Fixer → Builder → Emulator（由 LLM 按 prompt 驱动）
- **Prompt 约束**: "One Fixer call per failure iteration"、"Always call Builder after Fixer"
- **证据**: `prompts/project_emulator.py:36-48`

---

## 6. 实现追溯：关键证据代码位置

| 模块/功能 | 文件路径 | 行号/关键字 |
|-----------|----------|-------------|
| 主工作流入口 | main.py | 99-164 (run_workflow) |
| emulator_runner_agent 入口 | agents/emulator_runner_agent.py | 185-201 (run_emulator) |
| emulator_runner_agent 图构建 | agents/emulator_runner_agent.py | 168-183 (StateGraph) |
| emulator_runner_agent 系统提示 | prompts/project_emulator.py | 17-51 (system_prompting_en) |
| EmulateResult 模型 | models/emulate_results/emulate_result.py | 4-12 |
| Fixer 工具定义 | agents/fixer_agent.py | 267-273 (fixer_agent) |
| Builder 工具定义 | agents/builder_agent.py | 241-245 (builder_agent) |
| 仿真执行 | tools/emulator/emulate_runner.py | 48-93 (run_emulator) |
| 仿真结果封装 | tools/emulator/core.py | 10-49 (emulate_proj) |
| fault 函数解析 | tools/emulator/core.py | 103-157 (get_fault_function_from_emulate_output) |
| 替换更新 | core/data_manager.py | 49-59 (update_function_replacement) |
| 替换应用 | tools/builder/core.py | 25-41 (replace_funcs) |
| FailCheck | utils/failcheck.py | 109-215 (analyze_failed_conversation) |
| MCP Emulator 工具 | tools/emulator/mcp_server.py | 18-30 |
| Summary 提示 | prompts/summary_prompt.py | 1-28 (summary_prompt_en) |

---

## 7. 实现缺口与待补齐

### 7.1 prompts/emulator_multiagent.py 未接入

- **现状**: `prompts/emulator_multiagent.py` 定义了 `supervisor_prompt`、`project_builder_prompt`、`function_fixer_prompt`，描述了一个「supervisor 协调 project_builder_agent、function_fixer_agent、emulator_tool」的多智能体架构。
- **实际**: `emulator_runner_agent` 使用的是 `prompts/project_emulator.py`，且将 Fixer、Builder 作为**工具**绑定，由单一 LLM 驱动，而非独立的 supervisor 编排。
- **建议**: 若需实现「supervisor 显式编排」架构，可新增一个 supervisor_agent，将 `emulator_multiagent.supervisor_prompt` 作为其 system prompt，并让 supervisor 调用 emulator_runner_agent / builder_agent / fixer_agent。当前实现为「单主控 + 子 Agent 工具」模式。

### 7.2 Fixer 工具中 emulate_proj 未暴露

- **现状**: `agents/fixer_agent.py` 的工具列表包含 `mmio_function_emulate_info`、`function_calls_emulate_info`，但**不包含** `emulate_proj`（注释掉）。
- **影响**: Fixer 只能读取已有仿真输出，不能主动触发仿真。仿真由 emulator_runner_agent 通过 MCP Emulator 的 EmulateProject 执行。
- **结论**: 与当前设计一致（仿真由主控 Agent 发起），非缺口。

### 7.3 显式 Verifier Agent 缺失

- **现状**: 无独立的「Verifier」Agent。验证逻辑为：Emulator 返回的 `success` 字段 + `has_exceptional_loop`。
- **建议**: 若需更细粒度的验证（如断言、覆盖率），可新增 Verifier Agent，接收 Emulator 输出并返回结构化验证报告。

---

## 8. 附录：Agent 输入/输出契约摘要

### EmulateResult（emulator_runner_agent 输出）

```python
# 来源：models/emulate_results/emulate_result.py
class EmulateResult(BaseModel):
    std_err: str
    std_out: str
    exit_code: int
    success: bool
    reason: Literal["success", "failure"]
```

### ReplacementUpdate（Fixer 输出）

```python
# 来源：models/analyze_results/function_analyze.py
class ReplacementUpdate(BaseModel):
    function_name: str
    replacement_code: str
    reason: str
```

### emulate_proj 返回（Emulator 工具）

```python
# 来源：tools/emulator/core.py:42-48
{
    "std_out": bytes/str,
    "std_err": bytes/str,
    "exit_code": int,
    "success": bool,           # exit_code==0 and not has_loop
    "has_exceptional_loop": bool
}
```
