## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/rtthread/imxrt1052-nxp-evk/fatfs`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `BOARD_BootClockRUN` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/clock_config.c` | 156 | 2 |
| `BOARD_InitPins` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/pin_mux.c` | 50 | 1 |
| `CLOCK_DeinitArmPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 500 | 1 |
| `CLOCK_DeinitUsb1Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 575 | 1 |
| `CLOCK_DeinitUsb2Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 608 | 2 |
| `CLOCK_DeinitVideoPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 781 | 2 |
| `CLOCK_DisableUsbhs0PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 466 | 1 |
| `CLOCK_DisableUsbhs1PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1207 | 1 |
| `CLOCK_EnableUsbhs0PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 442 | 2 |
| `CLOCK_EnableUsbhs1Clock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 419 | 1 |
| `CLOCK_EnableUsbhs1PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1189 | 1 |
| `CLOCK_InitArmPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 479 | 2 |
| `CLOCK_InitAudioPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 620 | 1 |
| `CLOCK_InitEnetPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 793 | 1 |
| `CLOCK_InitExternalClk` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 150 | 1 |
| `CLOCK_InitRcOsc24M` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 197 | 1 |
| `CLOCK_InitSysPfd` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1038 | 1 |
| `CLOCK_InitSysPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 512 | 1 |
| `CLOCK_InitUsb1Pfd` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1075 | 1 |
| `CLOCK_InitUsb1Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 554 | 1 |
| `CLOCK_InitUsb2Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 587 | 1 |
| `CLOCK_InitVideoPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 707 | 1 |
| `CLOCK_SetDiv` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.h` | 919 | 1 |
| `GPIO_PinInit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_gpio.c` | 71 | 1 |
| `GPIO_PinWrite` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_gpio.c` | 105 | 1 |
| `GetUartSrcFreq` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c` | 559 | 1 |
| `LPUART_Deinit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 452 | 1 |
| `LPUART_EnableInterrupts` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 659 | 1 |
| `LPUART_GetStatusFlags` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 743 | 2 |
| `LPUART_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 236 | 1 |
| `LPUART_ReadByte` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.h` | 601 | 1 |
| `LPUART_WriteByte` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.h` | 587 | 1 |
| `SysTick_Config` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/CMSIS/Include/core_cm7.h` | 2553 | 1 |
| `SystemCoreClockUpdate` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/system_MIMXRT1052.c` | 128 | 1 |
| `SystemInit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/system_MIMXRT1052.c` | 73 | 2 |
| `XBARA_Deinit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c` | 88 | 1 |
| `XBARA_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c` | 73 | 2 |
| `XBARB_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbarb.c` | 73 | 1 |
| `imxrt_getc` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c` | 701 | 2 |
| `imxrt_pin_mode` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_gpio.c` | 522 | 2 |
| `imxrt_putc` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c` | 688 | 2 |

## 2. 各函数替换详情

### BOARD_BootClockRUN

```text
=== BOARD_BootClockRUN 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/clock_config.c
- 行号：156
- 函数内容：void BOARD_BootClockRUN(void)
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
    /* Set PERCLK_PODF. */
    CLOCK_SetDiv(kCLOCK_PerclkDiv, 1);
    /* Disable USDHC1 clock gate. */
    CLOCK_DisableClock(kCLOCK_Usdhc1);
    /* Set USDHC1_PODF. */
    CLOCK_SetDiv(kCLOCK_Usdhc1Div, 1);
    /* Set Usdhc1 clock source. */
    CLOCK_SetMux(kCLOCK_Usdhc1Mux, 0);
    /* Disable USDHC2 clock gate. */
    CLOCK_DisableClock(kCLOCK_Usdhc2);
    /* Set USDHC2_PODF. */
    CLOCK_SetDiv(kCLOCK_Usdhc2Div, 1);
    /* Set Usdhc2 clock source. */
    CLOCK_SetMux(kCLOCK_Usdhc2Mux, 0);
    /* In SDK projects, SDRAM (configured by SEMC) will be initialized in either debug script or dcd.
     * With this macro SKIP_SYSCLK_INIT, system pll (selected to be SEMC source clock in SDK projects) will be left unchanged.
     * Note: If another clock source is selected for SEMC, user may want to avoid changing that clock as well.*/
#ifndef SKIP_SYSCLK_INIT
    /* Disable Semc clock gate. */
    CLOCK_DisableClock(kCLOCK_Semc);
    /* Set SEMC_PODF. */
    CLOCK_SetDiv(kCLOCK_SemcDiv, 7);
    /* Set Semc alt clock source. */
    CLOCK_SetMux(kCLOCK_SemcAltMux, 0);
    /* Set Semc clock source. */
    CLOCK_SetMux(kCLOCK_SemcMux, 0);
#endif
    /* In SDK projects, external flash (configured by FLEXSPI) will be initialized by dcd.
     * With this macro XIP_EXTERNAL_FLASH, usb1 pll (selected to be FLEXSPI clock source in SDK projects) will be left unchanged.
     * Note: If another clock source is selected for FLEXSPI, user may want to avoid changing that clock as well.*/
#if !(defined(XIP_EXTERNAL_FLASH) && (XIP_EXTERNAL_FLASH == 1))
    /* Disable Flexspi clock gate. */
    CLOCK_DisableClock(kCLOCK_FlexSpi);
    /* Set FLEXSPI_PODF. */
    CLOCK_SetDiv(kCLOCK_FlexspiDiv, 0);
    /* Set Flexspi clock source. */
    CLOCK_SetMux(kCLOCK_FlexspiMux, 3);
#endif
    /* Disable CSI clock gate. */
    CLOCK_DisableClock(kCLOCK_Csi);
    /* Set CSI_PODF. */
    CLOCK_SetDiv(kCLOCK_CsiDiv, 1);
    /* Set Csi clock source. */
    CLOCK_SetMux(kCLOCK_CsiMux, 0);
    /* Disable LPSPI clock gate. */
    CLOCK_DisableClock(kCLOCK_Lpspi1);
    CLOCK_DisableClock(kCLOCK_Lpspi2);
    CLOCK_DisableClock(kCLOCK_Lpspi3);
    CLOCK_DisableClock(kCLOCK_Lpspi4);
    /* Set LPSPI_PODF. */
    CLOCK_SetDiv(kCLOCK_LpspiDiv, 4);
    /* Set Lpspi clock source. */
    CLOCK_SetMux(kCLOCK_LpspiMux, 2);
    /* Disable TRACE clock gate. */
    CLOCK_DisableClock(kCLOCK_Trace);
    /* Set TRACE_PODF. */
    CLOCK_SetDiv(kCLOCK_TraceDiv, 2);
    /* Set Trace clock source. */
    CLOCK_SetMux(kCLOCK_TraceMux, 2);
    /* Disable SAI1 clock gate. */
    CLOCK_DisableClock(kCLOCK_Sai1);
    /* Set SAI1_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Sai1PreDiv, 3);
    /* Set SAI1_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Sai1Div, 1);
    /* Set Sai1 clock source. */
    CLOCK_SetMux(kCLOCK_Sai1Mux, 0);
    /* Disable SAI2 clock gate. */
    CLOCK_DisableClock(kCLOCK_Sai2);
    /* Set SAI2_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Sai2PreDiv, 3);
    /* Set SAI2_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Sai2Div, 1);
    /* Set Sai2 clock source. */
    CLOCK_SetMux(kCLOCK_Sai2Mux, 0);
    /* Disable SAI3 clock gate. */
    CLOCK_DisableClock(kCLOCK_Sai3);
    /* Set SAI3_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Sai3PreDiv, 3);
    /* Set SAI3_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Sai3Div, 1);
    /* Set Sai3 clock source. */
    CLOCK_SetMux(kCLOCK_Sai3Mux, 0);
    /* Disable Lpi2c clock gate. */
    CLOCK_DisableClock(kCLOCK_Lpi2c1);
    CLOCK_DisableClock(kCLOCK_Lpi2c2);
    CLOCK_DisableClock(kCLOCK_Lpi2c3);
    /* Set LPI2C_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Lpi2cDiv, 0);
    /* Set Lpi2c clock source. */
    CLOCK_SetMux(kCLOCK_Lpi2cMux, 0);
    /* Disable CAN clock gate. */
    CLOCK_DisableClock(kCLOCK_Can1);
    CLOCK_DisableClock(kCLOCK_Can2);
    CLOCK_DisableClock(kCLOCK_Can1S);
    CLOCK_DisableClock(kCLOCK_Can2S);
    /* Set CAN_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_CanDiv, 1);
    /* Set Can clock source. */
    CLOCK_SetMux(kCLOCK_CanMux, 2);
    /* Disable UART clock gate. */
    CLOCK_DisableClock(kCLOCK_Lpuart1);
    CLOCK_DisableClock(kCLOCK_Lpuart2);
    CLOCK_DisableClock(kCLOCK_Lpuart3);
    CLOCK_DisableClock(kCLOCK_Lpuart4);
    CLOCK_DisableClock(kCLOCK_Lpuart5);
    CLOCK_DisableClock(kCLOCK_Lpuart6);
    CLOCK_DisableClock(kCLOCK_Lpuart7);
    CLOCK_DisableClock(kCLOCK_Lpuart8);
    /* Set UART_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_UartDiv, 0);
    /* Set Uart clock source. */
    CLOCK_SetMux(kCLOCK_UartMux, 0);
    /* Disable LCDIF clock gate. */
    CLOCK_DisableClock(kCLOCK_LcdPixel);
    /* Set LCDIF_PRED. */
    CLOCK_SetDiv(kCLOCK_LcdifPreDiv, 6);
    /* Set LCDIF_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_LcdifDiv, 7);
    /* Set Lcdif pre clock source. */
    CLOCK_SetMux(kCLOCK_LcdifPreMux, 5);
    /* Disable SPDIF clock gate. */
    CLOCK_DisableClock(kCLOCK_Spdif);
    /* Set SPDIF0_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Spdif0PreDiv, 1);
    /* Set SPDIF0_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Spdif0Div, 7);
    /* Set Spdif clock source. */
    CLOCK_SetMux(kCLOCK_SpdifMux, 3);
    /* Disable Flexio1 clock gate. */
    CLOCK_DisableClock(kCLOCK_Flexio1);
    /* Set FLEXIO1_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Flexio1PreDiv, 1);
    /* Set FLEXIO1_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Flexio1Div, 7);
    /* Set Flexio1 clock source. */
    CLOCK_SetMux(kCLOCK_Flexio1Mux, 3);
    /* Disable Flexio2 clock gate. */
    CLOCK_DisableClock(kCLOCK_Flexio2);
    /* Set FLEXIO2_CLK_PRED. */
    CLOCK_SetDiv(kCLOCK_Flexio2PreDiv, 1);
    /* Set FLEXIO2_CLK_PODF. */
    CLOCK_SetDiv(kCLOCK_Flexio2Div, 7);
    /* Set Flexio2 clock source. */
    CLOCK_SetMux(kCLOCK_Flexio2Mux, 3);
    /* Set Pll3 sw clock source. */
    CLOCK_SetMux(kCLOCK_Pll3SwMux, 0);
    /* Init ARM PLL. */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
    /* In SDK projects, SDRAM (configured by SEMC) will be initialized in either debug script or dcd.
     * With this macro SKIP_SYSCLK_INIT, system pll (selected to be SEMC source clock in SDK projects) will be left unchanged.
     * Note: If another clock source is selected for SEMC, user may want to avoid changing that clock as well.*/
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
    /* Disable pfd offset. */
    CCM_ANALOG->PLL_SYS &= ~CCM_ANALOG_PLL_SYS_PFD_OFFSET_EN_MASK;
#endif
    /* In SDK projects, external flash (configured by FLEXSPI) will be initialized by dcd.
     * With this macro XIP_EXTERNAL_FLASH, usb1 pll (selected to be FLEXSPI clock source in SDK projects) will be left unchanged.
     * Note: If another clock source is selected for FLEXSPI, user may want to avoid changing that clock as well.*/
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
    /* Disable Usb1 PLL output for USBPHY1. */
    CCM_ANALOG->PLL_USB1 &= ~CCM_ANALOG_PLL_USB1_EN_USB_CLKS_MASK;
#endif
    /* DeInit Audio PLL. */
    CLOCK_DeinitAudioPll();
    /* Bypass Audio PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllAudio, 1);
    /* Set divider for Audio PLL. */
    CCM_ANALOG->MISC2 &= ~CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK;
    CCM_ANALOG->MISC2 &= ~CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK;
    /* Enable Audio PLL output. */
    CCM_ANALOG->PLL_AUDIO |= CCM_ANALOG_PLL_AUDIO_ENABLE_MASK;
    /* DeInit Video PLL. */
    CLOCK_DeinitVideoPll();
    /* Bypass Video PLL. */
    CCM_ANALOG->PLL_VIDEO |= CCM_ANALOG_PLL_VIDEO_BYPASS_MASK;
    /* Set divider for Video PLL. */
    CCM_ANALOG->MISC2 = (CCM_ANALOG->MISC2 & (~CCM_ANALOG_MISC2_VIDEO_DIV_MASK)) | CCM_ANALOG_MISC2_VIDEO_DIV(0);
    /* Enable Video PLL output. */
    CCM_ANALOG->PLL_VIDEO |= CCM_ANALOG_PLL_VIDEO_ENABLE_MASK;
    /* DeInit Enet PLL. */
    CLOCK_DeinitEnetPll();
    /* Bypass Enet PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllEnet, 1);
    /* Set Enet output divider. */
    CCM_ANALOG->PLL_ENET = (CCM_ANALOG->PLL_ENET & (~CCM_ANALOG_PLL_ENET_DIV_SELECT_MASK)) | CCM_ANALOG_PLL_ENET_DIV_SELECT(1);
    /* Enable Enet output. */
    CCM_ANALOG->PLL_ENET |= CCM_ANALOG_PLL_ENET_ENABLE_MASK;
    /* Enable Enet25M output. */
    CCM_ANALOG->PLL_ENET |= CCM_ANALOG_PLL_ENET_ENET_25M_REF_EN_MASK;
    /* DeInit Usb2 PLL. */
    CLOCK_DeinitUsb2Pll();
    /* Bypass Usb2 PLL. */
    CLOCK_SetPllBypass(CCM_ANALOG, kCLOCK_PllUsb2, 1);
    /* Enable Usb2 PLL output. */
    CCM_ANALOG->PLL_USB2 |= CCM_ANALOG_PLL_USB2_ENABLE_MASK;
    /* Set preperiph clock source. */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    /* Set periph clock source. */
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    /* Set periph clock2 clock source. */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    /* Set per clock source. */
    CLOCK_SetMux(kCLOCK_PerclkMux, 0);
    /* Set lvds1 clock source. */
    CCM_ANALOG->MISC1 = (CCM_ANALOG->MISC1 & (~CCM_ANALOG_MISC1_LVDS1_CLK_SEL_MASK)) | CCM_ANALOG_MISC1_LVDS1_CLK_SEL(0);
    /* Set clock out1 divider. */
    CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO1_DIV_MASK)) | CCM_CCOSR_CLKO1_DIV(0);
    /* Set clock out1 source. */
    CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO1_SEL_MASK)) | CCM_CCOSR_CLKO1_SEL(1);
    /* Set clock out2 divider. */
    CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO2_DIV_MASK)) | CCM_CCOSR_CLKO2_DIV(0);
    /* Set clock out2 source. */
    CCM->CCOSR = (CCM->CCOSR & (~CCM_CCOSR_CLKO2_SEL_MASK)) | CCM_CCOSR_CLKO2_SEL(18);
    /* Set clock out1 drives clock out1. */
    CCM->CCOSR &= ~CCM_CCOSR_CLK_OUT_SEL_MASK;
    /* Disable clock out1. */
    CCM->CCOSR &= ~CCM_CCOSR_CLKO1_EN_MASK;
    /* Disable clock out2. */
    CCM->CCOSR &= ~CCM_CCOSR_CLKO2_EN_MASK;
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
    IOMUXC_GPR->GPR5 &= ~IOMUXC_GPR_GPR5_VREF_1M_CLK_GPT1_MASK;
    /* Set GPT2 High frequency reference clock source. */
    IOMUXC_GPR->GPR5 &= ~IOMUXC_GPR_GPR5_VREF_1M_CLK_GPT2_MASK;
    /* Set SystemCoreClock variable. */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：System clock initialization function that configures the entire clock tree including oscillators, PLLs, clock dividers, muxes, and peripheral clock gates for i.MX RT1052 microcontroller
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is a comprehensive clock initialization function. GetMMIOFunctionInfo reveals extensive hardware register accesses (XTALOSC24M->OSC_CONFIG2, CCM->CCR, DCDC registers, CCM_ANALOG registers, etc.) and a hardware polling loop waiting for DCDC status. The function initializes the entire clock system configuration, making it clearly an INIT type. It does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), and while it contains a polling loop, the primary purpose is initialization (INIT takes priority over LOOP). It is not CORE as it doesn't configure NVIC, OS kernel, or VTOR. The replacement preserves the essential system state (SystemCoreClock variable) while removing hardware-specific operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void BOARD_BootClockRUN(void)
{
    /* Minimal clock initialization for simulation */
    
    /* Initialize external clock (replacement exists) */
    CLOCK_InitExternalClk(0);
    
    /* Set basic clock dividers and muxes (replacements exist) */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1);
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    
    /* Initialize PLLs (replacements exist) */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
    
    /* Set final clock configuration */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    
    /* Set system core clock */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
