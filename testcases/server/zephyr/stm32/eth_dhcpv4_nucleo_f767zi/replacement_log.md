## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/stm32/eth_dhcpv4_nucleo_f767zi`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `HAL_RCCEx_GetPeriphCLKConfig` | `/home/haojie/zephyrproject/modules/hal/stm32/stm32cube/stm32f7xx/drivers/src/stm32f7xx_hal_rcc_ex.c` | 665 | 1 |
| `config_enable_default_clocks` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32f2_f4_f7.c` | 122 | 1 |
| `config_pll_sysclock` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32f2_f4_f7.c` | 57 | 1 |
| `eth_stm32_hal_set_config` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_stm32_hal.c` | 1582 | 1 |
| `eth_tx` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_stm32_hal.c` | 326 | 1 |
| `gpio_stm32_configure_raw` | `/home/haojie/zephyrproject/zephyr/drivers/gpio/gpio_stm32.c` | 157 | 1 |
| `gpio_stm32_port_get_raw` | `/home/haojie/zephyrproject/zephyr/drivers/gpio/gpio_stm32.c` | 399 | 1 |
| `set_up_fixed_clock_sources` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c` | 547 | 1 |
| `set_up_plls` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c` | 478 | 1 |
| `st_stm32f7_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/st_stm32/stm32f7/soc.c` | 28 | 1 |
| `stm32_clock_control_init` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c` | 719 | 1 |
| `stm32_clock_switch_to_hsi` | `/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c` | 460 | 1 |
| `stm32_exti_isr` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_exti_stm32.c` | 170 | 1 |
| `stm32_exti_trigger` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_exti_stm32.c` | 130 | 1 |
| `z_add_timeout` | `/home/haojie/zephyrproject/zephyr/kernel/timeout.c` | 99 | 1 |

## 2. 各函数替换详情

### HAL_RCCEx_GetPeriphCLKConfig

```text
=== HAL_RCCEx_GetPeriphCLKConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/modules/hal/stm32/stm32cube/stm32f7xx/drivers/src/stm32f7xx_hal_rcc_ex.c
- 行号：665
- 函数内容：void HAL_RCCEx_GetPeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tempreg = 0;

  /* Set all possible values for the extended clock type parameter------------*/
#if defined (STM32F765xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx)
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S      | RCC_PERIPHCLK_LPTIM1   |\
                                        RCC_PERIPHCLK_SAI1     | RCC_PERIPHCLK_SAI2     |\
                                        RCC_PERIPHCLK_TIM      | RCC_PERIPHCLK_RTC      |\
                                        RCC_PERIPHCLK_CEC      | RCC_PERIPHCLK_I2C4     |\
                                        RCC_PERIPHCLK_I2C1     | RCC_PERIPHCLK_I2C2     |\
                                        RCC_PERIPHCLK_I2C3     | RCC_PERIPHCLK_USART1   |\
                                        RCC_PERIPHCLK_USART2   | RCC_PERIPHCLK_USART3   |\
                                        RCC_PERIPHCLK_UART4    | RCC_PERIPHCLK_UART5    |\
                                        RCC_PERIPHCLK_USART6   | RCC_PERIPHCLK_UART7    |\
                                        RCC_PERIPHCLK_UART8    | RCC_PERIPHCLK_SDMMC1   |\
                                        RCC_PERIPHCLK_CLK48    | RCC_PERIPHCLK_SDMMC2   |\
                                        RCC_PERIPHCLK_DFSDM1   | RCC_PERIPHCLK_DFSDM1_AUDIO;
#else
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S      | RCC_PERIPHCLK_LPTIM1   |\
                                        RCC_PERIPHCLK_SAI1     | RCC_PERIPHCLK_SAI2     |\
                                        RCC_PERIPHCLK_TIM      | RCC_PERIPHCLK_RTC      |\
                                        RCC_PERIPHCLK_CEC      | RCC_PERIPHCLK_I2C4     |\
                                        RCC_PERIPHCLK_I2C1     | RCC_PERIPHCLK_I2C2     |\
                                        RCC_PERIPHCLK_I2C3     | RCC_PERIPHCLK_USART1   |\
                                        RCC_PERIPHCLK_USART2   | RCC_PERIPHCLK_USART3   |\
                                        RCC_PERIPHCLK_UART4    | RCC_PERIPHCLK_UART5    |\
                                        RCC_PERIPHCLK_USART6   | RCC_PERIPHCLK_UART7    |\
                                        RCC_PERIPHCLK_UART8    | RCC_PERIPHCLK_SDMMC1   |\
                                        RCC_PERIPHCLK_CLK48;
#endif /* STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx */

  /* Get the PLLI2S Clock configuration -----------------------------------------------*/
  PeriphClkInit->PLLI2S.PLLI2SN = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SN) >> RCC_PLLI2SCFGR_PLLI2SN_Pos);
  PeriphClkInit->PLLI2S.PLLI2SP = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SP) >> RCC_PLLI2SCFGR_PLLI2SP_Pos);
  PeriphClkInit->PLLI2S.PLLI2SQ = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SQ) >> RCC_PLLI2SCFGR_PLLI2SQ_Pos);
  PeriphClkInit->PLLI2S.PLLI2SR = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SR) >> RCC_PLLI2SCFGR_PLLI2SR_Pos);

  /* Get the PLLSAI Clock configuration -----------------------------------------------*/
  PeriphClkInit->PLLSAI.PLLSAIN = (uint32_t)((RCC->PLLSAICFGR & RCC_PLLSAICFGR_PLLSAIN) >> RCC_PLLSAICFGR_PLLSAIN_Pos);
  PeriphClkInit->PLLSAI.PLLSAIP = (uint32_t)((RCC->PLLSAICFGR & RCC_PLLSAICFGR_PLLSAIP) >> RCC_PLLSAICFGR_PLLSAIP_Pos);
  PeriphClkInit->PLLSAI.PLLSAIQ = (uint32_t)((RCC->PLLSAICFGR & RCC_PLLSAICFGR_PLLSAIQ) >> RCC_PLLSAICFGR_PLLSAIQ_Pos);
  PeriphClkInit->PLLSAI.PLLSAIR = (uint32_t)((RCC->PLLSAICFGR & RCC_PLLSAICFGR_PLLSAIR) >> RCC_PLLSAICFGR_PLLSAIR_Pos);

  /* Get the PLLSAI/PLLI2S division factors -------------------------------------------*/
  PeriphClkInit->PLLI2SDivQ = (uint32_t)((RCC->DCKCFGR1 & RCC_DCKCFGR1_PLLI2SDIVQ) >> RCC_DCKCFGR1_PLLI2SDIVQ_Pos);
  PeriphClkInit->PLLSAIDivQ = (uint32_t)((RCC->DCKCFGR1 & RCC_DCKCFGR1_PLLSAIDIVQ) >> RCC_DCKCFGR1_PLLSAIDIVQ_Pos);
  PeriphClkInit->PLLSAIDivR = (uint32_t)((RCC->DCKCFGR1 & RCC_DCKCFGR1_PLLSAIDIVR) >> RCC_DCKCFGR1_PLLSAIDIVR_Pos);

  /* Get the SAI1 clock configuration ----------------------------------------------*/
  PeriphClkInit->Sai1ClockSelection = __HAL_RCC_GET_SAI1_SOURCE();

  /* Get the SAI2 clock configuration ----------------------------------------------*/
  PeriphClkInit->Sai2ClockSelection = __HAL_RCC_GET_SAI2_SOURCE();

  /* Get the I2S clock configuration ------------------------------------------*/
  PeriphClkInit->I2sClockSelection = __HAL_RCC_GET_I2SCLKSOURCE();

  /* Get the I2C1 clock configuration ------------------------------------------*/
  PeriphClkInit->I2c1ClockSelection = __HAL_RCC_GET_I2C1_SOURCE();

  /* Get the I2C2 clock configuration ------------------------------------------*/
  PeriphClkInit->I2c2ClockSelection = __HAL_RCC_GET_I2C2_SOURCE();

  /* Get the I2C3 clock configuration ------------------------------------------*/
  PeriphClkInit->I2c3ClockSelection = __HAL_RCC_GET_I2C3_SOURCE();

  /* Get the I2C4 clock configuration ------------------------------------------*/
  PeriphClkInit->I2c4ClockSelection = __HAL_RCC_GET_I2C4_SOURCE();

  /* Get the USART1 clock configuration ------------------------------------------*/
  PeriphClkInit->Usart1ClockSelection = __HAL_RCC_GET_USART1_SOURCE();

  /* Get the USART2 clock configuration ------------------------------------------*/
  PeriphClkInit->Usart2ClockSelection = __HAL_RCC_GET_USART2_SOURCE();

  /* Get the USART3 clock configuration ------------------------------------------*/
  PeriphClkInit->Usart3ClockSelection = __HAL_RCC_GET_USART3_SOURCE();

  /* Get the UART4 clock configuration ------------------------------------------*/
  PeriphClkInit->Uart4ClockSelection = __HAL_RCC_GET_UART4_SOURCE();

  /* Get the UART5 clock configuration ------------------------------------------*/
  PeriphClkInit->Uart5ClockSelection = __HAL_RCC_GET_UART5_SOURCE();

  /* Get the USART6 clock configuration ------------------------------------------*/
  PeriphClkInit->Usart6ClockSelection = __HAL_RCC_GET_USART6_SOURCE();

  /* Get the UART7 clock configuration ------------------------------------------*/
  PeriphClkInit->Uart7ClockSelection = __HAL_RCC_GET_UART7_SOURCE();

  /* Get the UART8 clock configuration ------------------------------------------*/
  PeriphClkInit->Uart8ClockSelection = __HAL_RCC_GET_UART8_SOURCE();

  /* Get the LPTIM1 clock configuration ------------------------------------------*/
  PeriphClkInit->Lptim1ClockSelection = __HAL_RCC_GET_LPTIM1_SOURCE();

  /* Get the CEC clock configuration -----------------------------------------------*/
  PeriphClkInit->CecClockSelection = __HAL_RCC_GET_CEC_SOURCE();

  /* Get the CK48 clock configuration -----------------------------------------------*/
  PeriphClkInit->Clk48ClockSelection = __HAL_RCC_GET_CLK48_SOURCE();

  /* Get the SDMMC1 clock configuration -----------------------------------------------*/
  PeriphClkInit->Sdmmc1ClockSelection = __HAL_RCC_GET_SDMMC1_SOURCE();

#if defined (STM32F765xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx)
  /* Get the SDMMC2 clock configuration -----------------------------------------------*/
  PeriphClkInit->Sdmmc2ClockSelection = __HAL_RCC_GET_SDMMC2_SOURCE();

  /* Get the DFSDM clock configuration -----------------------------------------------*/
  PeriphClkInit->Dfsdm1ClockSelection = __HAL_RCC_GET_DFSDM1_SOURCE();

  /* Get the DFSDM AUDIO clock configuration -----------------------------------------------*/
  PeriphClkInit->Dfsdm1AudioClockSelection = __HAL_RCC_GET_DFSDM1AUDIO_SOURCE();
#endif /* STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx */

  /* Get the RTC Clock configuration -----------------------------------------------*/
  tempreg = (RCC->CFGR & RCC_CFGR_RTCPRE);
  PeriphClkInit->RTCClockSelection = (uint32_t)((tempreg) | (RCC->BDCR & RCC_BDCR_RTCSEL));

  /* Get the TIM Prescaler configuration --------------------------------------------*/
  if ((RCC->DCKCFGR1 & RCC_DCKCFGR1_TIMPRE) == RESET)
  {
    PeriphClkInit->TIMPresSelection = RCC_TIMPRES_DESACTIVATED;
  }
  else
  {
    PeriphClkInit->TIMPresSelection = RCC_TIMPRES_ACTIVATED;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads current peripheral clock configuration from RCC hardware registers and populates a structure with the configuration values.
- 是否需要替换：是
- 分类/替换原因：GetMMIOFunctionInfo shows this function reads multiple RCC hardware registers (PLLI2SCFGR, PLLSAICFGR, DCKCFGR1, CFGR, BDCR) to obtain current clock configuration. The function is classified as INIT because it reads hardware initialization/configuration state. According to INIT strategy, all MMIO/register access operations should be removed while preserving structure initialization. The replacement provides reasonable default values for clock configuration that represent a typical working state, ensuring the logical post-initialization state matches expected behavior.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Get the RCC_PeriphCLKInitTypeDef according to the internal
*         RCC configuration registers.
* @param  PeriphClkInit pointer to the configured RCC_PeriphCLKInitTypeDef structure
* @retval None
*/
void HAL_RCCEx_GetPeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  /* Set all possible values for the extended clock type parameter------------*/
#if defined (STM32F765xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx)
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S      | RCC_PERIPHCLK_LPTIM1   |\
                                        RCC_PERIPHCLK_SAI1     | RCC_PERIPHCLK_SAI2     |\
                                        RCC_PERIPHCLK_TIM      | RCC_PERIPHCLK_RTC      |\
                                        RCC_PERIPHCLK_CEC      | RCC_PERIPHCLK_I2C4     |\
                                        RCC_PERIPHCLK_I2C1     | RCC_PERIPHCLK_I2C2     |\
                                        RCC_PERIPHCLK_I2C3     | RCC_PERIPHCLK_USART1   |\
                                        RCC_PERIPHCLK_USART2   | RCC_PERIPHCLK_USART3   |\
                                        RCC_PERIPHCLK_UART4    | RCC_PERIPHCLK_UART5    |\
                                        RCC_PERIPHCLK_USART6   | RCC_PERIPHCLK_UART7    |\
                                        RCC_PERIPHCLK_UART8    | RCC_PERIPHCLK_SDMMC1   |\
                                        RCC_PERIPHCLK_CLK48    | RCC_PERIPHCLK_SDMMC2   |\
                                        RCC_PERIPHCLK_DFSDM1   | RCC_PERIPHCLK_DFSDM1_AUDIO;
#else
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S      | RCC_PERIPHCLK_LPTIM1   |\
                                        RCC_PERIPHCLK_SAI1     | RCC_PERIPHCLK_SAI2     |\
                                        RCC_PERIPHCLK_TIM      | RCC_PERIPHCLK_RTC      |\
                                        RCC_PERIPHCLK_CEC      | RCC_PERIPHCLK_I2C4     |\
                                        RCC_PERIPHCLK_I2C1     | RCC_PERIPHCLK_I2C2     |\
                                        RCC_PERIPHCLK_I2C3     | RCC_PERIPHCLK_USART1   |\
                                        RCC_PERIPHCLK_USART2   | RCC_PERIPHCLK_USART3   |\
                                        RCC_PERIPHCLK_UART4    | RCC_PERIPHCLK_UART5    |\
                                        RCC_PERIPHCLK_USART6   | RCC_PERIPHCLK_UART7    |\
                                        RCC_PERIPHCLK_UART8    | RCC_PERIPHCLK_SDMMC1   |\
                                        RCC_PERIPHCLK_CLK48;
#endif /* STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx */

  /* Provide default values for PLL configurations -----------------------------------------------*/
  PeriphClkInit->PLLI2S.PLLI2SN = 192;  /* Default PLLI2S N multiplier */
  PeriphClkInit->PLLI2S.PLLI2SP = 2;    /* Default PLLI2S P divider */
  PeriphClkInit->PLLI2S.PLLI2SQ = 4;    /* Default PLLI2S Q divider */
  PeriphClkInit->PLLI2S.PLLI2SR = 2;    /* Default PLLI2S R divider */

  PeriphClkInit->PLLSAI.PLLSAIN = 192;  /* Default PLLSAI N multiplier */
  PeriphClkInit->PLLSAI.PLLSAIP = 2;    /* Default PLLSAI P divider */
  PeriphClkInit->PLLSAI.PLLSAIQ = 4;    /* Default PLLSAI Q divider */
  PeriphClkInit->PLLSAI.PLLSAIR = 2;    /* Default PLLSAI R divider */

  /* Provide default division factors -------------------------------------------*/
  PeriphClkInit->PLLI2SDivQ = 1;        /* Default PLLI2S division factor for SAI1 */
  PeriphClkInit->PLLSAIDivQ = 1;        /* Default PLLSAI division factor for SAI1 */
  PeriphClkInit->PLLSAIDivR = 1;        /* Default PLLSAI division factor for LTDC */

  /* Provide default clock source selections ----------------------------------------------*/
  PeriphClkInit->Sai1ClockSelection = RCC_SAI1CLKSOURCE_PLLSAI;
  PeriphClkInit->Sai2ClockSelection = RCC_SAI2CLKSOURCE_PLLSAI;
  PeriphClkInit->I2sClockSelection = RCC_I2SCLKSOURCE_PLLI2S;
  PeriphClkInit->I2c1ClockSelection = RCC_I2C1CLKSOURCE_PCLK1;
  PeriphClkInit->I2c2ClockSelection = RCC_I2C2CLKSOURCE_PCLK1;
  PeriphClkInit->I2c3ClockSelection = RCC_I2C3CLKSOURCE_PCLK1;
  PeriphClkInit->I2c4ClockSelection = RCC_I2C4CLKSOURCE_PCLK1;
  PeriphClkInit->Usart1ClockSelection = RCC_USART1CLKSOURCE_PCLK2;
  PeriphClkInit->Usart2ClockSelection = RCC_USART2CLKSOURCE_PCLK1;
  PeriphClkInit->Usart3ClockSelection = RCC_USART3CLKSOURCE_PCLK1;
  PeriphClkInit->Uart4ClockSelection = RCC_UART4CLKSOURCE_PCLK1;
  PeriphClkInit->Uart5ClockSelection = RCC_UART5CLKSOURCE_PCLK1;
  PeriphClkInit->Usart6ClockSelection = RCC_USART6CLKSOURCE_PCLK2;
  PeriphClkInit->Uart7ClockSelection = RCC_UART7CLKSOURCE_PCLK1;
  PeriphClkInit->Uart8ClockSelection = RCC_UART8CLKSOURCE_PCLK1;
  PeriphClkInit->Lptim1ClockSelection = RCC_LPTIM1CLKSOURCE_LSI;
  PeriphClkInit->CecClockSelection = RCC_CECCLKSOURCE_LSE;
  PeriphClkInit->Clk48ClockSelection = RCC_CLK48CLKSOURCE_PLLSAIP;
  PeriphClkInit->Sdmmc1ClockSelection = RCC_SDMMC1CLKSOURCE_CLK48;

#if defined (STM32F765xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx)
  PeriphClkInit->Sdmmc2ClockSelection = RCC_SDMMC2CLKSOURCE_CLK48;
  PeriphClkInit->Dfsdm1ClockSelection = RCC_DFSDM1CLKSOURCE_PCLK2;
  PeriphClkInit->Dfsdm1AudioClockSelection = RCC_DFSDM1AUDIOCLKSOURCE_SAI1;
#endif /* STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx */

  /* Provide default RTC and TIM configurations -----------------------------------------------*/
  PeriphClkInit->RTCClockSelection = RCC_RTCCLKSOURCE_LSE;
  PeriphClkInit->TIMPresSelection = RCC_TIMPRES_DESACTIVATED;
}
```

=== 信息结束 ===
```

