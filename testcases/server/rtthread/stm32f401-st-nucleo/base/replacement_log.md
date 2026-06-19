## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/rtthread/stm32f401-st-nucleo/base`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `HAL_ADC_MspDeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 158 | 1 |
| `HAL_ADC_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 108 | 1 |
| `HAL_DMAEx_MultiBufferStart_IT` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_dma_ex.c` | 154 | 1 |
| `HAL_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 190 | 1 |
| `HAL_Delay` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 390 | 1 |
| `HAL_GPIO_EXTI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 492 | 1 |
| `HAL_GPIO_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 164 | 1 |
| `HAL_HalfDuplex_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 435 | 1 |
| `HAL_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 157 | 2 |
| `HAL_InitTick` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 253 | 2 |
| `HAL_LIN_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 509 | 1 |
| `HAL_MultiProcessor_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 591 | 1 |
| `HAL_NVIC_EnableIRQ` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 185 | 1 |
| `HAL_NVIC_SetPriority` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 163 | 1 |
| `HAL_NVIC_SetPriorityGrouping` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 141 | 1 |
| `HAL_PWREx_ControlVoltageScaling` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 288 | 1 |
| `HAL_PWREx_DisableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 165 | 1 |
| `HAL_PWREx_EnableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 141 | 1 |
| `HAL_PWR_ConfigPVD` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 275 | 1 |
| `HAL_PWR_EnterSTOPMode` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 445 | 1 |
| `HAL_PWR_PVD_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 509 | 1 |
| `HAL_RCCEx_DisablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2929 | 1 |
| `HAL_RCCEx_EnablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2846 | 1 |
| `HAL_RCCEx_GetPeriphCLKConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2680 | 1 |
| `HAL_RCCEx_PeriphCLKConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2551 | 1 |
| `HAL_RCC_ClockConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 591 | 2 |
| `HAL_RCC_GetPCLK1Freq` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 954 | 1 |
| `HAL_RCC_GetPCLK2Freq` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 966 | 1 |
| `HAL_RCC_GetSysClockFreq` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 885 | 1 |
| `HAL_RCC_NMI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 1084 | 1 |
| `HAL_RCC_OscConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 219 | 1 |
| `HAL_SPI_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c` | 311 | 1 |
| `HAL_TIM_Base_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 262 | 1 |
| `HAL_TIM_MspPostInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 333 | 1 |
| `HAL_UART_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 669 | 1 |
| `HAL_UART_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 2350 | 1 |
| `HAL_UART_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 357 | 1 |
| `HAL_UART_Receive` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 1221 | 1 |
| `HAL_UART_Transmit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 1135 | 1 |
| `SystemClock_Config` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/board.c` | 14 | 1 |
| `SystemCoreClockUpdate` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c` | 220 | 1 |
| `SystemInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c` | 167 | 2 |
| `UART_SetConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 3695 | 1 |
| `UART_WaitOnFlagUntilTimeout` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 3185 | 1 |
| `rt_hw_pin_init` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_gpio.c` | 763 | 1 |
| `stm32_dma_config` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c` | 1049 | 1 |
| `stm32_putc` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c` | 340 | 2 |
| `uart_isr` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c` | 460 | 1 |

## 2. 各函数替换详情

### HAL_ADC_MspDeInit

```text
=== HAL_ADC_MspDeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c
- 行号：158
- 函数内容：void HAL_ADC_MspDeInit(ADC_HandleTypeDef* hadc)
{
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspDeInit 0 */

  /* USER CODE END ADC1_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_ADC1_CLK_DISABLE();

    /**ADC1 GPIO Configuration
    PC0     ------> ADC1_IN10
    PC1     ------> ADC1_IN11
    PA0-WKUP     ------> ADC1_IN0
    PA1     ------> ADC1_IN1
    PA4     ------> ADC1_IN4
    PB0     ------> ADC1_IN8
    */
    HAL_GPIO_DeInit(GPIOC, GPIO_PIN_0|GPIO_PIN_1);

    HAL_GPIO_DeInit(GPIOA, GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4);

    HAL_GPIO_DeInit(GPIOB, GPIO_PIN_0);

  /* USER CODE BEGIN ADC1_MspDeInit 1 */

  /* USER CODE END ADC1_MspDeInit 1 */
  }

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：ADC MSP (Microcontroller Specific Package) de-initialization function that frees hardware resources used by ADC peripheral
- 是否需要替换：是
- 分类/替换原因：This function performs hardware de-initialization operations including disabling peripheral clock and de-initializing GPIO pins. GetFunctionInfo shows it contains __HAL_RCC_ADC1_CLK_DISABLE() and multiple HAL_GPIO_DeInit() calls. GetMMIOFunctionInfo indicates it's in the MMIO function set. According to classification priority, this is an INIT type function (de-initialization is the reverse of initialization). The function checks hardware instance (ADC1) and performs hardware-specific cleanup operations that need to be removed for simulation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief ADC MSP De-Initialization
* This function freeze the hardware resources used in this example
* @param hadc: ADC handle pointer
* @retval None
*/
void HAL_ADC_MspDeInit(ADC_HandleTypeDef* hadc)
{
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspDeInit 0 */

  /* USER CODE END ADC1_MspDeInit 0 */
    /* Peripheral clock disable - removed for simulation */
    // __HAL_RCC_ADC1_CLK_DISABLE();

    /**ADC1 GPIO Configuration
    PC0     ------> ADC1_IN10
    PC1     ------> ADC1_IN11
    PA0-WKUP     ------> ADC1_IN0
    PA1     ------> ADC1_IN1
    PA4     ------> ADC1_IN4
    PB0     ------> ADC1_IN8
    */
    // HAL_GPIO_DeInit(GPIOC, GPIO_PIN_0|GPIO_PIN_1);

    // HAL_GPIO_DeInit(GPIOA, GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4);

    // HAL_GPIO_DeInit(GPIOB, GPIO_PIN_0);

  /* USER CODE BEGIN ADC1_MspDeInit 1 */

  /* USER CODE END ADC1_MspDeInit 1 */
  }

}
```

=== 信息结束 ===
```

### HAL_ADC_MspInit

```text
=== HAL_ADC_MspInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c
- 行号：108
- 函数内容：void HAL_ADC_MspInit(ADC_HandleTypeDef* hadc)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspInit 0 */

  /* USER CODE END ADC1_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_ADC1_CLK_ENABLE();

    __HAL_RCC_GPIOC_CLK_ENABLE();
    __HAL_RCC_GPIOA_CLK_ENABLE();
    __HAL_RCC_GPIOB_CLK_ENABLE();
    /**ADC1 GPIO Configuration
    PC0     ------> ADC1_IN10
    PC1     ------> ADC1_IN11
    PA0-WKUP     ------> ADC1_IN0
    PA1     ------> ADC1_IN1
    PA4     ------> ADC1_IN4
    PB0     ------> ADC1_IN8
    */
    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN ADC1_MspInit 1 */

  /* USER CODE END ADC1_MspInit 1 */
  }

}


【初始分析（FunctionClassifier）】
- 函数类型：SKIP
- 函数用途/功能描述：Weak function for ADC MCU-specific package initialization, meant to be overridden by users for MCU-specific ADC setup.
- 是否需要替换：否
- 分类/替换原因：The function is declared as __weak with an empty default implementation containing only UNUSED(hadc) and comments. GetMMIOFunctionInfo confirms no MMIO operations. It's called by HAL_ADC_Init as part of initialization sequence but serves only as a placeholder for optional user-specific MCU initialization. Since the base implementation performs no hardware operations and is non-critical, it can be safely skipped.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：void HAL_ADC_MspInit(ADC_HandleTypeDef* hadc)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspInit 0 */

  /* USER CODE END ADC1_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_ADC1_CLK_ENABLE(); */

    /* [INIT REMOVED] GPIO clock enables removed */
    /* __HAL_RCC_GPIOC_CLK_ENABLE(); */
    /* __HAL_RCC_GPIOA_CLK_ENABLE(); */
    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */
    
    /**ADC1 GPIO Configuration
    PC0     ------> ADC1_IN10
    PC1     ------> ADC1_IN11
    PA0-WKUP     ------> ADC1_IN0
    PA1     ------> ADC1_IN1
    PA4     ------> ADC1_IN4
    PB0     ------> ADC1_IN8
    */
    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    /* Preserve GPIO initialization (will use replaced HAL_GPIO_Init) */
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN ADC1_MspInit 1 */

  /* USER CODE END ADC1_MspInit 1 */
  }

}
- 更新原因：Replace HAL_ADC_MspInit function to remove hardware-specific clock enable operations while preserving GPIO configuration structure initialization and HAL_GPIO_Init calls. The function contains __HAL_RCC_ADC1_CLK_ENABLE() and GPIO clock enable calls that access hardware registers. These are removed with [INIT REMOVED] comments. The HAL_GPIO_Init calls are preserved as they will use the already-replaced version that removes hardware operations.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_ADC_MspInit(ADC_HandleTypeDef* hadc)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspInit 0 */

  /* USER CODE END ADC1_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_ADC1_CLK_ENABLE(); */

    /* [INIT REMOVED] GPIO clock enables removed */
    /* __HAL_RCC_GPIOC_CLK_ENABLE(); */
    /* __HAL_RCC_GPIOA_CLK_ENABLE(); */
    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */
    
    /**ADC1 GPIO Configuration
    PC0     ------> ADC1_IN10
    PC1     ------> ADC1_IN11
    PA0-WKUP     ------> ADC1_IN0
    PA1     ------> ADC1_IN1
    PA4     ------> ADC1_IN4
    PB0     ------> ADC1_IN8
    */
    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    /* Preserve GPIO initialization (will use replaced HAL_GPIO_Init) */
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_0;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN ADC1_MspInit 1 */

  /* USER CODE END ADC1_MspInit 1 */
  }

}
    原因：Replace HAL_ADC_MspInit function to remove hardware-specific clock enable operations while preserving GPIO configuration structure initialization and HAL_GPIO_Init calls. The function contains __HAL_RCC_ADC1_CLK_ENABLE() and GPIO clock enable calls that access hardware registers. These are removed with [INIT REMOVED] comments. The HAL_GPIO_Init calls are preserved as they will use the already-replaced version that removes hardware operations.
    时间：

=== 信息结束 ===
```

### HAL_DMAEx_MultiBufferStart_IT

```text
=== HAL_DMAEx_MultiBufferStart_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_dma_ex.c
- 行号：154
- 函数内容：HAL_StatusTypeDef HAL_DMAEx_MultiBufferStart_IT(DMA_HandleTypeDef *hdma, uint32_t SrcAddress, uint32_t DstAddress, uint32_t SecondMemAddress, uint32_t DataLength)
{
  HAL_StatusTypeDef status = HAL_OK;
  
  /* Check the parameters */
  assert_param(IS_DMA_BUFFER_SIZE(DataLength));
  
  /* Memory-to-memory transfer not supported in double buffering mode */
  if (hdma->Init.Direction == DMA_MEMORY_TO_MEMORY)
  {
    hdma->ErrorCode = HAL_DMA_ERROR_NOT_SUPPORTED;
    return HAL_ERROR;
  }
  
  /* Check callback functions */
  if ((NULL == hdma->XferCpltCallback) || (NULL == hdma->XferM1CpltCallback) || (NULL == hdma->XferErrorCallback))
  {
    hdma->ErrorCode = HAL_DMA_ERROR_PARAM;
    return HAL_ERROR;
  }
  
  /* Process locked */
  __HAL_LOCK(hdma);
  
  if(HAL_DMA_STATE_READY == hdma->State)
  {
    /* Change DMA peripheral state */
    hdma->State = HAL_DMA_STATE_BUSY;
    
    /* Initialize the error code */
    hdma->ErrorCode = HAL_DMA_ERROR_NONE;
    
    /* Enable the Double buffer mode */
    hdma->Instance->CR |= (uint32_t)DMA_SxCR_DBM;
    
    /* Configure DMA Stream destination address */
    hdma->Instance->M1AR = SecondMemAddress;
    
    /* Configure the source, destination address and the data length */
    DMA_MultiBufferSetConfig(hdma, SrcAddress, DstAddress, DataLength); 
    
    /* Clear all flags */
    __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_TC_FLAG_INDEX(hdma));
    __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_HT_FLAG_INDEX(hdma));
    __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_TE_FLAG_INDEX(hdma));
    __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_DME_FLAG_INDEX(hdma));
    __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_FE_FLAG_INDEX(hdma));

    /* Enable Common interrupts*/
    hdma->Instance->CR  |= DMA_IT_TC | DMA_IT_TE | DMA_IT_DME;
    hdma->Instance->FCR |= DMA_IT_FE;
    
    if((hdma->XferHalfCpltCallback != NULL) || (hdma->XferM1HalfCpltCallback != NULL))
    {
      hdma->Instance->CR  |= DMA_IT_HT;
    }
    
    /* Enable the peripheral */
    __HAL_DMA_ENABLE(hdma); 
  }
  else
  {     
    /* Process unlocked */
    __HAL_UNLOCK(hdma);	  
    
    /* Return error status */
    status = HAL_BUSY;
  }  
  return status; 
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Starts multi-buffer DMA transfer with interrupt capability, configuring DMA hardware for double-buffer mode and enabling interrupts.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it initializes and starts DMA hardware for multi-buffer transfers with interrupts. Analysis shows: 1) It performs hardware register configuration (enabling double buffer mode, setting memory addresses, clearing flags, enabling interrupts); 2) It manages DMA state transitions (READY to BUSY); 3) It validates parameters and callback functions; 4) It uses locking mechanisms for thread safety. The function does not fit other classifications: not CORE (no NVIC/OS kernel operations), not RECV (doesn't perform data I/O), not IRQ (not an interrupt handler), not LOOP (no polling loops), not RETURNOK/SKIP (has significant hardware configuration that needs removal). The replacement preserves state management, error handling, and parameter validation while removing all hardware register accesses.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Starts the multi_buffer DMA Transfer with interrupt enabled.
* @param  hdma       pointer to a DMA_HandleTypeDef structure that contains
*                     the configuration information for the specified DMA Stream.
* @param  SrcAddress The source memory Buffer address
* @param  DstAddress The destination memory Buffer address
* @param  SecondMemAddress The second memory Buffer address in case of multi buffer Transfer
* @param  DataLength The length of data to be transferred from source to destination
* @retval HAL status
*/
HAL_StatusTypeDef HAL_DMAEx_MultiBufferStart_IT(DMA_HandleTypeDef *hdma, uint32_t SrcAddress, uint32_t DstAddress, uint32_t SecondMemAddress, uint32_t DataLength)
{
  HAL_StatusTypeDef status = HAL_OK;
  
  /* Check the parameters */
  assert_param(IS_DMA_BUFFER_SIZE(DataLength));
  
  /* Memory-to-memory transfer not supported in double buffering mode */
  if (hdma->Init.Direction == DMA_MEMORY_TO_MEMORY)
  {
    hdma->ErrorCode = HAL_DMA_ERROR_NOT_SUPPORTED;
    return HAL_ERROR;
  }
  
  /* Check callback functions */
  if ((NULL == hdma->XferCpltCallback) || (NULL == hdma->XferM1CpltCallback) || (NULL == hdma->XferErrorCallback))
  {
    hdma->ErrorCode = HAL_DMA_ERROR_PARAM;
    return HAL_ERROR;
  }
  
  /* Process locked */
  __HAL_LOCK(hdma);
  
  if(HAL_DMA_STATE_READY == hdma->State)
  {
    /* Change DMA peripheral state */
    hdma->State = HAL_DMA_STATE_BUSY;
    
    /* Initialize the error code */
    hdma->ErrorCode = HAL_DMA_ERROR_NONE;
    
    /* Skip hardware-specific configuration */
    /* Original: Enable the Double buffer mode - hdma->Instance->CR |= (uint32_t)DMA_SxCR_DBM; */
    /* Original: Configure DMA Stream destination address - hdma->Instance->M1AR = SecondMemAddress; */
    /* Original: Configure the source, destination address and the data length - DMA_MultiBufferSetConfig(hdma, SrcAddress, DstAddress, DataLength); */
    /* Original: Clear all flags - multiple __HAL_DMA_CLEAR_FLAG calls */
    /* Original: Enable Common interrupts - hdma->Instance->CR |= DMA_IT_TC | DMA_IT_TE | DMA_IT_DME; hdma->Instance->FCR |= DMA_IT_FE; */
    /* Original: Enable half transfer interrupt if callbacks exist - hdma->Instance->CR |= DMA_IT_HT; */
    /* Original: Enable the peripheral - __HAL_DMA_ENABLE(hdma); */
    
    /* Preserve state and structure initialization only */
  }
  else
  {     
    /* Process unlocked */
    __HAL_UNLOCK(hdma);	  
    
    /* Return error status */
    status = HAL_BUSY;
  }  
  return status; 
}
```

=== 信息结束 ===
```

### HAL_DeInit

```text
=== HAL_DeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c
- 行号：190
- 函数内容：HAL_StatusTypeDef HAL_DeInit(void)
{
  /* Reset of all peripherals */
  __HAL_RCC_APB1_FORCE_RESET();
  __HAL_RCC_APB1_RELEASE_RESET();

  __HAL_RCC_APB2_FORCE_RESET();
  __HAL_RCC_APB2_RELEASE_RESET();

  __HAL_RCC_AHB1_FORCE_RESET();
  __HAL_RCC_AHB1_RELEASE_RESET();

  __HAL_RCC_AHB2_FORCE_RESET();
  __HAL_RCC_AHB2_RELEASE_RESET();

  __HAL_RCC_AHB3_FORCE_RESET();
  __HAL_RCC_AHB3_RELEASE_RESET();

  /* De-Init the low level hardware */
  HAL_MspDeInit();
    
  /* Return function status */
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes the HAL common part, resets all peripherals, and calls low-level hardware de-initialization
- 是否需要替换：是
- 分类/替换原因：The function performs hardware de-initialization operations by resetting all peripherals through RCC macros (APB1, APB2, AHB1, AHB2, AHB3 buses) and calls HAL_MspDeInit(). GetMMIOFunctionInfo shows it contains hardware register accesses (though no explicit MMIO expressions were listed, the RCC macros are known to perform MMIO operations). This is a de-initialization function which is the inverse of initialization, fitting the INIT classification. The function contains hardware-specific operations that need to be removed while preserving the call to HAL_MspDeInit() and returning HAL_OK.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function de-Initializes common part of the HAL and stops the systick.
*         This function is optional.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_DeInit(void)
{
  /* Skip hardware-specific peripheral resets */
  /* __HAL_RCC_APB1_FORCE_RESET(); */
  /* __HAL_RCC_APB1_RELEASE_RESET(); */

  /* __HAL_RCC_APB2_FORCE_RESET(); */
  /* __HAL_RCC_APB2_RELEASE_RESET(); */

  /* __HAL_RCC_AHB1_FORCE_RESET(); */
  /* __HAL_RCC_AHB1_RELEASE_RESET(); */

  /* __HAL_RCC_AHB2_FORCE_RESET(); */
  /* __HAL_RCC_AHB2_RELEASE_RESET(); */

  /* __HAL_RCC_AHB3_FORCE_RESET(); */
  /* __HAL_RCC_AHB3_RELEASE_RESET(); */

  /* De-Init the low level hardware */
  HAL_MspDeInit();
    
  /* Return function status */
  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_Delay

```text
=== HAL_Delay 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c
- 行号：390
- 函数内容：__weak void HAL_Delay(uint32_t Delay)
{
  uint32_t tickstart = HAL_GetTick();
  uint32_t wait = Delay;

  /* Add a freq to guarantee minimum wait */
  if (wait < HAL_MAX_DELAY)
  {
    wait += (uint32_t)(uwTickFreq);
  }

  while((HAL_GetTick() - tickstart) < wait)
  {
  }
}


【替换更新】
- 更新代码：__weak void HAL_Delay(uint32_t Delay)
{
  /* [LOOP] Remove busy-wait loop */
  /* Original code has while loop that busy-waits for the specified delay */
  /* In emulation with RTOS, we should yield to other threads instead */
  
  /* For short delays, just return immediately */
  if (Delay == 0)
  {
    return;
  }
  
  /* For longer delays, we could use RTOS delay function if available */
  /* But to keep it simple and avoid dependencies, just return */
  /* The application should use RTOS delay functions instead of HAL_Delay */
  
  /* Note: In real hardware, HAL_Delay busy-waits using SysTick
   * In emulation, we don't want to busy-wait as it would block the emulator
   * and trigger exceptional loop detection */
}
- 更新原因：Create replacement for HAL_Delay to remove busy-wait loop. The original function contains a while loop that busy-waits for the specified delay by repeatedly calling HAL_GetTick(). In emulation, this would block the emulator and could trigger exceptional loop detection. This replacement removes the busy-wait loop. For RTOS applications, delay functionality should be provided by RTOS delay functions (e.g., rt_thread_delay) rather than busy-waiting.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__weak void HAL_Delay(uint32_t Delay)
{
  /* [LOOP] Remove busy-wait loop */
  /* Original code has while loop that busy-waits for the specified delay */
  /* In emulation with RTOS, we should yield to other threads instead */
  
  /* For short delays, just return immediately */
  if (Delay == 0)
  {
    return;
  }
  
  /* For longer delays, we could use RTOS delay function if available */
  /* But to keep it simple and avoid dependencies, just return */
  /* The application should use RTOS delay functions instead of HAL_Delay */
  
  /* Note: In real hardware, HAL_Delay busy-waits using SysTick
   * In emulation, we don't want to busy-wait as it would block the emulator
   * and trigger exceptional loop detection */
}
    原因：Create replacement for HAL_Delay to remove busy-wait loop. The original function contains a while loop that busy-waits for the specified delay by repeatedly calling HAL_GetTick(). In emulation, this would block the emulator and could trigger exceptional loop detection. This replacement removes the busy-wait loop. For RTOS applications, delay functionality should be provided by RTOS delay functions (e.g., rt_thread_delay) rather than busy-waiting.
    时间：

=== 信息结束 ===
```

### HAL_GPIO_EXTI_IRQHandler

```text
=== HAL_GPIO_EXTI_IRQHandler 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c
- 行号：492
- 函数内容：void HAL_GPIO_EXTI_IRQHandler(uint16_t GPIO_Pin)
{
  /* EXTI line interrupt detected */
  if(__HAL_GPIO_EXTI_GET_IT(GPIO_Pin) != RESET)
  {
    __HAL_GPIO_EXTI_CLEAR_IT(GPIO_Pin);
    HAL_GPIO_EXTI_Callback(GPIO_Pin);
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Handles EXTI interrupt requests for GPIO pins by checking interrupt flags, clearing them, and invoking callback functions
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler (IRQHandler) that processes EXTI interrupts. It contains hardware register operations (__HAL_GPIO_EXTI_GET_IT and __HAL_GPIO_EXTI_CLEAR_IT) to check and clear interrupt flags. The function is called from various EXTI interrupt handlers (EXTI0_IRQHandler, EXTI1_IRQHandler, etc.) and calls a user callback function. It does not involve NVIC configuration (which would be CORE), just EXTI peripheral handling. According to the classification priority, IRQ functions require replacement to remove hardware operations while preserving callback invocation and control flow.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  This function handles EXTI interrupt request.\n* @param  GPIO_Pin Specifies the pins connected EXTI line\n* @retval None\n*/\nvoid HAL_GPIO_EXTI_IRQHandler(uint16_t GPIO_Pin)\n{\n  /* EXTI line interrupt detected */\n  /* Simulate interrupt flag check - assume interrupt is pending */\n  /* Skip hardware register read: if(__HAL_GPIO_EXTI_GET_IT(GPIO_Pin) != RESET) */\n  {\n    /* Skip hardware register clear: __HAL_GPIO_EXTI_CLEAR_IT(GPIO_Pin); */\n    HAL_GPIO_EXTI_Callback(GPIO_Pin);\n  }\n}
```

=== 信息结束 ===
```

### HAL_GPIO_Init

```text
=== HAL_GPIO_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c
- 行号：164
- 函数内容：void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
{
  uint32_t position;
  uint32_t ioposition = 0x00U;
  uint32_t iocurrent = 0x00U;
  uint32_t temp = 0x00U;

  /* Check the parameters */
  assert_param(IS_GPIO_ALL_INSTANCE(GPIOx));
  assert_param(IS_GPIO_PIN(GPIO_Init->Pin));
  assert_param(IS_GPIO_MODE(GPIO_Init->Mode));

  /* Configure the port pins */
  for(position = 0U; position < GPIO_NUMBER; position++)
  {
    /* Get the IO position */
    ioposition = 0x01U << position;
    /* Get the current IO position */
    iocurrent = (uint32_t)(GPIO_Init->Pin) & ioposition;

    if(iocurrent == ioposition)
    {
      /*--------------------- GPIO Mode Configuration ------------------------*/
      /* In case of Output or Alternate function mode selection */
      if(((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) || \
          (GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Configure the IO Speed */
        temp = GPIOx->OSPEEDR; 
        temp &= ~(GPIO_OSPEEDER_OSPEEDR0 << (position * 2U));
        temp |= (GPIO_Init->Speed << (position * 2U));
        GPIOx->OSPEEDR = temp;

        /* Configure the IO Output Type */
        temp = GPIOx->OTYPER;
        temp &= ~(GPIO_OTYPER_OT_0 << position) ;
        temp |= (((GPIO_Init->Mode & OUTPUT_TYPE) >> OUTPUT_TYPE_Pos) << position);
        GPIOx->OTYPER = temp;
       }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        
        /* Activate the Pull-up or Pull down resistor for the current IO */
        temp = GPIOx->PUPDR;
        temp &= ~(GPIO_PUPDR_PUPDR0 << (position * 2U));
        temp |= ((GPIO_Init->Pull) << (position * 2U));
        GPIOx->PUPDR = temp;
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Configure Alternate function mapped with the current IO */
        temp = GPIOx->AFR[position >> 3U];
        temp &= ~(0xFU << ((uint32_t)(position & 0x07U) * 4U)) ;
        temp |= ((uint32_t)(GPIO_Init->Alternate) << (((uint32_t)position & 0x07U) * 4U));
        GPIOx->AFR[position >> 3U] = temp;
      }

      /* Configure IO Direction mode (Input, Output, Alternate or Analog) */
      temp = GPIOx->MODER;
      temp &= ~(GPIO_MODER_MODER0 << (position * 2U));
      temp |= ((GPIO_Init->Mode & GPIO_MODE) << (position * 2U));
      GPIOx->MODER = temp;

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Enable SYSCFG Clock */
        __HAL_RCC_SYSCFG_CLK_ENABLE();

        temp = SYSCFG->EXTICR[position >> 2U];
        temp &= ~(0x0FU << (4U * (position & 0x03U)));
        temp |= ((uint32_t)(GPIO_GET_INDEX(GPIOx)) << (4U * (position & 0x03U)));
        SYSCFG->EXTICR[position >> 2U] = temp;

        /* Clear Rising Falling edge configuration */
        temp = EXTI->RTSR;
        temp &= ~((uint32_t)iocurrent);
        if((GPIO_Init->Mode & TRIGGER_RISING) != 0x00U)
        {
          temp |= iocurrent;
        }
        EXTI->RTSR = temp;

        temp = EXTI->FTSR;
        temp &= ~((uint32_t)iocurrent);
        if((GPIO_Init->Mode & TRIGGER_FALLING) != 0x00U)
        {
          temp |= iocurrent;
        }
        EXTI->FTSR = temp;

        temp = EXTI->EMR;
        temp &= ~((uint32_t)iocurrent);
        if((GPIO_Init->Mode & EXTI_EVT) != 0x00U)
        {
          temp |= iocurrent;
        }
        EXTI->EMR = temp;

        /* Clear EXTI line configuration */
        temp = EXTI->IMR;
        temp &= ~((uint32_t)iocurrent);
        if((GPIO_Init->Mode & EXTI_IT) != 0x00U)
        {
          temp |= iocurrent;
        }
        EXTI->IMR = temp;
      }
    }
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes GPIO pins according to specified configuration parameters including mode, speed, pull-up/down, and alternate function settings.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a GPIO peripheral initialization function. GetMMIOFunctionInfo identified extensive MMIO register writes to GPIO configuration registers (OSPEEDR, OTYPER, PUPDR, AFR, MODER) and EXTI registers. The function performs hardware configuration without data transmission/reception, interrupt handling, or hardware-dependent polling loops. It validates parameters and applies configuration to specified pins through bitmask calculations, making it a classic INIT function that requires removal of hardware-specific operations while preserving configuration logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the GPIOx peripheral according to the specified parameters in the GPIO_Init.
* @param  GPIOx where x can be (A..K) to select the GPIO peripheral.
* @param  GPIO_Init pointer to a GPIO_InitTypeDef structure that contains
*         the configuration information for the specified GPIO peripheral.
* @retval None
*/
void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
{
  uint32_t position = 0x00;
  uint32_t ioposition = 0x00;
  uint32_t iocurrent = 0x00;
  uint32_t temp = 0x00;

  /* Check the parameters */
  assert_param(IS_GPIO_ALL_INSTANCE(GPIOx));
  assert_param(IS_GPIO_PIN(GPIO_Init->Pin));
  assert_param(IS_GPIO_MODE(GPIO_Init->Mode));

  /* Configure the port pins */
  for (position = 0; position < GPIO_NUMBER; position++)
  {
    /* Get the IO position */
    ioposition = ((uint32_t)0x01) << position;
    /* Get the current IO position */
    iocurrent = (uint32_t)(GPIO_Init->Pin) & ioposition;

    if (iocurrent == ioposition)
    {
      /*--------------------- GPIO Mode Configuration ------------------------*/
      /* In case of Output or Alternate function mode selection */
      if (((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) || ((GPIO_Init->Mode & GPIO_MODE) == MODE_AF))
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Configure the IO Speed - Hardware operation removed */
        /* temp = GPIOx->OSPEEDR; */
        /* temp &= ~(GPIO_OSPEEDER_OSPEEDR0 << (position * 2)); */
        /* temp |= (GPIO_Init->Speed << (position * 2)); */
        /* GPIOx->OSPEEDR = temp; */

        /* Configure the IO Output Type - Hardware operation removed */
        /* temp = GPIOx->OTYPER; */
        /* temp &= ~(GPIO_OTYPER_OT_0 << position) ; */
        /* temp |= (((GPIO_Init->Mode & OUTPUT_TYPE) >> OUTPUT_TYPE_Pos) << position); */
        /* GPIOx->OTYPER = temp; */
      }

      if ((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the Pull parameter */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));

        /* Activate the Pull-up or Pull down resistor for the current IO - Hardware operation removed */
        /* temp = GPIOx->PUPDR; */
        /* temp &= ~(GPIO_PUPDR_PUPDR0 << (position * 2)); */
        /* temp |= ((GPIO_Init->Pull) << (position * 2)); */
        /* GPIOx->PUPDR = temp; */
      }

      /* In case of Alternate function mode selection */
      if ((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));

        /* Configure Alternate function mapped with the current IO - Hardware operation removed */
        /* temp = GPIOx->AFR[position >> 3]; */
        /* temp &= ~((uint32_t)0xF << ((uint32_t)(position & (uint32_t)0x07) * 4)) ; */
        /* temp |= ((uint32_t)(GPIO_Init->Alternate) << (((uint32_t)position & (uint32_t)0x07) * 4)); */
        /* GPIOx->AFR[position >> 3] = temp; */
      }

      /* Configure IO Direction mode (Input, Output, Alternate or Analog) - Hardware operation removed */
      /* temp = GPIOx->MODER; */
      /* temp &= ~(GPIO_MODER_MODER0 << (position * 2)); */
      /* temp |= ((GPIO_Init->Mode & GPIO_MODE) << (position * 2)); */
      /* GPIOx->MODER = temp; */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if ((GPIO_Init->Mode & EXTI_MODE) != 0x00u)
      {
        /* Enable SYSCFG Clock - Hardware operation removed */
        /* __HAL_RCC_SYSCFG_CLK_ENABLE(); */

        /* Configure EXTI - Hardware operations removed */
        /* temp = SYSCFG->EXTICR[position >> 2]; */
        /* temp &= ~(((uint32_t)0x0F) << (4 * (position & 0x03))); */
        /* temp |= ((uint32_t)(GPIO_GET_INDEX(GPIOx)) << (4 * (position & 0x03))); */
        /* SYSCFG->EXTICR[position >> 2] = temp; */

        /* Clear Rising Falling edge configuration - Hardware operations removed */
        /* temp = EXTI->RTSR; */
        /* temp &= ~((uint32_t)iocurrent); */
        /* if ((GPIO_Init->Mode & TRIGGER_RISING) != 0x00u) */
        /* { */
        /*   temp |= iocurrent; */
        /* } */
        /* EXTI->RTSR = temp; */

        /* temp = EXTI->FTSR; */
        /* temp &= ~((uint32_t)iocurrent); */
        /* if ((GPIO_Init->Mode & TRIGGER_FALLING) != 0x00u) */
        /* { */
        /*   temp |= iocurrent; */
        /* } */
        /* EXTI->FTSR = temp; */

        /* temp = EXTI->EMR; */
        /* temp &= ~((uint32_t)iocurrent); */
        /* if ((GPIO_Init->Mode & EXTI_EVT) != 0x00u) */
        /* { */
        /*   temp |= iocurrent; */
        /* } */
        /* EXTI->EMR = temp; */

        /* Clear EXTI line configuration - Hardware operations removed */
        /* temp = EXTI->IMR; */
        /* temp &= ~((uint32_t)iocurrent); */
        /* if ((GPIO_Init->Mode & EXTI_IT) != 0x00u) */
        /* { */
        /*   temp |= iocurrent; */
        /* } */
        /* EXTI->IMR = temp; */
      }
    }
  }
}
```

=== 信息结束 ===
```

### HAL_HalfDuplex_Init

```text
=== HAL_HalfDuplex_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：435
- 函数内容：HAL_StatusTypeDef HAL_HalfDuplex_Init(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_HALFDUPLEX_INSTANCE(huart->Instance));
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Disable the peripheral */
  __HAL_UART_DISABLE(huart);

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* In half-duplex mode, the following bits must be kept cleared:
     - LINEN and CLKEN bits in the USART_CR2 register,
     - SCEN and IREN bits in the USART_CR3 register.*/
  CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN));
  CLEAR_BIT(huart->Instance->CR3, (USART_CR3_IREN | USART_CR3_SCEN));

  /* Enable the Half-Duplex mode by setting the HDSEL bit in the CR3 register */
  SET_BIT(huart->Instance->CR3, USART_CR3_HDSEL);

  /* Enable the peripheral */
  __HAL_UART_ENABLE(huart);

  /* Initialize the UART state*/
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes UART peripheral in half-duplex mode according to specified parameters and creates the associated handle.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs peripheral initialization (UART half-duplex mode configuration), 2) Contains direct hardware register accesses (CR2, CR3 registers via huart->Instance), 3) Calls low-level hardware initialization functions (HAL_UART_MspInit, UART_SetConfig), 4) Sets up the UART handle state and error codes, 5) Does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), contains no polling loops (not LOOP), and is not CORE (no NVIC/OS/VTOR configuration). The function follows the INIT strategy: removing MMIO/register access operations while preserving structure initialization, state management, and calls to other initialization functions (including potential NVIC configuration in HAL_UART_MspInit).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the half-duplex mode according to the specified
*         parameters in the UART_InitTypeDef and create the associated handle.
* @param  huart  Pointer to a UART_HandleTypeDef structure that contains
*                the configuration information for the specified UART module.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_HalfDuplex_Init(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_HALFDUPLEX_INSTANCE(huart->Instance));
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Skip hardware-specific configuration for simulation */
  /* Original: Disable the peripheral - __HAL_UART_DISABLE(huart); */
  /* Original: Set the UART Communication parameters - UART_SetConfig(huart); */
  /* Original: Clear bits in CR2 and CR3 registers for half-duplex mode */
  /* Original: Enable Half-Duplex mode by setting HDSEL bit in CR3 register */
  /* Original: Enable the peripheral - __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state*/
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_Init

