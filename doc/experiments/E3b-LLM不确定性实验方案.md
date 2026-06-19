# E3b LLM输出不确定性实验方案

## 创建时间：2026-05-06

---

## 一、实验目的

评估LLM输出的不确定性对本文方法最终结果的影响。具体回答：同一个固件多次经过完整的替换流程，最终仿真结果是否稳定收敛？

---

## 二、实验设计

### 2.1 样本选取

从5.4节已完成替换功能正确性验证的14个测试用例中，选取5个代表性固件。选取原则为覆盖不同平台、操作系统、外设类型和驱动复杂度梯度。

| 编号 | 固件名称 | 平台 | OS | 外设类型 | 识别数 | 替换数 | 迭代数 | 选样理由 |
|------|---------|------|-----|---------|--------|--------|--------|---------|
| U1 | NXP\_LwIP\_BareMetal | NXP | 裸机 | ETH | 105 | 61 | 20 | 中等复杂度，已有5.4.3节详细案例分析 |
| U2 | NXP\_I2C\_BareMetal | NXP | 裸机 | I2C | 104 | 50 | 45 | 迭代次数最多（45次），不确定性应最大 |
| U3 | LwIP\_StreamingServer（Cube：LwIP Streaming Server；testcase：`testcases/server/stm32/LwIP_StreamingServer`） | STM32 | FreeRTOS | ETH（LwIP TCP streaming） | 281 | 161 | 15 | STM32F4 + FreeRTOS + LwIP，与 U1 同属 LwIP/网络类；**识别数** = `classify_stats.json` 的 `total_functions`；**替换数** = 各类型 `counts_has_replacement.*.true` 之和（与 U1 同口径）；**迭代数** = 当前 `DATABASE_LwIP_StreamingServer` 下 `function_fix_*.json` 个数（单次流水线快照；三连跑后以各 run 的 isolated\_db 为准）。历史批次 §8.2 仍保留 `stm32f401-st-nucleo/eth` 三行作对照 |
| U4 | UART\_Hyperterminal\_IT | STM32 | FreeRTOS | UART | 120 | 87 | 8 | 高替换数但低迭代数，FreeRTOS+中断驱动 |
| U5 | imxrt1052-nxp-evk | NXP | RT-Thread | GPIO | 53 | 34 | 18 | GPIO类代表，基础外设场景 |

**覆盖情况**：
- 平台：NXP ×3、STM32 ×2
- 操作系统：裸机 ×2、FreeRTOS ×2、RT-Thread ×1
- 外设类型：ETH ×2、I2C ×1、UART ×1、GPIO ×1
- 迭代复杂度：8 ~ 45次，覆盖低/中/高三档

### 2.2 重复次数

每个固件独立运行 **n=3** 次（3个不同的LLM session）。

选择n=3的理由：
1. 单次完整替换流程耗时较长（LLM分析+生成+反馈闭环），n=3已能反映稳定性趋势
2. Agent领域通行做法（WebArena、SWE-bench多run实验）均采用n=3
3. n=5以上边际收益小，但计算成本为原来的5/3倍

### 2.3 实验条件

- **LLM模型**：DeepSeek V3.2（与主实验一致）
- **temperature**：使用系统固定配置（与主实验一致，不做temperature变量实验）
- **测试固件源码**：与主实验完全相同的版本
- **验证标准**：与5.4节一致——关键节点命中率100%即为通过
- **每次运行**：使用全新的LLM session（清除上下文缓存），确保独立性

### 2.4 控制变量

每次运行之间仅LLM session不同，以下条件保持不变：
- 固件源码版本
- CodeQL查询规则
- 替换策略配置
- 验证关键节点定义
- 硬件仿真环境

---

## 三、数据采集

### 3.1 采集指标

每次运行记录以下数据：

| 指标 | 说明 | 来源 |
|------|------|------|
| 驱动函数识别数 | 静态分析识别的驱动函数总数 | CodeQL输出 |
| 替换代码生成数 | 实际生成替换代码的函数数 | 替换模块日志 |
| 迭代修复次数 | 反馈闭环触发的迭代修复总次数 | 反馈闭环日志 |
| 关键节点命中率 | 预设关键节点被执行到的比例 | 仿真执行日志 |
| 仿真通过/失败 | 关键节点命中率是否为100% | 仿真执行日志 |
| LLM词元消耗 | 本次运行的总token数 | LLM调用日志 |
| 总处理时长 | 从开始到结束的wall time | 系统日志 |

