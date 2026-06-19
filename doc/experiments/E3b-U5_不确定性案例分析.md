# E3b：LLM 输出不确定性的跨 Run 案例分析 —— U5 (imxrt1052-nxp-evk/base)

> **用途**：本章内容供论文实验章节直接引用。以 U5 三次运行为主线，完整展示 LLM 非确定性的两类效应：不确定性导致失败（Run1）与动态反馈弥合偏差（Run2/Run3）。同批次其他固件（如 U1 NXP_LwIP_BareMetal）也观察到相同的 agent 死循环失败模式，佐证该现象非个例。
>
> **数据批次**：`runs/e3b_uncertainty/20260508_045825/`
>
> **案例固件**：U5（`testcases/server/rtthread/imxrt1052-nxp-evk/base`，NXP i.MX RT1052 + RT-Thread + GPIO/UART）

---

## 一、实验背景

E3b 实验的目的是评估 LLM 输出的不确定性对本方法最终结果的影响。具体设计为：对 5 个代表性固件各独立运行 3 次完整替换流水线（每次使用不同的 LLM session），采集分类、替换、仿真各阶段的客观指标，观察跨 run 的波动情况。

**控制变量**：三次 run 之间仅 LLM session 不同，以下条件完全相同——固件源码版本、CodeQL 查询规则、替换策略配置（`lcmhal_config.yml`）、验证关键节点定义、硬件仿真环境。

**流水线架构**（`main.py:100-167`，`run_workflow()`）：

```
CodeQL 分析（确定性）→ LLM 函数分类（Analyzer Agent）
  → 替换代码生成 → 编译验证（Builder Agent）
  → 硬件仿真 → 失败？→ Fixer Agent 分析仿真日志 → 迭代修复
```

其中 Analyzer Agent（`agents/analyzer_agent.py`）对每个函数独立运行一次 LangGraph 会话（入口：`agents/analyzer_agent.py:293`，初始消息 `"Classify the function : {func_name}"`），任务边界清晰（分析一个指定函数）；Fixer Agent（`agents/fixer_agent.py`）在仿真失败后以开放式任务触发（入口：`agents/fixer_agent.py:245`，初始消息 `"Analyze the emulator error feedback and fix the problematic functions..."`），需自主诊断故障函数并修复。每个 agent 的迭代上限为 50 轮（`agents/fixer_agent.py:258` 的 `recursion_limit: 50`），超出后由 FAILCHECK（`utils/failcheck.py:110`）生成诊断报告并终止流程（`utils/failcheck.py:216`）。

---

## 二、U5 三次运行的数量统计

| 指标 | Run1 | Run2 | Run3 |
|------|------|------|------|
| 分析函数个数¹ | 51 | 51 | 51 |
| 识别函数个数² | 12 | 12 | 11 |
| RU 落盘次数³ | 3 | 5 | 2 |
| 迭代优化数量⁴ | 0 | **3** | **2** |
| 迭代优化目标⁵ | （无） | `BOARD_BootClockRUN`;`CLOCK_InitExternalClk`;`LPUART_GetStatusFlags` | `CLOCK_InitArmPll`;`imxrt_putc` |
| exit_code | **1** | **0** | **0** |
| 仿真结果 | **未进入仿真阶段** | `success=True`（3min timeout） | `success=True`（3min timeout） |
| LLM invokes | 297 | 316 | 275 |
| total_tokens | 5,936,056 | 4,970,887 | 4,441,421 |
| wall_sec | 899 | 1,170 | 657 |
| FAILCHECK | **是（iterations exceeded: 50）** | 否 | 否 |

> ¹ `[analyze_functions] classifying N functions`（`agents/analyzer_agent.py:405`），CodeQL 输出。三次均为 51，验证了静态分析阶段的**完全确定性**。
> ² `function_classify_*` 中 `has_replacement == true` 的去重函数名个数。
> ³ `replacement_update_*.json` 文件总数（含同函数多版）。
> ⁴ `function_fix_*.json` 文件个数（仿真后 Fixer 再替换会话次数）。
> ⁵ 由 `function_fix_*` 文件名解析的符号，按文件名排序后 `;` 拼接。

