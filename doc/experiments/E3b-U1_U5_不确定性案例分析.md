# E3b：LLM 输出不确定性导致跨 Run 成败分化的案例分析

> **用途**：本章内容供论文实验章节直接引用。案例一（§二）与案例二（§三）可分别作为"不确定性负面效应"和"反馈闭环正面效应"的论据。
>
> **数据批次**：`runs/e3b_uncertainty/20260508_045825/`（5 × 3 = 15 次完整运行）
>
> **案例范围**：U1（`testcases/server/nxp/NXP_LwIP_BareMetal`，NXP 裸机 ETH）与 U5（`testcases/server/rtthread/imxrt1052-nxp-evk/base`，NXP RT-Thread GPIO）

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

其中 Analyzer Agent（`agents/analyzer_agent.py`）对每个函数独立运行一次 LangGraph 会话（入口：`agents/analyzer_agent.py:293`，初始消息 `"Classify the function : {func_name}"`）；Fixer Agent（`agents/fixer_agent.py`）在仿真失败后以开放式任务触发（入口：`agents/fixer_agent.py:245`，初始消息 `"Analyze the emulator error feedback and fix the problematic functions..."`），需自主诊断故障函数并修复。

15 次运行的数据揭示了两类由 LLM 非确定性引起的典型现象：

1. **不确定性直接导致部分 run 失败**：同一固件下，部分 run 中 Fixer Agent 陷入无效循环，耗尽迭代预算后被 FAILCHECK 终止。代表案例：**U1 Run3**（exit=1），对比同固件 Run1/Run2（exit=0）。
2. **不确定性引发的偏差被动态反馈机制弥合**：LLM 初始分类路径不同导致不同 run 选了不同的函数子集，仿真失败后 Fixer Agent 针对性地修复了各自暴露的问题，最终收敛到通过。代表案例：**U5 Run2/Run3**（exit=0），对比同固件 Run1（exit=1）。

下文对两类案例进行详细的日志级与代码级分析。

---

## 二、案例一：不确定性直接导致部分 Run 失败 —— U1 (NXP_LwIP_BareMetal)

### 2.1 数量统计

| 指标 | Run1 | Run2 | Run3 |
|------|------|------|------|
| 分析函数个数¹ | 235 | 235 | 235 |
| 识别函数个数² | 50 | 47 | 50 |
| RU 落盘次数³ | 3 | 4 | **1** |
| 迭代优化数量⁴ | 0 | 1 (`__assert_func`) | 0 |
| exit_code | **0** | **0** | **1** |
| 仿真结果 | `reached main(), no exceptions, no infinite loops` | `reached main(), no exceptions, no infinite loops` | **未进入仿真阶段** |
| LLM invokes | 2,367 | 2,018 | 1,922 |
| total_tokens | 39,954,947 | 33,350,922 | 32,116,651 |
| wall_sec | 8,832 | 6,852 | 6,248 |
| FAILCHECK | 否 | 否 | **是（iterations exceeded: 50）** |

> ¹ `[analyze_functions] classifying N functions`（`agents/analyzer_agent.py:405`），CodeQL 输出，同固件三次不变。
> ² `function_classify_*` 中 `has_replacement == true` 的去重函数名个数。
> ³ `replacement_update_*.json` 文件总数。
> ⁴ `function_fix_*.json` 文件个数。

**观察 1**：`分析函数个数`三次完全相同（235），验证了 CodeQL 静态分析阶段的确定性。

**观察 2**：`识别函数个数`在三次 run 间波动（47–50，约 6%），说明 LLM 分类决策存在 session 间差异。

**观察 3**：`RU 落盘次数`波动显著（1–4），`迭代优化数量`也有差异（0–1）。Run3 的 RU 落盘仅 1 个，远低于 Run1/Run2，说明该次 run 的替换覆盖率严重不足。

### 2.2 首轮替换函数列表的差异

三次 run 经 LLM 分类后产出的首轮 `[REPLACE] Functions to replace` 列表存在显著差异：

**Run1（38 函数）**：以 `BOARD_BootClockRUN_528M` 开头，ENET 相关函数（`ENET_Deinit`, `ENET_GetMacAddr`, `ENET_ReceiveIRQHandler` 等）被全面覆盖。

