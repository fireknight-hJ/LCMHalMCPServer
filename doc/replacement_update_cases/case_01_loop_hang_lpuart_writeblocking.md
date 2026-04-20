# Case 01 - Loop/Hang: `LPUART_WriteBlocking`

## 背景

- Demo: `nxp/NXP_FATFS_BareMetal`
- Function: `LPUART_WriteBlocking`
- 分类状态（触发 RU 时）:
  - `function_type=NA`
  - `has_replacement=false`
  - `in_baseline=false`
- 归类: `A_RU_only_not_replaced`（之前没换过，RU 新增覆盖）

## 触发问题

函数内存在硬件轮询等待（wait loop），在仿真环境里硬件标志位可能永远不满足，导致执行卡住或触发 exceptional loop。

## ReplacementUpdate 动作

- 去除/绕过硬件标志等待循环
- 保留接口行为，返回成功以保证流程继续

## 结果意义

- 这是典型的“卡住问题驱动替换”
- 属于覆盖增量案例：该函数原本不在 baseline 覆盖中，由 RU 补入

## 证据

- `replacement_update` 日志：`/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_WriteBlocking_20260317181852.json`
- 关键 reason 摘要：
  - “Avoid hardware wait loops in emulation... loops waiting for hardware flags may never be set...”

## 本轮修复闭环（2026-04-10）

### 1) 前因定位（为什么会出现 `function_type=NA`）

- 现象：在个别 RU 记录中看到 `function_type=NA`，同时存在 `replacement_update_*`。
- 解释：这里的 `NA` 不是 classifier 枚举值，语义是“该函数当次没有对应 `function_classify_*` 日志”，通常落在 `replacement_update_only_functions`。
- 这类情况不等于“函数不可分类”，只是日志链路并非 classify+RU 成对出现。

### 2) 静态分析差异（为什么该函数没进 mmio 候选）

- 对 `DATABASE_NXP_FATFS_BareMetal/lcmhal_tmp/mmio_info.json` 检查发现：
  - `LPUART_WriteBlocking` 在 `buffer_functions`；
  - 不在 `mmio_functions`；
  - `mmioinfo_mmioexpr_dict` 中没有该函数条目。
- 结论：该函数虽有明显寄存器轮询语义，但在当时候选构建中被归到 buffer 侧，导致 mmio 候选链路漏入。

### 3) 代码修复（全局开关，默认开启）

- 修改 `config/globs.py`：
  - 新增/启用 `enable_buffer_functions_as_mmio = True`（默认开启）。
- 修改 `tools/collector/collector.py`：
  - `get_mmio_func_list(db_path)` 由仅返回 `mmio_functions`，改为按开关合并
    `mmio_functions ∪ buffer_functions`，并做去重排序。
- 效果验证：
  - 开关开启时，NXP FATFS BareMetal 的 mmio 候选数量从 65 提升到 72；
  - `LPUART_WriteBlocking` 已出现在候选列表中。

### 4) 清理与复验动作

- 清理历史 RU 和 testcase 侧统计，避免旧结果污染：
  - 删除 DB 侧 `replacement_update_*.json`（相关函数）；
  - 删除 testcase 侧 `classify_stats_output.json`、`classify_stats.json`、`replacement_log.md`。
- 单函数复验：
  - `python main.py analyze testcases/server/nxp/NXP_FATFS_BareMetal --func-name LPUART_WriteBlocking`
  - 得到 classifier 结果：`function_type=LOOP`，`has_replacement=true`。

### 5) 运行期验证结论

- 复跑 `python main.py run testcases/server/nxp/NXP_FATFS_BareMetal` 后，替换链路包含
  `LPUART_WriteBlocking`，且替换落地成功（replace 成功计数正常）。
- `lcmhal.txt` 运行轨迹显示持续经过 `DbgConsole_Putchar -> HAL_UartSendBlocking`，
  说明已不再停在 `LPUART_WriteBlocking` 的硬件等待轮询。
- 当前剩余阻塞点转移为退出路径 exceptional loop：
  - `current function: strchr`
  - `current caller function: exit`
  - `end pc: _exit`

## 本案例当前结论

- `LPUART_WriteBlocking` 这一函数本身的修复目标已达成（分类与替换链路正确、运行不再卡在该函数）。
- 但 demo 端到端仍有独立问题（`exit/_exit/strchr` 路径 exceptional loop），应作为后续案例单独处理。