```text
=== HAL_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c
- 行号：157
- 函数内容：HAL_StatusTypeDef HAL_Init(void)
{
  /* Configure Flash prefetch, Instruction cache, Data cache */ 
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  __HAL_FLASH_INSTRUCTION_CACHE_ENABLE();
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  __HAL_FLASH_DATA_CACHE_ENABLE();
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  __HAL_FLASH_PREFETCH_BUFFER_ENABLE();
#endif /* PREFETCH_ENABLE */

  /* Set Interrupt Group Priority */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the HAL library by configuring flash caches, setting NVIC priority grouping, initializing SysTick timer, and calling low-level hardware initialization
- 是否需要替换：是
- 分类/替换原因：HAL_Init is an initialization function that performs system-wide HAL library setup. Analysis of the function shows it calls: 1) HAL_NVIC_SetPriorityGrouping (CORE function for NVIC configuration), 2) HAL_InitTick (SysTick timer initialization), and 3) HAL_MspInit (user hardware initialization). According to classification rules, functions that call CORE functions may be classified as INIT, but their replacement must preserve calls to NVIC/OS/VTOR primitives. The verification process confirmed that both HAL_NVIC_SetPriorityGrouping and HAL_InitTick must be preserved for emulator simulation. The replacement removes only the hardware-specific flash cache configuration while preserving all function calls that are essential for system operation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  This function is used to initialize the HAL Library; it must be the first\n*         instruction to be executed in the main program (before to call any other\n*         HAL function), it performs the following:\n*           Configure the Flash prefetch, instruction and Data caches.\n*           Configures the SysTick to generate an interrupt each 1 millisecond,\n*           which is clocked by the HSI (at this stage, the clock is not yet\n*           configured and thus the system is running from the internal HSI at 16 MHz).\n*           Set NVIC Group Priority to 4.\n*           Calls the HAL_MspInit() callback function defined in user file\n*           \"stm32f4xx_hal_msp.c\" to do the global low level hardware initialization\n*\n* @note   SysTick is used as time base for the HAL_Delay() function, the application\n*         need to ensure that the SysTick time base is always set to 1 millisecond\n*         to have correct HAL operation.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_Init(void)\n{\n  /* Set Interrupt Group Priority - PRESERVED as this is a CORE function call */\n  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);\n\n  /* Use systick as time base source and configure 1ms tick - PRESERVED for emulator */\n  HAL_InitTick(TICK_INT_PRIORITY);\n\n  /* Skip hardware-specific flash cache configuration */\n  /* [INIT REMOVED] Flash prefetch, instruction cache, data cache configuration */\n\n  /* Call low-level hardware initialization */\n  HAL_MspInit();\n\n  /* Return function status */\n  return HAL_OK;\n}
```

【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_Init(void)
{
  /* [INIT REMOVED] Flash cache configuration removed for emulation */
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_INSTRUCTION_CACHE_ENABLE(); */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_DATA_CACHE_ENABLE(); */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
#endif /* PREFETCH_ENABLE */

  /* CRITICAL: NVIC priority grouping MUST be preserved for RTOS scheduling */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* CRITICAL: Systick initialization MUST be preserved for RTOS scheduling */
  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* CRITICAL: Low level hardware initialization MUST be called */
  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
- 更新原因：Fix HAL_Init to preserve critical RTOS scheduling operations and call HAL_MspInit(). According to critical requirements, NVIC priority grouping, Systick initialization, and MspInit calls must NOT be removed or replaced with empty stubs. These operations are essential for RTOS operation and context switching. Without HAL_MspInit(), peripheral interrupt initialization might be missing, causing issues with interrupt handling. Flash cache configurations are still removed as they are not critical for RTOS scheduling.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_Init(void)
{
  /* [INIT REMOVED] Flash cache configuration removed for emulation */
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_INSTRUCTION_CACHE_ENABLE(); */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_DATA_CACHE_ENABLE(); */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
#endif /* PREFETCH_ENABLE */

  /* CRITICAL: NVIC priority grouping MUST be preserved for RTOS scheduling */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* CRITICAL: Systick initialization MUST be preserved for RTOS scheduling */
  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* [INIT REMOVED] Low level hardware initialization removed for emulation */
  /* Init the low level hardware */
  /* HAL_MspInit(); */

  /* Return function status */
  return HAL_OK;
}
    原因：Fix HAL_Init to preserve critical RTOS scheduling operations. According to critical requirements, NVIC priority grouping and Systick initialization must NOT be removed or replaced with empty stubs. These operations are essential for RTOS operation and context switching. Without them, the scheduler startup can cause HardFault. Flash cache configurations and low-level hardware initialization are still removed as they are not critical for RTOS scheduling.
    时间：

  版本 2:
    替换代码：HAL_StatusTypeDef HAL_Init(void)
{
  /* [INIT REMOVED] Flash cache configuration removed for emulation */
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_INSTRUCTION_CACHE_ENABLE(); */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* __HAL_FLASH_DATA_CACHE_ENABLE(); */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
#endif /* PREFETCH_ENABLE */

  /* CRITICAL: NVIC priority grouping MUST be preserved for RTOS scheduling */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* CRITICAL: Systick initialization MUST be preserved for RTOS scheduling */
  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* CRITICAL: Low level hardware initialization MUST be called */
  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
    原因：Fix HAL_Init to preserve critical RTOS scheduling operations and call HAL_MspInit(). According to critical requirements, NVIC priority grouping, Systick initialization, and MspInit calls must NOT be removed or replaced with empty stubs. These operations are essential for RTOS operation and context switching. Without HAL_MspInit(), peripheral interrupt initialization might be missing, causing issues with interrupt handling. Flash cache configurations are still removed as they are not critical for RTOS scheduling.
    时间：

=== 信息结束 ===
```

### HAL_InitTick

```text
=== HAL_InitTick 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c
- 行号：253
- 函数内容：__weak HAL_StatusTypeDef HAL_InitTick(uint32_t TickPriority)
{
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  if (HAL_SYSTICK_Config(SystemCoreClock / (1000U / uwTickFreq)) > 0U)
  {
    return HAL_ERROR;
  }

  /* Configure the SysTick IRQ priority */
  if (TickPriority < (1UL << __NVIC_PRIO_BITS))
  {
    HAL_NVIC_SetPriority(SysTick_IRQn, TickPriority, 0U);
    uwTickPrio = TickPriority;
  }
  else
  {
    return HAL_ERROR;
  }

  /* Return function status */
  return HAL_OK;
}


【替换更新】
- 更新代码：__weak HAL_StatusTypeDef HAL_InitTick(uint32_t TickPriority)
{
  /* CRITICAL: SysTick configuration MUST be preserved for RTOS scheduling */
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  if (HAL_SYSTICK_Config(SystemCoreClock / (1000U / uwTickFreq)) > 0U)
  {
    return HAL_ERROR;
  }

  /* CRITICAL: SysTick IRQ priority configuration MUST be preserved for RTOS scheduling */
  /* Configure the SysTick IRQ priority */
  if (TickPriority < (1UL << __NVIC_PRIO_BITS))
  {
    HAL_NVIC_SetPriority(SysTick_IRQn, TickPriority, 0U);
    uwTickPrio = TickPriority;
  }
  else
  {
    return HAL_ERROR;
  }

  /* Return function status */
  return HAL_OK;
}
- 更新原因：Fix HAL_InitTick to preserve critical SysTick configuration for RTOS scheduling. According to critical requirements, SysTick initialization must NOT be removed or replaced with empty stubs. SysTick is essential for RTOS timekeeping and context switching. The function must preserve both SysTick timer configuration and interrupt priority setting to ensure proper RTOS operation and prevent scheduler startup failures.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：__weak HAL_StatusTypeDef HAL_InitTick(uint32_t TickPriority)
{
  /* [INIT REMOVED] SysTick configuration removed for emulation */
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  /* if (HAL_SYSTICK_Config(SystemCoreClock / (1000U / uwTickFreq)) > 0U) */
  /* { */
  /*   return HAL_ERROR; */
  /* } */

  /* [INIT REMOVED] SysTick IRQ priority configuration removed for emulation */
  /* Configure the SysTick IRQ priority */
  /* if (TickPriority < (1UL << __NVIC_PRIO_BITS)) */
  /* { */
  /*   HAL_NVIC_SetPriority(SysTick_IRQn, TickPriority, 0U); */
  /*   uwTickPrio = TickPriority; */
  /* } */
  /* else */
  /* { */
  /*   return HAL_ERROR; */
  /* } */

  /* Return function status */
  return HAL_OK;
}
    原因：HAL_InitTick configures SysTick timer for 1ms interrupts and sets interrupt priority. These are hardware operations that need to be removed for emulation. The function is called by HAL_Init during system initialization. The replacement removes all hardware-dependent operations while returning success to ensure system initialization completes without errors in emulation environment.
    时间：

  版本 2:
    替换代码：__weak HAL_StatusTypeDef HAL_InitTick(uint32_t TickPriority)
{
  /* CRITICAL: SysTick configuration MUST be preserved for RTOS scheduling */
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  if (HAL_SYSTICK_Config(SystemCoreClock / (1000U / uwTickFreq)) > 0U)
  {
    return HAL_ERROR;
  }

  /* CRITICAL: SysTick IRQ priority configuration MUST be preserved for RTOS scheduling */
  /* Configure the SysTick IRQ priority */
  if (TickPriority < (1UL << __NVIC_PRIO_BITS))
  {
    HAL_NVIC_SetPriority(SysTick_IRQn, TickPriority, 0U);
    uwTickPrio = TickPriority;
  }
  else
  {
    return HAL_ERROR;
  }

  /* Return function status */
  return HAL_OK;
}
    原因：Fix HAL_InitTick to preserve critical SysTick configuration for RTOS scheduling. According to critical requirements, SysTick initialization must NOT be removed or replaced with empty stubs. SysTick is essential for RTOS timekeeping and context switching. The function must preserve both SysTick timer configuration and interrupt priority setting to ensure proper RTOS operation and prevent scheduler startup failures.
    时间：

=== 信息结束 ===
```

### HAL_LIN_Init

```text
=== HAL_LIN_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：509
- 函数内容：HAL_StatusTypeDef HAL_LIN_Init(UART_HandleTypeDef *huart, uint32_t BreakDetectLength)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the LIN UART instance */
  assert_param(IS_UART_LIN_INSTANCE(huart->Instance));

  /* Check the Break detection length parameter */
  assert_param(IS_UART_LIN_BREAK_DETECT_LENGTH(BreakDetectLength));
  assert_param(IS_UART_LIN_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_LIN_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Disable the peripheral */
  __HAL_UART_DISABLE(huart);

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* In LIN mode, the following bits must be kept cleared:
     - CLKEN bits in the USART_CR2 register,
     - SCEN, HDSEL and IREN bits in the USART_CR3 register.*/
  CLEAR_BIT(huart->Instance->CR2, (USART_CR2_CLKEN));
  CLEAR_BIT(huart->Instance->CR3, (USART_CR3_HDSEL | USART_CR3_IREN | USART_CR3_SCEN));

  /* Enable the LIN mode by setting the LINEN bit in the CR2 register */
  SET_BIT(huart->Instance->CR2, USART_CR2_LINEN);

  /* Set the USART LIN Break detection length. */
  CLEAR_BIT(huart->Instance->CR2, USART_CR2_LBDL);
  SET_BIT(huart->Instance->CR2, BreakDetectLength);

  /* Enable the peripheral */
  __HAL_UART_ENABLE(huart);

  /* Initialize the UART state*/
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the LIN (Local Interconnect Network) mode for a UART peripheral according to specified parameters including break detection length.
- 是否需要替换：是
- 分类/替换原因：This function is a peripheral initialization function that configures LIN mode for UART. It contains multiple hardware register accesses (CR2, CR3 operations), calls hardware-specific functions (__HAL_UART_DISABLE, __HAL_UART_ENABLE, UART_SetConfig), and updates the UART handle state. It fits the INIT category as it performs hardware initialization and configuration. The replacement removes all MMIO operations while preserving structure initialization, state updates, and the call to HAL_UART_MspInit which may contain NVIC operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_LIN_Init(UART_HandleTypeDef *huart, uint32_t BreakDetectLength)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the LIN UART instance */
  assert_param(IS_UART_LIN_INSTANCE(huart->Instance));

  /* Check the Break detection length parameter */
  assert_param(IS_UART_LIN_BREAK_DETECT_LENGTH(BreakDetectLength));
  assert_param(IS_UART_LIN_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_LIN_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Skip hardware-specific configuration */
  /* Original: __HAL_UART_DISABLE(huart); */
  /* Original: UART_SetConfig(huart); */
  /* Original: CLEAR_BIT(huart->Instance->CR2, (USART_CR2_CLKEN)); */
  /* Original: CLEAR_BIT(huart->Instance->CR3, (USART_CR3_HDSEL | USART_CR3_IREN | USART_CR3_SCEN)); */
  /* Original: SET_BIT(huart->Instance->CR2, USART_CR2_LINEN); */
  /* Original: CLEAR_BIT(huart->Instance->CR2, USART_CR2_LBDL); */
  /* Original: SET_BIT(huart->Instance->CR2, BreakDetectLength); */
  /* Original: __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state*/
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_MultiProcessor_Init

```text
=== HAL_MultiProcessor_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：591
- 函数内容：HAL_StatusTypeDef HAL_MultiProcessor_Init(UART_HandleTypeDef *huart, uint8_t Address, uint32_t WakeUpMethod)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_INSTANCE(huart->Instance));

  /* Check the Address & wake up method parameters */
  assert_param(IS_UART_WAKEUPMETHOD(WakeUpMethod));
  assert_param(IS_UART_ADDRESS(Address));
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Disable the peripheral */
  __HAL_UART_DISABLE(huart);

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* In Multi-Processor mode, the following bits must be kept cleared:
     - LINEN and CLKEN bits in the USART_CR2 register,
     - SCEN, HDSEL and IREN  bits in the USART_CR3 register */
  CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN));
  CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN));

  /* Set the USART address node */
  CLEAR_BIT(huart->Instance->CR2, USART_CR2_ADD);
  SET_BIT(huart->Instance->CR2, Address);

  /* Set the wake up method by setting the WAKE bit in the CR1 register */
  CLEAR_BIT(huart->Instance->CR1, USART_CR1_WAKE);
  SET_BIT(huart->Instance->CR1, WakeUpMethod);

  /* Enable the peripheral */
  __HAL_UART_ENABLE(huart);

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes UART in multi-processor mode, configuring address nodes and wake-up methods for multi-processor communication.
- 是否需要替换：是
- 分类/替换原因：This function is an initialization function that configures UART hardware for multi-processor mode. Analysis shows: 1) It contains multiple MMIO register writes (CR1, CR2, CR3 control registers) to configure the peripheral; 2) It performs hardware enable/disable operations; 3) It calls UART_SetConfig for communication parameter setup; 4) It initializes the UART handle state and error codes; 5) It calls HAL_UART_MspInit for low-level hardware initialization. The function fits the INIT classification criteria: it initializes peripheral configurations, contains MMIO/register access operations that need removal, and preserves resource allocation and structure initialization. It is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler), not LOOP (no polling loops), not RETURNOK/SKIP (has significant hardware operations), and not NODRIVER (clearly a hardware driver function).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_MultiProcessor_Init(UART_HandleTypeDef *huart, uint8_t Address, uint32_t WakeUpMethod)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_INSTANCE(huart->Instance));

  /* Check the Address & wake up method parameters */
  assert_param(IS_UART_WAKEUPMETHOD(WakeUpMethod));
  assert_param(IS_UART_ADDRESS(Address));
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Skip hardware-specific configuration for Multi-Processor mode */
  /* Original hardware operations removed:
     - __HAL_UART_DISABLE(huart);
     - UART_SetConfig(huart);
     - CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN));
     - CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN));
     - CLEAR_BIT(huart->Instance->CR2, USART_CR2_ADD);
     - SET_BIT(huart->Instance->CR2, Address);
     - CLEAR_BIT(huart->Instance->CR1, USART_CR1_WAKE);
     - SET_BIT(huart->Instance->CR1, WakeUpMethod);
     - __HAL_UART_ENABLE(huart);
  */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_NVIC_EnableIRQ

```text
=== HAL_NVIC_EnableIRQ 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c
- 行号：185
- 函数内容：void HAL_NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* Check the parameters */
  assert_param(IS_NVIC_DEVICE_IRQ(IRQn));
  
  /* Enable interrupt */
  NVIC_EnableIRQ(IRQn);
}


【替换更新】
- 更新代码：void HAL_NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* Check the parameters */
  assert_param(IS_NVIC_DEVICE_IRQ(IRQn));
  
  /* CRITICAL: NVIC interrupt enable MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_EnableIRQ which writes to NVIC->ISER register */
  NVIC_EnableIRQ(IRQn);
}
- 更新原因：Create replacement for HAL_NVIC_EnableIRQ that preserves critical NVIC interrupt enable configuration. According to critical requirements, NVIC enable writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling. The function calls NVIC_EnableIRQ (CMSIS inline) which writes to NVIC->ISER register that must be preserved for proper emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* Check the parameters */
  assert_param(IS_NVIC_DEVICE_IRQ(IRQn));
  
  /* CRITICAL: NVIC interrupt enable MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_EnableIRQ which writes to NVIC->ISER register */
  NVIC_EnableIRQ(IRQn);
}
    原因：Create replacement for HAL_NVIC_EnableIRQ that preserves critical NVIC interrupt enable configuration. According to critical requirements, NVIC enable writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling. The function calls NVIC_EnableIRQ (CMSIS inline) which writes to NVIC->ISER register that must be preserved for proper emulation.
    时间：

=== 信息结束 ===
```

### HAL_NVIC_SetPriority

```text
=== HAL_NVIC_SetPriority 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c
- 行号：163
- 函数内容：void HAL_NVIC_SetPriority(IRQn_Type IRQn, uint32_t PreemptPriority, uint32_t SubPriority)
{ 
  uint32_t prioritygroup = 0x00U;
  
  /* Check the parameters */
  assert_param(IS_NVIC_SUB_PRIORITY(SubPriority));
  assert_param(IS_NVIC_PREEMPTION_PRIORITY(PreemptPriority));
  
  prioritygroup = NVIC_GetPriorityGrouping();
  
  NVIC_SetPriority(IRQn, NVIC_EncodePriority(prioritygroup, PreemptPriority, SubPriority));
}


【替换更新】
- 更新代码：void HAL_NVIC_SetPriority(IRQn_Type IRQn, uint32_t PreemptPriority, uint32_t SubPriority)
{ 
  uint32_t prioritygroup = 0x00U;
  
  /* Check the parameters */
  assert_param(IS_NVIC_SUB_PRIORITY(SubPriority));
  assert_param(IS_NVIC_PREEMPTION_PRIORITY(PreemptPriority));
  
  prioritygroup = NVIC_GetPriorityGrouping();
  
  /* CRITICAL: NVIC priority configuration MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_SetPriority which writes to NVIC->IP or SCB->SHP registers */
  NVIC_SetPriority(IRQn, NVIC_EncodePriority(prioritygroup, PreemptPriority, SubPriority));
}
- 更新原因：Create replacement for HAL_NVIC_SetPriority that preserves critical NVIC priority configuration. According to critical requirements, NVIC priority writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling and scheduler operation. The function calls NVIC_SetPriority (CMSIS inline) which writes to hardware registers that must be preserved for proper emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_NVIC_SetPriority(IRQn_Type IRQn, uint32_t PreemptPriority, uint32_t SubPriority)
{ 
  uint32_t prioritygroup = 0x00U;
  
  /* Check the parameters */
  assert_param(IS_NVIC_SUB_PRIORITY(SubPriority));
  assert_param(IS_NVIC_PREEMPTION_PRIORITY(PreemptPriority));
  
  prioritygroup = NVIC_GetPriorityGrouping();
  
  /* CRITICAL: NVIC priority configuration MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_SetPriority which writes to NVIC->IP or SCB->SHP registers */
  NVIC_SetPriority(IRQn, NVIC_EncodePriority(prioritygroup, PreemptPriority, SubPriority));
}
    原因：Create replacement for HAL_NVIC_SetPriority that preserves critical NVIC priority configuration. According to critical requirements, NVIC priority writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling and scheduler operation. The function calls NVIC_SetPriority (CMSIS inline) which writes to hardware registers that must be preserved for proper emulation.
    时间：

=== 信息结束 ===
```

### HAL_NVIC_SetPriorityGrouping

```text
=== HAL_NVIC_SetPriorityGrouping 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c
- 行号：141
- 函数内容：void HAL_NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  /* Check the parameters */
  assert_param(IS_NVIC_PRIORITY_GROUP(PriorityGroup));
  
  /* Set the PRIGROUP[10:8] bits according to the PriorityGroup parameter value */
  NVIC_SetPriorityGrouping(PriorityGroup);
}


【替换更新】
- 更新代码：void HAL_NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  /* Check the parameters */
  assert_param(IS_NVIC_PRIORITY_GROUP(PriorityGroup));
  
  /* CRITICAL: NVIC priority grouping configuration MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_SetPriorityGrouping which writes to SCB->AIRCR register */
  NVIC_SetPriorityGrouping(PriorityGroup);
}
- 更新原因：Create replacement for HAL_NVIC_SetPriorityGrouping that preserves critical NVIC priority grouping configuration. According to critical requirements, NVIC configuration writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling. The function calls NVIC_SetPriorityGrouping (CMSIS inline) which writes to SCB->AIRCR register that must be preserved for proper emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  /* Check the parameters */
  assert_param(IS_NVIC_PRIORITY_GROUP(PriorityGroup));
  
  /* CRITICAL: NVIC priority grouping configuration MUST be preserved for RTOS interrupt handling */
  /* This calls NVIC_SetPriorityGrouping which writes to SCB->AIRCR register */
  NVIC_SetPriorityGrouping(PriorityGroup);
}
    原因：Create replacement for HAL_NVIC_SetPriorityGrouping that preserves critical NVIC priority grouping configuration. According to critical requirements, NVIC configuration writes must NOT be removed or stubbed as they are essential for RTOS interrupt handling. The function calls NVIC_SetPriorityGrouping (CMSIS inline) which writes to SCB->AIRCR register that must be preserved for proper emulation.
    时间：

=== 信息结束 ===
```

### HAL_PWREx_ControlVoltageScaling

```text
=== HAL_PWREx_ControlVoltageScaling 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c
- 行号：288
- 函数内容：HAL_StatusTypeDef HAL_PWREx_ControlVoltageScaling(uint32_t VoltageScaling)
{
  uint32_t tickstart = 0U;
  
  assert_param(IS_PWR_VOLTAGE_SCALING_RANGE(VoltageScaling));
  
  /* Enable PWR RCC Clock Peripheral */
  __HAL_RCC_PWR_CLK_ENABLE();
  
  /* Check if the PLL is used as system clock or not */
  if(__HAL_RCC_GET_SYSCLK_SOURCE() != RCC_CFGR_SWS_PLL)
  {
    /* Disable the main PLL */
    __HAL_RCC_PLL_DISABLE();
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();    
    /* Wait till PLL is disabled */  
    while(__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) != RESET)
    {
      if((HAL_GetTick() - tickstart ) > PLL_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      }
    }
    
    /* Set Range */
    __HAL_PWR_VOLTAGESCALING_CONFIG(VoltageScaling);
    
    /* Enable the main PLL */
    __HAL_RCC_PLL_ENABLE();
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();
    /* Wait till PLL is ready */  
    while(__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) == RESET)
    {
      if((HAL_GetTick() - tickstart ) > PLL_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      } 
    }
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();
    while((__HAL_PWR_GET_FLAG(PWR_FLAG_VOSRDY) == RESET))
    {
      if((HAL_GetTick() - tickstart ) > PWR_VOSRDY_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      } 
    }
  }
  else
  {
    return HAL_ERROR;
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures the main internal regulator output voltage for power-performance tradeoff by setting voltage scaling modes (Scale1: 1.4V, Scale2: 1.2V, Scale3: 1.0V).
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a power management configuration function that performs hardware initialization. GetMMIOFunctionInfo showed multiple register access operations including clock enable/disable, voltage scaling configuration, and flag checking. The function contains hardware-dependent polling loops waiting for PLL and voltage scaling ready flags. This is an initialization function that configures peripheral hardware (power management registers) and contains MMIO operations that need to be removed while preserving the logical flow and timeout handling structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Configures the main internal regulator output voltage.
* @param  VoltageScaling specifies the regulator output voltage to achieve
*         a tradeoff between performance and power consumption.
*          This parameter can be one of the following values:
*            @arg PWR_REGULATOR_VOLTAGE_SCALE1: Regulator voltage output range 1 mode,
*                                                typical output voltage at 1.4 V,
*                                                system frequency up to 216 MHz.
*            @arg PWR_REGULATOR_VOLTAGE_SCALE2: Regulator voltage output range 2 mode,
*                                                typical output voltage at 1.2 V,
*                                                system frequency up to 180 MHz.
*            @arg PWR_REGULATOR_VOLTAGE_SCALE3: Regulator voltage output range 2 mode,
*                                                typical output voltage at 1.00 V,
*                                                system frequency up to 151 MHz.
* @note To update the system clock frequency(SYSCLK):
*        - Set the HSI or HSE as system clock frequency using the HAL_RCC_ClockConfig().
*        - Call the HAL_RCC_OscConfig() to configure the PLL.
*        - Call HAL_PWREx_ConfigVoltageScaling() API to adjust the voltage scale.
*        - Set the new system clock frequency using the HAL_RCC_ClockConfig().
* @note The scale can be modified only when the HSI or HSE clock source is selected
*        as system clock source, otherwise the API returns HAL_ERROR.
* @note When the PLL is OFF, the voltage scale 3 is automatically selected and the VOS bits
*       value in the PWR_CR1 register are not taken in account.
* @note This API forces the PLL state ON to allow the possibility to configure the voltage scale 1 or 2.
* @note The new voltage scale is active only when the PLL is ON.
* @retval HAL Status
*/
HAL_StatusTypeDef HAL_PWREx_ControlVoltageScaling(uint32_t VoltageScaling)
{
  uint32_t tickstart = 0;

  assert_param(IS_PWR_REGULATOR_VOLTAGE(VoltageScaling));

  /* Skip hardware clock enable */
  /* __HAL_RCC_PWR_CLK_ENABLE(); */

  /* Check if the PLL is used as system clock or not */
  /* Simulate that PLL is not used as system clock to allow voltage scaling configuration */
  if(1) /* Assume PLL is not used as system clock to proceed with configuration */
  {
    /* Skip PLL disable/enable operations */
    /* __HAL_RCC_PLL_DISABLE(); */
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();    
    /* [LOOP REMOVED] Wait till PLL is disabled - assume already disabled */
    
    /* Skip voltage scaling hardware configuration */
    /* __HAL_PWR_VOLTAGESCALING_CONFIG(VoltageScaling); */
    
    /* Skip PLL enable operation */
    /* __HAL_RCC_PLL_ENABLE(); */
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();
    /* [LOOP REMOVED] Wait till PLL is ready - assume already ready */
    
    /* Get Start Tick */
    tickstart = HAL_GetTick();
    /* [LOOP REMOVED] Wait for voltage scaling ready - assume already ready */
  }
  else
  {
    return HAL_ERROR;
  }
  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_PWREx_DisableBkUpReg

```text
=== HAL_PWREx_DisableBkUpReg 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c
- 行号：165
- 函数内容：HAL_StatusTypeDef HAL_PWREx_DisableBkUpReg(void)
{
  uint32_t tickstart = 0U;

  *(__IO uint32_t *) CSR_BRE_BB = (uint32_t)DISABLE;

  /* Get tick */
  tickstart = HAL_GetTick();

  /* Wait till Backup regulator ready flag is set */  
  while(__HAL_PWR_GET_FLAG(PWR_FLAG_BRR) != RESET)
  {
    if((HAL_GetTick() - tickstart ) > PWR_BKPREG_TIMEOUT_VALUE)
    {
      return HAL_TIMEOUT;
    } 
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Disables the Backup Regulator in the STM32 power control system with timeout handling
- 是否需要替换：是
- 分类/替换原因：The function contains a peripheral-dependent polling loop (while(__HAL_PWR_GET_FLAG(PWR_FLAG_BRR) != RESET)) waiting for a hardware status flag to clear. GetMMIOFunctionInfo revealed multiple MMIO register accesses (PWR->CSR1 operations) and a binary operation for flag checking. The function performs hardware configuration but the key characteristic is the polling loop waiting for hardware status, making it fit the LOOP classification. It also has timeout handling logic using HAL_GetTick().
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Disables the Backup Regulator.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_PWREx_DisableBkUpReg(void)
{
  /* [LOOP REMOVED] Skip hardware register operations for backup regulator disable */
  /* [LOOP REMOVED] Skip waiting for backup regulator ready flag */
  
  /* Return success immediately, assuming operation completed */
  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_PWREx_EnableBkUpReg

```text
=== HAL_PWREx_EnableBkUpReg 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c
- 行号：141
- 函数内容：HAL_StatusTypeDef HAL_PWREx_EnableBkUpReg(void)
{
  uint32_t tickstart = 0U;

  *(__IO uint32_t *) CSR_BRE_BB = (uint32_t)ENABLE;

  /* Get tick */
  tickstart = HAL_GetTick();

  /* Wait till Backup regulator ready flag is set */  
  while(__HAL_PWR_GET_FLAG(PWR_FLAG_BRR) == RESET)
  {
    if((HAL_GetTick() - tickstart ) > PWR_BKPREG_TIMEOUT_VALUE)
    {
      return HAL_TIMEOUT;
    } 
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables the Backup Regulator in the STM32 power control system and waits for it to become ready
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs hardware initialization by writing to PWR->CSR1 registers to enable backup regulator. GetMMIOFunctionInfo confirmed two MMIO write operations and one MMIO read operation in a polling loop. The function's primary purpose is hardware initialization with a polling wait for status flag, which matches the INIT classification. It contains no data transmission/reception (not RECV), no interrupt handling (not IRQ), but does contain a polling loop (LOOP characteristic). According to priority order, INIT takes precedence over LOOP as the main purpose is initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief Enables the Backup Regulator.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_PWREx_EnableBkUpReg(void)\n{\n  uint32_t tickstart = 0;\n\n  /* [INIT REMOVED] Enable Backup regulator - original: PWR->CSR1 |= PWR_CSR1_BRE; */\n  \n  /* [INIT REMOVED] Workaround for hardware bug - original: PWR->CSR1 |= PWR_CSR1_EIWUP; */\n\n  /* Get tick */\n  tickstart = HAL_GetTick();\n\n  /* [LOOP REMOVED] Wait till Backup regulator ready flag is set - assume ready */\n  /* Original polling loop removed, assume regulator is ready */\n  \n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### HAL_PWR_ConfigPVD

```text
=== HAL_PWR_ConfigPVD 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：275
- 函数内容：void HAL_PWR_ConfigPVD(PWR_PVDTypeDef *sConfigPVD)
{
  /* Check the parameters */
  assert_param(IS_PWR_PVD_LEVEL(sConfigPVD->PVDLevel));
  assert_param(IS_PWR_PVD_MODE(sConfigPVD->Mode));
  
  /* Set PLS[7:5] bits according to PVDLevel value */
  MODIFY_REG(PWR->CR, PWR_CR_PLS, sConfigPVD->PVDLevel);
  
  /* Clear any previous config. Keep it clear if no event or IT mode is selected */
  __HAL_PWR_PVD_EXTI_DISABLE_EVENT();
  __HAL_PWR_PVD_EXTI_DISABLE_IT();
  __HAL_PWR_PVD_EXTI_DISABLE_RISING_EDGE();
  __HAL_PWR_PVD_EXTI_DISABLE_FALLING_EDGE(); 

  /* Configure interrupt mode */
  if((sConfigPVD->Mode & PVD_MODE_IT) == PVD_MODE_IT)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_IT();
  }
  
  /* Configure event mode */
  if((sConfigPVD->Mode & PVD_MODE_EVT) == PVD_MODE_EVT)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_EVENT();
  }
  
  /* Configure the edge */
  if((sConfigPVD->Mode & PVD_RISING_EDGE) == PVD_RISING_EDGE)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_RISING_EDGE();
  }
  
  if((sConfigPVD->Mode & PVD_FALLING_EDGE) == PVD_FALLING_EDGE)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_FALLING_EDGE();
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures the Power Voltage Detector (PVD) peripheral with specified voltage threshold and interrupt/event modes
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization and configuration of the Power Voltage Detector peripheral. Analysis shows it contains MMIO operations (MODIFY_REG(PWR->CR, ...)) and configures EXTI interrupt/event settings. The function validates parameters and sets up hardware registers based on the input configuration structure. As an INIT function, hardware-specific operations should be removed while preserving parameter validation and structure handling. GetMMIOFunctionInfo indicated hardware register accesses, and the function's purpose aligns with peripheral initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_PWR_ConfigPVD(PWR_PVDTypeDef *sConfigPVD)
{
  /* Check the parameters */
  assert_param(IS_PWR_PVD_LEVEL(sConfigPVD->PVDLevel));
  assert_param(IS_PWR_PVD_MODE(sConfigPVD->Mode));
  
  /* Skip hardware-specific configuration */
  /* Original: MODIFY_REG(PWR->CR, PWR_CR_PLS, sConfigPVD->PVDLevel); */
  
  /* Skip EXTI configuration for PVD */
  /* Original: __HAL_PWR_PVD_EXTI_DISABLE_EVENT(); */
  /* Original: __HAL_PWR_PVD_EXTI_DISABLE_IT(); */
  /* Original: __HAL_PWR_PVD_EXTI_DISABLE_RISING_EDGE(); */
  /* Original: __HAL_PWR_PVD_EXTI_DISABLE_FALLING_EDGE(); */
  
  /* Skip interrupt mode configuration */
  /* Original: if((sConfigPVD->Mode & PVD_MODE_IT) == PVD_MODE_IT) { __HAL_PWR_PVD_EXTI_ENABLE_IT(); } */
  
  /* Skip event mode configuration */
  /* Original: if((sConfigPVD->Mode & PVD_MODE_EVT) == PVD_MODE_EVT) { __HAL_PWR_PVD_EXTI_ENABLE_EVENT(); } */
  
  /* Skip edge configuration */
  /* Original: if((sConfigPVD->Mode & PVD_RISING_EDGE) == PVD_RISING_EDGE) { __HAL_PWR_PVD_EXTI_ENABLE_RISING_EDGE(); } */
  /* Original: if((sConfigPVD->Mode & PVD_FALLING_EDGE) == PVD_FALLING_EDGE) { __HAL_PWR_PVD_EXTI_ENABLE_FALLING_EDGE(); } */
}
```

=== 信息结束 ===
```

### HAL_PWR_EnterSTOPMode

```text
=== HAL_PWR_EnterSTOPMode 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：445
- 函数内容：void HAL_PWR_EnterSTOPMode(uint32_t Regulator, uint8_t STOPEntry)
{
  /* Check the parameters */
  assert_param(IS_PWR_REGULATOR(Regulator));
  assert_param(IS_PWR_STOP_ENTRY(STOPEntry));
  
  /* Select the regulator state in Stop mode: Set PDDS and LPDS bits according to PWR_Regulator value */
  MODIFY_REG(PWR->CR, (PWR_CR_PDDS | PWR_CR_LPDS), Regulator);
  
  /* Set SLEEPDEEP bit of Cortex System Control Register */
  SET_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk));
  
  /* Select Stop mode entry --------------------------------------------------*/
  if(STOPEntry == PWR_STOPENTRY_WFI)
  {   
    /* Request Wait For Interrupt */
    __WFI();
  }
  else
  {
    if(STOPEntry != PWR_STOPENTRY_WFE_NO_EVT_CLEAR)
    {
      /* Clear all pending event */
      __SEV();
      __WFE();
    }
    /* Request Wait For Event */
    __WFE();
  }
  /* Reset SLEEPDEEP bit of Cortex System Control Register */
  CLEAR_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk));  
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enters the microcontroller into STOP mode (low-power mode) by configuring power regulator settings and executing WFI/WFE instructions.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It initializes/configure the system for low-power STOP mode by setting hardware registers (PWR->CR for power control and SCB->SCR for sleep mode configuration). 2) It performs hardware-dependent operations including register writes and low-level CPU instructions (__WFI, __WFE, __SEV). 3) It doesn't perform data transmission/reception (not RECV), isn't an interrupt handler (not IRQ), doesn't contain peripheral-dependent polling loops (not LOOP), and isn't a simple return function (not RETURNOK). 4) It's not a CORE function because it doesn't configure NVIC, OS scheduler, or VTOR - it only sets SLEEPDEEP bit for low-power mode which is not core OS functionality. 5) The function contains MMIO operations (PWR->CR access) identified in the original code, confirming hardware dependency.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_PWR_EnterSTOPMode(uint32_t Regulator, uint8_t STOPEntry)
{
  /* Check the parameters */
  assert_param(IS_PWR_REGULATOR(Regulator));
  assert_param(IS_PWR_STOP_ENTRY(STOPEntry));
  
  /* Skip hardware-specific configuration */
  /* Original: MODIFY_REG(PWR->CR, (PWR_CR_PDDS | PWR_CR_LPDS), Regulator); */
  
  /* Skip setting SLEEPDEEP bit */
  /* Original: SET_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk)); */
  
  /* Select Stop mode entry --------------------------------------------------*/
  if(STOPEntry == PWR_STOPENTRY_WFI)
  {   
    /* Skip Wait For Interrupt instruction */
    /* Original: __WFI(); */
  }
  else
  {
    if(STOPEntry != PWR_STOPENTRY_WFE_NO_EVT_CLEAR)
    {
      /* Skip event clearing */
      /* Original: __SEV(); */
      /* Original: __WFE(); */
    }
    /* Skip Wait For Event instruction */
    /* Original: __WFE(); */
  }
  /* Skip resetting SLEEPDEEP bit */
  /* Original: CLEAR_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk)); */
}
```

=== 信息结束 ===
```