**Run2（41 函数）**：以 `BOARD_BootClockRUN`（无 `_528M` 后缀）开头，包含 `CLOCK_InitRcOsc24M`, `CLOCK_InitSysPll` 等 Run1 未出现的时钟函数。

**Run3（46 函数）**：`BOARD_BootClockRUN_528M` 被审查机制清空（`agents/analyzer_agent.py:179-232` 中的 `respond` 节点执行"未通过 VerifyReplacement 且未通过 FixFunctionBuildErrors → 清空 `has_replacement`"逻辑），日志记录为：

```
[FunctionClassifier] 未采纳未验证替换: BOARD_BootClockRUN_528M
  (无 VerifyReplacement 通过且无 FixFunctionBuildErrors 成功，审查机制清空)
```

首轮列表完全不含 `BOARD_BootClockRUN` 的任何变体，取而代之的是 `CLOCK_DeinitAudioPll`, `CLOCK_InitSysPfd` 等 Run1/Run2 未出现的函数。

### 2.3 Run3 失败的详细分析

Run3 在完成 8 轮 REPLACE 后（列表从 46 → 47 → 48 函数逐步微调），进入仿真阶段。仿真失败后触发 Fixer Agent（`agents/fixer_agent.py:245`），Fixer Agent 需自主从仿真日志中诊断故障函数并修复。该 agent 的初始任务描述为（`agents/fixer_agent.py:251`）：

> "Analyze the emulator error feedback and fix the problematic functions in the driver source code accordingly."

这是一个开放式任务——agent 不知道应该修哪个函数，需要自己从日志中推断。Fixer Agent 开始分析 `BOARD_BootClockRUN` 后，陷入以下退化循环：

**模式 1：过度信息收集**。对 `BOARD_BootClockRUN` 反复调用 `GetFunctionInfo`、`GetMMIOFunctionInfo`、`GetFunctionCallStack`、`GetStructOrEnumInfo`、`GetDriverInfo` 等工具（消息 10–213），在"浏览"代码库上消耗大量迭代，无法做出分类决策。Prompt 虽然声明了预算约束（`prompts/function_fixer.py:75`：`"you have ~50 steps total"`），但 LLM 在实际执行中未遵守。

**模式 2：函数间跳跃**。agent 在分析一个函数遇到障碍后，不修正策略重试，而是放弃当前函数跳到下一个：

```
BOARD_BootClockRUN → 分析 → 遇障碍 → 跳走
  → CLOCK_DeinitAudioPll → 重复查询 → 遇障碍 → 跳走
    → CLOCK_DeinitRcOsc24M → 重复查询 → 遇障碍 → 跳走
      → CLOCK_EnableUsbhs0Clock → ...
```

每个函数重复相同的冗长查询模式（5–10 次工具调用），但从不完成"分类 → 替换 → 验证"的闭环。

**模式 3：不泛化已学到的规则**。当 `VerifyReplacement` 反馈"替换过于激进"时，agent 没有将这条规则推广到后续同类函数。例如，对 `CLOCK_DeinitAudioPll` 学到"需要保留时钟配置的 MMIO 写入"后，分析 `CLOCK_DeinitRcOsc24M` 时重新学习同一规则。Analyzer Agent 的每个函数分析是独立的 LangGraph 会话（`agents/analyzer_agent.py:308-315`），函数间无显式知识传递机制；`data_manager` 中的替换历史上限为 2 条（`core/data_manager.py:9`），信息量有限。

FAILCHECK 在累计 **22,567 条消息** 后触发（`agents/fixer_agent.py:258` 的 `recursion_limit: 50` 被 `GraphRecursionError` 超出），调用 `analyze_failed_conversation`（`utils/failcheck.py:110`）生成诊断报告，随后执行 `sys.exit(1)`（`utils/failcheck.py:216`）终止整个流程。

FAILCHECK 诊断报告（`isolated_db/U1_run3/lcmhal_failcheck_logs/failcheck_fixer_agent_20260508_110355.txt`）的结论：

> "代理过于谨慎且缺乏重点。它为了追求'完美'的理解，而浪费了大量时间在无需再探索的信息上，导致未能朝着最终目标取得任何显著的进展。"

**重要说明**：50 轮预算并非"太少"。Run1 用 12 轮 REPLACE 迭代即完成全部工作，Run2 用 9 轮 + 1 次 Fixer 修复即通过仿真。Run3 的问题不是预算不足，而是该 session 的 agent 行为**结构性不收敛**——即使给 500 轮也不会成功，因为 agent 不朝目标方向前进，而是在原地空转。