### config_enable_default_clocks

```text
=== config_enable_default_clocks 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32f2_f4_f7.c
- 行号：122
- 函数内容：void config_enable_default_clocks(void)
{
	/* Power Interface clock enabled by default */
	LL_APB1_GRP1_EnableClock(LL_APB1_GRP1_PERIPH_PWR);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Activates default clocks by enabling the Power Interface clock
- 是否需要替换：是
- 分类/替换原因：This function is an initialization function that configures clock settings by enabling the PWR peripheral clock through hardware register writes. GetFunctionInfo shows it calls LL_APB1_GRP1_EnableClock which performs MMIO operations (writes to RCC->APB1ENR). GetFunctionCallStack reveals it's called from stm32_clock_control_init as part of clock control initialization. It fits the INIT category because it initializes peripheral configurations and contains hardware-dependent operations that need to be removed in the replacement.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Activate default clocks
*/
void config_enable_default_clocks(void)
{
	/* Power Interface clock enabled by default */
	/* Hardware register write removed for simulation */
}
```

=== 信息结束 ===
```

### config_pll_sysclock

```text
=== config_pll_sysclock 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32f2_f4_f7.c
- 行号：57
- 函数内容：void config_pll_sysclock(void)
{
	LL_RCC_PLL_ConfigDomain_SYS(get_pll_source(),
				    pllm(STM32_PLL_M_DIVISOR),
				    STM32_PLL_N_MULTIPLIER,
				    pllp(STM32_PLL_P_DIVISOR));

#if defined(CONFIG_SOC_SERIES_STM32F7X)
	/* Assuming we stay on Power Scale default value: Power Scale 1 */
	if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC > 180000000) {
		/* Enable the PLL (PLLON) before setting overdrive. Skipping the PLL
		 * locking phase since the system will be stalled during the switch
		 * (ODSW) but the PLL clock system will be running during the locking
		 * phase. See reference manual (RM0431) §4.1.4 Voltage regulator
		 * Sub section: Entering Over-drive mode.
		 */
		LL_RCC_PLL_Enable();

		/* Set Overdrive if needed before configuring the Flash Latency */
		LL_PWR_EnableOverDriveMode();
		while (LL_PWR_IsActiveFlag_OD() != 1) {
			/* Wait for OverDrive mode ready */
		}
		LL_PWR_EnableOverDriveSwitching();
		while (LL_PWR_IsActiveFlag_ODSW() != 1) {
			/* Wait for OverDrive switch ready */
		}

		/* The PLL could still not be locked when returning to the caller
		 * function. But the caller doesn't know we've turned on the PLL
		 * for the overdrive function. The caller will try to turn on the PLL
		 * And start waiting for the PLL locking phase to complete.
		 */
	}
#endif /* CONFIG_SOC_SERIES_STM32F7X */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures the PLL (Phase-Locked Loop) system clock for STM32 microcontrollers, including optional overdrive mode for STM32F7 series
- 是否需要替换：是
- 分类/替换原因：This function initializes clock hardware configuration: 1) Calls LL_RCC_PLL_ConfigDomain_SYS() to set PLL parameters, 2) For STM32F7 series, enables PLL and overdrive mode with polling loops waiting for hardware status flags. GetMMIOFunctionInfo shows it's in the MMIO function set (though no detailed expressions). The function contains hardware-dependent operations through LL layer calls and polling loops. It's called from set_up_plls() as part of system initialization. Classification priority: Not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not interrupt handler). Fits INIT category: 'Functions that initialize peripheral/configurations or allocate resources'.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Set up pll configuration
*/
void config_pll_sysclock(void)
{
	/* Skip hardware-specific PLL configuration */
	/* Original: LL_RCC_PLL_ConfigDomain_SYS(get_pll_source(),
			    pllm(STM32_PLL_M_DIVISOR),
			    STM32_PLL_N_MULTIPLIER,
			    pllp(STM32_PLL_P_DIVISOR)); */

#if defined(CONFIG_SOC_SERIES_STM32F7X)
	/* Assuming we stay on Power Scale default value: Power Scale 1 */
	if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC > 180000000) {
		/* Skip PLL enable for overdrive mode */
		/* Original: LL_RCC_PLL_Enable(); */

		/* Skip overdrive mode configuration */
		/* Original: LL_PWR_EnableOverDriveMode(); */
		/* Skip wait for OverDrive mode ready */
		/* Original while (LL_PWR_IsActiveFlag_OD() != 1) { } */

		/* Original: LL_PWR_EnableOverDriveSwitching(); */
		/* Skip wait for OverDrive switch ready */
		/* Original while (LL_PWR_IsActiveFlag_ODSW() != 1) { } */

		/* The PLL could still not be locked when returning to the caller
		 * function. But the caller doesn't know we've turned on the PLL
		 * for the overdrive function. The caller will try to turn on the PLL
		 * And start waiting for the PLL locking phase to complete.
		 */
	}
#endif /* CONFIG_SOC_SERIES_STM32F7X */
}
```

=== 信息结束 ===
```

### eth_stm32_hal_set_config

```text
=== eth_stm32_hal_set_config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_stm32_hal.c
- 行号：1582
- 函数内容：static int eth_stm32_hal_set_config(const struct device *dev,
				    enum ethernet_config_type type,
				    const struct ethernet_config *config)
{
	int ret = -ENOTSUP;
	struct eth_stm32_hal_dev_data *dev_data;
	ETH_HandleTypeDef *heth;

	dev_data = dev->data;
	heth = &dev_data->heth;

	switch (type) {
	case ETHERNET_CONFIG_TYPE_MAC_ADDRESS:
		memcpy(dev_data->mac_addr, config->mac_address.addr, 6);
		heth->Instance->MACA0HR = (dev_data->mac_addr[5] << 8) |
			dev_data->mac_addr[4];
		heth->Instance->MACA0LR = (dev_data->mac_addr[3] << 24) |
			(dev_data->mac_addr[2] << 16) |
			(dev_data->mac_addr[1] << 8) |
			dev_data->mac_addr[0];
		net_if_set_link_addr(dev_data->iface, dev_data->mac_addr,
				     sizeof(dev_data->mac_addr),
				     NET_LINK_ETHERNET);
		ret = 0;
		break;
	case ETHERNET_CONFIG_TYPE_PROMISC_MODE:
#if defined(CONFIG_NET_PROMISCUOUS_MODE)
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
		if (config->promisc_mode) {
			heth->Instance->MACPFR |= ETH_MACPFR_PR;
		} else {
			heth->Instance->MACPFR &= ~ETH_MACPFR_PR;
		}
#else
		if (config->promisc_mode) {
			heth->Instance->MACFFR |= ETH_MACFFR_PM;
		} else {
			heth->Instance->MACFFR &= ~ETH_MACFFR_PM;
		}
#endif  /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */
		ret = 0;
#endif /* CONFIG_NET_PROMISCUOUS_MODE */
		break;
	default:
		break;
	}

	return ret;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures Ethernet peripheral settings including MAC address and promiscuous mode
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs peripheral configuration operations for the STM32 Ethernet controller. The function handles two configuration types: 1) MAC address configuration - copies MAC address to device data and writes to hardware registers (MACA0HR/MACA0LR), 2) Promiscuous mode configuration - modifies hardware filter registers (MACPFR/MACFFR) based on STM32 series. The function contains direct hardware register accesses that need to be removed in the replacement while preserving non-hardware logic such as memory copy operations, network interface updates (net_if_set_link_addr), and return value handling. Although GetMMIOFunctionInfo returned an empty list, the source code clearly shows hardware register writes to heth->Instance->MACA0HR, heth->Instance->MACA0LR, heth->Instance->MACPFR, and heth->Instance->MACFFR.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Start interruption-poll thread */
static int eth_stm32_hal_set_config(const struct device *dev,
				    enum ethernet_config_type type,
				    const struct ethernet_config *config)
{
	int ret = -ENOTSUP;
	struct eth_stm32_hal_dev_data *dev_data;
	ETH_HandleTypeDef *heth;

	dev_data = dev->data;
	heth = &dev_data->heth;

	switch (type) {
	case ETHERNET_CONFIG_TYPE_MAC_ADDRESS:
		memcpy(dev_data->mac_addr, config->mac_address.addr, 6);
		/* Hardware register writes removed for simulation */
		net_if_set_link_addr(dev_data->iface, dev_data->mac_addr,
				     sizeof(dev_data->mac_addr),
				     NET_LINK_ETHERNET);
		ret = 0;
		break;
	case ETHERNET_CONFIG_TYPE_PROMISC_MODE:
#if defined(CONFIG_NET_PROMISCUOUS_MODE)
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
		/* Hardware register writes removed for simulation */
#else
		/* Hardware register writes removed for simulation */
#endif  /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */
		ret = 0;
#endif /* CONFIG_NET_PROMISCUOUS_MODE */
		break;
	default:
		break;
	}

	return ret;
}
```

=== 信息结束 ===
```

### eth_tx

```text
=== eth_tx 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_stm32_hal.c
- 行号：326
- 函数内容：static int eth_tx(const struct device *dev, struct net_pkt *pkt)
{
	struct eth_stm32_hal_dev_data *dev_data = dev->data;
	ETH_HandleTypeDef *heth;
	int res;
	size_t total_len;
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	size_t remaining_read;
	struct eth_stm32_tx_context ctx = {.pkt = pkt, .first_tx_buffer_index = 0};
	struct eth_stm32_tx_buffer_header *buf_header = NULL;
#else
	uint8_t *dma_buffer;
	__IO ETH_DMADescTypeDef *dma_tx_desc;
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */
	HAL_StatusTypeDef hal_ret = HAL_OK;
#if defined(CONFIG_PTP_CLOCK_STM32_HAL)
	bool timestamped_frame;
#endif /* CONFIG_PTP_CLOCK_STM32_HAL */

	__ASSERT_NO_MSG(pkt != NULL);
	__ASSERT_NO_MSG(pkt->frags != NULL);
	__ASSERT_NO_MSG(dev != NULL);
	__ASSERT_NO_MSG(dev_data != NULL);

	heth = &dev_data->heth;

	total_len = net_pkt_get_len(pkt);
	if (total_len > (ETH_STM32_TX_BUF_SIZE * ETH_TXBUFNB)) {
		LOG_ERR("PKT too big");
		return -EIO;
	}

	k_mutex_lock(&dev_data->tx_mutex, K_FOREVER);

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	ctx.first_tx_buffer_index = allocate_tx_buffer();
	buf_header = &dma_tx_buffer_header[ctx.first_tx_buffer_index];
#else /* CONFIG_ETH_STM32_HAL_API_V2 */
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	uint32_t cur_tx_desc_idx;

	cur_tx_desc_idx = heth->TxDescList.CurTxDesc;
	dma_tx_desc = (ETH_DMADescTypeDef *)heth->TxDescList.TxDesc[cur_tx_desc_idx];
#else
	dma_tx_desc = heth->TxDesc;
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */

	while (IS_ETH_DMATXDESC_OWN(dma_tx_desc) != (uint32_t)RESET) {
		k_yield();
	}
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_PTP_CLOCK_STM32_HAL)
	timestamped_frame = eth_is_ptp_pkt(net_pkt_iface(pkt), pkt);
	if (timestamped_frame) {
		/* Enable transmit timestamp */
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
		HAL_ETH_PTP_InsertTxTimestamp(heth);
#elif defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
		dma_tx_desc->DESC2 |= ETH_DMATXNDESCRF_TTSE;
#else
		dma_tx_desc->Status |= ETH_DMATXDESC_TTSE;
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */
	}
#endif /* CONFIG_PTP_CLOCK_STM32_HAL */

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	remaining_read = total_len;
	/* fill and allocate buffer until remaining data fits in one buffer */
	while (remaining_read > ETH_STM32_TX_BUF_SIZE) {
		if (net_pkt_read(pkt, buf_header->tx_buff.buffer, ETH_STM32_TX_BUF_SIZE)) {
			res = -ENOBUFS;
			goto error;
		}
		const uint16_t next_buffer_id = allocate_tx_buffer();

		buf_header->tx_buff.len = ETH_STM32_TX_BUF_SIZE;
		/* append new buffer to the linked list */
		buf_header->tx_buff.next = &dma_tx_buffer_header[next_buffer_id].tx_buff;
		/* and adjust tail pointer */
		buf_header = &dma_tx_buffer_header[next_buffer_id];
		remaining_read -= ETH_STM32_TX_BUF_SIZE;
	}
	if (net_pkt_read(pkt, buf_header->tx_buff.buffer, remaining_read)) {
		res = -ENOBUFS;
		goto error;
	}
	buf_header->tx_buff.len = remaining_read;
	buf_header->tx_buff.next = NULL;

#else /* CONFIG_ETH_STM32_HAL_API_V2 */
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	dma_buffer = dma_tx_buffer[cur_tx_desc_idx];
#else
	dma_buffer = (uint8_t *)(dma_tx_desc->Buffer1Addr);
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */

	if (net_pkt_read(pkt, dma_buffer, total_len)) {
		res = -ENOBUFS;
		goto error;
	}

#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	ETH_BufferTypeDef tx_buffer_def;

	tx_buffer_def.buffer = dma_buffer;
	tx_buffer_def.len = total_len;
	tx_buffer_def.next = NULL;
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X) || \
	defined(CONFIG_ETH_STM32_HAL_API_V2)

	tx_config.Length = total_len;
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	tx_config.pData = &ctx;
	tx_config.TxBuffer = &dma_tx_buffer_header[ctx.first_tx_buffer_index].tx_buff;
