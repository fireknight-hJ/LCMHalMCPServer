# ReplacementUpdate Casebook

## 1. This Document Solves What

This document gives concrete, data-backed examples for:

- why `ReplacementUpdate` appears,
- what kinds of functions trigger it,
- differences between:
  - functions not previously replaced,
  - functions previously identified but not replaced,
  - functions already replaced and then revised.

Data source in this repo:

- `testcases/server/**/classify_stats_output.json`
- `db_path/lcmhal_ai_log/replacement_update_*_*.json` (latest per function)
- Aggregated result files:
  - `run/replacement_update_ablation_server.json`
  - `run/replacement_update_ablation_server_no_hasrep.json`

## 2. Key Numbers (Current Snapshot)

- Total demos scanned: **39**
- Total latest `ReplacementUpdate` functions: **516**
- Coverage increment brought by `ReplacementUpdate`:
  - Baseline includes `has_replacement=true`: **+33** (`+1.50%` over baseline)
  - Baseline excludes `has_replacement=true`: **+40** (`+1.83%` over baseline)
- `RU-only` (not in baseline but added by RU): **192**
- `RU-overlap` (already in baseline, RU used to refine): **324**

### Reason category distribution (latest 516 functions, keyword-based)

- compile/warning fix: **203**
- MMIO/hardware-access isolation: **186**
- restore/revert original implementation: **137**
- loop/hang/timeout mitigation: **113**
- IRQ/handler related adjustment: **107**
- critical boot-time path (VTOR/SysTick/SystemInit/HAL_InitTick): **64**

## 3. Type A - Previously Not Replaced, Added By RU

Definition:

- `has_replacement=false` before,
- function not in baseline set,
- but gets included because `has_replacement_update=true`.

This is the most direct evidence of RU incremental contribution.

### Typical reasons

- Remove hardware wait loops to avoid exceptional loop.
- Replace direct MMIO register access with emulation-safe behavior.
- Fix runtime deadlocks in polling paths.
- Stabilize boot-time functions in emulator environment.

### Concrete examples

| Demo | Function | Prior state | Why RU appeared (from reason field) |
| --- | --- | --- | --- |
| `rtthread/imxrt1052-nxp-evk/uart` | `imxrt_putc` | not replaced | remove hardware wait loop to avoid exceptional loop |
| `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_DisableInterrupts` | not replaced | remove hardware register writes in emulation |
| `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_EnableInterrupts` | not replaced | avoid enabling hardware interrupts in emulator |
| `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_GetStatusFlags` | not replaced | simulate status flags to avoid wait-loop hang |
| `rtthread/imxrt1052-nxp-evk/base` | `imxrt_putc` | not replaced | remove hardware-dependent polling loop |
| `rtthread/imxrt1052-nxp-evk/base` | `LPUART_GetStatusFlags` | not replaced | avoid hardware reads that block flow |
| `rtthread/imxrt1052-nxp-evk/fatfs` | `imxrt_getc` | not replaced | align with replaced status-flag behavior |
| `rtthread/imxrt1052-nxp-evk/fatfs` | `GPIO_PinWrite` | not replaced | avoid MMIO write side effects in emulator |
| `rtthread/imxrt1052-nxp-evk/fatfs` | `SysTick_Config` | not replaced | critical scheduling path requires emulator-safe handling |
| `rtthread/stm32f401-st-nucleo/eth` | `SystemInit` | not replaced | fix critical VTOR/vector-table setup path |
| `rtthread/stm32f401-st-nucleo/eth` | `idle_thread_entry` | not replaced | add loop guard to avoid exceptional loop detection |
| `rtthread/stm32f401-st-nucleo/eth` | `UART_WaitOnFlagUntilTimeout` | not replaced | break hardware flag wait-loop dependency |
| `rtthread/stm32f401-st-nucleo/eth` | `HAL_UART_IRQHandler` | not replaced | replace hardware-dependent IRQ path |
| `rtthread/stm32f401-st-nucleo/eth` | `UART_Transmit_IT` | not replaced | remove interrupt path hardware dependency |
| `rtthread/stm32f401-st-nucleo/eth` | `HAL_InitTick` | not replaced | critical tick init path adapted for emulation |

## 4. Type B - Previously Identified, But Not Replaced; RU Adds Replacement

Definition:

- Function already falls in baseline by type (`INIT/IRQ/RECV/LOOP`),
- but `has_replacement=false` before,
- RU adds concrete replacement/update.

Count in current data: **54**.

### Why this happens

- Classifier identified function role correctly, but initial replacement was absent.
- Build verification later exposed syntax/signature/conditional-compile issues.
- RU supplies the missing replacement or corrected version.

### Concrete examples

