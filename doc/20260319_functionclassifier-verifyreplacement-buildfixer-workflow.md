# 从 FunctionClassifier 到 VerifyReplacement / BuildFixer：智能体协作工作流（LCMHalMCP 当前实现）

日期：2026-03-19  
适用范围：所有调用 `agents/analyzer_agent.py` 中 `function_classify()` 的替换分类场景（Classifier Agent 的 LangGraph 工具循环、`VerifyReplacement` 校验、`FixFunctionBuildErrors` 委托子修复）。  
证据范围：本文件所有关键结论均来自仓库代码/提示词，见文末“证据索引”。

---

## 1. 参与组件与职责边界

1. **Classifier Agent（LangGraph）**：`agents/analyzer_agent.py` 的 `function_classify()` 构建 LangGraph，并通过 `should_continue()` + `ToolNode` 驱动工具调用循环。  
   - 证据：`agents/analyzer_agent.py` 中 `build_graph()` 定义了图节点 `agent/tools/respond`，并把 `VerifyReplacement` 与 `builder_fixer_agent` 加入工具列表后绑定到模型（`tools = tools + [verify_replacement_tool, builder_fixer_agent]`）。来源：`agents/analyzer_agent.py:39-80`
   - 证据：控制流由 `should_continue()` 决定：只要最后一条消息包含 `tool_calls` 就回到 `tools` 节点，否则进入 `respond`。来源：`agents/analyzer_agent.py:198-205`

2. **VerifyReplacement（仅验证，不落盘）**：`tools/builder/core.py` 的 `verify_replacement(func_name, replace_code)`。  
   - 证据：`verify_replacement` docstring 明确“仅验证替换代码（Rubric + 可选编译），不落盘”。来源：`tools/builder/core.py:316-337`
   - 证据：`verify_replacement` 先调用 `check_replacement_rubric()`，不通过直接返回 `{"pass": False, ...}`。来源：`tools/builder/core.py:322-326`

3. **rubric check（LLM rubric + fail closed）**：`utils/replacement_rubric.py` 的 `check_replacement_rubric()`。  
   - 证据：`check_replacement_rubric` 异常捕获后“fail closed”，返回 `pass: False`，理由提示不会接受以避免错误代码持久化。来源：`utils/replacement_rubric.py:82-88`

4. **编译验证（临时应用 + 恢复）**：`tools/builder/core.py` 的 `_compile_verify_single_replacement()`。  
   - 证据：临时应用替换：`applied = function_replace(func_info, replace_code)`。来源：`tools/builder/core.py:286-292`
   - 证据：构建期间“无论成功失败都恢复原始代码”：`finally: function_recover(func_info)`。来源：`tools/builder/core.py:301-304`

5. **FixFunctionBuildErrors（委托子修复工具）**：`agents/builder_fixer_agent.py` 通过 `@tool("FixFunctionBuildErrors", ...)` 暴露。  
   - 证据：工具包装：`@tool("FixFunctionBuildErrors", ...)`，并声明可传入 `replace_code` 作为失败上下文。来源：`agents/builder_fixer_agent.py:170-175`
   - 证据：`run_builder_fix()` 构造用户输入时包含 `function_name`、`error_info`，并在 `replace_code` 存在时追加当前失败 replacement。来源：`agents/builder_fixer_agent.py:138-151`
   - 证据：成功标准在子 agent 提示词中写明“build succeeds 或 error_info 不再出现在 stderr”。来源：`agents/builder_fixer_agent.py:152-156`
   - 证据：额外的程序化校验：若 agent 返回 `success=True` 但 `error_info` 仍出现在 `stderr` 中，会把结果改为 `success=False`。来源：`agents/builder_fixer_agent.py:181-190`

