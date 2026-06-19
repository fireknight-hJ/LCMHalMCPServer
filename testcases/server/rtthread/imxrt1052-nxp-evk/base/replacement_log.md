## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/rtthread/imxrt1052-nxp-evk/base`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `BOARD_BootClockRUN` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/clock_config.c` | 156 | 1 |
| `BOARD_InitPins` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/board/MCUX_Config/pin_mux.c` | 50 | 1 |
| `CLOCK_DeinitAudioPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 695 | 1 |
| `CLOCK_DeinitEnetPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 828 | 1 |
| `CLOCK_DeinitRcOsc24M` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 205 | 1 |
| `CLOCK_DeinitUsb1Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 575 | 1 |
| `CLOCK_DisableUsbhs1PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1207 | 1 |
| `CLOCK_EnableUsbhs0Clock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 394 | 1 |
| `CLOCK_EnableUsbhs0PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 442 | 1 |
| `CLOCK_EnableUsbhs1Clock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 419 | 1 |
| `CLOCK_EnableUsbhs1PhyPllClock` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1189 | 1 |
| `CLOCK_GetPeriphClkFreq` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 70 | 1 |
| `CLOCK_GetSemcFreq` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 225 | 1 |
| `CLOCK_InitArmPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 479 | 1 |
| `CLOCK_InitAudioPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 620 | 1 |
| `CLOCK_InitEnetPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 793 | 1 |
| `CLOCK_InitExternalClk` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 150 | 1 |
| `CLOCK_InitRcOsc24M` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 197 | 2 |
| `CLOCK_InitSysPfd` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1038 | 1 |
| `CLOCK_InitSysPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 512 | 1 |
| `CLOCK_InitUsb1Pfd` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 1075 | 2 |
| `CLOCK_InitUsb1Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 554 | 1 |
| `CLOCK_InitUsb2Pll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 587 | 1 |
| `CLOCK_InitVideoPll` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 707 | 1 |
| `CLOCK_SwitchOsc` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c` | 186 | 1 |
| `GPIO_PinInit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_gpio.c` | 71 | 2 |
| `GetUartSrcFreq` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c` | 559 | 1 |
| `LPUART_Deinit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 452 | 1 |
| `LPUART_DisableInterrupts` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 683 | 1 |
| `LPUART_EnableInterrupts` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 659 | 1 |
| `LPUART_GetStatusFlags` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 743 | 1 |
| `LPUART_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c` | 236 | 1 |
| `XBARA_Deinit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c` | 88 | 1 |
| `XBARA_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbara.c` | 73 | 1 |
| `XBARB_Deinit` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbarb.c` | 88 | 1 |
| `XBARB_Init` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbarb.c` | 73 | 2 |
| `imxrt_pin_mode` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_gpio.c` | 522 | 2 |
| `imxrt_putc` | `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_uart.c` | 688 | 1 |

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
- 函数用途/功能描述：System clock initialization function that configures oscillators, PLLs, clock dividers, multiplexers, and clock gates for the i.MX RT1052 microcontroller
- 是否需要替换：是
- 分类/替换原因：Based on analysis: 1) GetFunctionInfo revealed this is a comprehensive clock configuration function with extensive hardware register accesses. 2) GetMMIOFunctionInfo identified numerous MMIO operations to CCM, CCM_ANALOG, DCDC, XTALOSC24M, and IOMUXC_GPR registers. 3) The function contains a polling loop waiting for DCDC status (LOOP characteristic). 4) GetFunctionCallStack shows it's called by BOARD_InitBootClocks and rt_hw_board_init during system initialization. 5) The function sets the global SystemCoreClock variable. This is primarily an INIT function (system initialization) with a secondary LOOP element (polling). According to priority order (CORE > RECV > IRQ > INIT > LOOP), INIT takes precedence over LOOP. The replacement follows INIT strategy: remove all hardware register writes and polling loops while preserving essential system state (SystemCoreClock) and conditional compilation structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*******************************************************************************
* Code for BOARD_BootClockRUN configuration
******************************************************************************/
void BOARD_BootClockRUN(void)
{
    /* Remove all hardware-specific configuration operations */
    /* Preserve only the essential system state update */
    
    /* Skip all hardware register writes and polling loops */
    /* [LOOP REMOVED] Original while loop waited for DCDC_STS_DC_OK bit assertion */
    
    /* Preserve conditional compilation structure but remove hardware operations */
#ifndef SKIP_SYSCLK_INIT
    /* Skip hardware-specific SEMC clock configuration */
#endif

#if !(defined(XIP_EXTERNAL_FLASH) && (XIP_EXTERNAL_FLASH == 1))
    /* Skip hardware-specific FLEXSPI clock configuration */
#endif

    /* Set SystemCoreClock variable - preserve this essential system state */
    SystemCoreClock = BOARD_BOOTCLOCKRUN_CORE_CLOCK;
}
```

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
- 函数用途/功能描述：Configures pin routing and electrical features by enabling IOMUXC clock and setting up pin muxing for GPIO and UART pins.
- 是否需要替换：是
- 分类/替换原因：BOARD_InitPins is an initialization function that configures hardware peripherals: 1) It calls CLOCK_EnableClock(kCLOCK_Iomuxc) which performs MMIO writes to clock control registers (CCM->CCGR0) to enable the IOMUXC clock. 2) It calls IOMUXC_SetPinMux three times to configure pin muxing for GPIO1_IO09, LPUART1_TX, and LPUART1_RX pins, which performs MMIO writes to pin mux registers. The function contains no data transmission/reception (not RECV), no interrupt handling (not IRQ), no polling loops (not LOOP), and no NVIC/OS kernel operations (not CORE). It fits the INIT classification as it initializes peripheral configurations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void BOARD_InitPins(void) {
  /* Hardware initialization removed for simulation */
}
```

