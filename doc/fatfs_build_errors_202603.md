# FATFS BSP 编译错误根因（2026-03）

## 现象

清理 ai_log 后重跑 fatfs demo，Build 报错：

1. `board/CubeMX_Config/Src/stm32f4xx_hal_msp.c:373: error: 'TIM_HandleTypeDef' has no member named 'ErrorCode'`
2. `board/board.c:63: error: static declaration of 'SystemClock_Config' follows non-static declaration`（board.h 声明为 `void SystemClock_Config(void);`）
3. `board/board.c:84: error: 'RCC_PLLInitTypeDef' has no member named 'PLLR'`

## 根因

均为 **FunctionClassifier 生成的替换代码** 与 **STM32F401 的 HAL 不一致**：

| 函数 | 错误 | 原因 |
|------|------|------|
| **HAL_TIM_MspPostInit** | `htim->ErrorCode = HAL_TIM_ERROR_NONE` | STM32F4 的 `TIM_HandleTypeDef` 只有 `State` 等，**没有 `ErrorCode`**（该成员在部分新 HAL 如 F7/H7 才有） |
| **SystemClock_Config** | `static void SystemClock_Config(void)` | 替换写成了 `static`，与 board.h 的 `void SystemClock_Config(void);` 不一致 |
| **SystemClock_Config** | `RCC_OscInitStruct.PLL.PLLR = 7` | STM32F401 的 `RCC_PLLInitTypeDef` **没有 PLLR**；PLLR 仅在 F410/F446/F469/F479/F412/F413/F423 等型号的 HAL 中存在 |

即：Classifier 用到了“其他芯片/其他 HAL”的模板（含 ErrorCode、PLLR、static），没有严格按**当前 BSP 的 HAL 与声明**生成。

## 修复方向

1. **Prompt**：在 FunctionClassifier 中明确要求  
   - 替换的**函数声明**（含 static/non-static）必须与**原始实现及头文件声明**完全一致；  
   - 只使用**当前工程 / 目标芯片 HAL 中真实存在的结构体成员**，不得使用其他系列 HAL 的成员（如 TIM 的 ErrorCode、RCC PLL 的 PLLR 在 F401 上不可用）。
2. **Rubric**：可在替换检查中增加“未使用不存在的结构体成员”“声明与头文件一致”等规则。
3. **本案例临时修复**：  
   - HAL_TIM_MspPostInit：替换中删除对 `htim->ErrorCode` 的赋值，只保留对 `State` 的设置；  
   - SystemClock_Config：声明改为 `void SystemClock_Config(void)`，并去掉对 `PLLR` 的赋值（或按芯片条件编译包裹）。

---

## Builder Agent 超时（50 轮）原因（2026-03 同次 run）

### 现象

Build 失败后触发 Builder Agent 修编，未在 50 步内返回“构建成功”，最终 `GraphRecursionError`，Failcheck 报 “Iterations exceeded: 50”。

### 原因

1. **步数上限固定为 50**  
   `builder_agent` 的 graph 使用 `recursion_limit=50`，即整图（agent → tools → agent → …）最多 50 步。只有某一步里模型**不再发起 tool_calls** 才会走到 `respond` 并结束；只要一直有 tool_calls，就会一直循环直到 50 步。

2. **Builder 手里既有“修编”工具也有“查库”工具**  
   Builder 除 `BuildProject`、`UpdateFunctionReplacement`、`GetReplaceFuncDetailsByFile`、`FixFunctionBuildErrors` 等修编工具外，还通过 MCP 拿到与 Collector 同套的 **GetFunctionInfo / GetMMIOFunctionInfo** 等。Prompt 里又写“遇到构建失败时用 GetFunctionInfo / GetMMIOFunctionInfo 了解函数”，模型容易先对**多个函数**轮番拉信息，而不是：先 BuildProject → 从 stderr 锁定**一个**出错函数 → 只查该函数 → 改替换 → 再 Build。

