## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/rtthread/stm32f401-st-nucleo/i2c`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `HAL_ADC_MspDeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 158 | 1 |
| `HAL_ADC_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 108 | 1 |
| `HAL_DMAEx_MultiBufferStart_IT` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_dma_ex.c` | 154 | 1 |
| `HAL_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 190 | 1 |
| `HAL_GPIO_EXTI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 492 | 1 |
| `HAL_GPIO_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_gpio.c` | 164 | 1 |
| `HAL_HalfDuplex_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 435 | 1 |
| `HAL_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal.c` | 157 | 1 |
| `HAL_LIN_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 509 | 1 |
| `HAL_MultiProcessor_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 591 | 1 |
| `HAL_PWREx_ControlVoltageScaling` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 288 | 1 |
| `HAL_PWREx_DisableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 165 | 1 |
| `HAL_PWREx_EnableBkUpReg` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr_ex.c` | 141 | 1 |
| `HAL_PWR_ConfigPVD` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 275 | 1 |
| `HAL_PWR_EnableBkUpAccess` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 108 | 1 |
| `HAL_PWR_PVD_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_pwr.c` | 509 | 1 |
| `HAL_RCCEx_DisablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2929 | 1 |
| `HAL_RCCEx_EnablePLLI2S` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2846 | 1 |
| `HAL_RCCEx_PeriphCLKConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc_ex.c` | 2551 | 1 |
| `HAL_RCC_ClockConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 591 | 1 |
| `HAL_RCC_GetClockConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 1058 | 1 |
| `HAL_RCC_MCOConfig` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 775 | 1 |
| `HAL_RCC_NMI_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c` | 1084 | 1 |
| `HAL_SPI_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c` | 437 | 1 |
| `HAL_SPI_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_spi.c` | 311 | 1 |
| `HAL_TIM_Base_MspInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 262 | 1 |
| `HAL_TIM_MspPostInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/CubeMX_Config/Src/stm32f4xx_hal_msp.c` | 333 | 1 |
| `HAL_UART_DeInit` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 669 | 1 |
| `HAL_UART_IRQHandler` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 2350 | 1 |
| `HAL_UART_Init` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 357 | 1 |
| `SystemClock_Config` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/board/board.c` | 14 | 1 |
| `SystemCoreClockUpdate` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_cmsis_driver-latest/Source/Templates/system_stm32f4xx.c` | 220 | 1 |
| `UART_Receive_IT` | `/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c` | 3594 | 1 |
| `rt_hw_pin_init` | `/home/haojie/rt-thread/bsp/stm32/libraries/HAL_Drivers/drivers/drv_gpio.c` | 763 | 1 |
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
- 函数用途/功能描述：ADC MSP (Microcontroller Specific Package) de-initialization function that disables peripheral clock and de-initializes GPIO pins used by ADC1
- 是否需要替换：是
- 分类/替换原因：Function performs hardware resource cleanup for ADC peripheral: 1) Disables ADC1 peripheral clock via __HAL_RCC_ADC1_CLK_DISABLE(), 2) De-initializes multiple GPIO pins (PC0, PC1, PA0, PA1, PA4, PB0) using HAL_GPIO_DeInit(). This is a de-initialization counterpart to initialization functions, classified as INIT type. GetMMIOFunctionInfo returned empty list but function clearly contains hardware operations (clock control and GPIO configuration). Not CORE (no NVIC/OS operations), not RECV (no data I/O), not IRQ (not interrupt handler), not LOOP (no polling loops).
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
- 函数类型：INIT
- 函数用途/功能描述：ADC MSP initialization function that configures hardware resources including peripheral clocks and GPIO pins for ADC operation
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This is a peripheral initialization function that enables ADC1, GPIOC, GPIOA, and GPIOB clocks and configures GPIO pins for analog mode. 2) Contains hardware-specific MMIO operations through __HAL_RCC_*_CLK_ENABLE() macros and HAL_GPIO_Init() calls. 3) Does NOT contain any CORE operations (NVIC configuration, OS kernel operations, or VTOR setup). 4) Does NOT enable interrupts or contain interrupt-related code. 5) Follows the INIT classification pattern - removes hardware operations while preserving structure initialization and logical flow. 6) GetFunctionCallStack shows it only calls HAL_GPIO_Init, which are hardware operations to be removed.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_ADC_MspInit(ADC_HandleTypeDef* hadc)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  if(hadc->Instance==ADC1)
  {
  /* USER CODE BEGIN ADC1_MspInit 0 */

  /* USER CODE END ADC1_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
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
    // HAL_GPIO_Init(GPIOC, &GPIO_InitStruct); // REMOVED FOR EMULATION

    GPIO_InitStruct.Pin = GPIO_PIN_0|GPIO_PIN_1|GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    // HAL_GPIO_Init(GPIOA, &GPIO_InitStruct); // REMOVED FOR EMULATION

    GPIO_InitStruct.Pin = GPIO_PIN_0;
    GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    // HAL_GPIO_Init(GPIOB, &GPIO_InitStruct); // REMOVED FOR EMULATION

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
- 函数用途/功能描述：Starts multi-buffer DMA transfer with interrupt enabled, configuring DMA for double buffering mode and enabling interrupts.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it initializes and configures the DMA peripheral for multi-buffer operation with interrupts. Analysis shows: 1) It contains multiple hardware register accesses (CR, M1AR, flag clearing, interrupt enabling, peripheral enabling); 2) It performs DMA peripheral configuration for double buffering mode; 3) It sets up interrupt enable bits; 4) It manages DMA state transitions (READY to BUSY); 5) It validates parameters and callback functions. The function fits the INIT category as it sets up peripheral hardware for operation but doesn't perform actual data transfer (not RECV), isn't an interrupt handler (not IRQ), contains no polling loops (not LOOP), and isn't core OS/NVIC functionality (not CORE).
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
    
    /* Skip hardware-specific configuration via DMA_MultiBufferSetConfig */
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
- 函数用途/功能描述：De-initializes common HAL components and resets peripheral buses (APB1, APB2, AHB1, AHB2, AHB3), then calls HAL_MspDeInit for low-level hardware de-initialization.
- 是否需要替换：是
- 分类/替换原因：Function performs hardware-specific peripheral bus resets using RCC macros (__HAL_RCC_*_FORCE_RESET/RELEASE_RESET) and calls HAL_MspDeInit(). This is a de-initialization function that configures hardware state, fitting the INIT category. It does not contain NVIC/OS/VTOR operations (not CORE), no data reception/transmission (not RECV), no interrupt handling (not IRQ), and no polling loops (not LOOP). The function is documented as optional, supporting the INIT classification where hardware operations can be removed while preserving the call to HAL_MspDeInit() and returning HAL_OK.
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
  /* Skip hardware peripheral resets in simulation */
  
  /* De-Init the low level hardware */
  HAL_MspDeInit();
    
  /* Return function status */
  return HAL_OK;
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
- 函数用途/功能描述：Handles EXTI (External Interrupt) interrupt requests for GPIO pins by checking interrupt flags, clearing them, and calling the user-defined callback function.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler for GPIO EXTI interrupts. Analysis shows: 1) Function name contains 'IRQHandler' indicating interrupt handling role; 2) It checks and clears hardware interrupt flags using __HAL_GPIO_EXTI_GET_IT and __HAL_GPIO_EXTI_CLEAR_IT macros; 3) It calls a callback function HAL_GPIO_EXTI_Callback for application-specific handling; 4) It is called from various EXTI interrupt handlers (EXTI0_IRQHandler, EXTI1_IRQHandler, etc.); 5) It does not qualify as CORE (no NVIC configuration, OS kernel, or VTOR operations). According to classification priority, IRQ functions handle interrupt-related operations and require replacement to remove hardware dependencies while preserving callback execution.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_GPIO_EXTI_IRQHandler(uint16_t GPIO_Pin)
{
  /* EXTI line interrupt detected */
  /* [IRQ REPLACEMENT] Skip hardware interrupt flag check and clear */
  /* Assume interrupt is pending and proceed to callback */
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
- 函数用途/功能描述：Initializes GPIO pins according to specified configuration parameters including mode, speed, pull-up/down resistors, alternate function, and EXTI interrupt configuration.
- 是否需要替换：是
- 分类/替换原因：The function is classified as INIT because: 1) GetFunctionInfo shows it's a GPIO initialization function that configures hardware registers; 2) GetMMIOFunctionInfo reveals extensive MMIO operations to GPIO registers (OSPEEDR, OTYPER, PUPDR, AFR, MODER) and EXTI registers (RTSR, FTSR, EMR, IMR); 3) It contains parameter validation and configuration logic but no data transmission/reception; 4) It's not an interrupt handler (IRQ), not a polling loop (LOOP), not CORE (no NVIC/OS/VTOR operations), and not a simple return function; 5) The function is called by various MspInit functions and driver code for peripheral initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the GPIOx peripheral according to the specified parameters in the GPIO_Init.
* @param  GPIOx where x can be (A..K) to select the GPIO peripheral for STM32F429X device or
*                      x can be (A..I) to select the GPIO peripheral for STM32F40XX and STM32F427X devices.
* @param  GPIO_Init pointer to a GPIO_InitTypeDef structure that contains
*         the configuration information for the specified GPIO peripheral.
* @retval None
*/
void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
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
      if(((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) ||
          (GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Skip hardware-specific configuration for IO Speed */
        /* Skip hardware-specific configuration for IO Output Type */
       }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        /* Skip hardware-specific configuration for Pull-up/Pull-down resistors */
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Skip hardware-specific configuration for Alternate function */
      }

      /* Skip hardware-specific configuration for IO Direction mode */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Enable SYSCFG Clock - keep this as it may be needed for other operations */
        __HAL_RCC_SYSCFG_CLK_ENABLE();

        /* Skip hardware-specific EXTI configuration */
        /* Skip Rising Falling edge configuration */
        /* Skip EXTI line configuration */
      }
    }
  }
}
```