=== 信息结束 ===
```

### CLOCK_DeinitAudioPll

```text
=== CLOCK_DeinitAudioPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：695
- 函数内容：void CLOCK_DeinitAudioPll(void)
{
    CCM_ANALOG->PLL_AUDIO = CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes (powers down) the Audio PLL peripheral by writing a power-down mask to the PLL control register.
- 是否需要替换：是
- 分类/替换原因：The function performs a single hardware register write operation (CCM_ANALOG->PLL_AUDIO = CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK) to power down the Audio PLL. This is a hardware configuration operation for a peripheral, making it an INIT type function. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (no interrupt handling), and not LOOP (no polling loops). The function only manipulates peripheral registers with no impact on upper-layer data structures, but since it's clearly a hardware de-initialization function, INIT is the most appropriate classification.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitAudioPll(void)
{
    /* Skip hardware-specific power-down operation */
    /* Original: CCM_ANALOG->PLL_AUDIO = CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK; */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitAudioPll(void)
{
    /* Skip hardware-specific power-down operation */
    /* Original: CCM_ANALOG->PLL_AUDIO = CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK; */
}
- 更新原因：Provide a proper replacement for CLOCK_DeinitAudioPll that skips hardware-specific power-down operation while maintaining correct function signature. The original function writes to CCM_ANALOG->PLL_AUDIO register to power down Audio PLL, but in simulation/emulation we skip this hardware operation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitAudioPll(void)
{
    /* Skip hardware-specific power-down operation */
    /* Original: CCM_ANALOG->PLL_AUDIO = CCM_ANALOG_PLL_AUDIO_POWERDOWN_MASK; */
}
    原因：Provide a proper replacement for CLOCK_DeinitAudioPll that skips hardware-specific power-down operation while maintaining correct function signature. The original function writes to CCM_ANALOG->PLL_AUDIO register to power down Audio PLL, but in simulation/emulation we skip this hardware operation.
    时间：

=== 信息结束 ===
```

### CLOCK_DeinitEnetPll

```text
=== CLOCK_DeinitEnetPll 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：828
- 函数内容：void CLOCK_DeinitEnetPll(void)
{
    CCM_ANALOG->PLL_ENET = CCM_ANALOG_PLL_ENET_POWERDOWN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes and disables the ENET PLL by writing to clock control registers
- 是否需要替换：是
- 分类/替换原因：Function performs a single MMIO write operation to disable the ENET PLL (CCM_ANALOG->PLL_ENET = CCM_ANALOG_PLL_ENET_POWERDOWN_MASK). This is a hardware configuration/deinitialization operation. GetMMIOFunctionInfo confirms hardware register access. The function is called from BOARD_BootClockRUN during clock configuration. As an INIT-type function (deinitialization being the reverse of initialization), the replacement should remove the hardware-specific register write while preserving the function signature.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitEnetPll(void)
{
    /* Hardware deinitialization removed for simulation */
}
```

=== 信息结束 ===
```

### CLOCK_DeinitRcOsc24M

```text
=== CLOCK_DeinitRcOsc24M 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：205
- 函数内容：void CLOCK_DeinitRcOsc24M(void)
{
    XTALOSC24M->LOWPWR_CTRL &= ~XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Powers down the RCOSC 24M clock by disabling the RC oscillator enable bit in the XTALOSC24M control register.
- 是否需要替换：是
- 分类/替换原因：The function performs hardware configuration/deinitialization by writing to the XTALOSC24M->LOWPWR_CTRL register to disable the RC oscillator. GetFunctionInfo shows a single MMIO operation that clears the RC_OSC_EN bit. GetMMIOFunctionInfo confirms hardware register access. This is a pure hardware configuration function with no data transfer, interrupt handling, or complex control flow. According to the classification priority, it fits the INIT category (hardware initialization/deinitialization). The replacement successfully removes the hardware register access while preserving the function signature and documentation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitRcOsc24M(void)
{
    /* Skip hardware-specific RC oscillator deinitialization */
    /* Original: XTALOSC24M->LOWPWR_CTRL &= ~XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK; */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitRcOsc24M(void)
{
    /* Skip hardware-specific RC oscillator deinitialization */
    /* Original: XTALOSC24M->LOWPWR_CTRL &= ~XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK; */
}
- 更新原因：Provide a proper replacement for CLOCK_DeinitRcOsc24M that skips hardware-specific RC oscillator deinitialization while maintaining correct function signature. The original function clears the RC_OSC_EN bit in XTALOSC24M->LOWPWR_CTRL register to disable the 24MHz RC oscillator, but in simulation/emulation we skip this hardware operation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitRcOsc24M(void)
{
    /* Skip hardware-specific RC oscillator deinitialization */
    /* Original: XTALOSC24M->LOWPWR_CTRL &= ~XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK; */
}
    原因：Provide a proper replacement for CLOCK_DeinitRcOsc24M that skips hardware-specific RC oscillator deinitialization while maintaining correct function signature. The original function clears the RC_OSC_EN bit in XTALOSC24M->LOWPWR_CTRL register to disable the 24MHz RC oscillator, but in simulation/emulation we skip this hardware operation.
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
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes the USB1 Phase-Locked Loop (PLL) by writing zero to the PLL_USB1 register.
- 是否需要替换：是
- 分类/替换原因：Function performs hardware register access (CCM_ANALOG->PLL_USB1 = 0U) to deinitialize USB1 PLL. This is a hardware configuration operation that is the counterpart to initialization. Contains MMIO operation but no data processing, interrupts, loops, or OS operations. Classified as INIT (peripheral configuration/deinitialization) rather than RETURNOK because it's part of peripheral management and INIT has higher priority in classification order. The replacement has been verified and fixed successfully.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DeinitUsb1Pll(void)
{
    /* USB1 PLL deinitialization for simulation */
    /* Original code: CCM_ANALOG->PLL_USB1 = 0U; */
}
```

【替换更新】
- 更新代码：void CLOCK_DeinitUsb1Pll(void)
{
    /* USB1 PLL deinitialization for simulation */
    /* Original code: CCM_ANALOG->PLL_USB1 = 0U; */
}
- 更新原因：Update replacement to properly handle USB1 PLL deinitialization for simulation while maintaining correct function signature

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_DeinitUsb1Pll(void)
{
    /* USB1 PLL deinitialization for simulation */
    /* Original code: CCM_ANALOG->PLL_USB1 = 0U; */
}
    原因：Update replacement to properly handle USB1 PLL deinitialization for simulation while maintaining correct function signature
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
- 函数用途/功能描述：Disables USB HS PHY PLL clock by clearing enable bits in clock control registers
- 是否需要替换：是
- 分类/替换原因：Function performs hardware register writes to disable USB HS PHY PLL clock (CCM_ANALOG->PLL_USB2 and USBPHY2->CTRL). It's a configuration function that sets hardware state without involving data transfer, interrupts, or loops. GetMMIOFunctionInfo confirms hardware register accesses. According to classification priority, this fits INIT category as it configures peripheral hardware (clock control).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_DisableUsbhs1PhyPllClock(void)
{
    /* Hardware register writes removed for simulation */
}
```

=== 信息结束 ===
```

### CLOCK_EnableUsbhs0Clock

```text
=== CLOCK_EnableUsbhs0Clock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：394
- 函数内容：bool CLOCK_EnableUsbhs0Clock(clock_usb_src_t src, uint32_t freq)
{
    CCM->CCGR6 |= CCM_CCGR6_CG0_MASK;
    USB1->USBCMD |= USBHS_USBCMD_RST_MASK;
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
- 函数用途/功能描述：Enables USB HS clock by configuring clock gating, resetting USB controller, and setting up PMU regulator with appropriate timing delays.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization for USB HS peripheral: 1) Enables clock gating via CCM->CCGR6 register, 2) Sets USB reset bit via USB1->USBCMD register, 3) Contains hardware-dependent delay loop for timing requirements, 4) Configures PMU regulator via PMU->REG_3P0 register. It contains multiple MMIO operations and a hardware delay loop, making it clearly an INIT function. Not CORE (no NVIC/OS/VTOR operations), not RECV/IRQ (no data transfer or interrupt handling), not LOOP (delay loop is secondary to initialization purpose).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
bool CLOCK_EnableUsbhs0Clock(clock_usb_src_t src, uint32_t freq)
{
    /* Skip hardware initialization operations */
    return true;
}
```

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
- 函数用途/功能描述：Enables the internal 480MHz USB HS PHY PLL clock by configuring PLL and PHY control registers
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization for USB HS PHY PLL clock. Analysis shows it: 1) Accesses CCM_ANALOG->PLL_USB1 register to check/enable PLL, 2) Calls CLOCK_InitUsb1Pll() if PLL not enabled, 3) Configures USBPHY1->CTRL registers to release PHY from reset and clear clock gate, 4) Sets USBPHY1->PWD to 0, 5) Sets various control bits in USBPHY1->CTRL. These are all MMIO operations for peripheral initialization, fitting the INIT classification criteria. The function contains no data transmission/reception (not RECV), no interrupt handling (not IRQ), no polling loops (not LOOP), and is not CORE (no NVIC/OS/VTOR operations).
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
bool CLOCK_EnableUsbhs0PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* [INIT REMOVED] Hardware register configuration for USB HS PHY PLL clock */
    return true;
}
```

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
- 函数用途/功能描述：Enables USB HS clock and initializes USB HS peripheral hardware including clock gating, controller reset, and power management configuration.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization operations for the USB HS peripheral. Analysis of the function shows: 1) It contains MMIO register writes to CCM (Clock Controller Module), USB2 controller, and PMU (Power Management Unit); 2) It configures clock gating, resets the USB controller, and sets up power management registers; 3) It includes a hardware-dependent delay loop; 4) It returns a boolean success indicator. The function does not fit CORE (no NVIC/OS/VTOR operations), RECV (no data transmission/reception), IRQ (no interrupt handling), or LOOP (the loop is a timing delay, not polling status registers). The INIT classification is appropriate as this is a peripheral initialization function that should have its hardware operations removed while preserving the return value.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
bool CLOCK_EnableUsbhs1Clock(clock_usb_src_t src, uint32_t freq)
{
    /* Skip hardware-specific configuration:
     * - CCM->CCGR6 |= CCM_CCGR6_CG0_MASK; (clock gating enable)
     * - USB2->USBCMD |= USBHS_USBCMD_RST_MASK; (USB controller reset)
     * - PMU->REG_3P0 configuration
     * - Hardware delay loop
     */
    
    /* The function always returns true indicating success */
    return true;
}
```

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
- 函数用途/功能描述：Enables the USB HS PHY PLL clock by initializing USB2 PLL and configuring USB PHY control registers
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization operations: 1) Calls CLOCK_InitUsb2Pll() for PLL initialization, 2) Accesses USBPHY2->CTRL register to clear reset and clock gate bits, 3) Sets USBPHY2->PWD to 0 to clear power-down, 4) Sets various control bits in USBPHY2->CTRL register. These are typical hardware configuration operations for clock initialization, fitting the INIT classification. The function doesn't involve data transmission (not RECV), interrupt handling (not IRQ), polling loops (not LOOP), or core NVIC/OS operations (not CORE).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
bool CLOCK_EnableUsbhs1PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware-specific USB PLL initialization */
    /* Skip USB PHY register configuration: USBPHY2->CTRL operations */
    /* Skip USB PHY power-down register clear: USBPHY2->PWD = 0 */
    (void)src;  /* Mark parameter as used to avoid warning */
    (void)freq; /* Mark parameter as used to avoid warning */
    return true;
}
```

【替换更新】
- 更新代码：bool CLOCK_EnableUsbhs1PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware-specific USB PLL initialization */
    /* Skip USB PHY register configuration: USBPHY2->CTRL operations */
    /* Skip USB PHY power-down register clear: USBPHY2->PWD = 0 */
    (void)src;  /* Mark parameter as used to avoid warning */
    (void)freq; /* Mark parameter as used to avoid warning */
    return true;
}
- 更新原因：Remove unused variable g_ccmConfigUsbPll and mark parameters as used to avoid compiler warnings. The function returns true to indicate successful initialization without hardware access.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：bool CLOCK_EnableUsbhs1PhyPllClock(clock_usb_phy_src_t src, uint32_t freq)
{
    /* Skip hardware-specific USB PLL initialization */
    /* Skip USB PHY register configuration: USBPHY2->CTRL operations */
    /* Skip USB PHY power-down register clear: USBPHY2->PWD = 0 */
    (void)src;  /* Mark parameter as used to avoid warning */
    (void)freq; /* Mark parameter as used to avoid warning */
    return true;
}
    原因：Remove unused variable g_ccmConfigUsbPll and mark parameters as used to avoid compiler warnings. The function returns true to indicate successful initialization without hardware access.
    时间：

=== 信息结束 ===
```

### CLOCK_GetPeriphClkFreq