3. **步数被“查库”耗掉**  
   若每轮都调多次 GetFunctionInfo / GetMMIOFunctionInfo（对不同函数），或反复 BuildProject 但错误多、修不完，则 50 步很快用尽，还没等到“构建成功且不再调工具”的那一步就触发递归上限。

4. **Failcheck 报告里的“分类”来自整段 session**  
   Failcheck 加载的是**整段 session**（含前面 Analyzer 对很多函数的分类对话），所以报告里大段“对一系列函数进行分类、GetFunctionInfo”等，多半是 **Analyzer** 的行为；真正导致超时的是 **Builder** 在这 50 步内没有在“少步数”内完成“定位错误 → 改替换 → 再构建成功”。

### 改进方向

- **Prompt**：明确要求“先且仅先调用 BuildProject；根据 stderr 只针对**第一个错误**对应的**一个**函数调用 GetFunctionInfo/GetMMIOFunctionInfo；再 UpdateFunctionReplacement 或 FixFunctionBuildErrors；再 BuildProject。单次失败不要对多个函数轮番查信息。”
- **步数**：若单次构建错误较多，可将 builder 的 `recursion_limit` 提高到 80～100，或按“待修函数数”动态设上限。
- **工具范围**：若希望 Builder 少“逛”库，可只暴露 GetFunctionAnalysisAndReplacementFormatted / GetReplaceFuncDetailsByFile，不把 GetFunctionInfo/GetMMIOFunctionInfo 暴露给 Builder（仅 Analyzer 使用）。

---

## 为何“单函数编译通过”措施没挡住首次构建失败？

### FunctionClassifier 里已有的 Rubric + 编译验证（你说的对）

在 **FunctionClassifier** 流程里已经做了 Rubric + 编译认证，具体是：

1. **VerifyReplacement 工具**（`tools/builder/tool.py` → `core.verify_replacement`）：Classifier 图内可用，内部先 rubric、再（若 `enable_compile_verify`）单函数编译验证，不落盘。
2. **Prompt**（`prompts/function_classifier.py`）：要求“在输出最终结果前，若有替换代码必须调用 VerifyReplacement，且只有 pass: true 才能结束”。
3. **respond 节点**（`agents/analyzer_agent.py`）：在生成最终 `final_response` 时，用 `_get_last_verified_replace_code(state["messages"])` 取**对话中最后一次 VerifyReplacement 且 pass=true** 的 `replace_code`，**覆盖** structured output 的 `function_replacement`，保证写出去的代码是“验证过”的那份。

所以：**只要 Classifier 在结束前调用了 VerifyReplacement 并且有一次 pass=true**，最终进 `mmio_info_list` 的 `function_replacement` 就是经过 Rubric + 单函数编译验证的。

### 可能没完全奏效的原因

- **模型并非每次都会按 prompt 执行**：有可能在“有替换代码”的情况下没有调用 VerifyReplacement 就输出了最终结果（例如直接给 structured output、不再发起 tool call），或先调了但 pass=false 后没有重试就结束，或 50 步用满提前结束。
- 此时 **`_get_last_verified_replace_code` 拿不到任何 pass=true 的调用**，返回 `None`，就不会覆盖；最终 `final_response.function_replacement` 就是 **模型原始输出**，没有经过 VerifyReplacement。
- **事后 rubric**（`function_classify` 返回前再跑一次 rubric）：失败时只写入 `replacement_check_reason`，**没有**清空 `function_replacement` 或阻止写入 `mmio_info_list`，也没有再做编译验证，所以进 `mmio_info_list` 的仍可能是未验证代码。

因此：Classifier 里的“单函数编译通过”措施在**模型按要求调用且通过**时是生效的；在**模型未调用或未通过**时，仍会 persist 未验证的替换，首次构建就可能失败。

（不在 replace_funcs 侧做二次验证：每次编译都会对大量函数跑验证、成本高，且验证不通过时无法返厂让模型修改，仅跳过意义有限，故保持由 Classifier 内 VerifyReplacement + 覆盖逻辑保证即可。）