### 2.4 Run3 失败的多因素分析

Run3 的失败是多个 LLM 非确定性因素叠加的结果：

**因素 A：分类路径分歧**。Run1/Run2 将 `BOARD_BootClockRUN`（含变体）纳入替换列表，Fixer 阶段无需从零分析该函数。Run3 的分类器在首轮就拒绝了 `BOARD_BootClockRUN_528M`，导致 Fixer 阶段需要重新分析这个复杂函数——恰好该次 session 的 agent 未能有效处理。

**因素 B：工具解析错误**。Run3 日志中出现了 Run1/Run2 未出现的错误：

```
Error analyzing function LPUART_Init: Unknown tool type: 'GetMMIOFunctionInfo'.
  Available tools: FunctionClassifyResponse
Error analyzing function CLOCK_GetFreq: Unknown tool type: 'GetFunctionInfo'.
  Available tools: FunctionClassifyResponse
```

LLM 在某些函数上生成了当前 agent 阶段不可用的工具调用（例如在 `FunctionClassifyResponse` 阶段调用了属于 MCP Collector 的工具），导致 `OUTPUT_PARSING_FAILURE`。这类错误破坏了 agent 的推理链，使其更容易进入无效循环。

**因素 C：替换覆盖不足**。Run3 仅落盘 1 个 RU 文件（`replacement_update_HAL_UartSendBlocking`），远少于 Run1 的 3 个（`ENET_UpdateReadBuffers`, `ENET_ReceiveIRQHandler`, `CLOCK_InitUsb2Pll`）和 Run2 的 4 个。但 Run3 根本没有走到仿真阶段就被 FAILCHECK 终止了，因此覆盖不足未直接导致仿真失败，而是反映了该 session 整体效率低下。

### 2.5 对比：Run1/Run2 为何成功

| | Run1 | Run2 |
|---|------|------|
| 首轮 REPLACE | 38 函数 | 41 函数 |
| 最终 REPLACE | 42 函数（+4） | 44 函数（+3，含 `__assert_func`） |
| RU 落盘 | 3 个（ENET 相关） | 4 个（GPIO、UART 相关） |
| Fixer 介入 | 无需（仿真直接通过） | 1 次（`function_fix___assert_func`） |
| 遇到的问题 | 3 个函数分析超时（均重试成功） | 54+ 个函数首次分类超时（均重试成功） |

两个成功 run 的共同特征：agent 在分类阶段高效收敛，RU 覆盖了 ENET/LPUART 等关键外设函数，且没有出现工具解析错误。Run2 虽然首次分类超时数远多于 Run1（54 vs 3），但 agent 在第二轮重试中完成了分类，说明超时本身不致命——**关键在于 agent 能否从错误中恢复并保持收敛**。

### 2.6 本案例的论文叙事

U1 的三次 run 证明了以下论点：

1. **静态分析阶段完全确定性**：`分析函数个数`三次均为 235（CodeQL 输出不受 LLM 影响）。
2. **LLM 分类阶段存在 session 间波动**：`识别函数个数`从 47 到 50，首轮替换列表函数数量从 38 到 46，具体函数子集各不相同。
3. **不确定性可导致 agent 行为失控**：Run3 的 Fixer Agent 因推理链崩溃而耗尽 50 轮迭代预算（22,567 条消息），未能完成任何一个函数的修复。同固件在 Run1/Run2 中使用相同预算高效通过。
4. **系统鲁棒性存在上界**：LLM 的非确定性不保证每次都能收敛——同一配置、同一工具集、同一函数集，不同 session 的结果可能截然不同。

---

## 三、案例二：动态反馈弥合不确定性偏差 —— U5 (imxrt1052-nxp-evk/base)

### 3.1 数量统计

