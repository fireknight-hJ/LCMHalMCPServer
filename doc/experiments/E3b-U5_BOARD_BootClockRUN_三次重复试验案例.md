# E3b 案例：`BOARD_BootClockRUN` 在 imxrt1052-nxp-evk/base 上三次重复试验（U5 Run1–3）

**目的**：以同一固件、同一函数、三次独立 LLM session 的**真实日志与落盘 JSON**为证据，说明  

1. **有的批次**：分类 + 验证链在**前期**即给出可采纳替换，**无需**再对该函数做仿真后 Fixer；  
2. **有的批次**：前期分析在**策略上**做出「不替换本函数」等结论，但**仿真仍落在原厂死循环**上，随后由 **`function_fix`（Fixer）** 按执行反馈补上一版替换；  
3. **有的批次**：前期在**同一函数上**出现**多版** `replacement_update_*`（策略从「砍 `CLOCK_SetMux`/`SetDiv`」到「恢复调用链」），**整次 run 仍失败**——用于对照**鲁棒性上界**。

**数据批次**：`runs/e3b_uncertainty/20260508_045825/`  
**工程侧源码位置**（来自 `GetFunctionInfo` 工具回传）：  
`/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/clock_config.c`，`BOARD_BootClockRUN` 约从 **第 156 行** 起（以当时构建机快照为准）。

**整次 run 成败**（`run_log.tsv`）：U5_run1 `exit_code=1`；U5_run2、U5_run3 `exit_code=0` 且日志含 `Emulate ... success=True`。

**代码对照**：`doc/experiments/snippets/` 下若干 `U5_*.c` 与对应 `lcmhal_ai_log/*.json` 字段 **逐字一致**（Unicode 转义已解码）。在仓库根目录执行 `python3 tools/extract_u5_board_snippets.py` 可从本批次 `isolated_db` 重新生成。下文 **§八** 摘录头尾便于速读，审稿人可打开同目录 `.c` 全文与 JSON 对账。

---

## 一、原厂 `BOARD_BootClockRUN` 在仿真里为何「危险」

NXP / MCUX 生成的 `BOARD_BootClockRUN` 是典型的**板级时钟树编排**：大量 `CLOCK_*` 库函数调用 + 直接写 `CCM` / `CCM_ANALOG` / `XTALOSC24M` / `DCDC` / `IOMUXC_GPR` 等寄存器。

与**死循环**最相关、三次试验里反复被日志点名的片段如下（语义与 `GetFunctionInfo` 回传的 `function_content` 一致；为可读性去掉转义）：

```c
/* Setting the VDD_SOC to 1.275V. It is necessary to config AHB to 600Mhz. */
DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(0x13);
/* Waiting for DCDC_STS_DC_OK bit is asserted */
while (DCDC_REG0_STS_DC_OK_MASK != (DCDC_REG0_STS_DC_OK_MASK & DCDC->REG0))
{
}
```

**更完整的 OEM 函数开头**（含 `XTALOSC24M`、`CCM->CCR`、上述 `DCDC` 写与 `while` 的完整上下文）见下文 **§8.2**。

在**真芯片**上，`DCDC->REG0` 的 `STS_DC_OK` 会由硬件置位，`while` 会退出。在**当前仿真环境**里，该位往往**不会按真实硬件时序置起**，线程在 `BOARD_BootClockRUN` 内**自旋**，被 LCMHAL 记为 **`Stop due to exceptional loop`**，`current function: BOARD_BootClockRUN`（见 U5_run2 的 `function_fix_BOARD_BootClockRUN_*.json` 内嵌的 `GetMMIOFunctionEmulateInfo` 返回文本）。

另一路风险来自 **`CLOCK_SetMux` / `CLOCK_SetDiv`**：SDK 里常为 **static inline**，展开后可能包含对 **`CCM->CDHIPR`** 等 busy-wait；若仿真对「握手位」不更新，也会表现为**异常循环**。U5_run1 **第一版** `replacement_update` 即按此假设**整段删除**大量 `CLOCK_SetMux`/`SetDiv`（见下文 §4）。

---

## 二、流水线与落盘文件（读本文档时应建立的对应关系）