### HAL_PWR_PVD_IRQHandler

```text
=== HAL_PWR_PVD_IRQHandler 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：509
- 函数内容：void HAL_PWR_PVD_IRQHandler(void)
{
  /* Check PWR Exti flag */
  if(__HAL_PWR_PVD_EXTI_GET_FLAG() != RESET)
  {
    /* PWR PVD interrupt user callback */
    HAL_PWR_PVDCallback();
    
    /* Clear PWR Exti pending bit */
    __HAL_PWR_PVD_EXTI_CLEAR_FLAG();
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Interrupt handler for Power Voltage Detector (PVD) interrupt that checks PVD EXTI flag and calls user callback function.
- 是否需要替换：是
- 分类/替换原因：This function is clearly an interrupt handler as indicated by its name 'IRQHandler'. It performs hardware-specific operations: checking the PVD EXTI flag using __HAL_PWR_PVD_EXTI_GET_FLAG() and clearing it with __HAL_PWR_PVD_EXTI_CLEAR_FLAG(). It then calls the user callback HAL_PWR_PVDCallback(). According to the classification priority, IRQ functions handle interrupt-related operations and should have hardware operations removed while preserving callback invocation and execution flow. This is not a CORE function (no NVIC/OS kernel/VTOR operations), not a RECV function (no data transmission/reception), and specifically fits the IRQ category for interrupt handlers.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief This function handles the PWR PVD interrupt request.
* @note This API should be called under the PVD_IRQHandler().
* @retval None
*/
void HAL_PWR_PVD_IRQHandler(void)
{
  /* Simulate PVD interrupt flag being set */
  /* PWR PVD interrupt user callback */
  HAL_PWR_PVDCallback();
  
  /* No need to clear hardware interrupt flags in simulation */
}
```

=== 信息结束 ===
```

### HAL_RCCEx_DisablePLLI2S

```text
=== HAL_RCCEx_DisablePLLI2S 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c
- 行号：2929
- 函数内容：HAL_StatusTypeDef HAL_RCCEx_DisablePLLI2S(void)
{
  uint32_t tickstart;

  /* Disable the PLLI2S */
  __HAL_RCC_PLLI2S_DISABLE();

  /* Wait till PLLI2S is disabled */
  tickstart = HAL_GetTick();
  while (READ_BIT(RCC->CR, RCC_CR_PLLI2SRDY) != RESET)
  {
    if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
    {
      /* return in case of Timeout detected */
      return HAL_TIMEOUT;
    }
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Disables the PLLI2S peripheral and waits for it to be fully disabled by polling the hardware status register.
- 是否需要替换：是
- 分类/替换原因：This function contains a hardware-dependent polling loop that waits for the PLLI2S status flag (RCC_CR_PLLI2SRDY) to be cleared. The loop condition depends on reading from the RCC->CR hardware register. According to the classification criteria, functions with peripheral-dependent loops where the condition or body depends on peripheral registers should be classified as LOOP. The function performs a pure driver operation (disabling PLLI2S) but includes a critical polling loop that needs to be handled.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  Disable PLLI2S.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_RCCEx_DisablePLLI2S(void)\n{\n  uint32_t tickstart;\n\n  /* Disable the PLLI2S */\n  /* [HARDWARE OPERATION REMOVED] __HAL_RCC_PLLI2S_DISABLE(); */\n\n  /* Wait till PLLI2S is disabled */\n  tickstart = HAL_GetTick();\n  /* [LOOP REMOVED] Waited for hardware PLLI2S disable status flag */\n  /* while(READ_BIT(RCC->CR, RCC_CR_PLLI2SRDY) != RESET)\n  {\n    if((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)\n    {\n      return HAL_TIMEOUT;\n    }\n  } */\n\n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### HAL_RCCEx_EnablePLLI2S

```text
=== HAL_RCCEx_EnablePLLI2S 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c
- 行号：2846
- 函数内容：HAL_StatusTypeDef HAL_RCCEx_EnablePLLI2S(RCC_PLLI2SInitTypeDef  *PLLI2SInit)
{
  uint32_t tickstart;

  /* Check for parameters */
  assert_param(IS_RCC_PLLI2SN_VALUE(PLLI2SInit->PLLI2SN));
  assert_param(IS_RCC_PLLI2SR_VALUE(PLLI2SInit->PLLI2SR));
#if defined(RCC_PLLI2SCFGR_PLLI2SM)
  assert_param(IS_RCC_PLLI2SM_VALUE(PLLI2SInit->PLLI2SM));
#endif /* RCC_PLLI2SCFGR_PLLI2SM */
#if defined(RCC_PLLI2SCFGR_PLLI2SP)
  assert_param(IS_RCC_PLLI2SP_VALUE(PLLI2SInit->PLLI2SP));
#endif /* RCC_PLLI2SCFGR_PLLI2SP */
#if defined(RCC_PLLI2SCFGR_PLLI2SQ)
  assert_param(IS_RCC_PLLI2SQ_VALUE(PLLI2SInit->PLLI2SQ));
#endif /* RCC_PLLI2SCFGR_PLLI2SQ */

  /* Disable the PLLI2S */
  __HAL_RCC_PLLI2S_DISABLE();

  /* Wait till PLLI2S is disabled */
  tickstart = HAL_GetTick();
  while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLI2SRDY) != RESET)
  {
    if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
    {
      /* return in case of Timeout detected */
      return HAL_TIMEOUT;
    }
  }

  /* Configure the PLLI2S division factors */
#if defined(STM32F446xx)
  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * (PLLI2SN/PLLI2SM) */
  /* I2SPCLK = PLLI2S_VCO / PLLI2SP */
  /* I2SQCLK = PLLI2S_VCO / PLLI2SQ */
  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */
  __HAL_RCC_PLLI2S_CONFIG(PLLI2SInit->PLLI2SM, PLLI2SInit->PLLI2SN, \
                          PLLI2SInit->PLLI2SP, PLLI2SInit->PLLI2SQ, PLLI2SInit->PLLI2SR);
#elif defined(STM32F412Zx) || defined(STM32F412Vx) || defined(STM32F412Rx) || defined(STM32F412Cx) ||\
      defined(STM32F413xx) || defined(STM32F423xx)
  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * (PLLI2SN/PLLI2SM)*/
  /* I2SQCLK = PLLI2S_VCO / PLLI2SQ */
  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */
  __HAL_RCC_PLLI2S_CONFIG(PLLI2SInit->PLLI2SM, PLLI2SInit->PLLI2SN, \
                          PLLI2SInit->PLLI2SQ, PLLI2SInit->PLLI2SR);
#elif defined(STM32F427xx) || defined(STM32F437xx) || defined(STM32F429xx) || defined(STM32F439xx) ||\
      defined(STM32F469xx) || defined(STM32F479xx)
  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * PLLI2SN */
  /* I2SQCLK = PLLI2S_VCO / PLLI2SQ */
  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */
  __HAL_RCC_PLLI2S_SAICLK_CONFIG(PLLI2SInit->PLLI2SN, PLLI2SInit->PLLI2SQ, PLLI2SInit->PLLI2SR);
#elif defined(STM32F411xE)
  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * (PLLI2SN/PLLI2SM) */
  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */
  __HAL_RCC_PLLI2S_I2SCLK_CONFIG(PLLI2SInit->PLLI2SM, PLLI2SInit->PLLI2SN, PLLI2SInit->PLLI2SR);
#else
  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) x PLLI2SN */
  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */
  __HAL_RCC_PLLI2S_CONFIG(PLLI2SInit->PLLI2SN, PLLI2SInit->PLLI2SR);
#endif /* STM32F446xx */

  /* Enable the PLLI2S */
  __HAL_RCC_PLLI2S_ENABLE();

  /* Wait till PLLI2S is ready */
  tickstart = HAL_GetTick();
  while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLI2SRDY) == RESET)
  {
    if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
    {
      /* return in case of Timeout detected */
      return HAL_TIMEOUT;
    }
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables and configures the PLLI2S (Phase-Locked Loop for I2S audio interface) with specified clock division factors
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a peripheral initialization function that configures PLLI2S clock settings. GetMMIOFunctionInfo identified multiple MMIO operations including register writes and status flag polling. The function contains hardware-specific macros (__HAL_RCC_PLLI2S_DISABLE, __HAL_RCC_PLLI2S_ENABLE, __HAL_RCC_PLLI2S_CONFIG) and polling loops waiting for hardware status flags. It performs parameter validation and timeout handling. This matches the INIT classification criteria: functions that initialize peripheral/configurations with hardware register access operations that need to be removed while preserving non-hardware logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  Enable PLLI2S.\n* @param  PLLI2SInit  pointer to an RCC_PLLI2SInitTypeDef structure that\n*         contains the configuration information for the PLLI2S\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_RCCEx_EnablePLLI2S(RCC_PLLI2SInitTypeDef  *PLLI2SInit)\n{\n  uint32_t tickstart;\n\n  /* Check for parameters */\n  assert_param(IS_RCC_PLLI2SN_VALUE(PLLI2SInit->PLLI2SN));\n  assert_param(IS_RCC_PLLI2SR_VALUE(PLLI2SInit->PLLI2SR));\n  assert_param(IS_RCC_PLLI2SQ_VALUE(PLLI2SInit->PLLI2SQ));\n#if defined(RCC_PLLI2SCFGR_PLLI2SP)\n  assert_param(IS_RCC_PLLI2SP_VALUE(PLLI2SInit->PLLI2SP));\n#endif /* RCC_PLLI2SCFGR_PLLI2SP */\n\n  /* Skip hardware disable operation */\n  /* __HAL_RCC_PLLI2S_DISABLE(); */\n\n  /* Skip waiting for PLLI2S to be disabled */\n  /* [LOOP REMOVED] Waited for hardware PLLI2S disabled flag */\n\n  /* Skip hardware configuration */\n  /* Configure the PLLI2S division factors */\n#if defined (STM32F722xx) || defined (STM32F723xx) || defined (STM32F732xx) || defined (STM32F733xx) || defined (STM32F730xx)\n  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * PLLI2SN */\n  /* I2SQCLK = PLLI2S_VCO / PLLI2SQ */\n  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */\n  /* __HAL_RCC_PLLI2S_CONFIG(PLLI2SInit->PLLI2SN, PLLI2SInit->PLLI2SQ, PLLI2SInit->PLLI2SR); */\n#else\n  /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * PLLI2SN */\n  /* I2SPCLK = PLLI2S_VCO / PLLI2SP */\n  /* I2SQCLK = PLLI2S_VCO / PLLI2SQ */\n  /* I2SRCLK = PLLI2S_VCO / PLLI2SR */\n  /* __HAL_RCC_PLLI2S_CONFIG(PLLI2SInit->PLLI2SN, PLLI2SInit->PLLI2SP, PLLI2SInit->PLLI2SQ, PLLI2SInit->PLLI2SR); */\n#endif /* STM32F722xx || STM32F723xx || STM32F732xx || STM32F733xx || STM32F730xx */\n\n  /* Skip hardware enable operation */\n  /* __HAL_RCC_PLLI2S_ENABLE(); */\n\n  /* Skip waiting for PLLI2S to be ready */\n  /* [LOOP REMOVED] Waited for hardware PLLI2S ready flag */\n\n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### HAL_RCCEx_GetPeriphCLKConfig

```text
=== HAL_RCCEx_GetPeriphCLKConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c
- 行号：2680
- 函数内容：void HAL_RCCEx_GetPeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tempreg;

  /* Set all possible values for the extended clock type parameter------------*/
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S | RCC_PERIPHCLK_RTC;

  /* Get the PLLI2S Clock configuration --------------------------------------*/
  PeriphClkInit->PLLI2S.PLLI2SN = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SN) >> RCC_PLLI2SCFGR_PLLI2SN_Pos);
  PeriphClkInit->PLLI2S.PLLI2SR = (uint32_t)((RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SR) >> RCC_PLLI2SCFGR_PLLI2SR_Pos);
#if defined(STM32F411xE)
  PeriphClkInit->PLLI2S.PLLI2SM = (uint32_t)(RCC->PLLI2SCFGR & RCC_PLLI2SCFGR_PLLI2SM);
#endif /* STM32F411xE */
  /* Get the RTC Clock configuration -----------------------------------------*/
  tempreg = (RCC->CFGR & RCC_CFGR_RTCPRE);
  PeriphClkInit->RTCClockSelection = (uint32_t)((tempreg) | (RCC->BDCR & RCC_BDCR_RTCSEL));

#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /* Get the TIM Prescaler configuration -------------------------------------*/
  if ((RCC->DCKCFGR & RCC_DCKCFGR_TIMPRE) == RESET)
  {
    PeriphClkInit->TIMPresSelection = RCC_TIMPRES_DESACTIVATED;
  }
  else
  {
    PeriphClkInit->TIMPresSelection = RCC_TIMPRES_ACTIVATED;
  }
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads peripheral clock configuration from RCC hardware registers (PLLI2S, RTC, TIM prescaler) and populates a configuration structure
- 是否需要替换：是
- 分类/替换原因：Function performs MMIO register reads from RCC peripheral registers (PLLI2SCFGR, CFGR, BDCR, DCKCFGR) to retrieve current clock configuration. This is a hardware-dependent initialization/configuration reading function that fits the INIT category. The function reads hardware state but doesn't perform data I/O (not RECV), isn't an interrupt handler (not IRQ), has no polling loops (not LOOP), and is not CORE (no NVIC/OS operations). The replacement removes all hardware register accesses and returns safe default values while preserving structure initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Configures the RCC_OscInitStruct according to the internal
* RCC configuration registers.
* @param  PeriphClkInit pointer to an RCC_PeriphCLKInitTypeDef structure that
* will be configured.
* @retval None
*/
void HAL_RCCEx_GetPeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  /* Set all possible values for the extended clock type parameter------------*/
  PeriphClkInit->PeriphClockSelection = RCC_PERIPHCLK_I2S | RCC_PERIPHCLK_RTC;

  /* Get the PLLI2S Clock configuration --------------------------------------*/
  /* [INIT REMOVED] Hardware register access removed for simulation */
  PeriphClkInit->PLLI2S.PLLI2SN = 0;
  PeriphClkInit->PLLI2S.PLLI2SR = 0;
#if defined(STM32F411xE)
  PeriphClkInit->PLLI2S.PLLI2SM = 0;
#endif /* STM32F411xE */
  
  /* Get the RTC Clock configuration -----------------------------------------*/
  /* [INIT REMOVED] Hardware register access removed for simulation */
  PeriphClkInit->RTCClockSelection = 0;

#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /* Get the TIM Prescaler configuration -------------------------------------*/
  /* [INIT REMOVED] Hardware register access removed for simulation */
  PeriphClkInit->TIMPresSelection = RCC_TIMPRES_DESACTIVATED;
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
}
```

=== 信息结束 ===
```

### HAL_RCCEx_PeriphCLKConfig

```text
=== HAL_RCCEx_PeriphCLKConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c
- 行号：2551
- 函数内容：HAL_StatusTypeDef HAL_RCCEx_PeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tickstart = 0U;
  uint32_t tmpreg1 = 0U;

  /* Check the parameters */
  assert_param(IS_RCC_PERIPHCLOCK(PeriphClkInit->PeriphClockSelection));

  /*---------------------------- I2S configuration ---------------------------*/
  if ((((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2S) == RCC_PERIPHCLK_I2S) ||
      (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_PLLI2S) == RCC_PERIPHCLK_PLLI2S))
  {
    /* check for Parameters */
    assert_param(IS_RCC_PLLI2SR_VALUE(PeriphClkInit->PLLI2S.PLLI2SR));
    assert_param(IS_RCC_PLLI2SN_VALUE(PeriphClkInit->PLLI2S.PLLI2SN));
#if defined(STM32F411xE)
    assert_param(IS_RCC_PLLI2SM_VALUE(PeriphClkInit->PLLI2S.PLLI2SM));
#endif /* STM32F411xE */
    /* Disable the PLLI2S */
    __HAL_RCC_PLLI2S_DISABLE();
    /* Get tick */
    tickstart = HAL_GetTick();
    /* Wait till PLLI2S is disabled */
    while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLI2SRDY)  != RESET)
    {
      if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
      {
        /* return in case of Timeout detected */
        return HAL_TIMEOUT;
      }
    }

#if defined(STM32F411xE)
    /* Configure the PLLI2S division factors */
    /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * (PLLI2SN/PLLI2SM) */
    /* I2SCLK = f(PLLI2S clock output) = f(VCO clock) / PLLI2SR */
    __HAL_RCC_PLLI2S_I2SCLK_CONFIG(PeriphClkInit->PLLI2S.PLLI2SM, PeriphClkInit->PLLI2S.PLLI2SN,
                                   PeriphClkInit->PLLI2S.PLLI2SR);
#else
    /* Configure the PLLI2S division factors */
    /* PLLI2S_VCO = f(VCO clock) = f(PLLI2S clock input) * (PLLI2SN/PLLM) */
    /* I2SCLK = f(PLLI2S clock output) = f(VCO clock) / PLLI2SR */
    __HAL_RCC_PLLI2S_CONFIG(PeriphClkInit->PLLI2S.PLLI2SN, PeriphClkInit->PLLI2S.PLLI2SR);
#endif /* STM32F411xE */

    /* Enable the PLLI2S */
    __HAL_RCC_PLLI2S_ENABLE();
    /* Get tick */
    tickstart = HAL_GetTick();
    /* Wait till PLLI2S is ready */
    while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLI2SRDY)  == RESET)
    {
      if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
      {
        /* return in case of Timeout detected */
        return HAL_TIMEOUT;
      }
    }
  }

  /*---------------------------- RTC configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));

    /* Enable Power Clock*/
    __HAL_RCC_PWR_CLK_ENABLE();

    /* Enable write access to Backup domain */
    PWR->CR |= PWR_CR_DBP;

    /* Get tick */
    tickstart = HAL_GetTick();

    while ((PWR->CR & PWR_CR_DBP) == RESET)
    {
      if ((HAL_GetTick() - tickstart) > RCC_DBP_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      }
    }
    /* Reset the Backup domain only if the RTC Clock source selection is modified from reset value */
    tmpreg1 = (RCC->BDCR & RCC_BDCR_RTCSEL);
    if ((tmpreg1 != 0x00000000U) && ((tmpreg1) != (PeriphClkInit->RTCClockSelection & RCC_BDCR_RTCSEL)))
    {
      /* Store the content of BDCR register before the reset of Backup Domain */
      tmpreg1 = (RCC->BDCR & ~(RCC_BDCR_RTCSEL));
      /* RTC Clock selection can be changed only if the Backup Domain is reset */
      __HAL_RCC_BACKUPRESET_FORCE();
      __HAL_RCC_BACKUPRESET_RELEASE();
      /* Restore the Content of BDCR register */
      RCC->BDCR = tmpreg1;

      /* Wait for LSE reactivation if LSE was enable prior to Backup Domain reset */
      if (HAL_IS_BIT_SET(RCC->BDCR, RCC_BDCR_LSEON))
      {
        /* Get tick */
        tickstart = HAL_GetTick();

        /* Wait till LSE is ready */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_LSERDY) == RESET)
        {
          if ((HAL_GetTick() - tickstart) > RCC_LSE_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
    }
    __HAL_RCC_RTC_CONFIG(PeriphClkInit->RTCClockSelection);
  }
#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /*---------------------------- TIM configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    __HAL_RCC_TIMCLKPRESCALER(PeriphClkInit->TIMPresSelection);
  }
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes extended peripheral clocks (I2S, SAI, LTDC, RTC, TIM, UARTs, USARTs, etc.) according to specified configuration parameters
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a clock configuration initialization function. GetMMIOFunctionInfo identified extensive MMIO register accesses (RCC->BDCR, RCC->PLLI2SCFGR, RCC->PLLSAICFGR, PWR->CR1) and hardware polling loops. The function configures multiple peripheral clock sources with hardware-dependent operations, timeout handling, and conditional compilation. It fits the INIT classification as it initializes hardware configurations, though it also contains LOOP characteristics for hardware polling. According to priority order, INIT takes precedence over LOOP.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the RCC extended peripherals clocks according to the specified
*         parameters in the RCC_PeriphCLKInitTypeDef.
* @param  PeriphClkInit pointer to an RCC_PeriphCLKInitTypeDef structure that
*         contains the configuration information for the Extended Peripherals
*         clocks(I2S, SAI, LTDC, RTC, TIM, UARTs, USARTs, LTPIM, SDMMC...).
*
* @note   Care must be taken when HAL_RCCEx_PeriphCLKConfig() is used to select
*         the RTC clock source; in this case the Backup domain will be reset in
*         order to modify the RTC Clock source, as consequence RTC registers (including
*         the backup registers) are set to their reset values.
*
* @retval HAL status
*/
HAL_StatusTypeDef HAL_RCCEx_PeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tickstart = 0;
  uint32_t tmpreg0 = 0;
  uint32_t tmpreg1 = 0;
  uint32_t plli2sused = 0;
  uint32_t pllsaiused = 0;

  /* Check the parameters */
  assert_param(IS_RCC_PERIPHCLOCK(PeriphClkInit->PeriphClockSelection));

  /*----------------------------------- I2S configuration ----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2S) == (RCC_PERIPHCLK_I2S))
  {
    /* Check the parameters */
    assert_param(IS_RCC_I2SCLKSOURCE(PeriphClkInit->I2sClockSelection));

    /* Enable the PLLI2S when it's used as clock source for I2S */
    if(PeriphClkInit->I2sClockSelection == RCC_I2SCLKSOURCE_PLLI2S)
    {
      plli2sused = 1;
    }
  }

  /*------------------------------------ SAI1 configuration --------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_SAI1) == (RCC_PERIPHCLK_SAI1))
  {
    /* Check the parameters */
    assert_param(IS_RCC_SAI1CLKSOURCE(PeriphClkInit->Sai1ClockSelection));

    /* Enable the PLLI2S when it's used as clock source for SAI */
    if(PeriphClkInit->Sai1ClockSelection == RCC_SAI1CLKSOURCE_PLLI2S)
    {
      plli2sused = 1;
    }
    /* Enable the PLLSAI when it's used as clock source for SAI */
    if(PeriphClkInit->Sai1ClockSelection == RCC_SAI1CLKSOURCE_PLLSAI)
    {
      pllsaiused = 1;
    }
  }

  /*------------------------------------ SAI2 configuration --------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_SAI2) == (RCC_PERIPHCLK_SAI2))
  {
    /* Check the parameters */
    assert_param(IS_RCC_SAI2CLKSOURCE(PeriphClkInit->Sai2ClockSelection));

    /* Enable the PLLI2S when it's used as clock source for SAI */
    if(PeriphClkInit->Sai2ClockSelection == RCC_SAI2CLKSOURCE_PLLI2S)
    {
      plli2sused = 1;
    }
    /* Enable the PLLSAI when it's used as clock source for SAI */
    if(PeriphClkInit->Sai2ClockSelection == RCC_SAI2CLKSOURCE_PLLSAI)
    {
      pllsaiused = 1;
    }
  }

  /*-------------------------------------- SPDIF-RX Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_SPDIFRX) == RCC_PERIPHCLK_SPDIFRX)
  {
      plli2sused = 1;
  }

  /*------------------------------------ RTC configuration --------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));

    /* Skip hardware-specific RTC configuration */
    /* [HARDWARE REMOVED] RTC clock source configuration */
  }

  /*------------------------------------ TIM configuration --------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    /* Check the parameters */
    assert_param(IS_RCC_TIMPRES(PeriphClkInit->TIMPresSelection));
  }

  /*-------------------------------------- I2C1 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2C1) == RCC_PERIPHCLK_I2C1)
  {
    /* Check the parameters */
    assert_param(IS_RCC_I2C1CLKSOURCE(PeriphClkInit->I2c1ClockSelection));
  }

  /*-------------------------------------- I2C2 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2C2) == RCC_PERIPHCLK_I2C2)
  {
    /* Check the parameters */
    assert_param(IS_RCC_I2C2CLKSOURCE(PeriphClkInit->I2c2ClockSelection));
  }

  /*-------------------------------------- I2C3 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2C3) == RCC_PERIPHCLK_I2C3)
  {
    /* Check the parameters */
    assert_param(IS_RCC_I2C3CLKSOURCE(PeriphClkInit->I2c3ClockSelection));
  }

  /*-------------------------------------- I2C4 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2C4) == RCC_PERIPHCLK_I2C4)
  {
    /* Check the parameters */
    assert_param(IS_RCC_I2C4CLKSOURCE(PeriphClkInit->I2c4ClockSelection));
  }

  /*-------------------------------------- USART1 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_USART1) == RCC_PERIPHCLK_USART1)
  {
    /* Check the parameters */
    assert_param(IS_RCC_USART1CLKSOURCE(PeriphClkInit->Usart1ClockSelection));
  }

  /*-------------------------------------- USART2 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_USART2) == RCC_PERIPHCLK_USART2)
  {
    /* Check the parameters */
    assert_param(IS_RCC_USART2CLKSOURCE(PeriphClkInit->Usart2ClockSelection));
  }

  /*-------------------------------------- USART3 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_USART3) == RCC_PERIPHCLK_USART3)
  {
    /* Check the parameters */
    assert_param(IS_RCC_USART3CLKSOURCE(PeriphClkInit->Usart3ClockSelection));
  }

  /*-------------------------------------- UART4 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_UART4) == RCC_PERIPHCLK_UART4)
  {
    /* Check the parameters */
    assert_param(IS_RCC_UART4CLKSOURCE(PeriphClkInit->Uart4ClockSelection));
  }

  /*-------------------------------------- UART5 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_UART5) == RCC_PERIPHCLK_UART5)
  {
    /* Check the parameters */
    assert_param(IS_RCC_UART5CLKSOURCE(PeriphClkInit->Uart5ClockSelection));
  }

  /*-------------------------------------- USART6 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_USART6) == RCC_PERIPHCLK_USART6)
  {
    /* Check the parameters */
    assert_param(IS_RCC_USART6CLKSOURCE(PeriphClkInit->Usart6ClockSelection));
  }

  /*-------------------------------------- UART7 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_UART7) == RCC_PERIPHCLK_UART7)
  {
    /* Check the parameters */
    assert_param(IS_RCC_UART7CLKSOURCE(PeriphClkInit->Uart7ClockSelection));
  }

  /*-------------------------------------- UART8 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_UART8) == RCC_PERIPHCLK_UART8)
  {
    /* Check the parameters */
    assert_param(IS_RCC_UART8CLKSOURCE(PeriphClkInit->Uart8ClockSelection));
  }

  /*--------------------------------------- CEC Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_CEC) == RCC_PERIPHCLK_CEC)
  {
    /* Check the parameters */
    assert_param(IS_RCC_CECCLKSOURCE(PeriphClkInit->CecClockSelection));
  }

  /*-------------------------------------- CK48 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_CLK48) == RCC_PERIPHCLK_CLK48)
  {
    /* Check the parameters */
    assert_param(IS_RCC_CLK48SOURCE(PeriphClkInit->Clk48ClockSelection));

    /* Enable the PLLSAI when it's used as clock source for CK48 */
    if(PeriphClkInit->Clk48ClockSelection == RCC_CLK48SOURCE_PLLSAIP)
    {
      pllsaiused = 1;
    }
  }

  /*-------------------------------------- LTDC Configuration -----------------------------------*/
#if defined(STM32F746xx) || defined(STM32F756xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx) || defined (STM32F750xx)
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_LTDC) == RCC_PERIPHCLK_LTDC)
  {
    pllsaiused = 1;
  }
#endif /* STM32F746xx || STM32F756xx || STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx || STM32F750xx */

  /*-------------------------------------- LPTIM1 Configuration -----------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_LPTIM1) == RCC_PERIPHCLK_LPTIM1)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LPTIM1CLK(PeriphClkInit->Lptim1ClockSelection));
   }

  /*------------------------------------- SDMMC1 Configuration ------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_SDMMC1) == RCC_PERIPHCLK_SDMMC1)
  {
    /* Check the parameters */
    assert_param(IS_RCC_SDMMC1CLKSOURCE(PeriphClkInit->Sdmmc1ClockSelection));
  }

#if defined (STM32F765xx) || defined (STM32F767xx) || defined (STM32F769xx) || defined (STM32F777xx) || defined (STM32F779xx)
  /*------------------------------------- SDMMC2 Configuration ------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_SDMMC2) == RCC_PERIPHCLK_SDMMC2)
  {
    /* Check the parameters */
    assert_param(IS_RCC_SDMMC2CLKSOURCE(PeriphClkInit->Sdmmc2ClockSelection));
  }

  /*------------------------------------- DFSDM1 Configuration -------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_DFSDM1) == RCC_PERIPHCLK_DFSDM1)
  {
    /* Check the parameters */
    assert_param(IS_RCC_DFSDM1CLKSOURCE(PeriphClkInit->Dfsdm1ClockSelection));
  }

  /*------------------------------------- DFSDM AUDIO Configuration -------------------------------------*/
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_DFSDM1_AUDIO) == RCC_PERIPHCLK_DFSDM1_AUDIO)
  {
    /* Check the parameters */
    assert_param(IS_RCC_DFSDM1AUDIOCLKSOURCE(PeriphClkInit->Dfsdm1AudioClockSelection));
  }
#endif /* STM32F767xx || STM32F769xx || STM32F777xx || STM32F779xx */

  /*-------------------------------------- PLLI2S Configuration ---------------------------------*/
  /* PLLI2S is configured when a peripheral will use it as source clock : SAI1, SAI2, I2S or SPDIF-RX */
  if((plli2sused == 1) || ((PeriphClkInit->PeriphClockSelection & RCC_PERIPHCLK_PLLI2S) == RCC_PERIPHCLK_PLLI2S))
  {
    /* Skip hardware-specific PLLI2S configuration */
    /* [HARDWARE REMOVED] PLLI2S disable/enable and configuration */
  }

  /*-------------------------------------- PLLSAI Configuration ---------------------------------*/
  /* PLLSAI is configured when a peripheral will use it as source clock : SAI1, SAI2, LTDC or CK48 */
  if(pllsaiused == 1)
  {
    /* Skip hardware-specific PLLSAI configuration */
    /* [HARDWARE REMOVED] PLLSAI disable/enable and configuration */
  }
  return HAL_OK;
}
```

