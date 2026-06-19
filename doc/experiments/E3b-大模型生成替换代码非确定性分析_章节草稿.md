# E3b：大模型生成替换代码的非确定性（章节草稿）

> **用途**：供 `chap05` 扩写「多次运行 / 日志与代码对照 / 反馈闭环」小节。节号 **5.x** 定稿时按正文编号替换。  
> **数据批次**：`runs/e3b_uncertainty/20260508_045825/`（15 次已齐）；与 [`E3b-批次20260508_045825_实测汇总.tsv`](./E3b-批次20260508_045825_实测汇总.tsv)、`run_log.tsv` 一致。**U3** 在 §2.1 现为 **`LwIP_StreamingServer`**（Cube **LwIP Streaming Server**）；本草稿表格中 **U3 三行仍为历史 `stm32f401-st-nucleo/eth`**，新 U3 三连跑见 [`E3b-LLM不确定性实验方案.md`](./E3b-LLM不确定性实验方案.md) §八首段及 `scripts/e3b_u3_lwip_streaming_server_triple_run.sh`。

---

## 与第 5.4 节的关系

本节**不重复**单次正确性证明，只回答：**同一输入配置下多次完整流水线**，客观数量与日志可观测终点**是否稳定**。**关键节点命中率 100%** 的细判据仍以 5.4 为准；**表 5-x 不列 exit/仿真**（与 REPLACE 末轮行一并见 `run_log.tsv` 与各 `logs/U*_run*.log`）。

---

### 5.x.3 客观数量统计

**表 5-x 各次运行数量统计（15 行）** — 与 [`E3b-批次20260508_045825_实测汇总.tsv`](./E3b-批次20260508_045825_实测汇总.tsv) **同源同值**（列名与实验方案 §8.2 一致；宽表在正文可拆行或转置）。

| 固件 | testcase（简） | Run | 分析¹ | 识别² | RU落盘³ | 迭代优化⁴ | 迭代目标（摘）⁵ | invokes⁶ | tokens⁶ | wall⁶ |
|------|-----------------|-----|-------|-------|---------|-----------|----------------|----------|---------|-------|
| U1 | NXP_LwIP_BareMetal | 1 | 235 | 50 | 3 | 0 |  | 2367 | 39954947 | 8832 |
| U1 | NXP_LwIP_BareMetal | 2 | 235 | 47 | 4 | 1 | __assert_func | 2018 | 33350922 | 6852 |
| U1 | NXP_LwIP_BareMetal | 3 | 235 | 50 | 1 | 0 |  | 1922 | 32116651 | 6248 |
| U2 | NXP_I2C_BareMetal | 1 | 109 | 33 | 5 | 0 |  | 1801 | 31203393 | 4632 |
| U2 | NXP_I2C_BareMetal | 2 | 109 | 47 | 4 | 0 |  | 1615 | 29093022 | 3893 |
| U2 | NXP_I2C_BareMetal | 3 | 109 | 32 | 7 | 0 |  | 1862 | 34200829 | 5074 |
| U3 | LwIP_StreamingServer | 1 | 281 | 161 | 21 | 15 | DP83848_GetLinkState;HAL_ETH_Init;HAL_RCCEx_PeriphCLKConfig | 2653 | 48479215 | 10238 |
| U3 | LwIP_StreamingServer | 2 | 281 | 148 | 18 | 12 | HAL_ETH_MspInit;HAL_RCCEx_PeriphCLKConfig;MX_LWIP_Init | 2381 | 43128603 | 8917 |
| U3 | LwIP_StreamingServer | 3 | 281 | 155 | 24 | 17 | DP83848_GetLinkState;HAL_ETH_Start_IT;HAL_RCCEx_PeriphCLKConfig | 2784 | 51163427 | 11503 |
| U4 | UART_Hyperterminal_IT | 1 | 170 | 121 | 1 | 0 |  | 1657 | 30936827 | 4877 |
| U4 | UART_Hyperterminal_IT | 2 | 170 | 106 | 0 | 0 |  | 1067 | 19982273 | 2341 |
| U4 | UART_Hyperterminal_IT | 3 | 170 | 112 | 6 | 0 |  | 1025 | 18934364 | 2286 |
| U5 | imxrt1052…/base | 1 | 51 | 12 | 3 | 0 |  | 297 | 5936056 | 899 |
| U5 | imxrt1052…/base | 2 | 51 | 12 | 5 | 3 | BOARD_BootClockRUN;CLOCK_InitExternalClk;LPUART_GetStatusFlags | 316 | 4970887 | 1170 |
| U5 | imxrt1052…/base | 3 | 51 | 11 | 2 | 2 | CLOCK_InitArmPll;imxrt_putc | 275 | 4441421 | 657 |

**脚注**  
1. **分析函数个数**：`[analyze_functions] classifying N functions` 的 N。  
2. **识别函数个数**：`function_classify_*` 落盘中 **`final_response.has_replacement == true`** 的不同函数名个数。  
3. **RU落盘次数**：`replacement_update_*.json` 文件总数（前期链上落盘，含同函数多版）。  
4. **迭代优化数量**：`function_fix_*.json` 文件个数（仿真反馈后再替换；**与旧表「动态修复会话次数」同数**）。  
5. **迭代优化目标**：由 `function_fix_*` 文件名解析的符号串（对账用）。  
6. 与 `run_log.tsv` 中 `[LLM Usage]`、`wall_sec` 一致。**exit / 仿真成功 / 末轮 REPLACE** 见 `run_log.tsv` 与 `logs/U*_run*.log`。