| 落盘 | 含义（与本案例相关） |
|------|----------------------|
| `function_classify_<函数>_*.json` | **FunctionClassifier 子图**整段对话 + **`final_response`**：`function_type`、`has_replacement`、`function_replacement`（采纳稿）、`classification_reason`。 |
| `replacement_update_<函数>_*.json` | 任意阶段调用 **`UpdateFunctionReplacement`** 且 **rubric/编译校验通过** 后，`data_manager` 写入的一版替换体 + `reason`。**同一 run 可多条**（时间戳不同）。 |
| `function_fix_<函数>_*.json` | **`function_fix()`（Fixer）** 整段会话结束时的归档；内含仿真工具返回、`UpdateFunctionReplacement` 调用与 **`final_response`**（仍为 `ReplacementUpdate` 结构）。 |

**重要**：`final_response.has_replacement == false` **并不保证**磁盘上没有 `replacement_update_*`——会话中途可能已调用工具落盘，但最终采纳策略又改为「不替换本函数」。**U5_run2 对 `BOARD_BootClockRUN` 即如此**（见 §4）。

---

## 三、U5_run3：**前期「一次过关」型**（本函数无 `function_fix`）

### 3.1 分类与采纳

- 日志：`isolated_db/U5_run3/lcmhal_ai_log/function_classify_BOARD_BootClockRUN_20260508053546.json`  
- **`final_response`**：`function_type: **INIT**`，`has_replacement: **true**`，`replacement_check_reason: null`。  
- 模型在 `classification_reason` 中明确写到：删除 **DCDC 轮询**、注释 **直写 MMIO**，**保留** `CLOCK_*` / `IOMUXC_*` 调用链与 `SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK`。

### 3.2 替换实现要点（与 `final_response.function_replacement` 一致）

策略可概括为：

- **去掉** `while (DCDC_REG0_STS_DC_OK_MASK ... DCDC->REG0)` 阻塞等待；  
- 对 `XTALOSC24M->…`、`CCM->CCR`、`DCDC->REG3`、大量 `CCM_ANALOG->…`、`CCM->CCOSR`、`IOMUXC_GPR->GPR5` 等 **inline 寄存器写**，改为 **`/* [MMIO] ... */` 注释**或等价「不在仿真路径上依赖真外设」的写法；  
- **保留** `CLOCK_SetRtcXtalFreq` → `CLOCK_SwitchOsc`、成片的 `CLOCK_SetMux` / `CLOCK_SetDiv` / `CLOCK_DisableClock`、条件编译块内的 `CLOCK_InitArmPll` / `CLOCK_InitSysPll` / `CLOCK_InitUsb1Pll` 等 **库级调用**，以维持「时钟树调用顺序」供后续已替换子函数衔接；  
- **保留** `SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;`（RTOS tick 依赖）。

本 run **未出现** `function_fix_BOARD_BootClockRUN_*.json`，且 **`main.py` exit=0**——在证据意义上：对 **`BOARD_BootClockRUN` 本函数**，**分类阶段给出的替换已通过 Verify 链路并被采纳**，后续**未再**因该函数触发 Fixer。

---

## 四、U5_run2：**前期策略与仿真冲突 → Fixer 兜底型**

### 4.1 分类阶段的「反转」结论

- 日志：`isolated_db/U5_run2/lcmhal_ai_log/function_classify_BOARD_BootClockRUN_20260508051417.json`  
- **`final_response`**：`function_type: **INIT**`，但 **`has_replacement: false`**，`function_replacement: ""`。  
- `classification_reason` 摘要：这是**大块板级 INIT**，子函数（`CLOCK_InitArmPll` 等）更适合**分别替换**；若强行整体 stub 易 **semantic degradation**；因此 **「保留原厂时钟初始化序列」**——在 **prompt 的 anti-stub 语义**下，这是**自洽的保守决策**。

### 4.2 与磁盘上 `replacement_update_*` 并存的原因

同 run 仍存在：

`isolated_db/U5_run2/lcmhal_ai_log/replacement_update_BOARD_BootClockRUN_20260508052702.json`

其 `reason` 写明 **LOOP / DCDC**：去掉 `while (DCDC_REG0_STS_DC_OK …)`，并把若干 MMIO 写改为注释，**保留**大量 `CLOCK_*` 调用——与 Run3 **同一技术家族**。这说明：**会话中途**模型曾 **`UpdateFunctionReplacement` 成功落盘**；但 **`function_classify` 的最终结构化输出**仍选择了 **`has_replacement:false`**。写论文时应**并列引用**两类落盘，避免读者以为「没有采纳稿 = 没有发生过替换尝试」。

### 4.3 仿真仍触发死循环 → `function_fix`

Fixer 归档：`function_fix_BOARD_BootClockRUN_20260508052822.json`。

工具返回的仿真摘要（节选，原文在 JSON 的 tool message 中）：