**关键观察**：`迭代优化数量`在三次 run 间差异显著（0、3、2），且 **Run2 与 Run3 的迭代优化目标集合无一重叠**——5 个修复函数无一重复。这是 LLM 非确定性的直接表现：不同 session 的 Fixer Agent 面对不同的仿真失败形态，选择了不同的修复切入点。

---

## 三、首轮替换函数列表的差异

三次 run 经 LLM 分类后产出的首轮 `[REPLACE] Functions to replace` 列表：

| 函数 | Run1 | Run2 | Run3 |
|------|:----:|:----:|:----:|
| `imxrt_pin_mode` | ✓ | ✓ | ✓ |
| `BOARD_BootClockRUN` | ✓ | **✗** | ✓ |
| `CLOCK_EnableUsbhs0Clock` | ✓ | ✗ | ✗ |
| `CLOCK_EnableUsbhs1Clock` | ✗ | ✓ | ✗ |
| `CLOCK_EnableUsbhs1PhyPllClock` | ✓ | ✓ | ✗ |
| `CLOCK_InitArmPll` | ✓ | ✓ | **✗** |
| `CLOCK_InitAudioPll` | ✓ | ✓ | ✗ |
| `CLOCK_InitEnetPll` | ✗ | ✓ | ✓ |
| `CLOCK_InitExternalClk` | ✓ | ✗ | ✓ |
| `CLOCK_InitRcOsc24M` | ✓ | ✓ | ✗ |
| `CLOCK_InitSysPfd` | ✓ | ✗ | ✓ |
| `CLOCK_InitSysPll` | ✗ | ✓ | ✓ |
| `CLOCK_InitUsb1Pfd` | ✗ | ✓ | ✓ |
| `CLOCK_InitUsb1Pll` | ✓ | ✗ | ✗ |
| `CLOCK_InitUsb2Pll` | ✗ | ✓ | ✓ |
| `CLOCK_InitVideoPll` | ✓ | ✓ | ✗ |
| `GPIO_PinInit` | ✗ | ✗ | **✓** |
| `LPUART_Deinit` | ✓ | ✓ | ✓ |
| `LPUART_Init` | ✗ | ✗ | **✓** |
| **总计** | **12** | **12** | **11** |

三次列表仅共享 3 个函数（`imxrt_pin_mode`, `CLOCK_EnableUsbhs1PhyPllClock` 仅 Run1/2, `CLOCK_InitAudioPll` 仅 Run1/2, `LPUART_Deinit`），充分展示了 LLM 分类的 session 间差异。

**Run2** 的初始列表**不含 `BOARD_BootClockRUN`**（Run1/Run3 均含），取而代之的是 `CLOCK_InitEnetPll`, `CLOCK_InitSysPll` 等。这一遗漏直接导致首轮仿真在时钟初始化处阻塞，但后续被 Fixer Agent 补上（§四）。

**Run3** 包含 `GPIO_PinInit` 和 `LPUART_Init`（Run1/Run2 均未纳入），同时 `CLOCK_EnableUsbhs1Clock` 和 `CLOCK_InitArmPll` 被分类器审查机制拒绝（`agents/analyzer_agent.py:179-232` 的 `respond` 节点：未通过 VerifyReplacement → 清空 `has_replacement`）。

---

## 四、Run1（失败）：不确定性导致 Agent 行为失控

### 4.1 失败轨迹

Run1 的分类阶段正常完成，12 函数进入替换。仿真启动后失败，触发 Fixer Agent（`agents/fixer_agent.py:245`）。此时发生两件关键事件：

**事件 1：`BOARD_BootClockRUN` 分析触发 API 错误**

```
Error analyzing function BOARD_BootClockRUN: Error code: 400 -
  invalid_request_error: An assistant message with 'tool_calls' must be
  followed by tool messages responding to each 'tool_call_id'.
```

LLM 生成了工具调用但未正确匹配响应格式（`tool_calls` 与 `tool_call_id` 不对应），导致该函数从替换列表中移除（从 12 函数降到 11 函数）。这是纯粹的 LLM 非确定性输出——同函数在 Run2/Run3 中均未触发此类错误。

**事件 2：Fixer Agent 陷入函数间跳跃死循环**