【替换更新】
- 更新代码：/**
* @brief  Initializes the GPIOx peripheral according to the specified parameters in the GPIO_Init.
* @param  GPIOx where x can be (A..K) to select the GPIO peripheral for STM32F429X device or
*                      x can be (A..I) to select the GPIO peripheral for STM32F40XX and STM32F427X devices.
* @param  GPIO_Init pointer to a GPIO_InitTypeDef structure that contains
*         the configuration information for the specified GPIO peripheral.
* @retval None
*/
void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
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
      if(((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) ||
          (GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Skip hardware-specific configuration for IO Speed */
        /* Skip hardware-specific configuration for IO Output Type */
       }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        /* Skip hardware-specific configuration for Pull-up/Pull-down resistors */
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Skip hardware-specific configuration for Alternate function */
      }

      /* Skip hardware-specific configuration for IO Direction mode */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Enable SYSCFG Clock - keep this as it may be needed for other operations */
        __HAL_RCC_SYSCFG_CLK_ENABLE();

        /* Skip hardware-specific EXTI configuration */
        /* Skip Rising Falling edge configuration */
        /* Skip EXTI line configuration */
      }
    }
  }
}
- 更新原因：Fixed syntax error: replaced double backslash line continuation (\\\) with single backslash or removed line continuation by putting condition on same line. Also removed unnecessary line continuation character entirely since the condition fits on one line.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Initializes the GPIOx peripheral according to the specified parameters in the GPIO_Init.
* @param  GPIOx where x can be (A..K) to select the GPIO peripheral for STM32F429X device or
*                      x can be (A..I) to select the GPIO peripheral for STM32F40XX and STM32F427X devices.
* @param  GPIO_Init pointer to a GPIO_InitTypeDef structure that contains
*         the configuration information for the specified GPIO peripheral.
* @retval None
*/
void HAL_GPIO_Init(GPIO_TypeDef  *GPIOx, GPIO_InitTypeDef *GPIO_Init)
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
      if(((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) ||
          (GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Skip hardware-specific configuration for IO Speed */
        /* Skip hardware-specific configuration for IO Output Type */
       }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        /* Skip hardware-specific configuration for Pull-up/Pull-down resistors */
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Skip hardware-specific configuration for Alternate function */
      }

      /* Skip hardware-specific configuration for IO Direction mode */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Enable SYSCFG Clock - keep this as it may be needed for other operations */
        __HAL_RCC_SYSCFG_CLK_ENABLE();

        /* Skip hardware-specific EXTI configuration */
        /* Skip Rising Falling edge configuration */
        /* Skip EXTI line configuration */
      }
    }
  }
}
    原因：Fixed syntax error: replaced double backslash line continuation (\\\) with single backslash or removed line continuation by putting condition on same line. Also removed unnecessary line continuation character entirely since the condition fits on one line.
    时间：

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
- 函数用途/功能描述：Initializes UART hardware for half-duplex mode according to specified parameters in the UART_InitTypeDef structure
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs hardware initialization for UART half-duplex mode, 2) Contains multiple MMIO/register access operations (__HAL_UART_DISABLE, __HAL_UART_ENABLE, CLEAR_BIT, SET_BIT on CR2/CR3 registers), 3) Calls other hardware initialization functions (HAL_UART_MspInit, UART_SetConfig), 4) Sets up peripheral configuration while preserving structure initialization and state management. The function follows the INIT strategy by removing hardware-specific operations while keeping parameter validation, state variable updates, and structure initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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

  /* Skip hardware-specific configuration */
  /* [INIT REMOVED] Disable the peripheral: __HAL_UART_DISABLE(huart); */
  
  /* Skip hardware-specific configuration */
  /* [INIT REMOVED] Set the UART Communication parameters: UART_SetConfig(huart); */
  
  /* Skip hardware-specific configuration */
  /* [INIT REMOVED] Clear bits in CR2 and CR3 registers for half-duplex mode */
  /* [INIT REMOVED] Enable Half-Duplex mode by setting HDSEL bit in CR3 register */
  
  /* Skip hardware-specific configuration */
  /* [INIT REMOVED] Enable the peripheral: __HAL_UART_ENABLE(huart); */

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
- 函数用途/功能描述：Initializes the HAL library by configuring flash cache, setting NVIC priority grouping, configuring SysTick timer, and calling low-level hardware initialization
- 是否需要替换：是
- 分类/替换原因：HAL_Init is a high-level initialization function that sets up the HAL environment. It calls HAL_NVIC_SetPriorityGrouping (CORE function for NVIC configuration), HAL_InitTick (SysTick configuration - not CORE), and HAL_MspInit (user hardware initialization). According to classification rules, functions that call CORE functions can be classified as INIT, and the replacement must preserve calls to NVIC/OS/VTOR primitives. The function contains no direct MMIO operations (GetMMIOFunctionInfo returned empty list), but performs system initialization through function calls. It fits the INIT category as it initializes peripheral/configurations and allocates resources.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_Init(void)
{
  /* Configure Flash prefetch, Instruction cache, Data cache */ 
#if (INSTRUCTION_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache enable operations */
#endif /* INSTRUCTION_CACHE_ENABLE */

#if (DATA_CACHE_ENABLE != 0U)
  /* Skip hardware-specific cache enable operations */
#endif /* DATA_CACHE_ENABLE */

#if (PREFETCH_ENABLE != 0U)
  /* Skip hardware-specific prefetch buffer enable operations */
#endif /* PREFETCH_ENABLE */

  /* Set Interrupt Group Priority - MUST PRESERVE this CORE function call */
  HAL_NVIC_SetPriorityGrouping(NVIC_PRIORITYGROUP_4);

  /* Use systick as time base source and configure 1ms tick (default clock after Reset is HSI) */
  HAL_InitTick(TICK_INT_PRIORITY);

  /* Init the low level hardware */
  HAL_MspInit();

  /* Return function status */
  return HAL_OK;
}
```

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
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization for LIN mode configuration. Analysis of the function code shows it contains multiple MMIO operations accessing UART peripheral registers (CR2, CR3) to configure LIN mode, clear/set control bits, and enable/disable the peripheral. The function also performs non-hardware operations like parameter validation, state management (gState, RxState), lock initialization, and error code setup. It calls HAL_UART_MspInit which may contain further hardware initialization. According to the classification priority, this is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data transmission/reception), not IRQ (not an interrupt handler), and not LOOP (no polling loops). It fits the INIT category as it initializes peripheral configurations.
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

  /* Skip hardware-specific peripheral configuration */
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
- 函数用途/功能描述：Initializes UART peripheral for Multi-Processor mode with address-based wake-up methods
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs hardware initialization of UART peripheral registers for multi-processor mode; 2) Contains direct MMIO register accesses to CR1, CR2, and CR3 registers (confirmed by GetFunctionInfo showing CLEAR_BIT/SET_BIT operations on huart->Instance registers); 3) Configures hardware-specific settings including address node and wake-up method; 4) Sets up the peripheral state machine; 5) Calls HAL_UART_MspInit which may contain NVIC configuration (preserved in replacement); 6) Follows INIT strategy by removing hardware register accesses while preserving structure initialization and state updates.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes the Multi-Processor mode according to the specified
*         parameters in the UART_InitTypeDef and create the associated handle.
* @param  huart  Pointer to a UART_HandleTypeDef structure that contains
*                the configuration information for the specified UART module.
* @param  Address USART address
* @param  WakeUpMethod specifies the USART wake-up method.
*         This parameter can be one of the following values:
*            @arg UART_WAKEUPMETHOD_IDLELINE: Wake-up by an idle line detection
*            @arg UART_WAKEUPMETHOD_ADDRESSMARK: Wake-up by an address mark
* @retval HAL status
*/
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
- 函数用途/功能描述：Configures the main internal regulator output voltage to achieve a tradeoff between performance and power consumption by setting voltage scaling levels.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It's a power management initialization/configuration function that sets up voltage scaling; 2) GetMMIOFunctionInfo revealed multiple hardware register accesses including clock enabling, PLL control, and flag checking operations; 3) It contains polling loops waiting for hardware flags (PLLRDY, VOSRDY) which are characteristic of hardware-dependent initialization; 4) It doesn't involve data transmission/reception (not RECV), isn't an interrupt handler (not IRQ), and doesn't contain NVIC/OS/VTOR operations (not CORE); 5) While it has LOOP characteristics (polling), INIT takes priority in the classification hierarchy as it's primarily a configuration function.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Configures the main internal regulator output voltage.
* @param  VoltageScaling specifies the regulator output voltage to achieve
*         a tradeoff between performance and power consumption.
*          This parameter can be one of the following values:
*            @arg PWR_REGULATOR_VOLTAGE_SCALE1: Regulator voltage output range 1 mode,
*                                               the maximum value of fHCLK is 168 MHz. It can be extended to
*                                               180 MHz by activating the over-drive mode.
*            @arg PWR_REGULATOR_VOLTAGE_SCALE2: Regulator voltage output range 2 mode,
*                                               the maximum value of fHCLK is 144 MHz. It can be extended to,
*                                               168 MHz by activating the over-drive mode.
*            @arg PWR_REGULATOR_VOLTAGE_SCALE3: Regulator voltage output range 3 mode,
*                                               the maximum value of fHCLK is 120 MHz.
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
  /* Parameter validation */
  assert_param(IS_PWR_VOLTAGE_SCALING_RANGE(VoltageScaling));
  
  /* Skip hardware-specific operations:
     - Clock enabling
     - PLL disable/enable
     - Register configuration
     - Polling loops for hardware flags
  */
  
  /* In simulation, we assume the operation succeeds */
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
- 函数用途/功能描述：Disables the Backup Regulator in the power control system
- 是否需要替换：是
- 分类/替换原因：Function performs hardware configuration (disabling backup regulator) with MMIO operations including a bit-band write to disable the regulator and a polling loop waiting for the backup regulator ready flag. It fits the INIT classification as it initializes/configures hardware settings. The function contains both hardware register access (CSR_BRE_BB write) and a polling loop (waiting for PWR_FLAG_BRR), but INIT takes priority over LOOP in the classification hierarchy.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_PWREx_DisableBkUpReg(void)
{
  /* Simulate disabling backup regulator - skip hardware operations */
  /* Skip bit-band write: *(__IO uint32_t *) CSR_BRE_BB = (uint32_t)DISABLE; */
  
  /* Skip polling loop waiting for backup regulator ready flag */
  /* while(__HAL_PWR_GET_FLAG(PWR_FLAG_BRR) != RESET) */
  
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
- 函数类型：LOOP
- 函数用途/功能描述：Enables the Backup Regulator and waits for it to become ready with timeout handling
- 是否需要替换：是
- 分类/替换原因：Function contains a hardware-dependent polling loop (while(__HAL_PWR_GET_FLAG(PWR_FLAG_BRR) == RESET)) that waits for the backup regulator ready flag. According to LOOP classification strategy, polling loops waiting for status flags should be skipped entirely, assuming the condition is already met. The function also performs MMIO write operation to enable the regulator (*(__IO uint32_t *) CSR_BRE_BB = (uint32_t)ENABLE), which should be removed. This is not a CORE function (no NVIC/OS/VTOR operations), not a data transmission/reception function, not an interrupt handler, and while it initializes hardware, its primary characteristic is the polling loop.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Enables the Backup Regulator.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_PWREx_EnableBkUpReg(void)
{
  /* Skip hardware write to enable backup regulator */
  /* [LOOP REMOVED] Skip polling for backup regulator ready flag */
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
- 函数用途/功能描述：Configures the Power Voltage Detector (PVD) by setting voltage threshold levels and configuring interrupt/event modes for power monitoring.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization and configuration for the PVD peripheral. It writes to PWR control registers (PWR->CR) to set voltage detection levels and configures EXTI settings for interrupt/event handling. The function contains MMIO operations (MODIFY_REG on PWR->CR) and hardware-specific configuration macros. It fits the INIT category as it initializes peripheral configurations without performing data transmission/reception, interrupt handling, or polling loops. The function is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), and not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_PWR_ConfigPVD(PWR_PVDTypeDef *sConfigPVD)
{
  /* Check the parameters */
  assert_param(IS_PWR_PVD_LEVEL(sConfigPVD->PVDLevel));
  assert_param(IS_PWR_PVD_MODE(sConfigPVD->Mode));
  
  /* Skip hardware-specific register configuration */
  /* [INIT REMOVED] MODIFY_REG(PWR->CR, PWR_CR_PLS, sConfigPVD->PVDLevel); */
  
  /* Skip EXTI configuration for PVD */
  /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_DISABLE_EVENT(); */
  /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_DISABLE_IT(); */
  /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_DISABLE_RISING_EDGE(); */
  /* [INIT REMOVED] __HAL_PWR_PVD_EXTI_DISABLE_FALLING_EDGE(); */

  /* Skip interrupt mode configuration */
  /* [INIT REMOVED] if((sConfigPVD->Mode & PVD_MODE_IT) == PVD_MODE_IT)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_IT();
  } */
  
  /* Skip event mode configuration */
  /* [INIT REMOVED] if((sConfigPVD->Mode & PVD_MODE_EVT) == PVD_MODE_EVT)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_EVENT();
  } */
  
  /* Skip edge configuration */
  /* [INIT REMOVED] if((sConfigPVD->Mode & PVD_RISING_EDGE) == PVD_RISING_EDGE)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_RISING_EDGE();
  } */
  
  /* [INIT REMOVED] if((sConfigPVD->Mode & PVD_FALLING_EDGE) == PVD_FALLING_EDGE)
  {
    __HAL_PWR_PVD_EXTI_ENABLE_FALLING_EDGE();
  } */
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
- 函数用途/功能描述：Enables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by setting the DBP bit in the power control register.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware register access to enable backup domain access. It writes to CR_DBP_BB (bit-band alias for DBP bit) and reads PWR->CR as a dummy read sequence. This is a hardware configuration/initialization function that sets up peripheral features. It doesn't involve data transmission (RECV), interrupt handling (IRQ), polling loops (LOOP), or core OS/NVIC operations (CORE). The function is classified as INIT because it initializes hardware configuration by enabling backup domain access.
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
  /* Hardware register access removed for simulation */
  /* Original: *(__IO uint32_t *) CR_DBP_BB = (uint32_t)ENABLE; */
  /* Original: dummyread = PWR->CR; */
  /* Backup domain access is considered enabled in simulation */
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
- 函数用途/功能描述：Handles the PWR PVD (Power Voltage Detector) interrupt request by checking the interrupt flag and calling the user callback function.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler (IRQHandler) that checks and clears PWR PVD interrupt flags and calls a user callback. It contains hardware-specific interrupt flag operations that need to be replaced while preserving the callback invocation. The function name clearly indicates it's an interrupt handler, and the implementation shows interrupt flag checking/clearing operations. GetMMIOFunctionInfo showed this function is in the MMIOFunction set, confirming hardware register accesses. The replacement removes hardware flag checking/clearing while preserving the callback execution.
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
  /* Simulate PWR Exti flag being set - always execute callback */
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
- 函数用途/功能描述：Disables the PLLI2S (Phase-Locked Loop for I2S) peripheral and waits for it to be fully disabled.
- 是否需要替换：是
- 分类/替换原因：Function contains a hardware-dependent polling loop that waits for the PLLI2SRDY status flag in the RCC->CR register to clear. GetMMIOFunctionInfo revealed register accesses to RCC->CR. The function calls __HAL_RCC_PLLI2S_DISABLE() (hardware operation) and then polls RCC->CR for status. According to classification priority, LOOP matches because it has a peripheral-dependent loop waiting for status flag. The LOOP strategy is to skip the polling loop entirely and assume the condition is met. This is not CORE (no NVIC/OS/VTOR), not RECV (no data I/O), not IRQ (no interrupt handling), not INIT (it's a disable function, not initialization).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_RCCEx_DisablePLLI2S(void)
{
  uint32_t tickstart;

  /* Disable the PLLI2S */
  /* [HARDWARE REMOVED] __HAL_RCC_PLLI2S_DISABLE(); */

  /* Wait till PLLI2S is disabled */
  tickstart = HAL_GetTick();
  /* [LOOP REMOVED] Skip polling for PLLI2S disable completion */
  /* while (READ_BIT(RCC->CR, RCC_CR_PLLI2SRDY) != RESET)
  {
    if ((HAL_GetTick() - tickstart) > PLLI2S_TIMEOUT_VALUE)
    {
      return HAL_TIMEOUT;
    }
  } */

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
- 函数用途/功能描述：Enables and configures the PLLI2S (Phase-Locked Loop for I2S) peripheral on STM32 microcontrollers
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This function initializes and configures hardware peripheral (PLLI2S) - typical INIT function. 2) Contains MMIO operations through macros like __HAL_RCC_PLLI2S_DISABLE(), __HAL_RCC_PLLI2S_CONFIG(), __HAL_RCC_PLLI2S_ENABLE(). 3) Includes polling loops waiting for hardware status flags (RCC_FLAG_PLLI2SRDY). 4) Performs parameter validation and timeout handling. 5) Not a CORE function (no NVIC/OS/VTOR operations). 6) Not a RECV/IRQ/LOOP function. As an INIT function, hardware operations should be removed while preserving parameter validation and returning success status.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Enable PLLI2S.
* @param  PLLI2SInit  pointer to an RCC_PLLI2SInitTypeDef structure that
*         contains the configuration information for the PLLI2S
* @retval HAL status
*/
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

  /* Skip hardware operations for PLLI2S disable/enable and configuration */
  /* Original: __HAL_RCC_PLLI2S_DISABLE(); */
  /* Original: Wait till PLLI2S is disabled - polling loop removed */
  /* Original: Configure PLLI2S division factors - hardware config removed */
  /* Original: __HAL_RCC_PLLI2S_ENABLE(); */
  /* Original: Wait till PLLI2S is ready - polling loop removed */

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
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This function performs hardware initialization of peripheral clocks (I2S, RTC, TIM). 2) It contains multiple MMIO operations (register accesses to RCC->BDCR, PWR->CR, etc.) and hardware-specific macros. 3) It has polling loops waiting for hardware status flags (PLLI2S ready, DBP flag, LSE ready). 4) It performs parameter validation and configuration but no data transmission/reception. 5) It does not contain any CORE operations (NVIC/OS kernel/VTOR configuration). According to classification priority (CORE > RECV > IRQ > INIT > LOOP > ...), this is primarily an INIT function with LOOP elements, so classified as INIT.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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
    
    /* [INIT REPLACEMENT] Skip hardware PLLI2S configuration */
  }

  /*---------------------------- RTC configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_RTC) == (RCC_PERIPHCLK_RTC))
  {
    /* Check for RTC Parameters used to output RTCCLK */
    assert_param(IS_RCC_RTCCLKSOURCE(PeriphClkInit->RTCClockSelection));
    
    /* [INIT REPLACEMENT] Skip hardware RTC configuration */
  }
  
#if defined(STM32F401xC) || defined(STM32F401xE) || defined(STM32F411xE)
  /*---------------------------- TIM configuration ---------------------------*/
  if (((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_TIM) == (RCC_PERIPHCLK_TIM))
  {
    /* [INIT REPLACEMENT] Skip hardware TIM prescaler configuration */
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
- 函数用途/功能描述：Initializes CPU, AHB and APB bus clocks according to specified parameters including system clock source, dividers, and flash latency
- 是否需要替换：否
- 分类/替换原因：GetFunctionInfo revealed this is a clock configuration initialization function. GetMMIOFunctionInfo showed multiple hardware register accesses (RCC->CFGR modifications, flash latency configuration, clock ready flag checks, and polling loops). The function contains hardware-dependent operations that need to be removed while preserving parameter validation, logical flow, and the call to HAL_InitTick (which handles SysTick configuration). This is classified as INIT rather than LOOP because its primary purpose is initialization, though it contains a polling loop for clock switch completion. According to priority order (CORE > RECV > IRQ > INIT > LOOP), INIT takes precedence over LOOP.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

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

    /* Wait for system clock switch to complete */
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
- 更新原因：Restored original function structure with hardware operations to ensure emulator sees SysTick configuration sequence. The emulator requires monitoring of RCC register writes and SysTick configuration for proper simulation. This preserves the exact call to HAL_InitTick(uwTickPrio) and maintains the logical flow that the emulator expects.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
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

    /* Wait for system clock switch to complete */
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
    原因：Restored original function structure with hardware operations to ensure emulator sees SysTick configuration sequence. The emulator requires monitoring of RCC register writes and SysTick configuration for proper simulation. This preserves the exact call to HAL_InitTick(uwTickPrio) and maintains the logical flow that the emulator expects.
    时间：

=== 信息结束 ===
```