```text
Stop due to exceptional loop.
current function: BOARD_BootClockRUN
current caller function: BOARD_BootClockRUN
end pc: 0x60004dbe
```

Fixer 的 **`final_response.reason`** 将根因归纳为：**DCDC `STS_DC_OK` 轮询在仿真中永不满足**；替换策略与 `replacement_update_20260508052702.json` **同族**：去阻塞环、注释硬件直写、**保留** `CLOCK_*` 调用与 `SystemCoreClock` 赋值。

**叙事对齐（你希望的「先分析、后死循环、再修复」）**：  

- **分析阶段**：给出「尽量不整体替换」的 **INIT 语义理由**（`has_replacement:false`）；  
- **执行阶段**：若仍走 **OEM 路径**（或中间态仍含 DCDC 环），仿真报 **exceptional loop**；  
- **修复阶段**：**Fixer** 根据日志**强制**写回一版可消去死循环的替换体——体现 **「静态规则 / 反 stub」与「可执行反馈」之间的张力**，以及系统在第二层反馈上的**补救能力**。

---

## 五、U5_run1：**同一函数上多版 `replacement_update`，整 run 仍失败（对照组）**

### 5.1 第一版：激进删除 `CLOCK_SetMux` / `CLOCK_SetDiv`

- `replacement_update_BOARD_BootClockRUN_20260508050956.json`  
- **`reason`**：仿真报 `BOARD_BootClockRUN` **exceptional loop**；归因于 **`CLOCK_SetMux`/`CLOCK_SetDiv` 为 static inline，内联后对 `CCM->CDHIPR` busy-wait**，在仿真中永不前进；故**删除本函数内几乎所有** `CLOCK_SetMux`/`CLOCK_SetDiv`（及经 `CLOCK_SetMux` 的 `Pll3SwMux`），仅保留 `CLOCK_DisableClock`、`CLOCK_Init*`、`IOMUXC_*`、`SystemCoreClock` 等。

这是与 Run3 **截然相反**的「**砍时钟 mux/div**」路线：在**同一 OEM 函数**上，不同 session 对「环路究竟在 DCDC 还是在 `CLOCK_SetMux` inline」的**假设权重不同**。

### 5.2 第二版：恢复 `CLOCK_SetMux`/`SetDiv` 调用链

- `replacement_update_BOARD_BootClockRUN_20260508051151.json`  
- **`reason`**：说明 exceptional loop 亦可能由 inline busy-wait 引起，但本版选择 **恢复** `CLOCK_SetMux`/`SetDiv`，把信任交给「仿真对 MMIO 的拦截」；与 Run3 的最终形态**更接近**。

### 5.3 分类最终仍采纳替换

`function_classify_BOARD_BootClockRUN_20260508050604.json` 的 **`final_response`**：`has_replacement: **true**`，`function_type: INIT`，`replacement_check_reason: null`——即 **Classifier 最终仍输出一整段可采纳替换**（正文与第二版 `replacement_update` 同族：保留大量 `CLOCK_*` 调用）。

### 5.4 整次 run 结果

**U5_run1 `exit_code=1`**，且 **无** `function_fix_BOARD_BootClockRUN_*.json`。  

**含义**（写论文时建议直写）：**多版 `replacement_update` + 采纳型 `function_classify` 仍不能保证端到端成功**；鲁棒性叙事必须保留 **「失败 run」** 作为上界，而不是只讲 Run2/3。

---

## 六、三条时间线对照（来龙去脉一览）

| 项目 | Run1 | Run2 | Run3 |
|------|------|------|------|
| **`function_classify` 最终 `has_replacement`** | `true` | `false` | `true` |
| **`replacement_update_BOARD_*` 条数** | **2**（策略先激进后回调） | **1**（中途落盘，与最终 `has_replacement:false` 并存） | **0**（本函数无独立 `replacement_update_*` 文件名；采纳稿在 `function_classify` 内） |
| **`function_fix_BOARD_*`** | 无 | **有** | 无 |
| **整次 run** | **失败** | **成功** | **成功** |
| **适合支撑的论点** | 非确定性：**同一 OEM、不同替换策略**；**迭代仍可能不收敛** | **分析策略（不替换）与仿真反馈冲突 → Fixer 纠偏** | **前期替换 + Verify 采纳即足够** |

---

## 七、与「系统鲁棒性」表述的推荐写法

