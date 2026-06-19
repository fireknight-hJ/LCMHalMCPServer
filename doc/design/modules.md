# 模块设计与结构

## 1. `main.py`

`main.py` 是 CLI 主入口，负责解析命令并编排工作流。

命令：

- `run`：完整闭环，包含构建建库、分析替换、编译、生成模拟配置、运行 EmulatorRunner、fault 函数恢复循环。
- `build`：只执行构建建库、分析替换、编译、生成模拟配置，不进入动态 EmulatorRunner 闭环。
- `emulate`：只运行当前 testcase 的 `emulate/output.elf` 与 `semu_config.yml`。
- `recover`：从 CodeQL DB 的 `src.zip` 恢复真实源码。
- `clean`：清理单函数或全部 `lcmhal_ai_log`，可选恢复源码。
- `analyze`：单函数分析。
- `dump-replacements`：导出 replacement 日志。
- `classify-stats`：统计分类结果，可批量扫描 testcase 根目录。

## 2. `agents/`

### `analyzer_agent.py`

FunctionClassifier 智能体。它通过 Collector MCP 工具获取函数源码、MMIO 信息、结构体/枚举、调用栈和 driver 信息，输出 `FunctionClassifyResponse`。

当前函数类型：

- `CORE`：OS/NVIC/scheduler/VTOR 等关键函数，不替换。
- `RECV`：接收/输入类函数，通常映射到 `HAL_BE_In` 或协议输入。
- `IRQ`：中断路径相关函数。
- `RETURNOK`：可用固定成功值推进执行的函数。
- `SKIP`：可跳过的延时、等待、日志等函数。
- `NODRIVER`：无硬件依赖或不应替换。
- `INIT`：初始化函数，需谨慎保留关键 delegate/寄存器语义。
- `LOOP`：阻塞轮询类函数。

### `builder_agent.py`

项目构建智能体。它调用 Builder 工具应用已有 replacement 并编译工程；若失败，可读取按文件组织的替换详情，调用 `builder_fixer_agent` 修复具体函数。

### `builder_fixer_agent.py`

单函数编译错误修复工具，暴露为 `FixFunctionBuildErrors`。输入函数名、错误片段和可选当前 replacement，输出是否修复成功、原因和修改摘要。

### `fixer_agent.py`

动态反馈修复智能体。它读取模拟器的 `lcmhal.txt`、`function.txt` 和已知替换上下文，生成 `ReplacementUpdate`，用于修复 exceptional loop、UNMAPPED、fault PC 等运行时问题。

### `emulator_runner_agent.py`

动态闭环主控智能体。工具包括 `EmulateProject`、`GetMMIOFunctionEmulateInfo`、`GetFunctionCallsEmulateInfo`、`Fixer` 和 `Builder`，用于执行：

```text
emulate -> diagnose -> fix -> build -> emulate
```

### `driver_locator_agent.py`

驱动目录定位智能体，用于识别 HAL driver 目录和 kernel support 目录。

## 3. `tools/collector/`

静态分析能力的主模块，读取 CodeQL DB 与 `src.zip`。

核心接口：

- `register_db(db_path)`：注册数据库。
- `validate_database(db_path)`：检查 DB、`src.zip` 等。
- `get_files_in_db_zip()` / `get_tree_in_db_zip()`：列出数据库源码归档。
- `get_mmio_func_list()`：返回后续流程使用的 MMIO 函数全集，当前覆盖 `MMIOFunction`，并可把 buffer 函数并入。
- `get_mmio_func_list_interesting_mmioexpr()`：较窄子集，来自 interesting MMIO expr 口径，主要用于对照旧实验。
- `get_mmio_files()`：返回 MMIO 相关文件。
- `get_mmio_func_info(func_name)`：返回 MMIO 表达式、包含关系和函数元数据。
- `get_function_info(func_name)` / `get_function_source(func_name)`：返回函数源码、文件和行号。
- `get_struct_or_enum_info(name)`：返回结构体/枚举定义和成员。
- `get_func_call_stack(func_name)`：递归调用栈。
- `get_driver_info(driver_name)`：driver 注册、调用、表达式等信息。

MCP 工具由 `tools/collector/mcp_server.py` 暴露，LangChain tool 包装在 `tools/collector/tool.py`。

## 4. `tools/builder/`

构建、验证和替换落盘控制模块。