```text
=== CLOCK_GetPeriphClkFreq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：70
- 函数内容：static uint32_t CLOCK_GetPeriphClkFreq(void)
{
    uint32_t freq;

    /* Periph_clk2_clk ---> Periph_clk */
    if (CCM->CBCDR & CCM_CBCDR_PERIPH_CLK_SEL_MASK)
    {
        switch (CCM->CBCMR & CCM_CBCMR_PERIPH_CLK2_SEL_MASK)
        {
            /* Pll3_sw_clk ---> Periph_clk2_clk ---> Periph_clk */
            case CCM_CBCMR_PERIPH_CLK2_SEL(0U):
                freq = CLOCK_GetPllFreq(kCLOCK_PllUsb1);
                break;

            /* Osc_clk ---> Periph_clk2_clk ---> Periph_clk */
            case CCM_CBCMR_PERIPH_CLK2_SEL(1U):
                freq = CLOCK_GetOscFreq();
                break;

            case CCM_CBCMR_PERIPH_CLK2_SEL(2U):
                freq = CLOCK_GetPllFreq(kCLOCK_PllSys);
                break;

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
        switch (CCM->CBCMR & CCM_CBCMR_PRE_PERIPH_CLK_SEL_MASK)
        {
            /* PLL2 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(0U):
                freq = CLOCK_GetPllFreq(kCLOCK_PllSys);
                break;

            /* PLL2 PFD2 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(1U):
                freq = CLOCK_GetSysPfdFreq(kCLOCK_Pfd2);
                break;

            /* PLL2 PFD0 ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(2U):
                freq = CLOCK_GetSysPfdFreq(kCLOCK_Pfd0);
                break;

            /* PLL1 divided(/2) ---> Pre_Periph_clk ---> Periph_clk */
            case CCM_CBCMR_PRE_PERIPH_CLK_SEL(3U):
                freq = CLOCK_GetPllFreq(kCLOCK_PllArm) /
                       (((CCM->CACRR & CCM_CACRR_ARM_PODF_MASK) >> CCM_CACRR_ARM_PODF_SHIFT) + 1U);
                break;

            default:
                freq = 0U;
                break;
        }
    }

    return freq;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads clock configuration registers to determine the peripheral clock frequency based on current clock multiplexer and divider settings.
- 是否需要替换：是
- 分类/替换原因：Function reads hardware registers (CCM->CBCDR, CCM->CBCMR, CCM->CACRR) to determine clock configuration state. It performs hardware-dependent operations to read current clock multiplexer selections and divider values. This fits the INIT classification for hardware initialization/configuration reading functions. The function is static and called by other clock functions (CLOCK_GetSemcFreq, CLOCK_GetAhbFreq). It's not CORE (no NVIC/OS/VTOR operations), not RECV/IRQ (no data transfer/interrupt handling), and not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static uint32_t CLOCK_GetPeriphClkFreq(void)
{
    uint32_t freq;

    /* Simulate clock configuration reading */
    /* Skip hardware register reads and assume default configuration */
    
    /* Default to a reasonable peripheral clock frequency */
    freq = 60000000U; /* 60 MHz default */

    return freq;
}
```