1. **Run3**：强调 **「单批次内，分类—生成—Verify 闭环即可对该函数给出可执行替换」**——对应你说的**「一次性给过」**（对该函数**无二次 `function_fix`**）。  
2. **Run2**：强调 **「静态策略（反 stub、保留 OEM）≠ 仿真一定安全」**；**执行反馈**触发 **Fixer**，在同一函数上**再写**一版与 DCDC 死循环对齐的替换——对应你说的**「先分析、后死循环、再修复」**；修复主体是 **`function_fix`**，不宜笼统说成「只靠后续 `replacement_update`」。  
3. **Run1**：强调 **「即使对同一函数有多条 `replacement_update`、且 `function_classify` 最终采纳替换，整 run 仍可能失败」**——这是**鲁棒性边界**，与 Run2/3 **必须同时出现**才诚实。

---

## 八、附录：原函数与替换体对照（摘录）

以下 C 块与 `doc/experiments/snippets/` 中同名 `.c` **一致**；中间用注释标出省略行数，全文以 snippet 文件与 **§九** JSON 为准。

### 8.1 摘录与再生

| 文件 | 来源 JSON 字段 |
|------|----------------|
| `doc/experiments/snippets/U5_BOARD_oem_BOARD_BootClockRUN_head50.c` | U5_run2 `function_classify_…51417.json` 内 `GetFunctionInfo` 回传的 `function_content`（仅前 50 行） |
| `…/U5_run3_BOARD_BootClockRUN_replace_full.c` | U5_run3 `function_classify_…53546.json` → `final_response.function_replacement` |
| `…/U5_run2_BOARD_BootClockRUN_function_fix_replace_full.c` | U5_run2 `function_fix_…52822.json` → `final_response.replacement_code` |
| `…/U5_run1_BOARD_BootClockRUN_replacement_update_v1_full.c` | U5_run1 `replacement_update_…50956.json` → `replacement_code` |
| `…/U5_run1_BOARD_BootClockRUN_replacement_update_v2_full.c` | U5_run1 `replacement_update_…51151.json` → `replacement_code` |
| `…/U5_run2_BOARD_BootClockRUN_replacement_update_full.c` | U5_run2 `replacement_update_…52702.json` → `replacement_code` |

再生命令（仓库根目录）：`python3 tools/extract_u5_board_snippets.py`。

### 8.2 OEM：`BOARD_BootClockRUN` 开头（与 §一 DCDC 片段衔接）

```c
/*******************************************************************************
* Code for BOARD_BootClockRUN configuration
******************************************************************************/
void BOARD_BootClockRUN(void)
{
    /* Init RTC OSC clock frequency. */
    CLOCK_SetRtcXtalFreq(32768U);
    /* Enable 1MHz clock output. */
    XTALOSC24M->OSC_CONFIG2 |= XTALOSC24M_OSC_CONFIG2_ENABLE_1M_MASK;
    /* Use free 1MHz clock output. */
    XTALOSC24M->OSC_CONFIG2 &= ~XTALOSC24M_OSC_CONFIG2_MUX_1M_MASK;
    /* Set XTAL 24MHz clock frequency. */
    CLOCK_SetXtalFreq(24000000U);
    /* Enable XTAL 24MHz clock source. */
    CLOCK_InitExternalClk(0);
    /* Enable internal RC. */
    CLOCK_InitRcOsc24M();
    /* Switch clock source to external OSC. */
    CLOCK_SwitchOsc(kCLOCK_XtalOsc);
    /* Set Oscillator ready counter value. */
    CCM->CCR = (CCM->CCR & (~CCM_CCR_OSCNT_MASK)) | CCM_CCR_OSCNT(127);
    /* Setting PeriphClk2Mux and PeriphMux to provide stable clock before PLLs are initialed */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1); /* Set PERIPH_CLK2 MUX to OSC */
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);     /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* Setting the VDD_SOC to 1.275V. It is necessary to config AHB to 600Mhz. */
    DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(0x13);
    /* Waiting for DCDC_STS_DC_OK bit is asserted */
    while (DCDC_REG0_STS_DC_OK_MASK != (DCDC_REG0_STS_DC_OK_MASK & DCDC->REG0))
    {
    }
    /* Set AHB_PODF. */
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    /* Disable IPG clock gate. */
    CLOCK_DisableClock(kCLOCK_Adc1);
    CLOCK_DisableClock(kCLOCK_Adc2);
    CLOCK_DisableClock(kCLOCK_Xbar1);
    CLOCK_DisableClock(kCLOCK_Xbar2);
    CLOCK_DisableClock(kCLOCK_Xbar3);
    /* Set IPG_PODF. */
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    /* Set ARM_PODF. */
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    /* Set PERIPH_CLK2_PODF. */
    CLOCK_SetDiv(kCLOCK_PeriphClk2Div, 0);
    /* Disable PERCLK clock gate. */
    CLOCK_DisableClock(kCLOCK_Gpt1);
    CLOCK_DisableClock(kCLOCK_Gpt1S);
    CLOCK_DisableClock(kCLOCK_Gpt2);
    CLOCK_DisableClock(kCLOCK_Gpt2S);
    CLOCK_DisableClock(kCLOCK_Pit);
```