```

【替换更新】
- 更新代码：void BOARD_BootClockRUN(void)
{
    /* Minimal clock initialization for simulation */
    
    /* Initialize external clock (replacement exists) */
    CLOCK_InitExternalClk(0);
    
    /* Set basic clock dividers and muxes (replacements exist) */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1);
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    
    /* Initialize PLLs (replacements exist) */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
    
    /* Set final clock configuration */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    
    /* Set system core clock */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
- 更新原因：Simplified replacement that includes only essential function calls to satisfy dependencies while maintaining simulation compatibility.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/*******************************************************************************
* Code for BOARD_BootClockRUN configuration
******************************************************************************/
void BOARD_BootClockRUN(void)
{
    /* [INIT REPLACEMENT] Remove hardware-specific clock initialization */
    
    /* Skip RTC OSC clock frequency setting */
    /* Original: CLOCK_SetRtcXtalFreq(32768U); */
    
    /* Skip 1MHz clock output enable/configuration */
    /* Original: XTALOSC24M->OSC_CONFIG2 |= XTALOSC24M_OSC_CONFIG2_ENABLE_1M_MASK; */
    /* Original: XTALOSC24M->OSC_CONFIG2 &= ~XTALOSC24M_OSC_CONFIG2_MUX_1M_MASK; */
    
    /* Skip XTAL 24MHz clock frequency setting */
    /* Original: CLOCK_SetXtalFreq(24000000U); */
    
    /* Call replaced external clock initialization (already has replacement) */
    CLOCK_InitExternalClk(0);
    
    /* Skip internal RC oscillator initialization */
    /* Original: CLOCK_InitRcOsc24M(); */
    
    /* Skip clock source switching */
    /* Original: CLOCK_SwitchOsc(kCLOCK_XtalOsc); */
    
    /* Skip oscillator ready counter configuration */
    /* Original: CCM->CCR = (CCM->CCR & (~CCM_CCR_OSCNT_MASK)) | CCM_CCR_OSCNT(127); */
    
    /* Call replaced mux functions (already have replacements) */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1); /* Set PERIPH_CLK2 MUX to OSC */
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);     /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    
    /* Skip DCDC voltage regulator configuration */
    /* Original: DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(0x13); */
    
    /* [LOOP REMOVED] Skip waiting for DCDC status */
    /* Original: while (DCDC_REG0_STS_DC_OK_MASK != (DCDC_REG0_STS_DC_OK_MASK & DCDC->REG0)) { } */
    
    /* Call replaced divider functions (already have replacements) */
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    
    /* Skip clock disable operations (not needed in simulation) */
    /* Original: CLOCK_DisableClock(kCLOCK_Adc1); etc. */
    
    /* Call replaced divider functions for various peripherals */
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    CLOCK_SetDiv(kCLOCK_PeriphClk2Div, 0);
    CLOCK_SetDiv(kCLOCK_PerclkDiv, 1);
    CLOCK_SetDiv(kCLOCK_Usdhc1Div, 1);
    CLOCK_SetDiv(kCLOCK_Usdhc2Div, 1);
    
    /* Call replaced mux functions for various peripherals */
    CLOCK_SetMux(kCLOCK_Usdhc1Mux, 0);
    CLOCK_SetMux(kCLOCK_Usdhc2Mux, 0);
    
    /* Skip conditional SEMC/FLEXSPI configuration based on macros */
    /* These are hardware-specific and not needed in simulation */
    
    /* Call replaced divider and mux functions for other peripherals */
    CLOCK_SetDiv(kCLOCK_CsiDiv, 1);
    CLOCK_SetMux(kCLOCK_CsiMux, 0);
    CLOCK_SetDiv(kCLOCK_LpspiDiv, 4);
    CLOCK_SetMux(kCLOCK_LpspiMux, 2);
    CLOCK_SetDiv(kCLOCK_TraceDiv, 2);
    CLOCK_SetMux(kCLOCK_TraceMux, 2);
    /* ... and many other similar calls */
    
    /* Call replaced PLL initialization functions (already have replacements) */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
    
#ifndef SKIP_SYSCLK_INIT
    CLOCK_InitSysPll(&sysPllConfig_BOARD_BootClockRUN);
    /* Skip PFD initialization (hardware-specific) */
#endif

#if !(defined(XIP_EXTERNAL_FLASH) && (XIP_EXTERNAL_FLASH == 1))
    CLOCK_InitUsb1Pll(&usb1PllConfig_BOARD_BootClockRUN);
    /* Skip PFD initialization (hardware-specific) */
    /* Skip USB1 PLL output disable (hardware-specific) */
#endif
    
    /* Skip Audio/Video/Enet/USB2 PLL deinit/bypass/enable operations */
    /* These are all hardware-specific register writes */
    
    /* Call replaced mux functions for final clock configuration */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    CLOCK_SetMux(kCLOCK_PerclkMux, 0);
    
    /* Skip IOMUXC configuration (hardware-specific) */
    /* Skip clock output configuration (hardware-specific) */
    
    /* Set SystemCoreClock variable (important for system timing) */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
    原因：This function is classified as INIT and contains extensive hardware register writes, polling loops, and calls to other hardware-dependent functions. It's the main clock initialization function called during system startup. The replacement removes all hardware-specific operations while preserving the function signature and calls to already-replaced functions (CLOCK_SetDiv, CLOCK_SetMux, CLOCK_InitArmPll, etc.). The polling loop waiting for DCDC status is removed to prevent blocking in emulation. The SystemCoreClock variable assignment is preserved as it's needed by the system.
    时间：

  版本 2:
    替换代码：void BOARD_BootClockRUN(void)
{
    /* Minimal clock initialization for simulation */
    
    /* Initialize external clock (replacement exists) */
    CLOCK_InitExternalClk(0);
    
    /* Set basic clock dividers and muxes (replacements exist) */
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 1);
    CLOCK_SetMux(kCLOCK_PeriphMux, 1);
    CLOCK_SetDiv(kCLOCK_AhbDiv, 0);
    CLOCK_SetDiv(kCLOCK_IpgDiv, 3);
    CLOCK_SetDiv(kCLOCK_ArmDiv, 1);
    
    /* Initialize PLLs (replacements exist) */
    CLOCK_InitArmPll(&armPllConfig_BOARD_BootClockRUN);
    
    /* Set final clock configuration */
    CLOCK_SetMux(kCLOCK_PrePeriphMux, 3);
    CLOCK_SetMux(kCLOCK_PeriphMux, 0);
    CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0);
    
    /* Set system core clock */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
    原因：Simplified replacement that includes only essential function calls to satisfy dependencies while maintaining simulation compatibility.
    时间：

=== 信息结束 ===
```

### BOARD_InitPins

```text
=== BOARD_InitPins 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/pin_mux.c
- 行号：50
- 函数内容：void BOARD_InitPins(void) {
  CLOCK_EnableClock(kCLOCK_Iomuxc);           /* iomuxc clock (iomuxc_clk_enable): 0x03U */

  IOMUXC_SetPinMux(
      IOMUXC_GPIO_AD_B0_09_GPIO1_IO09,        /* GPIO_AD_B0_09 is configured as GPIO1_IO09 */
      0U);                                    /* Software Input On Field: Input Path is determined by functionality */
  IOMUXC_SetPinMux(
      IOMUXC_GPIO_AD_B0_12_LPUART1_TX,        /* GPIO_AD_B0_12 is configured as LPUART1_TX */
      0U);                                    /* Software Input On Field: Input Path is determined by functionality */
  IOMUXC_SetPinMux(
      IOMUXC_GPIO_AD_B0_13_LPUART1_RX,        /* GPIO_AD_B0_13 is configured as LPUART1_RX */
      0U);                                    /* Software Input On Field: Input Path is determined by functionality */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures pin routing and electrical features for the board by enabling IOMUXC clock and setting up pin mux configurations.
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization operations: it calls CLOCK_EnableClock (which enables clock for IOMUXC) and IOMUXC_SetPinMux (which contains direct MMIO register writes to configure pin muxing). This is called by rt_hw_board_init during board initialization. The function fits the INIT category as it initializes peripheral configurations (pin muxing) without involving data transmission/reception (RECV), interrupt handling (IRQ), or core OS/NVIC operations (CORE).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void BOARD_InitPins(void) {
    /* Simulation-friendly pin initialization */
    /* Skip actual hardware operations for simulation */
    
    /* The original function would:
     * 1. Enable IOMUXC clock via CLOCK_EnableClock(kCLOCK_Iomuxc)
     * 2. Configure GPIO1_IO09 pin mux
     * 3. Configure LPUART1_TX pin mux  
     * 4. Configure LPUART1_RX pin mux
     */
    
    /* For simulation, we just return without hardware operations */
    return;
}
```

【替换更新】
- 更新代码：void BOARD_InitPins(void) {
    /* Simulation-friendly pin initialization */
    /* Skip actual hardware operations for simulation */
    
    /* The original function would:
     * 1. Enable IOMUXC clock via CLOCK_EnableClock(kCLOCK_Iomuxc)
     * 2. Configure GPIO1_IO09 pin mux
     * 3. Configure LPUART1_TX pin mux  
     * 4. Configure LPUART1_RX pin mux
     */
    
    /* For simulation, we just return without hardware operations */
    return;
}
- 更新原因：Create simulation-friendly replacement that maintains original function signature but removes hardware dependencies for build compatibility

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void BOARD_InitPins(void) {
    /* Simulation-friendly pin initialization */
    /* Skip actual hardware operations for simulation */
    
    /* The original function would:
     * 1. Enable IOMUXC clock via CLOCK_EnableClock(kCLOCK_Iomuxc)
     * 2. Configure GPIO1_IO09 pin mux
     * 3. Configure LPUART1_TX pin mux  
     * 4. Configure LPUART1_RX pin mux
     */
    
    /* For simulation, we just return without hardware operations */
    return;
}
    原因：Create simulation-friendly replacement that maintains original function signature but removes hardware dependencies for build compatibility
    时间：

