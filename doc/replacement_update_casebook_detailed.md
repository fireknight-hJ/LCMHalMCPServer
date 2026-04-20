# ReplacementUpdate 详细案例集（论文 Case Study 版）

## 目的与使用方式

- 目的：给出可直接用于论文的 `ReplacementUpdate` 前因后果案例证据。
- 证据来源：`testcases/server/**/classify_stats_output.json` 与各 testcase `db_path/lcmhal_ai_log/replacement_update_*_*.json`（每函数取最新一条）。
- 说明：文中“之前没换过/之前有换过”以 `classify_stats_output.json` 的 `has_replacement` 状态为准。

## 全局统计（当前快照）

- 最新 `ReplacementUpdate` 函数总数：**516**
- A类（新增覆盖）：**192**
- B类（已识别未替换，RU补替换）：**54**
- C类（已替换后继续修正）：**270**
- 覆盖增量（见消融结果）：+33（含 has_replacement baseline）/+40（不含 has_replacement baseline）

### 触发原因标签分布（关键词归类）

- `mmio/hw`: **223**
- `restore`: **204**
- `compile`: **203**
- `loop/hang`: **113**
- `irq`: **107**
- `boot-critical`: **64**

> 解读：RU并不只做“新增覆盖”，更多还在做“已替换函数的可编译/可运行修正”。

## A类：之前没换过，RU新增覆盖

- 语义：函数原本不在 baseline 覆盖里，RU 使其进入可处理集合，是“覆盖增量”的直接来源。

### Case 01: `LPUART_WriteBlocking` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_WriteBlocking_20260317181852.json`
- **replacement_code 长度**: `408`

**前因后果（来自 reason）**

- Avoid hardware wait loops in emulation. The original function contains loops waiting for hardware flags that may never be set in emulation. This replacement skips the wait loops since the actual data transmission is handled by HAL_BE_Out in the calling function, and returns success to allow the program to continue. This helps prevent any potential issues during program execution and exit.

### Case 02: `_exit` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update__exit_20260406205033.json`
- **replacement_code 长度**: `863`

**前因后果（来自 reason）**

- Improve _exit replacement to avoid infinite loops. The previous replacement used while(1) which could itself trigger exceptional loop detection. This version simply returns, allowing the call stack to unwind naturally. In emulation, this should allow the program to terminate cleanly without getting stuck in cleanup code that causes strchr exceptional loops.

### Case 03: `HAL_UartSendBlocking` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_HAL_UartSendBlocking_20260406203311.json`
- **replacement_code 长度**: `382`

**前因后果（来自 reason）**

- HAL_UartSendBlocking calls LPUART_WriteBlocking which contains hardware wait loops and register writes. Since LPUART_WriteBlocking has been replaced to avoid hardware access, this function just needs to return success without doing any hardware operations.

### Case 04: `LPUART_WriteBlocking` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_LPUART_WriteBlocking_20260406203209.json`
- **replacement_code 长度**: `304`

**前因后果（来自 reason）**

- LPUART_WriteBlocking contains hardware wait loops polling UART status registers and writes to UART data register. These cause emulator issues: polling loops could hang, hardware writes not needed. Replacement removes hardware access, returns success immediately.

### Case 05: `prvTaskExitError` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,compile,boot-critical`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_prvTaskExitError_20260406204823.json`
- **replacement_code 长度**: `333`

**前因后果（来自 reason）**

- prvTaskExitError contains an assertion that would always fail (configASSERT( uxCriticalNesting == ~0UL )) followed by an infinite loop. In emulation, we don't want assertion failures or infinite loops. The replacement just returns to allow graceful error handling. This function is called from xPortStartScheduler if the scheduler fails to start, but in emulation we want to avoid hard failures.

### Case 06: `vPortEndScheduler` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,boot-critical`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_vPortEndScheduler_20260406202300.json`
- **replacement_code 长度**: `241`

**前因后果（来自 reason）**

- vPortEndScheduler contains configASSERT(uxCriticalNesting == 1000UL) which always fails, causing an exceptional loop in emulation. This prevents the application from terminating normally when vTaskEndScheduler() is called. The function is essentially a stub for ports with 'nothing to return to'. In emulation context, we need to allow graceful termination without triggering assertion failures that cause exceptional loops.