（第 51 行起 OEM 仍继续；本附录只存 `U5_BOARD_oem_…_head50.c`。）

### 8.3 U5_run3：`function_classify` 采纳替换（头 + 尾）

**头**（相对 OEM：已去掉早期 `XTALOSC24M` 1MHz 位、`CCM->CCR`、`DCDC` 写与 `while` 等；**保留**早期 `CLOCK_SetMux(PeriphClk2/Periph)` 与后续 `CLOCK_SetDiv` / `DisableClock` 链）：

```c
void BOARD_BootClockRUN(void)
{
    /* Init RTC OSC clock frequency. */
    CLOCK_SetRtcXtalFreq(32768U);
    /* Set XTAL 24MHz clock frequency. */
    CLOCK_SetXtalFreq(24000000U);
    /* Enable XTAL 24MHz clock source. */
    CLOCK_InitExternalClk(0);
    /* Enable internal RC. */
    CLOCK_InitRcOsc24M();
    /* Switch clock source to external OSC. */
    CLOCK_SwitchOsc(kCLOCK_XtalOsc);
    /* Setting PeriphClk2Mux and PeriphMux to provide stable clock before PLLs are initialed */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1); /* Set PERIPH_CLK2 MUX to OSC */
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);     /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* Set AHB_PODF. */
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    /* Disable IPG clock gate. */
    CLOCK_DisableClock(kCLOCK_Adc1);
    CLOCK_DisableClock(kCLOCK_Adc2);
    CLOCK_DisableClock(kCLOCK_Xbar1);
    CLOCK_DisableClock(kCLOCK_Xbar2);
    CLOCK_DisableClock(kCLOCK_Xbar3);
    /* Set IPG_PODF. */
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    /* Set ARM_PODF. */
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    /* Set PERIPH_CLK2_PODF. */
    CLOCK_SetDiv(kCLOCK_PeriphClk2Div, 0);
    /* Disable PERCLK clock gate. */
    CLOCK_DisableClock(kCLOCK_Gpt1);
    CLOCK_DisableClock(kCLOCK_Gpt1S);
    CLOCK_DisableClock(kCLOCK_Gpt2);
    CLOCK_DisableClock(kCLOCK_Gpt2S);
    CLOCK_DisableClock(kCLOCK_Pit);
```

**中略**（约第 36–202 行：`CLOCK_SetDiv` / `CLOCK_DisableClock`、条件编译内 ARM/Sys/Usb1 PLL 与 PFD 等，与全文 `.c` 一致。）

**尾**（PLL 去初始化后 **显式** `CLOCK_SetMux` 收尾 + `IOMUXC_*` + `SystemCoreClock`；与 Run2 Fixer 末尾「注释掉 CCOSR / GPR5 MMIO」不同，Run3 **保留**末尾纯 `CLOCK_SetMux` / `IOMUXC` 调用）：

```c
    /* DeInit Audio PLL. */
    CLOCK_DeinitAudioPll();
    /* Bypass Audio PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllAudio, 1);
    /* DeInit Video PLL. */
    CLOCK_DeinitVideoPll();
    /* DeInit Enet PLL. */
    CLOCK_DeinitEnetPll();
    /* Bypass Enet PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllEnet, 1);
    /* DeInit Usb2 PLL. */
    CLOCK_DeinitUsb2Pll();
    /* Bypass Usb2 PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllUsb2, 1);
    /* Set preperiph clock source. */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    /* Set periph clock source. */
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    /* Set periph clock2 clock source. */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    /* Set per clock source. */
    CLOCK_SetMux(kCLOCK_PerclkMux, 0);
    /* Set SAI1 MCLK1 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk1Sel, 0);
    /* Set SAI1 MCLK2 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk2Sel, 0);
    /* Set SAI1 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk3Sel, 0);
    /* Set SAI2 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI2MClk3Sel, 0);
    /* Set SAI3 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI3MClk3Sel, 0);
    /* Set MQS configuration. */
    IOMUXC_MQSConfig(IOMUXC_GPR,kIOMUXC_MqsPwmOverSampleRate32, 0);
    /* Set ENET Tx clock source. */
    IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1RefClkMode, false);
    /* Set SystemCoreClock variable. */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
```