=== 信息结束 ===
```

### CLOCK_DeinitArmPll

```text
=== CLOCK_DeinitArmPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：500
- 函数内容：void CLOCK_DeinitArmPll(void)
{
    CCM_ANALOG->PLL_ARM = CCM_ANALOG_PLL_ARM_POWERDOWN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes (powers down) the ARM PLL by writing power-down mask to PLL control register.
- 是否需要替换：是
- 分类/替换原因：Function performs hardware-specific MMIO register write to control ARM PLL power state (CCM_ANALOG->PLL_ARM = CCM_ANALOG_PLL_ARM_POWERDOWN_MASK). This is a peripheral configuration operation that fits the INIT category (de-initialization is the inverse of initialization). The function contains no data I/O, interrupts, loops, or OS operations. It's not CORE (no NVIC/OS/VTOR), not RECV/IRQ, and not RETURNOK/SKIP since it has clear hardware register access that should be removed in simulation. GetMMIOFunctionInfo confirmed hardware register access, and GetFunctionInfo showed the simple implementation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitArmPll(void)
{
    /* Hardware-specific PLL power-down operation removed for simulation */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitArmPll(void)
{
    /* Hardware-specific PLL power-down operation removed for simulation */
}
- 更新原因：Replace hardware-specific MMIO operation with simulation-friendly stub to resolve build verification failure

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitArmPll(void)
{
    /* Hardware-specific PLL power-down operation removed for simulation */
}
    原因：Replace hardware-specific MMIO operation with simulation-friendly stub to resolve build verification failure
    时间：

=== 信息结束 ===
```

### CLOCK_DeinitUsb1Pll

```text
=== CLOCK_DeinitUsb1Pll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：575
- 函数内容：void CLOCK_DeinitUsb1Pll(void)
{
    CCM_ANALOG->PLL_USB1 = 0U;
}


【初始分析（FunctionClassifier）】
- 函数类型：SKIP
- 函数用途/功能描述：Deinitializes the USB1 PLL by writing 0 to its control register
- 是否需要替换：是
- 分类/替换原因：Function performs a single hardware register write (CCM_ANALOG->PLL_USB1 = 0U) to deinitialize the USB1 PLL. This is a simple peripheral configuration operation that can be safely ignored in emulation. The function has no return value, no data I/O, no loops, and no interrupt handling. It fits the SKIP category for non-critical driver functions that perform optional operations. The fixer restored the original hardware operation, indicating this function should not be modified.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitUsb1Pll(void)
{
    CCM_ANALOG->PLL_USB1 = 0U;
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitUsb1Pll(void)
{
    CCM_ANALOG->PLL_USB1 = 0U;
}
- 更新原因：Restoring original hardware deinitialization code to match the original function behavior. The previous stub replacement failed verification, likely because it didn't perform the actual hardware register write operation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitUsb1Pll(void)
{
    CCM_ANALOG->PLL_USB1 = 0U;
}
    原因：Restoring original hardware deinitialization code to match the original function behavior. The previous stub replacement failed verification, likely because it didn't perform the actual hardware register write operation.
    时间：

=== 信息结束 ===
```

### CLOCK_DeinitUsb2Pll

```text
=== CLOCK_DeinitUsb2Pll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：608
- 函数内容：void CLOCK_DeinitUsb2Pll(void)
{
    CCM_ANALOG->PLL_USB2 = 0U;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes the USB2 PLL by setting its control register to 0
- 是否需要替换：是
- 分类/替换原因：This function performs hardware deinitialization by writing to the CCM_ANALOG->PLL_USB2 register to disable/deinitialize the USB2 PLL. It contains MMIO operations (register write) but no data transmission/reception, interrupt handling, or polling loops. As a peripheral deinitialization function, it fits the INIT category which handles peripheral initialization/deinitialization operations. The replacement removes the hardware register access while preserving the function structure. GetMMIOFunctionInfo confirmed hardware register access, and GetFunctionCallStack shows it's called from BOARD_BootClockRUN during system initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitUsb2Pll(void)
{
    /* Hardware deinitialization removed for simulation */
    /* Original code: CCM_ANALOG->PLL_USB2 = 0U; */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitUsb2Pll(void)
{
    /* Hardware deinitialization removed for simulation */
    /* Original code: CCM_ANALOG->PLL_USB2 = 0U; */
}
- 更新原因：Fix function replacement to match original signature exactly and resolve compilation errors. The function performs USB2 PLL deinitialization which is simulated in the replacement.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitUsb2Pll(void)
{
    /* Deinitialize USB2 PLL - simulation only */
    /* Original code: CCM_ANALOG->PLL_USB2 = 0U; */
}
    原因：Fix replacement for CLOCK_DeinitUsb2Pll to match original function signature and provide proper simulation behavior. The original function writes 0 to PLL_USB2 register to deinitialize USB2 PLL.
    时间：

  版本 2:
    替换代码：void CLOCK_DeinitUsb2Pll(void)
{
    /* Hardware deinitialization removed for simulation */
    /* Original code: CCM_ANALOG->PLL_USB2 = 0U; */
}
    原因：Fix function replacement to match original signature exactly and resolve compilation errors. The function performs USB2 PLL deinitialization which is simulated in the replacement.
    时间：

=== 信息结束 ===
```

### CLOCK_DeinitVideoPll

```text
=== CLOCK_DeinitVideoPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：781
- 函数内容：void CLOCK_DeinitVideoPll(void)
{
    CCM_ANALOG->PLL_VIDEO = CCM_ANALOG_PLL_VIDEO_POWERDOWN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes the Video PLL by setting the powerdown mask in the CCM_ANALOG register
- 是否需要替换：是
- 分类/替换原因：This function performs a direct hardware register write (CCM_ANALOG->PLL_VIDEO = CCM_ANALOG_PLL_VIDEO_POWERDOWN_MASK) to de-initialize the Video PLL. It is a peripheral initialization/de-initialization function with no data I/O, interrupt handling, or polling loops. According to the classification priority order, INIT takes precedence over RETURNOK and SKIP for functions that configure peripheral hardware. The function contains MMIO operations (register write) but no other complex logic, making it suitable for INIT classification where hardware operations should be removed while preserving the function structure. The replacement successfully removes the hardware register access while maintaining the original function signature.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitVideoPll(void)
{
    /* Hardware de-initialization removed for simulation */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitVideoPll(void)
{
    /* Hardware de-initialization removed for simulation */
}
- 更新原因：Simplified replacement with just function body to pass verification

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitVideoPll(void)
{
    /* Hardware register write removed for simulation */
    /* Original: CCM_ANALOG->PLL_VIDEO = CCM_ANALOG_PLL_VIDEO_POWERDOWN_MASK; */
}
    原因：Fix replacement code to match original function signature and add proper comment about removed hardware access
    时间：

  版本 2:
    替换代码：void CLOCK_DeinitVideoPll(void)
{
    /* Hardware de-initialization removed for simulation */
}
    原因：Simplified replacement with just function body to pass verification
    时间：

=== 信息结束 ===
```

### CLOCK_DisableUsbhs0PhyPllClock

```text
=== CLOCK_DisableUsbhs0PhyPllClock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：466
- 函数内容：void CLOCK_DisableUsbhs0PhyPllClock(void)
{
    CCM_ANALOG->PLL_USB1 &= ~CCM_ANALOG_PLL_USB1_EN_USB_CLKS_MASK;
    USBPHY1->CTRL |= USBPHY_CTRL_CLKGATE_MASK; /* Set to 1U to gate clocks */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Disables the USB HS PHY PLL clock by clearing the USB clock enable bit and setting the clock gate bit.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware configuration operations to disable a peripheral clock. It contains direct MMIO register accesses to CCM_ANALOG->PLL_USB1 and USBPHY1->CTRL registers. According to the classification criteria, functions that initialize or configure peripheral hardware fall under the INIT category. The function does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), contains no polling loops (not LOOP), and is not related to NVIC/OS kernel operations (not CORE). As an INIT function, it requires replacement code that removes hardware-specific register accesses while preserving the function signature.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DisableUsbhs0PhyPllClock(void)
{
    /* Hardware register accesses removed for simulation */
}
```

【替换更新】
- 更新代码：void CLOCK_DisableUsbhs0PhyPllClock(void)
{
    /* Hardware register accesses removed for simulation */
}
- 更新原因：Function performs pure hardware register operations to disable USB HS PHY PLL clock. As a RETURNOK function, it can be safely replaced with empty implementation for simulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DisableUsbhs0PhyPllClock(void)
{
    /* Hardware register accesses removed for simulation */
}
    原因：Function performs pure hardware register operations to disable USB HS PHY PLL clock. As a RETURNOK function, it can be safely replaced with empty implementation for simulation.
    时间：

=== 信息结束 ===
```

### CLOCK_DisableUsbhs1PhyPllClock

```text
=== CLOCK_DisableUsbhs1PhyPllClock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：1207
- 函数内容：void CLOCK_DisableUsbhs1PhyPllClock(void)
{
    CCM_ANALOG->PLL_USB2 &= ~CCM_ANALOG_PLL_USB2_EN_USB_CLKS_MASK;
    USBPHY2->CTRL |= USBPHY_CTRL_CLKGATE_MASK; /* Set to 1U to gate clocks */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Disables USB HS PHY PLL clock by clearing clock enable bit and setting clock gate bit
- 是否需要替换：是
- 分类/替换原因：Function performs hardware register writes to disable USB HS PHY PLL clock (CCM_ANALOG->PLL_USB2 and USBPHY2->CTRL). This is a configuration/initialization function that sets hardware state. According to classification priority, it's INIT (initialization function) as it configures peripheral clock resources. Not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not interrupt handler), not LOOP (no polling loops). The replacement removes hardware register writes while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DisableUsbhs1PhyPllClock(void)
{
    /* Hardware register writes removed for simulation */
    /* CCM_ANALOG->PLL_USB2 &= ~CCM_ANALOG_PLL_USB2_EN_USB_CLKS_MASK; */
    /* USBPHY2->CTRL |= USBPHY_CTRL_CLKGATE_MASK; */
}
```

【替换更新】
- 更新代码：void CLOCK_DisableUsbhs1PhyPllClock(void)
{
    /* Hardware register writes removed for simulation */
    /* CCM_ANALOG->PLL_USB2 &= ~CCM_ANALOG_PLL_USB2_EN_USB_CLKS_MASK; */
    /* USBPHY2->CTRL |= USBPHY_CTRL_CLKGATE_MASK; */
}
- 更新原因：Fix replacement code to match original function signature and remove hardware register writes for simulation

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DisableUsbhs1PhyPllClock(void)
{
    /* Hardware register writes removed for simulation */
    /* CCM_ANALOG->PLL_USB2 &= ~CCM_ANALOG_PLL_USB2_EN_USB_CLKS_MASK; */
    /* USBPHY2->CTRL |= USBPHY_CTRL_CLKGATE_MASK; */
}
    原因：Fix replacement code to match original function signature and remove hardware register writes for simulation
    时间：

=== 信息结束 ===
```

### CLOCK_EnableUsbhs0PhyPllClock

```text
=== CLOCK_EnableUsbhs0PhyPllClock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：442
- 函数内容：bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    const clock_usb_pll_config_t g_ccmConfigUsbPll = {.loopDivider = 0U};
    if (CCM_ANALOG->PLL_USB1 & CCM_ANALOG_PLL_USB1_ENABLE_MASK)
    {
        CCM_ANALOG->PLL_USB1 |= CCM_ANALOG_PLL_USB1_EN_USB_CLKS_MASK;
    }
    else
    {
        CLOCK_InitUsb1Pll(&g_ccmConfigUsbPll);
    }
    USBPHY1->CTRL &= ~USBPHY_CTRL_SFTRST_MASK; /* release PHY from reset */
    USBPHY1->CTRL &= ~USBPHY_CTRL_CLKGATE_MASK;

    USBPHY1->PWD = 0;
    USBPHY1->CTRL |= USBPHY_CTRL_ENAUTOCLR_PHY_PWD_MASK | USBPHY_CTRL_ENAUTOCLR_CLKGATE_MASK |
                     USBPHY_CTRL_ENUTMILEVEL2_MASK | USBPHY_CTRL_ENUTMILEVEL3_MASK;
    return true;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables the USB HS PHY PLL clock by configuring the USB PHY PLL clock source and releasing the PHY from reset.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization operations for the USB PHY PLL clock. Analysis shows it contains multiple MMIO register accesses (CCM_ANALOG->PLL_USB1, USBPHY1->CTRL, USBPHY1->PWD) to configure hardware peripherals. The function initializes clock settings and releases the USB PHY from reset state. It follows the INIT pattern of setting up peripheral configurations without involving data transmission/reception (RECV), interrupt handling (IRQ), or polling loops (LOOP). The function is not CORE as it doesn't involve NVIC/OS kernel/VTOR operations. The replacement code has been successfully generated and verified to compile correctly.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware initialization for USB PHY PLL clock */
    /* Original hardware operations removed for simulation */
    return true;
}
```

【替换更新】
- 更新代码：bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware initialization for USB PHY PLL clock */
    /* Original hardware operations removed for simulation */
    return true;
}
- 更新原因：Removed unused variable g_ccmConfigUsbPll to fix compilation warning. The variable was declared but never used in the replacement code since hardware operations are skipped in simulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Hardware initialization removed for simulation */
    return true;
}
    原因：Simplified replacement to remove unused variable that may cause compilation issues. The original variable g_ccmConfigUsbPll of type clock_usb_pll_config_t may not be defined in the current context.
    时间：

  版本 2:
    替换代码：bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware initialization for USB PHY PLL clock */
    /* Original hardware operations removed for simulation */
    return true;
}
    原因：Removed unused variable g_ccmConfigUsbPll to fix compilation warning. The variable was declared but never used in the replacement code since hardware operations are skipped in simulation.
    时间：

=== 信息结束 ===
```

### CLOCK_EnableUsbhs1Clock

```text
=== CLOCK_EnableUsbhs1Clock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：419
- 函数内容：bool CLOCK_EnableUsbhs1Clock(clock_usb_src_t src, uint32_t freq)
{
    CCM->CCGR6 |= CCM_CCGR6_CG0_MASK;
    USB2->USBCMD |= USBHS_USBCMD_RST_MASK;
    for (volatile uint32_t i = 0; i < 400000;
         i++) /* Add a delay between RST and RS so make sure there is a DP pullup sequence*/
    {
        __ASM("nop");
    }
    PMU->REG_3P0 = (PMU->REG_3P0 & (~PMU_REG_3P0_OUTPUT_TRG_MASK)) |
                   (PMU_REG_3P0_OUTPUT_TRG(0x17) | PMU_REG_3P0_ENABLE_LINREG_MASK);
    return true;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables USB HS clock and initializes USB HS peripheral hardware including clock gating, controller reset, and PMU configuration
- 是否需要替换：否
- 分类/替换原因：Function performs hardware initialization operations: 1) Enables clock gating via CCM->CCGR6 register, 2) Resets USB controller via USB2->USBCMD register, 3) Contains a hardware-dependent delay loop for timing, 4) Configures PMU register for power management. These are all peripheral initialization operations that should be removed in simulation while preserving the function's logical success return. The function is classified as INIT rather than LOOP because its primary purpose is initialization (clock enable and peripheral setup), with the loop being a secondary timing element.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：bool CLOCK_EnableUsbhs1Clock(clock_usb_src_t src, uint32_t freq)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for emulation */
    /* Original: CCM->CCGR6 |= CCM_CCGR6_CG0_MASK; */
    /* Original: USB2->USBCMD |= USBHS_USBCMD_RST_MASK; */
    /* Original: Delay loop removed */
    /* Original: PMU->REG_3P0 configuration removed */
    return true;
}
- 更新原因：Updated replacement to match original function signature exactly and ensure proper formatting. The build succeeded with previous replacement, but ensuring consistency with original declaration.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：bool CLOCK_EnableUsbhs1Clock(clock_usb_src_t src, uint32_t freq)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for emulation */
    /* Original: CCM->CCGR6 |= CCM_CCGR6_CG0_MASK; */
    /* Original: USB2->USBCMD |= USBHS_USBCMD_RST_MASK; */
    /* Original: Delay loop removed */
    /* Original: PMU->REG_3P0 configuration removed */
    return true;
}
    原因：Updated replacement to match original function signature exactly and ensure proper formatting. The build succeeded with previous replacement, but ensuring consistency with original declaration.
    时间：

=== 信息结束 ===
```

### CLOCK_EnableUsbhs1PhyPllClock

```text
=== CLOCK_EnableUsbhs1PhyPllClock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：1189
- 函数内容：bool CLOCK_EnableUsbhs1PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    const clock_usb_pll_config_t g_ccmConfigUsbPll = {.loopDivider = 0U};
    CLOCK_InitUsb2Pll(&g_ccmConfigUsbPll);
    USBPHY2->CTRL &= ~USBPHY_CTRL_SFTRST_MASK; /* release PHY from reset */
    USBPHY2->CTRL &= ~USBPHY_CTRL_CLKGATE_MASK;

    USBPHY2->PWD = 0;
    USBPHY2->CTRL |= USBPHY_CTRL_ENAUTOCLR_PHY_PWD_MASK | USBPHY_CTRL_ENAUTOCLR_CLKGATE_MASK |
                     USBPHY_CTRL_ENUTMILEVEL2_MASK | USBPHY_CTRL_ENUTMILEVEL3_MASK;

    return true;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables the internal 480MHz USB HS PHY PLL clock by initializing USB2 PLL and configuring USB PHY control registers
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of USB PHY PLL clock subsystem. Contains MMIO register writes to USBPHY2->CTRL and USBPHY2->PWD, and calls CLOCK_InitUsb2Pll which contains MMIO operations to CCM_ANALOG->PLL_USB2. This is a peripheral initialization function that doesn't fit higher priority categories (CORE/RECV/IRQ). GetMMIOFunctionInfo shows hardware register accesses, and GetFunctionInfo confirms this is a clock initialization function.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*! brief Enable USB HS PHY PLL clock.
*
* This function enables the internal 480MHz USB PHY PLL clock.
*
* param src  USB HS PHY PLL clock source.
* param freq The frequency specified by src.
* retval true The clock is set successfully.
* retval false The clock source is invalid to get proper USB HS clock.
*/
bool CLOCK_EnableUsbhs1PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip all hardware initialization and configuration */
    /* Original function would: */
    /* 1. Initialize USB2 PLL */
    /* 2. Release USB PHY from reset */
    /* 3. Clear clock gate */
    /* 4. Set PWD register to 0 */
    /* 5. Configure various control bits */
    
    return true;
}
```

=== 信息结束 ===
```

### CLOCK_InitArmPll

```text
=== CLOCK_InitArmPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：479
- 函数内容：void CLOCK_InitArmPll(const clock_arm_pll_config_t *config)
{
    /* Bypass PLL first */
    CCM_ANALOG->PLL_ARM = (CCM_ANALOG->PLL_ARM & (~CCM_ANALOG_PLL_ARM_BYPASS_CLK_SRC_MASK)) |
                          CCM_ANALOG_PLL_ARM_BYPASS_MASK | CCM_ANALOG_PLL_ARM_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_ARM =
        (CCM_ANALOG->PLL_ARM & (~(CCM_ANALOG_PLL_ARM_DIV_SELECT_MASK | CCM_ANALOG_PLL_ARM_POWERDOWN_MASK))) |
        CCM_ANALOG_PLL_ARM_ENABLE_MASK | CCM_ANALOG_PLL_ARM_DIV_SELECT(config->loopDivider);

    while ((CCM_ANALOG->PLL_ARM & CCM_ANALOG_PLL_ARM_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_ARM &= ~CCM_ANALOG_PLL_ARM_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the ARM PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider selection, and lock waiting.
- 是否需要替换：否
- 分类/替换原因：GetFunctionInfo shows this is a PLL initialization function that configures hardware registers. GetMMIOFunctionInfo reveals multiple register accesses to CCM_ANALOG->PLL_ARM and a polling loop waiting for lock status. The function is called by BOARD_BootClockRUN during system initialization. It fits the INIT category as it initializes peripheral configurations (ARM PLL). While it contains a polling loop (LOOP characteristic), the primary purpose is initialization, and INIT has higher priority than LOOP in the classification hierarchy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：/*!
* brief Initialize the ARM PLL.
*
* This function initialize the ARM PLL with specific settings
*
* param config   configuration to set to PLL.
*/
void CLOCK_InitArmPll(const clock_arm_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for simulation */
    /* Original function would configure ARM PLL with specific settings */
    
    /* Skip hardware-specific configuration:
     * - CCM_ANALOG->PLL_ARM register writes for bypass configuration
     * - CCM_ANALOG->PLL_ARM register writes for divider selection and enabling
     * - Polling loop waiting for PLL lock
     * - Bypass disable operation
     */
    
    /* Preserve parameter validation and logical flow if any */
    (void)config; /* Use parameter to avoid unused parameter warning */
    
    /* No hardware operations in simulation environment */
}
- 更新原因：This function is classified as INIT and contains hardware register writes and polling loops that need to be removed for emulation. Following the pattern of other PLL initialization functions (CLOCK_InitSysPll, CLOCK_InitUsb1Pll, etc.), we remove all hardware-specific operations while preserving the function signature. The function is called by BOARD_BootClockRUN during system initialization and contains a polling loop waiting for PLL lock that would block emulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/*!
* brief Initialize the ARM PLL.
*
* This function initialize the ARM PLL with specific settings
*
* param config   configuration to set to PLL.
*/
void CLOCK_InitArmPll(const clock_arm_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for simulation */
    /* Original function would configure ARM PLL with specific settings */
    
    /* Skip hardware-specific configuration:
     * - CCM_ANALOG->PLL_ARM register writes for bypass configuration
     * - CCM_ANALOG->PLL_ARM register writes for divider selection and enabling
     * - Polling loop waiting for PLL lock
     * - Bypass disable operation
     */
    
    /* Preserve parameter validation and logical flow if any */
    (void)config; /* Use parameter to avoid unused parameter warning */
    
    /* No hardware operations in simulation environment */
}
    原因：This function is classified as INIT and contains hardware register writes and polling loops that need to be removed for emulation. Following the pattern of other PLL initialization functions (CLOCK_InitSysPll, CLOCK_InitUsb1Pll, etc.), we remove all hardware-specific operations while preserving the function signature. The function is called by BOARD_BootClockRUN during system initialization and contains a polling loop waiting for PLL lock that would block emulation.
    时间：

  版本 2:
    替换代码：/*!
* brief Initialize the ARM PLL.
*
* This function initialize the ARM PLL with specific settings
*
* param config   configuration to set to PLL.
*/
void CLOCK_InitArmPll(const clock_arm_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for simulation */
    /* Original function would configure ARM PLL with specific settings */
    
    /* Skip hardware-specific configuration:
     * - CCM_ANALOG->PLL_ARM register writes for bypass configuration
     * - CCM_ANALOG->PLL_ARM register writes for divider selection and enabling
     * - Polling loop waiting for PLL lock
     * - Bypass disable operation
     */
    
    /* Preserve parameter validation and logical flow if any */
    (void)config; /* Use parameter to avoid unused parameter warning */
    
    /* No hardware operations in simulation environment */
}
    原因：This function is classified as INIT and contains hardware register writes and polling loops that need to be removed for emulation. Following the pattern of other PLL initialization functions (CLOCK_InitSysPll, CLOCK_InitUsb1Pll, etc.), we remove all hardware-specific operations while preserving the function signature. The function is called by BOARD_BootClockRUN during system initialization and contains a polling loop waiting for PLL lock that would block emulation.
    时间：

=== 信息结束 ===
```

### CLOCK_InitAudioPll

```text
=== CLOCK_InitAudioPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：620
- 函数内容：void CLOCK_InitAudioPll(const clock_audio_pll_config_t *config)
{
    uint32_t pllAudio;
    uint32_t misc2 = 0;

    /* Bypass PLL first */
    CCM_ANALOG->PLL_AUDIO = (CCM_ANALOG->PLL_AUDIO & (~CCM_ANALOG_PLL_AUDIO_BYPASS_CLK_SRC_MASK)) |
                            CCM_ANALOG_PLL_AUDIO_BYPASS_MASK | CCM_ANALOG_PLL_AUDIO_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_AUDIO_NUM = CCM_ANALOG_PLL_AUDIO_NUM_A(config->numerator);
    CCM_ANALOG->PLL_AUDIO_DENOM = CCM_ANALOG_PLL_AUDIO_DENOM_B(config->denominator);

    /*
     * Set post divider:
     *
     * ------------------------------------------------------------------------
     * | config->postDivider | PLL_AUDIO[POST_DIV_SELECT]  | MISC2[AUDIO_DIV] |
     * ------------------------------------------------------------------------
     * |         1           |            2                |        0         |
     * ------------------------------------------------------------------------
     * |         2           |            1                |        0         |
     * ------------------------------------------------------------------------
     * |         4           |            2                |        3         |
     * ------------------------------------------------------------------------
     * |         8           |            1                |        3         |
     * ------------------------------------------------------------------------
     * |         16          |            0                |        3         |
     * ------------------------------------------------------------------------
     */
    pllAudio =
        (CCM_ANALOG->PLL_AUDIO & (~(CCM_ANALOG_PLL_AUDIO_DIV_SELECT_MASK | CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK))) |
        CCM_ANALOG_PLL_AUDIO_ENABLE_MASK | CCM_ANALOG_PLL_AUDIO_DIV_SELECT(config->loopDivider);

    switch (config->postDivider)
    {
        case 16:
            pllAudio |= CCM_ANALOG_PLL_AUDIO_POST_DIV_SELECT(0);
            misc2 = CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK | CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK;
            break;

        case 8:
            pllAudio |= CCM_ANALOG_PLL_AUDIO_POST_DIV_SELECT(1);
            misc2 = CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK | CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK;
            break;

        case 4:
            pllAudio |= CCM_ANALOG_PLL_AUDIO_POST_DIV_SELECT(2);
            misc2 = CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK | CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK;
            break;

        case 2:
            pllAudio |= CCM_ANALOG_PLL_AUDIO_POST_DIV_SELECT(1);
            break;

        default:
            pllAudio |= CCM_ANALOG_PLL_AUDIO_POST_DIV_SELECT(2);
            break;
    }

    CCM_ANALOG->MISC2 =
        (CCM_ANALOG->MISC2 & ~(CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK | CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK)) | misc2;

    CCM_ANALOG->PLL_AUDIO = pllAudio;

    while ((CCM_ANALOG->PLL_AUDIO & CCM_ANALOG_PLL_AUDIO_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_AUDIO &= ~CCM_ANALOG_PLL_AUDIO_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the Audio PLL with specific configuration settings including bypass, numerator/denominator values, and post-divider settings.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is an initialization function for Audio PLL hardware. GetMMIOFunctionInfo reveals multiple register accesses to CCM_ANALOG registers (PLL_AUDIO, PLL_AUDIO_NUM, PLL_AUDIO_DENOM, MISC2) and a polling loop waiting for PLL lock. The function configures peripheral hardware without data transmission, interrupt handling, or OS operations. It fits the INIT classification as it initializes peripheral configurations. The function also contains a peripheral-dependent polling loop, but INIT has higher priority than LOOP in the classification hierarchy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initializes the Audio PLL.
*
* This function initializes the Audio PLL with specific settings
*
* param config Configuration to set to PLL.
*/
void CLOCK_InitAudioPll(const clock_audio_pll_config_t *config)
{
    /* Remove all hardware-specific register accesses */
    /* Skip PLL bypass configuration */
    /* Skip numerator/denominator register writes */
    /* Skip post-divider configuration logic */
    /* Skip MISC2 register configuration */
    /* Skip final PLL_AUDIO register write */
    
    /* Remove polling loop waiting for PLL lock */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */
    
    /* Skip bypass disable operation */
    /* Function completes without hardware operations */
}
```

=== 信息结束 ===
```

### CLOCK_InitEnetPll

```text
=== CLOCK_InitEnetPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：793
- 函数内容：void CLOCK_InitEnetPll(const clock_enet_pll_config_t *config)
{
    uint32_t enet_pll = CCM_ANALOG_PLL_ENET_DIV_SELECT(config->loopDivider);

    CCM_ANALOG->PLL_ENET = (CCM_ANALOG->PLL_ENET & (~CCM_ANALOG_PLL_ENET_BYPASS_CLK_SRC_MASK)) |
                           CCM_ANALOG_PLL_ENET_BYPASS_MASK | CCM_ANALOG_PLL_ENET_BYPASS_CLK_SRC(config->src);

    if (config->enableClkOutput)
    {
        enet_pll |= CCM_ANALOG_PLL_ENET_ENABLE_MASK;
    }

    if (config->enableClkOutput25M)
    {
        enet_pll |= CCM_ANALOG_PLL_ENET_ENET_25M_REF_EN_MASK;
    }

    CCM_ANALOG->PLL_ENET =
        (CCM_ANALOG->PLL_ENET & (~(CCM_ANALOG_PLL_ENET_DIV_SELECT_MASK | CCM_ANALOG_PLL_ENET_POWERDOWN_MASK))) |
        enet_pll;

    /* Wait for stable */
    while ((CCM_ANALOG->PLL_ENET & CCM_ANALOG_PLL_ENET_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_ENET &= ~CCM_ANALOG_PLL_ENET_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the ENET (Ethernet) PLL (Phase-Locked Loop) with specific configuration settings including divider, clock source, and output enables.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs ENET PLL initialization with multiple hardware register writes to CCM_ANALOG->PLL_ENET. GetMMIOFunctionInfo confirmed multiple MMIO operations including register assignments and a polling loop waiting for PLL lock. The function fits the INIT category as it initializes peripheral hardware configuration, contains register writes, and has a polling loop characteristic of initialization functions. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler). While it contains a polling loop (LOOP characteristic), INIT has higher priority and the primary purpose is initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitEnetPll(const clock_enet_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for simulation */
    /* Original function would configure ENET PLL with specific settings */
    
    /* Skip hardware-specific configuration:
     * - CCM_ANALOG->PLL_ENET register writes
     * - Polling loop waiting for PLL lock
     */
    
    /* Preserve parameter validation and logical flow if any */
    (void)config; /* Use parameter to avoid unused parameter warning */
    
    /* No hardware operations in simulation environment */
}
```

=== 信息结束 ===
```

### CLOCK_InitExternalClk

```text
=== CLOCK_InitExternalClk 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：150
- 函数内容：void CLOCK_InitExternalClk(bool bypassXtalOsc)
{
    /* This device does not support bypass XTAL OSC. */
    assert(!bypassXtalOsc);

    CCM_ANALOG->MISC0_CLR = CCM_ANALOG_MISC0_XTAL_24M_PWD_MASK; /* Power up */
    while ((XTALOSC24M->LOWPWR_CTRL & XTALOSC24M_LOWPWR_CTRL_XTALOSC_PWRUP_STAT_MASK) == 0)
    {
    }
    CCM_ANALOG->MISC0_SET = CCM_ANALOG_MISC0_OSC_XTALOK_EN_MASK; /* detect freq */
    while ((CCM_ANALOG->MISC0 & CCM_ANALOG_MISC0_OSC_XTALOK_MASK) == 0)
    {
    }
    CCM_ANALOG->MISC0_CLR = CCM_ANALOG_MISC0_OSC_XTALOK_EN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the external 24MHz clock by powering up the crystal oscillator, waiting for stabilization, and enabling/disabling frequency detection
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization of the external clock peripheral. GetFunctionInfo shows it contains MMIO register accesses to CCM_ANALOG and XTALOSC24M registers. GetMMIOFunctionInfo confirms binary operations on hardware registers. The function has two polling loops waiting for hardware status flags (XTALOSC_PWRUP_STAT_MASK and OSC_XTALOK_MASK). It's called from BOARD_BootClockRUN during system initialization. While it contains LOOP characteristics (polling), its primary purpose is initialization, so INIT classification takes precedence over LOOP. The function doesn't involve NVIC/OS operations (not CORE), data transmission (not RECV), or interrupt handling (not IRQ).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitExternalClk(bool bypassXtalOsc)
{
    /* This device does not support bypass XTAL OSC. */
    assert(!bypassXtalOsc);

    /* [INIT REMOVED] Power up external crystal oscillator */
    /* CCM_ANALOG->MISC0_CLR = CCM_ANALOG_MISC0_XTAL_24M_PWD_MASK; */
    
    /* [LOOP REMOVED] Wait for oscillator power-up status */
    /* while ((XTALOSC24M->LOWPWR_CTRL & XTALOSC24M_LOWPWR_CTRL_XTALOSC_PWRUP_STAT_MASK) == 0) */
    /* { */
    /* } */
    
    /* [INIT REMOVED] Enable oscillator frequency detection */
    /* CCM_ANALOG->MISC0_SET = CCM_ANALOG_MISC0_OSC_XTALOK_EN_MASK; */
    
    /* [LOOP REMOVED] Wait for oscillator ready status */
    /* while ((CCM_ANALOG->MISC0 & CCM_ANALOG_MISC0_OSC_XTALOK_MASK) == 0) */
    /* { */
    /* } */
    
    /* [INIT REMOVED] Disable oscillator frequency detection */
    /* CCM_ANALOG->MISC0_CLR = CCM_ANALOG_MISC0_OSC_XTALOK_EN_MASK; */
}
```

=== 信息结束 ===
```

### CLOCK_InitRcOsc24M

```text
=== CLOCK_InitRcOsc24M 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：197
- 函数内容：void CLOCK_InitRcOsc24M(void)
{
    XTALOSC24M->LOWPWR_CTRL |= XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the 24MHz RC oscillator by enabling it through hardware register access
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs peripheral initialization (24MHz RC oscillator), 2) It contains hardware register access (XTALOSC24M->LOWPWR_CTRL |= XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK), 3) It is called from BOARD_BootClockRUN during system initialization, 4) It does not fit other classifications (not CORE/NVIC, not RECV/data transfer, not IRQ/interrupt handler, not LOOP/polling, not RETURNOK/status return, not SKIP/debug, not NODRIVER). The function's sole purpose is to enable the RC oscillator hardware, making it a clear INIT candidate.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initialize the RC oscillator 24MHz clock.
*/
void CLOCK_InitRcOsc24M(void)
{
    /* [INIT REMOVED] Hardware register access removed for simulation */
}
```

=== 信息结束 ===
```

### CLOCK_InitSysPfd

```text
=== CLOCK_InitSysPfd 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：1038
- 函数内容：void CLOCK_InitSysPfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd528;

    pfd528 = CCM_ANALOG->PFD_528 &
             ~((CCM_ANALOG_PFD_528_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_528_PFD0_FRAC_MASK) << (8 * pfdIndex));

    /* Disable the clock output first. */
    CCM_ANALOG->PFD_528 = pfd528 | (CCM_ANALOG_PFD_528_PFD0_CLKGATE_MASK << (8 * pfdIndex));

    /* Set the new value and enable output. */
    CCM_ANALOG->PFD_528 = pfd528 | (CCM_ANALOG_PFD_528_PFD0_FRAC(pfdFrac) << (8 * pfdIndex));
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the System PLL PFD (Phase Fractional Divider) for clock generation by configuring PFD fractional values and enabling/disabling clock output.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization of the System PLL PFD clock peripheral. It reads and writes to CCM_ANALOG->PFD_528 register to disable clock output, set new fractional values, and re-enable output. The function contains direct MMIO register accesses for hardware configuration, making it an INIT type function. It does not involve data transmission/reception (not RECV), interrupt handling (not IRQ), polling loops (not LOOP), or core OS/NVIC operations (not CORE). The replacement removes all hardware register accesses while preserving parameter processing logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitSysPfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd528;

    /* Skip hardware register access for PFD configuration */
    /* Original: pfd528 = CCM_ANALOG->PFD_528 & ~((CCM_ANALOG_PFD_528_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_528_PFD0_FRAC_MASK) << (8 * pfdIndex)); */
    /* Original: CCM_ANALOG->PFD_528 = pfd528 | (CCM_ANALOG_PFD_528_PFD0_CLKGATE_MASK << (8 * pfdIndex)); */
    /* Original: CCM_ANALOG->PFD_528 = pfd528 | (CCM_ANALOG_PFD_528_PFD0_FRAC(pfdFrac) << (8 * pfdIndex)); */
    
    /* Preserve parameter processing logic */
    (void)pfdIndex;
    (void)pfd528;
    (void)pfdFrac;
    
    /* Clock PFD initialization completed in simulation */
}
```

=== 信息结束 ===
```

### CLOCK_InitSysPll

```text
=== CLOCK_InitSysPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：512
- 函数内容：void CLOCK_InitSysPll(const clock_sys_pll_config_t *config)
{
    /* Bypass PLL first */
    CCM_ANALOG->PLL_SYS = (CCM_ANALOG->PLL_SYS & (~CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC_MASK)) |
                          CCM_ANALOG_PLL_SYS_BYPASS_MASK | CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_SYS =
        (CCM_ANALOG->PLL_SYS & (~(CCM_ANALOG_PLL_SYS_DIV_SELECT_MASK | CCM_ANALOG_PLL_SYS_POWERDOWN_MASK))) |
        CCM_ANALOG_PLL_SYS_ENABLE_MASK | CCM_ANALOG_PLL_SYS_DIV_SELECT(config->loopDivider);

    /* Initialize the fractional mode */
    CCM_ANALOG->PLL_SYS_NUM = CCM_ANALOG_PLL_SYS_NUM_A(config->numerator);
    CCM_ANALOG->PLL_SYS_DENOM = CCM_ANALOG_PLL_SYS_DENOM_B(config->denominator);

    /* Initialize the spread spectrum mode */
    CCM_ANALOG->PLL_SYS_SS = CCM_ANALOG_PLL_SYS_SS_STEP(config->ss_step) |
                             CCM_ANALOG_PLL_SYS_SS_ENABLE(config->ss_enable) |
                             CCM_ANALOG_PLL_SYS_SS_STOP(config->ss_stop);

    while ((CCM_ANALOG->PLL_SYS & CCM_ANALOG_PLL_SYS_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_SYS &= ~CCM_ANALOG_PLL_SYS_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the System PLL (Phase-Locked Loop) with specific configuration settings for clock generation
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a PLL initialization function that performs multiple MMIO register writes to CCM_ANALOG registers. GetMMIOFunctionInfo confirmed hardware register accesses including writes to PLL_SYS, PLL_SYS_NUM, PLL_SYS_DENOM, and PLL_SYS_SS registers. The function contains a polling loop waiting for PLL lock flag. This is classified as INIT because: 1) It's primarily a hardware initialization function, 2) It configures clock/PLL hardware, 3) It contains MMIO operations that need to be removed for simulation, 4) It's not CORE (no NVIC/OS/VTOR operations), 5) It's not RECV/IRQ (no data transfer or interrupt handling). The polling loop is handled as part of the INIT classification strategy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitSysPll(const clock_sys_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware register writes removed for simulation */
    /* [LOOP REMOVED] Waited for PLL lock flag */
    /* [INIT REPLACEMENT] Bypass disable operation removed */
}
```

=== 信息结束 ===
```

### CLOCK_InitUsb1Pfd

```text
=== CLOCK_InitUsb1Pfd 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：1075
- 函数内容：void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd480;

    pfd480 = CCM_ANALOG->PFD_480 &
             ~((CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_480_PFD0_FRAC_MASK) << (8 * pfdIndex));

    /* Disable the clock output first. */
    CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK << (8 * pfdIndex));

    /* Set the new value and enable output. */
    CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_FRAC(pfdFrac) << (8 * pfdIndex));
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the USB1 PLL PFD (Phase Fractional Divider) clock by configuring the PFD fractional value in hardware registers
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization by writing to CCM_ANALOG->PFD_480 register to configure USB1 PLL PFD settings. It disables clock output first, sets new fractional value, then enables output. This is a peripheral initialization function with direct MMIO register access, fitting the INIT classification criteria. No data transmission/reception, interrupt handling, or OS operations are present.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd480;

    /* Skip hardware register access for simulation */
    /* Original: pfd480 = CCM_ANALOG->PFD_480 &
             ~((CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_480_PFD0_FRAC_MASK) << (8 * pfdIndex)); */

    /* Original: Disable the clock output first. */
    /* CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK << (8 * pfdIndex)); */

    /* Original: Set the new value and enable output. */
    /* CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_FRAC(pfdFrac) << (8 * pfdIndex)); */

    /* Preserve parameter processing for consistency */
    (void)pfdIndex;
    (void)pfd480;
    (void)pfdFrac;
}
```

=== 信息结束 ===
```

### CLOCK_InitUsb1Pll

```text
=== CLOCK_InitUsb1Pll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：554
- 函数内容：void CLOCK_InitUsb1Pll(const clock_usb_pll_config_t *config)
{
    /* Bypass PLL first */
    CCM_ANALOG->PLL_USB1 = (CCM_ANALOG->PLL_USB1 & (~CCM_ANALOG_PLL_USB1_BYPASS_CLK_SRC_MASK)) |
                           CCM_ANALOG_PLL_USB1_BYPASS_MASK | CCM_ANALOG_PLL_USB1_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_USB1 = (CCM_ANALOG->PLL_USB1 & (~CCM_ANALOG_PLL_USB1_DIV_SELECT_MASK)) |
                           CCM_ANALOG_PLL_USB1_ENABLE_MASK | CCM_ANALOG_PLL_USB1_POWER_MASK |
                           CCM_ANALOG_PLL_USB1_EN_USB_CLKS_MASK | CCM_ANALOG_PLL_USB1_DIV_SELECT(config->loopDivider);

    while ((CCM_ANALOG->PLL_USB1 & CCM_ANALOG_PLL_USB1_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_USB1 &= ~CCM_ANALOG_PLL_USB1_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the USB1 PLL (Phase-Locked Loop) with specific configuration settings including clock source and divider selection.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs hardware initialization of the USB1 PLL. GetMMIOFunctionInfo showed multiple MMIO register accesses to CCM_ANALOG->PLL_USB1 for configuring bypass mode, clock source, divider settings, and a polling loop waiting for PLL lock. The function is called by CLOCK_EnableUsbhs0PhyPllClock. This is clearly an initialization function (INIT type) as it sets up hardware configuration without involving data transmission, interrupts, or core OS/NVIC operations. The replacement removes all hardware-specific MMIO operations and polling loops while preserving the function signature.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitUsb1Pll(const clock_usb_pll_config_t *config)
{
    /* [INIT REPLACEMENT] USB1 PLL initialization removed for simulation */
    /* Original hardware operations:
     * - Configure PLL bypass mode and clock source
     * - Set PLL divider and enable PLL
     * - Wait for PLL lock
     * - Disable bypass mode
     */
    (void)config; /* Prevent unused parameter warning */
}
```

=== 信息结束 ===
```

### CLOCK_InitUsb2Pll

```text
=== CLOCK_InitUsb2Pll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：587
- 函数内容：void CLOCK_InitUsb2Pll(const clock_usb_pll_config_t *config)
{
    /* Bypass PLL first */
    CCM_ANALOG->PLL_USB2 = (CCM_ANALOG->PLL_USB2 & (~CCM_ANALOG_PLL_USB2_BYPASS_CLK_SRC_MASK)) |
                           CCM_ANALOG_PLL_USB2_BYPASS_MASK | CCM_ANALOG_PLL_USB2_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_USB2 = (CCM_ANALOG->PLL_USB2 & (~CCM_ANALOG_PLL_USB2_DIV_SELECT_MASK)) |
                           CCM_ANALOG_PLL_USB2_ENABLE_MASK | CCM_ANALOG_PLL_USB2_POWER_MASK |
                           CCM_ANALOG_PLL_USB2_EN_USB_CLKS_MASK | CCM_ANALOG_PLL_USB2_DIV_SELECT(config->loopDivider);

    while ((CCM_ANALOG->PLL_USB2 & CCM_ANALOG_PLL_USB2_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_USB2 &= ~CCM_ANALOG_PLL_USB2_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the USB2 PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider selection, and enabling features.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a hardware initialization function that configures USB2 PLL registers. GetMMIOFunctionInfo confirmed multiple hardware register accesses to CCM_ANALOG->PLL_USB2. The function contains a polling loop waiting for PLL lock status. According to classification priority: 1) Not CORE (no NVIC/OS/VTOR operations), 2) Not RECV (no data I/O), 3) Not IRQ (not interrupt-related), 4) Is INIT (hardware initialization function), 5) Contains LOOP (polling for lock) but INIT takes priority. The function is called by CLOCK_EnableUsbhs1PhyPllClock for USB PHY clock initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitUsb2Pll(const clock_usb_pll_config_t *config)
{
    /* Skip hardware-specific PLL initialization */
    /* Original: Bypass PLL first and configure registers */
    /* Original: Wait for PLL lock */
    /* Original: Disable bypass */
}
```

=== 信息结束 ===
```

### CLOCK_InitVideoPll

```text
=== CLOCK_InitVideoPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：707
- 函数内容：void CLOCK_InitVideoPll(const clock_video_pll_config_t *config)
{
    uint32_t pllVideo;
    uint32_t misc2 = 0;

    /* Bypass PLL first */
    CCM_ANALOG->PLL_VIDEO = (CCM_ANALOG->PLL_VIDEO & (~CCM_ANALOG_PLL_VIDEO_BYPASS_CLK_SRC_MASK)) |
                            CCM_ANALOG_PLL_VIDEO_BYPASS_MASK | CCM_ANALOG_PLL_VIDEO_BYPASS_CLK_SRC(config->src);

    CCM_ANALOG->PLL_VIDEO_NUM = CCM_ANALOG_PLL_VIDEO_NUM_A(config->numerator);
    CCM_ANALOG->PLL_VIDEO_DENOM = CCM_ANALOG_PLL_VIDEO_DENOM_B(config->denominator);

    /*
     * Set post divider:
     *
     * ------------------------------------------------------------------------
     * | config->postDivider | PLL_VIDEO[POST_DIV_SELECT]  | MISC2[VIDEO_DIV] |
     * ------------------------------------------------------------------------
     * |         1           |            2                |        0         |
     * ------------------------------------------------------------------------
     * |         2           |            1                |        0         |
     * ------------------------------------------------------------------------
     * |         4           |            2                |        3         |
     * ------------------------------------------------------------------------
     * |         8           |            1                |        3         |
     * ------------------------------------------------------------------------
     * |         16          |            0                |        3         |
     * ------------------------------------------------------------------------
     */
    pllVideo =
        (CCM_ANALOG->PLL_VIDEO & (~(CCM_ANALOG_PLL_VIDEO_DIV_SELECT_MASK | CCM_ANALOG_PLL_VIDEO_POWERDOWN_MASK))) |
        CCM_ANALOG_PLL_VIDEO_ENABLE_MASK | CCM_ANALOG_PLL_VIDEO_DIV_SELECT(config->loopDivider);

    switch (config->postDivider)
    {
        case 16:
            pllVideo |= CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(0);
            misc2 = CCM_ANALOG_MISC2_VIDEO_DIV(3);
            break;

        case 8:
            pllVideo |= CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(1);
            misc2 = CCM_ANALOG_MISC2_VIDEO_DIV(3);
            break;

        case 4:
            pllVideo |= CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(2);
            misc2 = CCM_ANALOG_MISC2_VIDEO_DIV(3);
            break;

        case 2:
            pllVideo |= CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(1);
            break;

        default:
            pllVideo |= CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(2);
            break;
    }

    CCM_ANALOG->MISC2 = (CCM_ANALOG->MISC2 & ~CCM_ANALOG_MISC2_VIDEO_DIV_MASK) | misc2;

    CCM_ANALOG->PLL_VIDEO = pllVideo;

    while ((CCM_ANALOG->PLL_VIDEO & CCM_ANALOG_PLL_VIDEO_LOCK_MASK) == 0)
    {
    }

    /* Disable Bypass */
    CCM_ANALOG->PLL_VIDEO &= ~CCM_ANALOG_PLL_VIDEO_BYPASS_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes and configures the video PLL (Phase-Locked Loop) with specific divider, numerator, denominator, and source settings.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs hardware initialization of the video PLL through multiple MMIO register writes to CCM_ANALOG registers (PLL_VIDEO, PLL_VIDEO_NUM, PLL_VIDEO_DENOM, MISC2). GetMMIOFunctionInfo confirmed extensive MMIO operations including register reads, writes, and bitwise operations. The function contains a polling loop that waits for PLL lock flag. This matches the INIT classification criteria: functions that initialize peripheral/configurations with MMIO operations. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler). The polling loop is a secondary characteristic handled within the INIT replacement strategy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initialize the video PLL.
*
* This function configures the Video PLL with specific settings
*
* param config   configuration to set to PLL.
*/
void CLOCK_InitVideoPll(const clock_video_pll_config_t *config)
{
    /* Remove all hardware-specific MMIO operations */
    /* Original function performed PLL configuration via CCM_ANALOG registers */
    
    /* Skip the polling loop that waits for PLL lock */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */
    
    /* No hardware operations needed in simulation */
}
```

=== 信息结束 ===
```

### CLOCK_SetDiv

```text
=== CLOCK_SetDiv 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.h
- 行号：919
- 函数内容：static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift = CCM_TUPLE_BUSY_SHIFT(divider);
    CCM_TUPLE_REG(CCM, divider) = (CCM_TUPLE_REG(CCM, divider) & (~CCM_TUPLE_MASK(divider))) |
                                  (((uint32_t)((value) << CCM_TUPLE_SHIFT(divider))) & CCM_TUPLE_MASK(divider));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* Wait until CCM internal handshake finish. */
        while (CCM->CDHIPR & (1U << busyShift))
        {
        }
    }
}


【替换更新】
- 更新代码：static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift = CCM_TUPLE_BUSY_SHIFT(divider);
    /* [INIT REMOVED] Hardware register write removed: CCM_TUPLE_REG(CCM, divider) = ... */

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* [LOOP REMOVED] Skip waiting for CCM internal handshake finish */
        /* while (CCM->CDHIPR & (1U << busyShift)) */
    }
}
- 更新原因：Update replacement to use consistent comment format from analysis. The build already succeeds, but ensuring the replacement follows the established pattern with proper INIT and LOOP removal comments.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift = CCM_TUPLE_BUSY_SHIFT(divider);
    /* [INIT REMOVED] Hardware register write removed: CCM_TUPLE_REG(CCM, divider) = ... */

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* [LOOP REMOVED] Skip waiting for CCM internal handshake finish */
        /* while (CCM->CDHIPR & (1U << busyShift)) */
    }
}
    原因：Update replacement to use consistent comment format from analysis. The build already succeeds, but ensuring the replacement follows the established pattern with proper INIT and LOOP removal comments.
    时间：

=== 信息结束 ===
```

### GPIO_PinInit

```text
=== GPIO_PinInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_gpio.c
- 行号：71
- 函数内容：void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable GPIO clock. */
    CLOCK_EnableClock(s_gpioClock[GPIO_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */

    /* Register reset to default value */
    base->IMR &= ~(1U << pin);

    /* Configure GPIO pin direction */
    if (Config->direction == kGPIO_DigitalInput)
    {
        base->GDIR &= ~(1U << pin);
    }
    else
    {
        GPIO_PinWrite(base, pin, Config->outputLogic);
        base->GDIR |= (1U << pin);
    }

    /* Configure GPIO pin interrupt mode */
    GPIO_SetPinInterruptConfig(base, pin, Config->interruptMode);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes a GPIO pin with specified configuration including direction, output logic, and interrupt mode
- 是否需要替换：是
- 分类/替换原因：This function performs GPIO peripheral initialization by configuring pin direction (input/output), setting initial output logic, and configuring interrupt modes. It accesses GPIO hardware registers (IMR, GDIR) and calls other GPIO configuration functions. GetMMIOFunctionInfo confirms hardware register accesses. The function is called from imxrt_pin_mode for GPIO setup. Since it's a peripheral initialization function that writes to hardware registers, it should be classified as INIT with hardware operations removed while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Skip GPIO clock enable in simulation */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */

    /* Skip register reset to default value */
    /* base->IMR &= ~(1U << pin); */

    /* Skip GPIO pin direction configuration */
    /* if (Config->direction == kGPIO_DigitalInput)
    {
        base->GDIR &= ~(1U << pin);
    }
    else
    {
        GPIO_PinWrite(base, pin, Config->outputLogic);
        base->GDIR |= (1U << pin);
    } */

    /* Skip GPIO pin interrupt mode configuration */
    /* GPIO_SetPinInterruptConfig(base, pin, Config->interruptMode); */
}
```

=== 信息结束 ===
```

### GPIO_PinWrite

```text
=== GPIO_PinWrite 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_gpio.c
- 行号：105
- 函数内容：void GPIO_PinWrite(GPIO_Type *base, uint32_t pin, uint8_t output)
{
    assert(pin < 32);
    if (output == 0U)
    {
        base->DR &= ~(1U << pin); /* Set pin output to low level.*/
    }
    else
    {
        base->DR |= (1U << pin); /* Set pin output to high level.*/
    }
}


【替换更新】
- 更新代码：void GPIO_PinWrite(GPIO_Type *base, uint32_t pin, uint8_t output)
{
    assert(pin < 32);
    /* Skip hardware write in emulation environment */
    (void)base;
    (void)pin;
    (void)output;
}
- 更新原因：Replace GPIO_PinWrite to avoid hardware MMIO writes in emulator environment. The function performs GPIO hardware register writes (base->DR) which are not needed in emulation. Preserve assert for pin validation but skip actual hardware operations.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void GPIO_PinWrite(GPIO_Type *base, uint32_t pin, uint8_t output)
{
    assert(pin < 32);
    /* Skip hardware write in emulation environment */
    (void)base;
    (void)pin;
    (void)output;
}
    原因：Replace GPIO_PinWrite to avoid hardware MMIO writes in emulator environment. The function performs GPIO hardware register writes (base->DR) which are not needed in emulation. Preserve assert for pin validation but skip actual hardware operations.
    时间：

=== 信息结束 ===
```

### GetUartSrcFreq

```text
=== GetUartSrcFreq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c
- 行号：559
- 函数内容：uint32_t GetUartSrcFreq(LPUART_Type *uart_base)
{
    uint32_t freq;
#ifdef SOC_IMXRT1170_SERIES
    uint32_t base = (uint32_t) uart_base;
    switch (base)
    {
    case LPUART1_BASE:
        freq = CLOCK_GetRootClockFreq(kCLOCK_Root_Lpuart1);
        break;
    case LPUART12_BASE:
        freq = CLOCK_GetRootClockFreq(kCLOCK_Root_Lpuart12);
        break;
    default:
        freq = CLOCK_GetRootClockFreq(kCLOCK_Root_Lpuart2);
        break;
    }
#else
    /* To make it simple, we assume default PLL and divider settings, and the only variable
       from application is use PLL3 source or OSC source */
    if (CLOCK_GetMux(kCLOCK_UartMux) == 0) /* PLL3 div6 80M */
    {
        freq = (CLOCK_GetPllFreq(kCLOCK_PllUsb1) / 6U) / (CLOCK_GetDiv(kCLOCK_UartDiv) + 1U);
    }
    else
    {
        freq = CLOCK_GetOscFreq() / (CLOCK_GetDiv(kCLOCK_UartDiv) + 1U);
    }
#endif
    return freq;

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Returns the clock source frequency for a UART peripheral based on its base address and system clock configuration
- 是否需要替换：是
- 分类/替换原因：This function is part of UART initialization/configuration flow, called by imxrt_configure to determine the clock frequency for UART peripheral setup. It queries system clock configuration (mux, PLL, oscillator, dividers) which is essential for proper peripheral initialization. While it doesn't contain direct MMIO operations, it calls clock configuration functions that likely read hardware registers. It fits the INIT category as it provides critical configuration information for peripheral setup.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
uint32_t GetUartSrcFreq(LPUART_Type *uart_base)
{
    uint32_t freq;
#ifdef SOC_IMXRT1170_SERIES
    uint32_t base = (uint32_t) uart_base;
    switch (base)
    {
    case LPUART1_BASE:
        freq = 80000000U; /* Default frequency for LPUART1 */
        break;
    case LPUART12_BASE:
        freq = 80000000U; /* Default frequency for LPUART12 */
        break;
    default:
        freq = 80000000U; /* Default frequency for other LPUARTs */
        break;
    }
#else
    /* Return a default frequency for simulation */
    freq = 80000000U; /* 80 MHz default frequency */
#endif
    return freq;
}
```

=== 信息结束 ===
```

### LPUART_Deinit

```text
=== LPUART_Deinit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c
- 行号：452
- 函数内容：void LPUART_Deinit(LPUART_Type *base)
{
    uint32_t temp;

#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* Wait tx FIFO send out*/
    while (0 != ((base->WATER & LPUART_WATER_TXCOUNT_MASK) >> LPUART_WATER_TXWATER_SHIFT))
    {
    }
#endif
    /* Wait last char shift out */
    while (0 == (base->STAT & LPUART_STAT_TC_MASK))
    {
    }

    /* Clear all status flags */
    temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK);

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    temp |= LPUART_STAT_LBKDIF_MASK;
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK);
#endif

    base->STAT |= temp;

    /* Disable the module. */
    base->CTRL = 0;

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    uint32_t instance = LPUART_GetInstance(base);

    /* Disable lpuart clock */
    CLOCK_DisableClock(s_lpuartClock[instance]);

#if defined(LPUART_PERIPH_CLOCKS)
    CLOCK_DisableClock(s_lpuartPeriphClocks[instance]);
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Deinitializes an LPUART instance by waiting for transmit completion, clearing status flags, disabling the module, and disabling the clock
- 是否需要替换：是
- 分类/替换原因：Function contains hardware-dependent polling loops waiting for TX FIFO to empty and transmission complete flags (base->WATER and base->STAT register accesses). These are classic LOOP patterns where the loop condition depends on peripheral registers. The function also performs register writes to clear status flags and disable the module, but the primary classification driver is the polling loops. According to classification priority: LOOP matches before RETURNOK/SKIP/NODRIVER.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void LPUART_Deinit(LPUART_Type *base)
{
    uint32_t temp;

#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* [LOOP REMOVED] Waited for TX FIFO to empty */
#endif
    /* [LOOP REMOVED] Waited for transmission complete flag */

    /* Clear all status flags - hardware operation removed */
    temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK);

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    temp |= LPUART_STAT_LBKDIF_MASK;
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK);
#endif

    /* Disable the module - hardware operation removed */

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    uint32_t instance = LPUART_GetInstance(base);

    /* Disable lpuart clock */
    CLOCK_DisableClock(s_lpuartClock[instance]);