| Demo | Function | Type | Why RU appeared (from reason field) |
| --- | --- | --- | --- |
| `rtthread/imxrt1052-nxp-evk/base` | `imxrt_pin_mode` | `INIT` | fixed malformed `LOG_D` macro string split issue |
| `rtthread/imxrt1052-nxp-evk/base` | `CLOCK_InitUsb1Pll` | `INIT` | add missing replacement for PLL init consistency |
| `rtthread/imxrt1052-nxp-evk/i2c` | `CLOCK_InitArmPll` | `INIT` | simplify init replacement to avoid compile issues |
| `rtthread/imxrt1052-nxp-evk/i2c` | `LPI2C_CommonIRQHandler` | `IRQ` | resolve replacement verification/compile failure |
| `rtthread/imxrt1052-nxp-evk/i2c` | `LPI2C_MasterWaitForTxReady` | `LOOP` | fix `#if/#endif` structure error in replacement |
| `rtthread/imxrt1052-nxp-evk/i2c` | `LPI2C_MasterReceive` | `RECV` | simplify to avoid syntax and dependency issues |
| `rtthread/imxrt1052-nxp-evk/i2c` | `LPI2C_MasterTransferBlocking` | `RECV` | fix unused variable warnings with safe casts |
| `rtthread/imxrt1052-nxp-evk/fatfs` | `CLOCK_InitArmPll` | `INIT` | remove polling loops/hardware writes for emulation |
| `rtthread/stm32f401-st-nucleo/i2c` | `HAL_RCC_ClockConfig` | `INIT` | restore structure to keep expected SysTick sequence |
| `nxp/NXP_UART_FreeRTOS` | `uart_task` | `RECV` | bound loop iterations to avoid exceptional loop |
| `nxp/NXP_UART_FreeRTOS` | `LPUART_WriteBlocking` | `LOOP` | remove hardware polling on TDRE/TC flags |
| `nxp/NXP_UART_FreeRTOS` | `LPUART_WriteBlocking16bit` | `LOOP` | same class of hardware polling loop fix |
| `nxp/NXP_UART_FreeRTOS` | `LPUART_TransferReceiveNonBlocking` | `RECV` | emulate successful non-blocking receive path |
| `nxp/NXP_FATFS_BareMetal` | `LPUART_TransferHandleSendDataEmpty` | `IRQ` | simplify while-loop to one-shot safe processing |
| `nxp/NXP_LwIP_BareMetal` | `CLOCK_InitEnetPll` | `INIT` | fix function signature mismatch with header |

## 5. Type C - Previously Replaced, RU Further Refines

Definition:

- `has_replacement=true` already,
- function in baseline already,
- RU still appears to fix/iterate replacement quality.

This is the "quality-improvement" side of RU, not coverage expansion.

### Typical reasons

- Fix compile warnings/errors (`unused`, syntax, type mismatch).
- Restore original implementation when previous replacement was over-aggressive.
- Add null checks / guard logic.
- Keep emulator compatibility while preserving API behavior.

### Concrete examples

| Demo | Function | Type | Why RU appeared (from reason field) |
| --- | --- | --- | --- |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_InstallTCD` | `INIT` | restore original implementation after verification failure |
| `rtthread/imxrt1052-nxp-evk/uart` | `XBARA_Init` | `INIT` | fix simulation replacement syntax issues |
| `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_Init` | `INIT` | remove unused variables causing warnings |
| `rtthread/imxrt1052-nxp-evk/uart` | `CLOCK_InitAudioPll` | `INIT` | remove unused variable and stabilize build |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_SetTransferConfig` | `INIT` | provide stub without hardware register access |
| `rtthread/imxrt1052-nxp-evk/uart` | `GPIO_PinInit` | `INIT` | resolve unused symbol warnings in replacement |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_SubmitTransfer` | `RETURNOK` | restore original to ensure correct functionality |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_AbortTransfer` | `INIT` | add null-pointer checks for safety |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_Init` | `INIT` | clean conditional compilation and tmp variable usage |
| `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_StartTransfer` | `INIT` | refine hardware-write removal strategy |
| `rtthread/imxrt1052-nxp-evk/base` | `GPIO_PinInit` | `INIT` | simplify replacement and add proper void casts |
| `rtthread/imxrt1052-nxp-evk/base` | `CLOCK_DeinitAudioPll` | `INIT` | keep behavior while skipping hardware power-down |
| `rtthread/imxrt1052-nxp-evk/base` | `CLOCK_InitRcOsc24M` | `INIT` | simplify body to avoid compile instability |
| `rtthread/imxrt1052-nxp-evk/base` | `CLOCK_SwitchOsc` | `INIT` | fix signature/parameter usage to remove warnings |
| `rtthread/imxrt1052-nxp-evk/base` | `CLOCK_InitUsb1Pfd` | `INIT` | add missing declarations and correct parameter handling |

## 6. Why `replacement_update_count` Can Be Large But Increment Small

In current data:

- replacement-update logs across demos: **516**
- net new coverage increment: **33 ~ 40** (depending on baseline rule)

Interpretation:

- Many RU events are **refinements** on already-covered functions (Type C).
- RU contributes in two ways:
  1. **coverage expansion** (Type A/B, measured by `RU_Increment`),
  2. **quality stabilization** (Type C, not reflected by coverage-only metric).

So when validating RU usefulness, report both:

- coverage increment (`RU_Increment`),
- and downstream build/emulate success deltas (next experiment stage).

## 7. Suggested Next Step For Stronger Evidence

To prove "RU is useful" beyond coverage:

- Run pipeline-level A/B:
  - A: normal flow (with RU)
  - B: RU disabled
- Keep same testcase set, rounds, timeout, model, and parallelism.
- Compare:
  - build success rate,
  - emulate success rate,
  - task success rate,
  - plus coverage increment from this casebook.