【替换更新】
- 更新代码：/**
* @brief  Initializes the RCC extended peripherals clocks according to the specified
*         parameters in the RCC_PeriphCLKInitTypeDef.
* @param  PeriphClkInit pointer to an RCC_PeriphCLKInitTypeDef structure that
*         contains the configuration information for the Extended Peripherals
*         clocks(I2S, RTC, TIM).
*
* @note   Care must be taken when HAL_RCCEx_PeriphCLKConfig() is used to select
*         the RTC clock source; in this case the Backup domain will be reset in
*         order to modify the RTC Clock source, as consequence RTC registers (including
*         the backup registers) are set to their reset values.
*
* @retval HAL status
*/
HAL_StatusTypeDef HAL_RCCEx_PeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tickstart = 0U;
  uint32_t tmpreg1 = 0U;

  /* Check the parameters */
  assert_param(IS_RCC_PERIPHCLOCK(PeriphClkInit->PeriphClockSelection));

  /*---------------------------- I2S configuration ---------------------------*/
  if ((((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2S) == RCC_PERIPHCLK_I2S) ||
      (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_PLLI2S) == RCC_PERIPHCLK_PLLI2S))
  {
    /* check for Parameters */
    assert_param(IS_RCC_PLLI2SR_VALUE(PeriphClkInit->PLLI2S.PLLI2SR));
    assert_param(IS_RCC_PLLI2SN_VALUE(PeriphClkInit->PLLI2S.PLLI2SN));
#if defined(STM32F411xE)
    assert_param(IS_RCC_PLLI2SM_VALUE(PeriphClkInit->PLLI2S.PLLI2SM));
#endif /* STM32F411xE */
    
    /* Skip hardware-specific PLLI2S configuration */
    /* [HARDWARE REMOVED] PLLI2S disable/enable and configuration */
  }

  /*---------------------------- RTC configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));

    /* Skip hardware-specific RTC configuration */
    /* [HARDWARE REMOVED] RTC clock source configuration */
  }

#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /*---------------------------- TIM configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    /* Skip hardware-specific TIM prescaler configuration */
    /* [HARDWARE REMOVED] TIM clock prescaler configuration */
  }
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
  
  return HAL_OK;
}
- 更新原因：Fix HAL_RCCEx_PeriphCLKConfig for STM32F4: 1. Remove references to non-existent members (I2sClockSelection, Sai1ClockSelection, etc.), 2. Simplify to match STM32F4's actual capabilities (only I2S, RTC, TIM), 3. Keep conditional compilation for STM32F401/411, 4. Remove hardware-specific operations while keeping parameter validation

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Initializes the RCC extended peripherals clocks according to the specified
*         parameters in the RCC_PeriphCLKInitTypeDef.
* @param  PeriphClkInit pointer to an RCC_PeriphCLKInitTypeDef structure that
*         contains the configuration information for the Extended Peripherals
*         clocks(I2S, RTC, TIM).
*
* @note   Care must be taken when HAL_RCCEx_PeriphCLKConfig() is used to select
*         the RTC clock source; in this case the Backup domain will be reset in
*         order to modify the RTC Clock source, as consequence RTC registers (including
*         the backup registers) are set to their reset values.
*
* @retval HAL status
*/
HAL_StatusTypeDef HAL_RCCEx_PeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
  uint32_t tickstart = 0U;
  uint32_t tmpreg1 = 0U;

  /* Check the parameters */
  assert_param(IS_RCC_PERIPHCLOCK(PeriphClkInit->PeriphClockSelection));

  /*---------------------------- I2S configuration ---------------------------*/
  if ((((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2S) == RCC_PERIPHCLK_I2S) ||
      (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_PLLI2S) == RCC_PERIPHCLK_PLLI2S))
  {
    /* check for Parameters */
    assert_param(IS_RCC_PLLI2SR_VALUE(PeriphClkInit->PLLI2S.PLLI2SR));
    assert_param(IS_RCC_PLLI2SN_VALUE(PeriphClkInit->PLLI2S.PLLI2SN));
#if defined(STM32F411xE)
    assert_param(IS_RCC_PLLI2SM_VALUE(PeriphClkInit->PLLI2S.PLLI2SM));
#endif /* STM32F411xE */
    
    /* Skip hardware-specific PLLI2S configuration */
    /* [HARDWARE REMOVED] PLLI2S disable/enable and configuration */
  }

  /*---------------------------- RTC configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));

    /* Skip hardware-specific RTC configuration */
    /* [HARDWARE REMOVED] RTC clock source configuration */
  }

#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /*---------------------------- TIM configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    /* Skip hardware-specific TIM prescaler configuration */
    /* [HARDWARE REMOVED] TIM clock prescaler configuration */
  }
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
  
  return HAL_OK;
}
    原因：Fix HAL_RCCEx_PeriphCLKConfig for STM32F4: 1. Remove references to non-existent members (I2sClockSelection, Sai1ClockSelection, etc.), 2. Simplify to match STM32F4's actual capabilities (only I2S, RTC, TIM), 3. Keep conditional compilation for STM32F401/411, 4. Remove hardware-specific operations while keeping parameter validation
    时间：

=== 信息结束 ===
```

### HAL_RCC_ClockConfig

```text
=== HAL_RCC_ClockConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：591
- 函数内容：HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
{
  uint32_t tickstart;

  /* Check Null pointer */
  if (RCC_ClkInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_CLOCKTYPE(RCC_ClkInitStruct->ClockType));
  assert_param(IS_FLASH_LATENCY(FLatency));

  /* To correctly read data from FLASH memory, the number of wait states (LATENCY)
    must be correctly programmed according to the frequency of the CPU clock
    (HCLK) and the supply voltage of the device. */

  /* Increasing the number of wait states because of higher CPU frequency */
  if (FLatency > __HAL_FLASH_GET_LATENCY())
  {
    /* Program the new number of wait states to the LATENCY bits in the FLASH_ACR register */
    __HAL_FLASH_SET_LATENCY(FLatency);

    /* Check that the new number of wait states is taken into account to access the Flash
    memory by reading the FLASH_ACR register */
    if (__HAL_FLASH_GET_LATENCY() != FLatency)
    {
      return HAL_ERROR;
    }
  }

  /*-------------------------- HCLK Configuration --------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_HCLK) == RCC_CLOCKTYPE_HCLK)
  {
    /* Set the highest APBx dividers in order to ensure that we do not go through
       a non-spec phase whatever we decrease or increase HCLK. */
    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
    {
      MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_HCLK_DIV16);
    }

    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
    {
      MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, (RCC_HCLK_DIV16 << 3));
    }

    assert_param(IS_RCC_HCLK(RCC_ClkInitStruct->AHBCLKDivider));
    MODIFY_REG(RCC->CFGR, RCC_CFGR_HPRE, RCC_ClkInitStruct->AHBCLKDivider);
  }

  /*------------------------- SYSCLK Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_SYSCLK) == RCC_CLOCKTYPE_SYSCLK)
  {
    assert_param(IS_RCC_SYSCLKSOURCE(RCC_ClkInitStruct->SYSCLKSource));

    /* HSE is selected as System Clock Source */
    if (RCC_ClkInitStruct->SYSCLKSource == RCC_SYSCLKSOURCE_HSE)
    {
      /* Check the HSE ready flag */
      if (__HAL_RCC_GET_FLAG(RCC_FLAG_HSERDY) == RESET)
      {
        return HAL_ERROR;
      }
    }
    /* PLL is selected as System Clock Source */
    else if ((RCC_ClkInitStruct->SYSCLKSource == RCC_SYSCLKSOURCE_PLLCLK)   ||
             (RCC_ClkInitStruct->SYSCLKSource == RCC_SYSCLKSOURCE_PLLRCLK))
    {
      /* Check the PLL ready flag */
      if (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) == RESET)
      {
        return HAL_ERROR;
      }
    }
    /* HSI is selected as System Clock Source */
    else
    {
      /* Check the HSI ready flag */
      if (__HAL_RCC_GET_FLAG(RCC_FLAG_HSIRDY) == RESET)
      {
        return HAL_ERROR;
      }
    }

    __HAL_RCC_SYSCLK_CONFIG(RCC_ClkInitStruct->SYSCLKSource);

    /* Get Start Tick */
    tickstart = HAL_GetTick();

    while (__HAL_RCC_GET_SYSCLK_SOURCE() != (RCC_ClkInitStruct->SYSCLKSource << RCC_CFGR_SWS_Pos))
    {
      if ((HAL_GetTick() - tickstart) > CLOCKSWITCH_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      }
    }
  }

  /* Decreasing the number of wait states because of lower CPU frequency */
  if (FLatency < __HAL_FLASH_GET_LATENCY())
  {
    /* Program the new number of wait states to the LATENCY bits in the FLASH_ACR register */
    __HAL_FLASH_SET_LATENCY(FLatency);

    /* Check that the new number of wait states is taken into account to access the Flash
    memory by reading the FLASH_ACR register */
    if (__HAL_FLASH_GET_LATENCY() != FLatency)
    {
      return HAL_ERROR;
    }
  }

  /*-------------------------- PCLK1 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB1CLKDivider));
    MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_ClkInitStruct->APB1CLKDivider);
  }

  /*-------------------------- PCLK2 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB2CLKDivider));
    MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, ((RCC_ClkInitStruct->APB2CLKDivider) << 3U));
  }

  /* Update the SystemCoreClock global variable */
  SystemCoreClock = HAL_RCC_GetSysClockFreq() >> AHBPrescTable[(RCC->CFGR & RCC_CFGR_HPRE) >> RCC_CFGR_HPRE_Pos];

  /* Configure the source of time base considering new system clocks settings */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes CPU, AHB, and APB bus clocks according to specified parameters, configuring system clock sources, dividers, and flash latency settings.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a clock configuration function with extensive MMIO operations. GetMMIOFunctionInfo identified multiple register accesses to RCC->CFGR, flash latency operations, and hardware status checks. The function contains: 1) Direct hardware register writes for clock configuration, 2) Flash latency programming, 3) Clock source switching with timeout loops, 4) Hardware status flag polling. However, it also has critical non-hardware logic that must be preserved: SystemCoreClock global variable update and HAL_InitTick() call for system tick timer reconfiguration. This matches the INIT classification criteria as it initializes peripheral/configurations (system clocks) and contains MMIO operations that need removal while preserving structure validation, timeout handling, and system state updates.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the CPU, AHB and APB buses clocks according to the specified
*         parameters in the RCC_ClkInitStruct.
* @param  RCC_ClkInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC peripheral.
* @param  FLatency FLASH Latency, this parameter depend on device selected
*
* @note   The SystemCoreClock CMSIS variable is used to store System Clock Frequency
*         and updated by HAL_RCC_GetHCLKFreq() function called within this function
*
* @note   The HSI is used (enabled by hardware) as system clock source after
*         startup from Reset, wake-up from STOP and STANDBY mode, or in case
*         of failure of the HSE used directly or indirectly as system clock
*         (if the Clock Security System CSS is enabled).
*
* @note   A switch from one clock source to another occurs only if the target
*         clock source is ready (clock stable after startup delay or PLL locked).
*         If a clock source which is not yet ready is selected, the switch will
*         occur when the clock source will be ready.
*         You can use HAL_RCC_GetClockConfig() function to know which clock is
*         currently used as system clock source.
* @note   Depending on the device voltage range, the software has to set correctly
*         HPRE[3:0] bits to ensure that HCLK not exceed the maximum allowed frequency
*         (for more details refer to section above "Initialization/de-initialization functions")
* @retval None
*/
HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
{
  uint32_t tickstart = 0;

  /* Check Null pointer */
  if (RCC_ClkInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_CLOCKTYPE(RCC_ClkInitStruct->ClockType));
  assert_param(IS_FLASH_LATENCY(FLatency));

  /* To correctly read data from FLASH memory, the number of wait states (LATENCY)
     must be correctly programmed according to the frequency of the CPU clock
     (HCLK) and the supply voltage of the device. */

  /* Increasing the CPU frequency */
  if (FLatency > __HAL_FLASH_GET_LATENCY())
  {
    /* Program the new number of wait states to the LATENCY bits in the FLASH_ACR register */
    /* [INIT REMOVED] Hardware flash latency configuration removed */

    /* Check that the new number of wait states is taken into account to access the Flash
    memory by reading the FLASH_ACR register */
    /* [INIT REMOVED] Hardware flash latency verification removed */
  }

  /*-------------------------- HCLK Configuration --------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_HCLK) == RCC_CLOCKTYPE_HCLK)
  {
    /* Set the highest APBx dividers in order to ensure that we do not go through
       a non-spec phase whatever we decrease or increase HCLK. */
    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_HCLK_DIV16); */
    }

    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, (RCC_HCLK_DIV16 << 3)); */
    }

    /* Set the new HCLK clock divider */
    assert_param(IS_RCC_HCLK(RCC_ClkInitStruct->AHBCLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_HPRE, RCC_ClkInitStruct->AHBCLKDivider); */
  }

  /*------------------------- SYSCLK Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_SYSCLK) == RCC_CLOCKTYPE_SYSCLK)
  {
    assert_param(IS_RCC_SYSCLKSOURCE(RCC_ClkInitStruct->SYSCLKSource));

    /* HSE is selected as System Clock Source */
    if (RCC_ClkInitStruct->SYSCLKSource == RCC_SYSCLKSOURCE_HSE)
    {
      /* Check the HSE ready flag */
      /* [INIT REMOVED] Hardware HSE ready flag check removed - assume ready */
    }
    /* PLL is selected as System Clock Source */
    else if (RCC_ClkInitStruct->SYSCLKSource == RCC_SYSCLKSOURCE_PLLCLK)
    {
      /* Check the PLL ready flag */
      /* [INIT REMOVED] Hardware PLL ready flag check removed - assume ready */
    }
    /* HSI is selected as System Clock Source */
    else
    {
      /* Check the HSI ready flag */
      /* [INIT REMOVED] Hardware HSI ready flag check removed - assume ready */
    }

    /* [INIT REMOVED] __HAL_RCC_SYSCLK_CONFIG(RCC_ClkInitStruct->SYSCLKSource); */

    /* Get Start Tick*/
    tickstart = HAL_GetTick();

    /* [LOOP REMOVED] Wait for hardware clock switch completion - assume successful */
    /* while (__HAL_RCC_GET_SYSCLK_SOURCE() != (RCC_ClkInitStruct->SYSCLKSource << RCC_CFGR_SWS_Pos))
    {
      if ((HAL_GetTick() - tickstart) > CLOCKSWITCH_TIMEOUT_VALUE)
      {
        return HAL_TIMEOUT;
      }
    } */
  }

  /* Decreasing the number of wait states because of lower CPU frequency */
  if (FLatency < __HAL_FLASH_GET_LATENCY())
  {
    /* Program the new number of wait states to the LATENCY bits in the FLASH_ACR register */
    /* [INIT REMOVED] Hardware flash latency configuration removed */

    /* Check that the new number of wait states is taken into account to access the Flash
    memory by reading the FLASH_ACR register */
    /* [INIT REMOVED] Hardware flash latency verification removed */
  }

  /*-------------------------- PCLK1 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB1CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_ClkInitStruct->APB1CLKDivider); */
  }

  /*-------------------------- PCLK2 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB2CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, ((RCC_ClkInitStruct->APB2CLKDivider) << 3)); */
  }

  /* Update the SystemCoreClock global variable */
  /* Preserve the SystemCoreClock update logic but use a simulated value */
  /* Since we can't access hardware registers, use a reasonable default */
  SystemCoreClock = HAL_RCC_GetSysClockFreq() >> 1; /* Simplified calculation */

  /* Configure the source of time base considering new system clocks settings*/
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
```

【替换更新】
- 更新代码：/**
* @brief  Initializes the CPU, AHB and APB buses clocks according to the specified
*         parameters in the RCC_ClkInitStruct.
* @param  RCC_ClkInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC peripheral.
* @param  FLatency FLASH Latency, this parameter depend on device selected
*
* @note   The SystemCoreClock CMSIS variable is used to store System Clock Frequency
*         and updated by HAL_RCC_GetHCLKFreq() function called within this function
*
* @note   The HSI is used (enabled by hardware) as system clock source after
*         startup from Reset, wake-up from STOP and STANDBY mode, or in case
*         of failure of the HSE used directly or indirectly as system clock
*         (if the Clock Security System CSS is enabled).
*
* @note   A switch from one clock source to another occurs only if the target
*         clock source is ready (clock stable after startup delay or PLL locked).
*         If a clock source which is not yet ready is selected, the switch will
*         occur when the clock source will be ready.
*         You can use HAL_RCC_GetClockConfig() function to know which clock is
*         currently used as system clock source.
* @note   Depending on the device voltage range, the software has to set correctly
*         HPRE[3:0] bits to ensure that HCLK not exceed the maximum allowed frequency
*         (for more details refer to section above "Initialization/de-initialization functions")
* @retval None
*/
HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
{
  /* Check Null pointer */
  if (RCC_ClkInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_CLOCKTYPE(RCC_ClkInitStruct->ClockType));
  assert_param(IS_FLASH_LATENCY(FLatency));

  /* To correctly read data from FLASH memory, the number of wait states (LATENCY)
     must be correctly programmed according to the frequency of the CPU clock
     (HCLK) and the supply voltage of the device. */

  /* [INIT REMOVED] Skip flash latency configuration entirely for emulation */
  /* Original code has hardware operations for flash latency that we cannot emulate */

  /*-------------------------- HCLK Configuration --------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_HCLK) == RCC_CLOCKTYPE_HCLK)
  {
    /* Set the highest APBx dividers in order to ensure that we do not go through
       a non-spec phase whatever we decrease or increase HCLK. */
    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_HCLK_DIV16); */
    }

    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, (RCC_HCLK_DIV16 << 3)); */
    }

    /* Set the new HCLK clock divider */
    assert_param(IS_RCC_HCLK(RCC_ClkInitStruct->AHBCLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_HPRE, RCC_ClkInitStruct->AHBCLKDivider); */
  }

  /*------------------------- SYSCLK Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_SYSCLK) == RCC_CLOCKTYPE_SYSCLK)
  {
    assert_param(IS_RCC_SYSCLKSOURCE(RCC_ClkInitStruct->SYSCLKSource));

    /* Skip hardware ready flag checks for emulation */
    /* [INIT REMOVED] Hardware clock source ready flag checks removed */

    /* [INIT REMOVED] __HAL_RCC_SYSCLK_CONFIG(RCC_ClkInitStruct->SYSCLKSource); */

    /* [LOOP REMOVED] Skip hardware clock switch wait loop */
  }

  /* [INIT REMOVED] Skip flash latency configuration for decreasing frequency */

  /*-------------------------- PCLK1 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB1CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_ClkInitStruct->APB1CLKDivider); */
  }

  /*-------------------------- PCLK2 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB2CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, ((RCC_ClkInitStruct->APB2CLKDivider) << 3)); */
  }

  /* Update the SystemCoreClock global variable */
  /* Since we can't access hardware registers, use a reasonable default */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings*/
  /* Use the current tick priority */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
- 更新原因：Fix HAL_RCC_ClockConfig replacement to use uwTickPrio instead of hardcoded 0 for HAL_InitTick call. This ensures consistent SysTick priority configuration throughout the system initialization. The uwTickPrio variable is set by HAL_InitTick when it's called earlier in the initialization sequence, and using it here maintains the correct priority setting for SysTick interrupts.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Initializes the CPU, AHB and APB buses clocks according to the specified
*         parameters in the RCC_ClkInitStruct.
* @param  RCC_ClkInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC peripheral.
* @param  FLatency FLASH Latency, this parameter depend on device selected
*
* @note   The SystemCoreClock CMSIS variable is used to store System Clock Frequency
*         and updated by HAL_RCC_GetHCLKFreq() function called within this function
*
* @note   The HSI is used (enabled by hardware) as system clock source after
*         startup from Reset, wake-up from STOP and STANDBY mode, or in case
*         of failure of the HSE used directly or indirectly as system clock
*         (if the Clock Security System CSS is enabled).
*
* @note   A switch from one clock source to another occurs only if the target
*         clock source is ready (clock stable after startup delay or PLL locked).
*         If a clock source which is not yet ready is selected, the switch will
*         occur when the clock source will be ready.
*         You can use HAL_RCC_GetClockConfig() function to know which clock is
*         currently used as system clock source.
* @note   Depending on the device voltage range, the software has to set correctly
*         HPRE[3:0] bits to ensure that HCLK not exceed the maximum allowed frequency
*         (for more details refer to section above "Initialization/de-initialization functions")
* @retval None
*/
HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
{
  /* Check Null pointer */
  if (RCC_ClkInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_CLOCKTYPE(RCC_ClkInitStruct->ClockType));
  assert_param(IS_FLASH_LATENCY(FLatency));

  /* To correctly read data from FLASH memory, the number of wait states (LATENCY)
     must be correctly programmed according to the frequency of the CPU clock
     (HCLK) and the supply voltage of the device. */

  /* [INIT REMOVED] Skip flash latency configuration entirely for emulation */
  /* Original code has hardware operations for flash latency that we cannot emulate */

  /*-------------------------- HCLK Configuration --------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_HCLK) == RCC_CLOCKTYPE_HCLK)
  {
    /* Set the highest APBx dividers in order to ensure that we do not go through
       a non-spec phase whatever we decrease or increase HCLK. */
    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_HCLK_DIV16); */
    }

    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, (RCC_HCLK_DIV16 << 3)); */
    }

    /* Set the new HCLK clock divider */
    assert_param(IS_RCC_HCLK(RCC_ClkInitStruct->AHBCLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_HPRE, RCC_ClkInitStruct->AHBCLKDivider); */
  }

  /*------------------------- SYSCLK Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_SYSCLK) == RCC_CLOCKTYPE_SYSCLK)
  {
    assert_param(IS_RCC_SYSCLKSOURCE(RCC_ClkInitStruct->SYSCLKSource));

    /* Skip hardware ready flag checks for emulation */
    /* [INIT REMOVED] Hardware clock source ready flag checks removed */

    /* [INIT REMOVED] __HAL_RCC_SYSCLK_CONFIG(RCC_ClkInitStruct->SYSCLKSource); */

    /* [LOOP REMOVED] Skip hardware clock switch wait loop */
  }

  /* [INIT REMOVED] Skip flash latency configuration for decreasing frequency */

  /*-------------------------- PCLK1 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB1CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_ClkInitStruct->APB1CLKDivider); */
  }

  /*-------------------------- PCLK2 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB2CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, ((RCC_ClkInitStruct->APB2CLKDivider) << 3)); */
  }

  /* Update the SystemCoreClock global variable */
  /* Since we can't access hardware registers, use a reasonable default */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings*/
  /* Use default tick priority */
  HAL_InitTick(0);

  return HAL_OK;
}
    原因：Fix HAL_RCC_ClockConfig replacement to avoid calling hardware-dependent macros like __HAL_FLASH_GET_LATENCY(). Remove all conditional logic that depends on hardware register reads. Simplify the function to skip flash latency configuration entirely since we cannot emulate hardware flash operations. Keep parameter validation and essential system state updates (SystemCoreClock and HAL_InitTick).
    时间：

  版本 2:
    替换代码：/**
* @brief  Initializes the CPU, AHB and APB buses clocks according to the specified
*         parameters in the RCC_ClkInitStruct.
* @param  RCC_ClkInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC peripheral.
* @param  FLatency FLASH Latency, this parameter depend on device selected
*
* @note   The SystemCoreClock CMSIS variable is used to store System Clock Frequency
*         and updated by HAL_RCC_GetHCLKFreq() function called within this function
*
* @note   The HSI is used (enabled by hardware) as system clock source after
*         startup from Reset, wake-up from STOP and STANDBY mode, or in case
*         of failure of the HSE used directly or indirectly as system clock
*         (if the Clock Security System CSS is enabled).
*
* @note   A switch from one clock source to another occurs only if the target
*         clock source is ready (clock stable after startup delay or PLL locked).
*         If a clock source which is not yet ready is selected, the switch will
*         occur when the clock source will be ready.
*         You can use HAL_RCC_GetClockConfig() function to know which clock is
*         currently used as system clock source.
* @note   Depending on the device voltage range, the software has to set correctly
*         HPRE[3:0] bits to ensure that HCLK not exceed the maximum allowed frequency
*         (for more details refer to section above "Initialization/de-initialization functions")
* @retval None
*/
HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
{
  /* Check Null pointer */
  if (RCC_ClkInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_CLOCKTYPE(RCC_ClkInitStruct->ClockType));
  assert_param(IS_FLASH_LATENCY(FLatency));

  /* To correctly read data from FLASH memory, the number of wait states (LATENCY)
     must be correctly programmed according to the frequency of the CPU clock
     (HCLK) and the supply voltage of the device. */

  /* [INIT REMOVED] Skip flash latency configuration entirely for emulation */
  /* Original code has hardware operations for flash latency that we cannot emulate */

  /*-------------------------- HCLK Configuration --------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_HCLK) == RCC_CLOCKTYPE_HCLK)
  {
    /* Set the highest APBx dividers in order to ensure that we do not go through
       a non-spec phase whatever we decrease or increase HCLK. */
    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_HCLK_DIV16); */
    }

    if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
    {
      /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, (RCC_HCLK_DIV16 << 3)); */
    }

    /* Set the new HCLK clock divider */
    assert_param(IS_RCC_HCLK(RCC_ClkInitStruct->AHBCLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_HPRE, RCC_ClkInitStruct->AHBCLKDivider); */
  }

  /*------------------------- SYSCLK Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_SYSCLK) == RCC_CLOCKTYPE_SYSCLK)
  {
    assert_param(IS_RCC_SYSCLKSOURCE(RCC_ClkInitStruct->SYSCLKSource));

    /* Skip hardware ready flag checks for emulation */
    /* [INIT REMOVED] Hardware clock source ready flag checks removed */

    /* [INIT REMOVED] __HAL_RCC_SYSCLK_CONFIG(RCC_ClkInitStruct->SYSCLKSource); */

    /* [LOOP REMOVED] Skip hardware clock switch wait loop */
  }

  /* [INIT REMOVED] Skip flash latency configuration for decreasing frequency */

  /*-------------------------- PCLK1 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK1) == RCC_CLOCKTYPE_PCLK1)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB1CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE1, RCC_ClkInitStruct->APB1CLKDivider); */
  }

  /*-------------------------- PCLK2 Configuration ---------------------------*/
  if (((RCC_ClkInitStruct->ClockType) & RCC_CLOCKTYPE_PCLK2) == RCC_CLOCKTYPE_PCLK2)
  {
    assert_param(IS_RCC_PCLK(RCC_ClkInitStruct->APB2CLKDivider));
    /* [INIT REMOVED] MODIFY_REG(RCC->CFGR, RCC_CFGR_PPRE2, ((RCC_ClkInitStruct->APB2CLKDivider) << 3)); */
  }

  /* Update the SystemCoreClock global variable */
  /* Since we can't access hardware registers, use a reasonable default */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings*/
  /* Use the current tick priority */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
    原因：Fix HAL_RCC_ClockConfig replacement to use uwTickPrio instead of hardcoded 0 for HAL_InitTick call. This ensures consistent SysTick priority configuration throughout the system initialization. The uwTickPrio variable is set by HAL_InitTick when it's called earlier in the initialization sequence, and using it here maintains the correct priority setting for SysTick interrupts.
    时间：

=== 信息结束 ===
```

### HAL_RCC_GetPCLK1Freq

```text
=== HAL_RCC_GetPCLK1Freq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：954
- 函数内容：uint32_t HAL_RCC_GetPCLK1Freq(void)
{
  /* Get HCLK source and Compute PCLK1 frequency ---------------------------*/
  return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE1) >> RCC_CFGR_PPRE1_Pos]);
}


【初始分析（FunctionClassifier）】
- 函数类型：RETURNOK
- 函数用途/功能描述：Returns the PCLK1 (APB1 peripheral clock) frequency by reading the RCC configuration register and applying the appropriate prescaler.
- 是否需要替换：否
- 分类/替换原因：Function reads hardware register RCC->CFGR to determine APB1 prescaler setting and computes PCLK1 frequency based on HCLK frequency. This is a pure hardware read operation that returns a calculated value. It doesn't modify hardware state, perform data I/O, handle interrupts, initialize hardware, or contain peripheral-dependent loops. According to classification strategy, this fits RETURNOK - functions that only manipulate peripheral registers with no impact on upper-layer data structures and would return a success value or safe default.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：uint32_t HAL_RCC_GetPCLK1Freq(void)
{
  /* Get HCLK source and Compute PCLK1 frequency ---------------------------*/
  /* [INIT REMOVED] Hardware register read removed - return default value for emulation */
  /* Original: return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE1) >> RCC_CFGR_PPRE1_Pos]); */
  
  /* Return a reasonable default frequency for emulation (84MHz / 4 = 21MHz) */
  return 21000000;
}
- 更新原因：Create replacement for HAL_RCC_GetPCLK1Freq to remove hardware-dependent register read. The original function reads from RCC->CFGR register to determine clock prescaler. In emulation, we return a reasonable default value (21MHz) that matches typical STM32F4 configuration where HCLK is 84MHz and APB1 prescaler is 4.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：uint32_t HAL_RCC_GetPCLK1Freq(void)
{
  /* Get HCLK source and Compute PCLK1 frequency ---------------------------*/
  /* [INIT REMOVED] Hardware register read removed - return default value for emulation */
  /* Original: return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE1) >> RCC_CFGR_PPRE1_Pos]); */
  
  /* Return a reasonable default frequency for emulation (84MHz / 4 = 21MHz) */
  return 21000000;
}
    原因：Create replacement for HAL_RCC_GetPCLK1Freq to remove hardware-dependent register read. The original function reads from RCC->CFGR register to determine clock prescaler. In emulation, we return a reasonable default value (21MHz) that matches typical STM32F4 configuration where HCLK is 84MHz and APB1 prescaler is 4.
    时间：

=== 信息结束 ===
```

### HAL_RCC_GetPCLK2Freq

```text
=== HAL_RCC_GetPCLK2Freq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：966
- 函数内容：uint32_t HAL_RCC_GetPCLK2Freq(void)
{
  /* Get HCLK source and Compute PCLK2 frequency ---------------------------*/
  return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE2) >> RCC_CFGR_PPRE2_Pos]);
}


【初始分析（FunctionClassifier）】
- 函数类型：RETURNOK
- 函数用途/功能描述：Returns the PCLK2 (APB2 peripheral clock) frequency by reading RCC configuration registers and applying prescaler calculations.
- 是否需要替换：否
- 分类/替换原因：Function reads RCC->CFGR register (MMIO access) to determine clock prescaler configuration and returns computed frequency. It's a pure 'getter' function that returns hardware state information without performing data I/O, interrupt handling, initialization, or containing hardware-dependent loops. Called by peripheral drivers (e.g., UART_SetConfig) for clock configuration. Fits RETURNOK classification as it only manipulates/reads peripheral registers with no impact on upper-layer data structures.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：uint32_t HAL_RCC_GetPCLK2Freq(void)
{
  /* Get HCLK source and Compute PCLK2 frequency ---------------------------*/
  /* [INIT REMOVED] Hardware register read removed - return default value for emulation */
  /* Original: return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE2) >> RCC_CFGR_PPRE2_Pos]); */
  
  /* Return a reasonable default frequency for emulation (84MHz / 2 = 42MHz) */
  return 42000000;
}
- 更新原因：Create replacement for HAL_RCC_GetPCLK2Freq to remove hardware-dependent register read. The original function reads from RCC->CFGR register to determine clock prescaler. In emulation, we return a reasonable default value (42MHz) that matches typical STM32F4 configuration where HCLK is 84MHz and APB2 prescaler is 2.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：uint32_t HAL_RCC_GetPCLK2Freq(void)
{
  /* Get HCLK source and Compute PCLK2 frequency ---------------------------*/
  /* [INIT REMOVED] Hardware register read removed - return default value for emulation */
  /* Original: return (HAL_RCC_GetHCLKFreq() >> APBPrescTable[(RCC->CFGR & RCC_CFGR_PPRE2) >> RCC_CFGR_PPRE2_Pos]); */
  
  /* Return a reasonable default frequency for emulation (84MHz / 2 = 42MHz) */
  return 42000000;
}
    原因：Create replacement for HAL_RCC_GetPCLK2Freq to remove hardware-dependent register read. The original function reads from RCC->CFGR register to determine clock prescaler. In emulation, we return a reasonable default value (42MHz) that matches typical STM32F4 configuration where HCLK is 84MHz and APB2 prescaler is 2.
    时间：

=== 信息结束 ===
```

### HAL_RCC_GetSysClockFreq

```text
=== HAL_RCC_GetSysClockFreq 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：885
- 函数内容：__weak uint32_t HAL_RCC_GetSysClockFreq(void)
{
  uint32_t pllm = 0U;
  uint32_t pllvco = 0U;
  uint32_t pllp = 0U;
  uint32_t sysclockfreq = 0U;

  /* Get SYSCLK source -------------------------------------------------------*/
  switch (RCC->CFGR & RCC_CFGR_SWS)
  {
    case RCC_CFGR_SWS_HSI:  /* HSI used as system clock source */
    {
      sysclockfreq = HSI_VALUE;
      break;
    }
    case RCC_CFGR_SWS_HSE:  /* HSE used as system clock  source */
    {
      sysclockfreq = HSE_VALUE;
      break;
    }
    case RCC_CFGR_SWS_PLL:  /* PLL used as system clock  source */
    {
      /* PLL_VCO = (HSE_VALUE or HSI_VALUE / PLLM) * PLLN
      SYSCLK = PLL_VCO / PLLP */
      pllm = RCC->PLLCFGR & RCC_PLLCFGR_PLLM;
      if (__HAL_RCC_GET_PLL_OSCSOURCE() != RCC_PLLSOURCE_HSI)
      {
        /* HSE used as PLL clock source */
        pllvco = (uint32_t)((((uint64_t) HSE_VALUE * ((uint64_t)((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> RCC_PLLCFGR_PLLN_Pos)))) / (uint64_t)pllm);
      }
      else
      {
        /* HSI used as PLL clock source */
        pllvco = (uint32_t)((((uint64_t) HSI_VALUE * ((uint64_t)((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> RCC_PLLCFGR_PLLN_Pos)))) / (uint64_t)pllm);
      }
      pllp = ((((RCC->PLLCFGR & RCC_PLLCFGR_PLLP) >> RCC_PLLCFGR_PLLP_Pos) + 1U) * 2U);

      sysclockfreq = pllvco / pllp;
      break;
    }
    default:
    {
      sysclockfreq = HSI_VALUE;
      break;
    }
  }
  return sysclockfreq;
}


【替换更新】
- 更新代码：__weak uint32_t HAL_RCC_GetSysClockFreq(void)
{
  /* [INIT REMOVED] Hardware register reads removed - return default value for emulation */
  /* Original function reads RCC->CFGR and RCC->PLLCFGR registers to determine system clock frequency */
  
  /* Return a reasonable default frequency for emulation (84MHz for STM32F4) */
  return 84000000;
}
- 更新原因：Create replacement for HAL_RCC_GetSysClockFreq to remove hardware-dependent register reads. The original function reads from RCC->CFGR and RCC->PLLCFGR registers to determine the current system clock source and frequency. In emulation, we return a reasonable default value (84MHz) that matches typical STM32F4 configuration. This function is called by HAL_RCC_ClockConfig which updates SystemCoreClock global variable.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__weak uint32_t HAL_RCC_GetSysClockFreq(void)
{
  /* [INIT REMOVED] Hardware register reads removed - return default value for emulation */
  /* Original function reads RCC->CFGR and RCC->PLLCFGR registers to determine system clock frequency */
  
  /* Return a reasonable default frequency for emulation (84MHz for STM32F4) */
  return 84000000;
}
    原因：Create replacement for HAL_RCC_GetSysClockFreq to remove hardware-dependent register reads. The original function reads from RCC->CFGR and RCC->PLLCFGR registers to determine the current system clock source and frequency. In emulation, we return a reasonable default value (84MHz) that matches typical STM32F4 configuration. This function is called by HAL_RCC_ClockConfig which updates SystemCoreClock global variable.
    时间：

=== 信息结束 ===
```