#if defined(LPUART_PERIPH_CLOCKS)
    CLOCK_DisableClock(s_lpuartPeriphClocks[instance]);
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

=== 信息结束 ===
```

### LPUART_EnableInterrupts

```text
=== LPUART_EnableInterrupts 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c
- 行号：659
- 函数内容：void LPUART_EnableInterrupts(LPUART_Type *base, uint32_t mask)
{
    base->BAUD |= ((mask << 8) & (LPUART_BAUD_LBKDIE_MASK | LPUART_BAUD_RXEDGIE_MASK));
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    base->FIFO = (base->FIFO & ~(LPUART_FIFO_TXOF_MASK | LPUART_FIFO_RXUF_MASK)) |
                 ((mask << 8) & (LPUART_FIFO_TXOFE_MASK | LPUART_FIFO_RXUFE_MASK));
#endif
    mask &= 0xFFFFFF00U;
    base->CTRL |= mask;
}


【替换更新】
- 更新代码：void LPUART_EnableInterrupts(LPUART_Type *base, uint32_t mask)
{
    /* Preserve register writes for emulator to observe */
    /* The emulator needs to see these writes to simulate LPUART interrupts */
    base->BAUD |= ((mask << 8) & (LPUART_BAUD_LBKDIE_MASK | LPUART_BAUD_RXEDGIE_MASK));
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    base->FIFO = (base->FIFO & ~(LPUART_FIFO_TXOF_MASK | LPUART_FIFO_RXUF_MASK)) |
                 ((mask << 8) & (LPUART_FIFO_TXOFE_MASK | LPUART_FIFO_RXUFE_MASK));
#endif
    mask &= 0xFFFFFF00U;
    base->CTRL |= mask;
}
- 更新原因：Fix LPUART_EnableInterrupts while preserving register writes. The emulator needs to observe hardware register writes to properly simulate LPUART interrupts. Keep the original hardware writes but they will be intercepted by the emulator's memory hooks.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void LPUART_EnableInterrupts(LPUART_Type *base, uint32_t mask)
{
    /* Preserve register writes for emulator to observe */
    /* The emulator needs to see these writes to simulate LPUART interrupts */
    base->BAUD |= ((mask << 8) & (LPUART_BAUD_LBKDIE_MASK | LPUART_BAUD_RXEDGIE_MASK));
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    base->FIFO = (base->FIFO & ~(LPUART_FIFO_TXOF_MASK | LPUART_FIFO_RXUF_MASK)) |
                 ((mask << 8) & (LPUART_FIFO_TXOFE_MASK | LPUART_FIFO_RXUFE_MASK));
#endif
    mask &= 0xFFFFFF00U;
    base->CTRL |= mask;
}
    原因：Fix LPUART_EnableInterrupts while preserving register writes. The emulator needs to observe hardware register writes to properly simulate LPUART interrupts. Keep the original hardware writes but they will be intercepted by the emulator's memory hooks.
    时间：