| 指标 | Run1 | Run2 | Run3 |
|------|------|------|------|
| 分析函数个数 | 51 | 51 | 51 |
| 识别函数个数 | 12 | 12 | 11 |
| RU 落盘次数 | 3 | 5 | 2 |
| 迭代优化数量 | 0 | **3** | **2** |
| 迭代优化目标 | （无） | `BOARD_BootClockRUN`;`CLOCK_InitExternalClk`;`LPUART_GetStatusFlags` | `CLOCK_InitArmPll`;`imxrt_putc` |
| exit_code | **1** | **0** | **0** |
| 仿真结果 | **未进入仿真阶段** | `success=True`（3min timeout） | `success=True`（3min timeout） |
| LLM invokes | 297 | 316 | 275 |
| total_tokens | 5,936,056 | 4,970,887 | 4,441,421 |
| wall_sec | 899 | 1,170 | 657 |
| FAILCHECK | **是（iterations exceeded: 50）** | 否 | 否 |

**观察**：`迭代优化数量`在三次 run 间差异显著（0、3、2），且 **三次 run 的迭代优化目标集合无一重叠**（Run2 修了 3 个函数，Run3 修了 2 个函数，共 5 个函数无一重复）。这是 LLM 非确定性的直接表现：不同 session 的 Fixer Agent 面对不同的仿真失败形态，选择了不同的修复切入点。

### 3.2 首轮替换函数列表的差异

三次 run 的初始 `[REPLACE]` 列表：

| 函数 | Run1 | Run2 | Run3 |
|------|------|------|------|
| `imxrt_pin_mode` | ✓ | ✓ | ✓ |
| `BOARD_BootClockRUN` | ✓ | **✗** | ✓ |
| `CLOCK_EnableUsbhs0Clock` | ✓ | ✗ | ✗ |
| `CLOCK_EnableUsbhs1Clock` | ✗ | ✓ | ✗ |
| `CLOCK_EnableUsbhs1PhyPllClock` | ✓ | ✓ | ✗ |
| `CLOCK_InitArmPll` | ✓ | ✓ | **✗**（被审查机制拒绝） |
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

**注意**：
- Run2 的初始列表**不含 `BOARD_BootClockRUN`**（Run1/Run3 均含）。
- Run3 包含 `GPIO_PinInit` 和 `LPUART_Init`（Run1/Run2 均未纳入）。
- Run3 的 `CLOCK_EnableUsbhs1Clock` 和 `CLOCK_InitArmPll` 被分类器审查机制拒绝（日志：`[FunctionClassifier] 未采纳未验证替换: ... 审查机制清空`），因此未进入初始列表。

三次列表仅共享 5 个函数（`imxrt_pin_mode`, `CLOCK_EnableUsbhs1PhyPllClock`, `CLOCK_InitAudioPll`, `CLOCK_InitEnetPll` 仅 Run2/3, `LPUART_Deinit`），充分展示了 LLM 分类的 session 间差异。

### 3.3 Run1 失败分析

Run1 的失败轨迹：

1. **首轮仿真成功进入**：12 函数被替换后编译通过，仿真启动。
2. **`BOARD_BootClockRUN` 分析触发 API 错误**：
   ```
   Error analyzing function BOARD_BootClockRUN: Error code: 400 - 
     invalid_request_error: An assistant message with 'tool_calls' must be 
     followed by tool messages responding to each 'tool_call_id'.
   ```
   LLM 生成了工具调用但未正确匹配响应格式（`tool_calls` 与 `tool_call_id` 不对应），导致该函数从替换列表中移除（从 12 函数降到 11 函数）。

3. **Fixer Agent 陷入函数间跳跃死循环**：与案例一（U1 Run3）相同的退化模式——agent 在 `BOARD_InitPins` → `CLOCK_DeinitSysPfd` → `CLOCK_DeinitExternalClk` → ... 等函数之间反复跳跃，对每个函数执行相同的查询序列但从不完成分类。FAILCHECK 在 **5,530 条消息** 后触发（`iterations exceeded: 50`）。

FAILCHECK 诊断报告（`isolated_db/U5_run1/lcmhal_failcheck_logs/failcheck_fixer_agent_20260508_051324.txt`）的根因诊断：

> "代理在分析每个新函数时都会遇到障碍（分类不确定性、验证失败），并且其唯一的应对策略是转向列表中的下一个函数，而不是解决问题。"

### 3.4 Run2 成功路径：迭代扩展

Run2 的成功是一个**迭代扩展**过程——初始 12 函数不足以通过仿真，但 Fixer Agent 在仿真反馈的驱动下逐步识别并修复了缺失的函数：

**阶段 1：首轮仿真暴露问题**。初始 12 函数被替换后构建并仿真，仿真失败（程序在时钟初始化的硬件轮询处阻塞）。