### 8.4 U5_run2：`function_fix`（Fixer）最终 `replacement_code`（头 + 尾）

**头**（`[MMIO]` 注释与 **`[LOOP REMOVED]`** 标出 DCDC 忙等删除；策略与 Run3 同族）：

```c
void BOARD_BootClockRUN(void)
{
    /* Init RTC OSC clock frequency. */
    CLOCK_SetRtcXtalFreq(32768U);
    /* Enable 1MHz clock output. */
    /* [MMIO] XTALOSC24M->OSC_CONFIG2 |= XTALOSC24M_OSC_CONFIG2_ENABLE_1M_MASK; */
    /* Use free 1MHz clock output. */
    /* [MMIO] XTALOSC24M->OSC_CONFIG2 &= ~XTALOSC24M_OSC_CONFIG2_MUX_1M_MASK; */
    /* Set XTAL 24MHz clock frequency. */
    CLOCK_SetXtalFreq(24000000U);
    /* Enable XTAL 24MHz clock source. */
    CLOCK_InitExternalClk(0);
    /* Enable internal RC. */
    CLOCK_InitRcOsc24M();
    /* Switch clock source to external OSC. */
    CLOCK_SwitchOsc(kCLOCK_XtalOsc);
    /* Set Oscillator ready counter value. */
    /* [MMIO] CCM->CCR = (CCM->CCR & (~CCM_CCR_OSCNT_MASK)) | CCM_CCR_OSCNT(127); */
    /* Setting PeriphClk2Mux and PeriphMux to provide stable clock before PLLs are initialed */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1); /* Set PERIPH_CLK2 MUX to OSC */
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);     /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* Setting the VDD_SOC to 1.275V. It is necessary to config AHB to 600Mhz. */
    /* [MMIO] DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(0x13); */
    /* [LOOP REMOVED] Waiting for DCDC_STS_DC_OK bit - polling loop skipped for emulation */
    /* Set AHB_PODF. */
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    /* Disable IPG clock gate. */
    CLOCK_DisableClock(kCLOCK_Adc1);
    CLOCK_DisableClock(kCLOCK_Adc2);
    CLOCK_DisableClock(kCLOCK_Xbar1);
    CLOCK_DisableClock(kCLOCK_Xbar2);
    CLOCK_DisableClock(kCLOCK_Xbar3);
    /* Set IPG_PODF. */
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
```

**中略**（约第 36–264 行：与 Run3 类似的 `CLOCK_*` 主体 + 多处 `[MMIO]` 注释。）

**尾**（`CCM->CCOSR`、`IOMUXC_GPR->GPR5` 等为 **`/* [MMIO] … */`**；**仍保留** `IOMUXC_SetSaiMClkClockSource` / `IOMUXC_MQSConfig` / `IOMUXC_EnableMode` 与 `SystemCoreClock`）：

```c
    /* Set periph clock2 clock source. */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    /* Set per clock source. */
    CLOCK_SetMux(kCLOCK_PerclkMux, 0);
    /* Set lvds1 clock source. */
    /* [MMIO] CCM_ANALOG->MISC1 = (CCM_ANALOG->MISC1 & (~CCM_ANALOG_MISC1_LVDS1_CLK_SEL_MASK)) | CCM_ANALOG_MISC1_LVDS1_CLK_SEL(0); */
    /* Set clock out1 divider. */
    /* [MMIO] CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO1_DIV_MASK)) | CCM_CCOSR_CLKO1_DIV(0); */
    /* Set clock out1 source. */
    /* [MMIO] CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO1_SEL_MASK)) | CCM_CCOSR_CLKO1_SEL(1); */
    /* Set clock out2 divider. */
    /* [MMIO] CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO2_DIV_MASK)) | CCM_CCOSR_CLKO2_DIV(0); */
    /* Set clock out2 source. */
    /* [MMIO] CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO2_SEL_MASK)) | CCM_CCOSR_CLKO2_SEL(18); */
    /* Set clock out1 drives clock out1. */
    /* [MMIO] CCM->CCOSR &= ~CCM_CCOSR_CLK_OUT_SEL_MASK; */
    /* Disable clock out1. */
    /* [MMIO] CCM->CCOSR &= ~CCM_CCOSR_CLKO1_EN_MASK; */
    /* Disable clock out2. */
    /* [MMIO] CCM->CCOSR &= ~CCM_CCOSR_CLKO2_EN_MASK; */
    /* Set SAI1 MCLK1 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk1Sel, 0);
    /* Set SAI1 MCLK2 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk2Sel, 0);
    /* Set SAI1 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk3Sel, 0);
    /* Set SAI2 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI2MClk3Sel, 0);
    /* Set SAI3 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI3MClk3Sel, 0);
    /* Set MQS configuration. */
    IOMUXC_MQSConfig(IOMUXC_GPR,kIOMUXC_MqsPwmOverSampleRate32, 0);
    /* Set ENET Tx clock source. */
    IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1RefClkMode, false);
    /* Set GPT1 High frequency reference clock source. */
    /* [MMIO] IOMUXC_GPR->GPR5 &= ~IOMUXC_GPR_GPR5_VREF_1M_CLK_GPT1_MASK; */
    /* Set GPT2 High frequency reference clock source. */
    /* [MMIO] IOMUXC_GPR->GPR5 &= ~IOMUXC_GPR_GPR5_VREF_1M_CLK_GPT2_MASK; */
    /* Set SystemCoreClock variable. */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
```