### HAL_RCC_GetClockConfig

```text
=== HAL_RCC_GetClockConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_rcc.c
- 行号：1058
- 函数内容：void HAL_RCC_GetClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t *pFLatency)
{
  /* Set all possible values for the Clock type parameter --------------------*/
  RCC_ClkInitStruct->ClockType = RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;

  /* Get the SYSCLK configuration --------------------------------------------*/
  RCC_ClkInitStruct->SYSCLKSource = (uint32_t)(RCC->CFGR & RCC_CFGR_SW);

  /* Get the HCLK configuration ----------------------------------------------*/
  RCC_ClkInitStruct->AHBCLKDivider = (uint32_t)(RCC->CFGR & RCC_CFGR_HPRE);

  /* Get the APB1 configuration ----------------------------------------------*/
  RCC_ClkInitStruct->APB1CLKDivider = (uint32_t)(RCC->CFGR & RCC_CFGR_PPRE1);

  /* Get the APB2 configuration ----------------------------------------------*/
  RCC_ClkInitStruct->APB2CLKDivider = (uint32_t)((RCC->CFGR & RCC_CFGR_PPRE2) >> 3U);

  /* Get the Flash Wait State (Latency) configuration ------------------------*/
  *pFLatency = (uint32_t)(FLASH->ACR & FLASH_ACR_LATENCY);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Reads current clock configuration from RCC and FLASH peripheral registers and populates an RCC_ClkInitTypeDef structure with the configuration.
- 是否需要替换：是
- 分类/替换原因：Function reads hardware registers (RCC->CFGR and FLASH->ACR) to retrieve current clock configuration. It is classified as INIT because: 1) It is related to system clock configuration which is part of initialization domain, 2) It reads hardware registers that were set during system initialization, 3) In simulation, we need to provide reasonable default values for clock configuration. The function populates a data structure with configuration values that other parts of the system may depend on, so it cannot be skipped or treated as RETURNOK. The replacement removes MMIO register accesses and provides simulated default values for clock configuration (assuming HSI clock source, no clock division, and zero flash wait states).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Configures the RCC_ClkInitStruct according to the internal
* RCC configuration registers.
* @param  RCC_ClkInitStruct pointer to an RCC_ClkInitTypeDef structure that
* will be configured.
* @param  pFLatency Pointer on the Flash Latency.
* @retval None
*/
void HAL_RCC_GetClockConfig(RCC_ClkInitTypeDef  *RCC_ClkInitStruct, uint32_t *pFLatency)
{
  /* Set all possible values for the Clock type parameter --------------------*/
  RCC_ClkInitStruct->ClockType = RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;

  /* Get the SYSCLK configuration --------------------------------------------*/
  /* Simulated value: Assume HSI as system clock source */
  RCC_ClkInitStruct->SYSCLKSource = RCC_SYSCLKSOURCE_HSI;

  /* Get the HCLK configuration ----------------------------------------------*/
  /* Simulated value: Assume no division (AHB clock = SYSCLK) */
  RCC_ClkInitStruct->AHBCLKDivider = RCC_SYSCLK_DIV1;

  /* Get the APB1 configuration ----------------------------------------------*/
  /* Simulated value: Assume no division (APB1 clock = HCLK) */
  RCC_ClkInitStruct->APB1CLKDivider = RCC_HCLK_DIV1;

  /* Get the APB2 configuration ----------------------------------------------*/
  /* Simulated value: Assume no division (APB2 clock = HCLK) */
  RCC_ClkInitStruct->APB2CLKDivider = RCC_HCLK_DIV1;

  /* Get the Flash Wait State (Latency) configuration ------------------------*/
  /* Simulated value: Assume zero wait states */
  *pFLatency = FLASH_LATENCY_0;
}
```

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
- 函数用途/功能描述：Configures the Microcontroller Clock Output (MCO) pins to output various clock sources (HSI, LSE, HSE, PLL, etc.) with configurable prescalers.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a peripheral configuration function that sets up MCO clock output. GetMMIOFunctionInfo identified register writes to RCC->CFGR for clock source selection and prescaler configuration. The function performs GPIO initialization for MCO pins and contains hardware-specific register operations. It is classified as INIT because: 1) It initializes/configure peripheral hardware (MCO output), 2) Contains MMIO register writes that need to be removed, 3) No data transmission/reception (not RECV), 4) No interrupt handling (not IRQ), 5) No polling loops (not LOOP), 6) Not core OS/NVIC functionality (not CORE). The replacement follows INIT strategy by removing all hardware-specific operations while preserving parameter validation and conditional logic structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Selects the clock source to output on MCO1 pin(PA8) or on MCO2 pin(PC9).
* @note   PA8/PC9 should be configured in alternate function mode.
* @param  RCC_MCOx specifies the output direction for the clock source.
*          This parameter can be one of the following values:
*            @arg RCC_MCO1: Clock source to output on MCO1 pin(PA8).
*            @arg RCC_MCO2: Clock source to output on MCO2 pin(PC9).
* @param  RCC_MCOSource specifies the clock source to output.
*          This parameter can be one of the following values:
*            @arg RCC_MCO1SOURCE_HSI: HSI clock selected as MCO1 source
*            @arg RCC_MCO1SOURCE_LSE: LSE clock selected as MCO1 source
*            @arg RCC_MCO1SOURCE_HSE: HSE clock selected as MCO1 source
*            @arg RCC_MCO1SOURCE_PLLCLK: main PLL clock selected as MCO1 source
*            @arg RCC_MCO2SOURCE_SYSCLK: System clock (SYSCLK) selected as MCO2 source
*            @arg RCC_MCO2SOURCE_PLLI2SCLK: PLLI2S clock selected as MCO2 source, available for all STM32F4 devices except STM32F410xx
*            @arg RCC_MCO2SOURCE_I2SCLK: I2SCLK clock selected as MCO2 source, available only for STM32F410Rx devices
*            @arg RCC_MCO2SOURCE_HSE: HSE clock selected as MCO2 source
*            @arg RCC_MCO2SOURCE_PLLCLK: main PLL clock selected as MCO2 source
* @param  RCC_MCODiv specifies the MCOx prescaler.
*          This parameter can be one of the following values:
*            @arg RCC_MCODIV_1: no division applied to MCOx clock
*            @arg RCC_MCODIV_2: division by 2 applied to MCOx clock
*            @arg RCC_MCODIV_3: division by 3 applied to MCOx clock
*            @arg RCC_MCODIV_4: division by 4 applied to MCOx clock
*            @arg RCC_MCODIV_5: division by 5 applied to MCOx clock
* @note  For STM32F410Rx devices to output I2SCLK clock on MCO2 you should have
*        at last one of the SPI clocks enabled (SPI1, SPI2 or SPI5).
* @retval None
*/
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

    /* Skip hardware-specific MCO1 configuration */
    /* Original: __MCO1_CLK_ENABLE(); */
    /* Original: Configure MCO1 pin in alternate function mode */
    /* Original: MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO1 | RCC_CFGR_MCO1PRE), (RCC_MCOSource | RCC_MCODiv)); */
    /* Original: __HAL_RCC_MCO1_ENABLE(); */

  }