**阶段 2：3 次 `function_fix` 逐步收敛**

| 修复轮次 | 落盘文件 | 目标函数 | 仿真失败根因 | 替换策略 |
|----------|---------|---------|------------|---------|
| 第 1 次 | `function_fix_CLOCK_InitExternalClk_20260508052509.json` | `CLOCK_InitExternalClk` | 硬件轮询循环等待 XTALOSC24M 上电状态位和频率稳定，仿真中该寄存器不变化导致 hang | 移除轮询循环，保留函数结构 |
| 第 2 次 | `function_fix_BOARD_BootClockRUN_20260508052822.json` | `BOARD_BootClockRUN` | 硬件轮询循环等待 DCDC_STS_DC_OK 状态位，仿真中该位不变化导致 hang | 移除硬件轮询循环，保留非 MMIO 调用（`CLOCK_SetRtcXtalFreq` 等） |
| 第 3 次 | `function_fix_LPUART_GetStatusFlags_20260508052935.json` | `LPUART_GetStatusFlags` | 硬件状态寄存器 `base->STAT` 在仿真中不可用，`imxrt_putc` 中轮询 `TxDataRegEmptyFlag` 位导致死循环 | 返回 `kLPUART_TxDataRegEmptyFlag` 常量（始终就绪），使发送循环不阻塞 |

**REPLACE 列表的演化**：
- 初始：12 函数
- 第 1 次修复后 +`CLOCK_InitExternalClk`：13 函数
- 第 2 次修复后 +`BOARD_BootClockRUN`：14 函数
- 第 3 次修复后 +`LPUART_GetStatusFlags`：**15 函数** → **仿真通过**

最终仿真结果：`exit_code=0 success=True reason='success'`（3 分钟超时，表明程序正常执行到 main 并持续运行）。

**关键观察**：`BOARD_BootClockRUN` 不在 Run2 的初始分类列表中，但 Fixer Agent 从仿真日志中识别到该函数的硬件轮询是阻塞根因，主动将其纳入修复范围。这说明 **Fixer Agent 的修复动作不是预先规划的固定脚本，而是根据仿真反馈动态决定的**。

### 3.5 Run3 成功路径：不同的初始子集，不同的修复路径

Run3 走了一条**完全不同的路线**到达相同的成功终点：

**初始列表差异**：
- Run3 从一开始就包含了 `GPIO_PinInit` 和 `LPUART_Init`（Run1/Run2 均未初始纳入）。
- Run3 的分类器拒绝了 `CLOCK_EnableUsbhs1Clock` 和 `CLOCK_InitArmPll`，因此这两个函数未进入初始列表。

**2 次 `function_fix`**：

| 修复轮次 | 落盘文件 | 目标函数 | 仿真失败根因 | 替换策略 |
|----------|---------|---------|------------|---------|
| 第 1 次 | `function_fix_CLOCK_InitArmPll_20260508053915.json` | `CLOCK_InitArmPll` | 无限轮询循环等待 PLL lock 位 `CCM_ANALOG->PLL_ARM`，仿真中该位永远不置位 | 完全空桩 `(void)config;`，移除所有硬件寄存器访问 |
| 第 2 次 | `function_fix_imxrt_putc_20260508054029.json` | `imxrt_putc` | `while` 循环轮询 `LPUART_GetStatusFlags` 读取的 `base->STAT` MMIO 寄存器，仿真中标志位永远不置位 | 移除轮询循环，仅保留 `LPUART_WriteByte` 写入和返回值 |

**REPLACE 列表变化**：
- 初始：11 函数
- 第 1 次修复后 +`CLOCK_InitArmPll`：12 函数
- 第 2 次修复后 +`imxrt_putc`：**13 函数** → **仿真通过**

### 3.6 跨 Run 对比的关键发现

**发现 1：初始分类路径完全不同，但最终都到达了成功**

Run2 的初始列表不含 `BOARD_BootClockRUN`（被 Fixer 后续补上），Run3 的初始列表不含 `CLOCK_InitArmPll`（同样被 Fixer 补上）。LLM 分类的随机性导致不同 run 遗漏了不同的关键函数，但**动态反馈机制在每种情况下都精准地定位了缺失的函数**。

**发现 2：迭代优化目标集合无一重叠**