### 8.5 U5_run1：第一版 `replacement_update`（50956）— 与 Run3 **策略相反**的注释 + 仍保留的 PLL 段与结尾

**头**（`classification_reason` 同族说明见 §5.1；此处可见 **整段删除**早期 `CLOCK_SetMux` / `CLOCK_SetDiv` 的注释依据）：

```c
void BOARD_BootClockRUN(void)
{
    /* Init RTC OSC clock frequency. */
    CLOCK_SetRtcXtalFreq(32768U);
    /* Set XTAL 24MHz clock frequency. */
    CLOCK_SetXtalFreq(24000000U);
    /* Enable XTAL 24MHz clock source. */
    CLOCK_InitExternalClk(0);
    /* Enable internal RC. */
    CLOCK_InitRcOsc24M();
    /* Switch clock source to external OSC. */
    CLOCK_SwitchOsc(kCLOCK_XtalOsc);
    /* Note: CLOCK_SetMux and CLOCK_SetDiv calls are removed because they are inline
       functions containing busy-wait loops on CCM->CDHIPR that hang in emulation.
       Clock mux/div configuration is not needed in the emulated environment. */
    /* Disable IPG clock gate. */
    CLOCK_DisableClock(kCLOCK_Adc1);
    CLOCK_DisableClock(kCLOCK_Adc2);
    CLOCK_DisableClock(kCLOCK_Xbar1);
    CLOCK_DisableClock(kCLOCK_Xbar2);
    CLOCK_DisableClock(kCLOCK_Xbar3);
    /* Disable PERCLK clock gate. */
    CLOCK_DisableClock(kCLOCK_Gpt1);
    CLOCK_DisableClock(kCLOCK_Gpt1S);
    CLOCK_DisableClock(kCLOCK_Gpt2);
    CLOCK_DisableClock(kCLOCK_Gpt2S);
    CLOCK_DisableClock(kCLOCK_Pit);
    /* Disable USDHC1 clock gate. */
    CLOCK_DisableClock(kCLOCK_Usdhc1);
    /* Disable USDHC2 clock gate. */
    CLOCK_DisableClock(kCLOCK_Usdhc2);
#ifndef SKIP_SYSCLK_INIT
    /* Disable Semc clock gate. */
    CLOCK_DisableClock(kCLOCK_Semc);
#endif
#if !(defined(XIP_EXTERNAL_FLASH) && (XIP_EXTERNAL_FLASH == 1))
    /* Disable Flexspi clock gate. */
    CLOCK_DisableClock(kCLOCK_FlexSpi);
#endif
```

**中略**（约第 36–80 行：大量 `CLOCK_DisableClock`。）

**尾**（仍保留 `CLOCK_SetMux(kCLOCK_Pll3SwMux, …)`、`CLOCK_InitArmPll` / `CLOCK_InitSysPll` / `CLOCK_InitUsb1Pll` 与 PFD、PLL `DeInit` / `Bypass`、`IOMUXC_*`、`SystemCoreClock`；与第二版 51151 及 Run3 路线的差异请对照 `U5_run1_…_v2_full.c` 与 §5.2。）