#if defined(RCC_CFGR_MCO2)
  else
  {
    assert_param(IS_RCC_MCO2SOURCE(RCC_MCOSource));

    /* Skip hardware-specific MCO2 configuration */
    /* Original: __MCO2_CLK_ENABLE(); */
    /* Original: Configure MCO2 pin in alternate function mode */
    /* Original: MODIFY_REG(RCC->CFGR, (RCC_CFGR_MCO2 | RCC_CFGR_MCO2PRE), (RCC_MCOSource | (RCC_MCODiv << 3U))); */
    /* Original: __HAL_RCC_MCO2_ENABLE(); */
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
- 函数用途/功能描述：Interrupt handler for RCC Clock Security System (CSS) interrupt request, checks CSS flag and calls user callback
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler as indicated by its name '_IRQHandler' and its purpose of handling RCC CSS interrupts. It checks hardware interrupt flags using __HAL_RCC_GET_IT(RCC_IT_CSS), calls a user callback HAL_RCC_CSSCallback(), and clears interrupt flags with __HAL_RCC_CLEAR_IT(RCC_IT_CSS). Although GetMMIOFunctionInfo returned no explicit MMIO expressions, the macros likely hide register accesses to RCC peripheral. As an IRQ function, it should have hardware operations removed while preserving the callback invocation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_RCC_NMI_IRQHandler(void)
{
  /* Simulate CSS interrupt being triggered */
  /* Always call the user callback to preserve functionality */
  HAL_RCC_CSSCallback();
  
  /* Skip hardware interrupt flag checking and clearing */
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
- 函数用途/功能描述：De-initializes the SPI peripheral by disabling hardware and resetting state variables
- 是否需要替换：是
- 分类/替换原因：This function performs peripheral de-initialization operations including disabling the SPI peripheral clock and calling low-level hardware de-initialization (which may include NVIC operations). GetFunctionInfo shows it contains __HAL_SPI_DISABLE(hspi) which likely performs MMIO operations, and calls HAL_SPI_MspDeInit for hardware cleanup. While GetMMIOFunctionInfo returned empty, the function clearly performs hardware de-initialization. It doesn't fit RECV (no data transfer), IRQ (not an interrupt handler), LOOP (no polling), or CORE (not NVIC/OS kernel functions). De-initialization is the inverse of initialization, so INIT classification is appropriate. The replacement code removes the hardware-specific __HAL_SPI_DISABLE call while preserving all other logic including the call to HAL_SPI_MspDeInit which may contain NVIC operations that should be preserved.
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

  /* Skip disabling SPI peripheral clock (hardware operation) */
  /* __HAL_SPI_DISABLE(hspi); */

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
- 函数用途/功能描述：Initializes the SPI peripheral according to specified parameters in SPI_InitTypeDef and initializes the associated handle structure
- 是否需要替换：是
- 分类/替换原因：Function performs SPI peripheral initialization with multiple hardware register writes (MMIO operations) including disabling SPI, configuring control registers CR1/CR2, CRC polynomial register, and clearing I2S mode bit. It calls HAL_SPI_MspInit which may contain NVIC configuration (CORE operations). According to classification priority, this is an INIT type function that initializes peripheral configurations and should have hardware operations removed while preserving structure initialization, state updates, and calls to potentially CORE functions.
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
  /* Original: Disable the selected SPI peripheral - __HAL_SPI_DISABLE(hspi); */
  /* Original: Configure SPI registers - WRITE_REG operations removed */

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
- 函数类型：INIT
- 函数用途/功能描述：Initializes hardware resources for TIM (Timer) Base peripherals by enabling their clocks
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a TIM Base MSP initialization function that enables peripheral clocks for various TIM instances (TIM1, TIM2, TIM3, TIM4, TIM9, TIM11). GetMMIOFunctionInfo confirmed MMIO operations (register accesses) through __HAL_RCC_TIMx_CLK_ENABLE() macros. The function contains no NVIC configuration, OS-related calls, or VTOR operations, so it is not CORE. It's not a data reception/transmission function (RECV), not an interrupt handler (IRQ), and doesn't contain polling loops (LOOP). It's clearly an initialization function that sets up hardware resources, making INIT the appropriate classification. The replacement removes hardware-specific clock enable operations while preserving the conditional structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_TIM_Base_MspInit(TIM_HandleTypeDef* htim_base)
{
  if(htim_base->Instance==TIM1)
  {
  /* USER CODE BEGIN TIM1_MspInit 0 */

  /* USER CODE END TIM1_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
  /* USER CODE BEGIN TIM1_MspInit 1 */

  /* USER CODE END TIM1_MspInit 1 */
  }
  else if(htim_base->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspInit 0 */

  /* USER CODE END TIM2_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
  /* USER CODE BEGIN TIM2_MspInit 1 */

  /* USER CODE END TIM2_MspInit 1 */
  }
  else if(htim_base->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspInit 0 */

  /* USER CODE END TIM3_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
  /* USER CODE BEGIN TIM3_MspInit 1 */

  /* USER CODE END TIM3_MspInit 1 */
  }
  else if(htim_base->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspInit 0 */

  /* USER CODE END TIM4_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
  /* USER CODE BEGIN TIM4_MspInit 1 */

  /* USER CODE END TIM4_MspInit 1 */
  }
  else if(htim_base->Instance==TIM9)
  {
  /* USER CODE BEGIN TIM9_MspInit 0 */

  /* USER CODE END TIM9_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
  /* USER CODE BEGIN TIM9_MspInit 1 */

  /* USER CODE END TIM9_MspInit 1 */
  }
  else if(htim_base->Instance==TIM11)
  {
  /* USER CODE BEGIN TIM11_MspInit 0 */

  /* USER CODE END TIM11_MspInit 0 */
    /* Peripheral clock enable - REMOVED FOR EMULATION */
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
- 函数用途/功能描述：Post-initialization function for TIM peripheral that configures GPIO pins for TIM alternate functions
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is a TIM post-initialization function that configures GPIO pins for TIM channels. GetMMIOFunctionInfo reveals hardware register accesses through __HAL_RCC_GPIOx_CLK_ENABLE() calls and GPIO configuration. GetFunctionCallStack shows it calls HAL_GPIO_Init. This is an initialization function that sets up hardware configuration for TIM peripheral GPIO pins. According to classification priority: it's not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), not LOOP (no polling loops). It's an INIT function that should have hardware operations removed while preserving the logical structure and conditional branches.
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
    /* __HAL_RCC_GPIOA_CLK_ENABLE(); */ /* Hardware operation removed */
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
    /* HAL_GPIO_Init(GPIOA, &GPIO_InitStruct); */ /* Hardware operation removed */

  /* USER CODE BEGIN TIM1_MspPostInit 1 */

  /* USER CODE END TIM1_MspPostInit 1 */
  }
  else if(htim->Instance==TIM2)
  {
  /* USER CODE BEGIN TIM2_MspPostInit 0 */

  /* USER CODE END TIM2_MspPostInit 0 */

    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */ /* Hardware operation removed */
    /**TIM2 GPIO Configuration
    PB10     ------> TIM2_CH3
    PB3     ------> TIM2_CH2
    */
    GPIO_InitStruct.Pin = GPIO_PIN_10|GPIO_PIN_3;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF1_TIM2;
    /* HAL_GPIO_Init(GPIOB, &GPIO_InitStruct); */ /* Hardware operation removed */

  /* USER CODE BEGIN TIM2_MspPostInit 1 */

  /* USER CODE END TIM2_MspPostInit 1 */
  }
  else if(htim->Instance==TIM3)
  {
  /* USER CODE BEGIN TIM3_MspPostInit 0 */

  /* USER CODE END TIM3_MspPostInit 0 */

    /* __HAL_RCC_GPIOC_CLK_ENABLE(); */ /* Hardware operation removed */
    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */ /* Hardware operation removed */
    /**TIM3 GPIO Configuration
    PC7     ------> TIM3_CH2
    PB4     ------> TIM3_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    /* HAL_GPIO_Init(GPIOC, &GPIO_InitStruct); */ /* Hardware operation removed */

    GPIO_InitStruct.Pin = GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    /* HAL_GPIO_Init(GPIOB, &GPIO_InitStruct); */ /* Hardware operation removed */

  /* USER CODE BEGIN TIM3_MspPostInit 1 */

  /* USER CODE END TIM3_MspPostInit 1 */
  }
  else if(htim->Instance==TIM4)
  {
  /* USER CODE BEGIN TIM4_MspPostInit 0 */

  /* USER CODE END TIM4_MspPostInit 0 */

    /* __HAL_RCC_GPIOB_CLK_ENABLE(); */ /* Hardware operation removed */
    /**TIM4 GPIO Configuration
    PB6     ------> TIM4_CH1
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM4;
    /* HAL_GPIO_Init(GPIOB, &GPIO_InitStruct); */ /* Hardware operation removed */

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
- 函数用途/功能描述：Deinitializes the UART peripheral by disabling hardware, calling low-level deinitialization, and resetting the UART handle state.
- 是否需要替换：是
- 分类/替换原因：HAL_UART_DeInit is a deinitialization function that performs hardware deconfiguration operations. Analysis shows: 1) It calls __HAL_UART_DISABLE(huart) which likely performs MMIO operations to disable the peripheral, 2) It calls HAL_UART_MspDeInit for low-level hardware deinitialization, 3) It resets software state variables (ErrorCode, gState, RxState, etc.), 4) It doesn't fit other categories: not RECV (no data I/O), not IRQ (no interrupt handling), not LOOP (no polling), not CORE (no NVIC/OS kernel/VTOR operations). As an INIT-type function, the replacement strategy is to remove MMIO operations while preserving state management and callback calls.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  DeInitializes the UART peripheral.
* @param  huart  Pointer to a UART_HandleTypeDef structure that contains
*                the configuration information for the specified UART module.
* @retval HAL status
*/
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
  /* DeInit the low level hardware - preserve callback call */
  huart->MspDeInitCallback(huart);