#else
	tx_config.TxBuffer = &tx_buffer_def;
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

	/* Reset TX complete interrupt semaphore before TX request*/
	k_sem_reset(&dev_data->tx_int_sem);

	/* tx_buffer is allocated on function stack, we need */
	/* to wait for the transfer to complete */
	/* So it is not freed before the interrupt happens */
	hal_ret = HAL_ETH_Transmit_IT(heth, &tx_config);

	if (hal_ret != HAL_OK) {
		LOG_ERR("HAL_ETH_Transmit: failed!");
		res = -EIO;
		goto error;
	}

	/* Wait for end of TX buffer transmission */
	/* If the semaphore timeout breaks, it means */
	/* an error occurred or IT was not fired */
	if (k_sem_take(&dev_data->tx_int_sem,
			K_MSEC(ETH_DMA_TX_TIMEOUT_MS)) != 0) {

		LOG_ERR("HAL_ETH_TransmitIT tx_int_sem take timeout");
		res = -EIO;

#ifndef CONFIG_ETH_STM32_HAL_API_V2
		/* Content of the packet could be the reason for timeout */
		LOG_HEXDUMP_ERR(dma_buffer, total_len, "eth packet timeout");
#endif

		/* Check for errors */
		/* Ethernet device was put in error state */
		/* Error state is unrecoverable ? */
		if (HAL_ETH_GetState(heth) == HAL_ETH_STATE_ERROR) {
			LOG_ERR("%s: ETH in error state: errorcode:%x",
				__func__,
				HAL_ETH_GetError(heth));
			/* TODO recover from error state by restarting eth */
		}

		/* Check for DMA errors */
		if (HAL_ETH_GetDMAError(heth)) {
			LOG_ERR("%s: ETH DMA error: dmaerror:%x",
				__func__,
				HAL_ETH_GetDMAError(heth));
			/* DMA fatal bus errors are putting in error state*/
			/* TODO recover from this */
		}

		/* Check for MAC errors */
		if (HAL_ETH_GetMACError(heth)) {
			LOG_ERR("%s: ETH MAC error: macerror:%x",
				__func__,
				HAL_ETH_GetMACError(heth));
			/* MAC errors are putting in error state*/
			/* TODO recover from this */
		}

		goto error;
	}

#else
	hal_ret = HAL_ETH_TransmitFrame(heth, total_len);

	if (hal_ret != HAL_OK) {
		LOG_ERR("HAL_ETH_Transmit: failed!");
		res = -EIO;
		goto error;
	}

	/* When Transmit Underflow flag is set, clear it and issue a
	 * Transmit Poll Demand to resume transmission.
	 */
	if ((heth->Instance->DMASR & ETH_DMASR_TUS) != (uint32_t)RESET) {
		/* Clear TUS ETHERNET DMA flag */
		heth->Instance->DMASR = ETH_DMASR_TUS;
		/* Resume DMA transmission*/
		heth->Instance->DMATPDR = 0;
		res = -EIO;
		goto error;
	}
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X || CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_PTP_CLOCK_STM32_HAL) && !defined(CONFIG_ETH_STM32_HAL_API_V2)
	if (timestamped_frame) {
		/* Retrieve transmission timestamp from last DMA TX descriptor */
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
		ETH_TxDescListTypeDef * dma_tx_desc_list;

		__IO ETH_DMADescTypeDef *last_dma_tx_desc;

		dma_tx_desc_list = &heth->TxDescList;
		for (uint32_t i = 0; i < ETH_TX_DESC_CNT; i++) {
			const uint32_t last_desc_idx = (cur_tx_desc_idx + i) % ETH_TX_DESC_CNT;

			last_dma_tx_desc =
				(ETH_DMADescTypeDef *)dma_tx_desc_list->TxDesc[last_desc_idx];
			if (last_dma_tx_desc->DESC3 & ETH_DMATXNDESCWBF_LD) {
				break;
			}
		}

		while (IS_ETH_DMATXDESC_OWN(last_dma_tx_desc) != (uint32_t)RESET) {
			/* Wait for transmission */
			k_yield();
		}

		if ((last_dma_tx_desc->DESC3 & ETH_DMATXNDESCWBF_LD) &&
				(last_dma_tx_desc->DESC3 & ETH_DMATXNDESCWBF_TTSS)) {
			pkt->timestamp.second = last_dma_tx_desc->DESC1;
			pkt->timestamp.nanosecond = last_dma_tx_desc->DESC0;
		} else {
			/* Invalid value */
			pkt->timestamp.second = UINT64_MAX;
			pkt->timestamp.nanosecond = UINT32_MAX;
		}
#else
		__IO ETH_DMADescTypeDef *last_dma_tx_desc = dma_tx_desc;

		while (!(last_dma_tx_desc->Status & ETH_DMATXDESC_LS) &&
				last_dma_tx_desc->Buffer2NextDescAddr) {
			last_dma_tx_desc =
				(ETH_DMADescTypeDef *)last_dma_tx_desc->Buffer2NextDescAddr;
		}

		while (IS_ETH_DMATXDESC_OWN(last_dma_tx_desc) != (uint32_t)RESET) {
			/* Wait for transmission */
			k_yield();
		}

		if (last_dma_tx_desc->Status & ETH_DMATXDESC_LS &&
				last_dma_tx_desc->Status & ETH_DMATXDESC_TTSS) {
			pkt->timestamp.second = last_dma_tx_desc->TimeStampHigh;
			pkt->timestamp.nanosecond = last_dma_tx_desc->TimeStampLow;
		} else {
			/* Invalid value */
			pkt->timestamp.second = UINT64_MAX;
			pkt->timestamp.nanosecond = UINT32_MAX;
		}
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */

		net_if_add_tx_timestamp(pkt);
	}
#endif /* CONFIG_PTP_CLOCK_STM32_HAL && !CONFIG_ETH_STM32_HAL_API_V2 */

	res = 0;
error:

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	/* free package tx buffer */
	if (res != 0) {
		HAL_ETH_TxFreeCallback((uint32_t *)&ctx);
	} else if (HAL_ETH_ReleaseTxPacket(heth) != HAL_OK) {
		LOG_ERR("HAL_ETH_ReleaseTxPacket failed");
		res = -EIO;
	}
#endif

	k_mutex_unlock(&dev_data->tx_mutex);

	return res;
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Ethernet packet transmission function that sends network packets through STM32 HAL Ethernet driver with DMA descriptor management and optional PTP timestamping
- 是否需要替换：是
- 分类/替换原因：Function performs critical data transmission operations with hardware dependencies including DMA descriptor polling (IS_ETH_DMATXDESC_OWN), hardware register writes for timestamping and error handling, and calls to HAL_ETH_Transmit_IT/HAL_ETH_TransmitFrame. Contains OS operations (mutex, semaphores) that must be preserved. GetMMIOFunctionInfo returned empty but source code shows clear hardware register accesses. Classification as RECV (data transmission function) with replacement strategy to remove hardware operations while preserving buffer management, OS operations, and packet processing logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int eth_tx(const struct device *dev, struct net_pkt *pkt)
{
	struct eth_stm32_hal_dev_data *dev_data = dev->data;
	ETH_HandleTypeDef *heth;
	int res;
	size_t total_len;
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	size_t remaining_read;
	struct eth_stm32_tx_context ctx = {.pkt = pkt, .first_tx_buffer_index = 0};
	struct eth_stm32_tx_buffer_header *buf_header = NULL;
#else
	uint8_t *dma_buffer;
	__IO ETH_DMADescTypeDef *dma_tx_desc;
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */
	HAL_StatusTypeDef hal_ret = HAL_OK;
#if defined(CONFIG_PTP_CLOCK_STM32_HAL)
	bool timestamped_frame;
#endif /* CONFIG_PTP_CLOCK_STM32_HAL */

	__ASSERT_NO_MSG(pkt != NULL);
	__ASSERT_NO_MSG(pkt->frags != NULL);
	__ASSERT_NO_MSG(dev != NULL);
	__ASSERT_NO_MSG(dev_data != NULL);

	heth = &dev_data->heth;

	total_len = net_pkt_get_len(pkt);
	if (total_len > (ETH_STM32_TX_BUF_SIZE * ETH_TXBUFNB)) {
		LOG_ERR("PKT too big");
		return -EIO;
	}

	k_mutex_lock(&dev_data->tx_mutex, K_FOREVER);

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	ctx.first_tx_buffer_index = allocate_tx_buffer();
	buf_header = &dma_tx_buffer_header[ctx.first_tx_buffer_index];
#else /* CONFIG_ETH_STM32_HAL_API_V2 */
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	uint32_t cur_tx_desc_idx;

	cur_tx_desc_idx = heth->TxDescList.CurTxDesc;
	dma_tx_desc = (ETH_DMADescTypeDef *)heth->TxDescList.TxDesc[cur_tx_desc_idx];
#else
	dma_tx_desc = heth->TxDesc;
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */

	/* [LOOP REMOVED] Skip polling for DMA descriptor ownership */
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_PTP_CLOCK_STM32_HAL)
	timestamped_frame = eth_is_ptp_pkt(net_pkt_iface(pkt), pkt);
	if (timestamped_frame) {
		/* Enable transmit timestamp - simulated */
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
		/* HAL_ETH_PTP_InsertTxTimestamp(heth); - removed hardware call */
#elif defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
		/* dma_tx_desc->DESC2 |= ETH_DMATXNDESCRF_TTSE; - removed hardware write */
#else
		/* dma_tx_desc->Status |= ETH_DMATXDESC_TTSE; - removed hardware write */
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */
	}
#endif /* CONFIG_PTP_CLOCK_STM32_HAL */

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	remaining_read = total_len;
	/* fill and allocate buffer until remaining data fits in one buffer */
	while (remaining_read > ETH_STM32_TX_BUF_SIZE) {
		if (net_pkt_read(pkt, buf_header->tx_buff.buffer, ETH_STM32_TX_BUF_SIZE)) {
			res = -ENOBUFS;
			goto error;
		}
		const uint16_t next_buffer_id = allocate_tx_buffer();

		buf_header->tx_buff.len = ETH_STM32_TX_BUF_SIZE;
		/* append new buffer to the linked list */
		buf_header->tx_buff.next = &dma_tx_buffer_header[next_buffer_id].tx_buff;
		/* and adjust tail pointer */
		buf_header = &dma_tx_buffer_header[next_buffer_id];
		remaining_read -= ETH_STM32_TX_BUF_SIZE;
	}
	if (net_pkt_read(pkt, buf_header->tx_buff.buffer, remaining_read)) {
		res = -ENOBUFS;
		goto error;
	}
	buf_header->tx_buff.len = remaining_read;
	buf_header->tx_buff.next = NULL;

#else /* CONFIG_ETH_STM32_HAL_API_V2 */
#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	dma_buffer = dma_tx_buffer[cur_tx_desc_idx];
#else
	dma_buffer = (uint8_t *)(dma_tx_desc->Buffer1Addr);
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */

	if (net_pkt_read(pkt, dma_buffer, total_len)) {
		res = -ENOBUFS;
		goto error;
	}

#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X)
	ETH_BufferTypeDef tx_buffer_def;

	tx_buffer_def.buffer = dma_buffer;
	tx_buffer_def.len = total_len;
	tx_buffer_def.next = NULL;
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X */
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_SOC_SERIES_STM32H7X) || defined(CONFIG_SOC_SERIES_STM32H5X) || \
	defined(CONFIG_ETH_STM32_HAL_API_V2)

	tx_config.Length = total_len;
#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	tx_config.pData = &ctx;
	tx_config.TxBuffer = &dma_tx_buffer_header[ctx.first_tx_buffer_index].tx_buff;
#else
	tx_config.TxBuffer = &tx_buffer_def;
#endif /* CONFIG_ETH_STM32_HAL_API_V2 */

	/* Reset TX complete interrupt semaphore before TX request*/
	k_sem_reset(&dev_data->tx_int_sem);

	/* Simulate successful transmission */
	hal_ret = HAL_OK;

	if (hal_ret != HAL_OK) {
		LOG_ERR("HAL_ETH_Transmit: failed!");
		res = -EIO;
		goto error;
	}

	/* Simulate successful transmission completion */
	/* Give semaphore to indicate transmission complete */
	k_sem_give(&dev_data->tx_int_sem);

#else
	/* Simulate successful transmission */
	hal_ret = HAL_OK;

	if (hal_ret != HAL_OK) {
		LOG_ERR("HAL_ETH_Transmit: failed!");
		res = -EIO;
		goto error;
	}

	/* Skip hardware error checking and register writes */
#endif /* CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H5X || CONFIG_ETH_STM32_HAL_API_V2 */

#if defined(CONFIG_PTP_CLOCK_STM32_HAL) && !defined(CONFIG_ETH_STM32_HAL_API_V2)
	if (timestamped_frame) {
		/* Simulate timestamp retrieval */
		/* Skip hardware-dependent timestamp retrieval loops */
		net_if_add_tx_timestamp(pkt);
	}
#endif /* CONFIG_PTP_CLOCK_STM32_HAL && !CONFIG_ETH_STM32_HAL_API_V2 */

	res = 0;
error:

#if defined(CONFIG_ETH_STM32_HAL_API_V2)
	/* free package tx buffer */
	if (res != 0) {
		HAL_ETH_TxFreeCallback((uint32_t *)&ctx);
	} else if (HAL_ETH_ReleaseTxPacket(heth) != HAL_OK) {
		LOG_ERR("HAL_ETH_ReleaseTxPacket failed");
		res = -EIO;
	}
#endif

	k_mutex_unlock(&dev_data->tx_mutex);

	return res;
}
```

=== 信息结束 ===
```

### gpio_stm32_configure_raw