=== 信息结束 ===
```

### LPUART_GetStatusFlags

```text
=== LPUART_GetStatusFlags 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c
- 行号：743
- 函数内容：uint32_t LPUART_GetStatusFlags(LPUART_Type *base)
{
    uint32_t temp;
    temp = base->STAT;
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    temp |= (base->FIFO &
             (LPUART_FIFO_TXEMPT_MASK | LPUART_FIFO_RXEMPT_MASK | LPUART_FIFO_TXOF_MASK | LPUART_FIFO_RXUF_MASK)) >>
            16;
#endif
    return temp;
}


【替换更新】
- 更新代码：uint32_t LPUART_GetStatusFlags(LPUART_Type *base)
{
    uint32_t temp;
    /* In emulation, simulate status flags */
    /* Read the STAT register to preserve the observable read */
    temp = base->STAT;
    
    /* Always set TxDataRegEmptyFlag to avoid wait loops */
    /* kLPUART_TxDataRegEmptyFlag is typically 0x00800000U */
    temp |= 0x00800000U;
    
    return temp;
}
- 更新原因：Fix LPUART_GetStatusFlags to prevent hardware wait loops while preserving register read. Read the STAT register (emulator will intercept) and always set TxDataRegEmptyFlag to avoid wait loops in emulation. This allows the wait loop in imxrt_putc to exit immediately.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：uint32_t LPUART_GetStatusFlags(LPUART_Type *base)
{
    uint32_t temp;
    /* In emulation, simulate status flags */
    /* For TxDataRegEmptyFlag, always return true to avoid wait loops */
    /* For RxDataRegFullFlag, return false (no data available) */
    temp = kLPUART_TxDataRegEmptyFlag; /* Always indicate TX is ready */
    
    return temp;
}
    原因：Fix LPUART_GetStatusFlags to prevent hardware wait loops in emulation. The original function reads hardware status register which won't change in emulation. Return simulated status flags: always indicate TX is ready (to avoid wait loops) and RX has no data (unless we implement stdin simulation).
    时间：

  版本 2:
    替换代码：uint32_t LPUART_GetStatusFlags(LPUART_Type *base)
{
    uint32_t temp;
    /* In emulation, simulate status flags */
    /* Read the STAT register to preserve the observable read */
    temp = base->STAT;
    
    /* Always set TxDataRegEmptyFlag to avoid wait loops */
    /* kLPUART_TxDataRegEmptyFlag is typically 0x00800000U */
    temp |= 0x00800000U;
    
    return temp;
}
    原因：Fix LPUART_GetStatusFlags to prevent hardware wait loops while preserving register read. Read the STAT register (emulator will intercept) and always set TxDataRegEmptyFlag to avoid wait loops in emulation. This allows the wait loop in imxrt_putc to exit immediately.
    时间：

=== 信息结束 ===
```

### LPUART_Init

```text
=== LPUART_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c
- 行号：236
- 函数内容：status_t LPUART_Init(LPUART_Type *base, const lpuart_config_t *config, uint32_t srcClock_Hz)
{
    assert(config);
    assert(config->baudRate_Bps);
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->txFifoWatermark);
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->rxFifoWatermark);
#endif

    uint32_t temp;
    uint16_t sbr, sbrTemp;
    uint32_t osr, osrTemp, tempDiff, calculatedBaud, baudDiff;

    /* This LPUART instantiation uses a slightly different baud rate calculation
     * The idea is to use the best OSR (over-sampling rate) possible
     * Note, OSR is typically hard-set to 16 in other LPUART instantiations
     * loop to find the best OSR value possible, one that generates minimum baudDiff
     * iterate through the rest of the supported values of OSR */

    baudDiff = config->baudRate_Bps;
    osr = 0;
    sbr = 0;
    for (osrTemp = 4; osrTemp <= 32; osrTemp++)
    {
        /* calculate the temporary sbr value   */
        sbrTemp = (srcClock_Hz / (config->baudRate_Bps * osrTemp));
        /*set sbrTemp to 1 if the sourceClockInHz can not satisfy the desired baud rate*/
        if (sbrTemp == 0)
        {
            sbrTemp = 1;
        }
        /* Calculate the baud rate based on the temporary OSR and SBR values */
        calculatedBaud = (srcClock_Hz / (osrTemp * sbrTemp));

        tempDiff = calculatedBaud - config->baudRate_Bps;

        /* Select the better value between srb and (sbr + 1) */
        if (tempDiff > (config->baudRate_Bps - (srcClock_Hz / (osrTemp * (sbrTemp + 1)))))
        {
            tempDiff = config->baudRate_Bps - (srcClock_Hz / (osrTemp * (sbrTemp + 1)));
            sbrTemp++;
        }

        if (tempDiff <= baudDiff)
        {
            baudDiff = tempDiff;
            osr = osrTemp; /* update and store the best OSR value calculated */
            sbr = sbrTemp; /* update store the best SBR value calculated */
        }
    }

    /* Check to see if actual baud rate is within 3% of desired baud rate
     * based on the best calculate OSR value */
    if (baudDiff > ((config->baudRate_Bps / 100) * 3))
    {
        /* Unacceptable baud rate difference of more than 3%*/
        return kStatus_LPUART_BaudrateNotSupport;
    }

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)

    uint32_t instance = LPUART_GetInstance(base);

    /* Enable lpuart clock */
    CLOCK_EnableClock(s_lpuartClock[instance]);
#if defined(LPUART_PERIPH_CLOCKS)
    CLOCK_EnableClock(s_lpuartPeriphClocks[instance]);
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */

#if defined(FSL_FEATURE_LPUART_HAS_GLOBAL) && FSL_FEATURE_LPUART_HAS_GLOBAL
    /*Reset all internal logic and registers, except the Global Register */
    LPUART_SoftwareReset(base);
#else
    /* Disable LPUART TX RX before setting. */
    base->CTRL &= ~(LPUART_CTRL_TE_MASK | LPUART_CTRL_RE_MASK);
#endif

    temp = base->BAUD;

    /* Acceptable baud rate, check if OSR is between 4x and 7x oversampling.
     * If so, then "BOTHEDGE" sampling must be turned on */
    if ((osr > 3) && (osr < 8))
    {
        temp |= LPUART_BAUD_BOTHEDGE_MASK;
    }

    /* program the osr value (bit value is one less than actual value) */
    temp &= ~LPUART_BAUD_OSR_MASK;
    temp |= LPUART_BAUD_OSR(osr - 1);

    /* write the sbr value to the BAUD registers */
    temp &= ~LPUART_BAUD_SBR_MASK;
    base->BAUD = temp | LPUART_BAUD_SBR(sbr);

    /* Set bit count and parity mode. */
    base->BAUD &= ~LPUART_BAUD_M10_MASK;

    temp = base->CTRL &
           ~(LPUART_CTRL_PE_MASK | LPUART_CTRL_PT_MASK | LPUART_CTRL_M_MASK | LPUART_CTRL_ILT_MASK |
             LPUART_CTRL_IDLECFG_MASK);

    temp |=
        (uint8_t)config->parityMode | LPUART_CTRL_IDLECFG(config->rxIdleConfig) | LPUART_CTRL_ILT(config->rxIdleType);

#if defined(FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT) && FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT
    if (kLPUART_SevenDataBits == config->dataBitsCount)
    {
        if (kLPUART_ParityDisabled != config->parityMode)
        {
            temp &= ~LPUART_CTRL_M7_MASK; /* Seven data bits and one parity bit */
        }
        else
        {
            temp |= LPUART_CTRL_M7_MASK;
        }
    }
    else
#endif
    {
        if (kLPUART_ParityDisabled != config->parityMode)
        {
            temp |= LPUART_CTRL_M_MASK; /* Eight data bits and one parity bit */
        }
    }

    base->CTRL = temp;

#if defined(FSL_FEATURE_LPUART_HAS_STOP_BIT_CONFIG_SUPPORT) && FSL_FEATURE_LPUART_HAS_STOP_BIT_CONFIG_SUPPORT
    /* set stop bit per char */
    temp = base->BAUD & ~LPUART_BAUD_SBNS_MASK;
    base->BAUD = temp | LPUART_BAUD_SBNS((uint8_t)config->stopBitCount);
#endif

#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* Set tx/rx WATER watermark
       Note:
       Take care of the RX FIFO, RX interrupt request only assert when received bytes
       equal or more than RX water mark, there is potential issue if RX water
       mark larger than 1.
       For example, if RX FIFO water mark is 2, upper layer needs 5 bytes and
       5 bytes are received. the last byte will be saved in FIFO but not trigger
       RX interrupt because the water mark is 2.
     */
    base->WATER = (((uint32_t)(config->rxFifoWatermark) << 16) | config->txFifoWatermark);

    /* Enable tx/rx FIFO */
    base->FIFO |= (LPUART_FIFO_TXFE_MASK | LPUART_FIFO_RXFE_MASK);

    /* Flush FIFO */
    base->FIFO |= (LPUART_FIFO_TXFLUSH_MASK | LPUART_FIFO_RXFLUSH_MASK);
#endif

    /* Clear all status flags */
    temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK);

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    temp |= LPUART_STAT_LBKDIF_MASK;
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK);
#endif

#if defined(FSL_FEATURE_LPUART_HAS_MODEM_SUPPORT) && FSL_FEATURE_LPUART_HAS_MODEM_SUPPORT
    /* Set the CTS configuration/TX CTS source. */
    base->MODIR |= LPUART_MODIR_TXCTSC(config->txCtsConfig) | LPUART_MODIR_TXCTSSRC(config->txCtsSource);
    if (config->enableRxRTS)
    {
        /* Enable the receiver RTS(request-to-send) function. */
        base->MODIR |= LPUART_MODIR_RXRTSE_MASK;
    }
    if (config->enableTxCTS)
    {
        /* Enable the CTS(clear-to-send) function. */
        base->MODIR |= LPUART_MODIR_TXCTSE_MASK;
    }
#endif

    /* Set data bits order. */
    if (config->isMsb)
    {
        temp |= LPUART_STAT_MSBF_MASK;
    }
    else
    {
        temp &= ~LPUART_STAT_MSBF_MASK;
    }

    base->STAT |= temp;

    /* Enable TX/RX base on configure structure. */
    temp = base->CTRL;
    if (config->enableTx)
    {
        temp |= LPUART_CTRL_TE_MASK;
    }

    if (config->enableRx)
    {
        temp |= LPUART_CTRL_RE_MASK;
    }

    base->CTRL = temp;

    return kStatus_Success;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes an LPUART instance with user configuration including baud rate, parity, data bits, stop bits, FIFO settings, and other UART parameters.
- 是否需要替换：是
- 分类/替换原因：LPUART_Init is classified as INIT because: 1) It is a peripheral initialization function that configures LPUART hardware registers (BAUD, CTRL, STAT, WATER, FIFO, MODIR). 2) GetMMIOFunctionInfo analysis shows hardware register accesses throughout the function. 3) The function performs clock enabling, software reset, and comprehensive hardware configuration. 4) It contains algorithmic baud rate calculation but the core purpose is hardware initialization. 5) It does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), and does not contain peripheral-dependent polling loops (not LOOP). 6) It is not a CORE function as it doesn't involve NVIC, OS kernel, or VTOR operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
status_t LPUART_Init(LPUART_Type *base, const lpuart_config_t *config, uint32_t srcClock_Hz)
{
    assert(config);
    assert(config->baudRate_Bps);
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->txFifoWatermark);
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->rxFifoWatermark);
#endif

    uint32_t temp;
    uint16_t sbr, sbrTemp;
    uint32_t osr, osrTemp, tempDiff, calculatedBaud, baudDiff;

    /* This LPUART instantiation uses a slightly different baud rate calculation
     * The idea is to use the best OSR (over-sampling rate) possible
     * Note, OSR is typically hard-set to 16 in other LPUART instantiations
     * loop to find the best OSR value possible, one that generates minimum baudDiff
     * iterate through the rest of the supported values of OSR */

    baudDiff = config->baudRate_Bps;
    osr = 0;
    sbr = 0;
    for (osrTemp = 4; osrTemp <= 32; osrTemp++)
    {
        /* calculate the temporary sbr value   */
        sbrTemp = (srcClock_Hz / (config->baudRate_Bps * osrTemp));
        /*set sbrTemp to 1 if the sourceClockInHz can not satisfy the desired baud rate*/
        if (sbrTemp == 0)
        {
            sbrTemp = 1;
        }
        /* Calculate the baud rate based on the temporary OSR and SBR values */
        calculatedBaud = (srcClock_Hz / (osrTemp * sbrTemp));

        tempDiff = calculatedBaud - config->baudRate_Bps;

        /* Select the better value between srb and (sbr + 1) */
        if (tempDiff > (config->baudRate_Bps - (srcClock_Hz / (osrTemp * (sbrTemp + 1)))))
        {
            tempDiff = config->baudRate_Bps - (srcClock_Hz / (osrTemp * (sbrTemp + 1)));
            sbrTemp++;
        }

        if (tempDiff <= baudDiff)
        {
            baudDiff = tempDiff;
            osr = osrTemp; /* update and store the best OSR value calculated */
            sbr = sbrTemp; /* update store the best SBR value calculated */
        }
    }

    /* Check to see if actual baud rate is within 3% of desired baud rate
     * based on the best calculate OSR value */
    if (baudDiff > ((config->baudRate_Bps / 100) * 3))
    {
        /* Unacceptable baud rate difference of more than 3%*/
        return kStatus_LPUART_BaudrateNotSupport;
    }

    /* Skip hardware-specific configuration */
    return kStatus_Success;
}
```

=== 信息结束 ===
```

### LPUART_ReadByte

```text
=== LPUART_ReadByte 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.h
- 行号：601
- 函数内容：static inline uint8_t LPUART_ReadByte(LPUART_Type *base)
{
#if defined(FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT) && FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT
    uint32_t ctrl = base->CTRL;
    bool isSevenDataBits =
        ((ctrl & LPUART_CTRL_M7_MASK) ||
         ((!(ctrl & LPUART_CTRL_M7_MASK)) && (!(ctrl & LPUART_CTRL_M_MASK)) && (ctrl & LPUART_CTRL_PE_MASK)));

    if (isSevenDataBits)
    {
        return (base->DATA & 0x7F);
    }
    else
    {
        return base->DATA;
    }
#else
    return base->DATA;
#endif
}


【替换更新】
- 更新代码：static inline uint8_t LPUART_ReadByte(LPUART_Type *base)
{
    /* Read from DATA register (emulator will intercept) */
    /* In emulation, this will return 0 or simulated data */
#if defined(FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT) && FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT
    uint32_t ctrl = base->CTRL;
    bool isSevenDataBits =
        ((ctrl & LPUART_CTRL_M7_MASK) ||
         ((!(ctrl & LPUART_CTRL_M7_MASK)) && (!(ctrl & LPUART_CTRL_M_MASK)) && (ctrl & LPUART_CTRL_PE_MASK)));

    if (isSevenDataBits)
    {
        return (base->DATA & 0x7F);
    }
    else
    {
        return base->DATA;
    }
#else
    return base->DATA;
#endif
}
- 更新原因：Fix LPUART_ReadByte to preserve register reads. The original function reads from DATA register. Keep the structure but the emulator will intercept the read. This allows proper interaction with the emulator's memory hooks.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline uint8_t LPUART_ReadByte(LPUART_Type *base)
{
    /* Read from DATA register (emulator will intercept) */
    /* In emulation, this will return 0 or simulated data */
#if defined(FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT) && FSL_FEATURE_LPUART_HAS_7BIT_DATA_SUPPORT
    uint32_t ctrl = base->CTRL;
    bool isSevenDataBits =
        ((ctrl & LPUART_CTRL_M7_MASK) ||
         ((!(ctrl & LPUART_CTRL_M7_MASK)) && (!(ctrl & LPUART_CTRL_M_MASK)) && (ctrl & LPUART_CTRL_PE_MASK)));

    if (isSevenDataBits)
    {
        return (base->DATA & 0x7F);
    }
    else
    {
        return base->DATA;
    }
#else
    return base->DATA;
#endif
}
    原因：Fix LPUART_ReadByte to preserve register reads. The original function reads from DATA register. Keep the structure but the emulator will intercept the read. This allows proper interaction with the emulator's memory hooks.
    时间：

=== 信息结束 ===
```

### LPUART_WriteByte

```text
=== LPUART_WriteByte 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.h
- 行号：587
- 函数内容：static inline void LPUART_WriteByte(LPUART_Type *base, uint8_t data)
{
    base->DATA = data;
}


【替换更新】
- 更新代码：static inline void LPUART_WriteByte(LPUART_Type *base, uint8_t data)
{
    /* Write to DATA register (emulator will intercept) */
    base->DATA = data;
}
- 更新原因：Fix LPUART_WriteByte to preserve register writes. The original function writes to DATA register. Keep the structure but the emulator will intercept the write. This allows proper interaction with the emulator's memory hooks and potential output simulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline void LPUART_WriteByte(LPUART_Type *base, uint8_t data)
{
    /* Write to DATA register (emulator will intercept) */
    base->DATA = data;
}
    原因：Fix LPUART_WriteByte to preserve register writes. The original function writes to DATA register. Keep the structure but the emulator will intercept the write. This allows proper interaction with the emulator's memory hooks and potential output simulation.
    时间：

=== 信息结束 ===
```

### SysTick_Config

```text
=== SysTick_Config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/CMSIS/Include/core_cm7.h
- 行号：2553
- 函数内容：__STATIC_INLINE uint32_t SysTick_Config(uint32_t ticks)
{
  if ((ticks - 1UL) > SysTick_LOAD_RELOAD_Msk)
  {
    return (1UL);                                                   /* Reload value impossible */
  }

  SysTick->LOAD  = (uint32_t)(ticks - 1UL);                         /* set reload register */
  NVIC_SetPriority (SysTick_IRQn, (1UL << __NVIC_PRIO_BITS) - 1UL); /* set Priority for Systick Interrupt */
  SysTick->VAL   = 0UL;                                             /* Load the SysTick Counter Value */
  SysTick->CTRL  = SysTick_CTRL_CLKSOURCE_Msk |
                   SysTick_CTRL_TICKINT_Msk   |
                   SysTick_CTRL_ENABLE_Msk;                         /* Enable SysTick IRQ and SysTick Timer */
  return (0UL);                                                     /* Function successful */
}


【替换更新】
- 更新代码：/**
\brief   System Tick Configuration
\details Initializes the System Timer and its interrupt, and starts the System Tick Timer.
Counter is in free running mode to generate periodic interrupts.
\param [in]  ticks  Number of ticks between two interrupts.
\return          0  Function succeeded.
\return          1  Function failed.
\note    When the variable <b>__Vendor_SysTickConfig</b> is set to 1, then the
function <b>SysTick_Config</b> is not included. In this case, the file <b><i>device</i>.h</b>
must contain a vendor-specific implementation of this function.
*/
__STATIC_INLINE uint32_t SysTick_Config(uint32_t ticks)
{
  if ((ticks - 1UL) > SysTick_LOAD_RELOAD_Msk)
  {
    return (1UL);                                                   /* Reload value impossible */
  }

  /* CRITICAL: Preserve SysTick register writes for OS scheduling */
  SysTick->LOAD  = (uint32_t)(ticks - 1UL);                         /* set reload register */
  NVIC_SetPriority (SysTick_IRQn, (1UL << __NVIC_PRIO_BITS) - 1UL); /* set Priority for Systick Interrupt */
  SysTick->VAL   = 0UL;                                             /* Load the SysTick Counter Value */
  SysTick->CTRL  = SysTick_CTRL_CLKSOURCE_Msk |
                   SysTick_CTRL_TICKINT_Msk   |
                   SysTick_CTRL_ENABLE_Msk;                         /* Enable SysTick IRQ and SysTick Timer */
  return (0UL);                                                     /* Function successful */
}
- 更新原因：This function is CRITICAL for OS scheduling. According to the requirements, SysTick register writes (LOAD, VAL, CTRL) MUST be preserved as they are essential for timer interrupts and OS tick generation. The NVIC_SetPriority call should also be preserved. The replacement keeps all hardware register writes intact to ensure proper OS scheduling in emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
\brief   System Tick Configuration
\details Initializes the System Timer and its interrupt, and starts the System Tick Timer.
Counter is in free running mode to generate periodic interrupts.
\param [in]  ticks  Number of ticks between two interrupts.
\return          0  Function succeeded.
\return          1  Function failed.
\note    When the variable <b>__Vendor_SysTickConfig</b> is set to 1, then the
function <b>SysTick_Config</b> is not included. In this case, the file <b><i>device</i>.h</b>
must contain a vendor-specific implementation of this function.
*/
__STATIC_INLINE uint32_t SysTick_Config(uint32_t ticks)
{
  if ((ticks - 1UL) > SysTick_LOAD_RELOAD_Msk)
  {
    return (1UL);                                                   /* Reload value impossible */
  }

  /* CRITICAL: Preserve SysTick register writes for OS scheduling */
  SysTick->LOAD  = (uint32_t)(ticks - 1UL);                         /* set reload register */
  NVIC_SetPriority (SysTick_IRQn, (1UL << __NVIC_PRIO_BITS) - 1UL); /* set Priority for Systick Interrupt */
  SysTick->VAL   = 0UL;                                             /* Load the SysTick Counter Value */
  SysTick->CTRL  = SysTick_CTRL_CLKSOURCE_Msk |
                   SysTick_CTRL_TICKINT_Msk   |
                   SysTick_CTRL_ENABLE_Msk;                         /* Enable SysTick IRQ and SysTick Timer */
  return (0UL);                                                     /* Function successful */
}
    原因：This function is CRITICAL for OS scheduling. According to the requirements, SysTick register writes (LOAD, VAL, CTRL) MUST be preserved as they are essential for timer interrupts and OS tick generation. The NVIC_SetPriority call should also be preserved. The replacement keeps all hardware register writes intact to ensure proper OS scheduling in emulation.
    时间：

=== 信息结束 ===
```

### SystemCoreClockUpdate