#else
  /* DeInit the low level hardware - preserve callback call */
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
- 更新代码：void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
    /* In emulation, we don't process real hardware interrupts.
       This function is called from uart_isr when DMA TX is enabled.
       We'll simply return without doing anything to avoid
       getting stuck in hardware flag checking loops. */
    
    /* Prevent unused parameter warning */
    (void)huart;
    
    /* No hardware processing in emulation */
    return;
}
- 更新原因：Prevent potential exceptional loops in UART interrupt handling. The original HAL_UART_IRQHandler reads hardware registers (Instance->SR, Instance->CR1, Instance->CR3) and checks various flags which may not be properly simulated in emulation. This could lead to infinite loops or incorrect state transitions. Since we're already handling UART interrupts through uart_isr replacement, this function should do nothing in emulation to avoid hardware dependency issues.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
    /* In emulation, we don't process real hardware interrupts.
       This function is called from uart_isr when DMA TX is enabled.
       We'll simply return without doing anything to avoid
       getting stuck in hardware flag checking loops. */
    
    /* Prevent unused parameter warning */
    (void)huart;
    
    /* No hardware processing in emulation */
    return;
}
    原因：Prevent potential exceptional loops in UART interrupt handling. The original HAL_UART_IRQHandler reads hardware registers (Instance->SR, Instance->CR1, Instance->CR3) and checks various flags which may not be properly simulated in emulation. This could lead to infinite loops or incorrect state transitions. Since we're already handling UART interrupts through uart_isr replacement, this function should do nothing in emulation to avoid hardware dependency issues.
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
- 函数用途/功能描述：Initializes the UART peripheral according to specified parameters in UART_InitTypeDef and creates the associated handle
- 是否需要替换：是
- 分类/替换原因：This function is a UART initialization function that configures peripheral hardware. Analysis shows it: 1) Contains hardware register accesses (disabling/enabling peripheral via __HAL_UART_DISABLE/ENABLE macros, clearing CR2/CR3 register bits via CLEAR_BIT macros), 2) Calls other hardware configuration functions (UART_SetConfig, HAL_UART_MspInit), 3) Sets up the UART handle state variables. GetMMIOFunctionInfo indicated hardware dependencies, and GetFunctionCallStack shows it's called by stm32_configure for UART setup. It fits the INIT classification as it performs peripheral initialization with MMIO operations that need to be removed while preserving structure initialization and state setup.
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
  /* Original: Disable the peripheral - __HAL_UART_DISABLE(huart); */
  /* Original: Set the UART Communication parameters - UART_SetConfig(huart); */
  /* Original: Clear bits in CR2 and CR3 registers */
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
- 函数用途/功能描述：Configures the system clock, PLL, and bus clocks for STM32 microcontroller initialization
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs system clock initialization by configuring RCC (Reset and Clock Control) peripheral settings. Analysis shows: 1) It initializes clock configuration structures (RCC_OscInitTypeDef and RCC_ClkInitTypeDef), 2) It contains MMIO operations for hardware register access (confirmed by GetMMIOFunctionInfo), 3) It calls hardware-specific functions like __HAL_RCC_PWR_CLK_ENABLE(), __HAL_PWR_VOLTAGESCALING_CONFIG(), HAL_RCC_OscConfig(), and HAL_RCC_ClockConfig(), 4) It's called from rt_hw_board_init during board initialization, 5) It doesn't fit other classifications: not CORE (no NVIC/OS/VTOR operations), not RECV/IRQ/LOOP, not RETURNOK/SKIP/NEEDCHECK/NODRIVER. As an INIT function, hardware operations should be removed while preserving structure initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  /* Hardware-specific operations removed for emulation */
  
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
  
  /* Skip hardware configuration, assume success */
  
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  /* Skip hardware clock configuration, assume success */
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
- 函数用途/功能描述：Updates the SystemCoreClock global variable based on current clock register values to provide the core clock frequency for system timing
- 是否需要替换：是
- 分类/替换原因：Function reads hardware registers (RCC->CFGR, RCC->PLLCFGR) to determine current clock configuration and updates SystemCoreClock variable. This is critical for system timing (SysTick, etc.). In simulation, we need to provide a reasonable default value since actual hardware registers cannot be read. The function is called by rt_hw_systick_init for SysTick configuration. It doesn't fit CORE (no NVIC/OS operations), RECV/IRQ (not data transfer/interrupt), or LOOP (no polling loops) categories.
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
  /* In simulation, assume PLL is used with default configuration */
  /* Default configuration for STM32F401: HSI = 16MHz, PLL_M = 16, PLL_N = 336, PLL_P = 4 */
  /* SystemCoreClock = (HSI_VALUE / PLL_M) * PLL_N / PLL_P = (16MHz / 16) * 336 / 4 = 84MHz */
  
  /* Skip hardware register reads */
  SystemCoreClock = 84000000; /* 84 MHz default for STM32F401 */
  
  /* Skip HCLK prescaler calculation (assume HPRE = 1, no division) */
  /* SystemCoreClock remains unchanged */
}
```

=== 信息结束 ===
```