```text
=== gpio_stm32_configure_raw 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/gpio/gpio_stm32.c
- 行号：157
- 函数内容：static void gpio_stm32_configure_raw(const struct device *dev, int pin,
				     int conf, int func)
{
	const struct gpio_stm32_config *cfg = dev->config;
	GPIO_TypeDef *gpio = (GPIO_TypeDef *)cfg->base;

	int pin_ll = stm32_pinval_get(pin);

#ifdef CONFIG_SOC_SERIES_STM32F1X
	ARG_UNUSED(func);

	uint32_t temp = conf &
			      (STM32_MODE_INOUT_MASK << STM32_MODE_INOUT_SHIFT);

	if (temp == STM32_MODE_INPUT) {
		temp = conf & (STM32_CNF_IN_MASK << STM32_CNF_IN_SHIFT);

		if (temp == STM32_CNF_IN_ANALOG) {
			LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_ANALOG);
		} else if (temp == STM32_CNF_IN_FLOAT) {
			LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_FLOATING);
		} else {
			temp = conf & (STM32_PUPD_MASK << STM32_PUPD_SHIFT);

			if (temp == STM32_PUPD_PULL_UP) {
				LL_GPIO_SetPinPull(gpio, pin_ll,
							       LL_GPIO_PULL_UP);
			} else {
				LL_GPIO_SetPinPull(gpio, pin_ll,
							     LL_GPIO_PULL_DOWN);
			}

			LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_INPUT);
		}

	} else {
		temp = conf & (STM32_CNF_OUT_1_MASK << STM32_CNF_OUT_1_SHIFT);

		if (temp == STM32_CNF_GP_OUTPUT) {
			LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_OUTPUT);
		} else {
			LL_GPIO_SetPinMode(gpio, pin_ll,
							LL_GPIO_MODE_ALTERNATE);
		}

		temp = conf & (STM32_CNF_OUT_0_MASK << STM32_CNF_OUT_0_SHIFT);

		if (temp == STM32_CNF_PUSH_PULL) {
			LL_GPIO_SetPinOutputType(gpio, pin_ll,
						       LL_GPIO_OUTPUT_PUSHPULL);
		} else {
			LL_GPIO_SetPinOutputType(gpio, pin_ll,
						      LL_GPIO_OUTPUT_OPENDRAIN);
		}

		temp = conf &
			    (STM32_MODE_OSPEED_MASK << STM32_MODE_OSPEED_SHIFT);

		if (temp == STM32_MODE_OUTPUT_MAX_2) {
			LL_GPIO_SetPinSpeed(gpio, pin_ll,
							LL_GPIO_SPEED_FREQ_LOW);
		} else if (temp == STM32_MODE_OUTPUT_MAX_10) {
			LL_GPIO_SetPinSpeed(gpio, pin_ll,
						     LL_GPIO_SPEED_FREQ_MEDIUM);
		} else {
			LL_GPIO_SetPinSpeed(gpio, pin_ll,
						       LL_GPIO_SPEED_FREQ_HIGH);
		}
	}
#else
	unsigned int mode, otype, ospeed, pupd;

	mode = conf & (STM32_MODER_MASK << STM32_MODER_SHIFT);
	otype = conf & (STM32_OTYPER_MASK << STM32_OTYPER_SHIFT);
	ospeed = conf & (STM32_OSPEEDR_MASK << STM32_OSPEEDR_SHIFT);
	pupd = conf & (STM32_PUPDR_MASK << STM32_PUPDR_SHIFT);

	z_stm32_hsem_lock(CFG_HW_GPIO_SEMID, HSEM_LOCK_DEFAULT_RETRY);

#if defined(CONFIG_SOC_SERIES_STM32L4X) && defined(GPIO_ASCR_ASC0)
	/*
	 * For STM32L47xx/48xx, register ASCR should be configured to connect
	 * analog switch of gpio lines to the ADC.
	 */
	if (mode == STM32_MODER_ANALOG_MODE) {
		LL_GPIO_EnablePinAnalogControl(gpio, pin_ll);
	}
#endif

	LL_GPIO_SetPinOutputType(gpio, pin_ll, otype >> STM32_OTYPER_SHIFT);

	LL_GPIO_SetPinSpeed(gpio, pin_ll, ospeed >> STM32_OSPEEDR_SHIFT);

	LL_GPIO_SetPinPull(gpio, pin_ll, pupd >> STM32_PUPDR_SHIFT);

	if (mode == STM32_MODER_ALT_MODE) {
		if (pin < 8) {
			LL_GPIO_SetAFPin_0_7(gpio, pin_ll, func);
		} else {
			LL_GPIO_SetAFPin_8_15(gpio, pin_ll, func);
		}
	}

	LL_GPIO_SetPinMode(gpio, pin_ll, mode >> STM32_MODER_SHIFT);

	z_stm32_hsem_unlock(CFG_HW_GPIO_SEMID);
#endif  /* CONFIG_SOC_SERIES_STM32F1X */

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures STM32 GPIO hardware settings including mode, output type, speed, pull-up/down, and alternate function selection
- 是否需要替换：是
- 分类/替换原因：This function is a GPIO hardware initialization/configuration function that contains multiple LL_GPIO_* function calls which manipulate GPIO peripheral registers. It parses configuration parameters and sets up GPIO mode, output type, speed, pull-up/down settings, and alternate function mappings. The function includes hardware semaphore operations (z_stm32_hsem_lock/unlock) for atomic access to GPIO registers. According to the classification criteria, this is clearly an INIT type function as it performs peripheral initialization and configuration operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void gpio_stm32_configure_raw(const struct device *dev, int pin,
				     int conf, int func)
{
	const struct gpio_stm32_config *cfg = dev->config;
	GPIO_TypeDef *gpio = (GPIO_TypeDef *)cfg->base;

	int pin_ll = stm32_pinval_get(pin);

#ifdef CONFIG_SOC_SERIES_STM32F1X
	ARG_UNUSED(func);

	uint32_t temp = conf &
		      (STM32_MODE_INOUT_MASK << STM32_MODE_INOUT_SHIFT);

	if (temp == STM32_MODE_INPUT) {
		temp = conf & (STM32_CNF_IN_MASK << STM32_CNF_IN_SHIFT);

		if (temp == STM32_CNF_IN_ANALOG) {
			/* LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_ANALOG); */
		} else if (temp == STM32_CNF_IN_FLOAT) {
			/* LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_FLOATING); */
		} else {
			temp = conf & (STM32_PUPD_MASK << STM32_PUPD_SHIFT);

			if (temp == STM32_PUPD_PULL_UP) {
				/* LL_GPIO_SetPinPull(gpio, pin_ll, LL_GPIO_PULL_UP); */
			} else {
				/* LL_GPIO_SetPinPull(gpio, pin_ll, LL_GPIO_PULL_DOWN); */
			}

			/* LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_INPUT); */
		}

	} else {
		temp = conf & (STM32_CNF_OUT_1_MASK << STM32_CNF_OUT_1_SHIFT);

		if (temp == STM32_CNF_GP_OUTPUT) {
			/* LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_OUTPUT); */
		} else {
			/* LL_GPIO_SetPinMode(gpio, pin_ll, LL_GPIO_MODE_ALTERNATE); */
		}

		temp = conf & (STM32_CNF_OUT_0_MASK << STM32_CNF_OUT_0_SHIFT);

		if (temp == STM32_CNF_PUSH_PULL) {
			/* LL_GPIO_SetPinOutputType(gpio, pin_ll, LL_GPIO_OUTPUT_PUSHPULL); */
		} else {
			/* LL_GPIO_SetPinOutputType(gpio, pin_ll, LL_GPIO_OUTPUT_OPENDRAIN); */
		}

		temp = conf &
		    (STM32_MODE_OSPEED_MASK << STM32_MODE_OSPEED_SHIFT);

		if (temp == STM32_MODE_OUTPUT_MAX_2) {
			/* LL_GPIO_SetPinSpeed(gpio, pin_ll, LL_GPIO_SPEED_FREQ_LOW); */
		} else if (temp == STM32_MODE_OUTPUT_MAX_10) {
			/* LL_GPIO_SetPinSpeed(gpio, pin_ll, LL_GPIO_SPEED_FREQ_MEDIUM); */
		} else {
			/* LL_GPIO_SetPinSpeed(gpio, pin_ll, LL_GPIO_SPEED_FREQ_HIGH); */
		}
	}
#else
	unsigned int mode, otype, ospeed, pupd;

	mode = conf & (STM32_MODER_MASK << STM32_MODER_SHIFT);
	otype = conf & (STM32_OTYPER_MASK << STM32_OTYPER_SHIFT);
	ospeed = conf & (STM32_OSPEEDR_MASK << STM32_OSPEEDR_SHIFT);
	pupd = conf & (STM32_PUPDR_MASK << STM32_PUPDR_SHIFT);

	z_stm32_hsem_lock(CFG_HW_GPIO_SEMID, HSEM_LOCK_DEFAULT_RETRY);

#if defined(CONFIG_SOC_SERIES_STM32L4X) && defined(GPIO_ASCR_ASC0)
	/*
	 * For STM32L47xx/48xx, register ASCR should be configured to connect
	 * analog switch of gpio lines to the ADC.
	 */
	if (mode == STM32_MODER_ANALOG_MODE) {
		/* LL_GPIO_EnablePinAnalogControl(gpio, pin_ll); */
	}
#endif

	/* LL_GPIO_SetPinOutputType(gpio, pin_ll, otype >> STM32_OTYPER_SHIFT); */
	/* LL_GPIO_SetPinSpeed(gpio, pin_ll, ospeed >> STM32_OSPEEDR_SHIFT); */
	/* LL_GPIO_SetPinPull(gpio, pin_ll, pupd >> STM32_PUPDR_SHIFT); */

	if (mode == STM32_MODER_ALT_MODE) {
		if (pin < 8) {
			/* LL_GPIO_SetAFPin_0_7(gpio, pin_ll, func); */
		} else {
			/* LL_GPIO_SetAFPin_8_15(gpio, pin_ll, func); */
		}
	}

	/* LL_GPIO_SetPinMode(gpio, pin_ll, mode >> STM32_MODER_SHIFT); */

	z_stm32_hsem_unlock(CFG_HW_GPIO_SEMID);
#endif  /* CONFIG_SOC_SERIES_STM32F1X */

}
```

=== 信息结束 ===
```

### gpio_stm32_port_get_raw

```text
=== gpio_stm32_port_get_raw 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/gpio/gpio_stm32.c
- 行号：399
- 函数内容：static int gpio_stm32_port_get_raw(const struct device *dev, uint32_t *value)
{
	const struct gpio_stm32_config *cfg = dev->config;
	GPIO_TypeDef *gpio = (GPIO_TypeDef *)cfg->base;

	*value = LL_GPIO_ReadInputPort(gpio);

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Reads the raw input port value from a GPIO peripheral and stores it in the provided value pointer
- 是否需要替换：是
- 分类/替换原因：This function performs data reception from hardware by reading GPIO input port values through LL_GPIO_ReadInputPort(). GetMMIOFunctionInfo shows it contains hardware register access operations (though no explicit MMIO expressions were listed, the call to LL_GPIO_ReadInputPort indicates hardware reading). The function is classified as RECV because it reads hardware state (GPIO input values) and returns it to the caller, which is a data reception operation. It's not CORE (no NVIC/OS operations), not IRQ (not an interrupt handler), not INIT (not initialization), and not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int gpio_stm32_port_get_raw(const struct device *dev, uint32_t *value)
{
    const struct gpio_stm32_config *cfg = dev->config;
    GPIO_TypeDef *gpio = (GPIO_TypeDef *)cfg->base;

    // Simulate reading GPIO input port value
    // For GPIO simulation, we'll return a default value (0)
    *value = 0;
    
    return 0;
}
```

=== 信息结束 ===
```

### set_up_fixed_clock_sources

```text
=== set_up_fixed_clock_sources 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c
- 行号：547
- 函数内容：static void set_up_fixed_clock_sources(void)
{

	if (IS_ENABLED(STM32_HSE_ENABLED)) {
#if defined(STM32_HSE_BYPASS)
		/* Check if need to enable HSE bypass feature or not */
		if (IS_ENABLED(STM32_HSE_BYPASS)) {
			LL_RCC_HSE_EnableBypass();
		} else {
			LL_RCC_HSE_DisableBypass();
		}
#endif
#if STM32_HSE_TCXO
		LL_RCC_HSE_EnableTcxo();
#endif
#if STM32_HSE_DIV2
		LL_RCC_HSE_EnableDiv2();
#endif
		/* Enable HSE */
		LL_RCC_HSE_Enable();
		while (LL_RCC_HSE_IsReady() != 1) {
		/* Wait for HSE ready */
		}
	}

	if (IS_ENABLED(STM32_HSI_ENABLED)) {
		/* Enable HSI if not enabled */
		if (LL_RCC_HSI_IsReady() != 1) {
			/* Enable HSI */
			LL_RCC_HSI_Enable();
			while (LL_RCC_HSI_IsReady() != 1) {
			/* Wait for HSI ready */
			}
		}
#if STM32_HSI_DIV_ENABLED
		LL_RCC_SetHSIDiv(hsi_divider(STM32_HSI_DIVISOR));
#endif
	}

#if defined(STM32_MSI_ENABLED)
	if (IS_ENABLED(STM32_MSI_ENABLED)) {
		/* Set MSI Range */
#if defined(RCC_CR_MSIRGSEL)
		LL_RCC_MSI_EnableRangeSelection();
#endif /* RCC_CR_MSIRGSEL */

#if defined(CONFIG_SOC_SERIES_STM32L0X) || defined(CONFIG_SOC_SERIES_STM32L1X)
		LL_RCC_MSI_SetRange(STM32_MSI_RANGE << RCC_ICSCR_MSIRANGE_Pos);
#else
		LL_RCC_MSI_SetRange(STM32_MSI_RANGE << RCC_CR_MSIRANGE_Pos);
#endif /* CONFIG_SOC_SERIES_STM32L0X || CONFIG_SOC_SERIES_STM32L1X */

#if STM32_MSI_PLL_MODE
		/* Enable MSI hardware auto calibration */
		LL_RCC_MSI_EnablePLLMode();
#endif

		LL_RCC_MSI_SetCalibTrimming(0);

		/* Enable MSI if not enabled */
		if (LL_RCC_MSI_IsReady() != 1) {
			/* Enable MSI */
			LL_RCC_MSI_Enable();
			while (LL_RCC_MSI_IsReady() != 1) {
				/* Wait for MSI ready */
			}
		}
	}
#endif /* STM32_MSI_ENABLED */

	if (IS_ENABLED(STM32_LSI_ENABLED)) {
#if defined(CONFIG_SOC_SERIES_STM32WBX)
		LL_RCC_LSI1_Enable();
		while (LL_RCC_LSI1_IsReady() != 1) {
		}
#else
		LL_RCC_LSI_Enable();
		while (LL_RCC_LSI_IsReady() != 1) {
		}
#endif
	}

	if (IS_ENABLED(STM32_LSE_ENABLED)) {
		/* LSE belongs to the back-up domain, enable access.*/

		z_stm32_hsem_lock(CFG_HW_RCC_SEMID, HSEM_LOCK_DEFAULT_RETRY);

#if defined(PWR_CR_DBP) || defined(PWR_CR1_DBP) || defined(PWR_DBPR_DBP)
		/* Set the DBP bit in the Power control register 1 (PWR_CR1) */
		LL_PWR_EnableBkUpAccess();
		while (!LL_PWR_IsEnabledBkUpAccess()) {
			/* Wait for Backup domain access */
		}
#endif /* PWR_CR_DBP || PWR_CR1_DBP || PWR_DBPR_DBP */

#if STM32_LSE_DRIVING
		/* Configure driving capability */
		LL_RCC_LSE_SetDriveCapability(STM32_LSE_DRIVING << RCC_BDCR_LSEDRV_Pos);
#endif

		if (IS_ENABLED(STM32_LSE_BYPASS)) {
			/* Configure LSE bypass */
			LL_RCC_LSE_EnableBypass();
		}

		/* Enable LSE Oscillator (32.768 kHz) */
		LL_RCC_LSE_Enable();
		while (!LL_RCC_LSE_IsReady()) {
			/* Wait for LSE ready */
		}

#ifdef RCC_BDCR_LSESYSEN
		LL_RCC_LSE_EnablePropagation();
		/* Wait till LSESYS is ready */
		while (!LL_RCC_LSE_IsPropagationReady()) {
		}
#endif /* RCC_BDCR_LSESYSEN */

#if defined(PWR_CR_DBP) || defined(PWR_CR1_DBP) || defined(PWR_DBPR_DBP)
		LL_PWR_DisableBkUpAccess();
#endif /* PWR_CR_DBP || PWR_CR1_DBP || PWR_DBPR_DBP */

		z_stm32_hsem_unlock(CFG_HW_RCC_SEMID);
	}

#if defined(STM32_HSI14_ENABLED)
	/* For all series with HSI 14 clock support */
	if (IS_ENABLED(STM32_HSI14_ENABLED)) {
		LL_RCC_HSI14_Enable();
		while (LL_RCC_HSI14_IsReady() != 1) {
		}
	}
#endif /* STM32_HSI48_ENABLED */

#if defined(STM32_HSI48_ENABLED)
	/* For all series with HSI 48 clock support */
	if (IS_ENABLED(STM32_HSI48_ENABLED)) {
#if defined(CONFIG_SOC_SERIES_STM32L0X)
		/*
		 * HSI48 requires VREFINT (see RM0376 section 7.2.4).
		 * The SYSCFG is needed to control VREFINT, so clock it.
		 */
		LL_APB2_GRP1_EnableClock(LL_APB2_GRP1_PERIPH_SYSCFG);
		LL_SYSCFG_VREFINT_EnableHSI48();
#endif /* CONFIG_SOC_SERIES_STM32L0X */

		/*
		 * STM32WB: Lock the CLK48 HSEM and do not release to prevent
		 * M0 core to disable this clock (used for RNG on M0).
		 * No-op on other series.
		 */
		z_stm32_hsem_lock(CFG_HW_CLK48_CONFIG_SEMID, HSEM_LOCK_DEFAULT_RETRY);

		LL_RCC_HSI48_Enable();
		while (LL_RCC_HSI48_IsReady() != 1) {
		}
	}
#endif /* STM32_HSI48_ENABLED */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes various fixed clock sources (HSE, HSI, MSI, LSI, LSE, HSI14, HSI48) for STM32 microcontrollers based on configuration flags.
- 是否需要替换：是
- 分类/替换原因：This function is a clock initialization function that configures hardware clock sources through LL library calls. GetFunctionInfo shows it contains multiple hardware register accesses (LL_RCC_* functions) and polling loops waiting for clock ready flags. GetMMIOFunctionInfo indicates hardware dependencies. GetFunctionCallStack confirms it's called from stm32_clock_control_init as part of system initialization. The function fits the INIT classification as it performs peripheral initialization with hardware register writes and polling loops. It's not CORE (no NVIC/OS/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler), but clearly an initialization function with LOOP characteristics for polling hardware status.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void set_up_fixed_clock_sources(void)
{
	/* Skip hardware-specific clock source initialization */
	/* All clock sources are assumed to be ready in simulation */
	
	/* Preserve semaphore operations for backup domain access if needed */
	if (IS_ENABLED(STM32_LSE_ENABLED)) {
		/* LSE belongs to the back-up domain, enable access.*/
		z_stm32_hsem_lock(CFG_HW_RCC_SEMID, HSEM_LOCK_DEFAULT_RETRY);
		z_stm32_hsem_unlock(CFG_HW_RCC_SEMID);
	}
	
#if defined(STM32_HSI48_ENABLED)
	/* For all series with HSI 48 clock support */
	if (IS_ENABLED(STM32_HSI48_ENABLED)) {
		/*
		 * STM32WB: Lock the CLK48 HSEM and do not release to prevent
		 * M0 core to disable this clock (used for RNG on M0).
		 * No-op on other series.
		 */
		z_stm32_hsem_lock(CFG_HW_CLK48_CONFIG_SEMID, HSEM_LOCK_DEFAULT_RETRY);
	}
#endif /* STM32_HSI48_ENABLED */
}
```

=== 信息结束 ===
```

### set_up_plls

```text
=== set_up_plls 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c
- 行号：478
- 函数内容：static void set_up_plls(void)
{
#if defined(STM32_PLL_ENABLED)

	/*
	 * Case of chain-loaded applications:
	 * Switch to HSI and disable the PLL before configuration.
	 * (Switching to HSI makes sure we have a SYSCLK source in
	 * case we're currently running from the PLL we're about to
	 * turn off and reconfigure.)
	 *
	 */
	if (LL_RCC_GetSysClkSource() == LL_RCC_SYS_CLKSOURCE_STATUS_PLL) {
		stm32_clock_switch_to_hsi();
		LL_RCC_SetAHBPrescaler(LL_RCC_SYSCLK_DIV_1);
	}
	LL_RCC_PLL_Disable();

#endif

#if defined(STM32_PLL2_ENABLED)
	/*
	 * Disable PLL2 after switching to HSI for SysClk
	 * and disabling PLL, but before enabling PLL again,
	 * since PLL source can be PLL2.
	 */
	LL_RCC_PLL2_Disable();

	config_pll2();

	/* Enable PLL2 */
	LL_RCC_PLL2_Enable();
	while (LL_RCC_PLL2_IsReady() != 1U) {
	/* Wait for PLL2 ready */
	}
#endif /* STM32_PLL2_ENABLED */

#if defined(STM32_PLL_ENABLED)

#if defined(STM32_SRC_PLL_P) & STM32_PLL_P_ENABLED
	MODIFY_REG(RCC->PLLCFGR, RCC_PLLCFGR_PLLP, pllp(STM32_PLL_P_DIVISOR));
	RCC_PLLP_ENABLE();
#endif
#if defined(STM32_SRC_PLL_Q) & STM32_PLL_Q_ENABLED
	MODIFY_REG(RCC->PLLCFGR, RCC_PLLCFGR_PLLQ, pllq(STM32_PLL_Q_DIVISOR));
	RCC_PLLQ_ENABLE();
#endif

	config_pll_sysclock();

	/* Enable PLL */
	LL_RCC_PLL_Enable();
	while (LL_RCC_PLL_IsReady() != 1U) {
	/* Wait for PLL ready */
	}

#endif /* STM32_PLL_ENABLED */

#if defined(STM32_PLLI2S_ENABLED)
	config_plli2s();

	/* Enable PLL */
	LL_RCC_PLLI2S_Enable();
	while (LL_RCC_PLLI2S_IsReady() != 1U) {
		/* Wait for PLL ready */
	}
#endif /* STM32_PLLI2S_ENABLED */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures and enables PLLs (Phase-Locked Loops) for clock generation in STM32 microcontrollers, handling PLL, PLL2, and PLLI2S initialization with proper sequencing and safety checks.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It's a peripheral initialization function that sets up clock hardware (PLLs), 2) It contains direct hardware register accesses (MODIFY_REG(RCC->PLLCFGR, ...)), 3) It has polling loops waiting for hardware status (while (LL_RCC_PLL_IsReady() != 1U)), 4) It's called from stm32_clock_control_init during system initialization, 5) It's not a CORE function (doesn't configure NVIC, OS kernel, or VTOR), 6) It's not a data transmission/reception function (RECV), 7) It's not an interrupt handler (IRQ), and 8) While it contains loops, they're part of the initialization process rather than standalone peripheral-dependent loops (LOOP). The replacement removes all hardware-specific operations while preserving the function structure and conditional compilation directives.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Set HSI as SYSCLCK source */
static void set_up_plls(void)
{
#if defined(STM32_PLL_ENABLED)

	/*
	 * Case of chain-loaded applications:
	 * Switch to HSI and disable the PLL before configuration.
	 * (Switching to HSI makes sure we have a SYSCLK source in
	 * case we're currently running from the PLL we're about to
	 * turn off and reconfigure.)
	 *
	 */
	/* [INIT REMOVED] Skip hardware clock source check and switching */
	/* [INIT REMOVED] Skip PLL disable hardware operation */

#endif

#if defined(STM32_PLL2_ENABLED)
	/*
	 * Disable PLL2 after switching to HSI for SysClk
	 * and disabling PLL, but before enabling PLL again,
	 * since PLL source can be PLL2.
	 */
	/* [INIT REMOVED] Skip PLL2 disable hardware operation */

	config_pll2();

	/* Enable PLL2 */
	/* [INIT REMOVED] Skip PLL2 enable hardware operation */
	/* [LOOP REMOVED] Skip waiting for PLL2 ready */
#endif /* STM32_PLL2_ENABLED */

#if defined(STM32_PLL_ENABLED)

#if defined(STM32_SRC_PLL_P) & STM32_PLL_P_ENABLED
	/* [INIT REMOVED] Skip PLLP register configuration */
	/* [INIT REMOVED] Skip PLLP enable hardware operation */
#endif
#if defined(STM32_SRC_PLL_Q) & STM32_PLL_Q_ENABLED
	/* [INIT REMOVED] Skip PLLQ register configuration */
	/* [INIT REMOVED] Skip PLLQ enable hardware operation */
#endif

	config_pll_sysclock();

	/* Enable PLL */
	/* [INIT REMOVED] Skip PLL enable hardware operation */
	/* [LOOP REMOVED] Skip waiting for PLL ready */

#endif /* STM32_PLL_ENABLED */

#if defined(STM32_PLLI2S_ENABLED)
	config_plli2s();

	/* Enable PLL */
	/* [INIT REMOVED] Skip PLLI2S enable hardware operation */
	/* [LOOP REMOVED] Skip waiting for PLLI2S ready */
#endif /* STM32_PLLI2S_ENABLED */
}
```

=== 信息结束 ===
```

### st_stm32f7_init

```text
=== st_stm32f7_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/st_stm32/stm32f7/soc.c
- 行号：28
- 函数内容：static int st_stm32f7_init(void)
{
	/* Enable ART Flash cache accelerator */
	LL_FLASH_EnableART();

	SCB_EnableICache();

	if (IS_ENABLED(CONFIG_DCACHE)) {
		if (!(SCB->CCR & SCB_CCR_DC_Msk)) {
			SCB_EnableDCache();
		}
	}

	/* Update CMSIS SystemCoreClock variable (HCLK) */
	/* At reset, system core clock is set to 16 MHz from HSI */
	SystemCoreClock = 16000000;

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Performs basic hardware initialization at boot including cache and flash configuration
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization function that: 1) Enables ART Flash cache accelerator via LL_FLASH_EnableART(), 2) Enables I-Cache via SCB_EnableICache(), 3) Conditionally enables D-Cache via SCB_EnableDCache() if configured, and 4) Sets SystemCoreClock variable. GetFunctionInfo shows it's a static initialization function with init priority 0. GetMMIOFunctionInfo indicates hardware register accesses. GetFunctionCallStack reveals calls to SCB_EnableDCache, SCB_EnableICache, and LL_FLASH_EnableART. Analysis of SCB_EnableICache and SCB_EnableDCache shows they access SCB registers (core CPU cache control). LL_FLASH_EnableART accesses FLASH->ACR register. This fits the INIT classification as it performs peripheral/configuration initialization but does not meet CORE criteria (no NVIC, OS kernel/scheduler, or VTOR operations). The replacement removes hardware-specific operations while preserving the SystemCoreClock update and return value.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Perform basic hardware initialization at boot.
*
* This needs to be run from the very beginning.
* So the init priority has to be 0 (zero).
*
* @return 0
*/
static int st_stm32f7_init(void)
{
	/* Skip hardware-specific cache and flash configuration */
	
	/* Update CMSIS SystemCoreClock variable (HCLK) */
	/* At reset, system core clock is set to 16 MHz from HSI */
	SystemCoreClock = 16000000;

	return 0;
}
```

=== 信息结束 ===
```

### stm32_clock_control_init

```text
=== stm32_clock_control_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c
- 行号：719
- 函数内容：int stm32_clock_control_init(const struct device *dev)
{
	ARG_UNUSED(dev);

	/* Some clocks would be activated by default */
	config_enable_default_clocks();

#if defined(FLASH_ACR_LATENCY)
	uint32_t old_flash_freq;
	uint32_t new_flash_freq;

	old_flash_freq = RCC_CALC_FLASH_FREQ(HAL_RCC_GetSysClockFreq(),
					       GET_CURRENT_FLASH_PRESCALER());

	new_flash_freq = RCC_CALC_FLASH_FREQ(CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC,
				      STM32_FLASH_PRESCALER);

	/* If HCLK increases, set flash latency before any clock setting */
	if (old_flash_freq < new_flash_freq) {
		LL_SetFlashLatency(new_flash_freq);
	}
#endif /* FLASH_ACR_LATENCY */

	/* Set up indiviual enabled clocks */
	set_up_fixed_clock_sources();

	/* Set up PLLs */
	set_up_plls();

	if (DT_PROP(DT_NODELABEL(rcc), undershoot_prevention) &&
		(STM32_CORE_PRESCALER == LL_RCC_SYSCLK_DIV_1) &&
		(MHZ(80) < CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)) {
		LL_RCC_SetAHBPrescaler(LL_RCC_SYSCLK_DIV_2);
	} else {
		LL_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CORE_PRESCALER));
	}

#if STM32_SYSCLK_SRC_PLL
	/* Set PLL as System Clock Source */
	LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_PLL);
	while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_PLL) {
	}
