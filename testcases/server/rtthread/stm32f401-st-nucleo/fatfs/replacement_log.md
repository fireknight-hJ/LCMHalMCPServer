## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/rtthread/stm32f401-st-nucleo/fatfs`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `HAL_ADC_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 108 | 1 |
| `HAL_DMAEx_MultiBufferStart_IT` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_dma_ex.c` | 154 | 1 |
| `HAL_GPIO_EXTI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 492 | 1 |
| `HAL_GPIO_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 164 | 1 |
| `HAL_GPIO_LockPin` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 458 | 1 |
| `HAL_HalfDuplex_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 435 | 1 |
| `HAL_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 157 | 1 |
| `HAL_InitTick` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 253 | 1 |
| `HAL_LIN_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 509 | 1 |
| `HAL_MultiProcessor_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 591 | 1 |
| `HAL_NVIC_EnableIRQ` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 185 | 1 |
| `HAL_NVIC_SetPriority` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 163 | 1 |
| `HAL_NVIC_SetPriorityGrouping` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_cortex.c` | 141 | 1 |
| `HAL_PWREx_ControlVoltageScaling` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 288 | 1 |
| `HAL_PWREx_DisableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 165 | 1 |
| `HAL_PWREx_EnableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 141 | 1 |
| `HAL_PWR_ConfigPVD` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 275 | 1 |
| `HAL_PWR_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 90 | 1 |
| `HAL_PWR_EnableBkUpAccess` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 108 | 1 |
| `HAL_PWR_EnterSTANDBYMode` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 488 | 1 |
| `HAL_PWR_EnterSTOPMode` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 445 | 1 |
| `HAL_PWR_PVD_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 509 | 1 |
| `HAL_RCCEx_DisablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2929 | 1 |
| `HAL_RCCEx_EnablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2846 | 1 |
| `HAL_RCCEx_PeriphCLKConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2551 | 1 |
| `HAL_RCC_ClockConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 591 | 2 |
| `HAL_RCC_GetSysClockFreq` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 885 | 1 |
| `HAL_RCC_MCOConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 775 | 1 |
| `HAL_RCC_NMI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 1084 | 1 |
| `HAL_SPI_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c` | 437 | 1 |
| `HAL_SPI_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c` | 311 | 1 |
| `HAL_TIM_Base_MspDeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 439 | 1 |
| `HAL_TIM_Base_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 262 | 1 |
| `HAL_TIM_MspPostInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 333 | 1 |
| `HAL_UART_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 669 | 1 |
| `HAL_UART_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 357 | 1 |
| `SystemClock_Config` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/board.c` | 14 | 1 |
| `SystemCoreClockUpdate` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c` | 220 | 1 |
| `SystemInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c` | 167 | 2 |
| `__NVIC_EnableIRQ` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h` | 1725 | 1 |
| `__NVIC_SetPriority` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h` | 1855 | 1 |
| `__NVIC_SetPriorityGrouping` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h` | 1694 | 1 |
| `rt_hw_spi_bus_init` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_spi.c` | 548 | 1 |
| `rt_hw_systick_init` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drv_common.c` | 43 | 2 |
| `stm32_dma_config` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c` | 1049 | 1 |
| `stm32_putc` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_usart.c` | 340 | 1 |

## 2. 各函数替换详情

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
- 函数类型：INIT
- 函数用途/功能描述：ADC MSP (Microcontroller Specific Package) initialization function that configures hardware resources for ADC peripheral, including enabling clocks and configuring GPIO pins for analog mode.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is an ADC MSP initialization function that configures hardware resources. GetMMIOFunctionInfo showed it contains clock enable operations (__HAL_RCC_*_CLK_ENABLE) and GPIO initialization calls (HAL_GPIO_Init). The function performs pure hardware initialization with no data transfer, interrupt handling, or OS operations. It does not contain any NVIC configuration, OS kernel operations, or VTOR setup, so it is not CORE. According to the classification priority, INIT functions handle peripheral initialization and configuration. The replacement removes all hardware-specific MMIO operations while preserving the structure initialization and conditional logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief ADC MSP Initialization
* This function configures the hardware resources used in this example
* @param hadc: ADC handle pointer
* @retval None
*/
void HAL_ADC_MspInit(ADC_HandleTypeDef* hadc)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspInit 0 */

  /* USER CODE END ADC1_MspInit 0 */
    /* Peripheral clock enable - removed hardware-specific operation */
    // __HAL_RCC_ADC1_CLK_ENABLE();

    // __HAL_RCC_GPIOC_CLK_ENABLE();
    // __HAL_RCC_GPIOA_CLK_ENABLE();
    // __HAL_RCC_GPIOB_CLK_ENABLE();
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
    // HAL_GPIO_Init(GPIOC, &GPIO_InitStruct); /* Hardware operation removed */

    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    // HAL_GPIO_Init(GPIOA, &GPIO_InitStruct); /* Hardware operation removed */

    GPIO_InitStruct.Pin = GPIO_PIN_0;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    // HAL_GPIO_Init(GPIOB, &GPIO_InitStruct); /* Hardware operation removed */

  /* USER CODE BEGIN ADC1_MspInit 1 */

  /* USER CODE END ADC1_MspInit 1 */
  }

}
```

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
- 函数用途/功能描述：Starts multi-buffer DMA transfer with interrupt enabled, configuring DMA for double buffering mode and enabling interrupts
- 是否需要替换：是
- 分类/替换原因：This function initializes and configures the DMA peripheral for multi-buffer transfers with interrupts. It contains multiple hardware register accesses (enabling double buffer mode, setting memory addresses, clearing flags, enabling interrupts, and enabling the DMA peripheral) which are characteristic of initialization functions. The function performs parameter validation, state management, and callback checks but the core purpose is hardware configuration. According to the classification priority, it fits the INIT category as it sets up peripheral configurations without being a CORE (NVIC/OS/VTOR), RECV (data I/O), IRQ (interrupt handler), or LOOP (polling) function.
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
    
    /* Skip hardware-specific configuration for double buffer mode */
    /* hdma->Instance->CR |= (uint32_t)DMA_SxCR_DBM; */
    
    /* Skip hardware-specific configuration for second memory address */
    /* hdma->Instance->M1AR = SecondMemAddress; */
    
    /* Skip hardware-specific configuration call */
    /* DMA_MultiBufferSetConfig(hdma, SrcAddress, DstAddress, DataLength); */
    
    /* Skip clearing hardware flags */
    /* __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_TC_FLAG_INDEX(hdma)); */
    /* __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_HT_FLAG_INDEX(hdma)); */
    /* __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_TE_FLAG_INDEX(hdma)); */
    /* __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_DME_FLAG_INDEX(hdma)); */
    /* __HAL_DMA_CLEAR_FLAG (hdma, __HAL_DMA_GET_FE_FLAG_INDEX(hdma)); */

    /* Skip enabling hardware interrupts */
    /* hdma->Instance->CR  |= DMA_IT_TC | DMA_IT_TE | DMA_IT_DME; */
    /* hdma->Instance->FCR |= DMA_IT_FE; */
    
    /* Skip enabling half transfer interrupt based on callbacks */
    /* if((hdma->XferHalfCpltCallback != NULL) || (hdma->XferM1HalfCpltCallback != NULL)) */
    /* { */
    /*   hdma->Instance->CR  |= DMA_IT_HT; */
    /* } */
    
    /* Skip enabling the peripheral */
    /* __HAL_DMA_ENABLE(hdma); */
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
- 函数用途/功能描述：Handles GPIO external interrupt requests by checking interrupt flags, clearing them, and invoking callback functions
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler that processes GPIO EXTI (External Interrupt) events. Analysis shows: 1) It contains interrupt flag checking via __HAL_GPIO_EXTI_GET_IT macro, 2) It clears interrupt flags via __HAL_GPIO_EXTI_CLEAR_IT macro, 3) It calls callback function HAL_GPIO_EXTI_Callback, 4) It is called from various EXTI IRQ handlers (EXTI0_IRQHandler, EXTI1_IRQHandler, etc.). According to classification criteria, this matches IRQ (Interrupt-Related Functions) which handles interrupt flag checks and clears hardware operations. The replacement removes hardware-specific interrupt flag operations while preserving the callback invocation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function handles EXTI interrupt request.
* @param  GPIO_Pin Specifies the pins connected EXTI line
* @retval None
*/
void HAL_GPIO_EXTI_IRQHandler(uint16_t GPIO_Pin)
{
  /* Simulate EXTI line interrupt detected - always call callback */
  HAL_GPIO_EXTI_Callback(GPIO_Pin);
}
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
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs extensive MMIO operations to configure GPIO registers (OSPEEDR, OTYPER, PUPDR, AFR, MODER, and EXTI registers). 2) It is called from various MspInit functions and driver initialization code. 3) It contains parameter validation and configuration logic but no data transmission/reception. 4) It is not a CORE function (no NVIC/OS/VTOR operations). 5) It follows the INIT pattern: hardware initialization with register writes that should be removed while preserving parameter validation and control flow. The replacement removes all hardware register accesses while keeping the parameter checks and loop structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
{
  uint32_t position;
  uint32_t ioposition = 0x00U;
  uint32_t iocurrent = 0x00U;

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
        /* Hardware configuration removed for simulation */
      }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        /* Hardware configuration removed for simulation */
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Hardware configuration removed for simulation */
      }

      /* Hardware configuration removed for simulation */
      /* Configure IO Direction mode (Input, Output, Alternate or Analog) */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Hardware configuration removed for simulation */
        /* Note: EXTI configuration would normally enable interrupts */
        /* but hardware register writes are removed for simulation */
      }
    }
  }
}
```