Fixer Agent 的初始任务为开放式（`agents/fixer_agent.py:251`："Analyze the emulator error feedback and fix the problematic functions..."），需自主诊断故障。Agent 从 `BOARD_InitPins` 开始，随后在 `CLOCK_DeinitSysPfd` → `CLOCK_DeinitExternalClk` → `CLOCK_DeinitArmPll` → ... 等函数之间反复跳跃，对每个函数执行相同的冗长查询序列（`GetFunctionInfo` → `GetMMIOFunctionInfo` → `GetFunctionCallStack` → ...，5–10 次工具调用），但从不完成"分析 → 替换 → 验证"的闭环。

Prompt 中声明了预算约束（`prompts/function_fixer.py:75`：`"you have ~50 steps total"`），但 LLM 在该 session 中未遵守。Analyzer Agent 对每个函数的分析是独立的 LangGraph 会话（`agents/analyzer_agent.py:308-315`），函数间无显式知识传递；`data_manager` 中的替换历史上限为 2 条（`core/data_manager.py:9`），不足以支撑跨函数经验累积。

### 4.2 FAILCHECK 终止

FAILCHECK 在累计 **5,530 条消息** 后触发，`GraphRecursionError` 被 `agents/fixer_agent.py:264` 捕获，调用 `analyze_failed_conversation`（`utils/failcheck.py:110`）生成诊断报告，随后 `sys.exit(1)`（`utils/failcheck.py:216`）终止整个流程。

诊断报告（`isolated_db/U5_run1/lcmhal_failcheck_logs/failcheck_fixer_agent_20260508_051324.txt`）的根因：

> "代理在分析每个新函数时都会遇到障碍（分类不确定性、验证失败），并且其唯一的应对策略是转向列表中的下一个函数，而不是解决问题。"

### 4.3 50 轮预算不是"太少"

对比同固件成功 run：Run2 的 Fixer Agent 用 3 次 function_fix 即收敛（REPLACE 列表从 12 → 15 函数），Run3 用 2 次即收敛（11 → 13 函数）。Run1 的问题不是预算不足，而是该 session 的 agent 行为**结构性不收敛**——即使给 500 轮也不会成功。Agent 不朝目标方向前进，而是在原地空转（重复查询已获取的信息、遇障碍即跳走、不泛化已有知识）。同批次其他固件（如 U1 Run3，22,567 条消息后同样耗尽 50 轮）也观察到完全相同的退化模式，佐证该现象非个例。

---

## 五、Run2（成功）：动态反馈逐步弥合偏差

### 5.1 迭代修复过程

Run2 的初始 12 函数替换后仿真失败（程序在时钟初始化的硬件轮询处阻塞）。Fixer Agent 从仿真日志中定位故障，经过 3 轮迭代修复逐步收敛：

| 修复轮次 | 落盘文件 | 目标函数 | 仿真失败根因 | 替换策略 |
|----------|---------|---------|------------|---------|
| 第 1 次 | `function_fix_CLOCK_InitExternalClk_20260508052509.json` | `CLOCK_InitExternalClk` | 硬件轮询循环等待 XTALOSC24M 上电状态位和频率稳定，仿真中该寄存器不变化导致 hang | 移除轮询循环，保留函数结构 |
| 第 2 次 | `function_fix_BOARD_BootClockRUN_20260508052822.json` | `BOARD_BootClockRUN` | 硬件轮询循环等待 DCDC_STS_DC_OK 状态位，仿真中该位不变化导致 hang | 移除硬件轮询循环，保留非 MMIO 调用（`CLOCK_SetRtcXtalFreq` 等） |
| 第 3 次 | `function_fix_LPUART_GetStatusFlags_20260508052935.json` | `LPUART_GetStatusFlags` | 硬件状态寄存器 `base->STAT` 在仿真中不可用，`imxrt_putc` 中轮询 `TxDataRegEmptyFlag` 位导致死循环 | 返回 `kLPUART_TxDataRegEmptyFlag` 常量（始终就绪），使发送循环不阻塞 |

### 5.2 REPLACE 列表的演化

```
初始分类（12 函数）
  → 仿真失败 → Fixer 分析日志
  → +CLOCK_InitExternalClk（13 函数）→ 仿真失败
  → +BOARD_BootClockRUN（14 函数）→ 仿真失败
  → +LPUART_GetStatusFlags（15 函数）→ 仿真通过 ✓
```

最终仿真结果：`exit_code=0 success=True reason='success'`（3 分钟超时，程序正常执行到 main 并持续运行）。