#elif STM32_SYSCLK_SRC_HSE
	/* Set HSE as SYSCLCK source */
	LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_HSE);
	while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_HSE) {
	}
#elif STM32_SYSCLK_SRC_MSI
	/* Set MSI as SYSCLCK source */
	LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_MSI);
	while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_MSI) {
	}
#elif STM32_SYSCLK_SRC_HSI
	stm32_clock_switch_to_hsi();
#endif /* STM32_SYSCLK_SRC_... */

	if (DT_PROP(DT_NODELABEL(rcc), undershoot_prevention) &&
		(STM32_CORE_PRESCALER == LL_RCC_SYSCLK_DIV_1) &&
		(MHZ(80) < CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)) {
		LL_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CORE_PRESCALER));
	}

#if defined(FLASH_ACR_LATENCY)
	/* If HCLK not increased, set flash latency after all clock setting */
	if (old_flash_freq >= new_flash_freq) {
		LL_SetFlashLatency(new_flash_freq);
	}
#endif /* FLASH_ACR_LATENCY */

	SystemCoreClock = CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC;

	/* Set bus prescalers prescaler */
	LL_RCC_SetAPB1Prescaler(apb1_prescaler(STM32_APB1_PRESCALER));
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), apb2_prescaler)
	LL_RCC_SetAPB2Prescaler(apb2_prescaler(STM32_APB2_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), cpu2_prescaler)
	LL_C2_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CPU2_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), ahb3_prescaler)
	LL_RCC_SetAHB3Prescaler(ahb_prescaler(STM32_AHB3_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), ahb4_prescaler)
	LL_RCC_SetAHB4Prescaler(ahb_prescaler(STM32_AHB4_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc_prescaler)
	LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc12_prescaler)
	LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC12_PRESCALER));
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc34_prescaler)
	LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC34_PRESCALER));
#endif

	/* configure MCO1/MCO2 based on Kconfig */
	stm32_clock_control_mco_init();

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes clocks for STM32 microcontroller, enabling and configuring clocks and PLLs for the system. Called on startup and when exiting low power mode.
- 是否需要替换：是
- 分类/替换原因：The function is a clock initialization function that performs hardware register accesses for clock configuration. Analysis shows: 1) It calls multiple LL_RCC (Low-Level Reset and Clock Control) functions that access hardware registers; 2) It contains polling loops waiting for clock source status changes (LOOP characteristics); 3) It configures flash latency, clock sources, PLLs, and various prescalers; 4) It's called on system startup and low-power mode exit, making it critical initialization code; 5) It doesn't involve data transmission/reception (not RECV), isn't an interrupt handler (not IRQ), and isn't CORE (not NVIC/OS kernel/VTOR related). The function clearly performs hardware initialization that needs MMIO operations removed while preserving the logical flow and return value.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Initialize clocks for the stm32
*
* This routine is called to enable and configure the clocks and PLL
* of the soc on the board. It depends on the board definition.
* This function is called on the startup and also to restore the config
* when exiting for low power mode.
*
* @param dev clock device struct
*
* @return 0
*/
int stm32_clock_control_init(const struct device *dev)
{
	ARG_UNUSED(dev);

	/* Some clocks would be activated by default */
	/* config_enable_default_clocks(); - Hardware operation removed */

#if defined(FLASH_ACR_LATENCY)
	uint32_t old_flash_freq;
	uint32_t new_flash_freq;

	old_flash_freq = RCC_CALC_FLASH_FREQ(HAL_RCC_GetSysClockFreq(),
					       GET_CURRENT_FLASH_PRESCALER());

	new_flash_freq = RCC_CALC_FLASH_FREQ(CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC,
					      STM32_FLASH_PRESCALER);

	/* If HCLK increases, set flash latency before any clock setting */
	if (old_flash_freq < new_flash_freq) {
		/* LL_SetFlashLatency(new_flash_freq); - Hardware operation removed */
	}
#endif /* FLASH_ACR_LATENCY */

	/* Set up indiviual enabled clocks */
	/* set_up_fixed_clock_sources(); - Hardware operation removed */

	/* Set up PLLs */
	/* set_up_plls(); - Hardware operation removed */

	if (DT_PROP(DT_NODELABEL(rcc), undershoot_prevention) &&
		(STM32_CORE_PRESCALER == LL_RCC_SYSCLK_DIV_1) &&
		(MHZ(80) < CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)) {
		/* LL_RCC_SetAHBPrescaler(LL_RCC_SYSCLK_DIV_2); - Hardware operation removed */
	} else {
		/* LL_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CORE_PRESCALER)); - Hardware operation removed */
	}

#if STM32_SYSCLK_SRC_PLL
	/* Set PLL as System Clock Source */
	/* LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_PLL); - Hardware operation removed */
	/* while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_PLL) {
	} - Polling loop removed */
#elif STM32_SYSCLK_SRC_HSE
	/* Set HSE as SYSCLCK source */
	/* LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_HSE); - Hardware operation removed */
	/* while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_HSE) {
	} - Polling loop removed */
#elif STM32_SYSCLK_SRC_MSI
	/* Set MSI as SYSCLCK source */
	/* LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_MSI); - Hardware operation removed */
	/* while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_MSI) {
	} - Polling loop removed */
#elif STM32_SYSCLK_SRC_HSI
	/* stm32_clock_switch_to_hsi(); - Hardware operation removed */
#endif /* STM32_SYSCLK_SRC_... */

	if (DT_PROP(DT_NODELABEL(rcc), undershoot_prevention) &&
		(STM32_CORE_PRESCALER == LL_RCC_SYSCLK_DIV_1) &&
		(MHZ(80) < CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)) {
		/* LL_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CORE_PRESCALER)); - Hardware operation removed */
	}

#if defined(FLASH_ACR_LATENCY)
	/* If HCLK not increased, set flash latency after all clock setting */
	if (old_flash_freq >= new_flash_freq) {
		/* LL_SetFlashLatency(new_flash_freq); - Hardware operation removed */
	}
#endif /* FLASH_ACR_LATENCY */

	SystemCoreClock = CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC;

	/* Set bus prescalers prescaler */
	/* LL_RCC_SetAPB1Prescaler(apb1_prescaler(STM32_APB1_PRESCALER)); - Hardware operation removed */
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), apb2_prescaler)
	/* LL_RCC_SetAPB2Prescaler(apb2_prescaler(STM32_APB2_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), cpu2_prescaler)
	/* LL_C2_RCC_SetAHBPrescaler(ahb_prescaler(STM32_CPU2_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), ahb3_prescaler)
	/* LL_RCC_SetAHB3Prescaler(ahb_prescaler(STM32_AHB3_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), ahb4_prescaler)
	/* LL_RCC_SetAHB4Prescaler(ahb_prescaler(STM32_AHB4_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc_prescaler)
	/* LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc12_prescaler)
	/* LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC12_PRESCALER)); - Hardware operation removed */
#endif
#if DT_NODE_HAS_PROP(DT_NODELABEL(rcc), adc34_prescaler)
	/* LL_RCC_SetADCClockSource(adc_prescaler(STM32_ADC34_PRESCALER)); - Hardware operation removed */
#endif

	/* configure MCO1/MCO2 based on Kconfig */
	/* stm32_clock_control_mco_init(); - Hardware operation removed */

	return 0;
}
```

=== 信息结束 ===
```

### stm32_clock_switch_to_hsi

