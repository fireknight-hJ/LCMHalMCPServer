# ReplacementUpdate Case Files

这个目录按“一个案例一份文档”组织，便于论文逐条引用。

每个案例固定结构：

- 背景（demo、函数、分类状态）
- 触发问题（仿真中的具体风险）
- ReplacementUpdate 动作（做了什么替换/修正）
- 结果意义（属于覆盖增量还是质量增量）
- 证据路径（`replacement_update_*.json`）

## 分类口径（8类）

与 `INDEX_BY_CATEGORY.md` 保持一致，论文建议直接引用这套分类：

- **C1 - 替换阶段漏生成兜底类**  
  典型是 `INIT/LOOP` 等函数已识别，但初版替换缺失或不可用，RU 补齐。
- **C2 - 静态分析漏采接口补替换类**  
  函数不在静态候选中（或边界外），运行暴露问题后 RU 介入修复。
- **C3 - 卡住/死循环修复类**  
  处理 wait loop、polling loop、exceptional loop、超时等待等卡死问题。
- **C4 - MMIO/硬件访问隔离类**  
  将寄存器读写改为仿真可接受行为，减少硬件依赖，保留接口语义。
- **C5 - IRQ/中断路径保真修复类**  
  保留必要 ISR/NVIC 语义，同时去除硬件条件造成的不稳定路径。
- **C6 - 启动关键路径保护类**  
  覆盖 `SystemInit/SysTick/HAL_InitTick/VTOR` 等启动关键路径修正。
- **C7 - 编译/验证失败回修类**  
  修复签名不匹配、宏/语法问题、warning 导致的 verify/build 失败。
- **C8 - 过度替换回退/细化类**  
  对已替换函数做回退或细化，提升稳定性与行为一致性。

## 案例清单

- `case_01_loop_hang_lpuart_writeblocking.md` - Loop/Hang 类
- `case_02_mmio_access_clock_getoscfreq.md` - MMIO/硬件寄存器访问类
- `case_03_irq_path_hal_uartinit.md` - IRQ/中断路径类
- `case_04_boot_critical_systeminit.md` - 启动关键路径类
- `case_05_compile_fix_clock_initaudiopll.md` - 编译验证修复类

- `case_06_clock_setdiv.md` - Loop/Hang + MMIO wait loop
- `case_07_clock_setmux.md` - Loop/Hang + MMIO wait loop
- `case_08_prvtaskexiterror.md` - FreeRTOS exit path exceptional loop
- `case_09_vportendscheduler.md` - Scheduler end path exceptional loop
- `case_10_clock_getpllfreq.md` - PLL status polling loop in emulation
- `case_11_lpi2c_commonirqhandler.md` - IRQ handler replacement correction
- `case_12_clock_initaudiopll.md` - Compile verification refinement

- `case_13_imxrt_putc.md` - rtthread/imxrt1052-nxp-evk/uart / imxrt_putc
- `case_14_edma_installtcd.md` - rtthread/imxrt1052-nxp-evk/uart / EDMA_InstallTCD
- `case_15_xbara_init.md` - rtthread/imxrt1052-nxp-evk/uart / XBARA_Init
- `case_16_imxrt_pin_mode.md` - rtthread/imxrt1052-nxp-evk/uart / imxrt_pin_mode
- `case_17_lpuart_init.md` - rtthread/imxrt1052-nxp-evk/uart / LPUART_Init
- `case_18_edma_settransferconfig.md` - rtthread/imxrt1052-nxp-evk/uart / EDMA_SetTransferConfig
- `case_19_gpio_pininit.md` - rtthread/imxrt1052-nxp-evk/uart / GPIO_PinInit
- `case_20_edma_submittransfer.md` - rtthread/imxrt1052-nxp-evk/uart / EDMA_SubmitTransfer
- `case_21_lpuart_disableinterrupts.md` - rtthread/imxrt1052-nxp-evk/uart / LPUART_DisableInterrupts
- `case_22_lpuart_enableinterrupts.md` - rtthread/imxrt1052-nxp-evk/uart / LPUART_EnableInterrupts
- `case_23_lpuart_getstatusflags.md` - rtthread/imxrt1052-nxp-evk/uart / LPUART_GetStatusFlags
- `case_24_edma_aborttransfer.md` - rtthread/imxrt1052-nxp-evk/uart / EDMA_AbortTransfer

- `case_25_uart_sam0_poll_out.md` - zephyr/atmel/fs_littlefs_atsame54 / uart_sam0_poll_out / A_RU_only_not_replaced
- `case_26_flash_sam0_erase.md` - zephyr/atmel/fs_littlefs_atsame54 / flash_sam0_erase / A_RU_only_not_replaced
- `case_27_flash_sam0_read.md` - zephyr/atmel/fs_littlefs_atsame54 / flash_sam0_read / A_RU_only_not_replaced
- `case_28_sam0_eic_disable_interrupt.md` - zephyr/atmel/fs_littlefs_atsame54 / sam0_eic_disable_interrupt / A_RU_only_not_replaced
- `case_29_sys_clock_isr.md` - zephyr/atmel/fs_littlefs_atsame54 / sys_clock_isr / A_RU_only_not_replaced
- `case_30_uart_sam0_irq_rx_ready.md` - zephyr/atmel/fs_littlefs_atsame54 / uart_sam0_irq_rx_ready / A_RU_only_not_replaced
- `case_31_flash_sam0_write_page.md` - zephyr/atmel/fs_littlefs_atsame54 / flash_sam0_write_page / C_already_replaced_refined
- `case_32_flash_sam0_write_protection.md` - zephyr/atmel/fs_littlefs_atsame54 / flash_sam0_write_protection / C_already_replaced_refined

## Case Study（精选详解）

- `casestudy/case_01_lpuart_writeblocking.md` - NXP_FATFS_BareMetal / LPUART_WriteBlocking（本轮修复闭环）
- `casestudy/case_18_edma_settransferconfig.md` - rtthread/imxrt1052-nxp-evk/uart / EDMA_SetTransferConfig