6. **最末采纳优先级（关键）**：`agents/analyzer_agent.py` 的 `respond()` 使用：
   - `_get_last_verified_replace_code()`：从对话中提取最后一次 `VerifyReplacement` 且 `pass=true` 的 `replace_code`。来源：`agents/analyzer_agent.py:99-122`
   - `_has_fix_function_build_errors_success()`：判断对话中是否存在针对当前 `function_name` 且 `FixFunctionBuildErrors` 返回 `success=true` 的调用。来源：`agents/analyzer_agent.py:124-149`
   - `respond()` 采纳逻辑：`VerifyReplacement pass > FixFunctionBuildErrors success > 清空未验证 replacement`。来源：`agents/analyzer_agent.py:164-183`

---

## 2. 数据流/控制流总览（从 LangGraph 开始）

### 2.1 控制流：LangGraph 工具循环如何驱动 `VerifyReplacement` / `FixFunctionBuildErrors`

`function_classify()` 创建 LangGraph，其中：
- `agent` 节点：`call_model()` 让模型在 `state["messages"]` 上调用带工具的模型（`model_with_tools.ainvoke(messages)`）。来源：`agents/analyzer_agent.py:206-224`
- `tools` 节点：`tools_with_logging()` 用 `ToolNode(tools)` 执行 LLM 发出的 `tool_calls`。来源：`agents/analyzer_agent.py:79-97`
- `respond` 节点：当模型不再产生 `tool_calls` 时，进入 `respond()` 做最终采纳。来源：`agents/analyzer_agent.py:198-205`

并且 `build_graph()` 在构图时将 `VerifyReplacement` 与 `builder_fixer_agent` 加入 `tools`：  
`tools = tools + [verify_replacement_tool, builder_fixer_agent]`。来源：`agents/analyzer_agent.py:68-73`

因此，**Classifier Agent 在对话中“触发工具”**的机制是：
1. LLM 依据 `prompts/function_classifier.py` 的要求生成 replacement：当 `function_type` 为 `RECV/IRQ/INIT/LOOP` 时生成完整 replacement code（`has_replacement=true`），当 `function_type` 为 `CORE` 或其他 `RETURNOK/SKIP/NODRIVER` 时不生成 replacement（`has_replacement=false`）。来源：`prompts/function_classifier.py:274-303`
2. 在“必须在结束前验证”的约束下，LLM 会在消息中发出名为 `VerifyReplacement` 的 tool call；
3. `should_continue()` 看到最后一条消息有 `tool_calls`，就回到 `tools` 节点执行该工具；
4. 工具执行后会产生 tool result message，图再回到 `agent` 节点继续对话，直到最终不再产生 tool calls，进入 `respond()`。

### 2.2 数据流：`VerifyReplacement(func_name, replace_code)` 到 `FixFunctionBuildErrors(...)`

#### 2.2.1 `VerifyReplacement` 调用前置条件（来自提示词）

`prompts/function_classifier.py` 明确要求：  
“若你的分类包括 replacement code，**在结束前必须调用** VerifyReplacement(func_name, replace_code)”。并给出工具失败时的处理逻辑。  
- 证据：`prompts/function_classifier.py`：`VerifyReplacement(...)` 与结束前校验要求。来源：`prompts/function_classifier.py:47-51`

#### 2.2.2 `VerifyReplacement` 失败时如何委托 FixFunctionBuildErrors

同一段提示词要求当 `VerifyReplacement` 返回 `pass: false` 且提供 `build_stderr` 时：  
- 应调用 `FixFunctionBuildErrors(function_name, error_info=build_stderr, replace_code=replace_code)` 进行修复委托；  
- 若修复成功（`FixFunctionBuildErrors` 返回 `success: true`），把函数视为已验证，并输出最终 `has_replacement: true`。  
- 证据：`prompts/function_classifier.py` 末尾“Verification before final output”逻辑。来源：`prompts/function_classifier.py:51-51`

因此在数据流上：
- `replace_code` 从 classifier 生成后进入 `VerifyReplacement(func_name, replace_code)`；
- `VerifyReplacement` 在失败时（当开启编译验证时）可回传 `build_stderr`；
- classifier 将该 `build_stderr` 作为 `error_info` 传给 `FixFunctionBuildErrors(...)`，并可把当前失败的 `replace_code` 也一并传给 fixer（提示词里明确该参数可选）。来源：`prompts/function_classifier.py:49-49`