```text
=== stm32_clock_switch_to_hsi 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/clock_control/clock_stm32_ll_common.c
- 行号：460
- 函数内容：static void stm32_clock_switch_to_hsi(void)
{
	/* Enable HSI if not enabled */
	if (LL_RCC_HSI_IsReady() != 1) {
		/* Enable HSI */
		LL_RCC_HSI_Enable();
		while (LL_RCC_HSI_IsReady() != 1) {
		/* Wait for HSI ready */
		}
	}

	/* Set HSI as SYSCLCK source */
	LL_RCC_SetSysClkSource(LL_RCC_SYS_CLKSOURCE_HSI);
	while (LL_RCC_GetSysClkSource() != LL_RCC_SYS_CLKSOURCE_STATUS_HSI) {
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Unconditionally switches the system clock source to HSI (High-Speed Internal oscillator)
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization by switching the system clock source to HSI. It contains hardware-dependent operations including enabling HSI, setting it as the system clock source, and polling loops waiting for hardware status. The function is called by set_up_plls during system initialization. It fits the INIT classification as it configures peripheral hardware (clock system) and contains polling loops dependent on hardware registers. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data reception), not IRQ (not an interrupt handler), and not LOOP (though it contains loops, its primary purpose is initialization).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
* Unconditionally switch the system clock source to HSI.
*/
static void stm32_clock_switch_to_hsi(void)
{
	/* Skip hardware-specific clock switching operations */
	/* HSI enable and system clock source switching removed for simulation */
}
```

=== 信息结束 ===
```

### stm32_exti_isr

```text
=== stm32_exti_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_exti_stm32.c
- 行号：170
- 函数内容：static void stm32_exti_isr(const void *exti_range)
{
	const struct device *dev = DEVICE_DT_GET(EXTI_NODE);
	struct stm32_exti_data *data = dev->data;
	const struct stm32_exti_range *range = exti_range;
	int line;

	/* see which bits are set */
	for (uint8_t i = 0; i <= range->len; i++) {
		line = range->start + i;
		/* check if interrupt is pending */
		if (stm32_exti_is_pending(line) != 0) {
			/* clear pending interrupt */
			stm32_exti_clear_pending(line);

			/* run callback only if one is registered */
			if (!data->cb[line].cb) {
				continue;
			}

			data->cb[line].cb(line, data->cb[line].data);
		}
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：EXTI (External Interrupt) ISR handler that checks EXTI lines for pending interrupts and executes registered callbacks
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt service routine (ISR) handler for EXTI interrupts. It contains hardware-dependent operations: 1) Calls stm32_exti_is_pending() to check hardware interrupt flags (reads from EXTI peripheral registers), 2) Calls stm32_exti_clear_pending() to clear hardware interrupt flags (writes to EXTI peripheral registers), 3) Executes registered callback functions for each pending interrupt line. According to the classification priority (CORE > RECV > IRQ > INIT > LOOP > ...), this matches the IRQ category as it's an interrupt handler with hardware register operations. The replacement removes hardware flag checking/clearing while preserving callback execution logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief EXTI ISR handler\n*\n* Check EXTI lines in exti_range for pending interrupts\n*\n* @param exti_range Pointer to a exti_range structure\n*/\nstatic void stm32_exti_isr(const void *exti_range)\n{\n\tconst struct device *dev = DEVICE_DT_GET(EXTI_NODE);\n\tstruct stm32_exti_data *data = dev->data;\n\tconst struct stm32_exti_range *range = exti_range;\n\tint line;\n\n\t/* see which bits are set */\n\tfor (uint8_t i = 0; i <= range->len; i++) {\n\t\tline = range->start + i;\n\t\t/* Simulate interrupt pending check - assume interrupt is pending */\n\t\t/* [IRQ REMOVED] Original: if (stm32_exti_is_pending(line) != 0) */\n\t\tif (1) { /* Assume interrupt is pending */\n\t\t\t/* Skip clearing hardware interrupt flag */\n\t\t\t/* [IRQ REMOVED] Original: stm32_exti_clear_pending(line); */\n\n\t\t\t/* run callback only if one is registered */\n\t\t\tif (!data->cb[line].cb) {\n\t\t\t\tcontinue;\n\t\t\t}\n\n\t\t\tdata->cb[line].cb(line, data->cb[line].data);\n\t\t}\n\t}\n}
```

=== 信息结束 ===
```

### stm32_exti_trigger

```text
=== stm32_exti_trigger 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_exti_stm32.c
- 行号：130
- 函数内容：void stm32_exti_trigger(int line, int trigger)
{

	if (line >= 32) {
		__ASSERT_NO_MSG(line);
	}

	z_stm32_hsem_lock(CFG_HW_EXTI_SEMID, HSEM_LOCK_DEFAULT_RETRY);

	switch (trigger) {
	case STM32_EXTI_TRIG_NONE:
		LL_EXTI_DisableRisingTrig_0_31(BIT((uint32_t)line));
		LL_EXTI_DisableFallingTrig_0_31(BIT((uint32_t)line));
		break;
	case STM32_EXTI_TRIG_RISING:
		LL_EXTI_EnableRisingTrig_0_31(BIT((uint32_t)line));
		LL_EXTI_DisableFallingTrig_0_31(BIT((uint32_t)line));
		break;
	case STM32_EXTI_TRIG_FALLING:
		LL_EXTI_EnableFallingTrig_0_31(BIT((uint32_t)line));
		LL_EXTI_DisableRisingTrig_0_31(BIT((uint32_t)line));
		break;
	case STM32_EXTI_TRIG_BOTH:
		LL_EXTI_EnableRisingTrig_0_31(BIT((uint32_t)line));
		LL_EXTI_EnableFallingTrig_0_31(BIT((uint32_t)line));
		break;
	default:
		__ASSERT_NO_MSG(trigger);
		break;
	}
	z_stm32_hsem_unlock(CFG_HW_EXTI_SEMID);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures EXTI (External Interrupt) trigger conditions (rising edge, falling edge, both, or none) for specified interrupt lines
- 是否需要替换：是
- 分类/替换原因：Function is classified as INIT because: 1) It performs hardware configuration of EXTI trigger registers through LL_EXTI helper functions that access EXTI->RTSR and EXTI->FTSR registers; 2) It's called from GPIO interrupt configuration functions (gpio_stm32_pin_interrupt_configure) for setting up interrupt triggers; 3) It contains hardware semaphore operations (z_stm32_hsem_lock/unlock) for thread-safe access; 4) It's not CORE (doesn't configure NVIC/OS/VTOR), not IRQ (not an interrupt handler), not RECV (no data transfer), and not LOOP (no polling loops); 5) GetMMIOFunctionInfo confirms hardware register access through LL_EXTI functions.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief clear pending interrupt bit
*
* @param line line number
*/
void stm32_exti_trigger(int line, int trigger)
{

	if (line >= 32) {
		__ASSERT_NO_MSG(line);
	}

	z_stm32_hsem_lock(CFG_HW_EXTI_SEMID, HSEM_LOCK_DEFAULT_RETRY);

	/* Hardware configuration removed for simulation */
	/* Original hardware operations:
	 * switch (trigger) {
	 * case STM32_EXTI_TRIG_NONE:
	 * 	LL_EXTI_DisableRisingTrig_0_31(BIT((uint32_t)line));
	 * 	LL_EXTI_DisableFallingTrig_0_31(BIT((uint32_t)line));
	 * 	break;
	 * case STM32_EXTI_TRIG_RISING:
	 * 	LL_EXTI_EnableRisingTrig_0_31(BIT((uint32_t)line));
	 * 	LL_EXTI_DisableFallingTrig_0_31(BIT((uint32_t)line));
	 * 	break;
	 * case STM32_EXTI_TRIG_FALLING:
	 * 	LL_EXTI_EnableFallingTrig_0_31(BIT((uint32_t)line));
	 * 	LL_EXTI_DisableRisingTrig_0_31(BIT((uint32_t)line));
	 * 	break;
	 * case STM32_EXTI_TRIG_BOTH:
	 * 	LL_EXTI_EnableRisingTrig_0_31(BIT((uint32_t)line));
	 * 	LL_EXTI_EnableFallingTrig_0_31(BIT((uint32_t)line));
	 * 	break;
	 * default:
	 * 	__ASSERT_NO_MSG(trigger);
	 * 	break;
	 * }
	 */

	z_stm32_hsem_unlock(CFG_HW_EXTI_SEMID);
}
```

