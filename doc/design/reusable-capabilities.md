# 可拆卸与可复用能力清单

本文面向实验室同学说明：哪些部分可以从 LCMHalMCP 中拆出来独立复用，它们代表什么能力，能分析/模拟/反馈什么。

## 1. 静态分析能力

代表模块：

- `queries/`
- `tools/collector/`
- `models/query_results/`
- `utils/db_file.py`
- `utils/db_query.py`

能力说明：

- 基于 CodeQL DB 和 `src.zip`，提取 C/C++ 固件源码结构。
- 可作为 stdio MCP 服务，也可被 Python 直接调用。

具体能分析：

- 函数列表、函数源码、文件路径、起始行号。
- 函数调用关系，包括 caller/callee、直接/间接调用、返回类型和调用点行内容。
- 结构体、枚举、成员类型、定义位置。
- 驱动对象和驱动相关表达式，例如函数表、注册结构、driver-to-function-call。
- MMIO 相关函数、MMIO 表达式、包含 MMIO 的函数、driver 函数、buffer 函数。
- MMIO 相关文件集合。
- 从某个函数出发的调用栈/调用闭包。

可复用场景：

- 给其他嵌入式项目做驱动/外设函数索引。
- 给论文实验抽取 MMIO/driver 函数集合。
- 给别的 agent 提供 CodeQL-backed MCP 工具。
- 做代码理解、函数定位、结构体上下文补全。

## 2. MCP 工具服务能力

代表模块：

- `server.py`
- `tools/collector/mcp_server.py`
- `tools/builder/mcp_server.py`
- `tools/emulator/mcp_server.py`

能力说明：

- 把项目内部 Python 函数包装成 MCP tools。
- 支持 Cline、Cursor 或 LangChain MCP client 通过 stdio 调用。

可暴露工具：

- `GetFunctionInfo`
- `GetMMIOFunctionInfo`
- `GetStructOrEnumInfo`
- `GetFunctionCallStack`
- `GetDriverInfo`
- `BuildProject`
- `VerifyReplacement`
- `UpdateFunctionReplacement`
- `EmulateProject`
- `GetMMIOFunctionEmulateInfo`
- `GetFunctionCallsEmulateInfo`

可复用场景：

- 不使用 LCMHalMCP 全流程，只把 Collector 当成代码知识库。
- 给其他 LLM agent 提供构建/模拟反馈工具。
- 做交互式静态分析调试。

## 3. 函数分类与替换生成能力

代表模块：

- `agents/analyzer_agent.py`
- `prompts/function_classifier.py`
- `prompts/code_generation_rules.md`
- `utils/replacement_rubric.py`
- `models/analyze_results/function_analyze.py`

能力说明：

- 将硬件相关函数分类，并判断是否需要生成 replacement。
- 结合 CodeQL collector 上下文和 LLM 推理。
- 内置 fail-closed 策略，减少未验证代码进入结果。

具体能判断：

- `CORE`：NVIC、OS kernel、scheduler、VTOR 等不应替换路径。
- `RECV`：输入/接收类函数，适合映射到 `HAL_BE_In`、`HAL_BE_ENET_ReadFrame`。
- `IRQ`：中断处理或中断驱动路径。
- `RETURNOK`：可用固定返回值推进执行的函数。
- `SKIP`：delay、wait、日志、低风险跳过函数。
- `NODRIVER`：非硬件依赖函数。
- `INIT`：初始化函数，需保留 delegate call 和关键寄存器语义。
- `LOOP`：阻塞轮询或等待状态位函数。

具体能生成：

- 保留函数签名的 C replacement。
- 调用 `HAL_BE_Out` / `HAL_BE_In` / `HAL_BE_Block_Read` / `HAL_BE_Block_Write` / `HAL_BE_return_0` / `HAL_BE_return_1` 的模拟接口代码。
- 对 thin wrapper、CORE 函数、初始化关键路径给出不替换判断。

可复用场景：

- 批量给 HAL/driver 函数打标签。
- 生成仿真友好的 driver stub。
- 对比 full/minimal tool profile 的上下文消融实验。

## 4. 编译验证与修复能力

代表模块：

- `tools/builder/`
- `agents/builder_agent.py`
- `agents/builder_fixer_agent.py`
- `utils/build_log_extract.py`

能力说明：

- 不仅生成代码，还能临时应用替换并编译验证。
- 编译失败时可定位到单函数 replacement，调用 BuilderFixer 修复。

具体能反馈：

- 编译 stdout/stderr。
- exit code。
- 错误片段压缩。
- replacement 是否通过 rubric。
- replacement 是否通过临时编译验证。
- 修复是否成功、错误是否消失、修改摘要。

可复用场景：