### 3.2 额外分析（可选）

选1-2个固件（建议U1和U2），额外采集：
- **分类一致性**：同一函数在3次运行中被分为相同类别的比例
- **替换代码差异**：选2-3个代表性函数，对比3次运行生成的替换代码差异

---

## 四、结果呈现

### 4.1 主表格式

建议新增一个表格，放在5.6节末尾或作为5.6节的新小节（"LLM输出稳定性分析"）：

```
表：LLM输出稳定性分析结果

| 固件 | Run | 识别数 | 替换数 | 迭代数 | 关键节点命中率 | 通过 |
|------|-----|--------|--------|--------|--------------|------|
| U1   | 1   |        |        |        |              |      |
|      | 2   |        |        |        |              |      |
|      | 3   |        |        |        |              |      |
| U2   | 1   |        |        |        |              |      |
| ...  |     |        |        |        |              |      |
| 汇总 | -   | -      | -      | 均值±标准差 | -      | x/15 |
```

### 4.2 分析要点

1. **最终结果稳定性**：15次运行（5×3）中有多少次通过验证，汇总成功率
2. **中间过程波动**：迭代次数的均值±标准差（如 14.7 ± 3.2），说明中间过程可能不同但最终收敛
3. **识别数稳定性**：3次运行的驱动函数识别数是否一致（CodeQL是确定性的，应该完全一致，作为sanity check）
4. **收敛保障机制**：如果不一致，说明反馈闭环如何弥合差异，引用E3c中的不确定性缓解机制说明

---

## 五、预期结论

1. 驱动函数识别数在3次运行中完全一致（CodeQL是确定性工具）
2. 替换代码生成数可能有小幅波动（LLM分类判断存在不确定性）
3. 迭代次数可能波动，但最终均收敛到通过状态
4. 结论：LLM输出的不确定性影响中间过程但不影响最终结果，系统的多层验证与反馈闭环机制有效保障了结果稳定性

---

## 六、执行步骤

1. 准备5个固件的干净工程副本（确保源码与主实验一致）
2. 对每个固件，依次执行3次完整的替换流程（每次新建LLM session）
3. 采集每次运行的日志数据
4. 汇总数据，填入结果表格
5. 撰写分析段落，写入 `body/chap05_experiment.tex`

---

## 七、注意事项

- 如果某次运行出现失败（关键节点未100%命中），如实记录，不要丢弃。失败样本反而能说明不确定性的实际影响程度
- 如果出现失败，分析原因：是LLM分类错误导致、还是替换代码生成质量不足、还是反馈闭环未收敛
- 实验前确认LLM API调用无速率限制，避免因限流导致session异常
- **重复次数不足时**：不得以推测或「捏数据」冒充额外 Run 的实测列（识别/RU/迭代/tokens 等）。应改为减小 **n**、表格留空并脚注，或把该固件移出「跨 session 波动」结论范围

---

## 八、批次实测汇总（`runs/e3b_uncertainty/20260508_045825`）

本批已于仓库内跑满 **5×3=15** 次；机器可读汇总见 [`E3b-批次20260508_045825_实测汇总.tsv`](./E3b-批次20260508_045825_实测汇总.tsv)。表内只保留**前期分析替换**与**后期仿真反馈再替换**两条数量线（+ LLM 消耗列）；**exit / 仿真是否成功 / 末轮 REPLACE 行**请查同批 [`run_log.tsv`](../../runs/e3b_uncertainty/20260508_045825/run_log.tsv) 与各 `logs/U*_run*.log`。**§2.1 旧「识别数」**已弃用：现 **分析函数个数** = `classifying N` 的 N；**识别函数个数** = 分类子图采纳 `has_replacement` 的去重函数数。