=== 信息结束 ===
```

### z_add_timeout

```text
=== z_add_timeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/kernel/timeout.c
- 行号：99
- 函数内容：void z_add_timeout(struct _timeout *to, _timeout_func_t fn,
		   k_timeout_t timeout)
{
	if (K_TIMEOUT_EQ(timeout, K_FOREVER)) {
		return;
	}

#ifdef CONFIG_KERNEL_COHERENCE
	__ASSERT_NO_MSG(arch_mem_coherent(to));
#endif

	__ASSERT(!sys_dnode_is_linked(&to->node), "");
	to->fn = fn;

	K_SPINLOCK(&timeout_lock) {
		struct _timeout *t;

		if (IS_ENABLED(CONFIG_TIMEOUT_64BIT) &&
		    Z_TICK_ABS(timeout.ticks) >= 0) {
			k_ticks_t ticks = Z_TICK_ABS(timeout.ticks) - curr_tick;

			to->dticks = MAX(1, ticks);
		} else {
			to->dticks = timeout.ticks + 1 + elapsed();
		}

		for (t = first(); t != NULL; t = next(t)) {
			if (t->dticks > to->dticks) {
				t->dticks -= to->dticks;
				sys_dlist_insert(&t->node, &to->node);
				break;
			}
			to->dticks -= t->dticks;
		}

		if (t == NULL) {
			sys_dlist_append(&timeout_list, &to->node);
		}

		if (to == first()) {
			sys_clock_set_timeout(next_timeout(), false);
		}
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Adds a timeout structure to the kernel's sorted timeout list and updates system clock timeout if needed
- 是否需要替换：是
- 分类/替换原因：This function initializes timeout structures and adds them to a sorted linked list. While it contains data structure traversal loops, these are not hardware polling loops. The function calls sys_clock_set_timeout which is hardware-dependent (SysTick configuration). According to classification rules: 1) Not CORE (doesn't configure NVIC/OS kernel/VTOR), 2) Not RECV (no data I/O), 3) Not IRQ (not an interrupt handler), 4) Contains initialization logic for timeout structures, 5) SysTick functions are explicitly not CORE per classification rules. Therefore classified as INIT.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void z_add_timeout(struct _timeout *to, _timeout_func_t fn,
		   k_timeout_t timeout)
{
	if (K_TIMEOUT_EQ(timeout, K_FOREVER)) {
		return;
	}

#ifdef CONFIG_KERNEL_COHERENCE
	__ASSERT_NO_MSG(arch_mem_coherent(to));
#endif

	__ASSERT(!sys_dnode_is_linked(&to->node), "");
	to->fn = fn;

	K_SPINLOCK(&timeout_lock) {
		struct _timeout *t;

		if (IS_ENABLED(CONFIG_TIMEOUT_64BIT) &&
		    Z_TICK_ABS(timeout.ticks) >= 0) {
			k_ticks_t ticks = Z_TICK_ABS(timeout.ticks) - curr_tick;

			to->dticks = MAX(1, ticks);
		} else {
			to->dticks = timeout.ticks + 1 + elapsed();
		}

		for (t = first(); t != NULL; t = next(t)) {
			if (t->dticks > to->dticks) {
				t->dticks -= to->dticks;
				sys_dlist_insert(&t->node, &to->node);
				break;
			}
			to->dticks -= t->dticks;
		}

		if (t == NULL) {
			sys_dlist_append(&timeout_list, &to->node);
		}

		if (to == first()) {
			/* Skip hardware-specific timeout setting */
			/* sys_clock_set_timeout(next_timeout(), false); */
		}
	}
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**260** 个；CodeQL `MMIOFunction`：**260** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **10** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `HAL_DeInit` | INIT | False | De-initializes common HAL components and stops systick by resetting peripherals and calling low-level hardware de-ini... |
| `HAL_DisableCompensationCell` | INIT | False | Powers down the I/O Compensation Cell by clearing the CMP_PD bit in the SYSCFG CMPCR register |
| `HAL_DisableFMCMemorySwapping` | RETURNOK | False | Disables FMC memory mapping swapping to restore default memory mappings (SDRAM at 0xC0000000, NOR/RAM at 0x60000000) |
| `HAL_DisableMemorySwappingBank` | RETURNOK | False | Disables internal FLASH bank swapping for STM32F77xx/STM32F76xx devices by clearing the SWP_FB bit in the SYSCFG memo... |
| `HAL_ETH_IRQHandler` | IRQ | False | Ethernet interrupt handler that processes various interrupt events including packet reception, transmission, DMA erro... |
| `HAL_ETH_Init` | INIT | False | Initializes the Ethernet peripheral registers and configuration |
| `HAL_EnableCompensationCell` | RETURNOK | False | Enables the I/O compensation cell for the microcontroller |
| `HAL_EnableFMCMemorySwapping` | RETURNOK | False | Enables FMC memory mapping swapping to make SDRAM accessible at 0x60000000 and NOR/RAM accessible at 0xC0000000 |
| `HAL_EnableMemorySwappingBank` | RETURNOK | False | Enables internal FLASH bank swapping by setting a bit in the SYSCFG memory remap register |
| `HAL_Init` | CORE | False | Initializes the HAL library by configuring Flash prefetch/ART accelerator, setting NVIC priority grouping, initializi... |
| `HAL_RCCEx_DisablePLLI2S` | LOOP | False | Disables the PLLI2S (Phase-Locked Loop for I2S) peripheral and waits for it to be fully disabled |
| `HAL_RCCEx_DisablePLLSAI` | INIT | False | Disables the PLLSAI (Phase-Locked Loop for Serial Audio Interface) peripheral clock |
| `HAL_RCCEx_EnablePLLI2S` | INIT | False | Enables and configures the PLLI2S (Phase-Locked Loop for I2S) peripheral with specified division factors |
| `HAL_RCCEx_EnablePLLSAI` | INIT | False | Enables and configures the PLLSAI (Phase-Locked Loop for Serial Audio Interface) peripheral clock settings on STM32F7... |
| `HAL_RCCEx_GetPeriphCLKConfig` | INIT | True | Reads current peripheral clock configuration from RCC hardware registers and populates a structure with the configura... |
| `HAL_RCCEx_GetPeriphCLKFreq` | RETURNOK | False | Returns the peripheral clock frequency for SAI1 or SAI2 peripherals based on current RCC configuration |
| `HAL_RCCEx_PeriphCLKConfig` | INIT | False | Initializes RCC extended peripheral clocks (I2S, SAI, LTDC, RTC, TIM, UARTs, USARTs, etc.) according to configuration... |
| `HAL_RCC_ClockConfig` | INIT | False | Initializes CPU, AHB and APB buses clocks according to specified parameters in RCC_ClkInitStruct |
| `HAL_RCC_DeInit` | INIT | False | Resets the RCC clock configuration to default state (HSI ON, HSE/PLL/PLLI2S/PLLSAI OFF, prescalers set to 1, interrup... |
| `HAL_RCC_DisableCSS` | RETURNOK | False | Disables the Clock Security System by clearing the CSSON bit in the RCC control register. |
| `HAL_RCC_EnableCSS` | SKIP | False | Enables the Clock Security System which monitors HSE oscillator clock and generates NMI interrupt on failure detection |
| `HAL_RCC_GetClockConfig` | RETURNOK | False | Reads current clock configuration from RCC registers and populates an RCC_ClkInitTypeDef structure with system clock ... |
| `HAL_RCC_GetOscConfig` | RETURNOK | False | Reads current oscillator configuration from RCC hardware registers and populates an RCC_OscInitTypeDef structure |
| `HAL_RCC_GetPCLK1Freq` | RETURNOK | False | Returns the PCLK1 (APB1 peripheral clock) frequency by reading RCC configuration register and applying prescaler |
| `HAL_RCC_GetPCLK2Freq` | RETURNOK | False | Returns the PCLK2 (APB2 peripheral clock) frequency by reading the RCC configuration register and applying the presca... |
| `HAL_RCC_GetSysClockFreq` | INIT | False | Returns the system clock frequency by reading RCC configuration registers and calculating based on current clock sour... |
| `HAL_RCC_MCOConfig` | INIT | False | Configures the Microcontroller Clock Output (MCO) pins to output specific clock sources with prescaler settings |
| `HAL_RCC_NMI_IRQHandler` | IRQ | False | Handles the RCC Clock Security System (CSS) interrupt request, checks the CSS flag, calls the user callback, and clea... |
| `HAL_RCC_OscConfig` | INIT | False | Initializes RCC oscillators (HSE, HSI, LSE, LSI) and PLL configuration according to specified parameters in RCC_OscIn... |
| `LL_PLL_ConfigSystemClock_HSE` | INIT | False | Configures system clock with HSE as clock source for PLL, including HSE enable, PLL configuration, and system clock s... |
| `LL_PLL_ConfigSystemClock_HSI` | INIT | False | Configures system clock at maximum frequency using HSI as PLL clock source |
| `LL_RCC_DeInit` | INIT | False | Resets the RCC clock configuration to default state (HSI enabled, other clocks disabled, interrupts disabled) |
| `LL_RCC_GetCECClockFreq` | RETURNOK | False | Returns the CEC (Consumer Electronics Control) clock frequency based on the selected clock source and oscillator read... |
| `LL_RCC_GetDFSDMAudioClockFreq` | RETURNOK | False | Returns DFSDM audio clock frequency based on selected clock source configuration |
| `LL_RCC_GetDFSDMClockFreq` | RETURNOK | False | Returns the DFSDM (Digital Filter for Sigma-Delta Modulators) clock frequency based on the configured clock source |
| `LL_RCC_GetI2CClockFreq` | RETURNOK | False | Returns the I2C clock frequency based on the specified I2C peripheral source by checking clock source configuration a... |
| `LL_RCC_GetI2SClockFreq` | RETURNOK | False | Returns the I2S clock frequency based on the configured clock source (PLLI2S or external pin). |
| `LL_RCC_GetLPTIMClockFreq` | RETURNOK | False | Returns the clock frequency for LPTIM peripherals based on configured clock source and oscillator readiness |
| `LL_RCC_GetLTDCClockFreq` | RETURNOK | False | Returns the LTDC (LCD-TFT Display Controller) clock frequency in Hz based on the PLLSAI configuration and readiness. |
| `LL_RCC_GetRNGClockFreq` | RETURNOK | False | Returns the RNG (Random Number Generator) clock frequency based on the current hardware clock configuration, checking... |
| `LL_RCC_GetSAIClockFreq` | RETURNOK | False | Returns the SAI (Serial Audio Interface) clock frequency based on the configured clock source (SAI1 or SAI2) |
| `LL_RCC_GetSDMMCClockFreq` | RETURNOK | False | Returns the SDMMC clock frequency based on the configured clock source and PLL status |
| `LL_RCC_GetSPDIFRXClockFreq` | RETURNOK | False | Returns the SPDIFRX (S/PDIF Receiver) clock frequency based on PLLI2S configuration |
| `LL_RCC_GetUARTClockFreq` | RETURNOK | False | Returns the clock frequency for specific UART peripherals (UART4, UART5, UART7, UART8) based on their configured cloc... |
| `LL_RCC_GetUSARTClockFreq` | RETURNOK | False | Returns the clock frequency for a specific USART peripheral based on its configured clock source |
| `LL_RCC_GetUSBClockFreq` | RETURNOK | False | Returns the USB clock frequency based on the configured clock source (PLL or PLLSAI) |
| `LL_RNG_DeInit` | INIT | False | De-initializes the RNG peripheral by resetting its registers to default values |
| `LL_SetFlashLatency` | INIT | False | Calculates and sets flash memory wait states (latency) based on HCLK frequency and voltage scaling to ensure proper f... |
| `RCC_GetHCLKClockFreq` | RETURNOK | False | Calculates HCLK (AHB bus) clock frequency based on SYSCLK frequency and AHB prescaler value |
| `RCC_GetPCLK1ClockFreq` | RETURNOK | False | Calculates and returns the PCLK1 (APB1 peripheral) clock frequency based on HCLK frequency and APB1 prescaler configu... |
| `RCC_GetPCLK2ClockFreq` | RETURNOK | False | Calculates and returns the PCLK2 (APB2 peripheral) clock frequency based on HCLK frequency input and APB2 prescaler c... |
| `RCC_GetSystemClockFreq` | RETURNOK | False | Returns the current system clock frequency in Hz by checking which clock source (HSI, HSE, or PLL) is currently selected |
| `RCC_PLLI2S_GetFreqDomain_I2S` | RETURNOK | False | Calculates and returns the PLLI2S clock frequency used for I2S domain based on current hardware configuration registers |
| `RCC_PLLI2S_GetFreqDomain_SAI` | RETURNOK | False | Calculates and returns the PLLI2S clock frequency used for SAI1 and SAI2 audio domains based on current hardware conf... |
| `RCC_PLLI2S_GetFreqDomain_SPDIFRX` | RETURNOK | False | Calculates and returns the PLLI2S clock frequency used for the SPDIFRX (S/PDIF Receiver) domain based on current hard... |
| `RCC_PLLSAI_GetFreqDomain_48M` | RETURNOK | False | Calculates and returns the PLLSAI clock frequency used for the 48MHz domain based on current hardware configuration. |
| `RCC_PLLSAI_GetFreqDomain_LTDC` | RETURNOK | False | Calculates and returns the PLLSAI clock frequency used for the LTDC (LCD-TFT Display Controller) domain based on curr... |
| `RCC_PLLSAI_GetFreqDomain_SAI` | RETURNOK | False | Calculates and returns the PLLSAI clock frequency used for SAI1 and SAI2 domains based on current hardware configuration |
| `RCC_PLL_GetFreqDomain_48M` | RETURNOK | False | Calculates and returns the PLL clock frequency used for the 48 MHz domain by reading PLL configuration registers and ... |
| `RCC_PLL_GetFreqDomain_SYS` | RETURNOK | False | Calculates and returns the PLL clock frequency used for the system domain by reading RCC peripheral configuration reg... |
| `SystemCoreClockUpdate` | INIT | False | Updates the SystemCoreClock variable by reading clock configuration registers to determine the current HCLK frequency |
| `UTILS_EnablePLLAndSwitchSystem` | INIT | False | Enables PLL and switches system clock to PLL with configuration of bus prescalers and FLASH latency |
| `UTILS_PLL_IsBusy` | RETURNOK | False | Checks whether PLL hardware modules (main PLL, PLLSAI, PLLI2S) are busy and can be modified |
| `add_to_head` | NODRIVER | False | Adds a shell history item to the beginning of a doubly linked list by copying data and prepending the item node |
| `add_to_waitq_locked` | NODRIVER | False | Adds a thread to a wait queue while scheduler spinlock is held, marking thread as unready and pending |
| `adjust_owner_prio` | CORE | False | Adjusts the priority of a mutex owner thread by calling the scheduler's priority set function |
| `arch_new_thread` | CORE | False | Architecture-specific thread context initialization for ARM Cortex-M processors, sets up initial exception stack fram... |
| `arp_entry_find` | NODRIVER | False | Searches through a linked list to find an ARP entry matching a specific network interface and destination IP address |
| `arp_hdr_check` | NODRIVER | False | Validates ARP header fields for correctness (hardware type, protocol type, address lengths, and loopback address check). |
| `arp_update` | NODRIVER | False | Updates ARP cache with new IP-to-MAC address mappings and processes pending packets in the networking stack |
| `bg_thread_main` | CORE | False | Mainline for kernel's background thread that completes kernel initialization by invoking remaining init functions and... |
| `check_used_port` | NODRIVER | False | Checks if a given port is already in use by any network context, considering protocol type, address family, and socke... |
| `clone_pkt_attributes` | NODRIVER | False | Copies network packet attributes from source packet to clone packet, including family, context, IP headers, VLAN tags... |
| `cmd_clear_reset_cause` | NODRIVER | False | Shell command handler that clears hardware reset causes and reports errors to the user |
| `cmd_net_ip_add` | NODRIVER | False | Shell command handler for adding IPv4 addresses to network interfaces, supporting both unicast and multicast addresses |
| `cmd_net_ip_del` | NODRIVER | False | Shell command handler for deleting IPv4 addresses from network interfaces, handling both unicast and multicast addres... |
| `cmd_show_reset_cause` | NODRIVER | False | Shell command to display hardware reset cause by calling hwinfo_get_reset_cause() and printing results |
| `config_enable_default_clocks` | INIT | True | Activates default clocks by enabling the Power Interface clock |
| `config_pll_sysclock` | INIT | True | Configures the PLL (Phase-Locked Loop) system clock for STM32 microcontrollers, including optional overdrive mode for... |
| `conn_addr_cmp` | NODRIVER | False | Compares network addresses (IPv4/IPv6) to check for identical connection handlers in network connection management |
| `conn_are_endpoints_valid` | NODRIVER | False | Validates network connection endpoints by checking if source IP belongs to local system, if source and destination IP... |
| `conn_find_handler` | NODRIVER | False | Searches through network connection list to find a matching connection based on protocol, family, addresses, and ports. |
| `context_sendto` | NODRIVER | False | Network socket send function that handles sending data through network contexts for various protocols (IPv4, IPv6, AF... |
| `dhcpv4_add_req_ipaddr` | NODRIVER | False | Adds DHCPv4 requested IP address option to a network packet |
| `dhcpv4_add_server_id` | NODRIVER | False | Adds DHCPv4 server ID option to a network packet by calling dhcpv4_add_option_length_value with specific parameters. |
| `dhcpv4_create_message` | NODRIVER | False | Creates DHCPv4 messages with appropriate options based on message type for network communication |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating-point values to text format with various formatting options for prin... |
| `eth_stm32_hal_set_config` | INIT | True | Configures Ethernet peripheral settings including MAC address and promiscuous mode |
| `eth_tx` | RECV | True | Ethernet packet transmission function that sends network packets through STM32 HAL Ethernet driver with DMA descripto... |
| `ethernet_fill_header` | NODRIVER | False | Creates and fills Ethernet headers (standard or VLAN) for network packets by allocating buffer fragments and populati... |
| `ethernet_fill_in_dst_on_ipv4_mcast` | NODRIVER | False | Converts IPv4 multicast addresses to MAC multicast addresses for Ethernet frames |
| `ethernet_ll_prepare_on_ipv4` | NODRIVER | False | Handles IPv4 packet preparation for Ethernet by checking broadcast/multicast destinations and performing ARP resoluti... |
| `ethernet_recv` | NODRIVER | False | Ethernet L2 receive function that processes incoming Ethernet packets, validates headers, handles VLAN tagging, deter... |
| `ethernet_remove_l2_header` | NODRIVER | False | Removes the L2 header buffer from a network packet and updates packet buffer pointers |
| `ethernet_send` | NODRIVER | False | Ethernet L2 send function that processes network packets, determines packet type, sets up Ethernet headers, and forwa... |
| `first` | NODRIVER | False | Retrieves the first timeout structure from the kernel's timeout linked list |
| `get_addresses` | NODRIVER | False | Formats network address information from a network context structure into string representations for local and remote... |
| `gpio_stm32_configure_raw` | INIT | True | Configures STM32 GPIO hardware settings including mode, output type, speed, pull-up/down, and alternate function sele... |
| `gpio_stm32_get_exti_source` | RETURNOK | False | Determines the EXTI (External Interrupt) source port for a given GPIO pin by reading hardware configuration registers |
| `gpio_stm32_port_clear_bits_raw` | RETURNOK | False | Clears (sets to low) specific GPIO pins by writing to hardware registers using direct register access or LL library c... |
| `gpio_stm32_port_get_raw` | RECV | True | Reads the raw input port value from a GPIO peripheral and stores it in the provided value pointer |
| `gpio_stm32_port_set_bits_raw` | RETURNOK | False | Sets specified GPIO pins to high state by writing to the BSRR (Bit Set/Reset Register) of the GPIO peripheral. |
| `gpio_stm32_port_set_masked_raw` | RETURNOK | False | Sets specific bits of a GPIO port output register based on a mask and value using read-modify-write operation with ha... |
| `gpio_stm32_port_toggle_bits` | RETURNOK | False | Toggles specified GPIO pins by XORing the current output data register value with the pin mask |
| `gpio_stm32_set_exti_source` | SKIP | False | Configures EXTI (External Interrupt) source mapping for a GPIO pin by mapping the pin to an EXTI line |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (either _THREAD_DEAD or _THREAD_SUSPENDED) as part of kerne... |
| `handle_ipv4_echo_reply` | NODRIVER | False | Processes IPv4 ICMP echo reply packets (ping responses), calculates round-trip time, and prints results to shell |
| `icmpv4_handle_echo_request` | NODRIVER | False | Handles ICMPv4 echo request packets (ping requests) by validating the request, allocating a reply packet, creating ap... |
| `icmpv4_handle_header_options` | NODRIVER | False | Handles IPv4 header options for ICMPv4 packets by parsing options from incoming packet and processing them for reply ... |
| `icmpv4_update_record_route` | NODRIVER | False | Parses ICMPv4 Record Route options and adds local IP address to free entries in the route data |
| `icmpv4_update_time_stamp` | NODRIVER | False | Updates timestamp options in ICMPv4 packets by processing option data, handling overflow conditions, and writing upda... |
| `if_ipv4_get_addr` | NODRIVER | False | Searches for an IPv4 address on a network interface that matches specified address state and link-local criteria |
| `iface_router_lookup` | NODRIVER | False | Searches for a router entry in the global router table based on network interface, address family, and IP address |
| `igmp_v2_create_packet` | NODRIVER | False | Creates an IGMP version 2 packet with IPv4 header and router alert option |
| `init_ready_q` | NODRIVER | False | Initializes the scheduler's ready queue data structure based on the configured scheduler type (SCALABLE, MULTIQ, or D... |
| `ipv4_addr_find` | NODRIVER | False | Searches for an IPv4 address in a network interface's address list by iterating through unicast addresses and compari... |
| `ipv4_is_broadcast_address` | NODRIVER | False | Checks if a given IPv4 address is a broadcast address for a specific network interface by comparing it with the inter... |
| `ipv4_maddr_find` | NODRIVER | False | Searches for an IPv4 multicast address in a network interface's multicast address table based on usage status and opt... |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap structure with provided memory, setting up wait queue and system heap. |
| `k_mbox_get` | NODRIVER | False | Zephyr RTOS mailbox receive function that retrieves messages from a mailbox, searches for compatible senders, handles... |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox data structure by setting up transmit/receive wait queues, initializing a spinlock,... |
| `k_mem_slab_init` | NODRIVER | False | Initializes a memory slab (memory pool) in the Zephyr RTOS kernel by setting up the slab structure with block paramet... |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a Zephyr RTOS message queue by checking for waiting threads and freeing allocated buffer memory if dynamica... |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting up buffer pointers, size parameters, and internal s... |
| `k_poll_event_init` | NODRIVER | False | Initializes a Zephyr RTOS poll event structure with validation and field setup |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated memory if necessary |
| `k_stack_init` | NODRIVER | False | Initializes a kernel stack object by setting up wait queue, lock, and buffer pointers |
| `k_timer_init` | NODRIVER | False | Initializes a Zephyr kernel timer object by setting callback functions and internal data structures |
| `k_work_cancel_delayable_sync` | CORE | False | Cancels a delayed work item synchronously in Zephyr RTOS, checking if work is pending and waiting for cancellation co... |
| `k_work_cancel_sync` | NODRIVER | False | Cancels a work item synchronously in Zephyr RTOS, waiting for completion if the work is currently running |
| `k_work_flush` | NODRIVER | False | Flushes a work item, waiting for completion if necessary as part of Zephyr RTOS work queue subsystem |
| `k_work_flush_delayable` | CORE | False | Flushes a delayable work item in Zephyr RTOS, waiting for completion if necessary |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item structure in the Zephyr RTOS kernel work queue subsystem |
| `k_work_poll_init` | NODRIVER | False | Initializes a pollable work structure in Zephyr RTOS kernel for work queue polling |
| `k_work_poll_submit_to_queue` | NODRIVER | False | Submits polled work to a work queue in Zephyr RTOS, handling work ownership, event registration, timeout management, ... |
| `k_work_queue_start` | CORE | False | Starts a work queue thread in Zephyr RTOS by initializing data structures and creating/starting a kernel thread to pr... |
| `mbox_message_put` | CORE | False | Helper routine that handles both synchronous and asynchronous mailbox message sends, performing thread scheduling and... |
| `mgmt_thread` | NODRIVER | False | Network management thread that processes network management events and runs associated callbacks in an infinite loop |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the Zephyr kernel scheduler |
| `net_arp_input` | NODRIVER | False | Processes ARP (Address Resolution Protocol) packets, handling both requests and replies, updating ARP cache, and gene... |
| `net_arp_prepare` | NODRIVER | False | Prepares ARP requests by checking ARP cache and initiating ARP resolution if needed |
| `net_buf_alloc_len` | NODRIVER | False | Allocates a network buffer from a pool with specified size and timeout, handling buffer pool management and synchroni... |
| `net_buf_alloc_with_data` | NODRIVER | False | Allocates a network buffer and initializes it with external data |
| `net_buf_append_bytes` | NODRIVER | False | Appends multiple bytes to a network buffer, creating new fragments if needed when current fragment has insufficient s... |
| `net_buf_clone` | NODRIVER | False | Creates a clone (copy) of a network buffer, either by referencing the original data or allocating new memory and copy... |
| `net_buf_linearize` | NODRIVER | False | Copies data from a fragmented network buffer chain into a contiguous destination buffer, handling offsets and lengths. |
| `net_buf_reset` | NODRIVER | False | Resets a network buffer by resetting its internal simple buffer structure and performing state validation |
| `net_buf_unref` | NODRIVER | False | Decrements reference count of network buffer and frees it when count reaches zero, handling buffer fragments and cleanup |
| `net_calc_chksum` | NODRIVER | False | Calculates checksum for network packets, supporting IPv4 and IPv6 protocols with different protocol types (TCP, UDP, ... |
| `net_calc_chksum_ipv4` | NODRIVER | False | Calculates IPv4 checksum for network packets by summing header data and applying proper byte order conversion |
| `net_conn_input` | NODRIVER | False | Network connection input handler that matches incoming packets against registered connection handlers based on protoc... |
| `net_conn_register` | NODRIVER | False | Registers a network connection handler for processing incoming network packets based on protocol, addresses, and ports |
| `net_context_bind` | NODRIVER | False | Binds a network context to a specific address and port, handling multiple address families (IPv6, IPv4, AF_PACKET, AF... |
| `net_context_connect` | NODRIVER | False | Network socket connection function that establishes a connection to a remote address, handling both IPv4/IPv6 and UDP... |
| `net_context_create_ipv4_new` | NODRIVER | False | Creates IPv4 packets for network contexts by validating source addresses, setting packet headers (TTL, DSCP, ECN), an... |
| `net_dhcpv4_init` | NODRIVER | False | Initializes the DHCPv4 client subsystem by setting up UDP callbacks for DHCP ports, timeout work, and network interfa... |
| `net_dhcpv4_input` | NODRIVER | False | DHCPv4 packet input handler that processes incoming DHCP packets, validates them, parses options, and handles DHCP re... |
| `net_eth_ipv4_mcast_to_mac_addr` | NODRIVER | False | Converts an IPv4 multicast address to an Ethernet multicast MAC address according to RFC 1112 specification |
| `net_eth_ipv6_mcast_to_mac_addr` | NODRIVER | False | Converts an IPv6 multicast address to an Ethernet MAC address according to RFC 2464 by setting the first two bytes to... |
| `net_icmpv4_finalize` | NODRIVER | False | Finalizes ICMPv4 packets by calculating and setting the checksum in the ICMP header |
| `net_icmpv4_input` | NODRIVER | False | Processes incoming ICMPv4 packets in the network stack, performing header validation, checksum verification, and call... |
| `net_icmpv4_send_error` | NODRIVER | False | Creates and sends an ICMPv4 error message in response to an original packet, handling protocol validation, packet all... |
| `net_if_ipv4_addr_add` | NODRIVER | False | Adds an IPv4 address to a network interface by finding an available slot in the interface's address table and initial... |
| `net_if_ipv4_addr_lookup` | NODRIVER | False | Searches through all network interfaces to find a matching IPv4 address and returns the corresponding network interfa... |
| `net_if_ipv4_addr_mask_cmp` | NODRIVER | False | Compares an IPv4 address with network interface's configured addresses using subnet masking to check if they belong t... |
| `net_if_ipv4_addr_rm` | NODRIVER | False | Removes an IPv4 address from a network interface's unicast address list by marking it as unused and sending a managem... |
| `net_if_ipv4_get_best_match` | NODRIVER | False | Selects the best matching IPv4 source address from a network interface's unicast addresses based on prefix length mat... |
| `net_if_ipv4_maddr_add` | NODRIVER | False | Adds an IPv4 multicast address to a network interface by finding an available slot in the multicast address list and ... |
| `net_if_ipv4_select_src_addr` | NODRIVER | False | Selects an appropriate source IPv4 address for outgoing packets based on destination address and network interface |
| `net_ipv4_create` | NODRIVER | False | Creates an IPv4 packet header by setting Type of Service (TOS) fields and delegating to net_ipv4_create_full for comp... |
| `net_ipv4_finalize` | NODRIVER | False | Finalizes IPv4 packet headers by setting length, protocol, checksum fields and calling appropriate transport layer fi... |
| `net_ipv4_igmp_input` | NODRIVER | False | Processes IGMP (Internet Group Management Protocol) packets in the IPv4 network stack, validating headers, checksums,... |
| `net_ipv4_input` | NODRIVER | False | Processes incoming IPv4 packets, validates headers, and routes to appropriate protocol handlers (ICMP, TCP, UDP, etc.) |
| `net_ipv4_parse_hdr_options` | NODRIVER | False | Parses IPv4 header options from a network packet, validates them, and calls a callback for specific option types (RR ... |
| `net_mgmt_add_event_callback` | NODRIVER | False | Adds a network management event callback to the callback list for network event notifications |
| `net_mgmt_del_event_callback` | NODRIVER | False | Removes a network management event callback from the callback list and updates the global event mask |
| `net_pkt_append_buffer` | NODRIVER | False | Appends a buffer to a network packet's fragment chain, either setting it as the first buffer or inserting it as a fra... |
| `net_pkt_available_buffer` | NODRIVER | False | Calculates the available buffer space in a network packet by subtracting current length from maximum length |
| `net_pkt_available_payload_buffer` | NODRIVER | False | Calculates available payload buffer space in a network packet after accounting for protocol headers |
| `net_pkt_buffer_hexdump` | NODRIVER | False | Prints a hex dump of network packet buffer chain for debugging purposes |
| `net_pkt_buffer_info` | NODRIVER | False | Prints debug information about a network packet's buffer chain for shell output |
| `net_pkt_clone_internal` | NODRIVER | False | Internal function that clones a network packet by allocating a new packet buffer and copying data from the source packet |
| `net_pkt_compact` | NODRIVER | False | Compacts data in a network packet by copying data from subsequent fragments into current fragment when space is avail... |
| `net_pkt_copy` | NODRIVER | False | Copies data from one network packet to another using buffer cursors and memcpy operations |
| `net_pkt_cursor_init` | NODRIVER | False | Initializes the cursor position in a network packet structure by setting the buffer pointer and data position. |
| `net_pkt_cursor_operate` | NODRIVER | False | Internal network packet buffer operation function that performs skip/read/write/memset operations using a cursor acro... |
| `net_pkt_find_offset` | NODRIVER | False | Finds the offset of a pointer within a network packet's buffer chain by traversing linked list of net_buf fragments |
| `net_pkt_frag_add` | NODRIVER | False | Adds a network buffer fragment to a network packet's fragment chain |
| `net_pkt_frag_del` | NODRIVER | False | Deletes a fragment from a network packet's fragment list, handling reference counting and memory management |
| `net_pkt_frag_insert` | NODRIVER | False | Inserts a network buffer fragment into a network packet's fragment list by updating linked list pointers |
| `net_pkt_get_contiguous_len` | NODRIVER | False | Calculates the contiguous length available in a network packet buffer by advancing the cursor and computing remaining... |
| `net_pkt_get_current_offset` | NODRIVER | False | Calculates the current offset within a network packet by traversing the buffer chain from the start to the cursor pos... |
| `net_pkt_pull` | NODRIVER | False | Removes data from the beginning of a network packet buffer by adjusting buffer lengths and managing buffer fragments |
| `net_pkt_remaining_data` | NODRIVER | False | Calculates the remaining data in a network packet from the current cursor position to the end of the packet |
| `net_pkt_remove_tail` | NODRIVER | False | Removes a specified length from the tail of a network packet by adjusting buffer lengths and freeing excess fragments |
| `net_pkt_shallow_clone` | NODRIVER | False | Creates a shallow clone of a network packet by allocating a new packet structure and referencing the original buffer ... |
| `net_pkt_trim_buffer` | NODRIVER | False | Removes empty buffers from a network packet's buffer chain by iterating through buffer fragments and unreferencing bu... |
| `net_pkt_unref` | NODRIVER | False | Decrements reference count of a network packet and frees it when count reaches zero |
| `net_pkt_update_length` | NODRIVER | False | Updates the length of network packet buffers by iterating through buffer fragments and adjusting their lengths to mat... |
| `net_recv_data` | NODRIVER | False | Network packet reception handler that validates received packets, sets packet properties, applies filtering, and queu... |
| `net_rx` | NODRIVER | False | Processes received network packets destined back to the local system, updates statistics, detects loopback conditions... |
| `net_send_data` | NODRIVER | False | Network packet transmission function that validates packets, updates statistics, handles loopback packets, and sends ... |
| `net_udp_finalize` | NODRIVER | False | Finalizes UDP packet headers by calculating and setting UDP length and optional checksum |
| `net_udp_get_hdr` | NODRIVER | False | Extracts UDP header from a network packet by skipping IP header and options, then retrieving UDP header data |
| `net_udp_input` | NODRIVER | False | Validates UDP packet headers, performs checksum verification, and returns UDP header pointer or NULL on error |
| `net_udp_set_hdr` | NODRIVER | False | Sets a UDP header in a network packet by copying header data to the appropriate position in the packet buffer |
| `next` | NODRIVER | False | Helper function that returns the next timeout structure in the kernel's timeout linked list |
| `ping_work` | NODRIVER | False | Work handler for ping operations that manages ping sequence, schedules next ping, and sends ICMP echo requests |
| `pkt_alloc_buffer` | NODRIVER | False | Allocates network buffers from a pool with timeout support, handling multiple buffer fragments if needed to satisfy r... |
| `pkt_cursor_advance` | NODRIVER | False | Advances a packet cursor within a network packet buffer, checking if the cursor has reached the end of the current bu... |
| `pkt_cursor_jump` | NODRIVER | False | Moves packet cursor to next non-empty fragment in network packet buffer chain |
| `pkt_cursor_update` | NODRIVER | False | Updates the cursor position within a network packet buffer, determining whether to jump to next buffer or increment p... |
| `pkt_get_max_len` | NODRIVER | False | Calculates the maximum length of a network packet by summing the maximum lengths of all buffer fragments in the packe... |
| `processing_data` | NODRIVER | False | Network packet processing function that handles the result of process_data() and manages packet references based on t... |
| `ready_thread` | CORE | False | Scheduler function that marks a thread as ready and adds it to the run queue if not already queued |
| `remove_from_tail` | NODRIVER | False | Removes an element from the tail of a shell history list and frees its space from the ring buffer |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout list and adjusts the delta ticks of the next timeout if present |
| `send_igmp_report` | NODRIVER | False | Sends IGMP membership reports for active multicast groups on a network interface |
| `set_up_fixed_clock_sources` | INIT | True | Initializes various fixed clock sources (HSE, HSI, MSI, LSI, LSE, HSI14, HSI48) for STM32 microcontrollers based on c... |
| `set_up_plls` | INIT | True | Configures and enables PLLs (Phase-Locked Loops) for clock generation in STM32 microcontrollers, handling PLL, PLL2, ... |
| `signal_poller` | CORE | False | Handles poller thread signaling when poll events are not met, performing thread state management operations including... |
| `st_stm32f7_init` | INIT | True | Performs basic hardware initialization at boot including cache and flash configuration |
| `stm32_clock_control_init` | INIT | True | Initializes clocks for STM32 microcontroller, enabling and configuring clocks and PLLs for the system. Called on star... |
| `stm32_clock_switch_to_hsi` | INIT | True | Unconditionally switches the system clock source to HSI (High-Speed Internal oscillator) |
| `stm32_exti_disable` | RETURNOK | False | Disables EXTI (External Interrupt) interrupt requests for a specific line (0-31) on STM32 microcontrollers |
| `stm32_exti_enable` | CORE | False | Enables an EXTI (External Interrupt) line and its corresponding interrupt in the NVIC |
| `stm32_exti_isr` | IRQ | True | EXTI (External Interrupt) ISR handler that checks EXTI lines for pending interrupts and executes registered callbacks |
| `stm32_exti_trigger` | INIT | True | Configures EXTI (External Interrupt) trigger conditions (rising edge, falling edge, both, or none) for specified inte... |
| `timeout_rem` | NODRIVER | False | Calculates remaining time for a timeout by traversing the timeout list and subtracting elapsed time |
| `triggered_work_cancel` | NODRIVER | False | Cancels a triggered work item by removing its timeout, clearing event registrations, and resetting work queue ownership |
| `triggered_work_handler` | NODRIVER | False | Kernel work handler for poll events that clears event registrations and executes the real handler |
| `update_cache` | CORE | False | Updates the scheduler's ready queue cache based on preemption decisions, determining which thread should be cached as... |
| `z_abort_timeout` | NODRIVER | False | Aborts/cancels a scheduled timeout by removing it from the kernel timeout queue if it's currently linked. |
| `z_add_timeout` | INIT | True | Adds a timeout structure to the kernel's sorted timeout list and updates system clock timeout if needed |
| `z_cbvprintf_impl` | NODRIVER | False | Callback-based printf implementation that processes format strings and arguments, outputting characters through a use... |
| `z_handle_obj_poll_events` | NODRIVER | False | Handles poll events from a doubly-linked list by retrieving events and signaling them with the given state while hold... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr RTOS condition variable object by setting up its wait queue and kernel object tracking |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a mutex data structure in the Zephyr RTOS kernel by setting owner to NULL, lock count to 0, initializing ... |
| `z_impl_k_mutex_lock` | CORE | False | Zephyr RTOS mutex lock implementation with priority inheritance, handles mutex acquisition and thread scheduling |
| `z_impl_k_poll` | CORE | False | Zephyr RTOS kernel poll function that handles event polling with timeout support and manages thread state transitions |
| `z_impl_k_poll_signal_init` | NODRIVER | False | Initializes a Zephyr kernel poll signal object by setting up its poll events list, resetting the signaled flag, and i... |
| `z_impl_k_poll_signal_raise` | CORE | False | Raises a poll signal in the Zephyr RTOS kernel, updating signal state and potentially rescheduling tasks |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a kernel queue data structure by setting up the data queue list, spinlock, wait queue, and optional poll ... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a Zephyr RTOS semaphore object by setting initial count and limit, initializing wait queue, and performin... |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Zephyr kernel timer function that synchronously waits for a timer to expire and returns its status, resetting the sta... |
| `z_impl_k_yield` | CORE | False | Implements thread yielding in the Zephyr kernel scheduler, performing context switching and thread queue management. |
| `z_impl_net_addr_ntop` | NODRIVER | False | Converts binary network addresses (IPv4/IPv6) to human-readable string representation |
| `z_impl_net_addr_pton` | NODRIVER | False | Converts string representation of IP address (IPv4/IPv6) to binary format |
| `z_init_thread_base` | NODRIVER | False | Initializes the base thread structure in Zephyr RTOS kernel, setting up thread priority, state, options, and other th... |
| `z_priq_dumb_best` | CORE | False | Retrieves the best thread from a priority queue for scheduler operations |
| `z_priq_dumb_remove` | CORE | False | Removes a thread from a priority queue in the Zephyr RTOS scheduler |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue by checking the bitmask and returning the thread at... |
| `z_sched_waitq_walk` | NODRIVER | False | Walks through a wait queue and invokes a callback function on each waiting thread, using spinlocks for synchronization. |
| `z_set_prio` | CORE | False | Sets a thread's priority without rescheduling, changes run queue state, and returns whether rescheduling is needed la... |
| `z_setup_new_thread` | CORE | False | Initializes a new thread structure with stack, entry point, priority, and other thread parameters as part of the Zeph... |
| `z_shell_history_get` | NODRIVER | False | Retrieves command history items from shell history buffer, navigating through linked list and copying selected comman... |
| `z_shell_history_init` | NODRIVER | False | Initializes a shell history data structure by setting up a doubly linked list and resetting the current pointer |
| `z_shell_history_put` | NODRIVER | False | Adds a command line to the shell history buffer using ring buffer storage and linked list management |
| `z_timer_expiration_handler` | NODRIVER | False | Handles expiration of a kernel timer object in Zephyr RTOS, managing timer status, invoking user callbacks, and wakin... |
| `z_unpend_all` | CORE | False | Un-pends all threads from a wait queue and marks them as ready for scheduling |

## 附录：interesting MMIO expr 子集（共 10 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `HAL_ETH_Init`
- `HAL_RCCEx_DisablePLLI2S`
- `HAL_RCCEx_DisablePLLSAI`
- `HAL_RCCEx_EnablePLLI2S`
- `HAL_RCCEx_EnablePLLSAI`
- `HAL_RCCEx_PeriphCLKConfig`
- `HAL_RCC_ClockConfig`
- `HAL_RCC_DeInit`
- `HAL_RCC_MCOConfig`
- `HAL_RCC_OscConfig`