### UART_Receive_IT

```text
=== UART_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/rt-thread/bsp/stm32/stm32f401-st-nucleo/packages/stm32f4_hal_driver-latest/Src/stm32f4xx_hal_uart.c
- 行号：3594
- 函数内容：static HAL_StatusTypeDef UART_Receive_IT(UART_HandleTypeDef *huart)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;

  /* Check that a Rx process is ongoing */
  if (huart->RxState == HAL_UART_STATE_BUSY_RX)
  {
    if ((huart->Init.WordLength == UART_WORDLENGTH_9B) && (huart->Init.Parity == UART_PARITY_NONE))
    {
      pdata8bits  = NULL;
      pdata16bits = (uint16_t *) huart->pRxBuffPtr;
      *pdata16bits = (uint16_t)(huart->Instance->DR & (uint16_t)0x01FF);
      huart->pRxBuffPtr += 2U;
    }
    else
    {
      pdata8bits = (uint8_t *) huart->pRxBuffPtr;
      pdata16bits  = NULL;

      if ((huart->Init.WordLength == UART_WORDLENGTH_9B) || ((huart->Init.WordLength == UART_WORDLENGTH_8B) && (huart->Init.Parity == UART_PARITY_NONE)))
      {
        *pdata8bits = (uint8_t)(huart->Instance->DR & (uint8_t)0x00FF);
      }
      else
      {
        *pdata8bits = (uint8_t)(huart->Instance->DR & (uint8_t)0x007F);
      }
      huart->pRxBuffPtr += 1U;
    }

    if (--huart->RxXferCount == 0U)
    {
      /* Disable the UART Data Register not empty Interrupt */
      __HAL_UART_DISABLE_IT(huart, UART_IT_RXNE);

      /* Disable the UART Parity Error Interrupt */
      __HAL_UART_DISABLE_IT(huart, UART_IT_PE);

      /* Disable the UART Error Interrupt: (Frame error, noise error, overrun error) */
      __HAL_UART_DISABLE_IT(huart, UART_IT_ERR);

      /* Rx process is completed, restore huart->RxState to Ready */
      huart->RxState = HAL_UART_STATE_READY;

      /* Initialize type of RxEvent to Transfer Complete */
      huart->RxEventType = HAL_UART_RXEVENT_TC;

      /* Check current reception Mode :
         If Reception till IDLE event has been selected : */
      if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
      {
        /* Set reception type to Standard */
        huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

        /* Disable IDLE interrupt */
        ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);

        /* Check if IDLE flag is set */
        if (__HAL_UART_GET_FLAG(huart, UART_FLAG_IDLE))
        {
          /* Clear IDLE flag in ISR */
          __HAL_UART_CLEAR_IDLEFLAG(huart);
        }

#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
        /*Call registered Rx Event callback*/
        huart->RxEventCallback(huart, huart->RxXferSize);
#else
        /*Call legacy weak Rx Event callback*/
        HAL_UARTEx_RxEventCallback(huart, huart->RxXferSize);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
      }
      else
      {
        /* Standard reception API called */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
        /*Call registered Rx complete callback*/
        huart->RxCpltCallback(huart);
#else
        /*Call legacy weak Rx complete callback*/
        HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
      }

      return HAL_OK;
    }
    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【替换更新】
- 更新代码：static HAL_StatusTypeDef UART_Receive_IT(UART_HandleTypeDef *huart)
{
    /* In emulation, we don't have real hardware data registers.
       This function is called from HAL_UART_IRQHandler when RXNE flag is set.
       Since we're not processing real hardware interrupts in emulation,
       we'll just return HAL_OK to indicate success without actually
       reading from hardware registers. */
    
    /* Prevent unused parameter warning */
    (void)huart;
    
    /* Return success without hardware access */
    return HAL_OK;
}
- 更新原因：Prevent hardware access in emulation. The original UART_Receive_IT function reads from hardware data register (huart->Instance->DR) which doesn't exist in emulation. This could cause crashes or incorrect behavior. Since we're simulating UART interrupts through uart_isr replacement, this function should simply return success without accessing hardware.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static HAL_StatusTypeDef UART_Receive_IT(UART_HandleTypeDef *huart)
{
    /* In emulation, we don't have real hardware data registers.
       This function is called from HAL_UART_IRQHandler when RXNE flag is set.
       Since we're not processing real hardware interrupts in emulation,
       we'll just return HAL_OK to indicate success without actually
       reading from hardware registers. */
    
    /* Prevent unused parameter warning */
    (void)huart;
    
    /* Return success without hardware access */
    return HAL_OK;
}
    原因：Prevent hardware access in emulation. The original UART_Receive_IT function reads from hardware data register (huart->Instance->DR) which doesn't exist in emulation. This could cause crashes or incorrect behavior. Since we're simulating UART interrupts through uart_isr replacement, this function should simply return success without accessing hardware.
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
- 函数用途/功能描述：Initializes GPIO hardware by enabling clock for various GPIO ports and registers the pin device with RT-Thread OS
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a hardware initialization function that enables GPIO port clocks using __HAL_RCC_GPIOx_CLK_ENABLE() macros and registers a pin device driver. GetMMIOFunctionInfo confirmed hardware register accesses for clock enable operations. GetFunctionCallStack shows it's called by rt_hw_board_init during system initialization. This function fits the INIT classification as it performs peripheral initialization and resource setup, contains MMIO operations that need removal, and preserves the device registration logic. It is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), and not LOOP (no peripheral-dependent loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
int rt_hw_pin_init(void)
{
    // Remove all hardware-specific clock enable operations
    // Preserve the device registration logic
    
    return rt_device_pin_register("pin", &_stm32_pin_ops, RT_NULL);
}
```

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

    /* In emulation, we don't have real hardware flags.
       We'll simulate a simple RX event to keep the system running.
       This prevents getting stuck in exceptional loops due to
       missing or incorrectly simulated hardware flags. */
    
    /* Simulate RX event to keep data flow */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_RX_IND);
    
    /* Also simulate TX done event if needed */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_TX_DONE);
}
- 更新原因：Fix exceptional loop in UART interrupt handler. The original uart_isr function reads hardware flags (__HAL_UART_GET_FLAG) which may not behave correctly in emulation, potentially causing infinite loops or incorrect state transitions. In emulation, we need to provide simulated events to keep the serial subsystem running without getting stuck. This replacement provides basic RX and TX event simulation to prevent the exceptional loop error observed in the idle thread.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_isr(struct rt_serial_device *serial)
{
    struct stm32_uart *uart;

    RT_ASSERT(serial != RT_NULL);
    uart = rt_container_of(serial, struct stm32_uart, serial);

    /* In emulation, we don't have real hardware flags.
       We'll simulate a simple RX event to keep the system running.
       This prevents getting stuck in exceptional loops due to
       missing or incorrectly simulated hardware flags. */
    
    /* Simulate RX event to keep data flow */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_RX_IND);
    
    /* Also simulate TX done event if needed */
    rt_hw_serial_isr(serial, RT_SERIAL_EVENT_TX_DONE);
}
    原因：Fix exceptional loop in UART interrupt handler. The original uart_isr function reads hardware flags (__HAL_UART_GET_FLAG) which may not behave correctly in emulation, potentially causing infinite loops or incorrect state transitions. In emulation, we need to provide simulated events to keep the serial subsystem running without getting stuck. This replacement provides basic RX and TX event simulation to prevent the exceptional loop error observed in the idle thread.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**50** 个；CodeQL `MMIOFunction`：**50** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **20** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `HAL_ADC_MspDeInit` | INIT | True | ADC MSP (Microcontroller Specific Package) de-initialization function that disables peripheral clock and de-initializ... |
