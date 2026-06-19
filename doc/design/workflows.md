# 工作流设计

## 1. `run` 完整闭环

```text
python main.py run <testcase>
```

流程：

1. 读取 `<testcase>/lcmhal_config.yml` 并初始化 `config.globs`。
2. 调用 `build_proj_dbgen()` 执行清理、构建和 CodeQL DB 生成。
3. 注册 CodeQL DB。
4. `init_builder()` 加载 MMIO 函数并分析，初始化 `DataManager`。
5. `build_project()` 首次编译；若失败，调用 `Builder Agent` 递归修复。
6. `generate_emulator_configs()` 生成 `emulate/` 下的模拟配置。
7. `EmulatorRunner Agent` 运行动态闭环：
   - `EmulateProject`
   - 失败时读取 `GetMMIOFunctionEmulateInfo` / `GetFunctionCallsEmulateInfo`
   - 调用 `Fixer`
   - 调用 `Builder`
   - 再次 `EmulateProject`
8. 若模拟失败且可从 fault PC 解析出未分析函数，最多 3 轮执行 fault recovery：
   - `analyze_functions([fault_func])`
   - `replace_funcs()`
   - `build_project()`
   - `generate_emulator_configs()`
   - `run_emulator()`

## 2. `build` 半流程

```text
python main.py build <testcase>
```

用于批量生成替换、编译并产出模拟器输入，不进入动态反馈闭环。适合大批量平台矩阵的前处理。

步骤：

1. 构建/刷新 CodeQL DB。
2. Collector 读取 MMIO 函数。
3. Analyzer 对函数分类并生成 replacement。
4. Builder 应用 replacement 并编译。
5. 成功后生成 `base_config.yml`、`semu_config.yml`、`syms.yml` 等。

## 3. FunctionClassifier 验证闭环

Analyzer Agent 的替换采纳规则：

```text
LLM 生成 replacement
  -> VerifyReplacement(func_name, replace_code)
     -> replacement_rubric deterministic/LLM check
     -> 可选临时编译验证
  -> 如果 VerifyReplacement pass=true，采用该 replacement
  -> 如果失败且有 build_stderr，调用 FixFunctionBuildErrors
  -> 如果 BuilderFixer success=true，采用已落盘 replacement
  -> 否则清空未验证 replacement
```

这个策略避免“模型看起来写了替换，但没有被验证”的代码进入最终结果。

## 4. 编译验证事务

`_compile_verify_single_replacement()` 的事务语义：

```text
找到函数原始源码
  -> 临时替换到真实源码
  -> clear.sh
  -> build.sh
  -> 无论成功失败，finally 恢复原始源码
  -> 返回 ok/reason/build_stderr
```

`UpdateFunctionReplacement` 在真正写入 `DataManager` 前也会走 rubric 与可选编译验证。

## 5. 模拟器执行闭环

`tools/emulator/core.py` 对模拟成功的判定：

- 子进程 `exit_code == 0`
- `debug_output/lcmhal.txt` 中没有 `exceptional loop`

主要反馈：

- `std_out` / `std_err`：模拟器进程输出。
- `lcmhal.txt`：MMIO 函数进入、exceptional loop、当前函数、调用者函数。
- `function.txt`：函数调用序列，读取时会压缩重复行和短循环。
- `stdout.txt`：可包含 `UNMAPPED`、`fault PC` 等异常定位信息。

## 6. `dump-replacements`

```text
python main.py dump-replacements <testcase>
```

输出 `replacement_log.md`，包含：

- testcase 路径；
- 实际发生过替换的函数总览；
- 每个函数的原始分析、替换详情、替换历史；
- FunctionClassifier 汇总；
- interesting MMIO expr 子集对照。

## 7. `classify-stats`

```text
python main.py classify-stats <testcase-or-root>
```

单例模式统计一个 testcase 的 `lcmhal_ai_log`。批量模式递归扫描包含 `lcmhal_config.yml` 的目录，输出：

- 每个函数类型计数；
- `has_replacement` 拆分；
- replacement_update 数量；
- 跨 demo 总计和按函数名去重统计；
- 可选 JSON 机器可读输出。