---

## 3. VerifyReplacement 的内部实现：rubric + 可选编译（临时落盘 + 恢复）

### 3.1 rubric check：`check_replacement_rubric` 的 fail closed 行为

`tools/builder/core.py` 的 `verify_replacement()` 会先调用 `check_replacement_rubric(func_name, replace_code, original_code=...)`。  
- 证据：`verify_replacement` 调用 rubric。来源：`tools/builder/core.py:322-324`
- 证据：rubric 通过时 `pass: True`，失败时由 `check_replacement_rubric` 返回 reason。来源：`tools/builder/core.py:324-326`

在 `utils/replacement_rubric.py` 中，rubric checker 发生 LLM/network 异常时采用 fail-closed 策略：  
捕获异常后直接返回 `{"pass": False, "reason": "...not accepted to avoid persisting invalid code."}`。  
- 证据：`utils/replacement_rubric.py` 异常处理块。来源：`utils/replacement_rubric.py:82-88`

这确保了：**VerifyReplacement 在 rubric 阶段失败时会拒绝“持久化”的 replacement**（即便后续编译验证未发生，也不会让坏代码通过）。来源：`tools/builder/core.py:324-326`

### 3.2 编译验证：`_compile_verify_single_replacement` 的临时应用与恢复机制

当 `getattr(globs, "enable_compile_verify", False)` 为真时，`verify_replacement()` 会调用 `_compile_verify_single_replacement(func_name, replace_code)`。  
 - 证据：`enable_compile_verify` 分支。来源：`tools/builder/core.py:327-336`

`_compile_verify_single_replacement()` 的关键机制是：
1. **临时应用**：对源文件临时应用替换（调用 `function_replace(func_info, replace_code)`）。来源：`tools/builder/core.py:286-292`
2. **构建验证**：在临时状态下清理并构建工程：`clear_proj(globs.script_path)` + `build_proj(globs.script_path)`。来源：`tools/builder/core.py:294-301`
3. **无污染恢复**：用 `finally` 块恢复原始代码：`function_recover(func_info)`。来源：`tools/builder/core.py:301-304`

若编译失败，它返回：  
`{"ok": False, "reason": "Compile verification failed for replacement.", "build_stderr": build_output.std_err}`。  
- 证据：编译失败返回结构。来源：`tools/builder/core.py:305-311`

最终 `verify_replacement()` 将其转换为 `pass: False` 且携带 `build_stderr` 的返回结果。来源：`tools/builder/core.py:328-335`

---

## 4. 如果 VerifyReplacement 失败：FixFunctionBuildErrors 子修复与“成功落盘”

当 classifier 根据 `prompts/function_classifier.py` 规则决定调用 `FixFunctionBuildErrors(function_name, error_info, replace_code?)` 时，LangGraph 的 `tools` 节点会执行该 tool（来自 `agents/builder_fixer_agent.py` 的 `@tool` 包装）。

### 4.1 工具包装与输入构造（run_builder_fix）

`agents/builder_fixer_agent.py` 对外暴露的工具为 `FixFunctionBuildErrors`：  
- 证据：`@tool("FixFunctionBuildErrors", ...)` 描述与入参 `function_name`, `error_info`, `replace_code`（可选）。来源：`agents/builder_fixer_agent.py:170-175`

具体 user prompt 由 `run_builder_fix(function_name, error_info, replace_code)` 构造：  
- 证据：构造内容包含 `function_name` + `error_info`（build errors snippet）。来源：`agents/builder_fixer_agent.py:142-146`
- 证据：若传入 `replace_code`，会追加到提示词：“Current replacement code (failed verification; fix this code): ...”。来源：`agents/builder_fixer_agent.py:147-151`

并要求 fixer：  
“使用工具获取上下文（GetFunctionAnalysisAndReplacement/ GetReplaceFuncDetailsByFile）→ 用 UpdateFunctionReplacement 写入固定代码 → BuildProject”。  
- 证据：run_builder_fix prompt 中描述的流程。来源：`agents/builder_fixer_agent.py:152-156`