=== 信息结束 ===
```

### HAL_GPIO_LockPin

```text
=== HAL_GPIO_LockPin 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c
- 行号：458
- 函数内容：HAL_StatusTypeDef HAL_GPIO_LockPin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin)
{
  __IO uint32_t tmp = GPIO_LCKR_LCKK;

  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));

  /* Apply lock key write sequence */
  tmp |= GPIO_Pin;
  /* Set LCKx bit(s): LCKK='1' + LCK[15-0] */
  GPIOx->LCKR = tmp;
  /* Reset LCKx bit(s): LCKK='0' + LCK[15-0] */
  GPIOx->LCKR = GPIO_Pin;
  /* Set LCKx bit(s): LCKK='1' + LCK[15-0] */
  GPIOx->LCKR = tmp;
  /* Read LCKR register. This read is mandatory to complete key lock sequence */
  tmp = GPIOx->LCKR;

  /* Read again in order to confirm lock is active */
 if((GPIOx->LCKR & GPIO_LCKR_LCKK) != RESET)
  {
    return HAL_OK;
  }
  else
  {
    return HAL_ERROR;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Locks GPIO pin configuration registers to prevent modification until next reset
- 是否需要替换：是
- 分类/替换原因：Function performs GPIO peripheral configuration by writing a specific sequence to the LCKR (lock) register and reading back to verify lock status. Contains direct hardware register accesses (GPIOx->LCKR writes and reads) for locking GPIO pin configurations. Fits INIT classification as it initializes/performs configuration of peripheral hardware state. Not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not interrupt handler), not LOOP (no peripheral-dependent polling loops), not RETURNOK/SKIP (has hardware dependencies that need replacement), not NODRIVER (clearly has hardware register accesses).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Locks GPIO Pins configuration registers.
* @note   The locked registers are GPIOx_MODER, GPIOx_OTYPER, GPIOx_OSPEEDR,
*         GPIOx_PUPDR, GPIOx_AFRL and GPIOx_AFRH.
* @note   The configuration of the locked GPIO pins can no longer be modified
*         until the next reset.
* @param  GPIOx where x can be (A..F) to select the GPIO peripheral for STM32F4 family
* @param  GPIO_Pin specifies the port bit to be locked.
*         This parameter can be any combination of GPIO_PIN_x where x can be (0..15).
* @retval None
*/
HAL_StatusTypeDef HAL_GPIO_LockPin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));

  /* Skip hardware lock sequence in simulation */
  /* Original: Apply lock key write sequence and verify */
  
  /* Simulate successful lock */
  return HAL_OK;
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
- 函数用途/功能描述：Initializes UART in half-duplex mode according to specified parameters in UART_InitTypeDef structure
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization function that configures UART registers for half-duplex operation. Analysis shows: 1) It contains direct hardware register accesses (CR2, CR3 register manipulation via CLEAR_BIT/SET_BIT macros), 2) It calls other hardware initialization functions (HAL_UART_MspInit, UART_SetConfig), 3) It updates software state variables after hardware configuration, 4) It performs parameter validation and state checking, 5) It does not perform data transmission/reception (not RECV), is not an interrupt handler (not IRQ), contains no peripheral-dependent loops (not LOOP), and is not a CORE function (no NVIC/OS kernel/VTOR operations). GetMMIOFunctionInfo showed empty results but source code clearly contains hardware register accesses. According to classification priority, INIT is the correct classification.
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

  /* Skip hardware-specific configuration for half-duplex mode */
  /* Original hardware operations removed:
     - __HAL_UART_DISABLE(huart);
     - UART_SetConfig(huart);
     - CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN));
     - CLEAR_BIT(huart->Instance->CR3, (USART_CR3_IREN | USART_CR3_SCEN));
     - SET_BIT(huart->Instance->CR3, USART_CR3_HDSEL);
     - __HAL_UART_ENABLE(huart);
  */

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
- 函数用途/功能描述：Initializes the HAL library by configuring Flash cache/prefetch, setting NVIC priority grouping, initializing SysTick timer, and calling low-level hardware initialization.
- 是否需要替换：是
- 分类/替换原因：HAL_Init is a system initialization function that performs multiple initialization tasks: 1) Configures Flash prefetch, instruction cache, and data cache through macro calls; 2) Calls HAL_NVIC_SetPriorityGrouping to set NVIC priority grouping (CORE operation); 3) Calls HAL_InitTick to configure SysTick timer; 4) Calls HAL_MspInit for low-level hardware initialization. While it calls CORE functions (HAL_NVIC_SetPriorityGrouping), it is not itself a CORE function but an initialization wrapper. According to classification rules, functions that call CORE functions may be classified as INIT, and the replacement must preserve calls to NVIC/OS/VTOR primitives. This function fits the INIT category as it initializes system components and configurations. The replacement removes hardware-specific Flash cache/prefetch configuration macros but preserves the calls to NVIC configuration and SysTick initialization functions.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function is used to initialize the HAL Library; it must be the first
*         instruction to be executed in the main program (before to call any other
*         HAL function), it performs the following:
*           Configure the Flash prefetch, instruction and Data caches.
*           Configures the SysTick to generate an interrupt each 1 millisecond,
*           which is clocked by the HSI (at this stage, the clock is not yet
*           configured and thus the system is running from the internal HSI at 16 MHz).
*           Set NVIC Group Priority to 4.
*           Calls the HAL_MspInit() callback function defined in user file
*           "stm32f4xx_hal_msp.c" to do the global low level hardware initialization
*
* @note   SysTick is used as time base for the HAL_Delay() function, the application
*         need to ensure that the SysTick time base is always set to 1 millisecond
*         to have correct HAL operation.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_Init(void)
{
  /* Set Interrupt Group Priority - preserve CORE operation */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
```

【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_Init(void)
{
  /* Configure Flash prefetch, Instruction cache, Data cache */ 
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache configuration in simulation */
  /* __HAL_FLASH_INSTRUCTION_CACHE_ENABLE(); */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache configuration in simulation */
  /* __HAL_FLASH_DATA_CACHE_ENABLE(); */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* Skip hardware-specific prefetch configuration in simulation */
  /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
#endif /* PREFETCH_ENABLE */

  /* Set Interrupt Group Priority - CRITICAL: Must preserve NVIC configuration */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  /* CRITICAL: Must preserve SysTick configuration for OS scheduler */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
- 更新原因：HAL_Init is the main HAL initialization function that calls critical OS functions. According to CRITICAL requirements, we must preserve NVIC and SysTick configuration. This replacement: 1) Skips hardware-specific cache/prefetch configuration (not needed in simulation), 2) Preserves HAL_NVIC_SetPriorityGrouping call (critical for interrupt handling), 3) Preserves HAL_InitTick call (critical for SysTick configuration), 4) Calls HAL_MspInit (already has replacement). The function signature and return type are preserved from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_Init(void)
{
  /* Configure Flash prefetch, Instruction cache, Data cache */ 
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache configuration in simulation */
  /* __HAL_FLASH_INSTRUCTION_CACHE_ENABLE(); */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache configuration in simulation */
  /* __HAL_FLASH_DATA_CACHE_ENABLE(); */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* Skip hardware-specific prefetch configuration in simulation */
  /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
#endif /* PREFETCH_ENABLE */

  /* Set Interrupt Group Priority - CRITICAL: Must preserve NVIC configuration */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  /* CRITICAL: Must preserve SysTick configuration for OS scheduler */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
    原因：HAL_Init is the main HAL initialization function that calls critical OS functions. According to CRITICAL requirements, we must preserve NVIC and SysTick configuration. This replacement: 1) Skips hardware-specific cache/prefetch configuration (not needed in simulation), 2) Preserves HAL_NVIC_SetPriorityGrouping call (critical for interrupt handling), 3) Preserves HAL_InitTick call (critical for SysTick configuration), 4) Calls HAL_MspInit (already has replacement). The function signature and return type are preserved from the original.
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
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  /* CRITICAL: Must preserve SysTick configuration for OS scheduler */
  uint32_t ticks = SystemCoreClock / (1000U / uwTickFreq);
  
  if ((ticks - 1UL) > SysTick_LOAD_RELOAD_Msk)
  {
    return HAL_ERROR;
  }

  /* Preserve SysTick register writes - emulator will intercept these */
  SysTick->LOAD  = (uint32_t)(ticks - 1UL);                         /* set reload register */
  
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

  SysTick->VAL   = 0UL;                                             /* Load the SysTick Counter Value */
  SysTick->CTRL  = SysTick_CTRL_CLKSOURCE_Msk |
                   SysTick_CTRL_TICKINT_Msk   |
                   SysTick_CTRL_ENABLE_Msk;                         /* Enable SysTick IRQ and SysTick Timer */

  /* Return function status */
  return HAL_OK;
}
- 更新原因：HAL_InitTick is critical for OS scheduler operation as it configures the SysTick timer. According to CRITICAL requirements, we must NOT stub or remove SysTick configuration. This replacement preserves all SysTick register writes (LOAD, VAL, CTRL) so the emulator can intercept them and enable timer interrupts. It also preserves the NVIC priority configuration. The function signature and weak attribute are maintained from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__weak HAL_StatusTypeDef HAL_InitTick(uint32_t TickPriority)
{
  /* Configure the SysTick to have interrupt in 1ms time basis*/
  /* CRITICAL: Must preserve SysTick configuration for OS scheduler */
  uint32_t ticks = SystemCoreClock / (1000U / uwTickFreq);
  
  if ((ticks - 1UL) > SysTick_LOAD_RELOAD_Msk)
  {
    return HAL_ERROR;
  }

  /* Preserve SysTick register writes - emulator will intercept these */
  SysTick->LOAD  = (uint32_t)(ticks - 1UL);                         /* set reload register */
  
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

  SysTick->VAL   = 0UL;                                             /* Load the SysTick Counter Value */
  SysTick->CTRL  = SysTick_CTRL_CLKSOURCE_Msk |
                   SysTick_CTRL_TICKINT_Msk   |
                   SysTick_CTRL_ENABLE_Msk;                         /* Enable SysTick IRQ and SysTick Timer */

  /* Return function status */
  return HAL_OK;
}
    原因：HAL_InitTick is critical for OS scheduler operation as it configures the SysTick timer. According to CRITICAL requirements, we must NOT stub or remove SysTick configuration. This replacement preserves all SysTick register writes (LOAD, VAL, CTRL) so the emulator can intercept them and enable timer interrupts. It also preserves the NVIC priority configuration. The function signature and weak attribute are maintained from the original.
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
- 分类/替换原因：Function performs hardware initialization with direct MMIO register accesses (CR2, CR3 registers) to configure LIN mode. It calls HAL_UART_MspInit which may contain NVIC configuration (CORE operations). Contains parameter validation, state management, and hardware configuration operations. Fits INIT category: 'Functions that initialize peripheral/configurations or allocate resources'. Not CORE (doesn't directly configure NVIC), not RECV/IRQ/LOOP.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the LIN mode according to the specified
*         parameters in the UART_InitTypeDef and create the associated handle.
* @param  huart  Pointer to a UART_HandleTypeDef structure that contains
*                the configuration information for the specified UART module.
* @param  BreakDetectLength Specifies the LIN break detection length.
*         This parameter can be one of the following values:
*            @arg UART_LINBREAKDETECTLENGTH_10B: 10-bit break detection
*            @arg UART_LINBREAKDETECTLENGTH_11B: 11-bit break detection
* @retval HAL status
*/
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

  /* Skip hardware-specific configuration for LIN mode */
  /* Original hardware operations removed:
     - __HAL_UART_DISABLE(huart);
     - UART_SetConfig(huart);
     - CLEAR_BIT(huart->Instance->CR2, (USART_CR2_CLKEN));
     - CLEAR_BIT(huart->Instance->CR3, (USART_CR3_HDSEL | USART_CR3_IREN | USART_CR3_SCEN));
     - SET_BIT(huart->Instance->CR2, USART_CR2_LINEN);
     - CLEAR_BIT(huart->Instance->CR2, USART_CR2_LBDL);
     - SET_BIT(huart->Instance->CR2, BreakDetectLength);
     - __HAL_UART_ENABLE(huart);
  */

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
- 函数用途/功能描述：Initializes UART in Multi-Processor mode with specified address and wake-up method
- 是否需要替换：是
- 分类/替换原因：This function is a peripheral initialization function that configures UART hardware registers for multi-processor mode. GetFunctionInfo shows direct hardware register accesses (CR1, CR2, CR3 registers via CLEAR_BIT/SET_BIT macros), peripheral enable/disable operations, and calls to hardware configuration functions (UART_SetConfig, HAL_UART_MspInit). GetMMIOFunctionInfo confirms hardware dependencies. Following the INIT classification strategy, we preserve structure initialization and state management while removing hardware-specific register operations.
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

  /* Skip hardware-specific configuration */
  /* Original: Disable the peripheral - __HAL_UART_DISABLE(huart); */
  /* Original: Set the UART Communication parameters - UART_SetConfig(huart); */
  /* Original: Clear and set CR2/CR3 registers for Multi-Processor mode */
  /* Original: Set USART address node in CR2 register */
  /* Original: Set wake up method in CR1 register */
  /* Original: Enable the peripheral - __HAL_UART_ENABLE(huart); */

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
  
  /* CRITICAL: Must preserve interrupt enable configuration */
  /* Enable interrupt - preserve the NVIC enable call */
  NVIC_EnableIRQ(IRQn);
}
- 更新原因：HAL_NVIC_EnableIRQ is a critical function that enables interrupts. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the NVIC_EnableIRQ call (which likely calls __NVIC_EnableIRQ) so the emulator can intercept the hardware writes and properly enable interrupts. The function signature is maintained from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* Check the parameters */
  assert_param(IS_NVIC_DEVICE_IRQ(IRQn));
  
  /* CRITICAL: Must preserve interrupt enable configuration */
  /* Enable interrupt - preserve the NVIC enable call */
  NVIC_EnableIRQ(IRQn);
}
    原因：HAL_NVIC_EnableIRQ is a critical function that enables interrupts. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the NVIC_EnableIRQ call (which likely calls __NVIC_EnableIRQ) so the emulator can intercept the hardware writes and properly enable interrupts. The function signature is maintained from the original.
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
  
  /* CRITICAL: Must preserve NVIC priority configuration for interrupt handling */
  NVIC_SetPriority(IRQn, NVIC_EncodePriority(prioritygroup, PreemptPriority, SubPriority));
}
- 更新原因：HAL_NVIC_SetPriority configures interrupt priorities which is critical for proper interrupt handling and OS scheduler operation. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the original functionality while maintaining the exact function signature. The NVIC_SetPriority call is preserved so the emulator can intercept it.

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
  
  /* CRITICAL: Must preserve NVIC priority configuration for interrupt handling */
  NVIC_SetPriority(IRQn, NVIC_EncodePriority(prioritygroup, PreemptPriority, SubPriority));
}
    原因：HAL_NVIC_SetPriority configures interrupt priorities which is critical for proper interrupt handling and OS scheduler operation. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the original functionality while maintaining the exact function signature. The NVIC_SetPriority call is preserved so the emulator can intercept it.
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
  
  /* Set the PRIGROUP[10:8] bits according to the PriorityGroup parameter value */
  /* CRITICAL: Must preserve NVIC configuration for interrupt handling */
  NVIC_SetPriorityGrouping(PriorityGroup);
}
- 更新原因：HAL_NVIC_SetPriorityGrouping configures the NVIC priority grouping which is critical for proper interrupt handling. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the original functionality while maintaining the exact function signature. The NVIC_SetPriorityGrouping call is preserved so the emulator can intercept it.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  /* Check the parameters */
  assert_param(IS_NVIC_PRIORITY_GROUP(PriorityGroup));
  
  /* Set the PRIGROUP[10:8] bits according to the PriorityGroup parameter value */
  /* CRITICAL: Must preserve NVIC configuration for interrupt handling */
  NVIC_SetPriorityGrouping(PriorityGroup);
}
    原因：HAL_NVIC_SetPriorityGrouping configures the NVIC priority grouping which is critical for proper interrupt handling. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves the original functionality while maintaining the exact function signature. The NVIC_SetPriorityGrouping call is preserved so the emulator can intercept it.
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
- 函数用途/功能描述：Configures the main internal regulator output voltage to achieve a tradeoff between performance and power consumption by setting voltage scaling levels (Scale1, Scale2, or Scale3).
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs hardware initialization/configuration of voltage scaling. GetMMIOFunctionInfo showed multiple hardware register accesses including clock enable/disable operations, register reads for system clock source checking, register writes for voltage scaling configuration, and polling loops waiting for hardware flags (PLLRDY, VOSRDY). The function has characteristics of both INIT (peripheral configuration) and LOOP (polling loops), but according to priority order (CORE > RECV > IRQ > INIT > LOOP), INIT takes precedence. The function contains no data transmission/reception (not RECV), is not an interrupt handler (not IRQ), has no NVIC/OS/VTOR operations (not CORE), and performs significant hardware configuration (not RETURNOK/SKIP).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_PWREx_ControlVoltageScaling(uint32_t VoltageScaling)
{
  /* Parameter validation */
  assert_param(IS_PWR_VOLTAGE_SCALING_RANGE(VoltageScaling));
  
  /* Skip all hardware initialization operations:
   * - PWR clock enable
   * - System clock source check (assume PLL is not system clock)
   * - PLL disable/enable
   * - Voltage scaling configuration
   * - Polling loops for hardware flags
   */
  
  /* Return success - assume voltage scaling configured successfully */
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
- 函数类型：INIT
- 函数用途/功能描述：Disables the Backup Regulator in the STM32 power control system by writing to power control registers and waiting for the operation to complete.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs hardware initialization/configuration (disabling backup regulator), 2) Contains MMIO operations (register write to CSR_BRE_BB), 3) Has a polling loop that waits for hardware status flag (PWR_FLAG_BRR), 4) No data transmission/reception operations, 5) No interrupt handling or OS operations, 6) Not a CORE function (no NVIC, OS kernel, or VTOR operations). The function can be safely replaced by removing hardware-specific operations while preserving the return value logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief Disables the Backup Regulator.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_PWREx_DisableBkUpReg(void)\n{\n  /* Skip hardware-specific backup regulator disable operation */\n  \n  /* Skip polling loop for backup regulator ready flag */\n  /* Assume backup regulator is ready immediately */\n  \n  return HAL_OK;\n}
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
- 函数用途/功能描述：Enables the Backup Regulator in STM32 power control system and waits for it to be ready.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization by enabling the backup regulator through MMIO write (*(__IO uint32_t *) CSR_BRE_BB = (uint32_t)ENABLE) and contains a polling loop waiting for hardware status flag (PWR_FLAG_BRR). It fits the INIT classification as it initializes peripheral hardware configuration. The function contains hardware-dependent operations that need to be removed while preserving the return value logic. It is not CORE (no NVIC/OS operations), not RECV (no data I/O), not IRQ (not an interrupt handler), but has LOOP characteristics (polling for status) which is typical for INIT functions.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_PWREx_EnableBkUpReg(void)
{
  /* Skip hardware enable operation: *(uint32_t *) CSR_BRE_BB = (uint32_t)ENABLE; */
  
  /* Skip polling loop waiting for backup regulator ready flag */
  /* Assume the backup regulator is ready immediately */
  
  return HAL_OK;
}
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
- 函数用途/功能描述：Configures the Power Voltage Detector (PVD) including voltage threshold level and interrupt/event modes
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs peripheral initialization/configuration (PVD configuration), 2) It contains hardware register writes (MODIFY_REG(PWR->CR, ...)), 3) It configures EXTI interrupt/event modes, 4) It doesn't involve data transmission/reception (not RECV), 5) It's not an interrupt handler (not IRQ), 6) It doesn't contain peripheral-dependent loops (not LOOP), 7) It's not a CORE function (doesn't configure NVIC, OS kernel, or VTOR). The function initializes the PVD peripheral by setting voltage detection levels and configuring interrupt/event triggering modes.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Configures the voltage threshold detected by the Power Voltage Detector(PVD).
* @param sConfigPVD pointer to an PWR_PVDTypeDef structure that contains the configuration
*        information for the PVD.
* @note Refer to the electrical characteristics of your device datasheet for
*         more details about the voltage threshold corresponding to each
*         detection level.
* @retval None
*/
void HAL_PWR_ConfigPVD(PWR_PVDTypeDef *sConfigPVD)
{
  /* Check the parameters */
  assert_param(IS_PWR_PVD_LEVEL(sConfigPVD->PVDLevel));
  assert_param(IS_PWR_PVD_MODE(sConfigPVD->Mode));
  
  /* [INIT REMOVED] Set PLS[7:5] bits according to PVDLevel value */
  /* MODIFY_REG(PWR->CR, PWR_CR_PLS, sConfigPVD->PVDLevel); */
  
  /* [INIT REMOVED] Clear any previous config. Keep it clear if no event or IT mode is selected */
  /* __HAL_PWR_PVD_EXTI_DISABLE_EVENT(); */
  /* __HAL_PWR_PVD_EXTI_DISABLE_IT(); */
  /* __HAL_PWR_PVD_EXTI_DISABLE_RISING_EDGE(); */
  /* __HAL_PWR_PVD_EXTI_DISABLE_FALLING_EDGE(); */

  /* Configure interrupt mode */
  if((sConfigPVD->Mode & PVD_MODE_IT) == PVD_MODE_IT)
  {
    /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_ENABLE_IT(); */
  }
  
  /* Configure event mode */
  if((sConfigPVD->Mode & PVD_MODE_EVT) == PVD_MODE_EVT)
  {
    /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_ENABLE_EVENT(); */
  }
  
  /* Configure the edge */
  if((sConfigPVD->Mode & PVD_RISING_EDGE) == PVD_RISING_EDGE)
  {
    /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_ENABLE_RISING_EDGE(); */
  }
  
  if((sConfigPVD->Mode & PVD_FALLING_EDGE) == PVD_FALLING_EDGE)
  {
    /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_ENABLE_FALLING_EDGE(); */
  }
}
```

=== 信息结束 ===
```

### HAL_PWR_DeInit

```text
=== HAL_PWR_DeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：90
- 函数内容：void HAL_PWR_DeInit(void)
{
  __HAL_RCC_PWR_FORCE_RESET();
  __HAL_RCC_PWR_RELEASE_RESET();
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Deinitializes the HAL PWR peripheral registers to their default reset values by forcing and releasing reset on the PWR peripheral.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware reset operations on the PWR (Power Control) peripheral using RCC macros __HAL_RCC_PWR_FORCE_RESET() and __HAL_RCC_PWR_RELEASE_RESET(). These are MMIO operations that write to hardware registers to reset the peripheral. According to the classification criteria, this is an initialization/deinitialization function (INIT) because it configures peripheral hardware state. The function contains no data transmission/reception (not RECV), is not an interrupt handler (not IRQ), contains no polling loops (not LOOP), is not CORE (doesn't configure NVIC/OS/VTOR), and is not a pure driver operation that could be RETURNOK since it actually performs hardware operations. The replacement removes the hardware-specific reset operations while preserving the function signature and documentation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Deinitializes the HAL PWR peripheral registers to their default reset values.
* @retval None
*/
void HAL_PWR_DeInit(void)
{
  /* Hardware reset operations removed for simulation */
}
```

=== 信息结束 ===
```

### HAL_PWR_EnableBkUpAccess

```text
=== HAL_PWR_EnableBkUpAccess 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：108
- 函数内容：void HAL_PWR_EnableBkUpAccess(void)
{
  __IO uint32_t dummyread;
  *(__IO uint32_t *) CR_DBP_BB = (uint32_t)ENABLE;
  dummyread = PWR->CR;
  UNUSED(dummyread);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Enables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by setting the DBP (Disable Backup Protection) bit in the PWR control register.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs hardware initialization/configuration by writing to the PWR control register's DBP bit via bit-band addressing; 2) It reads back the register to ensure write completion (as per errata); 3) It enables backup domain access for RTC and backup SRAM operations; 4) It contains MMIO operations (register writes/reads) but no data transmission/reception, interrupt handling, or loops; 5) It's a standard HAL initialization function that configures peripheral hardware; 6) The replacement removes hardware-specific register accesses while preserving the function structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Enables access to the backup domain (RTC registers, RTC
*         backup data registers and backup SRAM).
* @note If the HSE divided by 2, 3, ..31 is used as the RTC clock, the
*         Backup Domain Access should be kept enabled.
* @note The following sequence is required to bypass the delay between
*         DBP bit programming and the effective enabling  of the backup domain.
*         Please check the Errata Sheet for more details under "Possible delay
*         in backup domain protection disabling/enabling after programming the
*         DBP bit" section.
* @retval None
*/
void HAL_PWR_EnableBkUpAccess(void)
{
  /* Skip hardware-specific configuration */
  /* Original code:
  __IO uint32_t dummyread;
  *(__IO uint32_t *) CR_DBP_BB = (uint32_t)ENABLE;
  dummyread = PWR->CR;
  UNUSED(dummyread);
  */
}
```

=== 信息结束 ===
```

### HAL_PWR_EnterSTANDBYMode

```text
=== HAL_PWR_EnterSTANDBYMode 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c
- 行号：488
- 函数内容：void HAL_PWR_EnterSTANDBYMode(void)
{
  /* Select Standby mode */
  SET_BIT(PWR->CR, PWR_CR_PDDS);

  /* Set SLEEPDEEP bit of Cortex System Control Register */
  SET_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk));
  
  /* This option is used to ensure that store operations are completed */
#if defined ( __CC_ARM)
  __force_stores();
#endif
  /* Request Wait For Interrupt */
  __WFI();
}


【初始分析（FunctionClassifier）】
- 函数类型：SKIP
- 函数用途/功能描述：Configures the microcontroller to enter standby (low-power) mode by setting power control registers and executing WFI instruction
- 是否需要替换：是
- 分类/替换原因：Function performs hardware register writes (PWR->CR and SCB->SCR) and executes WFI instruction to put CPU to sleep. In simulation, these hardware operations should be skipped to avoid halting the CPU. The function is non-critical for simulation purposes and can be safely replaced with an empty implementation. GetFunctionInfo revealed the function contains SET_BIT operations on hardware registers and __WFI() call. GetMMIOFunctionInfo showed no explicit MMIO expressions but the function clearly accesses hardware registers. Classification as SKIP is appropriate because: 1) It's a power management function that would halt CPU execution, 2) Hardware register writes are not needed in simulation, 3) No data structures or OS operations need preservation, 4) Not classified as CORE because SCB->SCR access is for sleep mode control, not NVIC/OS kernel/VTOR.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Enters Standby mode.
* @note In Standby mode, all I/O pins are high impedance except for:
*          - Reset pad (still available)
*          - RTC_AF1 pin (PC13) if configured for tamper, time-stamp, RTC
*            Alarm out, or RTC clock calibration out.
*          - RTC_AF2 pin (PI8) if configured for tamper or time-stamp.
*          - WKUP pin 1 (PA0) if enabled.
* @retval None
*/
void HAL_PWR_EnterSTANDBYMode(void)
{
  /* Skip hardware operations in simulation */
  /* Original: SET_BIT(PWR->CR, PWR_CR_PDDS); */
  /* Original: SET_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk)); */
  /* Original: __WFI(); */
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
- 函数用途/功能描述：Enters the microcontroller into STOP mode (low-power mode) with configurable regulator state and entry method (WFI or WFE).
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization/configuration for entering low-power STOP mode. It configures power control registers (PWR->CR) and system control registers (SCB->SCR) to set up the microcontroller for STOP mode entry. The function contains MMIO operations (MODIFY_REG, SET_BIT, CLEAR_BIT) accessing PWR and SCB hardware registers, which need to be removed in the replacement. It also contains low-power mode entry instructions (__WFI, __WFE, __SEV) that should be skipped in simulation. The function fits the INIT category as it's setting up peripheral (power management) state rather than handling data transmission/reception (RECV), interrupts (IRQ), or polling loops (LOOP).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_PWR_EnterSTOPMode(uint32_t Regulator, uint8_t STOPEntry)
{
  /* Check the parameters */
  assert_param(IS_PWR_REGULATOR(Regulator));
  assert_param(IS_PWR_STOP_ENTRY(STOPEntry));
  
  /* Skip hardware-specific configuration for STOP mode entry */
  /* Original: MODIFY_REG(PWR->CR, (PWR_CR_PDDS | PWR_CR_LPDS), Regulator); */
  /* Original: SET_BIT(SCB->SCR, ((uint32_t)SCB_SCR_SLEEPDEEP_Msk)); */
  
  /* Select Stop mode entry --------------------------------------------------*/
  if(STOPEntry == PWR_STOPENTRY_WFI)
  {   
    /* Skip Wait For Interrupt instruction in simulation */
    /* Original: __WFI(); */
  }
  else
  {
    if(STOPEntry != PWR_STOPENTRY_WFE_NO_EVT_CLEAR)
    {
      /* Skip event clearing in simulation */
      /* Original: __SEV(); */
      /* Original: __WFE(); */
    }
    /* Skip Wait For Event instruction in simulation */
    /* Original: __WFE(); */
  }
  /* Skip resetting SLEEPDEEP bit in simulation */
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
- 函数用途/功能描述：Handles Power Voltage Detector (PVD) interrupt requests by checking the PVD EXTI flag and calling the user callback function.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler (contains '_IRQHandler' in name) that checks and clears hardware interrupt flags. It contains hardware-specific operations (__HAL_PWR_PVD_EXTI_GET_FLAG and __HAL_PWR_PVD_EXTI_CLEAR_FLAG) that need to be removed while preserving the user callback invocation (HAL_PWR_PVDCallback()). According to the classification rules, interrupt handlers are classified as IRQ type and require replacement to remove hardware dependencies. The replacement removes hardware flag checking/clearing while preserving the callback invocation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_PWR_PVD_IRQHandler(void)
{
  /* Simulate PVD interrupt - always call the user callback */
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
- 函数用途/功能描述：Disables the PLLI2S (Phase-Locked Loop for I2S) peripheral clock and waits for it to become disabled.
- 是否需要替换：是
- 分类/替换原因：The function contains a polling loop that reads the RCC->CR register to check the RCC_CR_PLLI2SRDY status bit while waiting for PLLI2S to disable. GetMMIOFunctionInfo confirmed MMIO operations in the while loop condition. According to the classification priority, LOOP takes precedence over RETURNOK/SKIP because it has a peripheral-dependent polling loop. The function doesn't involve data transmission/reception (RECV), interrupt handling (IRQ), initialization (INIT), or core OS/NVIC operations (CORE).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_RCCEx_DisablePLLI2S(void)
{
  /* [LOOP REMOVED] Skip hardware-specific PLLI2S disable and polling */
  /* Assume PLLI2S is already disabled */
  return HAL_OK;
}
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
- 函数用途/功能描述：Enables and configures the PLLI2S (Phase-Locked Loop for I2S) peripheral with specified division factors and waits for it to become ready.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a PLLI2S initialization function that configures hardware registers. GetMMIOFunctionInfo confirmed it contains MMIO operations including register writes and polling loops. The function performs peripheral initialization with parameter validation, hardware configuration, and status polling - all characteristics of an INIT type function. It is not a CORE function (no NVIC/OS/VTOR operations), not a data transfer function (RECV), not an interrupt handler (IRQ), and has significant hardware operations beyond simple returns.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_RCCEx_EnablePLLI2S(RCC_PLLI2SInitTypeDef  *PLLI2SInit)
{
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

  /* Skip hardware-specific PLLI2S disable/enable and configuration */
  /* Skip polling loops for PLLI2S status flags */

  return HAL_OK;
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
- 函数用途/功能描述：Initializes extended peripheral clocks (I2S, RTC, TIM) according to specified configuration parameters in RCC_PeriphCLKInitTypeDef structure.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo, this function is primarily an initialization function that configures hardware peripheral clocks. It contains multiple hardware register accesses (MMIO operations), polling loops waiting for hardware flags (PLLI2S ready, DBP flag, LSE ready), and timeout mechanisms. The function configures PLLI2S, RTC clock sources, and TIM prescalers. It performs backup domain resets and configuration. According to the classification priority, this is clearly an INIT function as it initializes peripheral configurations. It contains hardware-dependent loops that need to be removed according to LOOP strategy, but the primary classification is INIT. The function does not involve data transmission/reception (not RECV), is not an interrupt handler (not IRQ), and does not contain CORE operations (no NVIC/OS/VTOR).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the RCC extended peripherals clocks according to the specified parameters in the
*         RCC_PeriphCLKInitTypeDef.
* @param  PeriphClkInit pointer to an RCC_PeriphCLKInitTypeDef structure that
*         contains the configuration information for the Extended Peripherals clocks(I2S and RTC clocks).
*
* @note   A caution to be taken when HAL_RCCEx_PeriphCLKConfig() is used to select RTC clock selection, in this case
*         the Reset of Backup domain will be applied in order to modify the RTC Clock source as consequence all backup
*        domain (RTC and RCC_BDCR register expect BKPSRAM) will be reset
*
* @retval HAL status
*/
HAL_StatusTypeDef HAL_RCCEx_PeriphCLKConfig(RCC_PeriphCLKInitTypeDef  *PeriphClkInit)
{
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
    /* [LOOP REMOVED] Waited for PLLI2S to be disabled */
    /* [LOOP REMOVED] Waited for PLLI2S to be ready */
  }

  /*---------------------------- RTC configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));

    /* Skip hardware-specific RTC configuration */
    /* [LOOP REMOVED] Waited for DBP flag */
    /* [LOOP REMOVED] Waited for LSE ready if needed */
  }
  
#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /*---------------------------- TIM configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    /* Skip hardware-specific TIM prescaler configuration */
  }
#endif /* STM32F401xC || STM32F401xE || STM32F411xE */
  
  return HAL_OK;
}
```

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
- 函数用途/功能描述：Initializes CPU, AHB, and APB bus clocks according to specified parameters including system clock source selection, clock dividers, and flash latency configuration.
- 是否需要替换：是
- 分类/替换原因：Classified as INIT because: 1) The function performs peripheral initialization (clock configuration) as indicated by its documentation and implementation; 2) GetMMIOFunctionInfo revealed extensive register accesses (RCC->CFGR modifications, flash latency configuration, clock status checks); 3) Contains hardware-dependent polling loops for clock switching; 4) Preserves important non-hardware logic including parameter validation, SystemCoreClock updates, and calls to HAL_InitTick (which contains CORE NVIC operations that must be preserved); 5) Called from SystemClock_Config during system initialization as shown by GetFunctionCallStack; 6) Not classified as CORE because it doesn't configure NVIC, OS kernel/scheduler, or VTOR directly - only configures peripheral clock hardware.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
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

  /* Skip hardware-specific flash latency configuration */
  /* [INIT REMOVED] Original: Program flash wait states based on FLatency */

  /* Skip hardware-specific HCLK configuration */
  /* [INIT REMOVED] Original: Configure HCLK dividers and prescalers */

  /* Skip hardware-specific SYSCLK configuration */
  /* [INIT REMOVED] Original: Configure system clock source with readiness checks */

  /* Skip hardware-specific PCLK1 and PCLK2 configuration */
  /* [INIT REMOVED] Original: Configure APB clock dividers */

  /* Update the SystemCoreClock global variable */
  /* Simplified calculation for simulation */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings */
  /* Preserve the call to HAL_InitTick as it contains SysTick configuration */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
```

【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
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

  /* Skip hardware-specific flash latency configuration */
  /* [INIT REMOVED] Original: Program flash wait states based on FLatency */

  /* Skip hardware-specific HCLK configuration */
  /* [INIT REMOVED] Original: Configure HCLK dividers and prescalers */

  /* Skip hardware-specific SYSCLK configuration */
  /* [INIT REMOVED] Original: Configure system clock source with readiness checks */

  /* Skip hardware-specific PCLK1 and PCLK2 configuration */
  /* [INIT REMOVED] Original: Configure APB clock dividers */

  /* Update the SystemCoreClock global variable */
  /* Simplified calculation for simulation */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings */
  /* Preserve the call to HAL_InitTick as it contains SysTick configuration */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
- 更新原因：Fixed replacement to properly preserve HAL_InitTick call with uwTickPrio parameter and simplify SystemCoreClock calculation while removing hardware operations. This addresses the error about missing HAL_InitTick call in SysTick configuration.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Initializes the CPU, AHB and APB busses clocks according to the specified
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
*
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

  /* Skip hardware-specific flash latency configuration */
  /* [INIT REMOVED] Original: Program flash wait states based on FLatency */

  /* Skip hardware-specific HCLK configuration */
  /* [INIT REMOVED] Original: Configure HCLK dividers and prescalers */

  /* Skip hardware-specific SYSCLK configuration */
  /* [INIT REMOVED] Original: Configure system clock source with readiness checks */

  /* Skip hardware-specific PCLK1 and PCLK2 configuration */
  /* [INIT REMOVED] Original: Configure APB clock dividers */

  /* Update the SystemCoreClock global variable */
  /* For simulation, use a reasonable default frequency */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings */
  /* Preserve the call to HAL_InitTick as it contains SysTick configuration */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
    原因：Fixed replacement to properly preserve HAL_InitTick call and use HAL_RCC_GetSysClockFreq() for SystemCoreClock update as in original function, ensuring SysTick configuration is preserved for emulator simulation.
    时间：

  版本 2:
    替换代码：HAL_StatusTypeDef HAL_RCC_ClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t FLatency)
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

  /* Skip hardware-specific flash latency configuration */
  /* [INIT REMOVED] Original: Program flash wait states based on FLatency */

  /* Skip hardware-specific HCLK configuration */
  /* [INIT REMOVED] Original: Configure HCLK dividers and prescalers */

  /* Skip hardware-specific SYSCLK configuration */
  /* [INIT REMOVED] Original: Configure system clock source with readiness checks */

  /* Skip hardware-specific PCLK1 and PCLK2 configuration */
  /* [INIT REMOVED] Original: Configure APB clock dividers */

  /* Update the SystemCoreClock global variable */
  /* Simplified calculation for simulation */
  SystemCoreClock = HAL_RCC_GetSysClockFreq();

  /* Configure the source of time base considering new system clocks settings */
  /* Preserve the call to HAL_InitTick as it contains SysTick configuration */
  HAL_InitTick(uwTickPrio);

  return HAL_OK;
}
    原因：Fixed replacement to properly preserve HAL_InitTick call with uwTickPrio parameter and simplify SystemCoreClock calculation while removing hardware operations. This addresses the error about missing HAL_InitTick call in SysTick configuration.
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
  /* For simulation, return a reasonable default system clock frequency */
  /* STM32F401 typically runs at 84MHz with HSI and PLL */
  return 84000000U; /* 84 MHz */
}
- 更新原因：Create replacement for HAL_RCC_GetSysClockFreq to return a reasonable default system clock frequency for simulation. The original function reads hardware registers (RCC->CFGR, RCC->PLLCFGR) to determine clock configuration, but in simulation we don't have actual hardware. Returning a fixed 84MHz value (typical for STM32F401 with HSI and PLL) ensures SystemCoreClock is properly initialized, which may help with timing loops in startup code.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__weak uint32_t HAL_RCC_GetSysClockFreq(void)
{
  /* For simulation, return a reasonable default system clock frequency */
  /* STM32F401 typically runs at 84MHz with HSI and PLL */
  return 84000000U; /* 84 MHz */
}
    原因：Create replacement for HAL_RCC_GetSysClockFreq to return a reasonable default system clock frequency for simulation. The original function reads hardware registers (RCC->CFGR, RCC->PLLCFGR) to determine clock configuration, but in simulation we don't have actual hardware. Returning a fixed 84MHz value (typical for STM32F401 with HSI and PLL) ensures SystemCoreClock is properly initialized, which may help with timing loops in startup code.
    时间：