**一句汇总**：**exit=0 且仿真成功：4/15**（见 `run_log.tsv`）；**分析函数个数**同固件三次内不变；**识别**、**RU落盘**、**迭代优化数量**均有 run 间波动。

**第三阶段兜底（跨 run 谁被修）**：**U3（`LwIP_StreamingServer`）** 下，`DP83848_GetLinkState` 在 **Run1、Run3** 有 `function_fix_DP83848_GetLinkState_*.json`，**Run2 无**（Run2 的 `function_fix_*` 涉及 `HAL_ETH_MspInit`、`MX_LWIP_Init` 等）。`HAL_RCCEx_PeriphCLKConfig` 在三次 run 中均有 `function_fix_*` 落盘，但次数各异。同 demo **U5** 下 **Run1** 无任意 `function_fix_*`，**Run2/Run3** 各有 **3、2** 次且**目标函数集合不同**。详见 [E3b-LLM不确定性实验方案.md §8.2.1](./E3b-LLM不确定性实验方案.md)。

---

### 5.x.4 函数级对照（抽样）

**表 5-x+1（示例，可增删）**

| 固件 | 函数 | 理由 |
|------|------|------|
| U5 | `imxrt_pin_mode` | U5_run2 有两次 `replacement_update_imxrt_pin_mode_*.json`（`reason` 指向 LOG_D/转义修正）；U5_run3 **无**该 `replacement_update` 落盘仍 exit=0；跨 run 与**同 run 内迭代**均可用。 |
| U3 | （Fixer 超限） | 三次迭代优化数量分别为 15、12、17（`function_fix_*` 文件数），识别函数 148–161 波动；`HAL_RCCEx_PeriphCLKConfig` 三次均被修但未收敛，作闭环预算边界例。 |

**代码级对照（U5 `BOARD_BootClockRUN`）**：OEM 片段与 Run1–3 替换体逐字摘录见 [E3b-U5_BOARD_BootClockRUN_三次重复试验案例.md](./E3b-U5_BOARD_BootClockRUN_三次重复试验案例.md) **§八** 与 `doc/experiments/snippets/U5_*.c`；可由 `python3 tools/extract_u5_board_snippets.py` 从批次 `isolated_db` 再生。

---

### 5.x.5 正面例：反馈修正（U5，`imxrt_pin_mode`，Run2）

证据：`isolated_db/U5_run2/lcmhal_ai_log/replacement_update_imxrt_pin_mode_20260508052109.json` → `…052324.json`。第二次 `reason` 写明去掉格式串中 `\n` 以规避转义问题；该 run **exit=0** 且日志含 **Emulate success=True**。

---

### 5.x.6 边界例：未在预算内收敛（U3）

三次 **exit=1**，未见仿真成功行；与 U5 的「部分 run 成功」对照，说明**反馈闭环不保证**有限资源内总收敛。

---

### 5.x.7 综合讨论（据本批数据）

**（1）数量**：**分析函数个数**（`classifying N`）在**同固件三次内稳定**；**识别**、**RU落盘**、**迭代优化数量**与 LLM 消耗均可**波动**；**4/15** 达到 exit=0 且仿真日志成功（见 `run_log.tsv`）。  
**（2）实现**：`replacement_update_*`（前期）与 **`function_fix_*`（后期迭代优化）** 触达函数集合均**因 run 而异**（见 §5.x.3 脚注与实验方案 §8.2.1）。  
**（3）机制**：扰动可被迭代吸收（§5.x.5），也可与步数/验证耦合导致失败（§5.x.6）；**鲁棒性有上界**。  
**（4）局限**：n=3；仿真成功行 ≠ 5.4 全量关键节点；案例为解释性抽样。

---

## 与全文衔接

- **5.4**：单次正确性；**本节**：多次统计 + 对照 + 讨论。  
- **执行路径**：[E3b-LLM不确定性实验方案.md §八](./E3b-LLM不确定性实验方案.md)、[E3b-LLM不确定性实验执行手册.md](./E3b-LLM不确定性实验执行手册.md)（若存在）。

---

## 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-08 | 初稿骨架。 |
| 2026-05-08 | 全批 15 行表与 U3/U5 案例；与 `20260508_045825` 对齐。 |
| 2026-05-08 | 表列改为「末轮成功替换个数」+「动态修复会话数」；§8.2.1 跨 run `function_fix` 例证写入方案并互链。 |
| 2026-05-08 | 与 TSV 对齐：列名改为分析/识别等中文；表 5-x 数值与 `E3b-批次…实测汇总.tsv` 同源。 |
| 2026-05-08 | 合并 RU 相关列：仅保留 **RU落盘次数**（含同函数多轮）；**动态修复**单列保留，与 RU 分源说明。 |
| 2026-05-08 | 表列再瘦：末轮/exit/仿真移出主表；**迭代优化数量**=原 `function_fix_*` 个数；**迭代优化目标**对账。 |
| 2026-05-08 | §5.x.4 增加 U5 `BOARD_BootClockRUN` 与案例文档 §八、`snippets/`、`extract_u5_board_snippets.py` 互链。 |
| 2026-05-07 | §2.1 U3 定为 `LwIP_StreamingServer`（`classify_stats.json` / 三连 `e3b_u3_lwip_streaming_server_triple_run.sh`）；本草稿首段与 §5.x.3 脚注同步；HTTP Socket RTOS 三连脚本仍保留作备选。 |