### 4.2 成功标准：build 成功或错误消失（含程序化二次校验）

fixer 的 success criterion 写在提示词中：  
“If build succeeds or the given error_info no longer appears in stderr, return success …”。  
- 证据：`agents/builder_fixer_agent.py` prompt。来源：`agents/builder_fixer_agent.py:154-156`

此外还有程序化校验：  
若 fixer 返回 `success=True`，但 `error_info` 仍存在于 `core_build_project()` 的 `stderr` 中，则强制把结果改为失败。  
- 证据：程序化检查。来源：`agents/builder_fixer_agent.py:181-190`

这为上层的采纳提供了“落盘已成功修复”的可判定依据。

### 4.3 落盘前的最终校验：update_function_replacement（rubric + 可选编译验证）

`FixFunctionBuildErrors` 子 agent 的提示词明确要求：修复代码后调用 `UpdateFunctionReplacement` 写入固定代码，然后再 `BuildProject`。来源：`agents/builder_fixer_agent.py:152-156`

`UpdateFunctionReplacement` 的“真正落盘”由 `tools/builder/core.py` 的 `update_function_replacement(func_name, replace_code, reason)` 负责，其内部在写入 `data_manager` 之前做两层校验：
1. **rubric check**：先调用 `check_replacement_rubric(func_name, replace_code, original_code=...)`；若不通过直接返回 `{"ok": False, "reason": ...}`，不会持久化。来源：`tools/builder/core.py:339-353`
2. **可选编译验证**：若开启 `enable_compile_verify`，会调用 `_compile_verify_single_replacement(func_name, replace_code)`；该函数的“临时应用 + finally 恢复”机制用于避免污染工作树。来源：`tools/builder/core.py:355-361`，且临时应用/恢复逻辑见 `tools/builder/core.py:271-304`

只有当 rubric（以及可选编译验证）都通过后，才会调用 `data_manager.update_function_replacement(func_name, replace_code, reason)` 完成落盘。来源：`tools/builder/core.py:362-368`

---

## 5. 最终采纳逻辑：respond() 如何在两种来源之间做优先级选择

`agents/analyzer_agent.py` 中的 `respond(state)` 负责从对话历史里提取验证/修复证据，然后决定最终输出的 `FunctionClassifyResponse` 中 `function_replacement` 采用哪一份代码。

### 5.1 从对话历史提取验证通过的 replace_code

`_get_last_verified_replace_code(messages)` 的逻辑是：
1. 首先把每个 tool call 的 `id -> (name, args)` 缓存在 `id_to_call`；
2. 然后遍历消息，找到 `tool_call_id` 指向的工具结果消息；
3. 当 `name == "VerifyReplacement"` 且解析出的返回 JSON 中 `data.get("pass") is True` 时，取该 tool call 的 args 里的 `replace_code`（并且只保留最后一次）。  
- 证据：`_get_last_verified_replace_code` 实现。来源：`agents/analyzer_agent.py:99-122`

因此它把“对话里的最后一次通过 VerifyReplacement 的 replacement”作为可采纳的源代码。

### 5.2 判断是否存在针对当前 function_name 的成功修复

`_has_fix_function_build_errors_success(messages, function_name)` 的逻辑是：
- 找到 `FixFunctionBuildErrors` tool call 的 args 中 `function_name` 是否匹配当前函数；
- 再解析工具结果内容 JSON，检查 `data.get("success") is True`。  
- 证据：`_has_fix_function_build_errors_success` 实现。来源：`agents/analyzer_agent.py:124-149`

### 5.3 respond() 的采纳优先级与“fail closed 清空未验证 replacement”

`respond()` 的优先级逻辑在代码中直接写明为：  
“VerifyReplacement pass > FixFunctionBuildErrors 成功 > 否则清空未验证替换”。  
- 证据：respond 内部注释与分支。来源：`agents/analyzer_agent.py:164-183`