**U3 固件说明（与本表区分）**：下列 **§8.2 主表中 U3 三行**仍为历史 **`stm32f401-st-nucleo/eth`**。正文若采用 **§2.1** 更新后的 U3（`LwIP_StreamingServer`），请另跑三连并用 `tools/e3b_batch_replacement_stats.py` 写新 TSV；自动化复原 DB + 工程 + 三连命令见 **`scripts/e3b_u3_lwip_streaming_server_triple_run.sh`**（**运行前**须 `export E3B_U3_CONFIRM=yes`）。HTTP Socket RTOS 版三连脚本仍保留为 **`scripts/e3b_u3_lwip_http_socket_rtos_triple_run.sh`**（仅当仍要以该 demo 复现实验时使用）。产出目录形如 `runs/e3b_uncertainty/<时间戳>_U3_LwIP_StreamingServer/`。

**若实在无法为 StreamServer 再跑两轮**：不要编造 Run2/Run3 的数字。可任选其一写进正文：**(1)** 明确 U3 子实验 **n=1**，扩展表里 Run2/Run3 用「—」并脚注「未重复 LLM session」；**(2)** 跨 run 波动仅讨论 §8.2 中已有四固件（或保留历史 eth 三行作 **U3** 波动例证，同时在 §2.1 注明正文样本与 §8.2 该三行 **demo 不一致**）；**(3)** U3 只报告 §2.1 静态规模（`classify_stats.json` / 当前 DB 日志），不参与「三次是否一致」的统计。

### 8.1 指标口径（与 TSV 列名一致）

| 列名 | 含义 | 来源 |
|------|------|------|
| 分析函数个数 | `[analyze_functions] classifying N` 的 **N** | `logs/U*_run*.log` |
| 识别函数个数 | `function_classify_*` 中 **`final_response.has_replacement == true`** 的去重函数名个数 | `isolated_db/.../lcmhal_ai_log/` |
| RU落盘次数 | `replacement_update_*.json` **文件数**（前期链上 `UpdateFunctionReplacement` 成功落盘，含同函数多版） | 同上 |
| 迭代优化数量 | `function_fix_*.json` **文件数**（仿真后 Fixer 再替换会话次数；**数值与旧版「动态修复会话次数」相同**） | 同上 |
| 迭代优化目标 | 由上述文件名解析的符号，按文件名排序后 `;` 拼接（便于对账） | 同上 |
| invokes / total_tokens / wall秒 | 与 `run_log.tsv` 一致 | `run_log.tsv` |

**复算**：`python3 tools/e3b_batch_replacement_stats.py --isolated-db-root runs/e3b_uncertainty/20260508_045825/isolated_db --summary-tsv doc/experiments/E3b-批次20260508_045825_实测汇总.tsv`

### 8.2 主表（15 次）

与 TSV 同源（制表可直接嵌入 TSV）。

| ID | testcase（相对仓库根） | Run | 分析 | 识别 | RU落盘 | 迭代优化（次） | 迭代优化目标（摘） | invokes | tokens | wall（s） |
|----|-------------------------|-----|------|------|--------|----------------|---------------------|---------|--------|-----------|
| U1 | `testcases/server/nxp/NXP_LwIP_BareMetal` | 1 | 235 | 50 | 3 | 0 |  | 2367 | 39954947 | 8832 |
| U1 | 同上 | 2 | 235 | 47 | 4 | 1 | __assert_func | 2018 | 33350922 | 6852 |
| U1 | 同上 | 3 | 235 | 50 | 1 | 0 |  | 1922 | 32116651 | 6248 |
| U2 | `testcases/server/nxp/NXP_I2C_BareMetal` | 1 | 109 | 33 | 5 | 0 |  | 1801 | 31203393 | 4632 |
| U2 | 同上 | 2 | 109 | 47 | 4 | 0 |  | 1615 | 29093022 | 3893 |
| U2 | 同上 | 3 | 109 | 32 | 7 | 0 |  | 1862 | 34200829 | 5074 |
| U3 | `testcases/server/stm32/LwIP_StreamingServer` | 1 | 281 | 161 | 21 | 15 | DP83848_GetLinkState;HAL_ETH_Init;HAL_RCCEx_PeriphCLKConfig | 2653 | 48479215 | 10238 |
| U3 | 同上 | 2 | 281 | 148 | 18 | 12 | HAL_ETH_MspInit;HAL_RCCEx_PeriphCLKConfig;MX_LWIP_Init | 2381 | 43128603 | 8917 |
| U3 | 同上 | 3 | 281 | 155 | 24 | 17 | DP83848_GetLinkState;HAL_ETH_Start_IT;HAL_RCCEx_PeriphCLKConfig | 2784 | 51163427 | 11503 |
| U4 | `testcases/server/stm32/UART_Hyperterminal_IT` | 1 | 170 | 121 | 1 | 0 |  | 1657 | 30936827 | 4877 |
| U4 | 同上 | 2 | 170 | 106 | 0 | 0 |  | 1067 | 19982273 | 2341 |
| U4 | 同上 | 3 | 170 | 112 | 6 | 0 |  | 1025 | 18934364 | 2286 |
| U5 | `testcases/server/rtthread/imxrt1052-nxp-evk/base` | 1 | 51 | 12 | 3 | 0 |  | 297 | 5936056 | 899 |
| U5 | 同上 | 2 | 51 | 12 | 5 | 3 | BOARD_BootClockRUN;CLOCK_InitExternalClk;LPUART_GetStatusFlags | 316 | 4970887 | 1170 |
| U5 | 同上 | 3 | 51 | 11 | 2 | 2 | CLOCK_InitArmPll;imxrt_putc | 275 | 4441421 | 657 |