- `proj_builder.py`：执行 testcase 的 `clear.sh`、`build.sh`，以及 CodeQL database 构建。
- `core.py`：
  - `replace_funcs()`：将 `DataManager` 中的 replacement 应用到真实源码。
  - `recover_funcs()`：恢复被替换函数。
  - `build_project()`：编译工程并返回 stdout/stderr/exit_code。
  - `verify_replacement()`：rubric + 可选编译验证，不持久化。
  - `_compile_verify_single_replacement()`：临时应用单函数替换、编译、finally 恢复。
  - `update_function_replacement()`：rubric + 可选编译验证通过后写入 `DataManager`。
  - `elf_to_bin()`：把 ELF 转为 BIN。
- `tool.py` / `mcp_server.py`：暴露 `BuildProject`、`VerifyReplacement`、`UpdateFunctionReplacement`、`GetFunctionAnalysisAndReplacement` 等工具。

## 5. `tools/replacer/`

源码替换与恢复模块。

- `code_replacer.py`：根据 `FunctionInfo` 找到原函数文本，调用 `src_replace()` 替换真实源码。
- `code_recover.py`：从 CodeQL DB 的 `src.zip` 恢复文件或函数。
- `diff_gen.py`：生成替换差异。

`utils/src_ops.py` 中的 `weak_funcdef` 会在 `.c` 文件顶部注入 `HAL_BE_return_0`、`HAL_BE_return_1`、`HAL_BE_In`、`HAL_BE_Out`、`HAL_BE_ENET_ReadFrame`、`HAL_BE_Block_Read`、`HAL_BE_Block_Write` 等弱符号。

## 6. `tools/emulator/`

模拟器配置生成、运行和反馈读取模块。

- `conf_generator.py`：
  - 生成 `base_config.yml`、`semu_rule.txt`、`base_input/input.bin`。
  - 调用 `fuzzemu-helper config base_config.yml -s` 生成 `semu_config.yml`。
  - 从 ELF 提取 `syms.yml`。
  - 修正 flash memory map、`initial_sp`、handler alias。
  - 写入 `mmio_funcs` 供 fuzzemu 跟踪。
- `emulate_runner.py`：
  - 确保 `output.bin` 与 `output.elf` 同步。
  - 运行 `python -m fuzzemu.harness input.bin semu_config.yml -d 5 --skip-mmio-hook`。
  - 支持 fuzz 模式、AFL 任务启动和任务列表。
- `core.py`：
  - `emulate_proj()` 返回 `EmulateResult`。
  - `mmio_function_emulate_info()` 读取 `debug_output/lcmhal.txt`。
  - `function_calls_emulate_info()` 读取并压缩 `debug_output/function.txt`。
  - `get_fault_function_from_emulate_output()` 将 UNMAPPED/fault PC 映射到 `syms.yml` 中最近的函数符号。

## 7. `core/`

`core/data_manager.py` 是跨模块状态中心。

保存：

- `mmio_info_list`：函数名到 `FunctionClassifyResponse`。
- `mmio_infos_by_file`：按文件聚合的分类结果。
- `replacement_updates`：函数名到当前 `ReplacementUpdate`。
- `replacement_updates_by_file`：按文件聚合的替换。
- `replacement_history`：每个函数最近几次替换历史。

## 8. `models/`

- `models/analyze_results/function_analyze.py`：函数分类、替换更新、修复响应。
- `models/build_results/`：构建输出和 BuilderFixer 结果。
- `models/emulate_results/`：模拟输出。
- `models/query_results/`：CodeQL 查询结果解析后的 dataclass，包括函数、调用、结构体、枚举、driver、MMIO 表达式等。

## 9. `queries/`

CodeQL 查询按用途组织：

- `queries/libraries/`：`CommonLocator.qll`、`DriverLocator.qll`、`MMIOAnalyzer.qll`、`RegistrationLocator.qll`。
- `queries/collectors/common/`：函数、调用、结构体、枚举、文件信息。
- `queries/collectors/driver/`：driver 来源、函数调用、全局变量、使用文件等。
- `queries/collectors/mmio/`：MMIO 函数、driver 函数、buffer 函数、MMIO 表达式和包含关系。
- `queries/tests/`：查询调试与回归测试。

## 10. `utils/`

重要工具：

- `db_file.py`：读取 `src.zip` 中文件、行、函数/结构体。
- `db_cache.py`：JSON 日志读写与缓存检查。
- `ai_log_manager.py` / `log_index.py`：session 日志、LangGraph 节点日志和索引。
- `replacement_rubric.py`：替换代码规则校验，含确定性检查和 LLM rubric。
- `build_log_extract.py`：压缩构建错误。
- `classify_log_stats.py`：分类日志统计。
- `lcmhal_testcase_scan.py`：扫描 testcase 目录。
- `src_ops.py`：源码替换、插入和 proj/src 路径映射。