### HAL_RCC_NMI_IRQHandler

```text
=== HAL_RCC_NMI_IRQHandler 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：1084
- 函数内容：void HAL_RCC_NMI_IRQHandler(void)
{
  /* Check RCC CSSF flag  */
  if (__HAL_RCC_GET_IT(RCC_IT_CSS))
  {
    /* RCC Clock Security System interrupt user callback */
    HAL_RCC_CSSCallback();

    /* Clear RCC CSS pending bit */
    __HAL_RCC_CLEAR_IT(RCC_IT_CSS);
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Interrupt handler for RCC Clock Security System (CSS) interrupt request, called under NMI_Handler to handle clock security system events
- 是否需要替换：是
- 分类/替换原因：This function is clearly an interrupt handler as indicated by its name ending with '_IRQHandler' and its purpose of handling RCC CSS interrupts. It checks interrupt flags, calls a user callback function, and clears interrupt flags. According to the classification priority, it fits the IRQ category (interrupt-related functions) as it contains interrupt handling logic but is not a CORE function (doesn't configure NVIC, OS kernel, or VTOR). The replacement removes hardware-specific interrupt flag operations while preserving the callback function call.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_RCC_NMI_IRQHandler(void)
{
  /* Simulate CSS interrupt being triggered */
  /* RCC Clock Security System interrupt user callback */
  HAL_RCC_CSSCallback();
  
  /* No need to check or clear hardware interrupt flags */
}
```

=== 信息结束 ===
```

### HAL_RCC_OscConfig

```text
=== HAL_RCC_OscConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：219
- 函数内容：__weak HAL_StatusTypeDef HAL_RCC_OscConfig(RCC_OscInitTypeDef  *RCC_OscInitStruct)
{
  uint32_t tickstart;
  uint32_t pll_config;
  /* Check Null pointer */
  if (RCC_OscInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_OSCILLATORTYPE(RCC_OscInitStruct->OscillatorType));
  /*------------------------------- HSE Configuration ------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSE) == RCC_OSCILLATORTYPE_HSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSE(RCC_OscInitStruct->HSEState));
    /* When the HSE is used as system clock or clock source for PLL in these cases HSE will not disabled */
    if ((__HAL_RCC_GET_SYSCLK_SOURCE() == RCC_CFGR_SWS_HSE) || \
        ((__HAL_RCC_GET_SYSCLK_SOURCE() == RCC_CFGR_SWS_PLL) && ((RCC->PLLCFGR & RCC_PLLCFGR_PLLSRC) == RCC_PLLCFGR_PLLSRC_HSE)))
    {
      if ((__HAL_RCC_GET_FLAG(RCC_FLAG_HSERDY) != RESET) && (RCC_OscInitStruct->HSEState == RCC_HSE_OFF))
      {
        return HAL_ERROR;
      }
    }
    else
    {
      /* Set the new HSE configuration ---------------------------------------*/
      __HAL_RCC_HSE_CONFIG(RCC_OscInitStruct->HSEState);

      /* Check the HSE State */
      if ((RCC_OscInitStruct->HSEState) != RCC_HSE_OFF)
      {
        /* Get Start Tick */
        tickstart = HAL_GetTick();

        /* Wait till HSE is ready */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_HSERDY) == RESET)
        {
          if ((HAL_GetTick() - tickstart) > HSE_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
      else
      {
        /* Get Start Tick */
        tickstart = HAL_GetTick();

        /* Wait till HSE is bypassed or disabled */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_HSERDY) != RESET)
        {
          if ((HAL_GetTick() - tickstart) > HSE_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
    }
  }
  /*----------------------------- HSI Configuration --------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSI) == RCC_OSCILLATORTYPE_HSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSI(RCC_OscInitStruct->HSIState));
    assert_param(IS_RCC_CALIBRATION_VALUE(RCC_OscInitStruct->HSICalibrationValue));

    /* Check if HSI is used as system clock or as PLL source when PLL is selected as system clock */
    if ((__HAL_RCC_GET_SYSCLK_SOURCE() == RCC_CFGR_SWS_HSI) || \
        ((__HAL_RCC_GET_SYSCLK_SOURCE() == RCC_CFGR_SWS_PLL) && ((RCC->PLLCFGR & RCC_PLLCFGR_PLLSRC) == RCC_PLLCFGR_PLLSRC_HSI)))
    {
      /* When HSI is used as system clock it will not disabled */
      if ((__HAL_RCC_GET_FLAG(RCC_FLAG_HSIRDY) != RESET) && (RCC_OscInitStruct->HSIState != RCC_HSI_ON))
      {
        return HAL_ERROR;
      }
      /* Otherwise, just the calibration is allowed */
      else
      {
        /* Adjusts the Internal High Speed oscillator (HSI) calibration value.*/
        __HAL_RCC_HSI_CALIBRATIONVALUE_ADJUST(RCC_OscInitStruct->HSICalibrationValue);
      }
    }
    else
    {
      /* Check the HSI State */
      if ((RCC_OscInitStruct->HSIState) != RCC_HSI_OFF)
      {
        /* Enable the Internal High Speed oscillator (HSI). */
        __HAL_RCC_HSI_ENABLE();

        /* Get Start Tick*/
        tickstart = HAL_GetTick();

        /* Wait till HSI is ready */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_HSIRDY) == RESET)
        {
          if ((HAL_GetTick() - tickstart) > HSI_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }

        /* Adjusts the Internal High Speed oscillator (HSI) calibration value. */
        __HAL_RCC_HSI_CALIBRATIONVALUE_ADJUST(RCC_OscInitStruct->HSICalibrationValue);
      }
      else
      {
        /* Disable the Internal High Speed oscillator (HSI). */
        __HAL_RCC_HSI_DISABLE();

        /* Get Start Tick*/
        tickstart = HAL_GetTick();

        /* Wait till HSI is ready */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_HSIRDY) != RESET)
        {
          if ((HAL_GetTick() - tickstart) > HSI_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
    }
  }
  /*------------------------------ LSI Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSI) == RCC_OSCILLATORTYPE_LSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSI(RCC_OscInitStruct->LSIState));

    /* Check the LSI State */
    if ((RCC_OscInitStruct->LSIState) != RCC_LSI_OFF)
    {
      /* Enable the Internal Low Speed oscillator (LSI). */
      __HAL_RCC_LSI_ENABLE();

      /* Get Start Tick*/
      tickstart = HAL_GetTick();

      /* Wait till LSI is ready */
      while (__HAL_RCC_GET_FLAG(RCC_FLAG_LSIRDY) == RESET)
      {
        if ((HAL_GetTick() - tickstart) > LSI_TIMEOUT_VALUE)
        {
          return HAL_TIMEOUT;
        }
      }
    }
    else
    {
      /* Disable the Internal Low Speed oscillator (LSI). */
      __HAL_RCC_LSI_DISABLE();

      /* Get Start Tick */
      tickstart = HAL_GetTick();

      /* Wait till LSI is ready */
      while (__HAL_RCC_GET_FLAG(RCC_FLAG_LSIRDY) != RESET)
      {
        if ((HAL_GetTick() - tickstart) > LSI_TIMEOUT_VALUE)
        {
          return HAL_TIMEOUT;
        }
      }
    }
  }
  /*------------------------------ LSE Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSE) == RCC_OSCILLATORTYPE_LSE)
  {
    FlagStatus       pwrclkchanged = RESET;

    /* Check the parameters */
    assert_param(IS_RCC_LSE(RCC_OscInitStruct->LSEState));

    /* Update LSE configuration in Backup Domain control register    */
    /* Requires to enable write access to Backup Domain of necessary */
    if (__HAL_RCC_PWR_IS_CLK_DISABLED())
    {
      __HAL_RCC_PWR_CLK_ENABLE();
      pwrclkchanged = SET;
    }

    if (HAL_IS_BIT_CLR(PWR->CR, PWR_CR_DBP))
    {
      /* Enable write access to Backup domain */
      SET_BIT(PWR->CR, PWR_CR_DBP);

      /* Wait for Backup domain Write protection disable */
      tickstart = HAL_GetTick();

      while (HAL_IS_BIT_CLR(PWR->CR, PWR_CR_DBP))
      {
        if ((HAL_GetTick() - tickstart) > RCC_DBP_TIMEOUT_VALUE)
        {
          return HAL_TIMEOUT;
        }
      }
    }

    /* Set the new LSE configuration -----------------------------------------*/
    __HAL_RCC_LSE_CONFIG(RCC_OscInitStruct->LSEState);
    /* Check the LSE State */
    if ((RCC_OscInitStruct->LSEState) != RCC_LSE_OFF)
    {
      /* Get Start Tick*/
      tickstart = HAL_GetTick();

      /* Wait till LSE is ready */
      while (__HAL_RCC_GET_FLAG(RCC_FLAG_LSERDY) == RESET)
      {
        if ((HAL_GetTick() - tickstart) > RCC_LSE_TIMEOUT_VALUE)
        {
          return HAL_TIMEOUT;
        }
      }
    }
    else
    {
      /* Get Start Tick */
      tickstart = HAL_GetTick();

      /* Wait till LSE is ready */
      while (__HAL_RCC_GET_FLAG(RCC_FLAG_LSERDY) != RESET)
      {
        if ((HAL_GetTick() - tickstart) > RCC_LSE_TIMEOUT_VALUE)
        {
          return HAL_TIMEOUT;
        }
      }
    }

    /* Restore clock configuration if changed */
    if (pwrclkchanged == SET)
    {
      __HAL_RCC_PWR_CLK_DISABLE();
    }
  }
  /*-------------------------------- PLL Configuration -----------------------*/
  /* Check the parameters */
  assert_param(IS_RCC_PLL(RCC_OscInitStruct->PLL.PLLState));
  if ((RCC_OscInitStruct->PLL.PLLState) != RCC_PLL_NONE)
  {
    /* Check if the PLL is used as system clock or not */
    if (__HAL_RCC_GET_SYSCLK_SOURCE() != RCC_CFGR_SWS_PLL)
    {
      if ((RCC_OscInitStruct->PLL.PLLState) == RCC_PLL_ON)
      {
        /* Check the parameters */
        assert_param(IS_RCC_PLLSOURCE(RCC_OscInitStruct->PLL.PLLSource));
        assert_param(IS_RCC_PLLM_VALUE(RCC_OscInitStruct->PLL.PLLM));
        assert_param(IS_RCC_PLLN_VALUE(RCC_OscInitStruct->PLL.PLLN));
        assert_param(IS_RCC_PLLP_VALUE(RCC_OscInitStruct->PLL.PLLP));
        assert_param(IS_RCC_PLLQ_VALUE(RCC_OscInitStruct->PLL.PLLQ));

        /* Disable the main PLL. */
        __HAL_RCC_PLL_DISABLE();

        /* Get Start Tick */
        tickstart = HAL_GetTick();

        /* Wait till PLL is disabled */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) != RESET)
        {
          if ((HAL_GetTick() - tickstart) > PLL_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }

        /* Configure the main PLL clock source, multiplication and division factors. */
        WRITE_REG(RCC->PLLCFGR, (RCC_OscInitStruct->PLL.PLLSource                                            | \
                                 RCC_OscInitStruct->PLL.PLLM                                                 | \
                                 (RCC_OscInitStruct->PLL.PLLN << RCC_PLLCFGR_PLLN_Pos)             | \
                                 (((RCC_OscInitStruct->PLL.PLLP >> 1U) - 1U) << RCC_PLLCFGR_PLLP_Pos) | \
                                 (RCC_OscInitStruct->PLL.PLLQ << RCC_PLLCFGR_PLLQ_Pos)));
        /* Enable the main PLL. */
        __HAL_RCC_PLL_ENABLE();

        /* Get Start Tick */
        tickstart = HAL_GetTick();

        /* Wait till PLL is ready */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) == RESET)
        {
          if ((HAL_GetTick() - tickstart) > PLL_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
      else
      {
        /* Disable the main PLL. */
        __HAL_RCC_PLL_DISABLE();

        /* Get Start Tick */
        tickstart = HAL_GetTick();

        /* Wait till PLL is disabled */
        while (__HAL_RCC_GET_FLAG(RCC_FLAG_PLLRDY) != RESET)
        {
          if ((HAL_GetTick() - tickstart) > PLL_TIMEOUT_VALUE)
          {
            return HAL_TIMEOUT;
          }
        }
      }
    }
    else
    {
      /* Check if there is a request to disable the PLL used as System clock source */
      if ((RCC_OscInitStruct->PLL.PLLState) == RCC_PLL_OFF)
      {
        return HAL_ERROR;
      }
      else
      {
        /* Do not return HAL_ERROR if request repeats the current configuration */
        pll_config = RCC->PLLCFGR;
#if defined (RCC_PLLCFGR_PLLR)
        if (((RCC_OscInitStruct->PLL.PLLState) == RCC_PLL_OFF) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLSRC) != RCC_OscInitStruct->PLL.PLLSource) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLM) != (RCC_OscInitStruct->PLL.PLLM) << RCC_PLLCFGR_PLLM_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLN) != (RCC_OscInitStruct->PLL.PLLN) << RCC_PLLCFGR_PLLN_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLP) != (((RCC_OscInitStruct->PLL.PLLP >> 1U) - 1U)) << RCC_PLLCFGR_PLLP_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLQ) != (RCC_OscInitStruct->PLL.PLLQ << RCC_PLLCFGR_PLLQ_Pos)) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLR) != (RCC_OscInitStruct->PLL.PLLR << RCC_PLLCFGR_PLLR_Pos)))
#else
        if (((RCC_OscInitStruct->PLL.PLLState) == RCC_PLL_OFF) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLSRC) != RCC_OscInitStruct->PLL.PLLSource) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLM) != (RCC_OscInitStruct->PLL.PLLM) << RCC_PLLCFGR_PLLM_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLN) != (RCC_OscInitStruct->PLL.PLLN) << RCC_PLLCFGR_PLLN_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLP) != (((RCC_OscInitStruct->PLL.PLLP >> 1U) - 1U)) << RCC_PLLCFGR_PLLP_Pos) ||
            (READ_BIT(pll_config, RCC_PLLCFGR_PLLQ) != (RCC_OscInitStruct->PLL.PLLQ << RCC_PLLCFGR_PLLQ_Pos)))
#endif /* RCC_PLLCFGR_PLLR */
        {
          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【替换更新】
- 更新代码：/**
* @brief  Initializes the RCC Oscillators according to the specified parameters in the
*         RCC_OscInitTypeDef.
* @param  RCC_OscInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC Oscillators.
* @note   The PLL is not disabled when used as system clock.
* @note   Transitions LSE Bypass to LSE On and LSE On to LSE Bypass are not
*         supported by this function. User should request a transition to LSE Off
*         first and then LSE On or LSE Bypass.
* @note   Transition HSE Bypass to HSE On and HSE On to HSE Bypass are not
*         supported by this function. User should request a transition to HSE Off
*         first and then HSE On or HSE Bypass.
* @retval HAL status
*/
__weak HAL_StatusTypeDef HAL_RCC_OscConfig(RCC_OscInitTypeDef  *RCC_OscInitStruct)
{
  /* Check Null pointer */
  if (RCC_OscInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_OSCILLATORTYPE(RCC_OscInitStruct->OscillatorType));

  /*------------------------------- HSE Configuration ------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSE) == RCC_OSCILLATORTYPE_HSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSE(RCC_OscInitStruct->HSEState));
    /* Skip hardware-specific clock source checks and configuration */
  }
  /*----------------------------- HSI Configuration --------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSI) == RCC_OSCILLATORTYPE_HSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSI(RCC_OscInitStruct->HSIState));
    assert_param(IS_RCC_CALIBRATION_VALUE(RCC_OscInitStruct->HSICalibrationValue));
    /* Skip hardware-specific clock source checks and configuration */
  }
  /*------------------------------ LSI Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSI) == RCC_OSCILLATORTYPE_LSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSI(RCC_OscInitStruct->LSIState));
    /* Skip hardware enable/disable operations */
  }
  /*------------------------------ LSE Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSE) == RCC_OSCILLATORTYPE_LSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSE(RCC_OscInitStruct->LSEState));
    /* Skip backup domain access and LSE configuration */
  }
  /*-------------------------------- PLL Configuration -----------------------*/
  /* Check the parameters */
  assert_param(IS_RCC_PLL(RCC_OscInitStruct->PLL.PLLState));
  if ((RCC_OscInitStruct->PLL.PLLState) != RCC_PLL_NONE)
  {
    /* Skip hardware-specific clock source checks */
    /* Skip PLL configuration and enable/disable operations */
  }
  return HAL_OK;
}
- 更新原因：Simplify HAL_RCC_OscConfig replacement to avoid all hardware-dependent macro calls. Remove any conditional logic that depends on hardware register reads like __HAL_RCC_GET_SYSCLK_SOURCE() and __HAL_RCC_GET_FLAG(). Keep only parameter validation and return HAL_OK for successful emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Initializes the RCC Oscillators according to the specified parameters in the
*         RCC_OscInitTypeDef.
* @param  RCC_OscInitStruct pointer to an RCC_OscInitTypeDef structure that
*         contains the configuration information for the RCC Oscillators.
* @note   The PLL is not disabled when used as system clock.
* @note   Transitions LSE Bypass to LSE On and LSE On to LSE Bypass are not
*         supported by this function. User should request a transition to LSE Off
*         first and then LSE On or LSE Bypass.
* @note   Transition HSE Bypass to HSE On and HSE On to HSE Bypass are not
*         supported by this function. User should request a transition to HSE Off
*         first and then HSE On or HSE Bypass.
* @retval HAL status
*/
__weak HAL_StatusTypeDef HAL_RCC_OscConfig(RCC_OscInitTypeDef  *RCC_OscInitStruct)
{
  /* Check Null pointer */
  if (RCC_OscInitStruct == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_RCC_OSCILLATORTYPE(RCC_OscInitStruct->OscillatorType));

  /*------------------------------- HSE Configuration ------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSE) == RCC_OSCILLATORTYPE_HSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSE(RCC_OscInitStruct->HSEState));
    /* Skip hardware-specific clock source checks and configuration */
  }
  /*----------------------------- HSI Configuration --------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSI) == RCC_OSCILLATORTYPE_HSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSI(RCC_OscInitStruct->HSIState));
    assert_param(IS_RCC_CALIBRATION_VALUE(RCC_OscInitStruct->HSICalibrationValue));
    /* Skip hardware-specific clock source checks and configuration */
  }
  /*------------------------------ LSI Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSI) == RCC_OSCILLATORTYPE_LSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSI(RCC_OscInitStruct->LSIState));
    /* Skip hardware enable/disable operations */
  }
  /*------------------------------ LSE Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSE) == RCC_OSCILLATORTYPE_LSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSE(RCC_OscInitStruct->LSEState));
    /* Skip backup domain access and LSE configuration */
  }
  /*-------------------------------- PLL Configuration -----------------------*/
  /* Check the parameters */
  assert_param(IS_RCC_PLL(RCC_OscInitStruct->PLL.PLLState));
  if ((RCC_OscInitStruct->PLL.PLLState) != RCC_PLL_NONE)
  {
    /* Skip hardware-specific clock source checks */
    /* Skip PLL configuration and enable/disable operations */
  }
  return HAL_OK;
}
    原因：Simplify HAL_RCC_OscConfig replacement to avoid all hardware-dependent macro calls. Remove any conditional logic that depends on hardware register reads like __HAL_RCC_GET_SYSCLK_SOURCE() and __HAL_RCC_GET_FLAG(). Keep only parameter validation and return HAL_OK for successful emulation.
    时间：

=== 信息结束 ===
```

### HAL_SPI_Init

```text
=== HAL_SPI_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c
- 行号：311
- 函数内容：HAL_StatusTypeDef HAL_SPI_Init(SPI_HandleTypeDef *hspi)
{
  /* Check the SPI handle allocation */
  if (hspi == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_SPI_ALL_INSTANCE(hspi->Instance));
  assert_param(IS_SPI_MODE(hspi->Init.Mode));
  assert_param(IS_SPI_DIRECTION(hspi->Init.Direction));
  assert_param(IS_SPI_DATASIZE(hspi->Init.DataSize));
  assert_param(IS_SPI_NSS(hspi->Init.NSS));
  assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));
  assert_param(IS_SPI_FIRST_BIT(hspi->Init.FirstBit));
  assert_param(IS_SPI_TIMODE(hspi->Init.TIMode));
  if (hspi->Init.TIMode == SPI_TIMODE_DISABLE)
  {
    assert_param(IS_SPI_CPOL(hspi->Init.CLKPolarity));
    assert_param(IS_SPI_CPHA(hspi->Init.CLKPhase));

    if (hspi->Init.Mode == SPI_MODE_MASTER)
    {
      assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));
    }
    else
    {
      /* Baudrate prescaler not use in Motoraola Slave mode. force to default value */
      hspi->Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_2;
    }
  }
  else
  {
    assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));

    /* Force polarity and phase to TI protocaol requirements */
    hspi->Init.CLKPolarity = SPI_POLARITY_LOW;
    hspi->Init.CLKPhase    = SPI_PHASE_1EDGE;
  }
#if (USE_SPI_CRC != 0U)
  assert_param(IS_SPI_CRC_CALCULATION(hspi->Init.CRCCalculation));
  if (hspi->Init.CRCCalculation == SPI_CRCCALCULATION_ENABLE)
  {
    assert_param(IS_SPI_CRC_POLYNOMIAL(hspi->Init.CRCPolynomial));
  }
#else
  hspi->Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
#endif /* USE_SPI_CRC */

  if (hspi->State == HAL_SPI_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    hspi->Lock = HAL_UNLOCKED;

#if (USE_HAL_SPI_REGISTER_CALLBACKS == 1U)
    /* Init the SPI Callback settings */
    hspi->TxCpltCallback       = HAL_SPI_TxCpltCallback;       /* Legacy weak TxCpltCallback       */
    hspi->RxCpltCallback       = HAL_SPI_RxCpltCallback;       /* Legacy weak RxCpltCallback       */
    hspi->TxRxCpltCallback     = HAL_SPI_TxRxCpltCallback;     /* Legacy weak TxRxCpltCallback     */
    hspi->TxHalfCpltCallback   = HAL_SPI_TxHalfCpltCallback;   /* Legacy weak TxHalfCpltCallback   */
    hspi->RxHalfCpltCallback   = HAL_SPI_RxHalfCpltCallback;   /* Legacy weak RxHalfCpltCallback   */
    hspi->TxRxHalfCpltCallback = HAL_SPI_TxRxHalfCpltCallback; /* Legacy weak TxRxHalfCpltCallback */
    hspi->ErrorCallback        = HAL_SPI_ErrorCallback;        /* Legacy weak ErrorCallback        */
    hspi->AbortCpltCallback    = HAL_SPI_AbortCpltCallback;    /* Legacy weak AbortCpltCallback    */

    if (hspi->MspInitCallback == NULL)
    {
      hspi->MspInitCallback = HAL_SPI_MspInit; /* Legacy weak MspInit  */
    }

    /* Init the low level hardware : GPIO, CLOCK, NVIC... */
    hspi->MspInitCallback(hspi);
#else
    /* Init the low level hardware : GPIO, CLOCK, NVIC... */
    HAL_SPI_MspInit(hspi);
#endif /* USE_HAL_SPI_REGISTER_CALLBACKS */
  }

  hspi->State = HAL_SPI_STATE_BUSY;

  /* Disable the selected SPI peripheral */
  __HAL_SPI_DISABLE(hspi);

  /*----------------------- SPIx CR1 & CR2 Configuration ---------------------*/
  /* Configure : SPI Mode, Communication Mode, Data size, Clock polarity and phase, NSS management,
  Communication speed, First bit and CRC calculation state */
  WRITE_REG(hspi->Instance->CR1, ((hspi->Init.Mode & (SPI_CR1_MSTR | SPI_CR1_SSI)) |
                                  (hspi->Init.Direction & (SPI_CR1_RXONLY | SPI_CR1_BIDIMODE)) |
                                  (hspi->Init.DataSize & SPI_CR1_DFF) |
                                  (hspi->Init.CLKPolarity & SPI_CR1_CPOL) |
                                  (hspi->Init.CLKPhase & SPI_CR1_CPHA) |
                                  (hspi->Init.NSS & SPI_CR1_SSM) |
                                  (hspi->Init.BaudRatePrescaler & SPI_CR1_BR_Msk) |
                                  (hspi->Init.FirstBit  & SPI_CR1_LSBFIRST) |
                                  (hspi->Init.CRCCalculation & SPI_CR1_CRCEN)));

  /* Configure : NSS management, TI Mode */
  WRITE_REG(hspi->Instance->CR2, (((hspi->Init.NSS >> 16U) & SPI_CR2_SSOE) | (hspi->Init.TIMode & SPI_CR2_FRF)));

#if (USE_SPI_CRC != 0U)
  /*---------------------------- SPIx CRCPOLY Configuration ------------------*/
  /* Configure : CRC Polynomial */
  if (hspi->Init.CRCCalculation == SPI_CRCCALCULATION_ENABLE)
  {
    WRITE_REG(hspi->Instance->CRCPR, (hspi->Init.CRCPolynomial & SPI_CRCPR_CRCPOLY_Msk));
  }
#endif /* USE_SPI_CRC */

#if defined(SPI_I2SCFGR_I2SMOD)
  /* Activate the SPI mode (Make sure that I2SMOD bit in I2SCFGR register is reset) */
  CLEAR_BIT(hspi->Instance->I2SCFGR, SPI_I2SCFGR_I2SMOD);
#endif /* SPI_I2SCFGR_I2SMOD */

  hspi->ErrorCode = HAL_SPI_ERROR_NONE;
  hspi->State     = HAL_SPI_STATE_READY;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the SPI peripheral according to specified parameters in the SPI_InitTypeDef structure and initializes the associated handle.
- 是否需要替换：是
- 分类/替换原因：The function is a peripheral initialization function that configures SPI hardware registers through MMIO operations (WRITE_REG, CLEAR_BIT, __HAL_SPI_DISABLE macros). It contains parameter validation, structure initialization (lock, callbacks), state management, and calls to low-level hardware initialization (HAL_SPI_MspInit). According to the classification priority, it fits the INIT type as it initializes peripheral configurations and contains hardware register accesses that need to be removed while preserving non-hardware logic and state management.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_SPI_Init(SPI_HandleTypeDef *hspi)
{
  /* Check the SPI handle allocation */
  if (hspi == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_SPI_ALL_INSTANCE(hspi->Instance));
  assert_param(IS_SPI_MODE(hspi->Init.Mode));
  assert_param(IS_SPI_DIRECTION(hspi->Init.Direction));
  assert_param(IS_SPI_DATASIZE(hspi->Init.DataSize));
  assert_param(IS_SPI_NSS(hspi->Init.NSS));
  assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));
  assert_param(IS_SPI_FIRST_BIT(hspi->Init.FirstBit));
  assert_param(IS_SPI_TIMODE(hspi->Init.TIMode));
  if (hspi->Init.TIMode == SPI_TIMODE_DISABLE)
  {
    assert_param(IS_SPI_CPOL(hspi->Init.CLKPolarity));
    assert_param(IS_SPI_CPHA(hspi->Init.CLKPhase));

    if (hspi->Init.Mode == SPI_MODE_MASTER)
    {
      assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));
    }
    else
    {
      /* Baudrate prescaler not use in Motoraola Slave mode. force to default value */
      hspi->Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_2;
    }
  }
  else
  {
    assert_param(IS_SPI_BAUDRATE_PRESCALER(hspi->Init.BaudRatePrescaler));

    /* Force polarity and phase to TI protocaol requirements */
    hspi->Init.CLKPolarity = SPI_POLARITY_LOW;
    hspi->Init.CLKPhase    = SPI_PHASE_1EDGE;
  }
#if (USE_SPI_CRC != 0U)
  assert_param(IS_SPI_CRC_CALCULATION(hspi->Init.CRCCalculation));
  if (hspi->Init.CRCCalculation == SPI_CRCCALCULATION_ENABLE)
  {
    assert_param(IS_SPI_CRC_POLYNOMIAL(hspi->Init.CRCPolynomial));
  }
#else
  hspi->Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
#endif /* USE_SPI_CRC */

  if (hspi->State == HAL_SPI_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    hspi->Lock = HAL_UNLOCKED;

#if (USE_HAL_SPI_REGISTER_CALLBACKS == 1U)
    /* Init the SPI Callback settings */
    hspi->TxCpltCallback       = HAL_SPI_TxCpltCallback;       /* Legacy weak TxCpltCallback       */
    hspi->RxCpltCallback       = HAL_SPI_RxCpltCallback;       /* Legacy weak RxCpltCallback       */
    hspi->TxRxCpltCallback     = HAL_SPI_TxRxCpltCallback;     /* Legacy weak TxRxCpltCallback     */
    hspi->TxHalfCpltCallback   = HAL_SPI_TxHalfCpltCallback;   /* Legacy weak TxHalfCpltCallback   */
    hspi->RxHalfCpltCallback   = HAL_SPI_RxHalfCpltCallback;   /* Legacy weak RxHalfCpltCallback   */
    hspi->TxRxHalfCpltCallback = HAL_SPI_TxRxHalfCpltCallback; /* Legacy weak TxRxHalfCpltCallback */
    hspi->ErrorCallback        = HAL_SPI_ErrorCallback;        /* Legacy weak ErrorCallback        */
    hspi->AbortCpltCallback    = HAL_SPI_AbortCpltCallback;    /* Legacy weak AbortCpltCallback    */

    if (hspi->MspInitCallback == NULL)
    {
      hspi->MspInitCallback = HAL_SPI_MspInit; /* Legacy weak MspInit  */
    }

    /* Init the low level hardware : GPIO, CLOCK, NVIC... */
    hspi->MspInitCallback(hspi);
#else
    /* Init the low level hardware : GPIO, CLOCK, NVIC... */
    HAL_SPI_MspInit(hspi);
#endif /* USE_HAL_SPI_REGISTER_CALLBACKS */
  }

  hspi->State = HAL_SPI_STATE_BUSY;

  /* Skip hardware-specific configuration */
  /* Original: __HAL_SPI_DISABLE(hspi); */
  /* Original: WRITE_REG(hspi->Instance->CR1, ...); */
  /* Original: WRITE_REG(hspi->Instance->CR2, ...); */
  /* Original: WRITE_REG(hspi->Instance->CRCPR, ...); */
  /* Original: CLEAR_BIT(hspi->Instance->I2SCFGR, SPI_I2SCFGR_I2SMOD); */

  hspi->ErrorCode = HAL_SPI_ERROR_NONE;
  hspi->State     = HAL_SPI_STATE_READY;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_TIM_Base_MspInit

```text
=== HAL_TIM_Base_MspInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c
- 行号：262
- 函数内容：void HAL_TIM_Base_MspInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspInit 0 */

  /* USER CODE END TIM1_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM1_CLK_ENABLE();
  /* USER CODE BEGIN TIM1_MspInit 1 */

  /* USER CODE END TIM1_MspInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspInit 0 */

  /* USER CODE END TIM2_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM2_CLK_ENABLE();
  /* USER CODE BEGIN TIM2_MspInit 1 */

  /* USER CODE END TIM2_MspInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspInit 0 */

  /* USER CODE END TIM3_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM3_CLK_ENABLE();
  /* USER CODE BEGIN TIM3_MspInit 1 */

  /* USER CODE END TIM3_MspInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspInit 0 */

  /* USER CODE END TIM4_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM4_CLK_ENABLE();
  /* USER CODE BEGIN TIM4_MspInit 1 */

  /* USER CODE END TIM4_MspInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspInit 0 */

  /* USER CODE END TIM9_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM9_CLK_ENABLE();
  /* USER CODE BEGIN TIM9_MspInit 1 */

  /* USER CODE END TIM9_MspInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspInit 0 */

  /* USER CODE END TIM11_MspInit 0 */
    /* Peripheral clock enable */
    __HAL_RCC_TIM11_CLK_ENABLE();
  /* USER CODE BEGIN TIM11_MspInit 1 */

  /* USER CODE END TIM11_MspInit 1 */
  }

}


【初始分析（FunctionClassifier）】
- 函数类型：SKIP
- 函数用途/功能描述：Weak empty implementation of TIM Base MSP initialization meant to be optionally overridden by user for hardware-specific initialization
- 是否需要替换：否
- 分类/替换原因：GetFunctionInfo revealed this is a __weak empty function with only UNUSED(htim) and a comment indicating it should be implemented in user files when needed. GetMMIOFunctionInfo confirmed no MMIO operations. GetFunctionCallStack shows it's called by HAL_TIM_Base_Init as part of initialization sequence. This is a classic MSP (Microcontroller Specific Package) pattern in STM32 HAL where empty placeholder functions are provided for optional user override. Since it's empty by default and contains no hardware operations, it can be safely classified as SKIP - a non-critical driver function performing optional operations that can be safely ignored.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：void HAL_TIM_Base_MspInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspInit 0 */

  /* USER CODE END TIM1_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM1_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM1_MspInit 1 */

  /* USER CODE END TIM1_MspInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspInit 0 */

  /* USER CODE END TIM2_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM2_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM2_MspInit 1 */

  /* USER CODE END TIM2_MspInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspInit 0 */

  /* USER CODE END TIM3_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM3_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM3_MspInit 1 */

  /* USER CODE END TIM3_MspInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspInit 0 */

  /* USER CODE END TIM4_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM4_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM4_MspInit 1 */

  /* USER CODE END TIM4_MspInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspInit 0 */

  /* USER CODE END TIM9_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM9_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM9_MspInit 1 */

  /* USER CODE END TIM9_MspInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspInit 0 */

  /* USER CODE END TIM11_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM11_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM11_MspInit 1 */

  /* USER CODE END TIM11_MspInit 1 */
  }

}
- 更新原因：Replace HAL_TIM_Base_MspInit function to remove hardware-specific clock enable operations. The function contains multiple __HAL_RCC_TIMx_CLK_ENABLE() calls that access hardware registers. These are removed with [INIT REMOVED] comments while preserving the function structure and conditional logic based on TIM instance.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_TIM_Base_MspInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspInit 0 */

  /* USER CODE END TIM1_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM1_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM1_MspInit 1 */

  /* USER CODE END TIM1_MspInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspInit 0 */

  /* USER CODE END TIM2_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM2_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM2_MspInit 1 */

  /* USER CODE END TIM2_MspInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspInit 0 */

  /* USER CODE END TIM3_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM3_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM3_MspInit 1 */

  /* USER CODE END TIM3_MspInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspInit 0 */

  /* USER CODE END TIM4_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM4_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM4_MspInit 1 */

  /* USER CODE END TIM4_MspInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspInit 0 */

  /* USER CODE END TIM9_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM9_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM9_MspInit 1 */

  /* USER CODE END TIM9_MspInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspInit 0 */

  /* USER CODE END TIM11_MspInit 0 */
    /* [INIT REMOVED] Peripheral clock enable removed */
    /* __HAL_RCC_TIM11_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM11_MspInit 1 */

  /* USER CODE END TIM11_MspInit 1 */
  }

}
    原因：Replace HAL_TIM_Base_MspInit function to remove hardware-specific clock enable operations. The function contains multiple __HAL_RCC_TIMx_CLK_ENABLE() calls that access hardware registers. These are removed with [INIT REMOVED] comments while preserving the function structure and conditional logic based on TIM instance.
    时间：

=== 信息结束 ===
```