| `HAL_ADC_MspInit` | INIT | True | ADC MSP initialization function that configures hardware resources including peripheral clocks and GPIO pins for ADC ... |
| `HAL_DMAEx_MultiBufferStart_IT` | INIT | True | Starts multi-buffer DMA transfer with interrupt enabled, configuring DMA for double buffering mode and enabling inter... |
| `HAL_DeInit` | INIT | True | De-initializes common HAL components and resets peripheral buses (APB1, APB2, AHB1, AHB2, AHB3), then calls HAL_MspDe... |
| `HAL_GPIO_DeInit` | RETURNOK | False | De-initializes GPIO peripheral registers to their default reset values, clearing mode, output type, speed, pull-up/do... |
| `HAL_GPIO_EXTI_IRQHandler` | IRQ | True | Handles EXTI (External Interrupt) interrupt requests for GPIO pins by checking interrupt flags, clearing them, and ca... |
| `HAL_GPIO_Init` | INIT | True | Initializes GPIO pins according to specified configuration parameters including mode, speed, pull-up/down resistors, ... |
| `HAL_GPIO_LockPin` | RETURNOK | False | Locks GPIO pin configuration registers to prevent further modification until the next reset |
| `HAL_GPIO_ReadPin` | RETURNOK | False | Reads the state of a specific GPIO pin by accessing the GPIO peripheral's Input Data Register (IDR). |
| `HAL_GPIO_TogglePin` | RETURNOK | False | Toggles the state of specified GPIO pins by reading the current output state and writing to the bit set/reset register |
| `HAL_GPIO_WritePin` | RETURNOK | False | Sets or clears a GPIO pin by writing to the GPIO BSRR (Bit Set/Reset Register) |
| `HAL_HalfDuplex_Init` | INIT | True | Initializes UART hardware for half-duplex mode according to specified parameters in the UART_InitTypeDef structure |
| `HAL_Init` | INIT | True | Initializes the HAL library by configuring flash cache, setting NVIC priority grouping, configuring SysTick timer, an... |
| `HAL_LIN_Init` | INIT | True | Initializes the LIN (Local Interconnect Network) mode for a UART peripheral according to specified parameters includi... |
| `HAL_MultiProcessor_Init` | INIT | True | Initializes UART peripheral for Multi-Processor mode with address-based wake-up methods |
| `HAL_PWREx_ControlVoltageScaling` | INIT | True | Configures the main internal regulator output voltage to achieve a tradeoff between performance and power consumption... |
| `HAL_PWREx_DisableBkUpReg` | INIT | True | Disables the Backup Regulator in the power control system |
| `HAL_PWREx_EnableBkUpReg` | LOOP | True | Enables the Backup Regulator and waits for it to become ready with timeout handling |
| `HAL_PWREx_GetVoltageRange` | RETURNOK | False | Reads and returns the voltage scaling range (VOS bit field) from the PWR control register |
| `HAL_PWR_ConfigPVD` | INIT | True | Configures the Power Voltage Detector (PVD) by setting voltage threshold levels and configuring interrupt/event modes... |
| `HAL_PWR_DeInit` | RETURNOK | False | Deinitializes the HAL PWR peripheral registers to their default reset values by forcing and releasing reset through R... |
| `HAL_PWR_DisableBkUpAccess` | RETURNOK | False | Disables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by clearing the DBP b... |
| `HAL_PWR_DisableWakeUpPin` | RETURNOK | False | Disables the wake-up pin functionality for power management by clearing the corresponding bit in the PWR control/stat... |
| `HAL_PWR_EnableBkUpAccess` | INIT | True | Enables access to the backup domain (RTC registers, RTC backup data registers and backup SRAM) by setting the DBP bit... |
| `HAL_PWR_EnableWakeUpPin` | RETURNOK | False | Enables wake-up pin functionality by setting bits in the PWR control/status register |
| `HAL_PWR_EnterSTANDBYMode` | CORE | False | Puts the microcontroller into Standby low-power mode by configuring power control registers and executing WFI instruc... |
| `HAL_PWR_EnterSTOPMode` | CORE | False | Enters the microcontroller into STOP low-power mode by configuring power regulator settings and using WFI/WFE instruc... |
| `HAL_PWR_PVD_IRQHandler` | IRQ | True | Handles the PWR PVD (Power Voltage Detector) interrupt request by checking the interrupt flag and calling the user ca... |
| `HAL_RCCEx_DisablePLLI2S` | LOOP | True | Disables the PLLI2S (Phase-Locked Loop for I2S) peripheral and waits for it to be fully disabled. |
| `HAL_RCCEx_EnablePLLI2S` | INIT | True | Enables and configures the PLLI2S (Phase-Locked Loop for I2S) peripheral on STM32 microcontrollers |
| `HAL_RCCEx_GetPeriphCLKConfig` | INIT | False | Reads peripheral clock configuration from RCC hardware registers and populates a configuration structure |
| `HAL_RCCEx_GetPeriphCLKFreq` | RETURNOK | False | Reads RCC hardware registers to calculate and return clock frequency for specific peripherals (currently only I2S) |
| `HAL_RCCEx_PeriphCLKConfig` | INIT | True | Initializes extended peripheral clocks (I2S, RTC, TIM) according to specified configuration parameters in RCC_PeriphC... |
| `HAL_RCC_ClockConfig` | INIT | False | Initializes CPU, AHB and APB bus clocks according to specified parameters including system clock source, dividers, an... |
| `HAL_RCC_GetClockConfig` | INIT | True | Reads current clock configuration from RCC and FLASH peripheral registers and populates an RCC_ClkInitTypeDef structu... |
| `HAL_RCC_GetPCLK1Freq` | RETURNOK | False | Returns the PCLK1 (APB1 peripheral clock) frequency by reading RCC configuration register and applying prescaler |
| `HAL_RCC_GetPCLK2Freq` | RETURNOK | False | Returns the PCLK2 (APB2 peripheral clock) frequency by reading RCC configuration register and applying prescaler |
| `HAL_RCC_MCOConfig` | INIT | True | Configures the Microcontroller Clock Output (MCO) pins to output various clock sources (HSI, LSE, HSE, PLL, etc.) wit... |
| `HAL_RCC_NMI_IRQHandler` | IRQ | True | Interrupt handler for RCC Clock Security System (CSS) interrupt request, checks CSS flag and calls user callback |
| `HAL_SPI_DeInit` | INIT | True | De-initializes the SPI peripheral by disabling hardware and resetting state variables |
| `HAL_SPI_Init` | INIT | True | Initializes the SPI peripheral according to specified parameters in SPI_InitTypeDef and initializes the associated ha... |
| `HAL_TIM_Base_MspDeInit` | INIT | False | Timer Base MSP De-Initialization function that disables peripheral clocks for TIM instances |
| `HAL_TIM_Base_MspInit` | INIT | True | Initializes hardware resources for TIM (Timer) Base peripherals by enabling their clocks |
| `HAL_TIM_MspPostInit` | INIT | True | Post-initialization function for TIM peripheral that configures GPIO pins for TIM alternate functions |
| `HAL_UART_DeInit` | INIT | True | Deinitializes the UART peripheral by disabling hardware, calling low-level deinitialization, and resetting the UART h... |
| `HAL_UART_Init` | INIT | True | Initializes the UART peripheral according to specified parameters in UART_InitTypeDef and creates the associated handle |
| `SystemClock_Config` | INIT | True | Configures the system clock, PLL, and bus clocks for STM32 microcontroller initialization |
| `SystemCoreClockUpdate` | INIT | True | Updates the SystemCoreClock global variable based on current clock register values to provide the core clock frequenc... |
| `rt_hw_pin_init` | INIT | True | Initializes GPIO hardware by enabling clock for various GPIO ports and registers the pin device with RT-Thread OS |
| `stm32_dma_config` | CORE | False | Configures DMA for UART communication (TX or RX mode) including DMA initialization, NVIC interrupt configuration, and... |

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