```text
=== SystemCoreClockUpdate 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/system_MIMXRT1052.c
- 行号：128
- 函数内容：void SystemCoreClockUpdate (void) {

    uint32_t freq;
    uint32_t PLL1MainClock;
    uint32_t PLL2MainClock;

    /* Periph_clk2_clk ---> Periph_clk */
    if (CCM->CBCDR & CCM_CBCDR_PERIPH_CLK_SEL_MASK)
    {
        switch (CCM->CBCMR & CCM_CBCMR_PERIPH_CLK2_SEL_MASK)
        {
            /* Pll3_sw_clk ---> Periph_clk2_clk ---> Periph_clk */
            case CCM_CBCMR_PERIPH_CLK2_SEL(0U):
                if(CCM_ANALOG->PLL_USB1 & CCM_ANALOG_PLL_USB1_BYPASS_MASK)
                {
                    freq = (((CCM_ANALOG->PLL_USB1 & CCM_ANALOG_PLL_USB1_BYPASS_CLK_SRC_MASK) >> CCM_ANALOG_PLL_USB1_BYPASS_CLK_SRC_SHIFT) == 0U) ?
                           CPU_XTAL_CLK_HZ : CPU_CLK1_HZ;
                }
                else
                {
                    freq = (CPU_XTAL_CLK_HZ * ((CCM_ANALOG->PLL_USB1 & CCM_ANALOG_PLL_USB1_DIV_SELECT_MASK) ? 22U : 20U));
                }
                break;

            /* Osc_clk ---> Periph_clk2_clk ---> Periph_clk */
            case CCM_CBCMR_PERIPH_CLK2_SEL(1U):
                freq = CPU_XTAL_CLK_HZ;
                break;

            case CCM_CBCMR_PERIPH_CLK2_SEL(2U):
                freq = (((CCM_ANALOG->PLL_SYS & CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC_MASK) >> CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC_SHIFT) == 0U) ?
                   CPU_XTAL_CLK_HZ : CPU_CLK1_HZ;

            case CCM_CBCMR_PERIPH_CLK2_SEL(3U):
            default:
                freq = 0U;
                break;
        }

        freq /= (((CCM->CBCDR & CCM_CBCDR_PERIPH_CLK2_PODF_MASK) >> CCM_CBCDR_PERIPH_CLK2_PODF_SHIFT) + 1U);
    }
    /* Pre_Periph_clk ---> Periph_clk */
    else
    {
        /* check if pll is bypassed */
        if(CCM_ANALOG->PLL_ARM & CCM_ANALOG_PLL_ARM_BYPASS_MASK)
        {
            PLL1MainClock = (((CCM_ANALOG->PLL_ARM & CCM_ANALOG_PLL_ARM_BYPASS_CLK_SRC_MASK) >> CCM_ANALOG_PLL_ARM_BYPASS_CLK_SRC_SHIFT) == 0U) ?
                   CPU_XTAL_CLK_HZ : CPU_CLK1_HZ;
        }
        else
        {
            PLL1MainClock = ((CPU_XTAL_CLK_HZ * ((CCM_ANALOG->PLL_ARM & CCM_ANALOG_PLL_ARM_DIV_SELECT_MASK) >>
                                             CCM_ANALOG_PLL_ARM_DIV_SELECT_SHIFT)) >> 1U);
        }

        /* check if pll is bypassed */
        if(CCM_ANALOG->PLL_SYS & CCM_ANALOG_PLL_SYS_BYPASS_MASK)
        {
            PLL2MainClock = (((CCM_ANALOG->PLL_SYS & CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC_MASK) >> CCM_ANALOG_PLL_SYS_BYPASS_CLK_SRC_SHIFT) == 0U) ?
                   CPU_XTAL_CLK_HZ : CPU_CLK1_HZ;
        }
        else
        {
            PLL2MainClock = (CPU_XTAL_CLK_HZ * ((CCM_ANALOG->PLL_SYS & CCM_ANALOG_PLL_SYS_DIV_SELECT_MASK) ? 22U : 20U));
        }
        PLL2MainClock += ((uint64_t)CPU_XTAL_CLK_HZ * ((uint64_t)(CCM_ANALOG->PLL_SYS_NUM))) / ((uint64_t)(CCM_ANALOG->PLL_SYS_DENOM));


        switch (CCM->CBCMR & CCM_CBCMR_PRE_PERIPH_CLK_SEL_MASK)
        {
            /* PLL2 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(0U):
                freq = PLL2MainClock;
                break;

            /* PLL2 PFD2 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(1U):
                freq = PLL2MainClock / ((CCM_ANALOG->PFD_528 & CCM_ANALOG_PFD_528_PFD2_FRAC_MASK) >> CCM_ANALOG_PFD_528_PFD2_FRAC_SHIFT) * 18U;
                break;

            /* PLL2 PFD0 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(2U):
                freq = PLL2MainClock / ((CCM_ANALOG->PFD_528 & CCM_ANALOG_PFD_528_PFD0_FRAC_MASK) >> CCM_ANALOG_PFD_528_PFD0_FRAC_SHIFT) * 18U;
                break;

            /* PLL1 divided(/2) ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(3U):
                freq = PLL1MainClock / (((CCM->CACRR & CCM_CACRR_ARM_PODF_MASK) >> CCM_CACRR_ARM_PODF_SHIFT) + 1U);
                break;

            default:
                freq = 0U;
                break;
        }
    }

    SystemCoreClock = (freq / (((CCM->CBCDR & CCM_CBCDR_AHB_PODF_MASK) >> CCM_CBCDR_AHB_PODF_SHIFT) + 1U));

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Updates the system core clock frequency by reading clock control module registers and calculating the current clock configuration.
- 是否需要替换：是
- 分类/替换原因：This function reads multiple hardware registers (CCM->CBCDR, CCM->CBCMR, CCM_ANALOG->PLL_USB1, CCM_ANALOG->PLL_SYS, CCM_ANALOG->PLL_ARM, CCM_ANALOG->PFD_528, CCM->CACRR) to determine the current clock configuration and updates the global SystemCoreClock variable. It performs hardware-dependent register reads but doesn't write to hardware or perform initialization of hardware resources. It's classified as INIT because it initializes/updates system state (the core clock frequency) based on hardware configuration. The replacement provides a reasonable default clock frequency (600 MHz for i.MX RT1052) for emulation instead of reading non-existent hardware registers.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void SystemCoreClockUpdate (void) {
    /* Provide a reasonable default system core clock frequency for emulation */
    /* Typical i.MX RT1052 runs at 600 MHz */
    SystemCoreClock = 600000000U;
}
```

=== 信息结束 ===
```

### SystemInit

```text
=== SystemInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/system_MIMXRT1052.c
- 行号：73
- 函数内容：void SystemInit (void) {
#if ((__FPU_PRESENT == 1) && (__FPU_USED == 1))
  SCB->CPACR |= ((3UL << 10*2) | (3UL << 11*2));    /* set CP10, CP11 Full Access */
#endif /* ((__FPU_PRESENT == 1) && (__FPU_USED == 1)) */

#if defined(__MCUXPRESSO)
    extern uint32_t g_pfnVectors[];  // Vector table defined in startup code
    SCB->VTOR = (uint32_t)g_pfnVectors;
#endif

/* Disable Watchdog Power Down Counter */
WDOG1->WMCR &= ~WDOG_WMCR_PDE_MASK;
WDOG2->WMCR &= ~WDOG_WMCR_PDE_MASK;

/* Watchdog disable */

#if (DISABLE_WDOG)
    if (WDOG1->WCR & WDOG_WCR_WDE_MASK)
    {
        WDOG1->WCR &= ~WDOG_WCR_WDE_MASK;
    }
    if (WDOG2->WCR & WDOG_WCR_WDE_MASK)
    {
        WDOG2->WCR &= ~WDOG_WCR_WDE_MASK;
    }
    RTWDOG->CNT = 0xD928C520U; /* 0xD928C520U is the update key */
    RTWDOG->TOVAL = 0xFFFF;
    RTWDOG->CS = (uint32_t) ((RTWDOG->CS) & ~RTWDOG_CS_EN_MASK) | RTWDOG_CS_UPDATE_MASK;
#endif /* (DISABLE_WDOG) */

    /* Disable Systick which might be enabled by bootrom */
    if (SysTick->CTRL & SysTick_CTRL_ENABLE_Msk)
    {
        SysTick->CTRL &= ~SysTick_CTRL_ENABLE_Msk;
    }

/* Enable instruction and data caches */
#if defined(__ICACHE_PRESENT) && __ICACHE_PRESENT
    if (SCB_CCR_IC_Msk != (SCB_CCR_IC_Msk & SCB->CCR)) {
        SCB_EnableICache();
    }
#endif
#if defined(__DCACHE_PRESENT) && __DCACHE_PRESENT
    if (SCB_CCR_DC_Msk != (SCB_CCR_DC_Msk & SCB->CCR)) {
        SCB_EnableDCache();
    }
#endif

  SystemInitHook();
}


【初始分析（FunctionClassifier）】
- 函数类型：CORE
- 函数用途/功能描述：System initialization function that configures core system registers including VTOR (vector table offset), FPU access, watchdog timers, SysTick, and caches
- 是否需要替换：否
- 分类/替换原因：Function contains SCB->VTOR write operation which sets the vector table offset - this is explicitly listed in CORE classification criteria. The function also accesses other core system registers (SCB->CPACR) and performs system-level initialization. According to classification priority (CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER), CORE takes precedence when VTOR operations are present. The emulator needs to see these register writes to properly simulate interrupts and scheduling.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：/* ----------------------------------------------------------------------------
-- SystemInit()
---------------------------------------------------------------------------- */
void SystemInit (void) {
#if ((__FPU_PRESENT == 1) && (__FPU_USED == 1))
  /* Preserve FPU access configuration */
  SCB->CPACR |= ((3UL << 10*2) | (3UL << 11*2));    /* set CP10, CP11 Full Access */
#endif /* ((__FPU_PRESENT == 1) && (__FPU_USED == 1)) */

  /* CRITICAL: Preserve VTOR write for emulation */
  /* For emulation, we need to set VTOR so the emulator can see it */
  /* Use conditional compilation to handle different toolchains */
#if defined(__MCUXPRESSO)
    /* Original MCUXpresso code */
    extern uint32_t g_pfnVectors[];  // Vector table defined in startup code
    SCB->VTOR = (uint32_t)g_pfnVectors;
#else
    /* For other toolchains, set VTOR to a reasonable default */
    /* The vector table is typically at the start of flash (0x60000000 for i.MX RT1052) */
    /* This allows the emulator to see the VTOR write */
    SCB->VTOR = 0x60000000U;
#endif

/* Skip watchdog power down counter disable (not needed in simulation) */
/* Original: WDOG1->WMCR &= ~WDOG_WMCR_PDE_MASK; */
/* Original: WDOG2->WMCR &= ~WDOG_WMCR_PDE_MASK; */

/* Skip watchdog disable logic (not needed in simulation) */
#if (DISABLE_WDOG)
    /* Skip watchdog disable operations */
#endif /* (DISABLE_WDOG) */

    /* Preserve Systick disable operation */
    if (SysTick->CTRL & SysTick_CTRL_ENABLE_Msk)
    {
        SysTick->CTRL &= ~SysTick_CTRL_ENABLE_Msk;
    }

/* Skip cache enable operations (not needed in simulation) */
#if defined(__ICACHE_PRESENT) && __ICACHE_PRESENT
    /* Skip instruction cache enable */
#endif
#if defined(__DCACHE_PRESENT) && __DCACHE_PRESENT
    /* Skip data cache enable */
#endif

  SystemInitHook();
}
- 更新原因：Fix VTOR write to handle both MCUXpresso and other toolchains. For MCUXpresso, use the original g_pfnVectors symbol. For other toolchains, set VTOR to a reasonable default (0x60000000 for i.MX RT1052 flash start). This ensures the emulator always sees a VTOR write, which is critical for proper interrupt and scheduling simulation. The previous version caused linker errors when g_pfnVectors was not defined.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/* ----------------------------------------------------------------------------
-- SystemInit()
---------------------------------------------------------------------------- */
void SystemInit (void) {
#if ((__FPU_PRESENT == 1) && (__FPU_USED == 1))
  /* Preserve FPU access configuration */
  SCB->CPACR |= ((3UL << 10*2) | (3UL << 11*2));    /* set CP10, CP11 Full Access */
#endif /* ((__FPU_PRESENT == 1) && (__FPU_USED == 1)) */

#if defined(__MCUXPRESSO)
    /* CRITICAL: Preserve VTOR write - DO NOT REMOVE */
    extern uint32_t g_pfnVectors[];  // Vector table defined in startup code
    SCB->VTOR = (uint32_t)g_pfnVectors;
#endif

/* Skip watchdog power down counter disable (not needed in simulation) */
/* Original: WDOG1->WMCR &= ~WDOG_WMCR_PDE_MASK; */
/* Original: WDOG2->WMCR &= ~WDOG_WMCR_PDE_MASK; */

/* Skip watchdog disable logic (not needed in simulation) */
#if (DISABLE_WDOG)
    /* Skip watchdog disable operations */
#endif /* (DISABLE_WDOG) */

    /* Preserve Systick disable operation */
    if (SysTick->CTRL & SysTick_CTRL_ENABLE_Msk)
    {
        SysTick->CTRL &= ~SysTick_CTRL_ENABLE_Msk;
    }

/* Skip cache enable operations (not needed in simulation) */
#if defined(__ICACHE_PRESENT) && __ICACHE_PRESENT
    /* Skip instruction cache enable */
#endif
#if defined(__DCACHE_PRESENT) && __DCACHE_PRESENT
    /* Skip data cache enable */
#endif

  SystemInitHook();
}
    原因：This function is critical for system initialization. According to the CRITICAL requirements: 1) SCB->VTOR writes MUST be preserved (vector table setup), 2) SysTick->CTRL writes should be preserved (system timer control), 3) SCB->CPACR for FPU should be preserved. Other hardware operations (watchdog, cache control) can be removed for simulation as they don't affect OS scheduling or interrupt handling. The replacement preserves the essential operations while removing unnecessary hardware-specific code.
    时间：

  版本 2:
    替换代码：/* ----------------------------------------------------------------------------
-- SystemInit()
---------------------------------------------------------------------------- */
void SystemInit (void) {
#if ((__FPU_PRESENT == 1) && (__FPU_USED == 1))
  /* Preserve FPU access configuration */
  SCB->CPACR |= ((3UL << 10*2) | (3UL << 11*2));    /* set CP10, CP11 Full Access */
#endif /* ((__FPU_PRESENT == 1) && (__FPU_USED == 1)) */

  /* CRITICAL: Preserve VTOR write for emulation */
  /* For emulation, we need to set VTOR so the emulator can see it */
  /* Use conditional compilation to handle different toolchains */
#if defined(__MCUXPRESSO)
    /* Original MCUXpresso code */
    extern uint32_t g_pfnVectors[];  // Vector table defined in startup code
    SCB->VTOR = (uint32_t)g_pfnVectors;
#else
    /* For other toolchains, set VTOR to a reasonable default */
    /* The vector table is typically at the start of flash (0x60000000 for i.MX RT1052) */
    /* This allows the emulator to see the VTOR write */
    SCB->VTOR = 0x60000000U;
#endif

/* Skip watchdog power down counter disable (not needed in simulation) */
/* Original: WDOG1->WMCR &= ~WDOG_WMCR_PDE_MASK; */
/* Original: WDOG2->WMCR &= ~WDOG_WMCR_PDE_MASK; */

/* Skip watchdog disable logic (not needed in simulation) */
#if (DISABLE_WDOG)
    /* Skip watchdog disable operations */
#endif /* (DISABLE_WDOG) */

    /* Preserve Systick disable operation */
    if (SysTick->CTRL & SysTick_CTRL_ENABLE_Msk)
    {
        SysTick->CTRL &= ~SysTick_CTRL_ENABLE_Msk;
    }

/* Skip cache enable operations (not needed in simulation) */
#if defined(__ICACHE_PRESENT) && __ICACHE_PRESENT
    /* Skip instruction cache enable */
#endif
#if defined(__DCACHE_PRESENT) && __DCACHE_PRESENT
    /* Skip data cache enable */
#endif

  SystemInitHook();
}
    原因：Fix VTOR write to handle both MCUXpresso and other toolchains. For MCUXpresso, use the original g_pfnVectors symbol. For other toolchains, set VTOR to a reasonable default (0x60000000 for i.MX RT1052 flash start). This ensures the emulator always sees a VTOR write, which is critical for proper interrupt and scheduling simulation. The previous version caused linker errors when g_pfnVectors was not defined.
    时间：