### HAL_TIM_MspPostInit

```text
=== HAL_TIM_MspPostInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c
- 行号：333
- 函数内容：void HAL_TIM_MspPostInit(TIM_HandleTypeDef* htim)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(htim->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspPostInit 0 */

  /* USER CODE END TIM1_MspPostInit 0 */
    __HAL_RCC_GPIOA_CLK_ENABLE();
    /**TIM1 GPIO Configuration
    PA7     ------> TIM1_CH1N
    PA8     ------> TIM1_CH1
    PA11     ------> TIM1_CH4
    */
    GPIO_InitStruct.Pin = GPIO_PIN_7|GPIO_PIN_8|GPIO_PIN_11;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF1_TIM1;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /* USER CODE BEGIN TIM1_MspPostInit 1 */

  /* USER CODE END TIM1_MspPostInit 1 */
  }
  else if(htim->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspPostInit 0 */

  /* USER CODE END TIM2_MspPostInit 0 */

    __HAL_RCC_GPIOB_CLK_ENABLE();
    /**TIM2 GPIO Configuration
    PB10     ------> TIM2_CH3
    PB3     ------> TIM2_CH2
    */
    GPIO_InitStruct.Pin = GPIO_PIN_10|GPIO_PIN_3;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF1_TIM2;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN TIM2_MspPostInit 1 */

  /* USER CODE END TIM2_MspPostInit 1 */
  }
  else if(htim->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspPostInit 0 */

  /* USER CODE END TIM3_MspPostInit 0 */

    __HAL_RCC_GPIOC_CLK_ENABLE();
    __HAL_RCC_GPIOB_CLK_ENABLE();
    /**TIM3 GPIO Configuration
    PC7     ------> TIM3_CH2
    PB4     ------> TIM3_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN TIM3_MspPostInit 1 */

  /* USER CODE END TIM3_MspPostInit 1 */
  }
  else if(htim->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspPostInit 0 */

  /* USER CODE END TIM4_MspPostInit 0 */

    __HAL_RCC_GPIOB_CLK_ENABLE();
    /**TIM4 GPIO Configuration
    PB6     ------> TIM4_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM4;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* USER CODE BEGIN TIM4_MspPostInit 1 */

  /* USER CODE END TIM4_MspPostInit 1 */
  }

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Post-initialization callback function that configures GPIO alternate functions for TIM (Timer) peripheral channels after TIM initialization.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this function configures GPIO alternate functions for TIM channels (TIM1, TIM2, TIM3, TIM4). GetMMIOFunctionInfo reveals hardware register accesses through __HAL_RCC_GPIOx_CLK_ENABLE() macros and HAL_GPIO_Init() calls. The function is a post-initialization callback that performs hardware-specific GPIO configuration for TIM peripherals. It contains no data transmission/reception (not RECV), no interrupt handling (not IRQ), no polling loops (not LOOP), and no NVIC/OS/kernel operations (not CORE). It performs initialization operations that configure hardware, making it an INIT function according to the classification criteria.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_TIM_MspPostInit(TIM_HandleTypeDef* htim)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(htim->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspPostInit 0 */

  /* USER CODE END TIM1_MspPostInit 0 */
    /* Skip hardware-specific GPIO clock enable */
    /**TIM1 GPIO Configuration
    PA7     ------> TIM1_CH1N
    PA8     ------> TIM1_CH1
    PA11     ------> TIM1_CH4
    */
    /* Skip GPIO configuration for simulation */
  /* USER CODE BEGIN TIM1_MspPostInit 1 */

  /* USER CODE END TIM1_MspPostInit 1 */
  }
  else if(htim->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspPostInit 0 */

  /* USER CODE END TIM2_MspPostInit 0 */

    /* Skip hardware-specific GPIO clock enable */
    /**TIM2 GPIO Configuration
    PB10     ------> TIM2_CH3
    PB3     ------> TIM2_CH2
    */
    /* Skip GPIO configuration for simulation */
  /* USER CODE BEGIN TIM2_MspPostInit 1 */

  /* USER CODE END TIM2_MspPostInit 1 */
  }
  else if(htim->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspPostInit 0 */

  /* USER CODE END TIM3_MspPostInit 0 */

    /* Skip hardware-specific GPIO clock enables */
    /**TIM3 GPIO Configuration
    PC7     ------> TIM3_CH2
    PB4     ------> TIM3_CH1
    */
    /* Skip GPIO configuration for simulation */
  /* USER CODE BEGIN TIM3_MspPostInit 1 */

  /* USER CODE END TIM3_MspPostInit 1 */
  }
  else if(htim->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspPostInit 0 */

  /* USER CODE END TIM4_MspPostInit 0 */

    /* Skip hardware-specific GPIO clock enable */
    /**TIM4 GPIO Configuration
    PB6     ------> TIM4_CH1
    */
    /* Skip GPIO configuration for simulation */
  /* USER CODE BEGIN TIM4_MspPostInit 1 */

  /* USER CODE END TIM4_MspPostInit 1 */
  }

}
```

=== 信息结束 ===
```

### HAL_UART_DeInit

```text
=== HAL_UART_DeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：669
- 函数内容：HAL_StatusTypeDef HAL_UART_DeInit(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_INSTANCE(huart->Instance));

  huart->gState = HAL_UART_STATE_BUSY;

  /* Disable the Peripheral */
  __HAL_UART_DISABLE(huart);

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
  if (huart->MspDeInitCallback == NULL)
  {
    huart->MspDeInitCallback = HAL_UART_MspDeInit;
  }
  /* DeInit the low level hardware */
  huart->MspDeInitCallback(huart);
#else
  /* DeInit the low level hardware */
  HAL_UART_MspDeInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_RESET;
  huart->RxState = HAL_UART_STATE_RESET;
  huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  /* Process Unlock */
  __HAL_UNLOCK(huart);

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes the UART peripheral by disabling hardware and resetting software state variables
- 是否需要替换：是
- 分类/替换原因：Function performs peripheral deinitialization (inverse of initialization) with hardware register access through __HAL_UART_DISABLE macro and calls low-level hardware deinitialization via HAL_UART_MspDeInit. Contains MMIO operations that need to be removed while preserving structure state resetting, callback mechanism, and unlock operation. GetMMIOFunctionInfo shows no explicit MMIO expressions but the function contains hardware-dependent macros. This is not CORE (no NVIC/OS operations), not RECV (no data transfer), not IRQ (not interrupt handler), not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_UART_DeInit(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  assert_param(IS_UART_INSTANCE(huart->Instance));

  huart->gState = HAL_UART_STATE_BUSY;

  /* Skip hardware peripheral disable */
  /* __HAL_UART_DISABLE(huart); */

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
  if (huart->MspDeInitCallback == NULL)
  {
    huart->MspDeInitCallback = HAL_UART_MspDeInit;
  }
  /* Skip low level hardware deinitialization */
  /* huart->MspDeInitCallback(huart); */
#else
  /* Skip low level hardware deinitialization */
  /* HAL_UART_MspDeInit(huart); */
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_RESET;
  huart->RxState = HAL_UART_STATE_RESET;
  huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  /* Process Unlock */
  __HAL_UNLOCK(huart);

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_UART_IRQHandler

```text
=== HAL_UART_IRQHandler 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：2350
- 函数内容：void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
  uint32_t isrflags   = READ_REG(huart->Instance->SR);
  uint32_t cr1its     = READ_REG(huart->Instance->CR1);
  uint32_t cr3its     = READ_REG(huart->Instance->CR3);
  uint32_t errorflags = 0x00U;
  uint32_t dmarequest = 0x00U;

  /* If no error occurs */
  errorflags = (isrflags & (uint32_t)(USART_SR_PE | USART_SR_FE | USART_SR_ORE | USART_SR_NE));
  if (errorflags == RESET)
  {
    /* UART in mode Receiver -------------------------------------------------*/
    if (((isrflags & USART_SR_RXNE) != RESET) && ((cr1its & USART_CR1_RXNEIE) != RESET))
    {
      UART_Receive_IT(huart);
      return;
    }
  }

  /* If some errors occur */
  if ((errorflags != RESET) && (((cr3its & USART_CR3_EIE) != RESET)
                                || ((cr1its & (USART_CR1_RXNEIE | USART_CR1_PEIE)) != RESET)))
  {
    /* UART parity error interrupt occurred ----------------------------------*/
    if (((isrflags & USART_SR_PE) != RESET) && ((cr1its & USART_CR1_PEIE) != RESET))
    {
      huart->ErrorCode |= HAL_UART_ERROR_PE;
    }

    /* UART noise error interrupt occurred -----------------------------------*/
    if (((isrflags & USART_SR_NE) != RESET) && ((cr3its & USART_CR3_EIE) != RESET))
    {
      huart->ErrorCode |= HAL_UART_ERROR_NE;
    }

    /* UART frame error interrupt occurred -----------------------------------*/
    if (((isrflags & USART_SR_FE) != RESET) && ((cr3its & USART_CR3_EIE) != RESET))
    {
      huart->ErrorCode |= HAL_UART_ERROR_FE;
    }

    /* UART Over-Run interrupt occurred --------------------------------------*/
    if (((isrflags & USART_SR_ORE) != RESET) && (((cr1its & USART_CR1_RXNEIE) != RESET)
                                                 || ((cr3its & USART_CR3_EIE) != RESET)))
    {
      huart->ErrorCode |= HAL_UART_ERROR_ORE;
    }

    /* Call UART Error Call back function if need be --------------------------*/
    if (huart->ErrorCode != HAL_UART_ERROR_NONE)
    {
      /* UART in mode Receiver -----------------------------------------------*/
      if (((isrflags & USART_SR_RXNE) != RESET) && ((cr1its & USART_CR1_RXNEIE) != RESET))
      {
        UART_Receive_IT(huart);
      }

      /* If Overrun error occurs, or if any error occurs in DMA mode reception,
         consider error as blocking */
      dmarequest = HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAR);
      if (((huart->ErrorCode & HAL_UART_ERROR_ORE) != RESET) || dmarequest)
      {
        /* Blocking error : transfer is aborted
           Set the UART state ready to be able to start again the process,
           Disable Rx Interrupts, and disable Rx DMA request, if ongoing */
        UART_EndRxTransfer(huart);

        /* Disable the UART DMA Rx request if enabled */
        if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAR))
        {
          ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAR);

          /* Abort the UART DMA Rx stream */
          if (huart->hdmarx != NULL)
          {
            /* Set the UART DMA Abort callback :
               will lead to call HAL_UART_ErrorCallback() at end of DMA abort procedure */
            huart->hdmarx->XferAbortCallback = UART_DMAAbortOnError;
            if (HAL_DMA_Abort_IT(huart->hdmarx) != HAL_OK)
            {
              /* Call Directly XferAbortCallback function in case of error */
              huart->hdmarx->XferAbortCallback(huart->hdmarx);
            }
          }
          else
          {
            /* Call user error callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
            /*Call registered error callback*/
            huart->ErrorCallback(huart);
#else
            /*Call legacy weak error callback*/
            HAL_UART_ErrorCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
          }
        }
        else
        {
          /* Call user error callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
          /*Call registered error callback*/
          huart->ErrorCallback(huart);
#else
          /*Call legacy weak error callback*/
          HAL_UART_ErrorCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
        }
      }
      else
      {
        /* Non Blocking error : transfer could go on.
           Error is notified to user through user error callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
        /*Call registered error callback*/
        huart->ErrorCallback(huart);
#else
        /*Call legacy weak error callback*/
        HAL_UART_ErrorCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

        huart->ErrorCode = HAL_UART_ERROR_NONE;
      }
    }
    return;
  } /* End if some error occurs */

  /* Check current reception Mode :
     If Reception till IDLE event has been selected : */
  if ((huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
      && ((isrflags & USART_SR_IDLE) != 0U)
      && ((cr1its & USART_SR_IDLE) != 0U))
  {
    __HAL_UART_CLEAR_IDLEFLAG(huart);

    /* Check if DMA mode is enabled in UART */
    if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAR))
    {
      /* DMA mode enabled */
      /* Check received length : If all expected data are received, do nothing,
         (DMA cplt callback will be called).
         Otherwise, if at least one data has already been received, IDLE event is to be notified to user */
      uint16_t nb_remaining_rx_data = (uint16_t) __HAL_DMA_GET_COUNTER(huart->hdmarx);
      if ((nb_remaining_rx_data > 0U)
          && (nb_remaining_rx_data < huart->RxXferSize))
      {
        /* Reception is not complete */
        huart->RxXferCount = nb_remaining_rx_data;

        /* In Normal mode, end DMA xfer and HAL UART Rx process*/
        if (huart->hdmarx->Init.Mode != DMA_CIRCULAR)
        {
          /* Disable PE and ERR (Frame error, noise error, overrun error) interrupts */
          ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_PEIE);
          ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_EIE);

          /* Disable the DMA transfer for the receiver request by resetting the DMAR bit
             in the UART CR3 register */
          ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAR);

          /* At end of Rx process, restore huart->RxState to Ready */
          huart->RxState = HAL_UART_STATE_READY;
          huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

          ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);

          /* Last bytes received, so no need as the abort is immediate */
          (void)HAL_DMA_Abort(huart->hdmarx);
        }

        /* Initialize type of RxEvent that correspond to RxEvent callback execution;
        In this case, Rx Event type is Idle Event */
        huart->RxEventType = HAL_UART_RXEVENT_IDLE;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
        /*Call registered Rx Event callback*/
        huart->RxEventCallback(huart, (huart->RxXferSize - huart->RxXferCount));
#else
        /*Call legacy weak Rx Event callback*/
        HAL_UARTEx_RxEventCallback(huart, (huart->RxXferSize - huart->RxXferCount));
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
      }
      return;
    }
    else
    {
      /* DMA mode not enabled */
      /* Check received length : If all expected data are received, do nothing.
         Otherwise, if at least one data has already been received, IDLE event is to be notified to user */
      uint16_t nb_rx_data = huart->RxXferSize - huart->RxXferCount;
      if ((huart->RxXferCount > 0U)
          && (nb_rx_data > 0U))
      {
        /* Disable the UART Parity Error Interrupt and RXNE interrupts */
        ATOMIC_CLEAR_BIT(huart->Instance->CR1, (USART_CR1_RXNEIE | USART_CR1_PEIE));

        /* Disable the UART Error Interrupt: (Frame error, noise error, overrun error) */
        ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_EIE);

        /* Rx process is completed, restore huart->RxState to Ready */
        huart->RxState = HAL_UART_STATE_READY;
        huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

        ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);

        /* Initialize type of RxEvent that correspond to RxEvent callback execution;
           In this case, Rx Event type is Idle Event */
        huart->RxEventType = HAL_UART_RXEVENT_IDLE;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
        /*Call registered Rx complete callback*/
        huart->RxEventCallback(huart, nb_rx_data);
#else
        /*Call legacy weak Rx Event callback*/
        HAL_UARTEx_RxEventCallback(huart, nb_rx_data);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
      }
      return;
    }
  }

  /* UART in mode Transmitter ------------------------------------------------*/
  if (((isrflags & USART_SR_TXE) != RESET) && ((cr1its & USART_CR1_TXEIE) != RESET))
  {
    UART_Transmit_IT(huart);
    return;
  }

  /* UART in mode Transmitter end --------------------------------------------*/
  if (((isrflags & USART_SR_TC) != RESET) && ((cr1its & USART_CR1_TCIE) != RESET))
  {
    UART_EndTransmit_IT(huart);
    return;
  }
}


【替换更新】
- 更新代码：/**
  * @brief  This function handles UART interrupt request.
  * @param  huart  Pointer to a UART_HandleTypeDef structure that contains
  *                the configuration information for the specified UART module.
  * @retval None
  */
void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
  /* [IRQ REMOVED] Hardware register reads removed for emulation */
  /* In emulation, we don't have real hardware registers to read */
  /* uint32_t isrflags   = READ_REG(huart->Instance->SR); */
  /* uint32_t cr1its     = READ_REG(huart->Instance->CR1); */
  /* uint32_t cr3its     = READ_REG(huart->Instance->CR3); */
  
  /* For emulation, we'll just clear any pending error flags and return */
  /* This prevents the function from getting stuck in hardware-dependent logic */
  
  /* Clear any error flags that might be set */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  
  /* If we're in DMA TX mode, we need to simulate transmission completion */
  /* This is to prevent the system from waiting for hardware events */
  
  /* Simply return without doing any hardware operations */
  /* The actual data transmission is handled by other replacement functions */
}
- 更新原因：Replace HAL_UART_IRQHandler to remove hardware-dependent operations. The original function reads hardware registers (SR, CR1, CR3) and performs complex interrupt handling based on hardware flags. In the emulation environment, these hardware registers don't exist, causing the function to fail or behave unpredictably. This replacement clears any error flags and returns without performing hardware operations, preventing the system from getting stuck in hardware-dependent interrupt handling logic. This is necessary to fix the "exceptional loop" issue where the system gets stuck in idle_thread_entry due to problematic UART interrupt handling.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
  * @brief  This function handles UART interrupt request.
  * @param  huart  Pointer to a UART_HandleTypeDef structure that contains
  *                the configuration information for the specified UART module.
  * @retval None
  */
void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
  /* [IRQ REMOVED] Hardware register reads removed for emulation */
  /* In emulation, we don't have real hardware registers to read */
  /* uint32_t isrflags   = READ_REG(huart->Instance->SR); */
  /* uint32_t cr1its     = READ_REG(huart->Instance->CR1); */
  /* uint32_t cr3its     = READ_REG(huart->Instance->CR3); */
  
  /* For emulation, we'll just clear any pending error flags and return */
  /* This prevents the function from getting stuck in hardware-dependent logic */
  
  /* Clear any error flags that might be set */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  
  /* If we're in DMA TX mode, we need to simulate transmission completion */
  /* This is to prevent the system from waiting for hardware events */
  
  /* Simply return without doing any hardware operations */
  /* The actual data transmission is handled by other replacement functions */
}
    原因：Replace HAL_UART_IRQHandler to remove hardware-dependent operations. The original function reads hardware registers (SR, CR1, CR3) and performs complex interrupt handling based on hardware flags. In the emulation environment, these hardware registers don't exist, causing the function to fail or behave unpredictably. This replacement clears any error flags and returns without performing hardware operations, preventing the system from getting stuck in hardware-dependent interrupt handling logic. This is necessary to fix the "exceptional loop" issue where the system gets stuck in idle_thread_entry due to problematic UART interrupt handling.
    时间：

=== 信息结束 ===
```

### HAL_UART_Init

```text
=== HAL_UART_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：357
- 函数内容：HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  if (huart->Init.HwFlowCtl != UART_HWCONTROL_NONE)
  {
    /* The hardware flow control is available only for USART1, USART2, USART3 and USART6.
       Except for STM32F446xx devices, that is available for USART1, USART2, USART3, USART6, UART4 and UART5.
    */
    assert_param(IS_UART_HWFLOW_INSTANCE(huart->Instance));
    assert_param(IS_UART_HARDWARE_FLOW_CONTROL(huart->Init.HwFlowCtl));
  }
  else
  {
    assert_param(IS_UART_INSTANCE(huart->Instance));
  }
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* Disable the peripheral */
  __HAL_UART_DISABLE(huart);

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* In asynchronous mode, the following bits must be kept cleared:
     - LINEN and CLKEN bits in the USART_CR2 register,
     - SCEN, HDSEL and IREN  bits in the USART_CR3 register.*/
  CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN));
  CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN));

  /* Enable the peripheral */
  __HAL_UART_ENABLE(huart);

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the UART mode according to specified parameters and creates the associated handle
- 是否需要替换：是
- 分类/替换原因：This function performs UART peripheral initialization including hardware register configuration (CR2, CR3 registers), calling low-level hardware initialization (HAL_UART_MspInit), and setting up UART communication parameters. It contains direct hardware register accesses via huart->Instance->CR2 and huart->Instance->CR3, and uses hardware-specific macros like __HAL_UART_DISABLE and __HAL_UART_ENABLE. According to the classification criteria, this is an INIT function because it initializes peripheral configurations and allocates resources. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not interrupt-related), and not LOOP (no polling loops). The replacement preserves parameter validation, state initialization, and callback setup while removing hardware-specific register operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  Initializes the UART mode according to the specified parameters in\n*         the UART_InitTypeDef and create the associated handle.\n* @param  huart  Pointer to a UART_HandleTypeDef structure that contains\n*                the configuration information for the specified UART module.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)\n{\n  /* Check the UART handle allocation */\n  if (huart == NULL)\n  {\n    return HAL_ERROR;\n  }\n\n  /* Check the parameters */\n  if (huart->Init.HwFlowCtl != UART_HWCONTROL_NONE)\n  {\n    /* The hardware flow control is available only for USART1, USART2, USART3 and USART6.\n       Except for STM32F446xx devices, that is available for USART1, USART2, USART3, USART6, UART4 and UART5.\n    */\n    assert_param(IS_UART_HWFLOW_INSTANCE(huart->Instance));\n    assert_param(IS_UART_HARDWARE_FLOW_CONTROL(huart->Init.HwFlowCtl));\n  }\n  else\n  {\n    assert_param(IS_UART_INSTANCE(huart->Instance));\n  }\n  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));\n  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));\n\n  if (huart->gState == HAL_UART_STATE_RESET)\n  {\n    /* Allocate lock resource and initialize it */\n    huart->Lock = HAL_UNLOCKED;\n\n#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)\n    UART_InitCallbacksToDefault(huart);\n\n    if (huart->MspInitCallback == NULL)\n    {\n      huart->MspInitCallback = HAL_UART_MspInit;\n    }\n\n    /* Init the low level hardware */\n    huart->MspInitCallback(huart);\n#else\n    /* Init the low level hardware : GPIO, CLOCK */\n    HAL_UART_MspInit(huart);\n#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */\n  }\n\n  huart->gState = HAL_UART_STATE_BUSY;\n\n  /* Skip hardware-specific peripheral disable */\n  /* __HAL_UART_DISABLE(huart); */\n\n  /* Skip hardware-specific UART configuration */\n  /* UART_SetConfig(huart); */\n\n  /* Skip hardware register clearing operations */\n  /* CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN)); */\n  /* CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN)); */\n\n  /* Skip hardware-specific peripheral enable */\n  /* __HAL_UART_ENABLE(huart); */\n\n  /* Initialize the UART state */\n  huart->ErrorCode = HAL_UART_ERROR_NONE;\n  huart->gState = HAL_UART_STATE_READY;\n  huart->RxState = HAL_UART_STATE_READY;\n  huart->RxEventType = HAL_UART_RXEVENT_TC;\n\n  return HAL_OK;\n}
```

【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  if (huart->Init.HwFlowCtl != UART_HWCONTROL_NONE)
  {
    /* The hardware flow control is available only for USART1, USART2, USART3 and USART6.
       Except for STM32F446xx devices, that is available for USART1, USART2, USART3, USART6, UART4 and UART5.
    */
    assert_param(IS_UART_HWFLOW_INSTANCE(huart->Instance));
    assert_param(IS_UART_HARDWARE_FLOW_CONTROL(huart->Init.HwFlowCtl));
  }
  else
  {
    assert_param(IS_UART_INSTANCE(huart->Instance));
  }
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* [INIT REMOVED] Disable the peripheral - hardware operation removed */
  /* __HAL_UART_DISABLE(huart); */

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* [INIT REMOVED] In asynchronous mode, the following bits must be kept cleared:
     - LINEN and CLKEN bits in the USART_CR2 register,
     - SCEN, HDSEL and IREN  bits in the USART_CR3 register. */
  /* CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN)); */
  /* CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN)); */

  /* [INIT REMOVED] Enable the peripheral - hardware operation removed */
  /* __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
- 更新原因：Create replacement for HAL_UART_Init to remove hardware-dependent operations. The original function contains MMIO register writes to disable/enable UART peripheral and clear configuration bits. These hardware operations are removed while preserving parameter validation, state machine updates, and callback initialization. The function maintains the same state transitions and return values as the original but without accessing hardware registers.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
  /* Check the UART handle allocation */
  if (huart == NULL)
  {
    return HAL_ERROR;
  }

  /* Check the parameters */
  if (huart->Init.HwFlowCtl != UART_HWCONTROL_NONE)
  {
    /* The hardware flow control is available only for USART1, USART2, USART3 and USART6.
       Except for STM32F446xx devices, that is available for USART1, USART2, USART3, USART6, UART4 and UART5.
    */
    assert_param(IS_UART_HWFLOW_INSTANCE(huart->Instance));
    assert_param(IS_UART_HARDWARE_FLOW_CONTROL(huart->Init.HwFlowCtl));
  }
  else
  {
    assert_param(IS_UART_INSTANCE(huart->Instance));
  }
  assert_param(IS_UART_WORD_LENGTH(huart->Init.WordLength));
  assert_param(IS_UART_OVERSAMPLING(huart->Init.OverSampling));

  if (huart->gState == HAL_UART_STATE_RESET)
  {
    /* Allocate lock resource and initialize it */
    huart->Lock = HAL_UNLOCKED;

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    UART_InitCallbacksToDefault(huart);

    if (huart->MspInitCallback == NULL)
    {
      huart->MspInitCallback = HAL_UART_MspInit;
    }

    /* Init the low level hardware */
    huart->MspInitCallback(huart);
#else
    /* Init the low level hardware : GPIO, CLOCK */
    HAL_UART_MspInit(huart);
#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */
  }

  huart->gState = HAL_UART_STATE_BUSY;

  /* [INIT REMOVED] Disable the peripheral - hardware operation removed */
  /* __HAL_UART_DISABLE(huart); */

  /* Set the UART Communication parameters */
  UART_SetConfig(huart);

  /* [INIT REMOVED] In asynchronous mode, the following bits must be kept cleared:
     - LINEN and CLKEN bits in the USART_CR2 register,
     - SCEN, HDSEL and IREN  bits in the USART_CR3 register. */
  /* CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN)); */
  /* CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN)); */

  /* [INIT REMOVED] Enable the peripheral - hardware operation removed */
  /* __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
    原因：Create replacement for HAL_UART_Init to remove hardware-dependent operations. The original function contains MMIO register writes to disable/enable UART peripheral and clear configuration bits. These hardware operations are removed while preserving parameter validation, state machine updates, and callback initialization. The function maintains the same state transitions and return values as the original but without accessing hardware registers.
    时间：

=== 信息结束 ===
```

### HAL_UART_Receive

```text
=== HAL_UART_Receive 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：1221
- 函数内容：HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->RxXferSize = Size;
    huart->RxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pRxData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    /* Check the remain data to be received */
    while (huart->RxXferCount > 0U)
    {
      if (UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_RXNE, RESET, tickstart, Timeout) != HAL_OK)
      {
        huart->RxState = HAL_UART_STATE_READY;

        return HAL_TIMEOUT;
      }
      if (pdata8bits == NULL)
      {
        *pdata16bits = (uint16_t)(huart->Instance->DR & 0x01FF);
        pdata16bits++;
      }
      else
      {
        if ((huart->Init.WordLength == UART_WORDLENGTH_9B) || ((huart->Init.WordLength == UART_WORDLENGTH_8B) && (huart->Init.Parity == UART_PARITY_NONE)))
        {
          *pdata8bits = (uint8_t)(huart->Instance->DR & (uint8_t)0x00FF);
        }
        else
        {
          *pdata8bits = (uint8_t)(huart->Instance->DR & (uint8_t)0x007F);
        }
        pdata8bits++;
      }
      huart->RxXferCount--;
    }

    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->RxXferSize = Size;
    huart->RxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pRxData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    /* [RECV] Remove hardware wait loop and data register reads */
    /* Skip waiting for RXNE flag and reading from DR register */
    /* In emulation, we need to provide data from stdin */
    
    /* Use HAL_BE_In to get data from stdin for emulation */
    if (pdata8bits != NULL)
    {
      HAL_BE_In(pdata8bits, Size);
    }
    else if (pdata16bits != NULL)
    {
      /* For 16-bit data, read as bytes and convert */
      uint8_t temp_buffer[Size * 2];
      HAL_BE_In(temp_buffer, Size * 2);
      /* Convert bytes to 16-bit values (simplified) */
      for (uint16_t i = 0; i < Size; i++)
      {
        pdata16bits[i] = (uint16_t)(temp_buffer[i * 2] | (temp_buffer[i * 2 + 1] << 8));
      }
    }
    
    /* Mark all data as received */
    huart->RxXferCount = 0U;

    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
- 更新原因：Create replacement for HAL_UART_Receive to remove hardware-dependent wait loops and add emulation input handling. The original function contains while loops that wait for UART hardware flags (RXNE) using UART_WaitOnFlagUntilTimeout and reads from the DR register. In emulation, we need to: 1) Remove hardware wait loops, 2) Use HAL_BE_In to get data from stdin instead of reading from hardware registers, 3) Preserve state machine transitions. This replacement allows the application to receive data in emulation without blocking on hardware flags.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->RxXferSize = Size;
    huart->RxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pRxData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    /* [RECV] Remove hardware wait loop and data register reads */
    /* Skip waiting for RXNE flag and reading from DR register */
    /* In emulation, we need to provide data from stdin */
    
    /* Use HAL_BE_In to get data from stdin for emulation */
    if (pdata8bits != NULL)
    {
      HAL_BE_In(pdata8bits, Size);
    }
    else if (pdata16bits != NULL)
    {
      /* For 16-bit data, read as bytes and convert */
      uint8_t temp_buffer[Size * 2];
      HAL_BE_In(temp_buffer, Size * 2);
      /* Convert bytes to 16-bit values (simplified) */
      for (uint16_t i = 0; i < Size; i++)
      {
        pdata16bits[i] = (uint16_t)(temp_buffer[i * 2] | (temp_buffer[i * 2 + 1] << 8));
      }
    }
    
    /* Mark all data as received */
    huart->RxXferCount = 0U;

    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Create replacement for HAL_UART_Receive to remove hardware-dependent wait loops and add emulation input handling. The original function contains while loops that wait for UART hardware flags (RXNE) using UART_WaitOnFlagUntilTimeout and reads from the DR register. In emulation, we need to: 1) Remove hardware wait loops, 2) Use HAL_BE_In to get data from stdin instead of reading from hardware registers, 3) Preserve state machine transitions. This replacement allows the application to receive data in emulation without blocking on hardware flags.
    时间：