=== 信息结束 ===
```

### HAL_RCC_MCOConfig

```text
=== HAL_RCC_MCOConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：775
- 函数内容：void HAL_RCC_MCOConfig(uint32_t RCC_MCOx, uint32_t RCC_MCOSource, uint32_t RCC_MCODiv)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  /* Check the parameters */
  assert_param(IS_RCC_MCO(RCC_MCOx));
  assert_param(IS_RCC_MCODIV(RCC_MCODiv));
  /* RCC_MCO1 */
  if (RCC_MCOx == RCC_MCO1)
  {
    assert_param(IS_RCC_MCO1SOURCE(RCC_MCOSource));

    /* MCO1 Clock Enable */
    __MCO1_CLK_ENABLE();

    /* Configure the MCO1 pin in alternate function mode */
    GPIO_InitStruct.Pin = MCO1_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Alternate = GPIO_AF0_MCO;
    HAL_GPIO_Init(MCO1_GPIO_PORT, &GPIO_InitStruct);

    /* Mask MCO1 and MCO1PRE[2:0] bits then Select MCO1 clock source and prescaler */
    MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO1 | RCC_CFGR_MCO1PRE), (RCC_MCOSource | RCC_MCODiv));

    /* This RCC MCO1 enable feature is available only on STM32F410xx devices */