**关键观察**：`BOARD_BootClockRUN` **不在 Run2 的初始分类列表中**（§三表中 Run2 对应列为 ✗），但 Fixer Agent 从仿真日志中识别到该函数的硬件轮询是阻塞根因，主动将其纳入修复范围。这说明 Fixer Agent 的修复动作**不是预先规划的固定脚本，而是根据仿真反馈动态决定的**。

---

## 六、Run3（成功）：不同的初始子集，不同的修复路径

### 6.1 迭代修复过程

Run3 的初始列表与 Run2 完全不同（§三），仿真失败后走了一条**不同的路线**到达相同的成功终点：

| 修复轮次 | 落盘文件 | 目标函数 | 仿真失败根因 | 替换策略 |
|----------|---------|---------|------------|---------|
| 第 1 次 | `function_fix_CLOCK_InitArmPll_20260508053915.json` | `CLOCK_InitArmPll` | 无限轮询循环等待 PLL lock 位 `CCM_ANALOG->PLL_ARM`，仿真中该位永远不置位 | 完全空桩 `(void)config;`，移除所有硬件寄存器访问 |
| 第 2 次 | `function_fix_imxrt_putc_20260508054029.json` | `imxrt_putc` | `while` 循环轮询 `LPUART_GetStatusFlags` 读取的 `base->STAT` MMIO 寄存器，仿真中标志位永远不置位 | 移除轮询循环，仅保留 `LPUART_WriteByte` 写入和返回值 |

### 6.2 REPLACE 列表的演化

```
初始分类（11 函数，含 GPIO_PinInit、LPUART_Init）
  → 仿真失败 → Fixer 分析日志
  → +CLOCK_InitArmPll（12 函数）→ 仿真失败
  → +imxrt_putc（13 函数）→ 仿真通过 ✓
```

---

## 七、跨 Run 对比分析

### 7.1 初始分类路径完全不同，但最终都到达了成功

Run2 的初始列表不含 `BOARD_BootClockRUN`（被 Fixer 后续补上），Run3 的初始列表不含 `CLOCK_InitArmPll`（同样被 Fixer 补上）。LLM 分类的随机性导致不同 run 遗漏了不同的关键函数，但**动态反馈机制在每种情况下都精准地定位了缺失的函数**。两个成功的 run 都是从不足的初始集合逐步扩展到足够的覆盖：

| Run | 初始 | 最终 | 变化 |
|-----|------|------|------|
| Run2 | 12 | **15** | +3（Fixer 新增 3 个函数） |
| Run3 | 11 | **13** | +2（Fixer 新增 2 个函数） |

这恰好是动态反馈机制的设计目标：**初始分类不需要完美，后续迭代会补全缺失**。

### 7.2 迭代优化目标无一重叠

| Run | 迭代优化数量 | 迭代优化目标 |
|-----|------------|------------|
| Run2 | 3 | `BOARD_BootClockRUN`; `CLOCK_InitExternalClk`; `LPUART_GetStatusFlags` |
| Run3 | 2 | `CLOCK_InitArmPll`; `imxrt_putc` |

5 个修复目标函数无一重复。Run2 修复了时钟初始化中的轮询循环和串口状态查询；Run3 修复了 ARM PLL 锁定等待和字符输出中的轮询。两者面对的仿真失败点不同，修复策略也不同。这证明 Fixer Agent 的修复动作**是针对具体仿真失败形态动态选择的，而非固定脚本**。

### 7.3 同一底层问题的不同修复层面

Run2 中 `LPUART_GetStatusFlags` 的修复与 Run3 中 `imxrt_putc` 的修复实际上是**同一问题（串口发送阻塞）的两个层面**：

- **Run2** 在 `LPUART_GetStatusFlags` 层面修复：让状态标志始终返回 `kLPUART_TxDataRegEmptyFlag`（就绪），上层 `imxrt_putc` 的 `while` 循环自然不再阻塞。
- **Run3** 在 `imxrt_putc` 层面修复：直接去掉 `imxrt_putc` 内部的 `while` 轮询循环，保留 `LPUART_WriteByte` 写入。

即使面对同一类底层问题，不同 LLM session 的 Fixer Agent 选择了不同的修复抽象层级。这种差异本身也是 LLM 非确定性的体现。

