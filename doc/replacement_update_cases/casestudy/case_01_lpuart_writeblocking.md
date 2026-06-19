# Case Study - `LPUART_WriteBlocking`（NXP_FATFS_BareMetal）

## 一句话结论

`LPUART_WriteBlocking` 本函数问题已修复：现在会被纳入 mmio 候选并生成有效替换，运行不再卡在该函数；当前剩余故障位于独立的 `exit/_exit/strchr` 路径。

## 背景与症状

- Demo: `testcases/server/nxp/NXP_FATFS_BareMetal`
- 目标函数: `LPUART_WriteBlocking`
- 初始症状:
  - 该函数未稳定进入 classify 日志链路（表现为 `function_type=NA` 语义）；
  - 在 `mmio_info.json` 中落于 `buffer_functions`，未进入 `mmio_functions`；
  - 仿真存在 loop/hang 风险，需由 RU 兜底。

## 根因分析

- 候选构建阶段仅使用 `mmio_functions`，导致被归在 `buffer_functions` 的函数被漏掉。
- `LPUART_WriteBlocking` 属于“语义上有硬件轮询/等待风险，但分类数据落在 buffer 桶”的边界函数。

## 修复动作

### 配置开关

- 文件: `config/globs.py`
- 变更: 增加 `enable_buffer_functions_as_mmio = True`（默认开启）
- 目的: 允许将 buffer 类函数并入 mmio 候选集合。

### 候选构建逻辑

- 文件: `tools/collector/collector.py`
- 变更: `get_mmio_func_list(db_path)` 在开关开启时合并：
  - `mmio_functions`
  - `buffer_functions`
- 处理: 去重后返回稳定有序列表。

### 验证步骤

- 清理历史 RU 与 testcase 统计文件，避免旧产物干扰。
- 单函数 analyze：
  - `python main.py analyze testcases/server/nxp/NXP_FATFS_BareMetal --func-name LPUART_WriteBlocking`
  - 输出：`function_type=LOOP`，`has_replacement=true`
- 全量 run：
  - `python main.py run testcases/server/nxp/NXP_FATFS_BareMetal`
  - 轨迹显示 UART 输出链路持续前进，不再在该函数点位卡死。

## 结果与边界

- 已达成：
  - `LPUART_WriteBlocking` 被正确纳入候选；
  - classifier 与 RU 结果闭环成立；
  - 运行时不再把该函数作为卡点。
- 未达成（独立后续问题）：
  - demo 仍在退出路径出现 exceptional loop：
    - `current function: strchr`
    - `current caller function: exit`
    - `end pc: _exit`

## 可引用证据

- case 主文档: `doc/replacement_update_cases/case_01_loop_hang_lpuart_writeblocking.md`
- 运行日志: `testcases/server/nxp/NXP_FATFS_BareMetal/emulate/debug_output/lcmhal.txt`
- 历史 RU 示例:
  - `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_WriteBlocking_20260317181852.json`