### Case 07: `CLOCK_SetDiv` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NODRIVER`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SetDiv_20260218192229.json`
- **replacement_code 长度**: `778`

**前因后果（来自 reason）**

- Remove hardware-dependent wait loop that causes emulation issues. The function writes to clock divider registers and then waits for hardware handshake completion. In emulation, we can't wait for hardware signals, so we remove the wait loop while preserving the register write operation.

### Case 08: `CLOCK_SetMux` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NODRIVER`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SetMux_20260218192237.json`
- **replacement_code 长度**: `742`

**前因后果（来自 reason）**

- Remove hardware-dependent wait loop that causes emulation issues. Similar to CLOCK_SetDiv, this function writes to clock mux registers and waits for hardware handshake. In emulation, we remove the wait loop while keeping the register write operation.

### Case 09: `CLOCK_IsPllEnabled` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_IsPllEnabled_20260317174218.json`
- **replacement_code 长度**: `266`

**前因后果（来自 reason）**

- Avoid reading hardware PLL status registers in emulation. The original function reads hardware registers to check if PLL is enabled, which may not be properly initialized in emulation. This replacement returns true (enabled) to avoid issues.

### Case 10: `SystemInit` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=CORE`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw,boot-critical`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_SystemInit_20260317174728.json`
- **replacement_code 长度**: `773`

**前因后果（来自 reason）**

- Fix SystemInit to preserve SysTick disable operation as required by CRITICAL rules. The emulator needs to see SysTick register writes for proper operation. Previous replacement incorrectly removed the SysTick disable which could cause issues if SysTick was enabled by bootrom.

### Case 11: `DbgConsole_Putchar` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_DbgConsole_Putchar_20260406203109.json`
- **replacement_code 长度**: `236`

**前因后果（来自 reason）**

- DbgConsole_Putchar calls hardware-dependent putChar function pointer which attempts to write to UART hardware registers. In emulation, we don't need actual hardware UART output, so we replace it with a stub that returns success. This prevents potential emulator issues with hardware register access while allowing console output operations to continue normally.

### Case 12: `HAL_UartInit` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw,irq,boot-critical`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_HAL_UartInit_20260406203820.json`
- **replacement_code 长度**: `1947`

**前因后果（来自 reason）**

- HAL_UartInit performs hardware UART initialization including NVIC interrupt enabling. According to the critical requirements, functions that enable NVIC interrupts should not be stubbed out completely. The replacement preserves NVIC interrupt enabling (which the emulator needs to see for proper interrupt simulation) while removing hardware-specific UART initialization. This allows the emulator to properly handle UART interrupts while avoiding hardware register access issues.

### Case 13: `LPUART_WriteBlocking` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPUART_WriteBlocking_20260406214525.json`
- **replacement_code 长度**: `1042`

**前因后果（来自 reason）**

- Fix LPUART_WriteBlocking to avoid hardware wait loops in emulation. The original function contains while loops waiting for hardware status flags (LPUART_STAT_TDRE_MASK and LPUART_STAT_TC_MASK) which will hang in emulation. The replacement skips these hardware-dependent wait loops and hardware register writes while preserving the function structure and return values.

### Case 14: `CLOCK_GetOscFreq` @ `nxp/NXP_UART_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_UART_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetOscFreq_20260223155713.json`
- **replacement_code 长度**: `241`

**前因后果（来自 reason）**

- Fixing potential hardware register read in CLOCK_GetOscFreq. The function reads XTALOSC24M->LOWPWR_CTRL hardware register which would have unpredictable values in emulation. The replacement returns a default 24MHz oscillator frequency without reading hardware registers, preserving the original function signature and return type.

### Case 15: `CLOCK_GetPllFreq` @ `nxp/NXP_UART_BareMetal`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=RETURNOK`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `loop/hang,compile,mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_UART_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetPllFreq_20260223155704.json`
- **replacement_code 长度**: `1362`

**前因后果（来自 reason）**