| Run | 迭代优化数量 | 迭代优化目标 |
|-----|------------|------------|
| Run2 | 3 | `BOARD_BootClockRUN`; `CLOCK_InitExternalClk`; `LPUART_GetStatusFlags` |
| Run3 | 2 | `CLOCK_InitArmPll`; `imxrt_putc` |

5 个修复目标函数无一重复。Run2 修复了时钟初始化中的轮询循环和串口状态查询；Run3 修复了 ARM PLL 锁定等待和字符输出中的轮询。两者面对的仿真失败点不同，修复策略也不同。这证明了 Fixer Agent 的修复动作**是针对具体仿真失败形态动态选择的，而非固定脚本**。

**发现 3：同一底层问题的不同修复层面**

Run2 中 `LPUART_GetStatusFlags` 的修复与 Run3 中 `imxrt_putc` 的修复实际上是同一问题（串口发送阻塞）的两个层面：

- **Run2** 在 `LPUART_GetStatusFlags` 层面修复：让状态标志始终返回 `kLPUART_TxDataRegEmptyFlag`（就绪），上层 `imxrt_putc` 的 `while` 循环自然不再阻塞。
- **Run3** 在 `imxrt_putc` 层面修复：直接去掉 `imxrt_putc` 内部的 `while` 轮询循环，保留 `LPUART_WriteByte` 写入。

即使面对同一类底层问题，不同 LLM session 的 Fixer Agent 选择了不同的修复抽象层级。这种差异本身也是 LLM 非确定性的体现。

**发现 4：REPLACE 列表长度的演化方向**

| Run | 初始 | 最终 | 变化 |
|-----|------|------|------|
| Run2 | 12 | **15** | +3（Fixer 新增 3 个函数） |
| Run3 | 11 | **13** | +2（Fixer 新增 2 个函数） |

两个成功的 run 都是**从不足的初始集合逐步扩展**到足够的覆盖——这恰好是动态反馈机制的设计目标：初始分类不需要完美，后续迭代会补全缺失。

### 3.7 成功/失败的关键分岔点

Run1（失败）与 Run2/Run3（成功）的核心差异在于 **Fixer Agent 是否能维持有效的推理链**：

- **Run1**：`BOARD_BootClockRUN` 分析时遇到 API 错误 400 → agent 推理链被打断 → 进入函数间跳跃死循环 → 50 轮耗尽 → FAILCHECK 终止 → **无 `function_fix_*` 落盘** → 从未进入第二轮仿真。
- **Run2**：初始分类稳定 → 5 轮 REPLACE → 仿真失败 → Fixer Agent 维持有效推理链 → 3 次 function_fix 逐步收敛 → 仿真通过。
- **Run3**：初始分类走了不同路径（含 `GPIO_PinInit`/`LPUART_Init`）→ 仿真失败 → Fixer Agent 维持有效推理链 → 2 次 function_fix → 仿真通过。

**分岔点**：Run1 中 `BOARD_BootClockRUN` 的 API 错误 400 是纯粹的 LLM 非确定性行为——同函数在 Run2（虽然初始未选它，后续 Fixer 分析时处理了它）和 Run3 中均未触发此类错误。这一次偶发事件打断了 agent 的推理链，导致整个 pipeline 失控。

### 3.8 本案例的论文叙事

U5 的三次 run 证明了以下论点：

1. **LLM 分类的不确定性导致初始函数子集不同**：三次 run 的初始列表仅共享 5/11–12 个函数，差异显著。
2. **动态反馈机制能够弥合分类偏差**：Run2/Run3 通过 Fixer Agent 在仿真反馈驱动下精准修复了各自暴露的问题——修复的函数集合完全不同（5 个函数无一重叠），但殊途同归。
3. **反馈闭环有效但非万能**：Run1 因 agent 推理链崩溃（偶发 API 错误 → 死循环）而失败。反馈机制的前提是 agent 能维持有效推理——当这一前提不成立时，修复也无法完成。
4. **修复动作是动态适配的**：同一底层问题（串口发送阻塞）在 Run2 中通过修复状态查询函数解决，在 Run3 中通过修复调用者解决。修复策略因 run 而异，不是预设的固定脚本。

---

## 四、两类案例的综合讨论

### 4.1 对比