- 给任意 C 工程做 LLM 代码补丁的“临时落盘 + 编译 + 恢复”验证。
- 将编译错误作为工具反馈喂给另一个 agent。
- 对生成代码做事务式校验，避免污染源码。

## 5. 源码替换与恢复能力

代表模块：

- `tools/replacer/`
- `utils/src_ops.py`
- `utils/db_file.py`

能力说明：

- 将 CodeQL DB 中的函数位置映射回真实源码路径。
- 按函数级别替换代码。
- 从 DB 的 `src.zip` 恢复文件。
- 自动注入 `HAL_BE_*` 弱符号。

具体能处理：

- UTF-8 / Windows-1252 等源码读取 fallback。
- 原函数文本找不到时生成 diff 诊断日志。
- `.c` 文件顶部注入弱符号，避免头文件重复定义。
- `proj_path` 到 `src_path` 的路径转换。

可复用场景：

- 单函数源到源转换。
- 批量插桩/替换/恢复。
- 为其他模拟器注入固定 hook 函数。

## 6. 模拟器配置生成能力

代表模块：

- `tools/emulator/conf_generator.py`
- `fuzzemu/`

能力说明：

- 从构建产物生成 fuzzemu 所需配置。
- 自动补齐符号、输入、规则、handler、memory map。

具体能生成/修正：

- `emulate/output.bin`
- `emulate/syms.yml`
- `emulate/base_config.yml`
- `emulate/semu_rule.txt`
- `emulate/base_input/input.bin`
- `emulate/semu_config.yml`
- flash size 4KB 对齐。
- `_estack` 到 `initial_sp` 的修正。
- `HAL_BE_*` 到 `fuzzemu.handlers.common.*` 的 handler 映射。
- `mmio_funcs` 追踪列表。

可复用场景：

- 给其他 ARM Cortex-M ELF 自动生成 fuzzemu 配置。
- 快速绑定一组函数到 Python handler。
- 复用符号提取、flash 修正、栈指针修正逻辑。

## 7. 模拟器运行与动态反馈能力

代表模块：

- `tools/emulator/core.py`
- `tools/emulator/emulate_runner.py`
- `fuzzemu/fuzzemu/`
- `fuzzemu/handlers/`

能力说明：

- 基于 fuzzemu/Unicorn 运行固件。
- 将 MMIO 函数调用、函数调用序列和异常写到 debug 输出。
- 为上层 agent 提供动态反馈。

具体能模拟：

- 输入类外设：通过 `HAL_BE_In` 从 `input.bin` 或 fuzz 输入填充 buffer。
- 输出类外设：通过 `HAL_BE_Out` 记录/消费输出。
- 以太网帧：通过 `HAL_BE_ENET_ReadFrame` 提供帧数据。
- 块设备：通过 `HAL_BE_Block_Read` / `HAL_BE_Block_Write` 模拟读写块数。
- 固定返回值：通过 `HAL_BE_return_0` / `HAL_BE_return_1` 或 handler 返回成功/状态码。
- delay/wait/PHY/MDIO 等函数：通过 handler alias 跳过或返回固定值。

具体能反馈：

- 是否模拟成功。
- stdout/stderr 和超时信息。
- `exceptional loop`、当前函数、当前调用者。
- MMIO 函数进入记录：PC、IRQ、目标函数、调用者函数。
- 函数调用序列与压缩后的循环模式。
- `UNMAPPED` / `fault PC` 到函数名的映射。

可复用场景：

- 对替换后的固件做无硬件动态验证。
- 为 LLM 或规则系统提供运行时诊断信息。
- 独立做 firmware fuzz / coverage / crash reproduction。

## 8. 动态闭环修复能力

代表模块：

- `agents/emulator_runner_agent.py`
- `agents/fixer_agent.py`
- `agents/builder_agent.py`

能力说明：

- 把模拟失败反馈转成代码修复，再构建回归。

闭环：

```text
EmulateProject
  -> GetMMIOFunctionEmulateInfo / GetFunctionCallsEmulateInfo
  -> Fixer
  -> Builder
  -> EmulateProject
```

可复用场景：

- 其他固件模拟项目的“失败-诊断-修复-回归”agent 框架。
- 以动态日志为证据的 replacement 迭代修复。

## 9. 批处理与实验统计能力

代表模块：

- `scripts/batch_main_analyze_*`
- `scripts/batch_main_analyze_adaptive.py`
- `scripts/e3b_*`
- `utils/classify_log_stats.py`
- `utils/lcmhal_testcase_scan.py`

能力说明：

- 扫描 testcase 矩阵并批量运行。
- 根据 retry 密度自动调节并发。
- 汇总分类、替换、token usage、实验批次表格。

可复用场景：

- 大规模 demo 评测。
- 多平台对比实验。
- 消融实验和不确定性实验统计。