- Fixing exceptional loop error in CLOCK_GetPllFreq. The function reads hardware registers (CCM_ANALOG->PLL_ARM, CCM_ANALOG->PLL_SYS, etc.) to calculate PLL frequencies. In emulation, these registers have unpredictable values which could cause infinite loops or incorrect calculations. The replacement returns reasonable default frequencies for each PLL type without reading hardware registers, preserving the original function signature and return type.

### Case 16: `LPUART_DisableInterrupts` @ `rtthread/imxrt1052-nxp-evk/base`

- **类别**: `A_RU_only_not_replaced`
- **分类状态**: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- **触发标签**: `mmio/hw,irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_base/lcmhal_ai_log/replacement_update_LPUART_DisableInterrupts_20260406203726.json`
- **replacement_code 长度**: `179`

**前因后果（来自 reason）**

- Replace LPUART_DisableInterrupts for consistency with LPUART_EnableInterrupts replacement. The function writes to hardware registers to disable interrupts, but in emulation we don't need to modify hardware state. The replacement skips all hardware operations while preserving the function signature.

## B类：之前已识别但没替换，RU补上替换

- 语义：函数早已被识别为重要路径（INIT/IRQ/RECV/LOOP），但没有替换；RU补上后可进入可执行修复链路。

### Case 17: `CLOCK_InitUsb2Pll` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=INIT`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_InitUsb2Pll_20260406211158.json`
- **replacement_code 长度**: `198`

**前因后果（来自 reason）**

- Simplify replacement to fix compile verification failure while maintaining correct function signature

### Case 18: `BOARD_BootClockRUN` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=INIT`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_BOARD_BootClockRUN_20260406204135.json`
- **replacement_code 长度**: `208`

**前因后果（来自 reason）**

- Update replacement to use hardcoded 600MHz value instead of BOARD_BOOTCLOCKRUN_CORE_CLOCK macro which might not be defined in all compilation contexts. This ensures the SystemCoreClock variable is properly initialized.

### Case 19: `CLOCK_InitVideoPll` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=INIT`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_CLOCK_InitVideoPll_20260406203007.json`
- **replacement_code 长度**: `433`

**前因后果（来自 reason）**

- Final minimal replacement to fix warnings and remove hardware accesses

### Case 20: `LPUART_Deinit` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=LOOP`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_LPUART_Deinit_20260406202338.json`
- **replacement_code 长度**: `710`

**前因后果（来自 reason）**

- Use the previously working replacement that was shown in GetFunctionAnalysisAndReplacement output, which should pass compilation verification.

### Case 21: `CLOCK_GetUsb1PfdFreq` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=INIT`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetUsb1PfdFreq_20260406211332.json`
- **replacement_code 长度**: `367`

**前因后果（来自 reason）**

- Final attempt: simple replacement that matches function signature, uses parameter (with void cast to avoid unused parameter warning), and returns reasonable simulated frequency based on original calculation logic.

### Case 22: `LPI2C_CommonIRQHandler` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=IRQ`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw,irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPI2C_CommonIRQHandler_20260406213438.json`
- **replacement_code 长度**: `433`

**前因后果（来自 reason）**

- Fix LPI2C_CommonIRQHandler by removing hardware register checks (base->MCR and base->SCR) while preserving function pointer calls and SDK_ISR_EXIT_BARRIER as required for IRQ classification. This resolves compilation errors caused by previous replacement issues.

### Case 23: `LPI2C_MasterStart` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=INIT`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPI2C_MasterStart_20260406212913.json`
- **replacement_code 长度**: `163`

**前因后果（来自 reason）**

- Using simplest possible replacement that returns success to avoid any compilation issues with hardware register accesses. This matches the existing replacement pattern.

### Case 24: `LPI2C_MasterTransferBlocking` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=RECV`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPI2C_MasterTransferBlocking_20260406212051.json`
- **replacement_code 长度**: `377`

**前因后果（来自 reason）**

- Extremely simplified version that should compile without any issues. Removes all complex logic and hardware dependencies.

### Case 25: `LPUART_TransferHandleSendDataEmpty` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=IRQ`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `loop/hang,irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferHandleSendDataEmpty_20260406202651.json`
- **replacement_code 长度**: `1247`

**前因后果（来自 reason）**

- Simplified version that processes data once instead of in a while loop. Removes hardware-dependent loop while maintaining data pointer updates and interrupt control.