**客观汇总**（exit/仿真见 `run_log.tsv`）：**分析函数个数**同固件三次内不变；**识别**、**RU落盘**、**迭代优化数量**均有 run 间波动（如 U3：识别 148–161，迭代优化 12–17；U5 迭代优化：0→3→2；U4 RU落盘：0→6→1）。

#### 8.2.1 同一 demo、某次未在仿真反馈阶段修某函数、另一次修到了（佐证第三阶段兜底）

以 **`function_fix_<函数名>_*.json` 是否落盘** 为准（与 **迭代优化数量** / Fixer 会话一致）：

1. **U3（`LwIP_StreamingServer`）— `DP83848_GetLinkState`**  
   - **Run1、Run3**：存在 `function_fix_DP83848_GetLinkState_*.json`。  
   - **Run2**：**无**对该函数的 `function_fix_*`；迭代优化会话涉及 `HAL_ETH_MspInit`、`MX_LWIP_Init` 等。  
   - **原因说明**：Run2 首轮待替换函数子集不同，`DP83848_GetLinkState` 未在该次 LLM 分类中被采纳为 `has_replacement`，自然也不会产生针对该函数的 `function_fix` 落盘。**分类/采纳路径不同 → 替换子集不同 → 动态阶段被点名的函数不同**。`HAL_RCCEx_PeriphCLKConfig` 在三次 run 中均有 `function_fix_*` 落盘，说明该函数被多次替换但反复触发仿真失败。

2. **U5（imxrt1052-nxp-evk/base）— 与 Run1 对照**  
   - **Run1**：迭代优化 **0**（无任何 `function_fix_*`）。  
   - **Run2**：**3** 次会话，涉及 `BOARD_BootClockRUN`、`CLOCK_InitExternalClk`、`LPUART_GetStatusFlags`。  
   - **Run3**：**2** 次会话，涉及 `CLOCK_InitArmPll`、`imxrt_putc`（与 Run2 **集合不同**）。  
   即：同一 demo 下，**有的重复完全未进入函数级 Fixer 落盘**，**有的重复**则对**不同子集**的驱动函数触发修复——可支撑「兜底不是固定脚本，而是随失败形态变化」。

明细与路径见 [`E3b-批次20260508_045825_实测汇总.tsv`](./E3b-批次20260508_045825_实测汇总.tsv) 的 **迭代优化目标** 列。

### 8.3 与 §五「预期结论」的对照（供讨论节使用）

本次数据**不支持**「15 次均在关键节点意义上全部通过」的强结论；更宜写为：**识别锚定稳定**，**替换规模与 LLM 消耗、终点 exit/仿真日志在 run 间波动**，部分固件（U1、U5）存在 **成功/失败混排**，其余三次均未出现仿真成功行——与「不确定性 + 预算/验证边界」并列讨论一致。