具体分支行为：
1. **VerifyReplacement pass=true：直接采用 verified_code**  
   `response = response.model_copy(update={"function_replacement": verified_code})`。来源：`agents/analyzer_agent.py:169-171`
2. **否则，如果 FixFunctionBuildErrors success：采用已落盘的 replacement**  
   从 `core.data_manager.data_manager.get_replacement_updates().get(current_fn)` 取 `ru.replacement_code`，并设置 `has_replacement=True`。  
   - 证据：落盘替换读取与采纳。来源：`agents/analyzer_agent.py:172-177`
3. **否则（两者都不满足）：若响应里带了 replacement，则清空**  
   - 证据：清空未验证 replacement 的条件与赋空逻辑。来源：`agents/analyzer_agent.py:178-183`

这实现了一个“fail closed”的最终策略：  
**只有存在 VerifyReplacement 通过或 FixFunctionBuildErrors 成功两类证据时，replacement 才会被写进最终响应。**

---

## 6. 额外安全层：function_classify 结束后再跑一次 rubric check

除了 LangGraph 内部的 `VerifyReplacement` 流程外，`function_classify()` 在 `graph.ainvoke()` 返回后还会执行一层“结束后 rubric 校验”。  
- 证据：`function_classify()` 中 `Rubric check: if classifier produced a replacement, validate it before use`。来源：`agents/analyzer_agent.py:268-281`

具体逻辑：
- 仅当 `final_response.has_replacement == True` 且 `function_replacement` 非空时，调用 `check_replacement_rubric(func_name, final_response.function_replacement, original_code=...)`；
- 若 rubric 不通过，把 `replacement_check_reason` 写入响应并重建 `FunctionClassifyResponse`。  
`d["replacement_check_reason"] = check_result["reason"]`。来源：`agents/analyzer_agent.py:276-280`

该层逻辑不改变最终采纳优先级（那是 `respond()` 决定的），但为“模型最终输出的 replacement 是否符合 rubric”提供了二次保护。

---

## 7. 流程图（Mermaid）

```mermaid
flowchart TD
  A[function_classify(func_name) 构建 LangGraph] --> B[LangGraph: agent(call_model)]
  B --> C{LLM 是否产生 tool_calls?}
  C -- 是 --> D[tools(ToolNode 执行工具)]
  D --> B
  C -- 否 --> E[respond(): 采纳优先级]
  E --> F[返回 final_response]
  F --> G[function_classify: 结束后 rubric check(可选)]
  G --> H[最终返回 FunctionClassifyResponse]
  
  subgraph Classifier 内部(按 prompts/function_classifier.py 约束)
    X[分类确定有 replacement_code(RECV/IRQ/INIT/LOOP)] --> Y[调用 VerifyReplacement(func_name, replace_code)]
    Y --> Z{VerifyReplacement pass?}
    Z -- 否 --> W[调用 FixFunctionBuildErrors(function_name, error_info=build_stderr, replace_code?)]
    W --> Z2{FixFunctionBuildErrors success?}
    Z2 -- 是 --> Y2[输出 has_replacement=true(视为已验证)]
    Z2 -- 否 --> Y3[输出失败/NODRIVER 等]
    Z -- 是 --> Y4[输出 has_replacement=true]
  end
  
  subgraph respond() 采纳优先级
    E1[取最后一次 VerifyReplacement(pass=true) 的 replace_code] --> E2{verified_code存在?}
    E2 -- 是 --> E3[用 verified_code 覆盖 function_replacement]
    E2 -- 否 --> E4{FixFunctionBuildErrors(success=true)存在?}
    E4 -- 是 --> E5[从 data_manager 读取已落盘 replacement_code]
    E4 -- 否 --> E6[清空未验证 replacement: has_replacement=false]
  end
```

---

## 8. 伪码（分支与调用顺序）

### 8.1 LangGraph 主循环 + respond() 采纳