### Case 26: `LPUART_TransferHandleIDLEReady` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=IRQ`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `irq,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_LPUART_TransferHandleIDLEReady_20260406202517.json`
- **replacement_code 长度**: `1489`

**前因后果（来自 reason）**

- Final clean replacement: removed all hardware-dependent operations while preserving callback logic and state management. Simplified the FIFO simulation to just check rxDataSize state. This addresses the original issue with non-existent HAL_BE_In function and follows IRQ replacement pattern.

### Case 27: `LPUART_TransferHandleReceiveDataFull` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=RECV`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `compile,irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferHandleReceiveDataFull_20260406213241.json`
- **replacement_code 长度**: `1250`

**前因后果（来自 reason）**

- Simplified replacement to avoid complex logic that might cause compilation issues. Preserves only callback logic and interrupt protection pattern while removing all hardware operations.

### Case 28: `LPUART_TransferHandleSendDataEmpty` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=IRQ`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferHandleSendDataEmpty_20260406213346.json`
- **replacement_code 长度**: `784`

**前因后果（来自 reason）**

- Minimal replacement that skips all hardware operations while maintaining basic functionality - updates buffer pointers and simulates interrupt protection

### Case 29: `LPUART_TransferSendNonBlocking` @ `nxp/NXP_I2C_BareMetal`

- **类别**: `B_in_baseline_not_replaced`
- **分类状态**: `function_type=IRQ`, `has_replacement=False`, `in_baseline=True`
- **触发标签**: `mmio/hw,irq`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferSendNonBlocking_20260406213036.json`
- **replacement_code 长度**: `1130`

**前因后果（来自 reason）**

- Applied correct replacement that removes hardware register access while preserving 16-bit data handling and interrupt protection. The hardware line is removed with a comment explaining it.

## C类：之前已替换，RU继续修正

- 语义：函数之前已有替换，但替换版本在编译、验证或运行中暴露问题，RU负责迭代修正。

### Case 30: `CLOCK_GetPllFreq` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetPllFreq_20260317173954.json`
- **replacement_code 长度**: `297`

**前因后果（来自 reason）**

- Avoid reading hardware PLL registers in emulation. The original function reads hardware registers to determine PLL frequency, which may not be properly initialized in emulation. This replacement returns a fixed reasonable frequency (600 MHz) to avoid issues.

### Case 31: `CLOCK_GetSemcFreq` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetSemcFreq_20260406203408.json`
- **replacement_code 长度**: `425`

**前因后果（来自 reason）**

- Fixed replacement to properly simulate the original function's logic. The original function reads hardware registers (CCM->CBCDR) to determine clock source and divider settings. This replacement simulates the default configuration path (Periph_clk -> SEMC Clock) with a divider of 1, which is a reasonable simulation that avoids hardware register access while maintaining the function's expected behavior.

### Case 32: `CLOCK_SetClockOutput2` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SetClockOutput2_20260406203316.json`
- **replacement_code 长度**: `481`

**前因后果（来自 reason）**

- Updated replacement to properly use function parameters to avoid unused parameter warnings while removing hardware-specific MMIO operations. The function signature matches the original exactly.

### Case 33: `CLOCK_SwitchOsc` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SwitchOsc_20260406202947.json`
- **replacement_code 长度**: `110`

**前因后果（来自 reason）**

- Fix replacement to include parameter handling and avoid unused parameter warnings. The original function takes clock_osc_t osc parameter which must be included in the replacement.

### Case 34: `LPUART_Deinit` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=LOOP`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_Deinit_20260406202811.json`
- **replacement_code 长度**: `727`

**前因后果（来自 reason）**

- Fix compilation issues by properly handling UART_RETRY_TIMES conditional compilation and maintaining original function structure while removing hardware accesses.

### Case 35: `LPUART_Init` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_Init_20260406202527.json`
- **replacement_code 长度**: `354`

**前因后果（来自 reason）**

- Restoring working replacement for LPUART_Init that avoids all hardware operations and returns success for emulation. This was previously working according to the system records.

### Case 36: `LPUART_TransferHandleReceiveDataFull` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=IRQ`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferHandleReceiveDataFull_20260406202615.json`
- **replacement_code 长度**: `4461`