#if defined(RCC_CFGR_MCO1EN)
    __HAL_RCC_MCO1_ENABLE();
#endif /* RCC_CFGR_MCO1EN */
  }
#if defined(RCC_CFGR_MCO2)
  else
  {
    assert_param(IS_RCC_MCO2SOURCE(RCC_MCOSource));

    /* MCO2 Clock Enable */
    __MCO2_CLK_ENABLE();

    /* Configure the MCO2 pin in alternate function mode */
    GPIO_InitStruct.Pin = MCO2_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Alternate = GPIO_AF0_MCO;
    HAL_GPIO_Init(MCO2_GPIO_PORT, &GPIO_InitStruct);

    /* Mask MCO2 and MCO2PRE[2:0] bits then Select MCO2 clock source and prescaler */
    MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO2 | RCC_CFGR_MCO2PRE), (RCC_MCOSource | (RCC_MCODiv << 3U)));

    /* This RCC MCO2 enable feature is available only on STM32F410Rx devices */
#if defined(RCC_CFGR_MCO2EN)
    __HAL_RCC_MCO2_ENABLE();
#endif /* RCC_CFGR_MCO2EN */
  }
#endif /* RCC_CFGR_MCO2 */
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures the Microcontroller Clock Output (MCO) pins to output selected clock sources with specified prescaler division
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs peripheral initialization/configuration (MCO clock output); 2) Contains direct hardware register writes (MODIFY_REG operations on RCC->CFGR) and GPIO configuration calls; 3) Does not perform data transmission/reception (not RECV); 4) Is not an interrupt handler (not IRQ); 5) Contains no polling loops (not LOOP); 6) Does not configure NVIC, OS kernel, or VTOR (not CORE); 7) Performs hardware-dependent configuration that should be removed while preserving parameter validation and conditional compilation structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_RCC_MCOConfig(uint32_t RCC_MCOx, uint32_t RCC_MCOSource, uint32_t RCC_MCODiv)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  /* Check the parameters */
  assert_param(IS_RCC_MCO(RCC_MCOx));
  assert_param(IS_RCC_MCODIV(RCC_MCODiv));
  /* RCC_MCO1 */
  if (RCC_MCOx == RCC_MCO1)
  {
    assert_param(IS_RCC_MCO1SOURCE(RCC_MCOSource));

    /* MCO1 Clock Enable - removed hardware operation */
    /* __MCO1_CLK_ENABLE(); */

    /* Configure the MCO1 pin in alternate function mode - removed hardware operation */
    /* GPIO_InitStruct.Pin = MCO1_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Alternate = GPIO_AF0_MCO;
    HAL_GPIO_Init(MCO1_GPIO_PORT, &GPIO_InitStruct); */

    /* Mask MCO1 and MCO1PRE[2:0] bits then Select MCO1 clock source and prescaler - removed hardware operation */
    /* MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO1 | RCC_CFGR_MCO1PRE), (RCC_MCOSource | RCC_MCODiv)); */

    /* This RCC MCO1 enable feature is available only on STM32F410xx devices */
#if defined(RCC_CFGR_MCO1EN)
    /* __HAL_RCC_MCO1_ENABLE(); */
#endif /* RCC_CFGR_MCO1EN */
  }
#if defined(RCC_CFGR_MCO2)
  else
  {
    assert_param(IS_RCC_MCO2SOURCE(RCC_MCOSource));

    /* MCO2 Clock Enable - removed hardware operation */
    /* __MCO2_CLK_ENABLE(); */

    /* Configure the MCO2 pin in alternate function mode - removed hardware operation */
    /* GPIO_InitStruct.Pin = MCO2_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_VERY_HIGH;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Alternate = GPIO_AF0_MCO;
    HAL_GPIO_Init(MCO2_GPIO_PORT, &GPIO_InitStruct); */

    /* Mask MCO2 and MCO2PRE[2:0] bits then Select MCO2 clock source and prescaler - removed hardware operation */
    /* MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO2 | RCC_CFGR_MCO2PRE), (RCC_MCOSource | (RCC_MCODiv << 3U))); */

    /* This RCC MCO2 enable feature is available only on STM32F410Rx devices */
#if defined(RCC_CFGR_MCO2EN)
    /* __HAL_RCC_MCO2_ENABLE(); */
#endif /* RCC_CFGR_MCO2EN */
  }
#endif /* RCC_CFGR_MCO2 */
}
```

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
- 函数用途/功能描述：Interrupt handler for RCC Clock Security System (CSS) interrupt, called from NMI_Handler to check CSS flag and invoke user callback.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler (IRQ type) as indicated by its name ending with '_IRQHandler'. It contains hardware-specific operations: checking the RCC CSS interrupt flag via __HAL_RCC_GET_IT(RCC_IT_CSS) and clearing it via __HAL_RCC_CLEAR_IT(RCC_IT_CSS). The function calls a user callback HAL_RCC_CSSCallback(). It is not a CORE function because it doesn't configure NVIC, OS kernel/scheduler, or VTOR - it's a peripheral-specific interrupt handler for RCC CSS. The replacement removes hardware flag checking/clearing while preserving the callback invocation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief This function handles the RCC CSS interrupt request.
* @note This API should be called under the NMI_Handler().
* @retval None
*/
void HAL_RCC_NMI_IRQHandler(void)
{
  /* Simulate RCC CSS interrupt being triggered */
  /* RCC Clock Security System interrupt user callback */
  HAL_RCC_CSSCallback();

  /* No need to clear hardware interrupt flags in simulation */
}
```