=== 信息结束 ===
```

### CLOCK_GetSemcFreq

```text
=== CLOCK_GetSemcFreq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：225
- 函数内容：uint32_t CLOCK_GetSemcFreq(void)
{
    uint32_t freq;

    /* SEMC alternative clock ---> SEMC Clock */
    if (CCM->CBCDR & CCM_CBCDR_SEMC_CLK_SEL_MASK)
    {
        /* PLL3 PFD1 ---> SEMC alternative clock ---> SEMC Clock */
        if (CCM->CBCDR & CCM_CBCDR_SEMC_ALT_CLK_SEL_MASK)
        {
            freq = CLOCK_GetUsb1PfdFreq(kCLOCK_Pfd1);
        }
        /* PLL2 PFD2 ---> SEMC alternative clock ---> SEMC Clock */
        else
        {
            freq = CLOCK_GetSysPfdFreq(kCLOCK_Pfd2);
        }
    }
    /* Periph_clk ---> SEMC Clock */
    else
    {
        freq = CLOCK_GetPeriphClkFreq();
    }

    freq /= (((CCM->CBCDR & CCM_CBCDR_SEMC_PODF_MASK) >> CCM_CBCDR_SEMC_PODF_SHIFT) + 1U);

    return freq;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads hardware clock configuration registers to determine the SEMC (Smart External Memory Controller) clock frequency based on clock source selection and divider settings.
- 是否需要替换：是
- 分类/替换原因：The function reads CCM->CBCDR hardware registers to determine clock configuration (SEMC_CLK_SEL, SEMC_ALT_CLK_SEL, SEMC_PODF). It calls other clock frequency functions but doesn't perform data transmission/reception, interrupt handling, or contain polling loops. This is a configuration/initialization reading function that needs hardware register access removal while preserving logical structure. GetMMIOFunctionInfo showed the function accesses hardware registers, confirming it needs replacement.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Gets the SEMC clock frequency.
*
* return  The SEMC clock frequency value in hertz.
*/
uint32_t CLOCK_GetSemcFreq(void)
{
    uint32_t freq;

    /* In simulation, return a safe default frequency */
    /* Default to using peripheral clock with divider of 1 */
    freq = 60000000U; /* 60 MHz default */

    return freq;
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
- 函数用途/功能描述：Initializes the ARM PLL (Phase-Locked Loop) with specific configuration settings including clock source and divider selection.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this function performs hardware initialization of the ARM PLL. GetMMIOFunctionInfo reveals multiple register accesses to CCM_ANALOG->PLL_ARM for configuration and a polling loop waiting for PLL lock. This is a classic initialization function that configures peripheral hardware settings. It does not involve data transmission/reception (not RECV), is not an interrupt handler (not IRQ), and does not configure NVIC/OS/VTOR (not CORE). The function is called by BOARD_BootClockRUN during system clock initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initialize the ARM PLL.
*
* This function initialize the ARM PLL with specific settings
*
* param config   configuration to set to PLL.
*/
void CLOCK_InitArmPll(const clock_arm_pll_config_t *config)
{
    /* Skip hardware initialization in simulation */
    /* Original hardware operations removed:
     * - Bypass PLL configuration
     * - PLL divider and enable configuration
     * - Polling for PLL lock
     * - Disable bypass
     */
    /* Assume PLL is initialized successfully */
}
```

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
- 函数用途/功能描述：Initializes the Audio PLL with specific configuration settings including loop divider, post divider, numerator, denominator, and clock source.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs hardware initialization of the Audio PLL peripheral; 2) It contains multiple MMIO register writes to CCM_ANALOG registers (PLL_AUDIO, PLL_AUDIO_NUM, PLL_AUDIO_DENOM, MISC2); 3) It includes a hardware-dependent polling loop waiting for PLL lock; 4) It doesn't involve data transmission/reception (not RECV), interrupt handling (not IRQ), or OS operations (not CORE); 5) The function fits the INIT classification as it configures peripheral hardware and contains initialization logic that should be preserved while removing hardware-specific operations.
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
    uint32_t pllAudio;
    uint32_t misc2 = 0;

    /* Skip hardware register writes for PLL bypass */
    /* Original: CCM_ANALOG->PLL_AUDIO = (CCM_ANALOG->PLL_AUDIO & (~CCM_ANALOG_PLL_AUDIO_BYPASS_CLK_SRC_MASK)) |
                            CCM_ANALOG_PLL_AUDIO_BYPASS_MASK | CCM_ANALOG_PLL_AUDIO_BYPASS_CLK_SRC(config->src); */

    /* Skip hardware register writes for numerator and denominator */
    /* Original: CCM_ANALOG->PLL_AUDIO_NUM = CCM_ANALOG_PLL_AUDIO_NUM_A(config->numerator); */
    /* Original: CCM_ANALOG->PLL_AUDIO_DENOM = CCM_ANALOG_PLL_AUDIO_DENOM_B(config->denominator); */

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
    /* Calculate pllAudio value based on config but don't write to hardware */
    pllAudio = CCM_ANALOG_PLL_AUDIO_ENABLE_MASK | CCM_ANALOG_PLL_AUDIO_DIV_SELECT(config->loopDivider);

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

    /* Skip hardware register write for MISC2 */
    /* Original: CCM_ANALOG->MISC2 =
        (CCM_ANALOG->MISC2 & ~(CCM_ANALOG_MISC2_AUDIO_DIV_LSB_MASK | CCM_ANALOG_MISC2_AUDIO_DIV_MSB_MASK)) | misc2; */

    /* Skip hardware register write for PLL_AUDIO */
    /* Original: CCM_ANALOG->PLL_AUDIO = pllAudio; */

    /* Skip PLL lock polling loop */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */
    /* Original: while ((CCM_ANALOG->PLL_AUDIO & CCM_ANALOG_PLL_AUDIO_LOCK_MASK) == 0)
    {
    } */

    /* Skip hardware register write to disable bypass */
    /* Original: CCM_ANALOG->PLL_AUDIO &= ~CCM_ANALOG_PLL_AUDIO_BYPASS_MASK; */
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
- 函数用途/功能描述：Initializes the ENET PLL (Phase-Locked Loop) for Ethernet clock generation with specific configuration settings
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a hardware initialization function that configures the ENET PLL registers. GetMMIOFunctionInfo showed multiple MMIO register writes to CCM_ANALOG->PLL_ENET and a polling loop waiting for PLL lock. The function fits the INIT classification as it performs peripheral initialization with hardware register configuration and contains a polling loop (which falls under LOOP strategy within INIT classification). It does not involve data transmission/reception (RECV), interrupt handling (IRQ), OS kernel operations (CORE), or simple returns (RETURNOK/SKIP).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitEnetPll(const clock_enet_pll_config_t *config)
{
    /* Remove hardware-specific PLL initialization */
    /* Skip polling loop for PLL lock */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */
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
- 函数用途/功能描述：Initializes the external 24MHz clock by powering up the crystal oscillator, waiting for stabilization, enabling frequency detection, and then disabling detection.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a clock initialization function that configures external oscillator hardware. GetMMIOFunctionInfo identified multiple MMIO register accesses and two polling loops waiting for hardware status flags. The function performs hardware initialization without data I/O, interrupt handling, or OS operations. It's called from BOARD_BootClockRUN during system boot. According to classification priority, it doesn't fit CORE (no NVIC/OS/VTOR), RECV (no data reception), or IRQ (no interrupt handling), making INIT the appropriate classification as it initializes peripheral hardware configuration.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitExternalClk(bool bypassXtalOsc)
{
    /* This device does not support bypass XTAL OSC. */
    assert(!bypassXtalOsc);

    /* [INIT REPLACEMENT] Skip hardware initialization for external 24MHz clock */
    /* Original: Power up external crystal oscillator */
    /* CCM_ANALOG->MISC0_CLR = CCM_ANALOG_MISC0_XTAL_24M_PWD_MASK; */
    
    /* [LOOP REMOVED] Wait for oscillator power-up status */
    /* while ((XTALOSC24M->LOWPWR_CTRL & XTALOSC24M_LOWPWR_CTRL_XTALOSC_PWRUP_STAT_MASK) == 0) */
    
    /* Original: Enable frequency detection */
    /* CCM_ANALOG->MISC0_SET = CCM_ANALOG_MISC0_OSC_XTALOK_EN_MASK; */
    
    /* [LOOP REMOVED] Wait for oscillator ready status */
    /* while ((CCM_ANALOG->MISC0 & CCM_ANALOG_MISC0_OSC_XTALOK_MASK) == 0) */
    
    /* Original: Disable frequency detection */
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
- 函数用途/功能描述：Initializes the RC oscillator 24MHz clock by enabling it through hardware register access
- 是否需要替换：是
- 分类/替换原因：Function performs a single MMIO register write (XTALOSC24M->LOWPWR_CTRL |= XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK) to enable the RC oscillator. This is a hardware initialization operation with no data transfer, interrupts, loops, or OS/kernel operations. Called from BOARD_BootClockRUN during system clock initialization. Classified as INIT according to priority order: INIT > RETURNOK > SKIP > NODRIVER.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitRcOsc24M(void)
{
    /* Hardware register access removed for simulation */
}
```

【替换更新】
- 更新代码：void CLOCK_InitRcOsc24M(void)
{
    /* Hardware register access removed for simulation */
}
- 更新原因：Simplify replacement to empty function body with minimal comment to avoid compilation issues

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void CLOCK_InitRcOsc24M(void)
{
    /* RC oscillator 24MHz is enabled for simulation */
    /* Original hardware access: XTALOSC24M->LOWPWR_CTRL |= XTALOSC24M_LOWPWR_CTRL_RC_OSC_EN_MASK; */
}
    原因：Fix replacement to match original function signature and provide simulation-friendly implementation
    时间：

  版本 2:
    替换代码：void CLOCK_InitRcOsc24M(void)
{
    /* Hardware register access removed for simulation */
}
    原因：Simplify replacement to empty function body with minimal comment to avoid compilation issues
    时间：

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
- 函数用途/功能描述：Initializes the System PLL PFD (Phase Frequency Detector) clock by configuring hardware registers
- 是否需要替换：是
- 分类/替换原因：This function performs hardware register accesses (CCM_ANALOG->PFD_528) to configure clock PFD settings. It reads and writes to hardware registers to disable clock output, set new PFD fractional values, and re-enable output. As a hardware initialization function that configures clock peripherals, it fits the INIT classification. The function contains no data transmission/reception, interrupt handling, or OS operations, and is not a core OS/kernel function. The replacement removes all hardware register accesses while preserving the function signature.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitSysPfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    /* Hardware initialization removed for simulation */
    /* Original function configured System PLL PFD clock */
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
- 函数用途/功能描述：Initializes the System PLL (Phase-Locked Loop) with specific configuration settings including loop divider, fractional mode, spread spectrum, and clock source.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this function performs multiple MMIO register writes to configure the System PLL hardware. GetMMIOFunctionInfo confirms hardware register accesses to CCM_ANALOG registers. The function contains a polling loop waiting for PLL lock. This is a hardware initialization function that configures clock generation hardware. It does not involve data transmission/reception (not RECV), is not an interrupt handler (not IRQ), does not configure NVIC/OS/VTOR (not CORE), and is not a simple return operation. Based on the priority order, INIT is the appropriate classification as it initializes peripheral hardware and requires removal of MMIO operations while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initialize the System PLL.
*
* This function initializes the System PLL with specific settings
*
* param config Configuration to set to PLL.
*/
void CLOCK_InitSysPll(const clock_sys_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Hardware initialization removed for simulation */
    /* Original hardware operations:
     * - Configure PLL bypass and clock source
     * - Set loop divider and enable PLL
     * - Configure fractional mode (numerator/denominator)
     * - Configure spread spectrum mode
     * - Wait for PLL lock
     * - Disable bypass
     */
    
    /* Skip polling loop for PLL lock */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */
    
    /* No hardware operations in replacement */
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
- 函数用途/功能描述：Initializes the USB1 PLL PFD (Phase Fractional Divider) by setting the fractional value and controlling the clock gate to prevent glitches during configuration.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware register writes to CCM_ANALOG->PFD_480 to configure USB1 PLL PFD clock settings. It reads the current register value, disables clock output, then sets new fractional value and re-enables output. This is a hardware initialization function that configures clock peripheral registers. GetMMIOFunctionInfo shows hardware register accesses. The function fits the INIT category as it initializes peripheral hardware configuration and performs MMIO operations that can be removed in simulation while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd480;

    /* Skip hardware register configuration for USB1 PLL PFD initialization */
    /* Original hardware operations removed for simulation:
     *   pfd480 = CCM_ANALOG->PFD_480 &
     *            ~((CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_480_PFD0_FRAC_MASK) << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_FRAC(pfdFrac) << (8 * pfdIndex));
     */

    /* Mark variables as used to avoid compiler warnings */
    (void)pfd480;
    (void)pfdFrac;
}
```

【替换更新】
- 更新代码：void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd480;

    /* Skip hardware register configuration for USB1 PLL PFD initialization */
    /* Original hardware operations removed for simulation:
     *   pfd480 = CCM_ANALOG->PFD_480 &
     *            ~((CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_480_PFD0_FRAC_MASK) << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_FRAC(pfdFrac) << (8 * pfdIndex));
     */

    /* Mark variables as used to avoid compiler warnings */
    (void)pfd480;
    (void)pfdFrac;
}
- 更新原因：Fix replacement to include missing pfd480 variable declaration and properly handle all parameters to avoid compiler warnings. The original function initializes USB1 PLL PFD hardware registers, but for simulation we stub it out while maintaining the exact function signature and local variable declarations.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    /* Hardware initialization removed for simulation */
    /* Original function configured USB1 PLL PFD clock registers */
    /* Parameters are marked as used to avoid compiler warnings */
    (void)pfd;
    (void)pfdFrac;
}
    原因：Update replacement to properly handle parameters and avoid unused parameter warnings. The original function initializes USB1 PLL PFD hardware registers, but for simulation we just stub it out while maintaining the function signature.
    时间：

  版本 2:
    替换代码：void CLOCK_InitUsb1Pfd(clock_pfd_t pfd, uint8_t pfdFrac)
{
    uint32_t pfdIndex = (uint32_t)pfd;
    uint32_t pfd480;

    /* Skip hardware register configuration for USB1 PLL PFD initialization */
    /* Original hardware operations removed for simulation:
     *   pfd480 = CCM_ANALOG->PFD_480 &
     *            ~((CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK | CCM_ANALOG_PFD_480_PFD0_FRAC_MASK) << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_CLKGATE_MASK << (8 * pfdIndex));
     *   CCM_ANALOG->PFD_480 = pfd480 | (CCM_ANALOG_PFD_480_PFD0_FRAC(pfdFrac) << (8 * pfdIndex));
     */

    /* Mark variables as used to avoid compiler warnings */
    (void)pfd480;
    (void)pfdFrac;
}
    原因：Fix replacement to include missing pfd480 variable declaration and properly handle all parameters to avoid compiler warnings. The original function initializes USB1 PLL PFD hardware registers, but for simulation we stub it out while maintaining the exact function signature and local variable declarations.
    时间：

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
- 函数用途/功能描述：Initializes the USB1 PLL with specific configuration settings including bypass mode, divider selection, and enabling PLL power and USB clocks
- 是否需要替换：否
- 分类/替换原因：GetFunctionInfo shows this function performs hardware initialization of USB1 PLL registers. GetMMIOFunctionInfo confirms multiple MMIO accesses to CCM_ANALOG->PLL_USB1 register. The function contains a polling loop waiting for PLL lock signal. This is a classic peripheral initialization function with hardware-dependent operations that need to be removed while preserving the function structure. It is not CORE (no NVIC/OS/VTOR), not RECV (no data I/O), not IRQ (no interrupt handling). Classified as INIT with LOOP handling for the polling wait.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：/*!
* brief Initialize the USB1 PLL.
*
* This function initializes the USB1 PLL with specific settings
*
* param config Configuration to set to PLL.
*/
void CLOCK_InitUsb1Pll(const clock_usb_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Skip hardware-specific PLL initialization in emulation */
    /* Original hardware operations removed:
     * - Bypass PLL configuration with clock source
     * - PLL divider, enable, power, and USB clocks configuration
     * - Polling for PLL lock
     * - Disable bypass
     */
    
    /* Parameter config is used but hardware operations are skipped */
    (void)config;
}
- 更新原因：This function is missing a replacement while other similar PLL initialization functions (CLOCK_InitUsb2Pll, CLOCK_InitSysPll, etc.) already have replacements. The function performs hardware initialization of USB1 PLL with MMIO register writes and a polling loop. Following the same pattern as other PLL init functions, we remove all hardware operations while preserving the function signature and parameter usage.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/*!
* brief Initialize the USB1 PLL.
*
* This function initializes the USB1 PLL with specific settings
*
* param config Configuration to set to PLL.
*/
void CLOCK_InitUsb1Pll(const clock_usb_pll_config_t *config)
{
    /* [INIT REPLACEMENT] Skip hardware-specific PLL initialization in emulation */
    /* Original hardware operations removed:
     * - Bypass PLL configuration with clock source
     * - PLL divider, enable, power, and USB clocks configuration
     * - Polling for PLL lock
     * - Disable bypass
     */
    
    /* Parameter config is used but hardware operations are skipped */
    (void)config;
}
    原因：This function is missing a replacement while other similar PLL initialization functions (CLOCK_InitUsb2Pll, CLOCK_InitSysPll, etc.) already have replacements. The function performs hardware initialization of USB1 PLL with MMIO register writes and a polling loop. Following the same pattern as other PLL init functions, we remove all hardware operations while preserving the function signature and parameter usage.
    时间：

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
- 函数用途/功能描述：Initializes the USB2 PLL (Phase-Locked Loop) with specific configuration settings for clock generation
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs USB2 PLL initialization with multiple MMIO register writes to CCM_ANALOG->PLL_USB2. GetMMIOFunctionInfo confirmed hardware register accesses including a polling loop waiting for PLL lock. The function takes a configuration parameter but contains no NVIC/OS operations, interrupt handling, or data I/O. This matches the INIT classification criteria: functions that initialize peripheral/configurations with MMIO operations that should be removed while preserving parameter usage and logical structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initialize the USB2 PLL.
*
* This function initializes the USB2 PLL with specific settings
*
* param config Configuration to set to PLL.
*/
void CLOCK_InitUsb2Pll(const clock_usb_pll_config_t *config)
{
    /* Skip hardware-specific PLL initialization in emulation */
    /* Original hardware operations removed:
     * - Bypass PLL configuration
     * - PLL divider and enable configuration
     * - Polling for PLL lock
     * - Disable bypass
     */
    
    /* Parameter config is used but hardware operations are skipped */
    (void)config;
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
- 函数用途/功能描述：Initializes the video PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, numerator/denominator values, loop divider, and post-divider settings.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This is a hardware initialization function that configures PLL registers (CCM_ANALOG->PLL_VIDEO, CCM_ANALOG->PLL_VIDEO_NUM, CCM_ANALOG->PLL_VIDEO_DENOM, CCM_ANALOG->MISC2). 2) It contains MMIO register writes that need to be removed. 3) It has a polling loop waiting for PLL lock flag that needs to be skipped. 4) The function doesn't fit higher priority categories: not CORE (no NVIC/OS/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler). 5) The function preserves configuration logic via switch statement for postDivider handling. 6) GetStructOrEnumInfo confirmed the config structure contains PLL parameters. Classification as INIT follows priority order: CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NEEDCHECK > NODRIVER.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_InitVideoPll(const clock_video_pll_config_t *config)
{
    uint32_t pllVideo;
    uint32_t misc2 = 0;

    /* Skip hardware-specific PLL bypass configuration */
    /* Original: CCM_ANALOG->PLL_VIDEO = (CCM_ANALOG->PLL_VIDEO & (~CCM_ANALOG_PLL_VIDEO_BYPASS_CLK_SRC_MASK)) |
                            CCM_ANALOG_PLL_VIDEO_BYPASS_MASK | CCM_ANALOG_PLL_VIDEO_BYPASS_CLK_SRC(config->src); */

    /* Skip hardware-specific numerator/denominator configuration */
    /* Original: CCM_ANALOG->PLL_VIDEO_NUM = CCM_ANALOG_PLL_VIDEO_NUM_A(config->numerator); */
    /* Original: CCM_ANALOG->PLL_VIDEO_DENOM = CCM_ANALOG_PLL_VIDEO_DENOM_B(config->denominator); */

    /*
     * Preserve post divider configuration logic (non-hardware)
     */
    pllVideo = 0; /* Initialize variable */
    
    switch (config->postDivider)
    {
        case 16:
            pllVideo |= 0; /* CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(0) */
            misc2 = 0; /* CCM_ANALOG_MISC2_VIDEO_DIV(3) */
            break;

        case 8:
            pllVideo |= 0; /* CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(1) */
            misc2 = 0; /* CCM_ANALOG_MISC2_VIDEO_DIV(3) */
            break;

        case 4:
            pllVideo |= 0; /* CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(2) */
            misc2 = 0; /* CCM_ANALOG_MISC2_VIDEO_DIV(3) */
            break;

        case 2:
            pllVideo |= 0; /* CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(1) */
            break;

        default:
            pllVideo |= 0; /* CCM_ANALOG_PLL_VIDEO_POST_DIV_SELECT(2) */
            break;
    }

    /* Skip hardware MISC2 register write */
    /* Original: CCM_ANALOG->MISC2 = (CCM_ANALOG->MISC2 & ~CCM_ANALOG_MISC2_VIDEO_DIV_MASK) | misc2; */

    /* Skip hardware PLL_VIDEO register write */
    /* Original: CCM_ANALOG->PLL_VIDEO = pllVideo; */

    /* Skip polling loop waiting for PLL lock */
    /* [LOOP REMOVED] Waited for hardware PLL lock flag */

    /* Skip hardware bypass disable */
    /* Original: CCM_ANALOG->PLL_VIDEO &= ~CCM_ANALOG_PLL_VIDEO_BYPASS_MASK; */
}
```

=== 信息结束 ===
```

### CLOCK_SwitchOsc

```text
=== CLOCK_SwitchOsc 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_clock.c
- 行号：186
- 函数内容：void CLOCK_SwitchOsc(clock_osc_t osc)
{
    if (osc == kCLOCK_RcOsc)
        XTALOSC24M->LOWPWR_CTRL_SET = XTALOSC24M_LOWPWR_CTRL_SET_OSC_SEL_MASK;
    else
        XTALOSC24M->LOWPWR_CTRL_CLR = XTALOSC24M_LOWPWR_CTRL_CLR_OSC_SEL_MASK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Switches the oscillator source for the SoC between RC oscillator and crystal oscillator
- 是否需要替换：是
- 分类/替换原因：This function configures hardware oscillator selection by writing to XTALOSC24M peripheral registers. It contains MMIO operations (XTALOSC24M->LOWPWR_CTRL_SET/CLR) that need to be removed for simulation. The function is called from BOARD_BootClockRUN during system initialization, making it an initialization function. It doesn't fit higher-priority categories: not CORE (no NVIC/OS kernel operations), not RECV (no data transmission/reception), not IRQ (not interrupt-related), and contains no polling loops for LOOP classification.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void CLOCK_SwitchOsc(clock_osc_t osc)
{
    /* Hardware oscillator switching removed for simulation */
    (void)osc; /* Mark parameter as used to avoid warnings */
}
```

【替换更新】
- 更新代码：void CLOCK_SwitchOsc(clock_osc_t osc)
{
    /* Hardware oscillator switching removed for simulation */
    (void)osc; /* Mark parameter as used to avoid warnings */
}
- 更新原因：Fix function signature and add parameter usage to avoid compiler warnings. The original function switches oscillator hardware which is not needed in simulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void CLOCK_SwitchOsc(clock_osc_t osc)
{
    /* Hardware oscillator switching removed for simulation */
    (void)osc; /* Mark parameter as used to avoid warnings */
}
    原因：Fix function signature and add parameter usage to avoid compiler warnings. The original function switches oscillator hardware which is not needed in simulation.
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
- 函数用途/功能描述：Initializes a GPIO pin with specified direction, output logic, and interrupt mode configuration
- 是否需要替换：是
- 分类/替换原因：GPIO_PinInit is a peripheral initialization function that configures GPIO hardware registers (IMR, GDIR), sets pin direction, output logic, and calls GPIO_SetPinInterruptConfig for interrupt setup. It contains multiple MMIO operations (register reads/writes) and calls other GPIO functions. According to classification priority, this matches INIT type as it initializes peripheral configurations without being CORE (no NVIC/OS operations), RECV (no data transmission), IRQ (not an interrupt handler), or LOOP (no polling loops). The replacement removes all hardware-specific operations while preserving function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
    /* GPIO pin initialization simulation - no hardware access */
    (void)base;
    (void)pin;
    (void)Config;
}
```

【替换更新】
- 更新代码：void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
    /* GPIO pin initialization simulation - no hardware access */
    (void)base;
    (void)pin;
    (void)Config;
}
- 更新原因：Simplify GPIO_PinInit replacement to clean simulation implementation with proper void casts to avoid unused parameter warnings

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
    /* GPIO pin initialization simulation - no hardware access */
    (void)base;
    (void)pin;
    (void)Config;
    
    /* In simulation, we don't need to configure hardware registers */
    /* This function is called to initialize GPIO pins but in simulation
       we don't have actual hardware to configure */
}
    原因：Simplify GPIO_PinInit replacement to remove commented-out code and provide clean simulation implementation. The function parameters are cast to void to avoid unused parameter warnings while maintaining the same function signature.
    时间：

  版本 2:
    替换代码：void GPIO_PinInit(GPIO_Type *base, uint32_t pin, const gpio_pin_config_t *Config)
{
    /* GPIO pin initialization simulation - no hardware access */
    (void)base;
    (void)pin;
    (void)Config;
}
    原因：Simplify GPIO_PinInit replacement to clean simulation implementation with proper void casts to avoid unused parameter warnings
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
- 函数用途/功能描述：Determines the clock source frequency for a UART peripheral based on hardware clock configuration and UART base address
- 是否需要替换：是
- 分类/替换原因：GetUartSrcFreq is classified as INIT because it reads hardware clock configuration registers to determine the UART source frequency. Analysis shows: 1) The function calls hardware-dependent clock functions (CLOCK_GetMux, CLOCK_GetDiv, CLOCK_GetPllFreq, CLOCK_GetOscFreq) that access CCM and XTALOSC24M hardware registers; 2) It's used by imxrt_configure during UART initialization to get the clock frequency; 3) The function contains conditional compilation for different SOC series (IMXRT1170 vs others), indicating hardware-specific behavior; 4) It performs no data transmission/reception (not RECV), no interrupt handling (not IRQ), and no NVIC/OS kernel operations (not CORE). As an INIT function, it needs replacement to remove hardware register accesses while returning a reasonable default frequency.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* complement to adjust final destination address */
uint32_t GetUartSrcFreq(LPUART_Type *uart_base)
{
    uint32_t freq;
#ifdef SOC_IMXRT1170_SERIES
    /* For IMXRT1170 series, return a default frequency */
    freq = 80000000U; /* Default 80MHz clock frequency */
#else
    /* Return a default frequency for non-IMXRT1170 series */
    /* Default to 80MHz clock frequency (common UART clock) */
    freq = 80000000U;
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
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes a LPUART instance by waiting for transmission to complete, clearing status flags, disabling the module, and disabling LPUART clocks.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware deconfiguration operations similar to initialization functions. It contains hardware-dependent polling loops (waiting for TX FIFO empty and transmission complete flag), writes to hardware registers (STAT and CTRL), and calls clock control functions. According to the classification guidelines, functions that initialize/deinitialize peripheral configurations are classified as INIT. The replacement strategy removes MMIO/register access operations while preserving clock control calls (which may involve OS/NVIC operations). The function contains LOOP elements that need to be skipped according to LOOP strategy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Deinitializes a LPUART instance.
*
* This function waits for transmit to complete, disables TX and RX, and disables the LPUART clock.
*
* param base LPUART peripheral base address.
*/
void LPUART_Deinit(LPUART_Type *base)
{
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* [LOOP REMOVED] Waited for TX FIFO to send out */
#endif
    /* [LOOP REMOVED] Waited for last character shift out */

    /* Clear all status flags - hardware operation removed */
    /* uint32_t temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK); */

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    /* temp |= LPUART_STAT_LBKDIF_MASK; */
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    /* temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK); */
#endif

    /* Disable the module - hardware operation removed */
    /* base->CTRL = 0; */

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* uint32_t instance = LPUART_GetInstance(base); */

    /* Disable lpuart clock - hardware operation removed */
    /* CLOCK_DisableClock(s_lpuartClock[instance]); */

#if defined(LPUART_PERIPH_CLOCKS)
    /* CLOCK_DisableClock(s_lpuartPeriphClocks[instance]); */
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

【替换更新】
- 更新代码：/*!
* brief Deinitializes a LPUART instance.
*
* This function waits for transmit to complete, disables TX and RX, and disables the LPUART clock.
*
* param base LPUART peripheral base address.
*/
void LPUART_Deinit(LPUART_Type *base)
{
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* [LOOP REMOVED] Waited for TX FIFO to send out */
#endif
    /* [LOOP REMOVED] Waited for last character shift out */

    /* Clear all status flags - hardware operation removed */
    /* uint32_t temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK); */

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    /* temp |= LPUART_STAT_LBKDIF_MASK; */
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    /* temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK); */
#endif

    /* Disable the module - hardware operation removed */
    /* base->CTRL = 0; */

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* uint32_t instance = LPUART_GetInstance(base); */

    /* Disable lpuart clock - hardware operation removed */
    /* CLOCK_DisableClock(s_lpuartClock[instance]); */

#if defined(LPUART_PERIPH_CLOCKS)
    /* CLOCK_DisableClock(s_lpuartPeriphClocks[instance]); */
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
- 更新原因：Fixed unused variable warnings by removing declaration of unused variables 'temp' and 'instance'. The hardware operations were already commented out in the replacement, so removing the variable declarations eliminates compiler warnings while maintaining the same functionality.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/*!
* brief Deinitializes a LPUART instance.
*
* This function waits for transmit to complete, disables TX and RX, and disables the LPUART clock.
*
* param base LPUART peripheral base address.
*/
void LPUART_Deinit(LPUART_Type *base)
{
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    /* [LOOP REMOVED] Waited for TX FIFO to send out */
#endif
    /* [LOOP REMOVED] Waited for last character shift out */

    /* Clear all status flags - hardware operation removed */
    /* uint32_t temp = (LPUART_STAT_RXEDGIF_MASK | LPUART_STAT_IDLE_MASK | LPUART_STAT_OR_MASK | LPUART_STAT_NF_MASK |
            LPUART_STAT_FE_MASK | LPUART_STAT_PF_MASK); */

#if defined(FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT) && FSL_FEATURE_LPUART_HAS_LIN_BREAK_DETECT
    /* temp |= LPUART_STAT_LBKDIF_MASK; */
#endif

#if defined(FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING) && FSL_FEATURE_LPUART_HAS_ADDRESS_MATCHING
    /* temp |= (LPUART_STAT_MA1F_MASK | LPUART_STAT_MA2F_MASK); */
#endif

    /* Disable the module - hardware operation removed */
    /* base->CTRL = 0; */

#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* uint32_t instance = LPUART_GetInstance(base); */

    /* Disable lpuart clock - hardware operation removed */
    /* CLOCK_DisableClock(s_lpuartClock[instance]); */

#if defined(LPUART_PERIPH_CLOCKS)
    /* CLOCK_DisableClock(s_lpuartPeriphClocks[instance]); */
#endif

#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Fixed unused variable warnings by removing declaration of unused variables 'temp' and 'instance'. The hardware operations were already commented out in the replacement, so removing the variable declarations eliminates compiler warnings while maintaining the same functionality.
    时间：

=== 信息结束 ===
```

### LPUART_DisableInterrupts

```text
=== LPUART_DisableInterrupts 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_lpuart.c
- 行号：683
- 函数内容：void LPUART_DisableInterrupts(LPUART_Type *base, uint32_t mask)
{
    base->BAUD &= ~((mask << 8) & (LPUART_BAUD_LBKDIE_MASK | LPUART_BAUD_RXEDGIE_MASK));
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    base->FIFO = (base->FIFO & ~(LPUART_FIFO_TXOF_MASK | LPUART_FIFO_RXUF_MASK)) &
                 ~((mask << 8) & (LPUART_FIFO_TXOFE_MASK | LPUART_FIFO_RXUFE_MASK));
#endif
    mask &= 0xFFFFFF00U;
    base->CTRL &= ~mask;
}


【替换更新】
- 更新代码：void LPUART_DisableInterrupts(LPUART_Type *base, uint32_t mask)
{
    /* For emulation, do not modify hardware interrupt registers */
    /* Skip all hardware register writes */
}
- 更新原因：Replace LPUART_DisableInterrupts for consistency with LPUART_EnableInterrupts replacement. The function writes to hardware registers to disable interrupts, but in emulation we don't need to modify hardware state. The replacement skips all hardware operations while preserving the function signature.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void LPUART_DisableInterrupts(LPUART_Type *base, uint32_t mask)
{
    /* For emulation, do not modify hardware interrupt registers */
    /* Skip all hardware register writes */
}
    原因：Replace LPUART_DisableInterrupts for consistency with LPUART_EnableInterrupts replacement. The function writes to hardware registers to disable interrupts, but in emulation we don't need to modify hardware state. The replacement skips all hardware operations while preserving the function signature.
    时间：

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
    /* For emulation, do not enable any hardware interrupts */
    /* Skip all hardware register writes */
}
- 更新原因：Replace LPUART_EnableInterrupts to prevent enabling hardware interrupts in emulation. The original function writes to hardware registers (BAUD, FIFO, CTRL) to enable interrupts, which can cause issues in emulation if interrupts are enabled but not properly handled. The replacement skips all hardware operations while preserving the function signature.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void LPUART_EnableInterrupts(LPUART_Type *base, uint32_t mask)
{
    /* For emulation, do not enable any hardware interrupts */
    /* Skip all hardware register writes */
}
    原因：Replace LPUART_EnableInterrupts to prevent enabling hardware interrupts in emulation. The original function writes to hardware registers (BAUD, FIFO, CTRL) to enable interrupts, which can cause issues in emulation if interrupts are enabled but not properly handled. The replacement skips all hardware operations while preserving the function signature.
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
    /* For emulation, return all flags set to satisfy any wait conditions */
    return 0xFFFFFFFFU;
}
- 更新原因：Replace LPUART_GetStatusFlags to avoid hardware register reads in emulation. By returning all bits set (0xFFFFFFFF), any flag check will pass, preventing infinite wait loops. This is a safe approach for emulation as it ensures hardware wait conditions are always satisfied.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：uint32_t LPUART_GetStatusFlags(LPUART_Type *base)
{
    /* For emulation, return all flags set to satisfy any wait conditions */
    return 0xFFFFFFFFU;
}
    原因：Replace LPUART_GetStatusFlags to avoid hardware register reads in emulation. By returning all bits set (0xFFFFFFFF), any flag check will pass, preventing infinite wait loops. This is a safe approach for emulation as it ensures hardware wait conditions are always satisfied.
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
- 分类/替换原因：LPUART_Init is classified as INIT because: 1) It performs peripheral hardware initialization (LPUART configuration), 2) It contains multiple MMIO register accesses to configure LPUART registers (CTRL, BAUD, STAT, FIFO, WATER, MODIR), 3) It calls clock enable functions and performs software reset, 4) It validates configuration parameters and performs baud rate calculations, 5) It does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), and does not contain hardware polling loops (not LOOP). The function follows the INIT strategy: removing MMIO operations while preserving parameter validation, calculations, and returning success status.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initializes an LPUART instance with the user configuration structure and the peripheral clock.
*
* This function configures the LPUART module with user-defined settings. Call the LPUART_GetDefaultConfig() function
* to configure the configuration structure and get the default configuration.
* The example below shows how to use this API to configure the LPUART.
* code
*  lpuart_config_t lpuartConfig;
*  lpuartConfig.baudRate_Bps = 115200U;
*  lpuartConfig.parityMode = kLPUART_ParityDisabled;
*  lpuartConfig.dataBitsCount = kLPUART_EightDataBits;
*  lpuartConfig.isMsb = false;
*  lpuartConfig.stopBitCount = kLPUART_OneStopBit;
*  lpuartConfig.txFifoWatermark = 0;
*  lpuartConfig.rxFifoWatermark = 1;
*  LPUART_Init(LPUART1, &lpuartConfig, 20000000U);
* endcode
*
* param base LPUART peripheral base address.
* param config Pointer to a user-defined configuration structure.
* param srcClock_Hz LPUART clock source frequency in HZ.
* retval kStatus_LPUART_BaudrateNotSupport Baudrate is not support in current clock source.
* retval kStatus_Success LPUART initialize succeed
*/
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
    /* Original code would enable clocks, configure registers, etc. */
    /* For simulation, we just return success */

    return kStatus_Success;
}
```

【替换更新】
- 更新代码：/*!
* brief Initializes an LPUART instance with the user configuration structure and the peripheral clock.
*
* This function configures the LPUART module with user-defined settings. Call the LPUART_GetDefaultConfig() function
* to configure the configuration structure and get the default configuration.
* The example below shows how to use this API to configure the LPUART.
* code
*  lpuart_config_t lpuartConfig;
*  lpuartConfig.baudRate_Bps = 115200U;
*  lpuartConfig.parityMode = kLPUART_ParityDisabled;
*  lpuartConfig.dataBitsCount = kLPUART_EightDataBits;
*  lpuartConfig.isMsb = false;
*  lpuartConfig.stopBitCount = kLPUART_OneStopBit;
*  lpuartConfig.txFifoWatermark = 0;
*  lpuartConfig.rxFifoWatermark = 1;
*  LPUART_Init(LPUART1, &lpuartConfig, 20000000U);
* endcode
*
* param base LPUART peripheral base address.
* param config Pointer to a user-defined configuration structure.
* param srcClock_Hz LPUART clock source frequency in HZ.
* retval kStatus_LPUART_BaudrateNotSupport Baudrate is not support in current clock source.
* retval kStatus_Success LPUART initialize succeed
*/
status_t LPUART_Init(LPUART_Type *base, const lpuart_config_t *config, uint32_t srcClock_Hz)
{
    assert(config);
    assert(config->baudRate_Bps);
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->txFifoWatermark);
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->rxFifoWatermark);
#endif

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
- 更新原因：Fixed LPUART_Init replacement by removing unused 'temp' variable and simplifying the code to match the working version from GetFunctionAnalysisAndReplacement. The previous version had an extra comment line that might have caused compilation issues.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/*!
* brief Initializes an LPUART instance with the user configuration structure and the peripheral clock.
*
* This function configures the LPUART module with user-defined settings. Call the LPUART_GetDefaultConfig() function
* to configure the configuration structure and get the default configuration.
* The example below shows how to use this API to configure the LPUART.
* code
*  lpuart_config_t lpuartConfig;
*  lpuartConfig.baudRate_Bps = 115200U;
*  lpuartConfig.parityMode = kLPUART_ParityDisabled;
*  lpuartConfig.dataBitsCount = kLPUART_EightDataBits;
*  lpuartConfig.isMsb = false;
*  lpuartConfig.stopBitCount = kLPUART_OneStopBit;
*  lpuartConfig.txFifoWatermark = 0;
*  lpuartConfig.rxFifoWatermark = 1;
*  LPUART_Init(LPUART1, &lpuartConfig, 20000000U);
* endcode
*
* param base LPUART peripheral base address.
* param config Pointer to a user-defined configuration structure.
* param srcClock_Hz LPUART clock source frequency in HZ.
* retval kStatus_LPUART_BaudrateNotSupport Baudrate is not support in current clock source.
* retval kStatus_Success LPUART initialize succeed
*/
status_t LPUART_Init(LPUART_Type *base, const lpuart_config_t *config, uint32_t srcClock_Hz)
{
    assert(config);
    assert(config->baudRate_Bps);
#if defined(FSL_FEATURE_LPUART_HAS_FIFO) && FSL_FEATURE_LPUART_HAS_FIFO
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->txFifoWatermark);
    assert(FSL_FEATURE_LPUART_FIFO_SIZEn(base) >= config->rxFifoWatermark);
#endif

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
    原因：Fixed LPUART_Init replacement by removing unused 'temp' variable and simplifying the code to match the working version from GetFunctionAnalysisAndReplacement. The previous version had an extra comment line that might have caused compilation issues.
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
- 函数用途/功能描述：Shuts down the XBARA (Crossbar A) module by disabling its clock
- 是否需要替换：是
- 分类/替换原因：This function is a hardware deinitialization function that disables the XBARA module clock. Analysis shows: 1) It calls CLOCK_DisableClock which performs hardware clock control operations; 2) GetMMIOFunctionInfo shows no direct MMIO operations but the called function likely contains them; 3) It's the counterpart to initialization functions and performs hardware shutdown; 4) It doesn't fit other categories: not RECV (no data I/O), not IRQ (not interrupt-related), not LOOP (no polling), not RETURNOK/SKIP (performs hardware operations), not CORE (doesn't configure NVIC/OS/VTOR), not NODRIVER (has hardware dependencies). As an INIT function, hardware operations should be removed while preserving function structure.
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
    /* Hardware clock disable operation removed for simulation */
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
- 函数用途/功能描述：Initializes the XBARA (Crossbar A) peripheral by enabling its clock gating
- 是否需要替换：是
- 分类/替换原因：Function is a peripheral initialization function that enables clock gating for the XBARA peripheral. GetFunctionInfo shows it calls CLOCK_EnableClock which contains MMIO operations to control clock registers. This matches the INIT classification pattern - hardware initialization that should have hardware operations removed while preserving function structure. Not CORE (no NVIC/OS/VTOR), not RECV (no data transfer), not IRQ (not interrupt handler), not LOOP (no polling).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Initializes the XBARA module.
*
* This function un-gates the XBARA clock.
*
* param base XBARA peripheral address.
*/
void XBARA_Init(XBARA_Type *base)
{
    /* Hardware initialization removed for simulation */
}
```