=== 信息结束 ===
```

### HAL_UART_Transmit

```text
=== HAL_UART_Transmit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：1135
- 函数内容：HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  const uint8_t  *pdata8bits;
  const uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (const uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    while (huart->TxXferCount > 0U)
    {
      if (UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_TXE, RESET, tickstart, Timeout) != HAL_OK)
      {
        huart->gState = HAL_UART_STATE_READY;

        return HAL_TIMEOUT;
      }
      if (pdata8bits == NULL)
      {
        huart->Instance->DR = (uint16_t)(*pdata16bits & 0x01FFU);
        pdata16bits++;
      }
      else
      {
        huart->Instance->DR = (uint8_t)(*pdata8bits & 0xFFU);
        pdata8bits++;
      }
      huart->TxXferCount--;
    }

    if (UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_TC, RESET, tickstart, Timeout) != HAL_OK)
    {
      huart->gState = HAL_UART_STATE_READY;

      return HAL_TIMEOUT;
    }

    /* At end of Tx process, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  const uint8_t  *pdata8bits;
  const uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (const uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    /* [TRANSMIT] Remove hardware wait loop and data register writes */
    /* Skip waiting for TXE flag and writing to DR register */
    /* Instead, simulate successful transmission by decrementing count */
    huart->TxXferCount = 0U;

    /* [TRANSMIT] Skip waiting for TC flag */
    /* UART_WaitOnFlagUntilTimeout would wait for transmission complete */

    /* At end of Tx process, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
- 更新原因：Create replacement for HAL_UART_Transmit to remove hardware-dependent wait loops. The original function contains while loops that wait for UART hardware flags (TXE and TC) using UART_WaitOnFlagUntilTimeout, which will never complete in emulation. This replacement removes the hardware wait loops and data register writes while preserving the state machine transitions and parameter validation. The function returns success immediately to allow the application to continue without blocking on hardware flags.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  const uint8_t  *pdata8bits;
  const uint16_t *pdata16bits;
  uint32_t tickstart = 0U;

  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    /* In case of 9bits/No Parity transfer, pData needs to be handled as a uint16_t pointer */
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (const uint16_t *) pData;
    }
    else
    {
      pdata8bits  = pData;
      pdata16bits = NULL;
    }

    /* [TRANSMIT] Remove hardware wait loop and data register writes */
    /* Skip waiting for TXE flag and writing to DR register */
    /* Instead, simulate successful transmission by decrementing count */
    huart->TxXferCount = 0U;

    /* [TRANSMIT] Skip waiting for TC flag */
    /* UART_WaitOnFlagUntilTimeout would wait for transmission complete */

    /* At end of Tx process, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Create replacement for HAL_UART_Transmit to remove hardware-dependent wait loops. The original function contains while loops that wait for UART hardware flags (TXE and TC) using UART_WaitOnFlagUntilTimeout, which will never complete in emulation. This replacement removes the hardware wait loops and data register writes while preserving the state machine transitions and parameter validation. The function returns success immediately to allow the application to continue without blocking on hardware flags.
    时间：

=== 信息结束 ===
```

### SystemClock_Config

```text
=== SystemClock_Config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/board.c
- 行号：14
- 函数内容：void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2);
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures the system clock using HSE oscillator and PLL to achieve 200MHz system frequency with appropriate clock dividers for AHB, APB1, and APB2 buses.
- 是否需要替换：是
- 分类/替换原因：This function is a system initialization function that configures clock peripherals. GetMMIOFunctionInfo revealed register accesses for clock control operations. The function initializes clock configuration structures and calls hardware-dependent HAL functions for oscillator and clock configuration. It is called from main() during system startup, making it clearly an INIT type function that needs hardware operations removed while preserving structure initialization and error handling logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  System Clock Configuration
*         The system Clock is configured as follow :
*            System Clock source            = PLL (HSE)
*            SYSCLK(Hz)                     = 200000000
*            HCLK(Hz)                       = 200000000
*            AHB Prescaler                  = 1
*            APB1 Prescaler                 = 4
*            APB2 Prescaler                 = 2
*            HSE Frequency(Hz)              = 25000000
*            PLL_M                          = 25
*            PLL_N                          = 400
*            PLL_P                          = 2
*            PLL_Q                          = 9
*            PLL_R                          = 7
*            VDD(V)                         = 3.3
*            Main regulator output voltage  = Scale1 mode
*            Flash Latency(WS)              = 7
* @param  None
* @retval None
*/
static void SystemClock_Config(void)
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct;
  RCC_OscInitTypeDef RCC_OscInitStruct;
  HAL_StatusTypeDef ret = HAL_OK;
  
  /* [INIT REMOVED] Enable Power Control clock */
  /* __HAL_RCC_PWR_CLK_ENABLE(); */
  
  /* [INIT REMOVED] The voltage scaling allows optimizing the power consumption when the device is 
     clocked below the maximum system frequency, to update the voltage scaling value 
     regarding system frequency refer to product datasheet.  */
  /* __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1); */

  /* Enable HSE Oscillator and activate PLL with HSE as source */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 400;  
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 9;
  RCC_OscInitStruct.PLL.PLLR = 7;  
  
  /* [INIT REMOVED] Hardware oscillator configuration would happen here */
  /* ret = HAL_RCC_OscConfig(&RCC_OscInitStruct); */
  /* Assume successful configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }

  /* [INIT REMOVED] Activate the OverDrive to reach the 200 MHz Frequency */
  /* ret = HAL_PWREx_EnableOverDrive(); */
  /* Assume successful overdrive enable for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }
  
  /* Select PLL as system clock source and configure the HCLK, PCLK1 and PCLK2 clocks dividers */
  RCC_ClkInitStruct.ClockType = (RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2);
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;  
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2; 
  
  /* [INIT REMOVED] Hardware clock configuration would happen here */
  /* ret = HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_7); */
  /* Assume successful clock configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }
}
```

【替换更新】
- 更新代码：/**
* @brief  System Clock Configuration
*         The system Clock is configured as follow :
*            System Clock source            = PLL (HSI)
*            SYSCLK(Hz)                     = 84000000
*            HCLK(Hz)                       = 84000000
*            AHB Prescaler                  = 1
*            APB1 Prescaler                 = 2
*            APB2 Prescaler                 = 1
*            HSI Frequency(Hz)              = 16000000
*            PLL_M                          = 16
*            PLL_N                          = 336
*            PLL_P                          = 4
*            PLL_Q                          = 4
*            VDD(V)                         = 3.3
*            Main regulator output voltage  = Scale2 mode
*            Flash Latency(WS)              = 2
* @param  None
* @retval None
*/
void SystemClock_Config(void)
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  HAL_StatusTypeDef ret = HAL_OK;
  
  /* [INIT REMOVED] Enable Power Control clock */
  /* __HAL_RCC_PWR_CLK_ENABLE(); */
  
  /* [INIT REMOVED] The voltage scaling allows optimizing the power consumption when the device is 
     clocked below the maximum system frequency, to update the voltage scaling value 
     regarding system frequency refer to product datasheet.  */
  /* __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2); */

  /* Enable HSI Oscillator and activate PLL with HSI as source */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  
  /* [INIT REMOVED] Hardware oscillator configuration would happen here */
  /* ret = HAL_RCC_OscConfig(&RCC_OscInitStruct); */
  /* Assume successful configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }

  /* Select PLL as system clock source and configure the HCLK, PCLK1 and PCLK2 clocks dividers */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
  
  /* [INIT REMOVED] Hardware clock configuration would happen here */
  /* ret = HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2); */
  /* Assume successful clock configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }
}
- 更新原因：Fix SystemClock_Config function: 1. Remove 'static' keyword to match declaration in board.h, 2. Use correct PLL structure members for STM32F4 (no PLLR), 3. Use correct clock configuration values from original function (HSI at 84MHz), 4. Initialize structures with {0} to match original

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
* @brief  System Clock Configuration
*         The system Clock is configured as follow :
*            System Clock source            = PLL (HSI)
*            SYSCLK(Hz)                     = 84000000
*            HCLK(Hz)                       = 84000000
*            AHB Prescaler                  = 1
*            APB1 Prescaler                 = 2
*            APB2 Prescaler                 = 1
*            HSI Frequency(Hz)              = 16000000
*            PLL_M                          = 16
*            PLL_N                          = 336
*            PLL_P                          = 4
*            PLL_Q                          = 4
*            VDD(V)                         = 3.3
*            Main regulator output voltage  = Scale2 mode
*            Flash Latency(WS)              = 2
* @param  None
* @retval None
*/
void SystemClock_Config(void)
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  HAL_StatusTypeDef ret = HAL_OK;
  
  /* [INIT REMOVED] Enable Power Control clock */
  /* __HAL_RCC_PWR_CLK_ENABLE(); */
  
  /* [INIT REMOVED] The voltage scaling allows optimizing the power consumption when the device is 
     clocked below the maximum system frequency, to update the voltage scaling value 
     regarding system frequency refer to product datasheet.  */
  /* __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2); */

  /* Enable HSI Oscillator and activate PLL with HSI as source */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 4;
  
  /* [INIT REMOVED] Hardware oscillator configuration would happen here */
  /* ret = HAL_RCC_OscConfig(&RCC_OscInitStruct); */
  /* Assume successful configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }

  /* Select PLL as system clock source and configure the HCLK, PCLK1 and PCLK2 clocks dividers */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
  
  /* [INIT REMOVED] Hardware clock configuration would happen here */
  /* ret = HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2); */
  /* Assume successful clock configuration for simulation */
  ret = HAL_OK;
  
  if(ret != HAL_OK)
  {
    Error_Handler();
  }
}
    原因：Fix SystemClock_Config function: 1. Remove 'static' keyword to match declaration in board.h, 2. Use correct PLL structure members for STM32F4 (no PLLR), 3. Use correct clock configuration values from original function (HSI at 84MHz), 4. Initialize structures with {0} to match original
    时间：

=== 信息结束 ===
```

### SystemCoreClockUpdate

```text
=== SystemCoreClockUpdate 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c
- 行号：220
- 函数内容：void SystemCoreClockUpdate(void)
{
  uint32_t tmp = 0, pllvco = 0, pllp = 2, pllsource = 0, pllm = 2;
  
  /* Get SYSCLK source -------------------------------------------------------*/
  tmp = RCC->CFGR & RCC_CFGR_SWS;

  switch (tmp)
  {
    case 0x00:  /* HSI used as system clock source */
      SystemCoreClock = HSI_VALUE;
      break;
    case 0x04:  /* HSE used as system clock source */
      SystemCoreClock = HSE_VALUE;
      break;
    case 0x08:  /* PLL used as system clock source */

      /* PLL_VCO = (HSE_VALUE or HSI_VALUE / PLL_M) * PLL_N
         SYSCLK = PLL_VCO / PLL_P
         */    
      pllsource = (RCC->PLLCFGR & RCC_PLLCFGR_PLLSRC) >> 22;
      pllm = RCC->PLLCFGR & RCC_PLLCFGR_PLLM;
      
      if (pllsource != 0)
      {
        /* HSE used as PLL clock source */
        pllvco = (HSE_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }
      else
      {
        /* HSI used as PLL clock source */
        pllvco = (HSI_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }

      pllp = (((RCC->PLLCFGR & RCC_PLLCFGR_PLLP) >>16) + 1 ) *2;
      SystemCoreClock = pllvco/pllp;
      break;
    default:
      SystemCoreClock = HSI_VALUE;
      break;
  }
  /* Compute HCLK frequency --------------------------------------------------*/
  /* Get HCLK prescaler */
  tmp = AHBPrescTable[((RCC->CFGR & RCC_CFGR_HPRE) >> 4)];
  /* HCLK frequency */
  SystemCoreClock >>= tmp;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads RCC hardware registers to determine current clock configuration and updates the SystemCoreClock global variable with the current HCLK frequency.
- 是否需要替换：是
- 分类/替换原因：Function performs MMIO reads of RCC->CFGR and RCC->PLLCFGR registers to determine current clock source and configuration. It's called during system initialization by rt_hw_systick_init to establish system clock frequency for SysTick configuration. Classified as INIT because it reads hardware configuration during initialization phase and establishes system state (SystemCoreClock variable). The replacement removes hardware register reads and provides a default system clock frequency (168 MHz typical for STM32F401) for emulation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Update SystemCoreClock variable according to Clock Register Values.
*         The SystemCoreClock variable contains the core clock (HCLK), it can
*         be used by the user application to setup the SysTick timer or configure
*         other parameters.
*
* @note   Each time the core clock (HCLK) changes, this function must be called
*         to update SystemCoreClock variable value. Otherwise, any configuration
*         based on this variable will be incorrect.
*
* @note   - The system frequency computed by this function is not the real
*           frequency in the chip. It is calculated based on the predefined
*           constant and the selected clock source:
*
*           - If SYSCLK source is HSI, SystemCoreClock will contain the HSI_VALUE(*)
*
*           - If SYSCLK source is HSE, SystemCoreClock will contain the HSE_VALUE(**)
*
*           - If SYSCLK source is PLL, SystemCoreClock will contain the HSE_VALUE(**)
*             or HSI_VALUE(*) multiplied/divided by the PLL factors.
*
*         (*) HSI_VALUE is a constant defined in stm32f4xx_hal_conf.h file (default value
*             16 MHz) but the real value may vary depending on the variations
*             in voltage and temperature.
*
*         (**) HSE_VALUE is a constant defined in stm32f4xx_hal_conf.h file (its value
*              depends on the application requirements), user has to ensure that HSE_VALUE
*              is same as the real frequency of the crystal used. Otherwise, this function
*              may have wrong result.
*
*         - The result of this function could be not correct when using fractional
*           value for HSE crystal.
*
* @param  None
* @retval None
*/
void SystemCoreClockUpdate(void)
{
  /* In emulation, assume PLL is used with typical configuration */
  /* Typical configuration for STM32F401: HSE = 8MHz, PLL_M = 8, PLL_N = 336, PLL_P = 2 */
  /* SystemCoreClock = (HSE_VALUE / PLL_M) * PLL_N / PLL_P = (8000000 / 8) * 336 / 2 = 168000000 Hz */
  
  /* Skip hardware register reads and use default value */
  SystemCoreClock = 168000000;
  
  /* Skip HCLK prescaler calculation (assume HPRE = 1, no division) */
  /* SystemCoreClock remains unchanged */
}
```

【替换更新】
- 更新代码：void SystemCoreClockUpdate(void)
{
  uint32_t tmp = 0, pllvco = 0, pllp = 2, pllsource = 0, pllm = 2;
  
  /* Get SYSCLK source -------------------------------------------------------*/
  /* [INIT REMOVED] Hardware register read removed for emulation */
  /* tmp = RCC->CFGR & RCC_CFGR_SWS; */
  
  /* For emulation, assume HSI is used as system clock source */
  tmp = 0x00;  /* HSI used as system clock source */

  switch (tmp)
  {
    case 0x00:  /* HSI used as system clock source */
      SystemCoreClock = HSI_VALUE;
      break;
    case 0x04:  /* HSE used as system clock source */
      SystemCoreClock = HSE_VALUE;
      break;
    case 0x08:  /* PLL used as system clock source */

      /* PLL_VCO = (HSE_VALUE or HSI_VALUE / PLL_M) * PLL_N
         SYSCLK = PLL_VCO / PLL_P
         */    
      /* [INIT REMOVED] Hardware register reads removed for emulation */
      /* pllsource = (RCC->PLLCFGR & RCC_PLLCFGR_PLLSRC) >> 22;
      pllm = RCC->PLLCFGR & RCC_PLLCFGR_PLLM; */
      
      /* For emulation, use default values */
      pllsource = 0;
      pllm = 2;
      
      if (pllsource != 0)
      {
        /* HSE used as PLL clock source */
        pllvco = (HSE_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }
      else
      {
        /* HSI used as PLL clock source */
        pllvco = (HSI_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }

      /* [INIT REMOVED] Hardware register read removed for emulation */
      /* pllp = (((RCC->PLLCFGR & RCC_PLLCFGR_PLLP) >>16) + 1 ) *2; */
      pllp = 2; /* Default value */
      SystemCoreClock = pllvco/pllp;
      break;
    default:
      SystemCoreClock = HSI_VALUE;
      break;
  }
  /* Compute HCLK frequency --------------------------------------------------*/
  /* Get HCLK prescaler */
  /* [INIT REMOVED] Hardware register read removed for emulation */
  /* tmp = AHBPrescTable[((RCC->CFGR & RCC_CFGR_HPRE) >> 4)]; */
  tmp = 0; /* Default: no prescaler */
  
  /* HCLK frequency */
  SystemCoreClock >>= tmp;
}
- 更新原因：SystemCoreClockUpdate contains multiple hardware register reads (RCC->CFGR, RCC->PLLCFGR) to determine system clock configuration. These are MMIO operations that need to be removed for emulation. The function is classified as INIT type since it updates system configuration information. The replacement preserves the calculation structure while removing hardware-specific register reads and using default values for emulation. This prevents emulation issues when the function is called to update the system clock frequency variable.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void SystemCoreClockUpdate(void)
{
  uint32_t tmp = 0, pllvco = 0, pllp = 2, pllsource = 0, pllm = 2;
  
  /* Get SYSCLK source -------------------------------------------------------*/
  /* [INIT REMOVED] Hardware register read removed for emulation */
  /* tmp = RCC->CFGR & RCC_CFGR_SWS; */
  
  /* For emulation, assume HSI is used as system clock source */
  tmp = 0x00;  /* HSI used as system clock source */

  switch (tmp)
  {
    case 0x00:  /* HSI used as system clock source */
      SystemCoreClock = HSI_VALUE;
      break;
    case 0x04:  /* HSE used as system clock source */
      SystemCoreClock = HSE_VALUE;
      break;
    case 0x08:  /* PLL used as system clock source */

      /* PLL_VCO = (HSE_VALUE or HSI_VALUE / PLL_M) * PLL_N
         SYSCLK = PLL_VCO / PLL_P
         */    
      /* [INIT REMOVED] Hardware register reads removed for emulation */
      /* pllsource = (RCC->PLLCFGR & RCC_PLLCFGR_PLLSRC) >> 22;
      pllm = RCC->PLLCFGR & RCC_PLLCFGR_PLLM; */
      
      /* For emulation, use default values */
      pllsource = 0;
      pllm = 2;
      
      if (pllsource != 0)
      {
        /* HSE used as PLL clock source */
        pllvco = (HSE_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }
      else
      {
        /* HSI used as PLL clock source */
        pllvco = (HSI_VALUE / pllm) * ((RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> 6);
      }

      /* [INIT REMOVED] Hardware register read removed for emulation */
      /* pllp = (((RCC->PLLCFGR & RCC_PLLCFGR_PLLP) >>16) + 1 ) *2; */
      pllp = 2; /* Default value */
      SystemCoreClock = pllvco/pllp;
      break;
    default:
      SystemCoreClock = HSI_VALUE;
      break;
  }
  /* Compute HCLK frequency --------------------------------------------------*/
  /* Get HCLK prescaler */
  /* [INIT REMOVED] Hardware register read removed for emulation */
  /* tmp = AHBPrescTable[((RCC->CFGR & RCC_CFGR_HPRE) >> 4)]; */
  tmp = 0; /* Default: no prescaler */
  
  /* HCLK frequency */
  SystemCoreClock >>= tmp;
}
    原因：SystemCoreClockUpdate contains multiple hardware register reads (RCC->CFGR, RCC->PLLCFGR) to determine system clock configuration. These are MMIO operations that need to be removed for emulation. The function is classified as INIT type since it updates system configuration information. The replacement preserves the calculation structure while removing hardware-specific register reads and using default values for emulation. This prevents emulation issues when the function is called to update the system clock frequency variable.
    时间：

=== 信息结束 ===
```

### SystemInit

```text
=== SystemInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c
- 行号：167
- 函数内容：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
  #if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
    SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
  #endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  SystemInit_ExtMemCtl(); 
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* Configure the Vector Table location -------------------------------------*/
#if defined(USER_VECT_TAB_ADDRESS)
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#endif /* USER_VECT_TAB_ADDRESS */
}


【替换更新】
- 更新代码：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
  #if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
    /* CRITICAL: FPU configuration for Cortex-M4 with FPU */
    SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
  #endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* External memory initialization if needed */
  SystemInit_ExtMemCtl(); 
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* CRITICAL: Configure the Vector Table location -------------------------------------*/
  /* VTOR configuration MUST be preserved for RTOS context switching */
  /* In emulation, we must always set VTOR to prevent crashes during context switch */
  /* Even if USER_VECT_TAB_ADDRESS is not defined, set VTOR to a reasonable default */
#if defined(USER_VECT_TAB_ADDRESS)
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#else
  /* Set VTOR to a reasonable default for emulation */
  /* Use typical STM32 vector table address */
  SCB->VTOR = 0x08000000; /* Default flash base address */
#endif /* USER_VECT_TAB_ADDRESS */
}
- 更新原因：Update SystemInit replacement to always set VTOR in emulation. The original code only sets VTOR if USER_VECT_TAB_ADDRESS is defined. In emulation, if VTOR is not set, the vector table remains at address 0x0, which may be unmapped in the emulator, causing crashes during context switch. To ensure reliable emulation, we always set VTOR: if USER_VECT_TAB_ADDRESS is defined, use the configured value; otherwise, use a reasonable default (0x08000000, typical STM32 flash base). This preserves the original conditional behavior while ensuring VTOR is always set for emulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
  #if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
    /* CRITICAL: FPU configuration for Cortex-M4 with FPU */
    SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
  #endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* External memory initialization if needed */
  SystemInit_ExtMemCtl(); 
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* CRITICAL: Configure the Vector Table location -------------------------------------*/
  /* VTOR configuration MUST be preserved for RTOS context switching */
#if defined(USER_VECT_TAB_ADDRESS)
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#endif /* USER_VECT_TAB_ADDRESS */
}
    原因：Create replacement for SystemInit that preserves critical VTOR and FPU configuration. According to critical requirements, VTOR writes must NEVER be removed or stubbed as they are essential for RTOS context switching. The emulator's first context switch reads from the vector table address set by VTOR, and removing this write would cause an unmapped read at 0x0 and crash. Also preserve FPU configuration for Cortex-M4 with FPU support.
    时间：

  版本 2:
    替换代码：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
  #if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
    /* CRITICAL: FPU configuration for Cortex-M4 with FPU */
    SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
  #endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* External memory initialization if needed */
  SystemInit_ExtMemCtl(); 
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* CRITICAL: Configure the Vector Table location -------------------------------------*/
  /* VTOR configuration MUST be preserved for RTOS context switching */
  /* In emulation, we must always set VTOR to prevent crashes during context switch */
  /* Even if USER_VECT_TAB_ADDRESS is not defined, set VTOR to a reasonable default */
#if defined(USER_VECT_TAB_ADDRESS)
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#else
  /* Set VTOR to a reasonable default for emulation */
  /* Use typical STM32 vector table address */
  SCB->VTOR = 0x08000000; /* Default flash base address */
#endif /* USER_VECT_TAB_ADDRESS */
}
    原因：Update SystemInit replacement to always set VTOR in emulation. The original code only sets VTOR if USER_VECT_TAB_ADDRESS is defined. In emulation, if VTOR is not set, the vector table remains at address 0x0, which may be unmapped in the emulator, causing crashes during context switch. To ensure reliable emulation, we always set VTOR: if USER_VECT_TAB_ADDRESS is defined, use the configured value; otherwise, use a reasonable default (0x08000000, typical STM32 flash base). This preserves the original conditional behavior while ensuring VTOR is always set for emulation.
    时间：

=== 信息结束 ===
```

### UART_SetConfig

```text
=== UART_SetConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：3695
- 函数内容：static void UART_SetConfig(UART_HandleTypeDef *huart)
{
  uint32_t tmpreg;
  uint32_t pclk;

  /* Check the parameters */
  assert_param(IS_UART_BAUDRATE(huart->Init.BaudRate));
  assert_param(IS_UART_STOPBITS(huart->Init.StopBits));
  assert_param(IS_UART_PARITY(huart->Init.Parity));
  assert_param(IS_UART_MODE(huart->Init.Mode));

  /*-------------------------- USART CR2 Configuration -----------------------*/
  /* Configure the UART Stop Bits: Set STOP[13:12] bits
     according to huart->Init.StopBits value */
  MODIFY_REG(huart->Instance->CR2, USART_CR2_STOP, huart->Init.StopBits);

  /*-------------------------- USART CR1 Configuration -----------------------*/
  /* Configure the UART Word Length, Parity and mode:
     Set the M bits according to huart->Init.WordLength value
     Set PCE and PS bits according to huart->Init.Parity value
     Set TE and RE bits according to huart->Init.Mode value
     Set OVER8 bit according to huart->Init.OverSampling value */

  tmpreg = (uint32_t)huart->Init.WordLength | huart->Init.Parity | huart->Init.Mode | huart->Init.OverSampling;
  MODIFY_REG(huart->Instance->CR1,
             (uint32_t)(USART_CR1_M | USART_CR1_PCE | USART_CR1_PS | USART_CR1_TE | USART_CR1_RE | USART_CR1_OVER8),
             tmpreg);

  /*-------------------------- USART CR3 Configuration -----------------------*/
  /* Configure the UART HFC: Set CTSE and RTSE bits according to huart->Init.HwFlowCtl value */
  MODIFY_REG(huart->Instance->CR3, (USART_CR3_RTSE | USART_CR3_CTSE), huart->Init.HwFlowCtl);


#if defined(USART6) && defined(UART9) && defined(UART10)
    if ((huart->Instance == USART1) || (huart->Instance == USART6) || (huart->Instance == UART9) || (huart->Instance == UART10))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#elif defined(USART6)
    if ((huart->Instance == USART1) || (huart->Instance == USART6))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#else
    if (huart->Instance == USART1)
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#endif /* USART6 */
    else
    {
      pclk = HAL_RCC_GetPCLK1Freq();
    }
  /*-------------------------- USART BRR Configuration ---------------------*/
  if (huart->Init.OverSampling == UART_OVERSAMPLING_8)
  {
    huart->Instance->BRR = UART_BRR_SAMPLING8(pclk, huart->Init.BaudRate);
  }
  else
  {
    huart->Instance->BRR = UART_BRR_SAMPLING16(pclk, huart->Init.BaudRate);
  }
}


【替换更新】
- 更新代码：static void UART_SetConfig(UART_HandleTypeDef *huart)
{
  uint32_t tmpreg;
  uint32_t pclk;

  /* Check the parameters */
  assert_param(IS_UART_BAUDRATE(huart->Init.BaudRate));
  assert_param(IS_UART_STOPBITS(huart->Init.StopBits));
  assert_param(IS_UART_PARITY(huart->Init.Parity));
  assert_param(IS_UART_MODE(huart->Init.Mode));

  /*-------------------------- USART CR2 Configuration -----------------------*/
  /* [INIT REMOVED] Configure the UART Stop Bits: Set STOP[13:12] bits
     according to huart->Init.StopBits value - hardware operation removed */
  /* MODIFY_REG(huart->Instance->CR2, USART_CR2_STOP, huart->Init.StopBits); */

  /*-------------------------- USART CR1 Configuration -----------------------*/
  /* Configure the UART Word Length, Parity and mode:
     Set the M bits according to huart->Init.WordLength value
     Set PCE and PS bits according to huart->Init.Parity value
     Set TE and RE bits according to huart->Init.Mode value
     Set OVER8 bit according to huart->Init.OverSampling value */

  tmpreg = (uint32_t)huart->Init.WordLength | huart->Init.Parity | huart->Init.Mode | huart->Init.OverSampling;
  
  /* [INIT REMOVED] Hardware register modification removed */
  /* MODIFY_REG(huart->Instance->CR1,
             (uint32_t)(USART_CR1_M | USART_CR1_PCE | USART_CR1_PS | USART_CR1_TE | USART_CR1_RE | USART_CR1_OVER8),
             tmpreg); */

  /*-------------------------- USART CR3 Configuration -----------------------*/
  /* [INIT REMOVED] Configure the UART HFC: Set CTSE and RTSE bits according to huart->Init.HwFlowCtl value - hardware operation removed */
  /* MODIFY_REG(huart->Instance->CR3, (USART_CR3_RTSE | USART_CR3_CTSE), huart->Init.HwFlowCtl); */


#if defined(USART6) && defined(UART9) && defined(UART10)
    if ((huart->Instance == USART1) || (huart->Instance == USART6) || (huart->Instance == UART9) || (huart->Instance == UART10))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#elif defined(USART6)
    if ((huart->Instance == USART1) || (huart->Instance == USART6))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#else
    if (huart->Instance == USART1)
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#endif /* USART6 */
    else
    {
      pclk = HAL_RCC_GetPCLK1Freq();
    }
  /*-------------------------- USART BRR Configuration ---------------------*/
  if (huart->Init.OverSampling == UART_OVERSAMPLING_8)
  {
    /* [INIT REMOVED] Hardware baud rate register write removed */
    /* huart->Instance->BRR = UART_BRR_SAMPLING8(pclk, huart->Init.BaudRate); */
  }
  else
  {
    /* [INIT REMOVED] Hardware baud rate register write removed */
    /* huart->Instance->BRR = UART_BRR_SAMPLING16(pclk, huart->Init.BaudRate); */
  }
}
- 更新原因：Create replacement for UART_SetConfig static function to remove hardware-dependent operations. The original function contains multiple MODIFY_REG macro calls and direct register writes to UART configuration registers (CR1, CR2, CR3, BRR). These hardware operations are removed while preserving parameter validation and baud rate calculation logic. The function maintains the same control flow but without accessing hardware registers.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void UART_SetConfig(UART_HandleTypeDef *huart)
{
  uint32_t tmpreg;
  uint32_t pclk;

  /* Check the parameters */
  assert_param(IS_UART_BAUDRATE(huart->Init.BaudRate));
  assert_param(IS_UART_STOPBITS(huart->Init.StopBits));
  assert_param(IS_UART_PARITY(huart->Init.Parity));
  assert_param(IS_UART_MODE(huart->Init.Mode));

  /*-------------------------- USART CR2 Configuration -----------------------*/
  /* [INIT REMOVED] Configure the UART Stop Bits: Set STOP[13:12] bits
     according to huart->Init.StopBits value - hardware operation removed */
  /* MODIFY_REG(huart->Instance->CR2, USART_CR2_STOP, huart->Init.StopBits); */

  /*-------------------------- USART CR1 Configuration -----------------------*/
  /* Configure the UART Word Length, Parity and mode:
     Set the M bits according to huart->Init.WordLength value
     Set PCE and PS bits according to huart->Init.Parity value
     Set TE and RE bits according to huart->Init.Mode value
     Set OVER8 bit according to huart->Init.OverSampling value */

  tmpreg = (uint32_t)huart->Init.WordLength | huart->Init.Parity | huart->Init.Mode | huart->Init.OverSampling;
  
  /* [INIT REMOVED] Hardware register modification removed */
  /* MODIFY_REG(huart->Instance->CR1,
             (uint32_t)(USART_CR1_M | USART_CR1_PCE | USART_CR1_PS | USART_CR1_TE | USART_CR1_RE | USART_CR1_OVER8),
             tmpreg); */

  /*-------------------------- USART CR3 Configuration -----------------------*/
  /* [INIT REMOVED] Configure the UART HFC: Set CTSE and RTSE bits according to huart->Init.HwFlowCtl value - hardware operation removed */
  /* MODIFY_REG(huart->Instance->CR3, (USART_CR3_RTSE | USART_CR3_CTSE), huart->Init.HwFlowCtl); */


#if defined(USART6) && defined(UART9) && defined(UART10)
    if ((huart->Instance == USART1) || (huart->Instance == USART6) || (huart->Instance == UART9) || (huart->Instance == UART10))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#elif defined(USART6)
    if ((huart->Instance == USART1) || (huart->Instance == USART6))
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#else
    if (huart->Instance == USART1)
    {
      pclk = HAL_RCC_GetPCLK2Freq();
    }
#endif /* USART6 */
    else
    {
      pclk = HAL_RCC_GetPCLK1Freq();
    }
  /*-------------------------- USART BRR Configuration ---------------------*/
  if (huart->Init.OverSampling == UART_OVERSAMPLING_8)
  {
    /* [INIT REMOVED] Hardware baud rate register write removed */
    /* huart->Instance->BRR = UART_BRR_SAMPLING8(pclk, huart->Init.BaudRate); */
  }
  else
  {
    /* [INIT REMOVED] Hardware baud rate register write removed */
    /* huart->Instance->BRR = UART_BRR_SAMPLING16(pclk, huart->Init.BaudRate); */
  }
}
    原因：Create replacement for UART_SetConfig static function to remove hardware-dependent operations. The original function contains multiple MODIFY_REG macro calls and direct register writes to UART configuration registers (CR1, CR2, CR3, BRR). These hardware operations are removed while preserving parameter validation and baud rate calculation logic. The function maintains the same control flow but without accessing hardware registers.
    时间：

=== 信息结束 ===
```

### UART_WaitOnFlagUntilTimeout

```text
=== UART_WaitOnFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：3185
- 函数内容：static HAL_StatusTypeDef UART_WaitOnFlagUntilTimeout(UART_HandleTypeDef *huart, uint32_t Flag, FlagStatus Status,
                                                     uint32_t Tickstart, uint32_t Timeout)
{
  /* Wait until flag is set */
  while ((__HAL_UART_GET_FLAG(huart, Flag) ? SET : RESET) == Status)
  {
    /* Check for the Timeout */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
      {

        return HAL_TIMEOUT;
      }

      if ((READ_BIT(huart->Instance->CR1, USART_CR1_RE) != 0U) && (Flag != UART_FLAG_TXE) && (Flag != UART_FLAG_TC))
      {
        if (__HAL_UART_GET_FLAG(huart, UART_FLAG_ORE) == SET)
        {
          /* Clear Overrun Error flag*/
          __HAL_UART_CLEAR_OREFLAG(huart);

          /* Blocking error : transfer is aborted
          Set the UART state ready to be able to start again the process,
          Disable Rx Interrupts if ongoing */
          UART_EndRxTransfer(huart);

          huart->ErrorCode = HAL_UART_ERROR_ORE;

          /* Process Unlocked */
          __HAL_UNLOCK(huart);

          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【替换更新】
- 更新代码：static HAL_StatusTypeDef UART_WaitOnFlagUntilTimeout(UART_HandleTypeDef *huart, uint32_t Flag, FlagStatus Status,
                                                     uint32_t Tickstart, uint32_t Timeout)
{
  /* [LOOP] Remove hardware-dependent wait loop */
  /* Original code waits for UART hardware flags which will never be set in emulation */
  /* Instead, return success immediately to avoid blocking */
  
  /* Check for timeout if specified */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      return HAL_TIMEOUT;
    }
  }
  
  /* In emulation, assume the flag is already in the desired state */
  /* Skip the while loop that checks __HAL_UART_GET_FLAG */
  
  return HAL_OK;
}
- 更新原因：Create replacement for UART_WaitOnFlagUntilTimeout to remove hardware-dependent wait loop. The original function contains a while loop that waits for UART hardware flags (TXE, TC, etc.) by checking __HAL_UART_GET_FLAG. In emulation, these hardware flags will never be set, causing infinite loops. This replacement removes the hardware wait loop while preserving timeout checking logic. The function returns success immediately to allow the calling functions to continue without blocking on hardware flags.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static HAL_StatusTypeDef UART_WaitOnFlagUntilTimeout(UART_HandleTypeDef *huart, uint32_t Flag, FlagStatus Status,
                                                     uint32_t Tickstart, uint32_t Timeout)
{
  /* [LOOP] Remove hardware-dependent wait loop */
  /* Original code waits for UART hardware flags which will never be set in emulation */
  /* Instead, return success immediately to avoid blocking */
  
  /* Check for timeout if specified */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      return HAL_TIMEOUT;
    }
  }
  
  /* In emulation, assume the flag is already in the desired state */
  /* Skip the while loop that checks __HAL_UART_GET_FLAG */
  
  return HAL_OK;
}
    原因：Create replacement for UART_WaitOnFlagUntilTimeout to remove hardware-dependent wait loop. The original function contains a while loop that waits for UART hardware flags (TXE, TC, etc.) by checking __HAL_UART_GET_FLAG. In emulation, these hardware flags will never be set, causing infinite loops. This replacement removes the hardware wait loop while preserving timeout checking logic. The function returns success immediately to allow the calling functions to continue without blocking on hardware flags.
    时间：

=== 信息结束 ===
```

### rt_hw_pin_init

```text
=== rt_hw_pin_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_gpio.c
- 行号：763
- 函数内容：int rt_hw_pin_init(void)
{
#if defined(__HAL_RCC_GPIOA_CLK_ENABLE)
    __HAL_RCC_GPIOA_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOB_CLK_ENABLE)
    __HAL_RCC_GPIOB_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOC_CLK_ENABLE)
    __HAL_RCC_GPIOC_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOD_CLK_ENABLE)
    __HAL_RCC_GPIOD_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOE_CLK_ENABLE)
    __HAL_RCC_GPIOE_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOF_CLK_ENABLE)
    __HAL_RCC_GPIOF_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOG_CLK_ENABLE)
#ifdef SOC_SERIES_STM32L4
    HAL_PWREx_EnableVddIO2();
#endif
    __HAL_RCC_GPIOG_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOH_CLK_ENABLE)
    __HAL_RCC_GPIOH_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOI_CLK_ENABLE)
    __HAL_RCC_GPIOI_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOJ_CLK_ENABLE)
    __HAL_RCC_GPIOJ_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOK_CLK_ENABLE)
    __HAL_RCC_GPIOK_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOM_CLK_ENABLE)
    __HAL_RCC_GPIOM_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPION_CLK_ENABLE)
    __HAL_RCC_GPION_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOO_CLK_ENABLE)
    __HAL_RCC_GPIOO_CLK_ENABLE();
#endif

#if defined(__HAL_RCC_GPIOP_CLK_ENABLE)
    __HAL_RCC_GPIOP_CLK_ENABLE();
#endif

    return rt_device_pin_register("pin", &_stm32_pin_ops, RT_NULL);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes GPIO hardware by enabling clock for GPIO ports and registers pin device with RT-Thread OS
- 是否需要替换：是
- 分类/替换原因：Function is classified as INIT because: 1) It performs hardware initialization by enabling GPIO peripheral clocks via __HAL_RCC_GPIOx_CLK_ENABLE() macros (MMIO operations), 2) It registers a pin device with the operating system via rt_device_pin_register(), 3) GetMMIOFunctionInfo revealed multiple MMIO expressions related to GPIO clock enable operations, 4) The function is called during board initialization (rt_hw_board_init calls it), 5) It doesn't contain NVIC/OS kernel operations (not CORE), data transmission (not RECV), interrupt handling (not IRQ), or peripheral-dependent loops (not LOOP).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Configure GPIO_InitStructure */
int rt_hw_pin_init(void)
{
    /* Skip hardware-specific GPIO clock enable operations */
    /* Original function had conditional __HAL_RCC_GPIOx_CLK_ENABLE() calls */
    
    return rt_device_pin_register("pin", &_stm32_pin_ops, RT_NULL);
}
```

【替换更新】
- 更新代码：int rt_hw_pin_init(void)
{
#if defined(__HAL_RCC_GPIOA_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOA clock enable removed */
    /* __HAL_RCC_GPIOA_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOB_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOB clock enable removed */
    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOC_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOC clock enable removed */
    /* __HAL_RCC_GPIOC_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOD_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOD clock enable removed */
    /* __HAL_RCC_GPIOD_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOE_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOE clock enable removed */
    /* __HAL_RCC_GPIOE_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOF_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOF clock enable removed */
    /* __HAL_RCC_GPIOF_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOG_CLK_ENABLE)
#ifdef SOC_SERIES_STM32L4
    /* [INIT REMOVED] Hardware power control removed */
    /* HAL_PWREx_EnableVddIO2(); */
#endif
    /* [INIT REMOVED] Hardware GPIOG clock enable removed */
    /* __HAL_RCC_GPIOG_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOH_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOH clock enable removed */
    /* __HAL_RCC_GPIOH_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOI_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOI clock enable removed */
    /* __HAL_RCC_GPIOI_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOJ_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOJ clock enable removed */
    /* __HAL_RCC_GPIOJ_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOK_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOK clock enable removed */
    /* __HAL_RCC_GPIOK_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOM_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOM clock enable removed */
    /* __HAL_RCC_GPIOM_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPION_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPION clock enable removed */
    /* __HAL_RCC_GPION_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOO_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOO clock enable removed */
    /* __HAL_RCC_GPIOO_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOP_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOP clock enable removed */
    /* __HAL_RCC_GPIOP_CLK_ENABLE(); */
#endif

    return rt_device_pin_register("pin", &_stm32_pin_ops, RT_NULL);
}
- 更新原因：Replace rt_hw_pin_init function to remove hardware-specific clock enable operations while preserving RTOS pin device registration. The function contains multiple __HAL_RCC_GPIOx_CLK_ENABLE() calls that access hardware registers. These are removed with [INIT REMOVED] comments. The rt_device_pin_register call is preserved as it's RTOS functionality, not hardware-dependent.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：int rt_hw_pin_init(void)
{
#if defined(__HAL_RCC_GPIOA_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOA clock enable removed */
    /* __HAL_RCC_GPIOA_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOB_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOB clock enable removed */
    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOC_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOC clock enable removed */
    /* __HAL_RCC_GPIOC_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOD_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOD clock enable removed */
    /* __HAL_RCC_GPIOD_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOE_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOE clock enable removed */
    /* __HAL_RCC_GPIOE_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOF_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOF clock enable removed */
    /* __HAL_RCC_GPIOF_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOG_CLK_ENABLE)
#ifdef SOC_SERIES_STM32L4
    /* [INIT REMOVED] Hardware power control removed */
    /* HAL_PWREx_EnableVddIO2(); */
#endif
    /* [INIT REMOVED] Hardware GPIOG clock enable removed */
    /* __HAL_RCC_GPIOG_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOH_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOH clock enable removed */
    /* __HAL_RCC_GPIOH_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOI_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOI clock enable removed */
    /* __HAL_RCC_GPIOI_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOJ_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOJ clock enable removed */
    /* __HAL_RCC_GPIOJ_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOK_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOK clock enable removed */
    /* __HAL_RCC_GPIOK_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOM_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOM clock enable removed */
    /* __HAL_RCC_GPIOM_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPION_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPION clock enable removed */
    /* __HAL_RCC_GPION_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOO_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOO clock enable removed */
    /* __HAL_RCC_GPIOO_CLK_ENABLE(); */
#endif

#if defined(__HAL_RCC_GPIOP_CLK_ENABLE)
    /* [INIT REMOVED] Hardware GPIOP clock enable removed */
    /* __HAL_RCC_GPIOP_CLK_ENABLE(); */
#endif

    return rt_device_pin_register("pin", &_stm32_pin_ops, RT_NULL);
}
    原因：Replace rt_hw_pin_init function to remove hardware-specific clock enable operations while preserving RTOS pin device registration. The function contains multiple __HAL_RCC_GPIOx_CLK_ENABLE() calls that access hardware registers. These are removed with [INIT REMOVED] comments. The rt_device_pin_register call is preserved as it's RTOS functionality, not hardware-dependent.
    时间：

=== 信息结束 ===
```

### stm32_dma_config

```text
=== stm32_dma_config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c
- 行号：1049
- 函数内容：static void stm32_dma_config(struct rt_serial_device *serial, rt_ubase_t flag)
{
    struct rt_serial_rx_fifo *rx_fifo;
    DMA_HandleTypeDef *DMA_Handle;
    struct dma_config *dma_config;
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    RT_ASSERT(flag == RT_DEVICE_FLAG_DMA_TX || flag == RT_DEVICE_FLAG_DMA_RX);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        DMA_Handle = &uart->dma_rx.handle;
        dma_config = uart->config->dma_rx;
    }
    else /* RT_DEVICE_FLAG_DMA_TX == flag */
    {
        DMA_Handle = &uart->dma_tx.handle;
        dma_config = uart->config->dma_tx;
    }
    LOG_D("%s dma config start", uart->config->name);

    {
        rt_uint32_t tmpreg = 0x00U;
#if defined(SOC_SERIES_STM32F1) || defined(SOC_SERIES_STM32F0) || defined(SOC_SERIES_STM32G0) \
    || defined(SOC_SERIES_STM32L0)|| defined(SOC_SERIES_STM32F3) || defined(SOC_SERIES_STM32L1)
        /* enable DMA clock && Delay after an RCC peripheral clock enabling*/
        SET_BIT(RCC->AHBENR, dma_config->dma_rcc);
        tmpreg = READ_BIT(RCC->AHBENR, dma_config->dma_rcc);
#elif defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WL) \
    || defined(SOC_SERIES_STM32G4)|| defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32WB)
        /* enable DMA clock && Delay after an RCC peripheral clock enabling*/
        SET_BIT(RCC->AHB1ENR, dma_config->dma_rcc);
        tmpreg = READ_BIT(RCC->AHB1ENR, dma_config->dma_rcc);
#elif defined(SOC_SERIES_STM32MP1)
        /* enable DMA clock && Delay after an RCC peripheral clock enabling*/
        SET_BIT(RCC->MP_AHB2ENSETR, dma_config->dma_rcc);
        tmpreg = READ_BIT(RCC->MP_AHB2ENSETR, dma_config->dma_rcc);
#endif

#if (defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WL) || defined(SOC_SERIES_STM32G4) || defined(SOC_SERIES_STM32WB)) && defined(DMAMUX1)
        /* enable DMAMUX clock for L4+ and G4 */
        __HAL_RCC_DMAMUX1_CLK_ENABLE();
#elif defined(SOC_SERIES_STM32MP1)
        __HAL_RCC_DMAMUX_CLK_ENABLE();
#endif

        UNUSED(tmpreg);   /* To avoid compiler warnings */
    }

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        __HAL_LINKDMA(&(uart->handle), hdmarx, uart->dma_rx.handle);
    }
    else if (RT_DEVICE_FLAG_DMA_TX == flag)
    {
        __HAL_LINKDMA(&(uart->handle), hdmatx, uart->dma_tx.handle);
    }

#if defined(SOC_SERIES_STM32F1) || defined(SOC_SERIES_STM32F0) || defined(SOC_SERIES_STM32L0)|| defined(SOC_SERIES_STM32F3) || defined(SOC_SERIES_STM32L1) || defined(SOC_SERIES_STM32U5) || defined(SOC_SERIES_STM32H5)
    DMA_Handle->Instance                 = dma_config->Instance;
#elif defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
    DMA_Handle->Instance                 = dma_config->Instance;
    DMA_Handle->Init.Channel             = dma_config->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WL) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32G4) || defined(SOC_SERIES_STM32WB)\
    || defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32MP1)
    DMA_Handle->Instance                 = dma_config->Instance;
    DMA_Handle->Init.Request             = dma_config->request;