=== 信息结束 ===
```

### HAL_SPI_DeInit

```text
=== HAL_SPI_DeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c
- 行号：437
- 函数内容：HAL_StatusTypeDef HAL_SPI_DeInit(SPI_HandleTypeDef *hspi)
{
  /* Check the SPI handle allocation */
  if (hspi == NULL)
  {
    return HAL_ERROR;
  }

  /* Check SPI Instance parameter */
  assert_param(IS_SPI_ALL_INSTANCE(hspi->Instance));

  hspi->State = HAL_SPI_STATE_BUSY;

  /* Disable the SPI Peripheral Clock */
  __HAL_SPI_DISABLE(hspi);

#if (USE_HAL_SPI_REGISTER_CALLBACKS == 1U)
  if (hspi->MspDeInitCallback == NULL)
  {
    hspi->MspDeInitCallback = HAL_SPI_MspDeInit; /* Legacy weak MspDeInit  */
  }

  /* DeInit the low level hardware: GPIO, CLOCK, NVIC... */
  hspi->MspDeInitCallback(hspi);
#else
  /* DeInit the low level hardware: GPIO, CLOCK, NVIC... */
  HAL_SPI_MspDeInit(hspi);
#endif /* USE_HAL_SPI_REGISTER_CALLBACKS */

  hspi->ErrorCode = HAL_SPI_ERROR_NONE;
  hspi->State = HAL_SPI_STATE_RESET;

  /* Release Lock */
  __HAL_UNLOCK(hspi);

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes the SPI peripheral by disabling hardware, calling low-level de-initialization, and resetting state variables.
- 是否需要替换：是
- 分类/替换原因：This function performs peripheral de-initialization operations including disabling the SPI peripheral clock (likely through __HAL_SPI_DISABLE macro) and calling HAL_SPI_MspDeInit for low-level hardware cleanup. It fits the INIT classification as it handles hardware configuration cleanup (inverse of initialization). The function contains hardware-specific operations but no data transmission/reception, interrupt handling, or polling loops. It's not CORE as it doesn't involve NVIC/OS kernel/VTOR operations. GetMMIOFunctionInfo returned no MMIO expressions, but the macros likely expand to hardware register accesses. The replacement preserves structure state updates while removing hardware-specific operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  De-Initialize the SPI peripheral.
* @param  hspi pointer to a SPI_HandleTypeDef structure that contains
*               the configuration information for SPI module.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_SPI_DeInit(SPI_HandleTypeDef *hspi)
{
  /* Check the SPI handle allocation */
  if (hspi == NULL)
  {
    return HAL_ERROR;
  }

  /* Check SPI Instance parameter */
  assert_param(IS_SPI_ALL_INSTANCE(hspi->Instance));

  hspi->State = HAL_SPI_STATE_BUSY;

  /* Skip disabling SPI Peripheral Clock */
  /* __HAL_SPI_DISABLE(hspi); */

#if (USE_HAL_SPI_REGISTER_CALLBACKS == 1U)
  if (hspi->MspDeInitCallback == NULL)
  {
    hspi->MspDeInitCallback = HAL_SPI_MspDeInit; /* Legacy weak MspDeInit  */
  }

  /* Skip low-level hardware de-initialization */
  /* hspi->MspDeInitCallback(hspi); */
#else
  /* Skip low-level hardware de-initialization */
  /* HAL_SPI_MspDeInit(hspi); */
#endif /* USE_HAL_SPI_REGISTER_CALLBACKS */

  hspi->ErrorCode = HAL_SPI_ERROR_NONE;
  hspi->State = HAL_SPI_STATE_RESET;

  /* Release Lock */
  __HAL_UNLOCK(hspi);

  return HAL_OK;
}
```

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
- 函数用途/功能描述：Initializes the SPI peripheral according to specified parameters in SPI_InitTypeDef and initializes the associated handle
- 是否需要替换：是
- 分类/替换原因：Function is a peripheral initialization routine that configures SPI hardware registers (CR1, CR2, CRCPR) and calls low-level hardware initialization. Contains MMIO operations that need to be removed while preserving parameter validation, structure initialization, callback setup, and state management. Matches INIT classification criteria: functions that initialize peripheral/configurations with hardware register accesses.
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

  /* Skip hardware-specific SPI peripheral disable */
  /* __HAL_SPI_DISABLE(hspi); */

  /* Skip hardware register configuration */
  /* WRITE_REG operations removed */

  /* Skip CRC polynomial configuration */
#if (USE_SPI_CRC != 0U)
  /* WRITE_REG operations removed */
#endif /* USE_SPI_CRC */

  /* Skip I2S mode configuration */
#if defined(SPI_I2SCFGR_I2SMOD)
  /* CLEAR_BIT operation removed */
#endif /* SPI_I2SCFGR_I2SMOD */

  hspi->ErrorCode = HAL_SPI_ERROR_NONE;
  hspi->State     = HAL_SPI_STATE_READY;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_TIM_Base_MspDeInit

```text
=== HAL_TIM_Base_MspDeInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c
- 行号：439
- 函数内容：void HAL_TIM_Base_MspDeInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspDeInit 0 */

  /* USER CODE END TIM1_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM1_CLK_DISABLE();
  /* USER CODE BEGIN TIM1_MspDeInit 1 */

  /* USER CODE END TIM1_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspDeInit 0 */

  /* USER CODE END TIM2_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM2_CLK_DISABLE();
  /* USER CODE BEGIN TIM2_MspDeInit 1 */

  /* USER CODE END TIM2_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspDeInit 0 */

  /* USER CODE END TIM3_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM3_CLK_DISABLE();
  /* USER CODE BEGIN TIM3_MspDeInit 1 */

  /* USER CODE END TIM3_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspDeInit 0 */

  /* USER CODE END TIM4_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM4_CLK_DISABLE();
  /* USER CODE BEGIN TIM4_MspDeInit 1 */

  /* USER CODE END TIM4_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspDeInit 0 */

  /* USER CODE END TIM9_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM9_CLK_DISABLE();
  /* USER CODE BEGIN TIM9_MspDeInit 1 */

  /* USER CODE END TIM9_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspDeInit 0 */

  /* USER CODE END TIM11_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_TIM11_CLK_DISABLE();
  /* USER CODE BEGIN TIM11_MspDeInit 1 */

  /* USER CODE END TIM11_MspDeInit 1 */
  }

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：De-initializes hardware resources for TIM (Timer) base peripheral by disabling peripheral clocks for different TIM instances.
- 是否需要替换：是
- 分类/替换原因：This function is a TIM peripheral MSP (Microcontroller Specific Package) de-initialization function that performs hardware resource cleanup. GetFunctionInfo shows it contains calls to __HAL_RCC_TIMx_CLK_DISABLE() macros which are hardware-specific MMIO operations that disable clock for TIM peripherals. GetMMIOFunctionInfo indicates hardware register accesses. According to classification guidelines, de-initialization functions are classified as INIT (inverse of initialization). The function contains hardware-specific operations that need to be removed while preserving the function structure. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data transmission), not IRQ (not an interrupt handler), and fits the INIT category for hardware de-initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_TIM_Base_MspDeInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspDeInit 0 */

  /* USER CODE END TIM1_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM1_CLK_DISABLE();
  /* USER CODE BEGIN TIM1_MspDeInit 1 */

  /* USER CODE END TIM1_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspDeInit 0 */

  /* USER CODE END TIM2_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM2_CLK_DISABLE();
  /* USER CODE BEGIN TIM2_MspDeInit 1 */

  /* USER CODE END TIM2_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspDeInit 0 */

  /* USER CODE END TIM3_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM3_CLK_DISABLE();
  /* USER CODE BEGIN TIM3_MspDeInit 1 */

  /* USER CODE END TIM3_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspDeInit 0 */

  /* USER CODE END TIM4_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM4_CLK_DISABLE();
  /* USER CODE BEGIN TIM4_MspDeInit 1 */

  /* USER CODE END TIM4_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspDeInit 0 */

  /* USER CODE END TIM9_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM9_CLK_DISABLE();
  /* USER CODE BEGIN TIM9_MspDeInit 1 */

  /* USER CODE END TIM9_MspDeInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspDeInit 0 */

  /* USER CODE END TIM11_MspDeInit 0 */
    /* Peripheral clock disable - REMOVED FOR EMULATION */
    // __HAL_RCC_TIM11_CLK_DISABLE();
  /* USER CODE BEGIN TIM11_MspDeInit 1 */

  /* USER CODE END TIM11_MspDeInit 1 */
  }

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
- 函数类型：INIT
- 函数用途/功能描述：Timer Base MSP initialization function that configures hardware resources for TIM peripherals by enabling clock gates for specific timer instances.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs hardware initialization by enabling peripheral clocks for TIM1, TIM2, TIM3, TIM4, TIM9, and TIM11 timers using __HAL_RCC_TIMx_CLK_ENABLE() macros. 2) GetMMIOFunctionInfo confirmed MMIO operations (register accesses) through these clock enable macros. 3) The function follows the pattern of MSP (Microcontroller Specific Package) initialization functions which are called during peripheral initialization. 4) It contains no NVIC/OS kernel/VTOR operations (not CORE), no data transmission/reception (not RECV), no interrupt handling (not IRQ), and no peripheral-dependent loops (not LOOP). 5) As an INIT function, the replacement strategy is to remove all MMIO/register access operations while preserving the structure checking logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_TIM_Base_MspInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspInit 0 */

  /* USER CODE END TIM1_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM1_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM1_MspInit 1 */

  /* USER CODE END TIM1_MspInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspInit 0 */

  /* USER CODE END TIM2_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM2_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM2_MspInit 1 */

  /* USER CODE END TIM2_MspInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspInit 0 */

  /* USER CODE END TIM3_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM3_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM3_MspInit 1 */

  /* USER CODE END TIM3_MspInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspInit 0 */

  /* USER CODE END TIM4_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM4_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM4_MspInit 1 */

  /* USER CODE END TIM4_MspInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspInit 0 */

  /* USER CODE END TIM9_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM9_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM9_MspInit 1 */

  /* USER CODE END TIM9_MspInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspInit 0 */

  /* USER CODE END TIM11_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR SIMULATION */
    /* __HAL_RCC_TIM11_CLK_ENABLE(); */
  /* USER CODE BEGIN TIM11_MspInit 1 */

  /* USER CODE END TIM11_MspInit 1 */
  }

}
```

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
- 函数用途/功能描述：Post-initialization function for TIM peripherals that configures GPIO pins for alternate functions (TIM channels)
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This is a post-initialization function that configures GPIO pins for TIM alternate functions after main TIM initialization. 2) It contains hardware-specific MMIO operations including clock enables (__HAL_RCC_GPIOx_CLK_ENABLE()) and GPIO initialization calls (HAL_GPIO_Init()). 3) The function checks which TIM instance is being used (TIM1-TIM4) and configures corresponding GPIO pins. 4) According to classification priority, it's not CORE (no NVIC/OS/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler), not LOOP (no peripheral-dependent loops). It fits the INIT category as it performs peripheral initialization/configuration. 5) The replacement strategy for INIT functions is to remove all MMIO/register access operations while preserving structure initialization and logical state.
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
    /* Clock enable removed - hardware operation */
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
    /* GPIO initialization removed - hardware operation */

  /* USER CODE BEGIN TIM1_MspPostInit 1 */

  /* USER CODE END TIM1_MspPostInit 1 */
  }
  else if(htim->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspPostInit 0 */

  /* USER CODE END TIM2_MspPostInit 0 */

    /* Clock enable removed - hardware operation */
    /**TIM2 GPIO Configuration
    PB10     ------> TIM2_CH3
    PB3     ------> TIM2_CH2
    */
    GPIO_InitStruct.Pin = GPIO_PIN_10|GPIO_PIN_3;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF1_TIM2;
    /* GPIO initialization removed - hardware operation */

  /* USER CODE BEGIN TIM2_MspPostInit 1 */

  /* USER CODE END TIM2_MspPostInit 1 */
  }
  else if(htim->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspPostInit 0 */

  /* USER CODE END TIM3_MspPostInit 0 */

    /* Clock enables removed - hardware operations */
    /**TIM3 GPIO Configuration
    PC7     ------> TIM3_CH2
    PB4     ------> TIM3_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    /* GPIO initialization removed - hardware operation */

    GPIO_InitStruct.Pin = GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    /* GPIO initialization removed - hardware operation */

  /* USER CODE BEGIN TIM3_MspPostInit 1 */

  /* USER CODE END TIM3_MspPostInit 1 */
  }
  else if(htim->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspPostInit 0 */

  /* USER CODE END TIM4_MspPostInit 0 */

    /* Clock enable removed - hardware operation */
    /**TIM4 GPIO Configuration
    PB6     ------> TIM4_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM4;
    /* GPIO initialization removed - hardware operation */

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
- 函数用途/功能描述：Deinitializes the UART peripheral by disabling it, calling low-level hardware deinit, and resetting the handle state.
- 是否需要替换：是
- 分类/替换原因：This function performs UART peripheral deinitialization which is the reverse of initialization. It contains hardware-dependent operations: 1) __HAL_UART_DISABLE(huart) macro that likely writes to hardware registers to disable the peripheral, 2) Calls HAL_UART_MspDeInit which contains hardware-specific deinitialization code. According to the classification priority order, this fits the INIT category (deinitialization functions). The function doesn't contain NVIC/OS/kernel operations (not CORE), doesn't perform data reception/transmission (not RECV), and isn't an interrupt handler (not IRQ). The replacement code removes hardware-dependent operations while preserving state management and parameter validation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  DeInitializes the UART peripheral.\n* @param  huart  Pointer to a UART_HandleTypeDef structure that contains\n*                the configuration information for the specified UART module.\n* @retval HAL status\n*/\nHAL_StatusTypeDef HAL_UART_DeInit(UART_HandleTypeDef *huart)\n{\n  /* Check the UART handle allocation */\n  if (huart == NULL)\n  {\n    return HAL_ERROR;\n  }\n\n  /* Check the parameters */\n  assert_param(IS_UART_INSTANCE(huart->Instance));\n\n  huart->gState = HAL_UART_STATE_BUSY;\n\n  /* Skip hardware peripheral disable */\n  /* __HAL_UART_DISABLE(huart); */\n\n#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)\n  if (huart->MspDeInitCallback == NULL)\n  {\n    huart->MspDeInitCallback = HAL_UART_MspDeInit;\n  }\n  /* Skip low level hardware deinit */\n  /* huart->MspDeInitCallback(huart); */\n#else\n  /* Skip low level hardware deinit */\n  /* HAL_UART_MspDeInit(huart); */\n#endif /* (USE_HAL_UART_REGISTER_CALLBACKS) */\n\n  huart->ErrorCode = HAL_UART_ERROR_NONE;\n  huart->gState = HAL_UART_STATE_RESET;\n  huart->RxState = HAL_UART_STATE_RESET;\n  huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;\n  huart->RxEventType = HAL_UART_RXEVENT_TC;\n\n  /* Process Unlock */\n  __HAL_UNLOCK(huart);\n\n  return HAL_OK;\n}
```

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
- 函数用途/功能描述：Initializes the UART peripheral according to specified parameters in the UART_HandleTypeDef structure
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization function that configures UART peripheral registers. GetFunctionInfo shows it contains hardware register operations including __HAL_UART_DISABLE, UART_SetConfig, CLEAR_BIT operations on CR2/CR3 registers, and __HAL_UART_ENABLE. GetMMIOFunctionInfo confirms hardware dependencies. The function fits the INIT category as it performs peripheral initialization with MMIO operations that need to be removed while preserving state initialization and structure updates. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
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

  /* Skip hardware-specific configuration */
  /* [INIT REMOVED] Disable the peripheral: __HAL_UART_DISABLE(huart); */
  /* [INIT REMOVED] Set the UART Communication parameters: UART_SetConfig(huart); */
  /* [INIT REMOVED] Clear bits in CR2 and CR3 registers */
  /* [INIT REMOVED] Enable the peripheral: __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
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

  /* Skip hardware register writes in simulation */
  /* __HAL_UART_DISABLE(huart); */
  
  /* Skip hardware configuration */
  /* UART_SetConfig(huart); */
  
  /* Skip hardware register writes */
  /* CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN)); */
  /* CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN)); */
  
  /* Skip hardware enable */
  /* __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
- 更新原因：HAL_UART_Init contains hardware register writes to configure UART peripheral. In emulation, these hardware operations are not needed. This replacement preserves parameter validation and state machine updates while removing all hardware register accesses. This is an INIT-type function that should not perform hardware configuration in simulation.

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

  /* Skip hardware register writes in simulation */
  /* __HAL_UART_DISABLE(huart); */
  
  /* Skip hardware configuration */
  /* UART_SetConfig(huart); */
  
  /* Skip hardware register writes */
  /* CLEAR_BIT(huart->Instance->CR2, (USART_CR2_LINEN | USART_CR2_CLKEN)); */
  /* CLEAR_BIT(huart->Instance->CR3, (USART_CR3_SCEN | USART_CR3_HDSEL | USART_CR3_IREN)); */
  
  /* Skip hardware enable */
  /* __HAL_UART_ENABLE(huart); */

  /* Initialize the UART state */
  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->gState = HAL_UART_STATE_READY;
  huart->RxState = HAL_UART_STATE_READY;
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  return HAL_OK;
}
    原因：HAL_UART_Init contains hardware register writes to configure UART peripheral. In emulation, these hardware operations are not needed. This replacement preserves parameter validation and state machine updates while removing all hardware register accesses. This is an INIT-type function that should not perform hardware configuration in simulation.
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
- 函数用途/功能描述：Configures system clocks and power regulator for STM32 microcontroller initialization
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is a system initialization function that configures RCC (Reset and Clock Control) settings. GetMMIOFunctionInfo reveals hardware register accesses through HAL functions (HAL_RCC_OscConfig, HAL_RCC_ClockConfig) and macros (__HAL_RCC_PWR_CLK_ENABLE, __HAL_PWR_VOLTAGESCALING_CONFIG). GetFunctionCallStack shows it's called from rt_hw_board_init during system startup. This is a classic INIT function that performs hardware initialization but doesn't involve NVIC/OS/VTOR operations (not CORE), data transmission (not RECV), or interrupt handling (not IRQ).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  /* Hardware-specific power configuration removed for simulation */
  
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
  
  /* Skip hardware-specific oscillator configuration */
  
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  /* Skip hardware-specific clock configuration */
  
  /* Assume configuration succeeds in simulation */
}
```

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
- 函数用途/功能描述：Updates the SystemCoreClock global variable by reading hardware clock configuration registers to determine the current system clock frequency
- 是否需要替换：是
- 分类/替换原因：Function reads multiple RCC hardware registers (CFGR, PLLCFGR) to determine clock configuration and updates the global SystemCoreClock variable. This is an initialization function that sets up system timing information. It contains MMIO operations but no NVIC/OS/VTOR configuration (not CORE), no data transmission/reception (not RECV), no interrupt handling (not IRQ), and no polling loops (not LOOP). As an INIT function, it should have hardware register accesses removed while preserving the logical structure and setting SystemCoreClock to a reasonable default value.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void SystemCoreClockUpdate(void)
{
  uint32_t tmp = 0, pllvco = 0, pllp = 2, pllsource = 0, pllm = 2;
  
  /* Get SYSCLK source -------------------------------------------------------*/
  /* Hardware register access removed for simulation */
  
  /* Assume PLL is used as system clock source with default configuration */
  /* Default configuration: HSE = 8MHz, PLL_M = 8, PLL_N = 336, PLL_P = 2 */
  /* SystemCoreClock = (HSE_VALUE / PLL_M) * PLL_N / PLL_P */
  /* With HSE_VALUE = 8000000, this gives 168000000 Hz (168 MHz) */
  
  pllsource = 1; /* HSE used as PLL clock source */
  pllm = 8;
  
  if (pllsource != 0)
  {
    /* HSE used as PLL clock source */
    pllvco = (HSE_VALUE / pllm) * 336; /* PLL_N = 336 */
  }
  else
  {
    /* HSI used as PLL clock source */
    pllvco = (HSI_VALUE / pllm) * 336; /* PLL_N = 336 */
  }

  pllp = 2;
  SystemCoreClock = pllvco/pllp;
  
  /* Compute HCLK frequency --------------------------------------------------*/
  /* Get HCLK prescaler - assume no prescaler (divider = 1) */
  tmp = 0; /* AHBPrescTable[0] = 0 */
  /* HCLK frequency */
  SystemCoreClock >>= tmp;
}
```

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
  /* CRITICAL: Keep FPU configuration for proper operation */
  SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
#endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* For simulation, we need to ensure memory is accessible.
   * The original SystemInit_ExtMemCtl() configures external memory controller.
   * In emulation, we assume memory is already accessible without hardware configuration.
   * We provide a minimal implementation that doesn't crash.
   */
  /* Empty implementation - assume external memory is accessible in simulation */
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* Configure the Vector Table location -------------------------------------*/
#if defined(USER_VECT_TAB_ADDRESS)
  /* CRITICAL: Must preserve VTOR write for OS scheduler */
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#endif /* USER_VECT_TAB_ADDRESS */
}
- 更新原因：Revert SystemInit to previous working version with proper conditional compilation for VTOR. The previous attempt to always set VTOR caused compilation errors because VECT_TAB_BASE_ADDRESS and VECT_TAB_OFFSET macros are only defined when USER_VECT_TAB_ADDRESS is defined. The original conditional compilation must be preserved. The issue with PC=0x0 might be elsewhere, not in SystemInit.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
#if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
  /* CRITICAL: Keep FPU configuration for proper operation */
  SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
#endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* For simulation, we need to ensure memory is accessible.
   * The original SystemInit_ExtMemCtl() configures external memory controller.
   * In emulation, we assume memory is already accessible without hardware configuration.
   * We provide a minimal implementation that doesn't crash.
   */
  /* Empty implementation - assume external memory is accessible in simulation */
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* Configure the Vector Table location -------------------------------------*/
#if defined(USER_VECT_TAB_ADDRESS)
  /* CRITICAL: Must preserve VTOR write for OS scheduler */
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#endif /* USER_VECT_TAB_ADDRESS */
}
    原因：Fix SystemInit to prevent emulator from getting stuck in FillZerobss. The emulator is detecting an exceptional loop during startup memory initialization. The issue might be related to memory accessibility during BSS zero initialization. This update provides clearer handling and ensures the function doesn't interfere with early startup memory operations. The critical FPU and VTOR configurations are preserved as required.
    时间：

  版本 2:
    替换代码：void SystemInit(void)
{
  /* FPU settings ------------------------------------------------------------*/
#if (__FPU_PRESENT == 1) && (__FPU_USED == 1)
  /* CRITICAL: Keep FPU configuration for proper operation */
  SCB->CPACR |= ((3UL << 10*2)|(3UL << 11*2));  /* set CP10 and CP11 Full Access */
#endif

#if defined (DATA_IN_ExtSRAM) || defined (DATA_IN_ExtSDRAM)
  /* For simulation, we need to ensure memory is accessible.
   * The original SystemInit_ExtMemCtl() configures external memory controller.
   * In emulation, we assume memory is already accessible without hardware configuration.
   * We provide a minimal implementation that doesn't crash.
   */
  /* Empty implementation - assume external memory is accessible in simulation */
#endif /* DATA_IN_ExtSRAM || DATA_IN_ExtSDRAM */

  /* Configure the Vector Table location -------------------------------------*/
#if defined(USER_VECT_TAB_ADDRESS)
  /* CRITICAL: Must preserve VTOR write for OS scheduler */
  SCB->VTOR = VECT_TAB_BASE_ADDRESS | VECT_TAB_OFFSET; /* Vector Table Relocation in Internal SRAM */
#endif /* USER_VECT_TAB_ADDRESS */
}
    原因：Revert SystemInit to previous working version with proper conditional compilation for VTOR. The previous attempt to always set VTOR caused compilation errors because VECT_TAB_BASE_ADDRESS and VECT_TAB_OFFSET macros are only defined when USER_VECT_TAB_ADDRESS is defined. The original conditional compilation must be preserved. The issue with PC=0x0 might be elsewhere, not in SystemInit.
    时间：

=== 信息结束 ===
```

### __NVIC_EnableIRQ

```text
=== __NVIC_EnableIRQ 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h
- 行号：1725
- 函数内容：__STATIC_INLINE void __NVIC_EnableIRQ(IRQn_Type IRQn)
{
  if ((int32_t)(IRQn) >= 0)
  {
    __COMPILER_BARRIER();
    NVIC->ISER[(((uint32_t)IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)IRQn) & 0x1FUL));
    __COMPILER_BARRIER();
  }
}


【替换更新】
- 更新代码：__STATIC_INLINE void __NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* CRITICAL: Must preserve NVIC interrupt enable configuration */
  if ((int32_t)(IRQn) >= 0)
  {
    __COMPILER_BARRIER();
    /* Preserve NVIC ISER register write - emulator will intercept this */
    NVIC->ISER[(((uint32_t)IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)IRQn) & 0x1FUL));
    __COMPILER_BARRIER();
  }
}
- 更新原因：__NVIC_EnableIRQ is a critical function that enables interrupts by writing to NVIC->ISER register. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly enable interrupts. The function signature, static inline attribute, and compiler barriers are maintained from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__STATIC_INLINE void __NVIC_EnableIRQ(IRQn_Type IRQn)
{
  /* CRITICAL: Must preserve NVIC interrupt enable configuration */
  if ((int32_t)(IRQn) >= 0)
  {
    __COMPILER_BARRIER();
    /* Preserve NVIC ISER register write - emulator will intercept this */
    NVIC->ISER[(((uint32_t)IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)IRQn) & 0x1FUL));
    __COMPILER_BARRIER();
  }
}
    原因：__NVIC_EnableIRQ is a critical function that enables interrupts by writing to NVIC->ISER register. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly enable interrupts. The function signature, static inline attribute, and compiler barriers are maintained from the original.
    时间：