```python
def should_continue(state):
    return "tools" if state["messages"][-1].tool_calls else "respond"

def respond(state):
    verified_code = last_VerifyReplacement_pass_true_replace_code(state["messages"])
    fixer_success = has_FixFunctionBuildErrors_success(state["messages"], state["function_name"])

    if verified_code:
        # 优先级 1：采用通过 VerifyReplacement 的代码
        response.function_replacement = verified_code
    elif fixer_success:
        # 优先级 2：采用 fixer 已落盘的 replacement
        response.function_replacement = data_manager.get_replacement_updates()[current_fn].replacement_code
        response.has_replacement = True
    else:
        # 优先级 3：fail closed，清空未验证 replacement
        if response.has_replacement and response.function_replacement.strip():
            response.has_replacement = False
            response.function_replacement = ""

    return response
```

### 8.2 VerifyReplacement / FixFunctionBuildErrors（按工具内部与提示词约束的调用序）

```python
def classifier_execution(function_type):
    if function_type in {"RECV", "IRQ", "INIT", "LOOP"}:
        replace_code = generate_replacement_code()

        vr = VerifyReplacement(func_name, replace_code)
        if vr.pass is False:
            # prompts/function_classifier.py：如果有 build_stderr 则委托 FixFunctionBuildErrors
            fb = FixFunctionBuildErrors(function_name=func_name,
                                         error_info=vr.build_stderr,
                                         replace_code=replace_code)
            if fb.success is True:
                output(has_replacement=True, function_replacement="(不一定由 LLM 直接给出，而由 respond() 读取已落盘代码)")
            else:
                output(has_replacement=False or NODRIVER)
        else:
            output(has_replacement=True, function_replacement=replace_code)
```

---

## 9. 证据索引（本文件引用到的关键代码/提示词）

1. `prompts/function_classifier.py`
   - VerifyReplacement / FixFunctionBuildErrors / 结束前校验要求：来源：`prompts/function_classifier.py:47-51`
   - 分类输出规则：`Execution Instructions`、`has_replacement` 与 replacement code 生成条件：来源：`prompts/function_classifier.py:254-303`

2. `agents/analyzer_agent.py`
   - LangGraph 工具注入（`verify_replacement_tool` + `builder_fixer_agent`）：来源：`agents/analyzer_agent.py:39-73`
   - 工具循环控制（`should_continue`）：来源：`agents/analyzer_agent.py:198-205`
   - 从对话提取 `VerifyReplacement(pass=true)` 的最后 verified code：来源：`agents/analyzer_agent.py:99-122`
   - 判断 `FixFunctionBuildErrors(success=true)`：来源：`agents/analyzer_agent.py:124-149`
   - respond 采纳优先级与清空未验证 replacement：来源：`agents/analyzer_agent.py:164-183`
   - 结束后 rubric check：来源：`agents/analyzer_agent.py:268-281`

3. `tools/builder/core.py`
   - rubric + 可选编译验证的 verify_replacement：来源：`tools/builder/core.py:316-336`
   - `_compile_verify_single_replacement` 临时应用与恢复：来源：`tools/builder/core.py:271-313`
   - update_function_replacement 的 rubric + 可选编译 verify 再落盘：来源：`tools/builder/core.py:339-368`

4. `utils/replacement_rubric.py`
   - fail closed：rubric 异常时拒绝 replacement：来源：`utils/replacement_rubric.py:82-88`

5. `agents/builder_fixer_agent.py`
   - FixFunctionBuildErrors 工具包装：来源：`agents/builder_fixer_agent.py:170-175`
   - run_builder_fix 用户输入构造（error_info、可选 replace_code、要求 UpdateFunctionReplacement + BuildProject）：来源：`agents/builder_fixer_agent.py:138-156`
   - 成功标准（提示词）+ 程序化二次校验（error_info 仍在 stderr 则失败）：来源：`agents/builder_fixer_agent.py:152-156`、`agents/builder_fixer_agent.py:181-190`

6. `tools/builder/tool.py`（VerifyReplacement 工具包装）
   - `VerifyReplacement` 的 tool 描述与返回值 JSON 串行化：来源：`tools/builder/tool.py:72-80`

