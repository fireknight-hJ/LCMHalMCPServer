# ReplacementUpdate Cases Index (8-Class Taxonomy)

- Total cases: **32**
- This index follows the agreed 8 classes for paper writing.

## C1 - Missing INIT/LOOP Fallback In Replacement Stage

Meaning: function is identified (often INIT/LOOP family), but replacement was not generated or not usable; RU fills the gap.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_11_lpi2c_commonirqhandler.md` | `nxp/NXP_I2C_BareMetal` | `LPI2C_CommonIRQHandler` |
| `case_21_lpuart_disableinterrupts.md` | `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_DisableInterrupts` |
| `case_22_lpuart_enableinterrupts.md` | `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_EnableInterrupts` |
| `case_23_lpuart_getstatusflags.md` | `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_GetStatusFlags` |

## C2 - Static Analysis Missed Interface, Runtime-Driven Replacement

Meaning: function is outside static candidate set (or typed NA/NODRIVER), but runtime/emulation failures trigger RU.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_01_loop_hang_lpuart_writeblocking.md` | `nxp/NXP_FATFS_BareMetal` | `LPUART_WriteBlocking` |
| `case_02_mmio_access_clock_getoscfreq.md` | `nxp/NXP_UART_BareMetal` | `CLOCK_GetOscFreq` |
| `case_03_irq_path_hal_uartinit.md` | `nxp/NXP_FATFS_FreeRTOS` | `HAL_UartInit` |
| `case_13_imxrt_putc.md` | `rtthread/imxrt1052-nxp-evk/uart` | `imxrt_putc` |

## C3 - Loop/Hang Mitigation

Meaning: replacement is triggered to break polling loops, exceptional loops, or deadlock-like wait patterns.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_06_clock_setdiv.md` | `nxp/NXP_I2C_BareMetal` | `CLOCK_SetDiv` |
| `case_07_clock_setmux.md` | `nxp/NXP_I2C_BareMetal` | `CLOCK_SetMux` |
| `case_08_prvtaskexiterror.md` | `nxp/NXP_FATFS_FreeRTOS` | `prvTaskExitError` |
| `case_09_vportendscheduler.md` | `nxp/NXP_FATFS_FreeRTOS` | `vPortEndScheduler` |
| `case_25_uart_sam0_poll_out.md` | `zephyr/atmel/fs_littlefs_atsame54` | `uart_sam0_poll_out` |

## C4 - MMIO/Hardware Access Isolation

Meaning: replace direct register read/write with emulation-safe behavior while keeping API semantics.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_10_clock_getpllfreq.md` | `nxp/NXP_UART_BareMetal` | `CLOCK_GetPllFreq` |
| `case_26_flash_sam0_erase.md` | `zephyr/atmel/fs_littlefs_atsame54` | `flash_sam0_erase` |
| `case_27_flash_sam0_read.md` | `zephyr/atmel/fs_littlefs_atsame54` | `flash_sam0_read` |
| `case_31_flash_sam0_write_page.md` | `zephyr/atmel/fs_littlefs_atsame54` | `flash_sam0_write_page` |
| `case_32_flash_sam0_write_protection.md` | `zephyr/atmel/fs_littlefs_atsame54` | `flash_sam0_write_protection` |

## C5 - IRQ Path Preservation / Repair

Meaning: keep necessary ISR/interrupt semantics while removing hardware-dependent checks or side effects.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_03_irq_path_hal_uartinit.md` | `nxp/NXP_FATFS_FreeRTOS` | `HAL_UartInit` |
| `case_11_lpi2c_commonirqhandler.md` | `nxp/NXP_I2C_BareMetal` | `LPI2C_CommonIRQHandler` |
| `case_28_sam0_eic_disable_interrupt.md` | `zephyr/atmel/fs_littlefs_atsame54` | `sam0_eic_disable_interrupt` |
| `case_29_sys_clock_isr.md` | `zephyr/atmel/fs_littlefs_atsame54` | `sys_clock_isr` |
| `case_30_uart_sam0_irq_rx_ready.md` | `zephyr/atmel/fs_littlefs_atsame54` | `uart_sam0_irq_rx_ready` |

## C6 - Boot-Critical Path Protection

Meaning: RU protects startup-critical behavior (e.g., SystemInit/SysTick/VTOR family) from over-stubbing.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_04_boot_critical_systeminit.md` | `nxp/NXP_FATFS_BareMetal` | `SystemInit` |
| `case_09_vportendscheduler.md` | `nxp/NXP_FATFS_FreeRTOS` | `vPortEndScheduler` |
| `case_08_prvtaskexiterror.md` | `nxp/NXP_FATFS_FreeRTOS` | `prvTaskExitError` |

## C7 - Compile/Verification Failure Fix

Meaning: RU is triggered by signature mismatch, macro/syntax issue, warning escalation, or verification failure.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_05_compile_fix_clock_initaudiopll.md` | `nxp/NXP_FATFS_FreeRTOS` | `CLOCK_InitAudioPll` |
| `case_12_clock_initaudiopll.md` | `nxp/NXP_FATFS_FreeRTOS` | `CLOCK_InitAudioPll` |
| `case_16_imxrt_pin_mode.md` | `rtthread/imxrt1052-nxp-evk/uart` | `imxrt_pin_mode` |
| `case_17_lpuart_init.md` | `rtthread/imxrt1052-nxp-evk/uart` | `LPUART_Init` |

## C8 - Over-Replacement Rollback / Refinement

Meaning: previous replacement is too aggressive or unstable; RU restores original parts or refines implementation.

| CaseFile | Demo | Function |
| --- | --- | --- |
| `case_14_edma_installtcd.md` | `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_InstallTCD` |
| `case_15_xbara_init.md` | `rtthread/imxrt1052-nxp-evk/uart` | `XBARA_Init` |
| `case_18_edma_settransferconfig.md` | `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_SetTransferConfig` |
| `case_19_gpio_pininit.md` | `rtthread/imxrt1052-nxp-evk/uart` | `GPIO_PinInit` |
| `case_20_edma_submittransfer.md` | `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_SubmitTransfer` |
| `case_24_edma_aborttransfer.md` | `rtthread/imxrt1052-nxp-evk/uart` | `EDMA_AbortTransfer` |