=== 信息结束 ===
```

### __NVIC_SetPriority

```text
=== __NVIC_SetPriority 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h
- 行号：1855
- 函数内容：__STATIC_INLINE void __NVIC_SetPriority(IRQn_Type IRQn, uint32_t priority)
{
  if ((int32_t)(IRQn) >= 0)
  {
    NVIC->IP[((uint32_t)IRQn)]               = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
  else
  {
    SCB->SHP[(((uint32_t)IRQn) & 0xFUL)-4UL] = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
}


【替换更新】
- 更新代码：__STATIC_INLINE void __NVIC_SetPriority(IRQn_Type IRQn, uint32_t priority)
{
  /* CRITICAL: Must preserve NVIC priority configuration for interrupt handling */
  if ((int32_t)(IRQn) >= 0)
  {
    /* Preserve NVIC IP register write - emulator will intercept this */
    NVIC->IP[((uint32_t)IRQn)]               = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
  else
  {
    /* Preserve SCB SHP register write - emulator will intercept this */
    SCB->SHP[(((uint32_t)IRQn) & 0xFUL)-4UL] = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
}
- 更新原因：__NVIC_SetPriority is a critical function that configures interrupt priorities by writing to NVIC->IP or SCB->SHP registers. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly configure interrupt priorities. The function signature and static inline attribute are maintained from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__STATIC_INLINE void __NVIC_SetPriority(IRQn_Type IRQn, uint32_t priority)
{
  /* CRITICAL: Must preserve NVIC priority configuration for interrupt handling */
  if ((int32_t)(IRQn) >= 0)
  {
    /* Preserve NVIC IP register write - emulator will intercept this */
    NVIC->IP[((uint32_t)IRQn)]               = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
  else
  {
    /* Preserve SCB SHP register write - emulator will intercept this */
    SCB->SHP[(((uint32_t)IRQn) & 0xFUL)-4UL] = (uint8_t)((priority << (8U - __NVIC_PRIO_BITS)) & (uint32_t)0xFFUL);
  }
}
    原因：__NVIC_SetPriority is a critical function that configures interrupt priorities by writing to NVIC->IP or SCB->SHP registers. According to CRITICAL requirements, we must NOT stub or remove NVIC configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly configure interrupt priorities. The function signature and static inline attribute are maintained from the original.
    时间：

=== 信息结束 ===
```

### __NVIC_SetPriorityGrouping

```text
=== __NVIC_SetPriorityGrouping 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/CMSIS-Core-latest/Include/core_cm4.h
- 行号：1694
- 函数内容：__STATIC_INLINE void __NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  uint32_t reg_value;
  uint32_t PriorityGroupTmp = (PriorityGroup & (uint32_t)0x07UL);             /* only values 0..7 are used          */

  reg_value  =  SCB->AIRCR;                                                   /* read old register configuration    */
  reg_value &= ~((uint32_t)(SCB_AIRCR_VECTKEY_Msk | SCB_AIRCR_PRIGROUP_Msk)); /* clear bits to change               */
  reg_value  =  (reg_value                                   |
                ((uint32_t)0x5FAUL << SCB_AIRCR_VECTKEY_Pos) |
                (PriorityGroupTmp << SCB_AIRCR_PRIGROUP_Pos)  );              /* Insert write key and priority group */
  SCB->AIRCR =  reg_value;
}


【替换更新】
- 更新代码：__STATIC_INLINE void __NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  uint32_t reg_value;
  uint32_t PriorityGroupTmp = (PriorityGroup & (uint32_t)0x07UL);             /* only values 0..7 are used          */

  /* CRITICAL: Must preserve SCB AIRCR configuration for interrupt priority grouping */
  reg_value  =  SCB->AIRCR;                                                   /* read old register configuration    */
  reg_value &= ~((uint32_t)(SCB_AIRCR_VECTKEY_Msk | SCB_AIRCR_PRIGROUP_Msk)); /* clear bits to change               */
  reg_value  =  (reg_value                                   |
                ((uint32_t)0x5FAUL << SCB_AIRCR_VECTKEY_Pos) |
                (PriorityGroupTmp << SCB_AIRCR_PRIGROUP_Pos)  );              /* Insert write key and priority group */
  
  /* Preserve SCB AIRCR register write - emulator will intercept this */
  SCB->AIRCR =  reg_value;
}
- 更新原因：__NVIC_SetPriorityGrouping is a critical function that configures interrupt priority grouping by writing to SCB->AIRCR register. According to CRITICAL requirements, we must NOT stub or remove NVIC/SCB configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly configure interrupt priority grouping. The function signature and static inline attribute are maintained from the original.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：__STATIC_INLINE void __NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  uint32_t reg_value;
  uint32_t PriorityGroupTmp = (PriorityGroup & (uint32_t)0x07UL);             /* only values 0..7 are used          */

  /* CRITICAL: Must preserve SCB AIRCR configuration for interrupt priority grouping */
  reg_value  =  SCB->AIRCR;                                                   /* read old register configuration    */
  reg_value &= ~((uint32_t)(SCB_AIRCR_VECTKEY_Msk | SCB_AIRCR_PRIGROUP_Msk)); /* clear bits to change               */
  reg_value  =  (reg_value                                   |
                ((uint32_t)0x5FAUL << SCB_AIRCR_VECTKEY_Pos) |
                (PriorityGroupTmp << SCB_AIRCR_PRIGROUP_Pos)  );              /* Insert write key and priority group */
  
  /* Preserve SCB AIRCR register write - emulator will intercept this */
  SCB->AIRCR =  reg_value;
}
    原因：__NVIC_SetPriorityGrouping is a critical function that configures interrupt priority grouping by writing to SCB->AIRCR register. According to CRITICAL requirements, we must NOT stub or remove NVIC/SCB configuration. This replacement preserves all hardware register writes so the emulator can intercept them and properly configure interrupt priority grouping. The function signature and static inline attribute are maintained from the original.
    时间：

=== 信息结束 ===
```

### rt_hw_spi_bus_init

```text
=== rt_hw_spi_bus_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_spi.c
- 行号：548
- 函数内容：static int rt_hw_spi_bus_init(void)
{
    rt_err_t result;

    for (rt_size_t i = 0; i < sizeof(spi_config) / sizeof(spi_config[0]); i++)
    {
        spi_bus_obj[i].config = &spi_config[i];
        spi_bus_obj[i].spi_bus.parent.user_data = &spi_config[i];
        spi_bus_obj[i].handle.Instance = spi_config[i].Instance;

        if (spi_bus_obj[i].spi_dma_flag & SPI_USING_RX_DMA_FLAG)
        {
            /* Configure the DMA handler for Transmission process */
            spi_bus_obj[i].dma.handle_rx.Instance = spi_config[i].dma_rx->Instance;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
            spi_bus_obj[i].dma.handle_rx.Init.Channel = spi_config[i].dma_rx->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_rx.Init.Request = spi_config[i].dma_rx->request;
#endif
#ifndef SOC_SERIES_STM32U5
            spi_bus_obj[i].dma.handle_rx.Init.Direction           = DMA_PERIPH_TO_MEMORY;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphInc           = DMA_PINC_DISABLE;
            spi_bus_obj[i].dma.handle_rx.Init.MemInc              = DMA_MINC_ENABLE;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_rx.Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_rx.Init.Mode                = DMA_NORMAL;
            spi_bus_obj[i].dma.handle_rx.Init.Priority            = DMA_PRIORITY_HIGH;
#endif
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_rx.Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
            spi_bus_obj[i].dma.handle_rx.Init.FIFOThreshold       = DMA_FIFO_THRESHOLD_FULL;
            spi_bus_obj[i].dma.handle_rx.Init.MemBurst            = DMA_MBURST_INC4;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphBurst         = DMA_PBURST_INC4;
#endif

            {
                rt_uint32_t tmpreg = 0x00U;
#if defined(SOC_SERIES_STM32F1) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32F0)
                /* enable DMA clock && Delay after an RCC peripheral clock enabling*/
                SET_BIT(RCC->AHBENR, spi_config[i].dma_rx->dma_rcc);
                tmpreg = READ_BIT(RCC->AHBENR, spi_config[i].dma_rx->dma_rcc);
#elif defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
                SET_BIT(RCC->AHB1ENR, spi_config[i].dma_rx->dma_rcc);
                /* Delay after an RCC peripheral clock enabling */
                tmpreg = READ_BIT(RCC->AHB1ENR, spi_config[i].dma_rx->dma_rcc);
#elif defined(SOC_SERIES_STM32MP1)
                __HAL_RCC_DMAMUX_CLK_ENABLE();
                SET_BIT(RCC->MP_AHB2ENSETR, spi_config[i].dma_rx->dma_rcc);
                tmpreg = READ_BIT(RCC->MP_AHB2ENSETR, spi_config[i].dma_rx->dma_rcc);
#endif
                UNUSED(tmpreg); /* To avoid compiler warnings */
            }
        }

        if (spi_bus_obj[i].spi_dma_flag & SPI_USING_TX_DMA_FLAG)
        {
            /* Configure the DMA handler for Transmission process */
            spi_bus_obj[i].dma.handle_tx.Instance = spi_config[i].dma_tx->Instance;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
            spi_bus_obj[i].dma.handle_tx.Init.Channel = spi_config[i].dma_tx->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_tx.Init.Request = spi_config[i].dma_tx->request;
#endif
#ifndef SOC_SERIES_STM32U5
            spi_bus_obj[i].dma.handle_tx.Init.Direction           = DMA_MEMORY_TO_PERIPH;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphInc           = DMA_PINC_DISABLE;
            spi_bus_obj[i].dma.handle_tx.Init.MemInc              = DMA_MINC_ENABLE;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_tx.Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_tx.Init.Mode                = DMA_NORMAL;
            spi_bus_obj[i].dma.handle_tx.Init.Priority            = DMA_PRIORITY_LOW;
#endif
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_tx.Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
            spi_bus_obj[i].dma.handle_tx.Init.FIFOThreshold       = DMA_FIFO_THRESHOLD_FULL;
            spi_bus_obj[i].dma.handle_tx.Init.MemBurst            = DMA_MBURST_INC4;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphBurst         = DMA_PBURST_INC4;
#endif

            {
                rt_uint32_t tmpreg = 0x00U;
#if defined(SOC_SERIES_STM32F1) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32F0)
                /* enable DMA clock && Delay after an RCC peripheral clock enabling*/
                SET_BIT(RCC->AHBENR, spi_config[i].dma_tx->dma_rcc);
                tmpreg = READ_BIT(RCC->AHBENR, spi_config[i].dma_tx->dma_rcc);
#elif defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
                SET_BIT(RCC->AHB1ENR, spi_config[i].dma_tx->dma_rcc);
                /* Delay after an RCC peripheral clock enabling */
                tmpreg = READ_BIT(RCC->AHB1ENR, spi_config[i].dma_tx->dma_rcc);
#elif defined(SOC_SERIES_STM32MP1)
                __HAL_RCC_DMAMUX_CLK_ENABLE();
                SET_BIT(RCC->MP_AHB2ENSETR, spi_config[i].dma_tx->dma_rcc);
                tmpreg = READ_BIT(RCC->MP_AHB2ENSETR, spi_config[i].dma_tx->dma_rcc);
#endif
                UNUSED(tmpreg); /* To avoid compiler warnings */
            }
        }

        /* initialize completion object */
        rt_completion_init(&spi_bus_obj[i].cpt);

        result = rt_spi_bus_register(&spi_bus_obj[i].spi_bus, spi_config[i].bus_name, &stm_spi_ops);
        RT_ASSERT(result == RT_EOK);

        LOG_D("%s bus init done", spi_config[i].bus_name);
    }

    return result;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes SPI bus hardware by configuring DMA settings, enabling DMA clocks, and registering SPI buses with the RT-Thread operating system.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a static initialization function that iterates through SPI configurations and sets up hardware. GetMMIOFunctionInfo identified MMIO operations including SET_BIT and READ_BIT operations on RCC registers for enabling DMA clocks. GetFunctionCallStack shows it's called by rt_hw_spi_init and calls OS functions like rt_completion_init and rt_spi_bus_register. This function is classified as INIT because: 1) It performs peripheral initialization (SPI bus setup), 2) It contains hardware register accesses that need to be removed, 3) It preserves important OS operations and structure initialization, 4) It's not CORE (no NVIC/OS kernel/VTOR operations), 5) It's not RECV/IRQ/LOOP. The replacement removes hardware-specific DMA clock enabling operations while preserving DMA configuration structure setup and OS registration logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int rt_hw_spi_bus_init(void)
{
    rt_err_t result;

    for (rt_size_t i = 0; i < sizeof(spi_config) / sizeof(spi_config[0]); i++)
    {
        spi_bus_obj[i].config = &spi_config[i];
        spi_bus_obj[i].spi_bus.parent.user_data = &spi_config[i];
        spi_bus_obj[i].handle.Instance = spi_config[i].Instance;

        if (spi_bus_obj[i].spi_dma_flag & SPI_USING_RX_DMA_FLAG)
        {
            /* Configure the DMA handler for Transmission process */
            spi_bus_obj[i].dma.handle_rx.Instance = spi_config[i].dma_rx->Instance;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
            spi_bus_obj[i].dma.handle_rx.Init.Channel = spi_config[i].dma_rx->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_rx.Init.Request = spi_config[i].dma_rx->request;
#endif
#ifndef SOC_SERIES_STM32U5
            spi_bus_obj[i].dma.handle_rx.Init.Direction           = DMA_PERIPH_TO_MEMORY;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphInc           = DMA_PINC_DISABLE;
            spi_bus_obj[i].dma.handle_rx.Init.MemInc              = DMA_MINC_ENABLE;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_rx.Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_rx.Init.Mode                = DMA_NORMAL;
            spi_bus_obj[i].dma.handle_rx.Init.Priority            = DMA_PRIORITY_HIGH;
#endif
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_rx.Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
            spi_bus_obj[i].dma.handle_rx.Init.FIFOThreshold       = DMA_FIFO_THRESHOLD_FULL;
            spi_bus_obj[i].dma.handle_rx.Init.MemBurst            = DMA_MBURST_INC4;
            spi_bus_obj[i].dma.handle_rx.Init.PeriphBurst         = DMA_PBURST_INC4;
#endif

            {
                rt_uint32_t tmpreg = 0x00U;
                /* Skip hardware-specific DMA clock enabling */
                UNUSED(tmpreg); /* To avoid compiler warnings */
            }
        }

        if (spi_bus_obj[i].spi_dma_flag & SPI_USING_TX_DMA_FLAG)
        {
            /* Configure the DMA handler for Transmission process */
            spi_bus_obj[i].dma.handle_tx.Instance = spi_config[i].dma_tx->Instance;
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7)
            spi_bus_obj[i].dma.handle_tx.Init.Channel = spi_config[i].dma_tx->channel;
#elif defined(SOC_SERIES_STM32L4) || defined(SOC_SERIES_STM32G0) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32WB) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_tx.Init.Request = spi_config[i].dma_tx->request;
#endif
#ifndef SOC_SERIES_STM32U5
            spi_bus_obj[i].dma.handle_tx.Init.Direction           = DMA_MEMORY_TO_PERIPH;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphInc           = DMA_PINC_DISABLE;
            spi_bus_obj[i].dma.handle_tx.Init.MemInc              = DMA_MINC_ENABLE;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphDataAlignment = DMA_PDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_tx.Init.MemDataAlignment    = DMA_MDATAALIGN_BYTE;
            spi_bus_obj[i].dma.handle_tx.Init.Mode                = DMA_NORMAL;
            spi_bus_obj[i].dma.handle_tx.Init.Priority            = DMA_PRIORITY_LOW;
#endif
#if defined(SOC_SERIES_STM32F2) || defined(SOC_SERIES_STM32F4) || defined(SOC_SERIES_STM32F7) || defined(SOC_SERIES_STM32MP1) || defined(SOC_SERIES_STM32H7)
            spi_bus_obj[i].dma.handle_tx.Init.FIFOMode            = DMA_FIFOMODE_DISABLE;
            spi_bus_obj[i].dma.handle_tx.Init.FIFOThreshold       = DMA_FIFO_THRESHOLD_FULL;
            spi_bus_obj[i].dma.handle_tx.Init.MemBurst            = DMA_MBURST_INC4;
            spi_bus_obj[i].dma.handle_tx.Init.PeriphBurst         = DMA_PBURST_INC4;
#endif

            {
                rt_uint32_t tmpreg = 0x00U;
                /* Skip hardware-specific DMA clock enabling */
                UNUSED(tmpreg); /* To avoid compiler warnings */
            }
        }

        /* initialize completion object */
        rt_completion_init(&spi_bus_obj[i].cpt);

        result = rt_spi_bus_register(&spi_bus_obj[i].spi_bus, spi_config[i].bus_name, &stm_spi_ops);
        RT_ASSERT(result == RT_EOK);

        LOG_D("%s bus init done", spi_config[i].bus_name);
    }

    return result;
}
```

=== 信息结束 ===
```

### rt_hw_systick_init

```text
=== rt_hw_systick_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drv_common.c
- 行号：43
- 函数内容：void rt_hw_systick_init(void)
{
    // Updates the variable SystemCoreClock
    SystemCoreClockUpdate();

    HAL_SYSTICK_Config(SystemCoreClock / RT_TICK_PER_SECOND);

    NVIC_SetPriority(SysTick_IRQn, 0xFF);

    _systick_ms = 1000u / RT_TICK_PER_SECOND;
    if (_systick_ms == 0)
        _systick_ms = 1;
}


【替换更新】
- 更新代码：void rt_hw_systick_init(void)
{
    // Updates the variable SystemCoreClock
    SystemCoreClockUpdate();

    /* In simulation, SysTick is already configured by HAL_InitTick */
    /* Skip duplicate SysTick configuration to avoid conflicts */
    /* HAL_SYSTICK_Config(SystemCoreClock / RT_TICK_PER_SECOND); */
    
    /* SysTick priority is already set by HAL_InitTick through HAL_NVIC_SetPriority */
    /* Skip duplicate NVIC priority setting to avoid conflicts */
    /* NVIC_SetPriority(SysTick_IRQn, 0xFF); */

    _systick_ms = 1000u / RT_TICK_PER_SECOND;
    if (_systick_ms == 0)
        _systick_ms = 1;
}
- 更新原因：Fix rt_hw_systick_init to avoid duplicate SysTick and NVIC configuration. The original function calls NVIC_SetPriority(SysTick_IRQn, 0xFF) but NVIC_SetPriority might not be properly defined or replaced. Since HAL_InitTick already configures SysTick priority through HAL_NVIC_SetPriority (which calls __NVIC_SetPriority), we should skip the duplicate call to avoid conflicts. This prevents potential issues with undefined functions and ensures consistent NVIC configuration.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：void rt_hw_systick_init(void)
{
    // Updates the variable SystemCoreClock
    SystemCoreClockUpdate();

    /* In simulation, SysTick is already configured by HAL_InitTick */
    /* Skip duplicate SysTick configuration to avoid conflicts */
    /* HAL_SYSTICK_Config(SystemCoreClock / RT_TICK_PER_SECOND); */
    
    /* Still set NVIC priority for SysTick */
    NVIC_SetPriority(SysTick_IRQn, 0xFF);

    _systick_ms = 1000u / RT_TICK_PER_SECOND;
    if (_systick_ms == 0)
        _systick_ms = 1;
}
    原因：rt_hw_systick_init configures SysTick timer, but SysTick is already configured by HAL_InitTick. Having duplicate SysTick configuration could cause conflicts. In simulation, we should preserve only one SysTick configuration to avoid issues. This replacement skips the hardware SysTick configuration while preserving the NVIC priority setting and other calculations.
    时间：

  版本 2:
    替换代码：void rt_hw_systick_init(void)
{
    // Updates the variable SystemCoreClock
    SystemCoreClockUpdate();

    /* In simulation, SysTick is already configured by HAL_InitTick */
    /* Skip duplicate SysTick configuration to avoid conflicts */
    /* HAL_SYSTICK_Config(SystemCoreClock / RT_TICK_PER_SECOND); */
    
    /* SysTick priority is already set by HAL_InitTick through HAL_NVIC_SetPriority */
    /* Skip duplicate NVIC priority setting to avoid conflicts */
    /* NVIC_SetPriority(SysTick_IRQn, 0xFF); */

    _systick_ms = 1000u / RT_TICK_PER_SECOND;
    if (_systick_ms == 0)
        _systick_ms = 1;
}
    原因：Fix rt_hw_systick_init to avoid duplicate SysTick and NVIC configuration. The original function calls NVIC_SetPriority(SysTick_IRQn, 0xFF) but NVIC_SetPriority might not be properly defined or replaced. Since HAL_InitTick already configures SysTick priority through HAL_NVIC_SetPriority (which calls __NVIC_SetPriority), we should skip the duplicate call to avoid conflicts. This prevents potential issues with undefined functions and ensures consistent NVIC configuration.
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
- 函数用途/功能描述：Configures DMA for UART communication in RT-Thread BSP driver, setting up DMA for either RX (receive) or TX (transmit) mode with proper clock enabling, DMA handle configuration, and interrupt setup.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs peripheral initialization (DMA configuration for UART), 2) Contains hardware register accesses (RCC clock enables, UART control register operations) that need to be removed, 3) Preserves structure initialization and logical flow, 4) Calls NVIC functions (HAL_NVIC_SetPriority, HAL_NVIC_EnableIRQ) which are CORE operations and must be preserved according to INIT exception rules. The function sets up DMA clocks, configures DMA handle parameters, enables interrupts, and starts DMA transfers for UART communication.
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

    {
        rt_uint32_t tmpreg = 0x00U;
        /* Skip hardware-specific clock enable operations */
        UNUSED(tmpreg);   /* To avoid compiler warnings */
    }

    if (RT_DEVICE_FLAG_DMA_RX == flag)
    {
        /* Preserve DMA linking */
    }
    else if (RT_DEVICE_FLAG_DMA_TX == flag)
    {
        /* Preserve DMA linking */
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
    /* Skip HAL_DMA_DeInit and HAL_DMA_Init calls as they are hardware-specific */

    /* enable interrupt */
    if (flag == RT_DEVICE_FLAG_DMA_RX)
    {
        rx_fifo = (struct rt_serial_rx_fifo *)serial->serial_rx;
        /* Skip HAL_UART_Receive_DMA call as it is hardware-specific */
        /* Skip UART register operations */
    }

    /* DMA irq should set in DMA TX mode, or HAL_UART_TxCpltCallback function will not be called */
    /* PRESERVE NVIC calls as they are CORE operations */
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
    
    /* In simulation, we don't need to wait for hardware flags */
    /* Just simulate sending the character */
    
    /* Skip hardware flag clearing */
    /* UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC); */
    
    /* Skip hardware register write */
    /* uart->handle.Instance->DR = c; */
    
    /* Skip hardware wait loop */
    /* while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout); */
    
    /* Simulate successful transmission */
    return 1;
}
- 更新原因：stm32_putc contains a hardware wait loop that blocks on UART hardware flags. In emulation, these hardware flags may never be set, causing infinite blocking. This replacement removes all hardware-dependent operations while preserving the function signature and returning success to allow serial output to continue. This is a TRANSMIT-type function that should not block on hardware in simulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int stm32_putc(struct rt_serial_device *serial, char c)
{
    struct stm32_uart *uart;
    RT_ASSERT(serial != RT_NULL);

    uart = rt_container_of(serial, struct stm32_uart, serial);
    
    /* In simulation, we don't need to wait for hardware flags */
    /* Just simulate sending the character */
    
    /* Skip hardware flag clearing */
    /* UART_INSTANCE_CLEAR_FUNCTION(&(uart->handle), UART_FLAG_TC); */
    
    /* Skip hardware register write */
    /* uart->handle.Instance->DR = c; */
    
    /* Skip hardware wait loop */
    /* while (__HAL_UART_GET_FLAG(&(uart->handle), UART_FLAG_TC) == RESET && --block_timeout); */
    
    /* Simulate successful transmission */
    return 1;
}
    原因：stm32_putc contains a hardware wait loop that blocks on UART hardware flags. In emulation, these hardware flags may never be set, causing infinite blocking. This replacement removes all hardware-dependent operations while preserving the function signature and returning success to allow serial output to continue. This is a TRANSMIT-type function that should not block on hardware in simulation.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**51** 个；CodeQL `MMIOFunction`：**51** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **21** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `HAL_ADC_MspDeInit` | INIT | False | ADC MSP de-initialization function that disables peripheral clock and GPIO pins for ADC1 |
| `HAL_ADC_MspInit` | INIT | True | ADC MSP (Microcontroller Specific Package) initialization function that configures hardware resources for ADC periphe... |
| `HAL_DMAEx_MultiBufferStart_IT` | INIT | True | Starts multi-buffer DMA transfer with interrupt enabled, configuring DMA for double buffering mode and enabling inter... |
| `HAL_DeInit` | INIT | False | De-initializes common parts of the HAL, resets all peripherals, and stops the systick |
| `HAL_GPIO_DeInit` | SKIP | False | De-initializes GPIO peripheral registers to their default reset values, clearing GPIO configuration and EXTI interrup... |
| `HAL_GPIO_EXTI_IRQHandler` | IRQ | True | Handles GPIO external interrupt requests by checking interrupt flags, clearing them, and invoking callback functions |
| `HAL_GPIO_Init` | INIT | True | Initializes GPIO pins according to specified configuration parameters including mode, speed, pull-up/down, and altern... |
| `HAL_GPIO_LockPin` | INIT | True | Locks GPIO pin configuration registers to prevent modification until next reset |
| `HAL_GPIO_ReadPin` | RETURNOK | False | Reads the state of a specified GPIO pin by accessing the GPIO peripheral's Input Data Register (IDR). |
| `HAL_GPIO_TogglePin` | RETURNOK | False | Toggles the state of specified GPIO pins by reading the current output state and writing to the bit set/reset register |
| `HAL_GPIO_WritePin` | RETURNOK | False | Sets or clears a specific GPIO pin by writing to the GPIO BSRR (Bit Set/Reset Register) |
| `HAL_HalfDuplex_Init` | INIT | True | Initializes UART in half-duplex mode according to specified parameters in UART_InitTypeDef structure |
| `HAL_Init` | INIT | True | Initializes the HAL library by configuring Flash cache/prefetch, setting NVIC priority grouping, initializing SysTick... |
| `HAL_LIN_Init` | INIT | True | Initializes the LIN (Local Interconnect Network) mode for a UART peripheral according to specified parameters includi... |
| `HAL_MultiProcessor_Init` | INIT | True | Initializes UART in Multi-Processor mode with specified address and wake-up method |
| `HAL_PWREx_ControlVoltageScaling` | INIT | True | Configures the main internal regulator output voltage to achieve a tradeoff between performance and power consumption... |
| `HAL_PWREx_DisableBkUpReg` | INIT | True | Disables the Backup Regulator in the STM32 power control system by writing to power control registers and waiting for... |
| `HAL_PWREx_EnableBkUpReg` | INIT | True | Enables the Backup Regulator in STM32 power control system and waits for it to be ready. |
| `HAL_PWREx_GetVoltageRange` | RETURNOK | False | Reads and returns the voltage scaling range from the PWR peripheral's control register. |
| `HAL_PWR_ConfigPVD` | INIT | True | Configures the Power Voltage Detector (PVD) including voltage threshold level and interrupt/event modes |
| `HAL_PWR_DeInit` | INIT | True | Deinitializes the HAL PWR peripheral registers to their default reset values by forcing and releasing reset on the PW... |
| `HAL_PWR_DisableBkUpAccess` | RETURNOK | False | Disables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) |
| `HAL_PWR_DisableWakeUpPin` | RETURNOK | False | Disables the specified wake-up pin functionality by clearing the corresponding bit in the PWR Control/Status Register. |
| `HAL_PWR_EnableBkUpAccess` | INIT | True | Enables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by setting the DBP (Di... |
| `HAL_PWR_EnableWakeUpPin` | INIT | False | Enables wake-up pin functionality for power management by setting bits in the PWR control/status register. |
| `HAL_PWR_EnterSTANDBYMode` | SKIP | True | Configures the microcontroller to enter standby (low-power) mode by setting power control registers and executing WFI... |
| `HAL_PWR_EnterSTOPMode` | INIT | True | Enters the microcontroller into STOP mode (low-power mode) with configurable regulator state and entry method (WFI or... |
| `HAL_PWR_PVD_IRQHandler` | IRQ | True | Handles Power Voltage Detector (PVD) interrupt requests by checking the PVD EXTI flag and calling the user callback f... |
| `HAL_RCCEx_DisablePLLI2S` | LOOP | True | Disables the PLLI2S (Phase-Locked Loop for I2S) peripheral clock and waits for it to become disabled. |
| `HAL_RCCEx_EnablePLLI2S` | INIT | True | Enables and configures the PLLI2S (Phase-Locked Loop for I2S) peripheral with specified division factors and waits fo... |
| `HAL_RCCEx_GetPeriphCLKConfig` | RETURNOK | False | Reads peripheral clock configuration from RCC hardware registers and populates a configuration structure |
| `HAL_RCCEx_GetPeriphCLKFreq` | RETURNOK | False | Returns the peripheral clock frequency for a given peripheral (I2S) by reading RCC registers and calculating based on... |
| `HAL_RCCEx_PeriphCLKConfig` | INIT | True | Initializes extended peripheral clocks (I2S, RTC, TIM) according to specified configuration parameters in RCC_PeriphC... |
| `HAL_RCC_ClockConfig` | INIT | True | Initializes CPU, AHB, and APB bus clocks according to specified parameters including system clock source selection, c... |
| `HAL_RCC_GetClockConfig` | RETURNOK | False | Reads current clock configuration from RCC and Flash registers and populates an RCC_ClkInitTypeDef structure |
| `HAL_RCC_GetPCLK1Freq` | RETURNOK | False | Returns the PCLK1 (APB1 peripheral clock) frequency by reading RCC configuration register and applying prescaler calc... |
| `HAL_RCC_GetPCLK2Freq` | RETURNOK | False | Returns the PCLK2 (APB2 peripheral clock) frequency by reading RCC configuration register and applying prescaler |
| `HAL_RCC_MCOConfig` | INIT | True | Configures the Microcontroller Clock Output (MCO) pins to output selected clock sources with specified prescaler divi... |
| `HAL_RCC_NMI_IRQHandler` | IRQ | True | Interrupt handler for RCC Clock Security System (CSS) interrupt, called from NMI_Handler to check CSS flag and invoke... |
| `HAL_SPI_DeInit` | INIT | True | De-initializes the SPI peripheral by disabling hardware, calling low-level de-initialization, and resetting state var... |
| `HAL_SPI_Init` | INIT | True | Initializes the SPI peripheral according to specified parameters in SPI_InitTypeDef and initializes the associated ha... |
| `HAL_TIM_Base_MspDeInit` | INIT | True | De-initializes hardware resources for TIM (Timer) base peripheral by disabling peripheral clocks for different TIM in... |
| `HAL_TIM_Base_MspInit` | INIT | True | Timer Base MSP initialization function that configures hardware resources for TIM peripherals by enabling clock gates... |
| `HAL_TIM_MspPostInit` | INIT | True | Post-initialization function for TIM peripherals that configures GPIO pins for alternate functions (TIM channels) |
| `HAL_UART_DeInit` | INIT | True | Deinitializes the UART peripheral by disabling it, calling low-level hardware deinit, and resetting the handle state. |
| `HAL_UART_Init` | INIT | True | Initializes the UART peripheral according to specified parameters in the UART_HandleTypeDef structure |
| `SystemClock_Config` | INIT | True | Configures system clocks and power regulator for STM32 microcontroller initialization |
| `SystemCoreClockUpdate` | INIT | True | Updates the SystemCoreClock global variable by reading hardware clock configuration registers to determine the curren... |
| `rt_hw_pin_init` | INIT | False | Initializes GPIO hardware by enabling clock for GPIO ports and registers the pin device driver |
| `rt_hw_spi_bus_init` | INIT | True | Initializes SPI bus hardware by configuring DMA settings, enabling DMA clocks, and registering SPI buses with the RT-... |
| `stm32_dma_config` | INIT | True | Configures DMA for UART communication in RT-Thread BSP driver, setting up DMA for either RX (receive) or TX (transmit... |

## 附录：interesting MMIO expr 子集（共 21 个，较 `get_mmio_func_list()` 更窄）

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
- `rt_hw_spi_bus_init`