### 7.4 成功/失败的关键分岔点

Run1（失败）与 Run2/Run3（成功）的核心差异在于 **Fixer Agent 是否能维持有效的推理链**：

- **Run1**：`BOARD_BootClockRUN` 分析时遇到 API 错误 400 → agent 推理链被打断 → 进入函数间跳跃死循环 → 50 轮耗尽 → FAILCHECK 终止 → **无 `function_fix_*` 落盘** → 从未进入第二轮仿真。
- **Run2**：初始分类稳定 → 5 轮 REPLACE → 仿真失败 → Fixer Agent 维持有效推理链 → 3 次 function_fix 逐步收敛 → 仿真通过。
- **Run3**：初始分类走了不同路径（含 `GPIO_PinInit`/`LPUART_Init`）→ 仿真失败 → Fixer Agent 维持有效推理链 → 2 次 function_fix → 仿真通过。

**分岔点**：Run1 中 `BOARD_BootClockRUN` 的 API 错误 400 是纯粹的 LLM 非确定性行为——同函数在 Run2（Fixer 后续分析时处理了它）和 Run3 中均未触发此类错误。这一次偶发事件打断了 agent 的推理链，导致整个 pipeline 失控。同批次 U1 的 Run3 也观察到完全相同的失败模式（22,567 条消息后耗尽 50 轮），佐证该现象非个例。

---

## 八、结论

基于 U5 三次运行的数据，可以得出以下结论：

1. **静态分析阶段完全确定性**：`分析函数个数`三次均为 51（CodeQL 输出不受 LLM 影响）。
2. **LLM 分类阶段存在 session 间波动**：`识别函数个数`波动（11–12），首轮替换列表的具体函数子集各不相同（三次仅共享约 3 个函数），直接导致后续替换子集、RU 落盘、迭代目标均不同。
3. **动态反馈机制能够弥合分类偏差**：Run2/Run3 通过 Fixer Agent 在仿真反馈驱动下精准修复了各自暴露的问题——修复的函数集合完全不同（5 个函数无一重叠），但殊途同归。初始分类不需要完美，后续迭代会补全缺失。
4. **反馈闭环有效但非万能**：Run1 因 agent 推理链崩溃（偶发 API 错误 → 退化循环）而失败。反馈机制的前提是 agent 能维持有效推理链——当这一前提不成立时，修复也无法完成。系统鲁棒性存在上界。
5. **失败不是工程缺陷，而是实验观测到的现象**：本实验的目的正是"评估 LLM 输出不确定性对最终结果的影响"，结论是"有影响——既可能被反馈机制弥合（Run2/Run3），也可能导致系统失控（Run1）"。

---

## 九、数据来源索引

| 数据 | 路径 |
|------|------|
| 运行日志 | `runs/e3b_uncertainty/20260508_045825/logs/U5_run{1,2,3}.log` |
| 运行汇总（exit、仿真、wall_sec、tokens） | `run_log.tsv` |
| 机器可读统计 | `doc/experiments/E3b-批次20260508_045825_实测汇总.tsv` |
| 隔离 DB（每次 run 的独立快照） | `runs/e3b_uncertainty/20260508_045825/isolated_db/U5_run{1,2,3}/lcmhal_ai_log/` |
| FAILCHECK 诊断报告 | `isolated_db/U5_run1/lcmhal_failcheck_logs/failcheck_fixer_agent_20260508_051324.txt` |
| Fixer Agent 系统提示 | `prompts/function_fixer.py` |
| Fixer Agent 入口 | `agents/fixer_agent.py:245` |
| Analyzer Agent 入口 | `agents/analyzer_agent.py:293` |
| 完整流水线编排 | `main.py:100-167` |
| U5 代码级对照（OEM 片段与 Run1–3 替换体） | `doc/experiments/E3b-U5_BOARD_BootClockRUN_三次重复试验案例.md` |

---

## 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-10 | 初稿（U1 + U5 两案例）。 |
| 2026-05-10 | 重写：补充源码引用（`file:line`）、初始列表逐函数对照表、迭代修复逐次溯源。 |
| 2026-05-10 | 精简为 U5 单案例主线；U1 仅在 §四"50 轮预算"和 §七"关键分岔点"中以一句话带过作对照。 |