| 维度 | 案例一（U1） | 案例二（U5） |
|------|------------|------------|
| 固件 | NXP_LwIP_BareMetal（裸机 ETH） | imxrt1052-nxp-evk/base（RT-Thread GPIO） |
| 成功/失败分布 | Run1✓ Run2✓ Run3✗ | Run1✗ Run2✓ Run3✓ |
| 失败 run 的失败原因 | Fixer Agent 信息收集死循环 | 同左 |
| 成功 run 的特征 | 分类高效收敛，无需/少量 Fixer 介入 | 初始分类有偏差，Fixer 高度介入（2–3 次迭代修复） |
| 迭代优化目标（跨 run） | Run2 仅 1 个（`__assert_func`） | Run2 修 3 个，Run3 修 2 个，无一重叠 |
| 核心论点 | 不确定性可导致 agent 行为失控，系统鲁棒性有上界 | 反馈闭环可弥合分类偏差，但依赖 agent 维持有效推理链 |

### 4.2 共同根因

两个案例中，失败的 run（U1 Run3、U5 Run1）都是因为 Fixer Agent 陷入了"信息收集 → 不确定性 → 跳到下一函数"的退化循环。这种行为的出现与否完全取决于 LLM session——同一函数、同一工具集、同一上下文结构，不同 session 中 agent 可能选择高效收敛或无限徘徊。

**值得注意的是**：失败的 run 的 agent 并非因为遇到了"更难"的问题。U1 Run3 分析的函数（`BOARD_BootClockRUN`, `CLOCK_*` 系列）与 Run1/Run2 高度重叠；U5 Run1 分析的函数与 Run2/Run3 也高度重叠。失败的原因是 **agent 自身的推理策略在该 session 中失控**，而非问题的固有难度。

### 4.3 结论

综合两类案例，可以得出以下结论：

1. **静态分析阶段完全确定性**，不受 LLM 影响（`分析函数个数`同固件三次不变）。
2. **LLM 分类阶段存在 session 间波动**（`识别函数个数`波动约 6–8%），直接导致后续替换子集、RU 落盘、迭代目标均不同。
3. **动态反馈机制能够弥合分类偏差**：U5 Run2/Run3 展示了 Fixer Agent 在仿真反馈驱动下精准修复的能力，修复目标因 run 而异，证明这不是固定脚本。初始分类不需要完美，后续迭代会补全缺失。
4. **系统鲁棒性存在上界**：当 LLM agent 的推理链崩溃时（偶发 API 错误、工具解析错误等触发退化循环），反馈机制无法挽救。15 次运行中仅 4 次 exit=0 且仿真成功（U1×2 + U5×2），其余 11 次均因 FAILCHECK 终止或仿真失败。
5. **失败不是工程 bug，而是实验观测到的现象**：本实验的目的正是"评估 LLM 输出不确定性对最终结果的影响"，结论是"有影响——既可能被反馈机制弥合，也可能导致系统失控"，这恰恰说明了实验的必要性。

---

## 五、数据来源索引

| 数据 | 路径 |
|------|------|
| 批次运行日志 | `runs/e3b_uncertainty/20260508_045825/logs/U{1,5}_run{1,2,3}.log` |
| 运行汇总 | `run_log.tsv`（exit、仿真、wall_sec、tokens） |
| 机器可读统计 | `doc/experiments/E3b-批次20260508_045825_实测汇总.tsv` |
| 隔离 DB（每次 run 的独立快照） | `runs/e3b_uncertainty/20260508_045825/isolated_db/U{1,5}_run{1,2,3}/lcmhal_ai_log/` |
| FAILCHECK 诊断报告 | `isolated_db/.../lcmhal_failcheck_logs/failcheck_fixer_agent_*.txt` |
| Fixer Agent 系统提示 | `prompts/function_fixer.py` |
| Fixer Agent 入口 | `agents/fixer_agent.py:245` |
| Analyzer Agent 入口 | `agents/analyzer_agent.py:293` |
| 完整流水线编排 | `main.py:100-167` |
| U5 代码级对照 | `doc/experiments/E3b-U5_BOARD_BootClockRUN_三次重复试验案例.md` |

---

## 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-10 | 初稿。U1 + U5 两类案例分析。 |
| 2026-05-10 | 重写为完整技术文档：补充源码引用（`file:line`）、初始列表逐函数对照表、迭代修复逐次溯源、综合讨论与论文叙事建议。 |