=== 信息结束 ===
```

### XBARA_Deinit

```text
=== XBARA_Deinit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c
- 行号：88
- 函数内容：void XBARA_Deinit(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Disable XBARA module clock. */
    CLOCK_DisableClock(s_xbaraClock[XBARA_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Shuts down the XBARA module by disabling its clock
- 是否需要替换：是
- 分类/替换原因：This is a peripheral deinitialization function that disables hardware clocks. GetFunctionInfo shows it calls CLOCK_DisableClock() which likely contains MMIO operations. GetMMIOFunctionInfo returned empty list but the function is clearly hardware-dependent as it operates on XBARA peripheral. According to classification priority, INIT functions include initialization/deinitialization operations. This function should have its hardware operations removed while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Shuts down the XBARA module.
*
* This function disables XBARA clock.
*
* param base XBARA peripheral address.
*/
void XBARA_Deinit(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Disable XBARA module clock. */
    /* [INIT REMOVED] CLOCK_DisableClock(s_xbaraClock[XBARA_GetInstance(base)]); */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

=== 信息结束 ===
```

### XBARA_Init

```text
=== XBARA_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c
- 行号：73
- 函数内容：void XBARA_Init(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable XBARA module clock. */
    CLOCK_EnableClock(s_xbaraClock[XBARA_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the XBARA (Crossbar A) module by enabling its clock
- 是否需要替换：是
- 分类/替换原因：This is a peripheral initialization function that enables the clock for the XBARA module. GetFunctionInfo shows it calls CLOCK_EnableClock which likely contains MMIO operations for clock gating. GetMMIOFunctionInfo returned empty list but the function clearly performs hardware initialization. It fits the INIT classification as it sets up peripheral configuration without data I/O, interrupt handling, or polling loops. The replacement removes hardware-specific clock enabling while preserving the conditional compilation structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void XBARA_Init(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware-specific clock enabling removed for simulation */
    (void)base; /* Mark parameter as used to avoid warnings */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

【替换更新】
- 更新代码：void XBARA_Init(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware-specific clock enabling removed for simulation */
    (void)base; /* Mark parameter as used to avoid warnings */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
- 更新原因：Update replacement to include (void)base to avoid potential unused parameter warnings while preserving original function structure

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void XBARA_Init(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware clock enable removed for simulation */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Finalizing replacement with proper structure matching original function
    时间：

  版本 2:
    替换代码：void XBARA_Init(XBARA_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware-specific clock enabling removed for simulation */
    (void)base; /* Mark parameter as used to avoid warnings */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Update replacement to include (void)base to avoid potential unused parameter warnings while preserving original function structure
    时间：

=== 信息结束 ===
```

### XBARB_Init

```text
=== XBARB_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbarb.c
- 行号：73
- 函数内容：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable XBARB module clock. */
    CLOCK_EnableClock(s_xbarbClock[XBARB_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}


【初始分析（FunctionClassifier）】
- 函数类型：SKIP
- 函数用途/功能描述：Initializes the XBARB (Crossbar B) module by enabling its clock gate
- 是否需要替换：是
- 分类/替换原因：This function enables the clock for XBARB peripheral through CLOCK_EnableClock(). While it performs hardware register writes, it's a simple clock gating operation that can be safely ignored for simulation. The original INIT classification would require removing hardware operations, but build verification showed pre-existing compilation errors in other files, and the fixer restored the original implementation. Given the function's simplicity and the optional nature of clock enabling for simulation, SKIP classification is appropriate. The function doesn't initialize data structures or affect upper-layer logic, making it safe to skip.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable XBARB module clock. */
    CLOCK_EnableClock(s_xbarbClock[XBARB_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

【替换更新】
- 更新代码：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable XBARB module clock. */
    CLOCK_EnableClock(s_xbarbClock[XBARB_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
- 更新原因：Restoring original XBARB_Init implementation with proper clock enable call as the previous replacement was incomplete and might be causing compilation issues

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Enable XBARB module clock. */
    CLOCK_EnableClock(s_xbarbClock[XBARB_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Restoring original XBARB_Init implementation with proper clock enable call as the previous replacement was incomplete and might be causing compilation issues
    时间：

=== 信息结束 ===
```

### imxrt_getc

```text
=== imxrt_getc 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c
- 行号：701
- 函数内容：static int imxrt_getc(struct rt_serial_device *serial)
{
    int ch;
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    ch = -1;
    if (LPUART_GetStatusFlags(uart->uart_base) & kLPUART_RxDataRegFullFlag)
    {
        ch = LPUART_ReadByte(uart->uart_base);
    }

    return ch;
}


【替换更新】
- 更新代码：static int imxrt_getc(struct rt_serial_device *serial)
{
    int ch;
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    ch = -1;
    /* Check if data is available */
    /* LPUART_GetStatusFlags doesn't set RxDataRegFullFlag by default */
    /* So this will typically return -1 (no data) */
    if (LPUART_GetStatusFlags(uart->uart_base) & kLPUART_RxDataRegFullFlag)
    {
        ch = LPUART_ReadByte(uart->uart_base);
    }
    
    return ch;
}
- 更新原因：Update imxrt_getc to work with replaced LPUART_GetStatusFlags. Keep the original structure but rely on replaced LPUART_GetStatusFlags which doesn't set RxDataRegFullFlag by default, so it will return -1 (no data) in emulation unless we implement stdin simulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int imxrt_getc(struct rt_serial_device *serial)
{
    int ch;
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    /* In emulation, we simulate reading from stdin */
    /* Use HAL_BE_In to read from stdin if available */
    /* For now, return -1 to indicate no data available */
    ch = -1;
    
    return ch;
}
    原因：Fix potential issues in imxrt_getc. The original function checks for hardware flag kLPUART_RxDataRegFullFlag which won't be set in emulation. In POSIX emulation, we should handle input differently or return -1 to indicate no data available.
    时间：

  版本 2:
    替换代码：static int imxrt_getc(struct rt_serial_device *serial)
{
    int ch;
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    ch = -1;
    /* Check if data is available */
    /* LPUART_GetStatusFlags doesn't set RxDataRegFullFlag by default */
    /* So this will typically return -1 (no data) */
    if (LPUART_GetStatusFlags(uart->uart_base) & kLPUART_RxDataRegFullFlag)
    {
        ch = LPUART_ReadByte(uart->uart_base);
    }
    
    return ch;
}
    原因：Update imxrt_getc to work with replaced LPUART_GetStatusFlags. Keep the original structure but rely on replaced LPUART_GetStatusFlags which doesn't set RxDataRegFullFlag by default, so it will return -1 (no data) in emulation unless we implement stdin simulation.
    时间：

=== 信息结束 ===
```

### imxrt_pin_mode

```text
=== imxrt_pin_mode 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_gpio.c
- 行号：522
- 函数内容：static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        LOG_D("invalid pin,rtt pin: %d,port: %d,pin: %d \n", pin,port + 1,pin_num);
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
#endif
    }
    break;

    case PIN_MODE_INPUT:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLDOWN:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x3030U;    /* 100K Ohm Pull Down */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLUP:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0xB030U;    /* 100K Ohm Pull Up */
#endif
    }
    break;

    case PIN_MODE_OUTPUT_OD:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;
    }
#ifndef SOC_IMXRT1170_SERIES
    if (mask_tab[port].gpio != GPIO5)
    {
        CLOCK_EnableClock(kCLOCK_Iomuxc);
        IOMUXC_SetPinMux(MUX_BASE + reg_offset[pin] * 4, 0x5U, 0, 0, CONFIG_BASE + reg_offset[pin] * 4, 1);
        IOMUXC_SetPinConfig(MUX_BASE + reg_offset[pin] * 4, 0x5U, 0, 0, CONFIG_BASE + reg_offset[pin] * 4, config_value);
    }
    else
    {
        CLOCK_EnableClock(kCLOCK_IomuxcSnvs);
        IOMUXC_SetPinMux(GPIO5_MUX_BASE + pin_num * 4, 0x5U, 0, 0, GPIO5_CONFIG_BASE + pin_num * 4, 1);
        IOMUXC_SetPinConfig(GPIO5_MUX_BASE + pin_num * 4, 0x5U, 0, 0, GPIO5_CONFIG_BASE + pin_num * 4, config_value);
    }
#else
    if ((mask_tab[port].gpio != GPIO6) && (mask_tab[port].gpio != GPIO13))
    {
        CLOCK_EnableClock(kCLOCK_Iomuxc);
        IOMUXC_SetPinMux(MUX_BASE + reg_offset[pin] * 4, 0x5U, 0, 0, CONFIG_BASE + reg_offset[pin] * 4, 1);
    }
    if (mask_tab[port].gpio == GPIO6)
    {
        CLOCK_EnableClock(kCLOCK_Iomuxc_Lpsr);
        IOMUXC_SetPinMux(GPIO6_MUX_BASE + pin_num * 4, 0x5U, 0, 0, GPIO6_CONFIG_BASE + pin_num * 4, 1);
    }
    if (mask_tab[port].gpio == GPIO13)
    {
        CLOCK_EnableClock(kCLOCK_Iomuxc);
        IOMUXC_SetPinMux(GPIO13_MUX_BASE + pin_num * 4, 0x5U, 0, 0, GPIO13_CONFIG_BASE + pin_num * 4, 1);
    }

#endif

    GPIO_PinInit(mask_tab[port].gpio, pin_num, &gpio);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures GPIO pin mode (input/output/pull-up/pull-down/open-drain) and IOMUX settings for i.MX RT processors
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization: enables clock gates for IOMUXC, configures pin multiplexing via IOMUXC_SetPinMux, sets pin electrical properties via IOMUXC_SetPinConfig, and initializes GPIO pin direction/interrupt mode via GPIO_PinInit. GetMMIOFunctionInfo shows it's in CodeQL MMIOFunction set. Analysis reveals it's a static GPIO configuration function that sets up peripheral hardware for different pin modes. Classification as INIT is appropriate because it initializes and configures hardware resources (GPIO pins and IOMUX settings).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        /* LOG_D removed to fix compilation error */
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
#endif
    }
    break;

    case PIN_MODE_INPUT:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLDOWN:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x3030U;    /* 100K Ohm Pull Down */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLUP:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0xB030U;    /* 100K Ohm Pull Up */
#endif
    }
    break;

    case PIN_MODE_OUTPUT_OD:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;
    }

    /* Skip hardware-specific configuration */
    /* Mark variables as used to avoid warnings */
    (void)gpio;
#ifndef SOC_IMXRT1170_SERIES
    (void)config_value;
#endif
    (void)port;
    (void)pin_num;
    (void)dev;
}
```

【替换更新】
- 更新代码：static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        /* LOG_D removed to fix compilation error */
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
#endif
    }
    break;

    case PIN_MODE_INPUT:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLDOWN:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x3030U;    /* 100K Ohm Pull Down */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLUP:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0xB030U;    /* 100K Ohm Pull Up */
#endif
    }
    break;

    case PIN_MODE_OUTPUT_OD:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;
    }

    /* Skip hardware-specific configuration */
    /* Mark variables as used to avoid warnings */
    (void)gpio;
#ifndef SOC_IMXRT1170_SERIES
    (void)config_value;
#endif
    (void)port;
    (void)pin_num;
    (void)dev;
}
- 更新原因：Use verified working replacement with complete (void) casts for all unused variables to fix compilation verification

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        /* LOG_D removed to fix compilation error - original had split string literal */
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
#endif
    }
    break;

    case PIN_MODE_INPUT:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLDOWN:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x3030U;    /* 100K Ohm Pull Down */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLUP:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0xB030U;    /* 100K Ohm Pull Up */
#endif
    }
    break;

    case PIN_MODE_OUTPUT_OD:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;
    }

    /* Skip hardware-specific configuration */
    /* Mark variables as used to avoid warnings */
    (void)gpio;
#ifndef SOC_IMXRT1170_SERIES
    (void)config_value;
#endif
    (void)port;
    (void)pin_num;
    (void)dev;
}
    原因：Function already fixed - removed problematic LOG_D macro call with split string literal that was causing compilation errors. Added (void) casts for unused variables. Build verification shows successful compilation with exit code 0.
    时间：

  版本 2:
    替换代码：static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        /* LOG_D removed to fix compilation error */
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
#endif
    }
    break;

    case PIN_MODE_INPUT:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLDOWN:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x3030U;    /* 100K Ohm Pull Down */
#endif
    }
    break;

    case PIN_MODE_INPUT_PULLUP:
    {
        gpio.direction = kGPIO_DigitalInput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0xB030U;    /* 100K Ohm Pull Up */
#endif
    }
    break;

    case PIN_MODE_OUTPUT_OD:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0830U;    /* Open Drain Enable */
#endif
    }
    break;
    }

    /* Skip hardware-specific configuration */
    /* Mark variables as used to avoid warnings */
    (void)gpio;
#ifndef SOC_IMXRT1170_SERIES
    (void)config_value;
#endif
    (void)port;
    (void)pin_num;
    (void)dev;
}
    原因：Use verified working replacement with complete (void) casts for all unused variables to fix compilation verification
    时间：

=== 信息结束 ===
```

### imxrt_putc

```text
=== imxrt_putc 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c
- 行号：688
- 函数内容：static int imxrt_putc(struct rt_serial_device *serial, char ch)
{
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    LPUART_WriteByte(uart->uart_base, ch);
    while (!(LPUART_GetStatusFlags(uart->uart_base) & kLPUART_TxDataRegEmptyFlag));

    return 1;
}


【替换更新】
- 更新代码：static int imxrt_putc(struct rt_serial_device *serial, char ch)
{
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    /* Write to DATA register (emulator will intercept) */
    LPUART_WriteByte(uart->uart_base, ch);
    
    /* Check status flags - LPUART_GetStatusFlags now returns TxDataRegEmptyFlag set */
    /* So this wait loop will exit immediately */
    while (!(LPUART_GetStatusFlags(uart->uart_base) & kLPUART_TxDataRegEmptyFlag));
    
    return 1;
}
- 更新原因：Update imxrt_putc to work with replaced LPUART_GetStatusFlags. Keep the original structure but rely on replaced LPUART_GetStatusFlags which always returns TxDataRegEmptyFlag set, allowing the wait loop to exit immediately in emulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int imxrt_putc(struct rt_serial_device *serial, char ch)
{
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    /* In emulation, we simulate writing the byte without hardware wait */
    /* Skip the hardware register write and wait loop */
    /* Just return success to indicate byte was "written" */
    
    return 1;
}
    原因：Fix exceptional loop in imxrt_putc. The original function contains a hardware wait loop that waits for LPUART_TxDataRegEmptyFlag, which causes infinite loop in emulation. In POSIX emulation, we should skip hardware-dependent operations and return success immediately.
    时间：

  版本 2:
    替换代码：static int imxrt_putc(struct rt_serial_device *serial, char ch)
{
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    /* Write to DATA register (emulator will intercept) */
    LPUART_WriteByte(uart->uart_base, ch);
    
    /* Check status flags - LPUART_GetStatusFlags now returns TxDataRegEmptyFlag set */
    /* So this wait loop will exit immediately */
    while (!(LPUART_GetStatusFlags(uart->uart_base) & kLPUART_TxDataRegEmptyFlag));
    
    return 1;
}
    原因：Update imxrt_putc to work with replaced LPUART_GetStatusFlags. Keep the original structure but rely on replaced LPUART_GetStatusFlags which always returns TxDataRegEmptyFlag set, allowing the wait loop to exit immediately in emulation.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**51** 个；CodeQL `MMIOFunction`：**51** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **11** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `BOARD_BootClockRUN` | INIT | True | System clock initialization function that configures the entire clock tree including oscillators, PLLs, clock divider... |
| `BOARD_InitPins` | INIT | True | Configures pin routing and electrical features for the board by enabling IOMUXC clock and setting up pin mux configur... |
| `CLOCK_DeinitArmPll` | INIT | True | De-initializes (powers down) the ARM PLL by writing power-down mask to PLL control register. |
| `CLOCK_DeinitAudioPll` | SKIP | False | De-initializes the Audio PLL by writing a power-down mask to the PLL control register. |
| `CLOCK_DeinitEnetPll` | RETURNOK | False | Deinitializes the ENET PLL by disabling it through hardware register access |
| `CLOCK_DeinitExternalClk` | RETURNOK | False | Deinitializes and powers down the external 24MHz clock oscillator |
| `CLOCK_DeinitRcOsc24M` | SKIP | False | Powers down the RCOSC 24M clock by clearing the RC_OSC_EN bit in the XTALOSC24M LOWPWR_CTRL register. |
| `CLOCK_DeinitSysPfd` | INIT | False | De-initializes (disables) the System PLL PFD clock by setting the clock gate bit in the PFD_528 register. |
| `CLOCK_DeinitSysPll` | RETURNOK | False | De-initializes (powers down) the System PLL by writing a power-down mask to the clock control register. |
| `CLOCK_DeinitUsb1Pfd` | SKIP | False | De-initializes (disables) the USB1 PLL PFD (Phase Frequency Detector) clock |
| `CLOCK_DeinitUsb1Pll` | SKIP | True | Deinitializes the USB1 PLL by writing 0 to its control register |
| `CLOCK_DeinitUsb2Pll` | INIT | True | Deinitializes the USB2 PLL by setting its control register to 0 |
| `CLOCK_DeinitVideoPll` | INIT | True | De-initializes the Video PLL by setting the powerdown mask in the CCM_ANALOG register |
| `CLOCK_DisableUsbhs0PhyPllClock` | INIT | True | Disables the USB HS PHY PLL clock by clearing the USB clock enable bit and setting the clock gate bit. |
| `CLOCK_DisableUsbhs1PhyPllClock` | INIT | True | Disables USB HS PHY PLL clock by clearing clock enable bit and setting clock gate bit |
| `CLOCK_EnableUsbhs0Clock` | INIT | False | Enables USB HS clock by configuring clock gating registers, resetting USB controller, and setting up power management |
| `CLOCK_EnableUsbhs0PhyPllClock` | INIT | True | Enables the USB HS PHY PLL clock by configuring the USB PHY PLL clock source and releasing the PHY from reset. |
| `CLOCK_EnableUsbhs1Clock` | INIT | False | Enables USB HS clock and initializes USB HS peripheral hardware including clock gating, controller reset, and PMU con... |
| `CLOCK_EnableUsbhs1PhyPllClock` | INIT | True | Enables the internal 480MHz USB HS PHY PLL clock by initializing USB2 PLL and configuring USB PHY control registers |
| `CLOCK_GetAhbFreq` | RETURNOK | False | Calculates and returns the AHB (Advanced High-performance Bus) clock frequency in hertz based on hardware register co... |
| `CLOCK_GetFreq` | NODRIVER | False | Gets the clock frequency for a specific clock name by routing to appropriate frequency calculation functions |
| `CLOCK_GetIpgFreq` | RETURNOK | False | Calculates and returns the IPG (IP bus) clock frequency by reading the CCM CBCDR register divider value and dividing ... |
| `CLOCK_GetPerClkFreq` | RETURNOK | False | Gets the PER (Peripheral) clock frequency in hertz by reading clock configuration registers |
| `CLOCK_GetPeriphClkFreq` | RETURNOK | False | Reads CCM (Clock Control Module) registers to determine and return the peripheral clock frequency based on current cl... |
| `CLOCK_GetPllFreq` | RETURNOK | False | Gets the current output frequency of a specific PLL (Arm, Sys, Usb1, Audio, Video, Enet, etc.) by reading hardware re... |
| `CLOCK_GetSemcFreq` | RETURNOK | False | Reads SEMC (Smart External Memory Controller) clock frequency from hardware clock configuration registers |
| `CLOCK_GetSysPfdFreq` | RETURNOK | False | Calculates and returns the current System PLL PFD (Phase Fractional Divider) output frequency based on the selected P... |
| `CLOCK_GetUsb1PfdFreq` | RETURNOK | False | Calculates and returns the current USB1 PLL PFD (Phase Fractional Divider) output frequency based on the selected PFD... |
| `CLOCK_InitArmPll` | INIT | False | Initializes the ARM PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider selec... |
| `CLOCK_InitAudioPll` | INIT | True | Initializes the Audio PLL with specific configuration settings including bypass, numerator/denominator values, and po... |
| `CLOCK_InitEnetPll` | INIT | True | Initializes the ENET (Ethernet) PLL (Phase-Locked Loop) with specific configuration settings including divider, clock... |
| `CLOCK_InitExternalClk` | INIT | True | Initializes the external 24MHz clock by powering up the crystal oscillator, waiting for stabilization, and enabling/d... |
| `CLOCK_InitRcOsc24M` | INIT | True | Initializes the 24MHz RC oscillator by enabling it through hardware register access |
| `CLOCK_InitSysPfd` | INIT | True | Initializes the System PLL PFD (Phase Fractional Divider) for clock generation by configuring PFD fractional values a... |
| `CLOCK_InitSysPll` | INIT | True | Initializes the System PLL (Phase-Locked Loop) with specific configuration settings for clock generation |
| `CLOCK_InitUsb1Pfd` | INIT | True | Initializes the USB1 PLL PFD (Phase Fractional Divider) clock by configuring the PFD fractional value in hardware reg... |
| `CLOCK_InitUsb1Pll` | INIT | True | Initializes the USB1 PLL (Phase-Locked Loop) with specific configuration settings including clock source and divider ... |
| `CLOCK_InitUsb2Pll` | INIT | True | Initializes the USB2 PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider sele... |
| `CLOCK_InitVideoPll` | INIT | True | Initializes and configures the video PLL (Phase-Locked Loop) with specific divider, numerator, denominator, and sourc... |
| `CLOCK_SwitchOsc` | RETURNOK | False | Switches the oscillator source for the SoC between RC oscillator and crystal oscillator |
| `GPIO_PinInit` | INIT | True | Initializes a GPIO pin with specified configuration including direction, output logic, and interrupt mode |
| `GetUartSrcFreq` | INIT | True | Returns the clock source frequency for a UART peripheral based on its base address and system clock configuration |
| `LPUART_Deinit` | LOOP | True | Deinitializes an LPUART instance by waiting for transmit completion, clearing status flags, disabling the module, and... |
| `LPUART_Init` | INIT | True | Initializes an LPUART instance with user configuration including baud rate, parity, data bits, stop bits, FIFO settin... |
| `SystemCoreClockUpdate` | INIT | True | Updates the system core clock frequency by reading clock control module registers and calculating the current clock c... |
| `SystemInit` | CORE | False | System initialization function that configures core system registers including VTOR (vector table offset), FPU access... |
| `XBARA_Deinit` | INIT | True | Shuts down the XBARA module by disabling its clock |
| `XBARA_Init` | INIT | True | Initializes the XBARA (Crossbar A) module by enabling its clock |
| `XBARB_Deinit` | INIT | False | Deinitializes the XBARB (Crossbar B) peripheral by disabling its clock |
| `XBARB_Init` | SKIP | True | Initializes the XBARB (Crossbar B) module by enabling its clock gate |
| `imxrt_pin_mode` | INIT | True | Configures GPIO pin mode (input/output/pull-up/pull-down/open-drain) and IOMUX settings for i.MX RT processors |

## 附录：interesting MMIO expr 子集（共 11 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `BOARD_BootClockRUN`
- `CLOCK_InitArmPll`
- `CLOCK_InitAudioPll`
- `CLOCK_InitEnetPll`
- `CLOCK_InitExternalClk`
- `CLOCK_InitSysPll`
- `CLOCK_InitUsb1Pll`
- `CLOCK_InitUsb2Pll`
- `CLOCK_InitVideoPll`
- `CLOCK_SetDiv`
- `CLOCK_SetMux`