```c
    /* Set Pll3 sw clock source. */
    CLOCK_SetMux(kCLOCK_Pll3SwMux, 0);
    /* Init ARM PLL. */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
#ifndef SKIP_SYSCLK_INIT
    /* Init System PLL. */
    CLOCK_InitSysPll(&sysPllConfig_BOARD_BootClockRUN);
    /* Init System pfd0. */
    CLOCK_InitSysPfd(kCLOCK_Pfd0, 27);
    /* Init System pfd1. */
    CLOCK_InitSysPfd(kCLOCK_Pfd1, 16);
    /* Init System pfd2. */
    CLOCK_InitSysPfd(kCLOCK_Pfd2, 24);
    /* Init System pfd3. */
    CLOCK_InitSysPfd(kCLOCK_Pfd3, 16);
#endif
#if !(defined(XIP_EXTERNAL_FLASH) && (XIP_EXTERNAL_FLASH == 1))
    /* Init Usb1 PLL. */
    CLOCK_InitUsb1Pll(&usb1PllConfig_BOARD_BootClockRUN);
    /* Init Usb1 pfd0. */
    CLOCK_InitUsb1Pfd(kCLOCK_Pfd0, 33);
    /* Init Usb1 pfd1. */
    CLOCK_InitUsb1Pfd(kCLOCK_Pfd1, 16);
    /* Init Usb1 pfd2. */
    CLOCK_InitUsb1Pfd(kCLOCK_Pfd2, 17);
    /* Init Usb1 pfd3. */
    CLOCK_InitUsb1Pfd(kCLOCK_Pfd3, 19);
#endif
    /* DeInit Audio PLL. */
    CLOCK_DeinitAudioPll();
    /* Bypass Audio PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllAudio, 1);
    /* DeInit Video PLL. */
    CLOCK_DeinitVideoPll();
    /* DeInit Enet PLL. */
    CLOCK_DeinitEnetPll();
    /* Bypass Enet PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllEnet, 1);
    /* DeInit Usb2 PLL. */
    CLOCK_DeinitUsb2Pll();
    /* Bypass Usb2 PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllUsb2, 1);
    /* Note: Final CLOCK_SetMux calls are also removed due to busy-wait loops. */
    /* Set SAI1 MCLK1 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk1Sel, 0);
    /* Set SAI1 MCLK2 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk2Sel, 0);
    /* Set SAI1 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI1MClk3Sel, 0);
    /* Set SAI2 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI2MClk3Sel, 0);
    /* Set SAI3 MCLK3 clock source. */
    IOMUXC_SetSaiMClkClockSource(IOMUXC_GPR, kIOMUXC_GPR_SAI3MClk3Sel, 0);
    /* Set MQS configuration. */
    IOMUXC_MQSConfig(IOMUXC_GPR,kIOMUXC_MqsPwmOverSampleRate32, 0);
    /* Set ENET Tx clock source. */
    IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1RefClkMode, false);
    /* Set SystemCoreClock variable. */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
```

---

## 九、证据索引（便于审稿人复现）

| 材料 | 路径 |
|------|------|
| **逐字 C 摘录（推荐先看）** | `doc/experiments/snippets/U5_*.c`（字段映射与再生命令见 **§8.1**） |
| Run1 分类 | `…/isolated_db/U5_run1/lcmhal_ai_log/function_classify_BOARD_BootClockRUN_20260508050604.json` |
| Run1 替换 v1 / v2 | `…/replacement_update_BOARD_BootClockRUN_20260508050956.json`、`…51151.json` |
| Run2 分类 | `…/U5_run2/…/function_classify_BOARD_BootClockRUN_20260508051417.json` |
| Run2 中途替换落盘 | `…/replacement_update_BOARD_BootClockRUN_20260508052702.json` |
| Run2 Fixer | `…/function_fix_BOARD_BootClockRUN_20260508052822.json` |
| Run3 分类 | `…/U5_run3/…/function_classify_BOARD_BootClockRUN_20260508053546.json` |
| 批次总表 | `doc/experiments/E3b-批次20260508_045825_实测汇总.tsv`、`runs/…/run_log.tsv` |

---

## 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-08 | 初稿：基于 `20260508_045825` 批次 U5 三次 `BOARD_BootClockRUN` 的 `function_classify` / `replacement_update` / `function_fix` 与 `run_log.tsv` 整理。 |
| 2026-05-08 | 增补 **§八** 附录：OEM 头、Run3 采纳替换、Run2 Fixer、Run1 第一版 `replacement_update` 头尾对照；`snippets` 与 `extract_u5_board_snippets.py` 互链；原证据索引改为 **§九**。 |