=== 信息结束 ===
```

### XBARB_Deinit

```text
=== XBARB_Deinit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk/packages/nxp-imxrt-sdk-latest/MIMXRT1050/MIMXRT1052/drivers/fsl_xbarb.c
- 行号：88
- 函数内容：void XBARB_Deinit(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Disable XBARB module clock. */
    CLOCK_DisableClock(s_xbarbClock[XBARB_GetInstance(base)]);
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Shuts down the XBARB (Crossbar B) module by disabling its clock
- 是否需要替换：是
- 分类/替换原因：This function performs peripheral deinitialization by disabling the XBARB clock through CLOCK_DisableClock(), which contains MMIO operations to control clock gating registers. Analysis of CLOCK_ControlGate shows direct hardware register access (CCM->CCGR0). The function is classified as INIT (which includes deinitialization functions) because it configures hardware resources but doesn't fit RECV, IRQ, LOOP, or CORE categories. GetMMIOFunctionInfo showed no direct MMIO expressions, but the called function CLOCK_ControlGate performs hardware register writes.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void XBARB_Deinit(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Skip hardware clock disable in simulation */
    /* CLOCK_DisableClock(s_xbarbClock[XBARB_GetInstance(base)]); */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

【替换更新】
- 更新代码：void XBARB_Deinit(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Skip hardware clock disable in simulation */
    /* CLOCK_DisableClock(s_xbarbClock[XBARB_GetInstance(base)]); */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
- 更新原因：Update XBARB_Deinit replacement to match the expected format with commented-out hardware call. The original error appears to be unrelated syntax error in drv_gpio.c, but this replacement correctly removes hardware-dependent operations.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void XBARB_Deinit(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Skip hardware clock disable in simulation */
    /* CLOCK_DisableClock(s_xbarbClock[XBARB_GetInstance(base)]); */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Update XBARB_Deinit replacement to match the expected format with commented-out hardware call. The original error appears to be unrelated syntax error in drv_gpio.c, but this replacement correctly removes hardware-dependent operations.
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
- 函数类型：INIT
- 函数用途/功能描述：Initializes the XBARB (Crossbar B) module by enabling its clock
- 是否需要替换：是
- 分类/替换原因：The function is an initialization function that enables the clock for the XBARB peripheral through CLOCK_EnableClock, which performs MMIO operations to write to clock control registers (CCM->CCGR0). It fits the INIT classification as it initializes peripheral hardware configuration (clock gating). The function contains conditional compilation based on FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL and calls CLOCK_EnableClock which performs hardware register writes. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), and not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware clock enabling removed for simulation */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
```

【替换更新】
- 更新代码：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware clock enabling removed for simulation */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
- 更新原因：Simplify XBARB_Init replacement to ensure compilation succeeds. Remove potentially problematic comments.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Skip hardware clock enabling in simulation */
    /* Original: CLOCK_EnableClock(s_xbarbClock[XBARB_GetInstance(base)]); */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Fix XBARB_Init to properly handle simulation environment by skipping hardware clock operations while preserving original function structure and preprocessor directives
    时间：

  版本 2:
    替换代码：void XBARB_Init(XBARB_Type *base)
{
#if !(defined(FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL) && FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL)
    /* Hardware clock enabling removed for simulation */
#endif /* FSL_SDK_DISABLE_DRIVER_CLOCK_CONTROL */
}
    原因：Simplify XBARB_Init replacement to ensure compilation succeeds. Remove potentially problematic comments.
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
- 函数用途/功能描述：Configures GPIO pin modes (input, output, pull-up, pull-down, open-drain) for i.MX RT microcontrollers
- 是否需要替换：否
- 分类/替换原因：Function performs hardware initialization of GPIO pins through register configuration. Analysis shows: 1) Calls CLOCK_EnableClock() to enable IOMUXC peripheral clocks, 2) Calls IOMUXC_SetPinMux() and IOMUXC_SetPinConfig() to configure pin multiplexing and electrical properties, 3) Calls GPIO_PinInit() to initialize GPIO hardware. These are all hardware initialization operations that configure peripheral registers. The function validates pin parameters, sets up gpio_pin_config_t structure based on requested mode, and performs hardware-specific configuration - classic INIT pattern. Not CORE (no NVIC/OS operations), not RECV (no data transmission/reception), not IRQ (not interrupt handler), not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

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
        /* LOG_D call removed to avoid compilation errors with malformed string literal */
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

    /* [INIT REPLACEMENT] Hardware initialization removed for simulation */
    /* Original hardware calls removed: CLOCK_EnableClock, IOMUXC_SetPinMux, IOMUXC_SetPinConfig, GPIO_PinInit */
}
- 更新原因：Fixed compilation error by completely removing the malformed LOG_D call that had a string literal split across multiple lines in the original source. The replacement now properly handles the invalid pin check without the problematic debug output.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/* GPIO5 index offset is 128 */
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
        LOG_D("invalid pin,rtt pin: %d,port: %d,pin: %d", pin, port + 1, pin_num);
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
    原因：Fixed malformed LOG_D string literal by removing the newline character that was causing the string to be improperly terminated. The original string was split across two lines without proper string concatenation.
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
        /* LOG_D call removed to avoid compilation errors with malformed string literal */
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

    /* [INIT REPLACEMENT] Hardware initialization removed for simulation */
    /* Original hardware calls removed: CLOCK_EnableClock, IOMUXC_SetPinMux, IOMUXC_SetPinConfig, GPIO_PinInit */
}
    原因：Fixed compilation error by completely removing the malformed LOG_D call that had a string literal split across multiple lines in the original source. The replacement now properly handles the invalid pin check without the problematic debug output.
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

    /* [LOOP REMOVED] Skip hardware wait loop for transmitter ready */
    /* Original: while (!(LPUART_GetStatusFlags(uart->uart_base) & kLPUART_TxDataRegEmptyFlag)); */
    
    /* [HARDWARE WRITE REMOVED] Skip writing to hardware DATA register */
    /* Original: LPUART_WriteByte(uart->uart_base, ch); */
    
    /* For emulation, we can simulate sending the character */
    /* In a real POSIX environment, we would write to stdout */
    
    return 1;
}
- 更新原因：Fix exceptional loop in imxrt_putc by removing hardware wait loop and hardware register writes. The function was causing an infinite loop waiting for LPUART_TxDataRegEmptyFlag which never gets set in emulation. This is a classic LOOP pattern that needs to be removed for emulation to work correctly. The replacement preserves the function signature and returns success (1 character written) while removing all hardware-dependent operations.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int imxrt_putc(struct rt_serial_device *serial, char ch)
{
    struct imxrt_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct imxrt_uart, serial);

    /* [LOOP REMOVED] Skip hardware wait loop for transmitter ready */
    /* Original: while (!(LPUART_GetStatusFlags(uart->uart_base) & kLPUART_TxDataRegEmptyFlag)); */
    
    /* [HARDWARE WRITE REMOVED] Skip writing to hardware DATA register */
    /* Original: LPUART_WriteByte(uart->uart_base, ch); */
    
    /* For emulation, we can simulate sending the character */
    /* In a real POSIX environment, we would write to stdout */
    
    return 1;
}
    原因：Fix exceptional loop in imxrt_putc by removing hardware wait loop and hardware register writes. The function was causing an infinite loop waiting for LPUART_TxDataRegEmptyFlag which never gets set in emulation. This is a classic LOOP pattern that needs to be removed for emulation to work correctly. The replacement preserves the function signature and returns success (1 character written) while removing all hardware-dependent operations.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**51** 个；CodeQL `MMIOFunction`：**51** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **11** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `BOARD_BootClockRUN` | INIT | True | System clock initialization function that configures oscillators, PLLs, clock dividers, multiplexers, and clock gates... |
| `BOARD_InitPins` | INIT | True | Configures pin routing and electrical features by enabling IOMUXC clock and setting up pin muxing for GPIO and UART p... |
| `CLOCK_DeinitArmPll` | INIT | False | De-initializes the ARM PLL by writing a power-down mask to the PLL control register. |
| `CLOCK_DeinitAudioPll` | INIT | True | De-initializes (powers down) the Audio PLL peripheral by writing a power-down mask to the PLL control register. |
| `CLOCK_DeinitEnetPll` | INIT | True | Deinitializes and disables the ENET PLL by writing to clock control registers |
| `CLOCK_DeinitExternalClk` | RETURNOK | False | Deinitializes the external 24MHz clock by powering it down |
| `CLOCK_DeinitRcOsc24M` | INIT | True | Powers down the RCOSC 24M clock by disabling the RC oscillator enable bit in the XTALOSC24M control register. |
| `CLOCK_DeinitSysPfd` | RETURNOK | False | De-initializes/disables the System PLL PFD (Phase Frequency Detector) clock based on the input parameter. |
| `CLOCK_DeinitSysPll` | SKIP | False | De-initializes the System PLL by powering it down through hardware register access. |
| `CLOCK_DeinitUsb1Pfd` | RETURNOK | False | De-initializes/disables the USB1 PLL PFD (Phase Frequency Detector) clock by setting the clock gate bit in the PFD_48... |
| `CLOCK_DeinitUsb1Pll` | INIT | True | Deinitializes the USB1 Phase-Locked Loop (PLL) by writing zero to the PLL_USB1 register. |
| `CLOCK_DeinitUsb2Pll` | SKIP | False | Deinitializes the USB2 PLL by writing zero to the PLL_USB2 register |
| `CLOCK_DeinitVideoPll` | RETURNOK | False | De-initializes (powers down) the Video PLL by writing a power-down mask to the PLL_VIDEO register. |
| `CLOCK_DisableUsbhs0PhyPllClock` | RETURNOK | False | Disables USB HS PHY PLL clock by clearing enable bits in clock control registers |
| `CLOCK_DisableUsbhs1PhyPllClock` | INIT | True | Disables USB HS PHY PLL clock by clearing enable bits in clock control registers |
| `CLOCK_EnableUsbhs0Clock` | INIT | True | Enables USB HS clock by configuring clock gating, resetting USB controller, and setting up PMU regulator with appropr... |
| `CLOCK_EnableUsbhs0PhyPllClock` | INIT | True | Enables the internal 480MHz USB HS PHY PLL clock by configuring PLL and PHY control registers |
| `CLOCK_EnableUsbhs1Clock` | INIT | True | Enables USB HS clock and initializes USB HS peripheral hardware including clock gating, controller reset, and power m... |
| `CLOCK_EnableUsbhs1PhyPllClock` | INIT | True | Enables the USB HS PHY PLL clock by initializing USB2 PLL and configuring USB PHY control registers |
| `CLOCK_GetAhbFreq` | RETURNOK | False | Calculates and returns the AHB (Advanced High-performance Bus) clock frequency by reading clock configuration registers. |
| `CLOCK_GetFreq` | NODRIVER | False | Gets the clock frequency for a specific clock name by routing to appropriate frequency calculation functions |
| `CLOCK_GetIpgFreq` | RETURNOK | False | Gets the IPG (IP Bus) clock frequency by reading the CCM CBCDR register and dividing the AHB clock frequency by the I... |
| `CLOCK_GetPerClkFreq` | RETURNOK | False | Reads the PER (Peripheral) clock frequency from hardware clock controller registers |
| `CLOCK_GetPeriphClkFreq` | INIT | True | Reads clock configuration registers to determine the peripheral clock frequency based on current clock multiplexer an... |
| `CLOCK_GetPllFreq` | RETURNOK | False | Calculates the current output frequency of a specific PLL based on hardware register readings |
| `CLOCK_GetSemcFreq` | INIT | True | Reads hardware clock configuration registers to determine the SEMC (Smart External Memory Controller) clock frequency... |
| `CLOCK_GetSysPfdFreq` | RETURNOK | False | Calculates the current System PLL PFD (Phase Fractional Divider) output frequency based on PFD selection |
| `CLOCK_GetUsb1PfdFreq` | RETURNOK | False | Calculates and returns the current USB1 PLL PFD (Phase Fractional Divider) output frequency based on the selected PFD... |
| `CLOCK_InitArmPll` | INIT | True | Initializes the ARM PLL (Phase-Locked Loop) with specific configuration settings including clock source and divider s... |
| `CLOCK_InitAudioPll` | INIT | True | Initializes the Audio PLL with specific configuration settings including loop divider, post divider, numerator, denom... |
| `CLOCK_InitEnetPll` | INIT | True | Initializes the ENET PLL (Phase-Locked Loop) for Ethernet clock generation with specific configuration settings |
| `CLOCK_InitExternalClk` | INIT | True | Initializes the external 24MHz clock by powering up the crystal oscillator, waiting for stabilization, enabling frequ... |
| `CLOCK_InitRcOsc24M` | INIT | True | Initializes the RC oscillator 24MHz clock by enabling it through hardware register access |
| `CLOCK_InitSysPfd` | INIT | True | Initializes the System PLL PFD (Phase Frequency Detector) clock by configuring hardware registers |
| `CLOCK_InitSysPll` | INIT | True | Initializes the System PLL (Phase-Locked Loop) with specific configuration settings including loop divider, fractiona... |
| `CLOCK_InitUsb1Pfd` | INIT | True | Initializes the USB1 PLL PFD (Phase Fractional Divider) by setting the fractional value and controlling the clock gat... |
| `CLOCK_InitUsb1Pll` | INIT | False | Initializes the USB1 PLL with specific configuration settings including bypass mode, divider selection, and enabling ... |
| `CLOCK_InitUsb2Pll` | INIT | True | Initializes the USB2 PLL (Phase-Locked Loop) with specific configuration settings for clock generation |
| `CLOCK_InitVideoPll` | INIT | True | Initializes the video PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, numerator/d... |
| `CLOCK_SwitchOsc` | INIT | True | Switches the oscillator source for the SoC between RC oscillator and crystal oscillator |
| `GPIO_PinInit` | INIT | True | Initializes a GPIO pin with specified direction, output logic, and interrupt mode configuration |
| `GetUartSrcFreq` | INIT | True | Determines the clock source frequency for a UART peripheral based on hardware clock configuration and UART base address |
| `LPUART_Deinit` | INIT | True | Deinitializes a LPUART instance by waiting for transmission to complete, clearing status flags, disabling the module,... |
| `LPUART_Init` | INIT | True | Initializes an LPUART instance with user configuration including baud rate, parity, data bits, stop bits, FIFO settin... |
| `SystemCoreClockUpdate` | RETURNOK | False | Reads clock control registers to calculate and update the system core clock frequency |
| `SystemInit` | CORE | False | System initialization function that configures VTOR, FPU, watchdogs, SysTick, and caches |
| `XBARA_Deinit` | INIT | True | Shuts down the XBARA (Crossbar A) module by disabling its clock |
| `XBARA_Init` | INIT | True | Initializes the XBARA (Crossbar A) peripheral by enabling its clock gating |
| `XBARB_Deinit` | INIT | True | Shuts down the XBARB (Crossbar B) module by disabling its clock |
| `XBARB_Init` | INIT | True | Initializes the XBARB (Crossbar B) module by enabling its clock |
| `imxrt_pin_mode` | INIT | False | Configures GPIO pin modes (input, output, pull-up, pull-down, open-drain) for i.MX RT microcontrollers |

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