#endif
    DMA_Handle->Init.PeriphInc           = DMA_PINC_DISABLE;
    DMA_Handle->Init.MemInc              = DMA_MINC_ENABLE;
    DMA_Handle->Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
    DMA_Handle->Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        DMA_Handle->Init.Direction           = DMA_PERIPH_TO_MEMORY;
        DMA_Handle->Init.Mode                = DMA_CIRCULAR;
    }
    else if (RT_DEVICE_FLAG_DMA_TX == flag)
    {
        DMA_Handle->Init.Direction           = DMA_MEMORY_TO_PERIPH;
        DMA_Handle->Init.Mode                = DMA_NORMAL;
    }

    DMA_Handle->Init.Priority            = DMA_PRIORITY_MEDIUM;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32MP1)
    DMA_Handle->Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
#endif
    if (HAL_DMA_DeInit(DMA_Handle) != HAL_OK)
    {
        RT_ASSERT(0);
    }

    if (HAL_DMA_Init(DMA_Handle) != HAL_OK)
    {
        RT_ASSERT(0);
    }

    /* enable interrupt */
    if (flag == RT_DEVICE_FLAG_DMA_RX)
    {
        rx_fifo = (struct rt_serial_rx_fifo *)serial->serial_rx;
        /* Start DMA transfer */
        if (HAL_UART_Receive_DMA(&(uart->handle), rx_fifo->buffer, serial->config.bufsz) != HAL_OK)
        {
            /* Transfer error in reception process */
            RT_ASSERT(0);
        }
        CLEAR_BIT(uart->handle.Instance->CR3, USART_CR3_EIE);
        __HAL_UART_ENABLE_IT(&(uart->handle), UART_IT_IDLE);
    }

    /* DMA irq should set in DMA TX mode, or HAL_UART_TxCpltCallback function will not be called */
    HAL_NVIC_SetPriority(dma_config->dma_irq, 0, 0);
    HAL_NVIC_EnableIRQ(dma_config->dma_irq);

    HAL_NVIC_SetPriority(uart->config->irq_type, 1, 0);
    HAL_NVIC_EnableIRQ(uart->config->irq_type);

    LOG_D("%s dma %s instance: %x", uart->config->name, flag == RT_DEVICE_FLAG_DMA_RX ? "RX" : "TX", DMA_Handle->Instance);
    LOG_D("%s dma config done", uart->config->name);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures DMA for UART communication in STM32 microcontrollers, setting up DMA for either transmission or reception based on the flag parameter
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization for DMA configuration. Analysis shows: 1) It contains direct MMIO register accesses for clock enabling (RCC->AHBENR, RCC->AHB1ENR, etc.), 2) It configures DMA parameters and structure initialization, 3) It calls NVIC configuration functions (HAL_NVIC_SetPriority, HAL_NVIC_EnableIRQ) which are CORE functions, but according to classification rules, functions that call CORE functions may be classified as INIT as long as the replacement preserves those CORE calls. The function's primary purpose is hardware initialization for DMA-UART communication setup, making INIT the appropriate classification over other types like CORE (not directly NVIC/OS kernel), RECV (not data transfer), or IRQ (not an interrupt handler).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void stm32_dma_config(struct rt_serial_device *serial, rt_ubase_t flag)
{
    struct rt_serial_rx_fifo *rx_fifo;
    DMA_HandleTypeDef *DMA_Handle;
    struct dma_config *dma_config;
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    RT_ASSERT(flag == RT_DEVICE_FLAG_DMA_TX || flag == RT_DEVICE_FLAG_DMA_RX);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        DMA_Handle = &uart->dma_rx.handle;
        dma_config = uart->config->dma_rx;
    }
    else /* RT_DEVICE_FLAG_DMA_TX == flag */
    {
        DMA_Handle = &uart->dma_tx.handle;
        dma_config = uart->config->dma_tx;
    }
    LOG_D("%s dma config start", uart->config->name);

    /* Skip hardware-specific clock enabling operations */
    {
        rt_uint32_t tmpreg = 0x00U;
        UNUSED(tmpreg);   /* To avoid compiler warnings */
    }

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        __HAL_LINKDMA(&(uart->handle), hdmarx, uart->dma_rx.handle);
    }
    else if (RT_DEVICE_FLAG_DMA_TX == flag)
    {
        __HAL_LINKDMA(&(uart->handle), hdmatx, uart->dma_tx.handle);
    }

    /* Preserve DMA handle structure initialization */
#if defined(SOC_SERIES_STM32F1) || defined(SOC_SERIES_STM32F0) || defined(SOC_SERIES_STM32L0)|| defined(SOC_SERIES_STM32F3) || defined(SOC_SERIES_STM32L1) || defined(SOC_SERIES_STM32U5) || defined(SOC_SERIES_STM32H5)
    DMA_Handle->Instance                 = dma_config->Instance;
#elif defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
    DMA_Handle->Instance                 = dma_config->Instance;
    DMA_Handle->Init.Channel             = dma_config->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WL) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32G4) || defined(SOC_SERIES_STM32WB)\
    || defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32MP1)
    DMA_Handle->Instance                 = dma_config->Instance;
    DMA_Handle->Init.Request             = dma_config->request;
#endif
    DMA_Handle->Init.PeriphInc           = DMA_PINC_DISABLE;
    DMA_Handle->Init.MemInc              = DMA_MINC_ENABLE;
    DMA_Handle->Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
    DMA_Handle->Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        DMA_Handle->Init.Direction           = DMA_PERIPH_TO_MEMORY;
        DMA_Handle->Init.Mode                = DMA_CIRCULAR;
    }
    else if (RT_DEVICE_FLAG_DMA_TX == flag)
    {
        DMA_Handle->Init.Direction           = DMA_MEMORY_TO_PERIPH;
        DMA_Handle->Init.Mode                = DMA_NORMAL;
    }

    DMA_Handle->Init.Priority            = DMA_PRIORITY_MEDIUM;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32MP1)
    DMA_Handle->Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
#endif

    /* Skip HAL_DMA_DeInit and HAL_DMA_Init calls as they contain hardware operations */
    /* if (HAL_DMA_DeInit(DMA_Handle) != HAL_OK) */
    /* { */
    /*     RT_ASSERT(0); */
    /* } */
    /* if (HAL_DMA_Init(DMA_Handle) != HAL_OK) */
    /* { */
    /*     RT_ASSERT(0); */
    /* } */

    /* enable interrupt */
    if (flag == RT_DEVICE_FLAG_DMA_RX)
    {
        rx_fifo = (struct rt_serial_rx_fifo *)serial->serial_rx;
        /* Skip HAL_UART_Receive_DMA call as it contains hardware operations */
        /* if (HAL_UART_Receive_DMA(&(uart->handle), rx_fifo->buffer, serial->config.bufsz) != HAL_OK) */
        /* { */
        /*     RT_ASSERT(0); */
        /* } */
        /* Skip UART register operations */
        /* CLEAR_BIT(uart->handle.Instance->CR3, USART_CR3_EIE); */
        /* __HAL_UART_ENABLE_IT(&(uart->handle), UART_IT_IDLE); */
    }

    /* DMA irq should set in DMA TX mode, or HAL_UART_TxCpltCallback function will not be called */
    /* PRESERVE NVIC calls as they are CORE functions */
    HAL_NVIC_SetPriority(dma_config->dma_irq, 0, 0);
    HAL_NVIC_EnableIRQ(dma_config->dma_irq);

    HAL_NVIC_SetPriority(uart->config->irq_type, 1, 0);
    HAL_NVIC_EnableIRQ(uart->config->irq_type);

    LOG_D("%s dma %s instance: %x", uart->config->name, flag == RT_DEVICE_FLAG_DMA_RX ? "RX" : "TX", DMA_Handle->Instance);
    LOG_D("%s dma config done", uart->config->name);
}
```

=== 信息结束 ===
```

### stm32_putc

```text
=== stm32_putc 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c
- 行号：340
- 函数内容：static int stm32_putc(struct rt_serial_device *serial, char c)
{
    struct stm32_uart *uart;
    RT_ASSERT(serial != RT_NULL);

    uart = rt_container_of(serial, struct stm32_uart, serial);
    rt_uint32_t block_timeout = uart->tx_block_timeout;
    UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC);
#if defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WL) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32F0) \
    || defined(SOC_SERIES_STM32L0) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32H7) || defined(SOC_SERIES_STM32L5) \
    || defined(SOC_SERIES_STM32G4) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32F3)  \
    || defined(SOC_SERIES_STM32U5) || defined(SOC_SERIES_STM32H5) || defined(SOC_SERIES_STM32H7RS)
    uart->handle.Instance->TDR = c;
#else
    uart->handle.Instance->DR = c;
#endif
    while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout);
    return (block_timeout != 0) ? 1 : -1;
}


【替换更新】
- 更新代码：static int stm32_putc(struct rt_serial_device *serial, char c)
{
    struct stm32_uart *uart;
    RT_ASSERT(serial != RT_NULL);

    uart = rt_container_of(serial, struct stm32_uart, serial);
    
    /* Declare but don't use block_timeout to avoid unused variable warning */
    /* rt_uint32_t block_timeout = uart->tx_block_timeout; */
    
    /* Skip all hardware operations in emulation */
    /* Original: UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC); */
    /* Original: uart->handle.Instance->DR = c; (or TDR for some series) */
    /* Original: while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout); */
    
    /* Simulate successful transmission */
    return 1;
}
- 更新原因：Update stm32_putc replacement to avoid potential compilation warnings. The original function declares block_timeout variable which is used in the hardware wait loop. In the replacement, we don't use this variable, so we comment it out to avoid unused variable warnings. All hardware operations are removed for emulation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int stm32_putc(struct rt_serial_device *serial, char c)
{
    struct stm32_uart *uart;
    RT_ASSERT(serial != RT_NULL);

    uart = rt_container_of(serial, struct stm32_uart, serial);
    
    /* Skip all hardware operations in emulation */
    /* Original: UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC); */
    /* Original: uart->handle.Instance->DR = c; (or TDR for some series) */
    /* Original: while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout); */
    
    /* Simulate successful transmission */
    return 1;
}
    原因：Fix stm32_putc replacement to completely remove hardware-dependent operations. The previous replacement still attempted to clear UART TC flag using UART_INSTANCE_CLEAR_FUNCTION macro which likely expands to hardware register access. In emulation, we should skip all hardware operations including flag clearing. The function should simply return success to allow console output to proceed without hardware dependencies.
    时间：

  版本 2:
    替换代码：static int stm32_putc(struct rt_serial_device *serial, char c)
{
    struct stm32_uart *uart;
    RT_ASSERT(serial != RT_NULL);

    uart = rt_container_of(serial, struct stm32_uart, serial);
    
    /* Declare but don't use block_timeout to avoid unused variable warning */
    /* rt_uint32_t block_timeout = uart->tx_block_timeout; */
    
    /* Skip all hardware operations in emulation */
    /* Original: UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC); */
    /* Original: uart->handle.Instance->DR = c; (or TDR for some series) */
    /* Original: while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout); */
    
    /* Simulate successful transmission */
    return 1;
}
    原因：Update stm32_putc replacement to avoid potential compilation warnings. The original function declares block_timeout variable which is used in the hardware wait loop. In the replacement, we don't use this variable, so we comment it out to avoid unused variable warnings. All hardware operations are removed for emulation.
    时间：

=== 信息结束 ===
```

### uart_isr

```text
=== uart_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c
- 行号：460
- 函数内容：static void uart_isr(struct rt_serial_device *serial)
{
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    /* UART in mode Receiver -------------------------------------------------*/
    if ((__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_RXNE) != RESET) &&
            (__HAL_UART_GET_IT_SOURCE(&(uart->handle), UART_IT_RXNE) != RESET))
    {
        rt_hw_serial_isr(serial, RT_SERIAL_EVENT_RX_IND);
    }
    else if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) &&
            (__HAL_UART_GET_IT_SOURCE(&(uart->handle), UART_IT_TC) != RESET))
    {
        if ((serial->parent.open_flag & RT_DEVICE_FLAG_DMA_TX) != 0)
        {
            HAL_UART_IRQHandler(&(uart->handle));
        }
        else
        {
            /* Transmission complete interrupt disable ( CR1 Register) */
            __HAL_UART_DISABLE_IT(&(uart->handle), UART_IT_TC);
            rt_hw_serial_isr(serial, RT_SERIAL_EVENT_TX_DONE);
        }
        UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC);
    }
#ifdef RT_SERIAL_USING_DMA
    else if ((uart->uart_dma_flag) && (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_IDLE) != RESET)
             && (__HAL_UART_GET_IT_SOURCE(&(uart->handle), UART_IT_IDLE) != RESET))
    {
        dma_recv_isr(serial, UART_RX_DMA_IT_IDLE_FLAG);
        __HAL_UART_CLEAR_IDLEFLAG(&uart->handle);
    }
#endif
    else
    {
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_ORE) != RESET)
        {
            __HAL_UART_CLEAR_OREFLAG(&uart->handle);
        }
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_NE) != RESET)
        {
            __HAL_UART_CLEAR_NEFLAG(&uart->handle);
        }
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_FE) != RESET)
        {
            __HAL_UART_CLEAR_FEFLAG(&uart->handle);
        }
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_PE) != RESET)
        {
            __HAL_UART_CLEAR_PEFLAG(&uart->handle);
        }
#if !defined(SOC_SERIES_STM32L4) && !defined(SOC_SERIES_STM32WL) && !defined(SOC_SERIES_STM32F7) && !defined(SOC_SERIES_STM32F0) \
    && !defined(SOC_SERIES_STM32L0) && !defined(SOC_SERIES_STM32G0) && !defined(SOC_SERIES_STM32H7) \
    && !defined(SOC_SERIES_STM32G4) && !defined(SOC_SERIES_STM32MP1) && !defined(SOC_SERIES_STM32WB) \
    && !defined(SOC_SERIES_STM32L5) && !defined(SOC_SERIES_STM32U5) && !defined(SOC_SERIES_STM32H5) && !defined(SOC_SERIES_STM32H7RS)
#ifdef SOC_SERIES_STM32F3
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_LBDF) != RESET)
        {
            UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_LBDF);
        }
#else
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_LBD) != RESET)
        {
            UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_LBD);
        }
#endif
#endif
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_CTS) != RESET)
        {
            UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_CTS);
        }
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TXE) != RESET)
        {
            UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TXE);
        }
        if (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_RXNE) != RESET)
        {
            UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_RXNE);
        }
    }
}


【替换更新】
- 更新代码：static void uart_isr(struct rt_serial_device *serial)
{
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    /* [IRQ REMOVED] Hardware flag checks removed for emulation */
    /* In emulation, we don't have real hardware flags to check */
    
    /* For emulation, we'll simulate that we always have data to receive */
    /* This allows the RTOS to continue processing without getting stuck */
    
    /* Simulate RX data available */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_RX_IND);
    
    /* Also simulate TX completion if needed */
    if ((serial->parent.open_flag & RT_DEVICE_FLAG_DMA_TX) != 0)
    {
        /* For DMA TX mode, we need to simulate transmission completion */
        /* Call the IRQ handler (which we've already replaced) */
        HAL_UART_IRQHandler(&(uart->handle));
    }
    else
    {
        /* For non-DMA TX, simulate transmission completion */
        rt_hw_serial_isr(serial, RT_SERIAL_EVENT_TX_DONE);
    }
    
    /* Clear any simulated error flags */
    /* In emulation, we don't have real error flags to clear */
}
- 更新原因：Replace uart_isr to remove hardware-dependent operations. The original function checks hardware flags using __HAL_UART_GET_FLAG macros which read from hardware registers. In the emulation environment, these hardware registers don't exist, causing the function to fail or return unpredictable values. This replacement simulates that data is always available for reception and transmission is always complete, allowing the RTOS to continue processing without getting stuck. This is necessary to fix the "exceptional loop" issue where the system gets stuck in idle_thread_entry due to problematic UART interrupt handling with hardware flag checks.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_isr(struct rt_serial_device *serial)
{
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    /* [IRQ REMOVED] Hardware flag checks removed for emulation */
    /* In emulation, we don't have real hardware flags to check */
    
    /* For emulation, we'll simulate that we always have data to receive */
    /* This allows the RTOS to continue processing without getting stuck */
    
    /* Simulate RX data available */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_RX_IND);
    
    /* Also simulate TX completion if needed */
    if ((serial->parent.open_flag & RT_DEVICE_FLAG_DMA_TX) != 0)
    {
        /* For DMA TX mode, we need to simulate transmission completion */
        /* Call the IRQ handler (which we've already replaced) */
        HAL_UART_IRQHandler(&(uart->handle));
    }
    else
    {
        /* For non-DMA TX, simulate transmission completion */
        rt_hw_serial_isr(serial, RT_SERIAL_EVENT_TX_DONE);
    }
    
    /* Clear any simulated error flags */
    /* In emulation, we don't have real error flags to clear */
}
    原因：Replace uart_isr to remove hardware-dependent operations. The original function checks hardware flags using __HAL_UART_GET_FLAG macros which read from hardware registers. In the emulation environment, these hardware registers don't exist, causing the function to fail or return unpredictable values. This replacement simulates that data is always available for reception and transmission is always complete, allowing the RTOS to continue processing without getting stuck. This is necessary to fix the "exceptional loop" issue where the system gets stuck in idle_thread_entry due to problematic UART interrupt handling with hardware flag checks.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**50** 个；CodeQL `MMIOFunction`：**50** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **20** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `HAL_ADC_MspDeInit` | INIT | True | ADC MSP (Microcontroller Specific Package) de-initialization function that frees hardware resources used by ADC perip... |
| `HAL_ADC_MspInit` | SKIP | False | Weak function for ADC MCU-specific package initialization, meant to be overridden by users for MCU-specific ADC setup. |
| `HAL_DMAEx_MultiBufferStart_IT` | INIT | True | Starts multi-buffer DMA transfer with interrupt capability, configuring DMA hardware for double-buffer mode and enabl... |
| `HAL_DeInit` | INIT | True | De-initializes the HAL common part, resets all peripherals, and calls low-level hardware de-initialization |
| `HAL_GPIO_DeInit` | RETURNOK | False | De-initializes GPIO peripheral registers to their default reset values by clearing configuration for specified GPIO p... |
| `HAL_GPIO_EXTI_IRQHandler` | IRQ | True | Handles EXTI interrupt requests for GPIO pins by checking interrupt flags, clearing them, and invoking callback funct... |
| `HAL_GPIO_Init` | INIT | True | Initializes GPIO pins according to specified configuration parameters including mode, speed, pull-up/down, and altern... |
| `HAL_GPIO_LockPin` | RETURNOK | False | Locks GPIO pin configuration registers to prevent further modification until the next reset |
| `HAL_GPIO_ReadPin` | RETURNOK | False | Reads the state of a specified GPIO pin by accessing the GPIO peripheral's Input Data Register (IDR). |
| `HAL_GPIO_TogglePin` | RETURNOK | False | Toggles specified GPIO pins by reading current output state and writing to BSRR register |
| `HAL_GPIO_WritePin` | RETURNOK | False | Sets or clears a specific GPIO pin by writing to the GPIO BSRR (Bit Set/Reset Register) |
| `HAL_HalfDuplex_Init` | INIT | True | Initializes UART peripheral in half-duplex mode according to specified parameters and creates the associated handle. |
| `HAL_Init` | INIT | True | Initializes the HAL library by configuring flash caches, setting NVIC priority grouping, initializing SysTick timer, ... |
| `HAL_LIN_Init` | INIT | True | Initializes the LIN (Local Interconnect Network) mode for a UART peripheral according to specified parameters includi... |
| `HAL_MultiProcessor_Init` | INIT | True | Initializes UART in multi-processor mode, configuring address nodes and wake-up methods for multi-processor communica... |
| `HAL_PWREx_ControlVoltageScaling` | INIT | True | Configures the main internal regulator output voltage for power-performance tradeoff by setting voltage scaling modes... |
| `HAL_PWREx_DisableBkUpReg` | LOOP | True | Disables the Backup Regulator in the STM32 power control system with timeout handling |
| `HAL_PWREx_EnableBkUpReg` | INIT | True | Enables the Backup Regulator in the STM32 power control system and waits for it to become ready |
| `HAL_PWREx_GetVoltageRange` | RETURNOK | False | Returns the configured voltage scaling range from the power control register (VOS bit field). |
| `HAL_PWR_ConfigPVD` | INIT | True | Configures the Power Voltage Detector (PVD) peripheral with specified voltage threshold and interrupt/event modes |
| `HAL_PWR_DeInit` | RETURNOK | False | Deinitializes the HAL PWR peripheral registers to their default reset values by forcing and releasing reset on the PW... |
| `HAL_PWR_DisableBkUpAccess` | RETURNOK | False | Disables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by clearing the DBP b... |
| `HAL_PWR_DisableWakeUpPin` | RETURNOK | False | Disables the specified wake-up pin functionality in the Power (PWR) peripheral |
| `HAL_PWR_EnableBkUpAccess` | SKIP | False | Enables access to the backup domain (RTC registers, backup data registers, and backup SRAM) by setting the DBP bit in... |
| `HAL_PWR_EnableWakeUpPin` | RETURNOK | False | Enables wake-up pin functionality for power management by setting bits in the PWR control/status register. |
| `HAL_PWR_EnterSTANDBYMode` | CORE | False | Enters STM32 standby mode by configuring power control registers and executing WFI instruction |
| `HAL_PWR_EnterSTOPMode` | INIT | True | Enters the microcontroller into STOP mode (low-power mode) by configuring power regulator settings and executing WFI/... |
| `HAL_PWR_PVD_IRQHandler` | IRQ | True | Interrupt handler for Power Voltage Detector (PVD) interrupt that checks PVD EXTI flag and calls user callback function. |
| `HAL_RCCEx_DisablePLLI2S` | LOOP | True | Disables the PLLI2S peripheral and waits for it to be fully disabled by polling the hardware status register. |
| `HAL_RCCEx_EnablePLLI2S` | INIT | True | Enables and configures the PLLI2S (Phase-Locked Loop for I2S audio interface) with specified clock division factors |
| `HAL_RCCEx_GetPeriphCLKConfig` | INIT | True | Reads peripheral clock configuration from RCC hardware registers (PLLI2S, RTC, TIM prescaler) and populates a configu... |
| `HAL_RCCEx_GetPeriphCLKFreq` | RETURNOK | False | Returns the peripheral clock frequency for a given peripheral (I2S) by reading and calculating from hardware clock co... |
| `HAL_RCCEx_PeriphCLKConfig` | INIT | True | Initializes extended peripheral clocks (I2S, SAI, LTDC, RTC, TIM, UARTs, USARTs, etc.) according to specified configu... |
| `HAL_RCC_ClockConfig` | INIT | True | Initializes CPU, AHB, and APB bus clocks according to specified parameters, configuring system clock sources, divider... |
| `HAL_RCC_GetClockConfig` | RETURNOK | False | Reads the current clock configuration from RCC and Flash registers and populates a structure with the configuration v... |
| `HAL_RCC_GetPCLK1Freq` | RETURNOK | False | Returns the PCLK1 (APB1 peripheral clock) frequency by reading the RCC configuration register and applying the approp... |
| `HAL_RCC_GetPCLK2Freq` | RETURNOK | False | Returns the PCLK2 (APB2 peripheral clock) frequency by reading RCC configuration registers and applying prescaler cal... |
| `HAL_RCC_MCOConfig` | RETURNOK | False | Configures the Microcontroller Clock Output (MCO) pins to output specific clock sources with configurable prescalers |
| `HAL_RCC_NMI_IRQHandler` | IRQ | True | Interrupt handler for RCC Clock Security System (CSS) interrupt request, called under NMI_Handler to handle clock sec... |
| `HAL_SPI_DeInit` | INIT | False | De-initializes the SPI peripheral by disabling the peripheral clock, calling low-level hardware de-initialization, an... |
| `HAL_SPI_Init` | INIT | True | Initializes the SPI peripheral according to specified parameters in the SPI_InitTypeDef structure and initializes the... |
| `HAL_TIM_Base_MspDeInit` | INIT | False | De-initializes hardware resources for TIM (Timer) peripherals by disabling their clock signals |
| `HAL_TIM_Base_MspInit` | SKIP | False | Weak empty implementation of TIM Base MSP initialization meant to be optionally overridden by user for hardware-speci... |
| `HAL_TIM_MspPostInit` | INIT | True | Post-initialization callback function that configures GPIO alternate functions for TIM (Timer) peripheral channels af... |
| `HAL_UART_DeInit` | INIT | True | Deinitializes the UART peripheral by disabling hardware and resetting software state variables |
| `HAL_UART_Init` | INIT | True | Initializes the UART mode according to specified parameters and creates the associated handle |
| `SystemClock_Config` | INIT | True | Configures the system clock using HSE oscillator and PLL to achieve 200MHz system frequency with appropriate clock di... |
| `SystemCoreClockUpdate` | INIT | True | Reads RCC hardware registers to determine current clock configuration and updates the SystemCoreClock global variable... |
| `rt_hw_pin_init` | INIT | True | Initializes GPIO hardware by enabling clock for GPIO ports and registers pin device with RT-Thread OS |
| `stm32_dma_config` | INIT | True | Configures DMA for UART communication in STM32 microcontrollers, setting up DMA for either transmission or reception ... |

## 附录：interesting MMIO expr 子集（共 20 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `HAL_ADC_MspInit`
- `HAL_GPIO_DeInit`
- `HAL_GPIO_Init`
- `HAL_MspInit`
- `HAL_PWREx_ControlVoltageScaling`
- `HAL_PWREx_DisableBkUpReg`
- `HAL_PWREx_EnableBkUpReg`
- `HAL_RCCEx_DisablePLLI2S`
- `HAL_RCCEx_EnablePLLI2S`
- `HAL_RCCEx_PeriphCLKConfig`
- `HAL_RCC_ClockConfig`
- `HAL_RCC_DeInit`
- `HAL_RCC_MCOConfig`
- `HAL_RCC_OscConfig`
- `HAL_SPI_MspInit`
- `HAL_TIM_Base_MspInit`
- `HAL_TIM_MspPostInit`
- `HAL_UART_MspInit`
- `SystemClock_Config`
- `rt_hw_pin_init`