**前因后果（来自 reason）**

- Removed non-existent HAL_BE_In() calls and replaced with simple simulation logic. Maintained original function structure while removing hardware dependencies.

### Case 37: `SystemCoreClockUpdate` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_SystemCoreClockUpdate_20260317173341.json`
- **replacement_code 长度**: `320`

**前因后果（来自 reason）**

- Prevent division by zero and other calculation errors in clock frequency calculations. The original function reads hardware clock registers and performs division operations that may fail in emulation when hardware is not properly initialized. This replacement sets SystemCoreClock to 600 MHz (a reasonable value for this platform) to avoid these issues.

### Case 38: `CLOCK_EnableUsbhs1PhyPllClock` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_EnableUsbhs1PhyPllClock_20260406203607.json`
- **replacement_code 长度**: `165`

**前因后果（来自 reason）**

- Add parameter usage to avoid unused parameter warnings while keeping the function simple and skipping hardware initialization.

### Case 39: `CLOCK_InitSysPfd` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_InitSysPfd_20260406203320.json`
- **replacement_code 长度**: `468`

**前因后果（来自 reason）**

- Simplify replacement to match current working version, removing hardware register accesses while preserving function signature and avoiding compilation warnings.

### Case 40: `CLOCK_InitSysPll` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_InitSysPll_20260406211017.json`
- **replacement_code 长度**: `106`

**前因后果（来自 reason）**

- Fix conflicting types error by providing correct function signature that matches header declaration

### Case 41: `GPIO_PinInit` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_GPIO_PinInit_20260406203134.json`
- **replacement_code 长度**: `636`

**前因后果（来自 reason）**

- Simplified replacement to fix compile verification failure. Removed complex conditional logic that might cause issues, kept only essential clock control code and added comment about skipping hardware access.

### Case 42: `LPUART_TransferStopRingBuffer` @ `nxp/NXP_FATFS_BareMetal`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,mmio/hw`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_LPUART_TransferStopRingBuffer_20260406202408.json`
- **replacement_code 长度**: `578`

**前因后果（来自 reason）**

- Simplify comment format to avoid potential compilation issues. Remove detailed register operation description from comment.

### Case 43: `CLOCK_EnableUsbhs1Clock` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_CLOCK_EnableUsbhs1Clock_20260406203514.json`
- **replacement_code 长度**: `602`

**前因后果（来自 reason）**

- Fix replacement to match original function signature exactly, including variable declaration. The original function declares uint32_t i = 0; at the beginning, which should be preserved in the replacement to avoid compilation issues.

### Case 44: `CLOCK_InitArmPll` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_CLOCK_InitArmPll_20260406202759.json`
- **replacement_code 长度**: `138`

**前因后果（来自 reason）**

- Simplified replacement that handles unused parameter and provides minimal simulation stub

### Case 45: `CLOCK_InitAudioPll` @ `nxp/NXP_FATFS_FreeRTOS`

- **类别**: `C_already_replaced_refined`
- **分类状态**: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- **触发标签**: `compile,restore`
- **证据文件**: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_CLOCK_InitAudioPll_20260406202919.json`
- **replacement_code 长度**: `526`

**前因后果（来自 reason）**

- Fix compilation errors by providing a clean replacement that matches original function signature exactly and removes all hardware operations while preserving function structure.

## 写论文时可直接引用的结论模板

- `ReplacementUpdate` 具有双重作用：
  1) 对 A/B 类函数提供覆盖增量（新增进入可处理集合）；
  2) 对 C 类函数提供质量增量（修正已有替换，提升编译/运行稳定性）。
- 在本快照中，A类+B类构成“净新增覆盖”的主要来源；C类占比更高，说明系统在后期更多执行“替换质量修复”。
- 因此，评估RU时应同时报告：覆盖增量 + 下游成功率变化。

## 复现实验脚本

```bash
python scripts/replacement_update_ablation.py --root testcases/server --output-prefix run/replacement_update_ablation_server
python scripts/replacement_update_ablation.py --root testcases/server --exclude-has-replacement --output-prefix run/replacement_update_ablation_server_no_hasrep
```