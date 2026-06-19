## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/stm32/UART_Hyperterminal_IT`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `BSP_COM_Init` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c` | 351 | 1 |
| `BSP_LED_Init` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c` | 205 | 1 |
| `BSP_PB_Init` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c` | 281 | 1 |
| `FLASH_WaitForLastOperation` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash.c` | 544 | 1 |
| `FSMC_BANK3_MspInit` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c` | 675 | 1 |
| `HAL_FLASHEx_Erase` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash_ex.c` | 160 | 1 |
| `HAL_GPIO_Init` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c` | 164 | 1 |
| `HAL_GPIO_ReadPin` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c` | 375 | 1 |
| `HAL_GPIO_WritePin` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c` | 410 | 1 |
| `HAL_I2C_Master_Receive` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1177 | 1 |
| `HAL_I2C_Master_Receive_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 2117 | 1 |
| `HAL_I2C_Master_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1756 | 1 |
| `HAL_I2C_Master_Seq_Receive_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3964 | 1 |
| `HAL_I2C_Master_Seq_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3843 | 1 |
| `HAL_I2C_Master_Seq_Transmit_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3663 | 1 |
| `HAL_I2C_Master_Seq_Transmit_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3568 | 1 |
| `HAL_I2C_Master_Transmit` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1056 | 1 |
| `HAL_I2C_Master_Transmit_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1962 | 1 |
| `HAL_I2C_Master_Transmit_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1679 | 1 |
| `HAL_I2C_Mem_Read` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 2626 | 1 |
| `HAL_I2C_Mem_Read_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3236 | 1 |
| `HAL_I2C_Mem_Read_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 2963 | 1 |
| `HAL_I2C_Mem_Write` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 2503 | 1 |
| `HAL_I2C_Mem_Write_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 3054 | 1 |
| `HAL_I2C_Mem_Write_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 2878 | 1 |
| `HAL_I2C_Slave_Receive` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1558 | 1 |
| `HAL_I2C_Slave_Seq_Receive_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 4485 | 1 |
| `HAL_I2C_Slave_Seq_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 4419 | 1 |
| `HAL_I2C_Slave_Seq_Transmit_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 4245 | 1 |
| `HAL_I2C_Slave_Seq_Transmit_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 4179 | 1 |
| `HAL_I2C_Slave_Transmit` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 1428 | 1 |
| `HAL_RCC_OscConfig` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_rcc.c` | 219 | 1 |
| `HAL_UARTEx_ReceiveToIdle` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1588 | 1 |
| `HAL_UARTEx_ReceiveToIdle_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1773 | 1 |
| `HAL_UARTEx_ReceiveToIdle_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1713 | 1 |
| `HAL_UART_Abort` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1859 | 1 |
| `HAL_UART_AbortTransmit_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 2195 | 1 |
| `HAL_UART_GetState` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 2928 | 2 |
| `HAL_UART_IRQHandler` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 2350 | 1 |
| `HAL_UART_Receive` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1221 | 1 |
| `HAL_UART_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1347 | 2 |
| `HAL_UART_Transmit` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1135 | 1 |
| `HAL_UART_Transmit_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1379 | 1 |
| `HAL_UART_Transmit_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 1308 | 2 |
| `I2C_DMAAbort` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7122 | 1 |
| `I2C_Master_ADDR` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 5852 | 1 |
| `I2C_RequestMemoryRead` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 6827 | 1 |
| `I2C_RequestMemoryWrite` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 6747 | 1 |
| `I2C_Slave_ADDR` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 6122 | 1 |
| `I2C_Slave_STOPF` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 6173 | 1 |
| `I2C_WaitOnBTFFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7357 | 1 |
| `I2C_WaitOnFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7225 | 1 |
| `I2C_WaitOnMasterAddressFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7262 | 1 |
| `I2C_WaitOnRXNEFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7463 | 1 |
| `I2C_WaitOnSTOPFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7398 | 1 |
| `I2C_WaitOnSTOPRequestThroughIT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7434 | 1 |
| `I2C_WaitOnTXEFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c` | 7316 | 1 |
| `I2Cx_MspInit` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c` | 465 | 1 |
| `SystemClock_Config` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Src/main.c` | 193 | 1 |
| `UART_DMAReceiveCplt` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 3042 | 1 |
| `UART_DMATransmitCplt` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 2988 | 1 |
| `UART_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 3594 | 1 |
| `UART_Start_Receive_DMA` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 3271 | 1 |
| `UART_Start_Receive_IT` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 3236 | 1 |
| `UART_WaitOnFlagUntilTimeout` | `/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c` | 3185 | 1 |

## 2. 各函数替换详情

### BSP_COM_Init

```text
=== BSP_COM_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c
- 行号：351
- 函数内容：void BSP_COM_Init(COM_TypeDef COM, UART_HandleTypeDef *huart)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  
  /* Enable GPIO clock */
  EVAL_COMx_TX_GPIO_CLK_ENABLE(COM);
  EVAL_COMx_RX_GPIO_CLK_ENABLE(COM);
  
  /* Enable USART clock */
  EVAL_COMx_CLK_ENABLE(COM);
  
  /* Configure USART Tx as alternate function */
  GPIO_InitStruct.Pin = COM_TX_PIN[COM];
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Alternate = COM_TX_AF[COM];
  HAL_GPIO_Init(COM_TX_PORT[COM], &GPIO_InitStruct);
  
  /* Configure USART Rx as alternate function */
  GPIO_InitStruct.Pin = COM_RX_PIN[COM];
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Alternate = COM_RX_AF[COM];
  HAL_GPIO_Init(COM_RX_PORT[COM], &GPIO_InitStruct);
  
  /* USART configuration */
  huart->Instance = COM_USART[COM];
  HAL_UART_Init(huart);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures COM port (UART) hardware by enabling clocks, configuring GPIO pins as alternate functions, and initializing UART peripheral.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a BSP initialization function that configures COM port hardware. GetMMIOFunctionInfo showed hardware register accesses through macros and HAL functions. The function enables GPIO and USART clocks, configures TX/RX pins as alternate functions, sets up UART handle instance, and calls HAL_UART_Init. This matches the INIT classification criteria: peripheral initialization function with MMIO operations that can be removed while preserving structure initialization and state. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data reception), not IRQ (not an interrupt handler), not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Configures COM port.
* @param  COM: COM port to be configured.
*          This parameter can be one of the following values:
*            @arg  COM1
*            @arg  COM2
* @param  huart: Pointer to a UART_HandleTypeDef structure that contains the
*                configuration information for the specified USART peripheral.
*/
void BSP_COM_Init(COM_TypeDef COM, UART_HandleTypeDef *huart)
{
  /* Set the UART instance based on COM port */
  huart->Instance = COM_USART[COM];
  
  /* Initialize UART - hardware-specific operations will be handled in HAL_UART_Init */
  HAL_UART_Init(huart);
}
```

【替换更新】
- 更新代码：/**
* @brief  Configures COM port.
* @param  COM: COM port to be configured.
*          This parameter can be one of the following values:
*            @arg  COM1
*            @arg  COM2
* @param  huart: Pointer to a UART_HandleTypeDef structure that contains the
*                configuration information for the specified USART peripheral.
*/
void BSP_COM_Init(COM_TypeDef COM, UART_HandleTypeDef *huart)
{
  /* Set the UART instance based on COM port */
  huart->Instance = COM_USART[COM];
  
  /* Initialize UART - hardware-specific operations will be handled in HAL_UART_Init */
  HAL_UART_Init(huart);
}
- 更新原因：Simplify BSP_COM_Init implementation by removing commented-out hardware operations and keeping only essential UART instance assignment and initialization call. This should resolve any potential syntax issues from malformed comments.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/**
* @brief  Configures COM port.
* @param  COM: COM port to be configured.
*          This parameter can be one of the following values:
*            @arg  COM1
*            @arg  COM2
* @param  huart: Pointer to a UART_HandleTypeDef structure that contains the
*                configuration information for the specified USART peripheral.
*/
void BSP_COM_Init(COM_TypeDef COM, UART_HandleTypeDef *huart)
{
  /* Set the UART instance based on COM port */
  huart->Instance = COM_USART[COM];
  
  /* Initialize UART - hardware-specific operations will be handled in HAL_UART_Init */
  HAL_UART_Init(huart);
}
    原因：Simplify BSP_COM_Init implementation by removing commented-out hardware operations and keeping only essential UART instance assignment and initialization call. This should resolve any potential syntax issues from malformed comments.
    时间：

=== 信息结束 ===
```

### BSP_LED_Init

```text
=== BSP_LED_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c
- 行号：205
- 函数内容：void BSP_LED_Init(Led_TypeDef Led)
{
  GPIO_InitTypeDef  GPIO_InitStruct;
  
  /* Enable the GPIO_LED clock */
  LEDx_GPIO_CLK_ENABLE(Led);

  /* Configure the GPIO_LED pin */
  GPIO_InitStruct.Pin = GPIO_PIN[Led];
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
  
  HAL_GPIO_Init(GPIO_PORT[Led], &GPIO_InitStruct);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes LED GPIO pins by enabling clock and configuring pin settings
- 是否需要替换：是
- 分类/替换原因：This is an initialization function that configures LED GPIO hardware. GetFunctionInfo shows it enables GPIO clock via LEDx_GPIO_CLK_ENABLE and calls HAL_GPIO_Init for hardware configuration. GetMMIOFunctionInfo indicates hardware-dependent operations through function calls. The function is called from main() to initialize LEDs. As an INIT function, it should have hardware operations removed while preserving structure initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void BSP_LED_Init(Led_TypeDef Led)
{
  GPIO_InitTypeDef  GPIO_InitStruct;
  
  /* Skip hardware clock enable */
  /* LEDx_GPIO_CLK_ENABLE(Led); */

  /* Configure the GPIO_LED pin structure (preserved for state consistency) */
  GPIO_InitStruct.Pin = GPIO_PIN[Led];
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
  
  /* Skip hardware GPIO initialization */
  /* HAL_GPIO_Init(GPIO_PORT[Led], &GPIO_InitStruct); */
}
```

=== 信息结束 ===
```

### BSP_PB_Init

```text
=== BSP_PB_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c
- 行号：281
- 函数内容：void BSP_PB_Init(Button_TypeDef Button, ButtonMode_TypeDef Button_Mode)
{
  GPIO_InitTypeDef GPIO_InitStruct;
  
  /* Enable the BUTTON clock */
  BUTTONx_GPIO_CLK_ENABLE(Button);
  
  if(Button_Mode == BUTTON_MODE_GPIO)
  {
    /* Configure Button pin as input */
    GPIO_InitStruct.Pin = BUTTON_PIN[Button];
    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
    
    HAL_GPIO_Init(BUTTON_PORT[Button], &GPIO_InitStruct);
  }
  
  if(Button_Mode == BUTTON_MODE_EXTI)
  {
    /* Configure Button pin as input with External interrupt */
    GPIO_InitStruct.Pin = BUTTON_PIN[Button];
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
    
    if(Button != BUTTON_WAKEUP)
    {
      GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING; 
    }
    else
    {
      GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
    }
    
    HAL_GPIO_Init(BUTTON_PORT[Button], &GPIO_InitStruct);
    
    /* Enable and set Button EXTI Interrupt to the lowest priority */
    HAL_NVIC_SetPriority((IRQn_Type)(BUTTON_IRQn[Button]), 0x0F, 0x0);
    HAL_NVIC_EnableIRQ((IRQn_Type)(BUTTON_IRQn[Button]));
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures button GPIO and EXTI lines for push buttons on STM324xG evaluation board
- 是否需要替换：是
- 分类/替换原因：This is an initialization function that configures button GPIO pins and EXTI interrupt lines. Analysis using GetFunctionInfo and GetMMIOFunctionInfo shows it performs hardware initialization including GPIO clock enable, pin configuration, and NVIC interrupt setup. The function calls HAL_NVIC_SetPriority and HAL_NVIC_EnableIRQ which are CORE functions that must be preserved. According to classification rules, functions that call CORE functions should be classified as INIT, not CORE. The replacement follows INIT strategy by removing hardware-specific operations (GPIO clock enable, HAL_GPIO_Init calls) while preserving structure initialization and critical NVIC calls.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  Configures button GPIO and EXTI Line.\n* @param  Button: Button to be configured\n*          This parameter can be one of the following values:\n*            @arg  BUTTON_WAKEUP: Wakeup Push Button\n*            @arg  BUTTON_TAMPER: Tamper Push Button\n*            @arg  BUTTON_KEY: Key Push Button\n*            @arg  BUTTON_RIGHT: Joystick Right Push Button\n*            @arg  BUTTON_LEFT: Joystick Left Push Button\n*            @arg  BUTTON_UP: Joystick Up Push Button\n*            @arg  BUTTON_DOWN: Joystick Down Push Button\n*            @arg  BUTTON_SEL: Joystick Sel Push Button\n* @param  Button_Mode: Button mode\n*          This parameter can be one of the following values:\n*            @arg  BUTTON_MODE_GPIO: Button will be used as simple IO\n*            @arg  BUTTON_MODE_EXTI: Button will be connected to EXTI line\n*                                    with interrupt generation capability\n*/\nvoid BSP_PB_Init(Button_TypeDef Button, ButtonMode_TypeDef Button_Mode)\n{\n  GPIO_InitTypeDef GPIO_InitStruct;\n  \n  /* Skip hardware-specific clock enable */\n  /* BUTTONx_GPIO_CLK_ENABLE(Button); */\n  \n  if(Button_Mode == BUTTON_MODE_GPIO)\n  {\n    /* Configure Button pin as input - preserve structure initialization */\n    GPIO_InitStruct.Pin = BUTTON_PIN[Button];\n    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;\n    GPIO_InitStruct.Pull = GPIO_NOPULL;\n    GPIO_InitStruct.Speed = GPIO_SPEED_FAST;\n    \n    /* Skip hardware GPIO initialization */\n    /* HAL_GPIO_Init(BUTTON_PORT[Button], &GPIO_InitStruct); */\n  }\n  \n  if(Button_Mode == BUTTON_MODE_EXTI)\n  {\n    /* Configure Button pin as input with External interrupt - preserve structure initialization */\n    GPIO_InitStruct.Pin = BUTTON_PIN[Button];\n    GPIO_InitStruct.Pull = GPIO_NOPULL;\n    GPIO_InitStruct.Speed = GPIO_SPEED_FAST;\n    \n    if(Button != BUTTON_WAKEUP)\n    {\n      GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING; \n    }\n    else\n    {\n      GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;\n    }\n    \n    /* Skip hardware GPIO initialization */\n    /* HAL_GPIO_Init(BUTTON_PORT[Button], &GPIO_InitStruct); */\n    \n    /* Enable and set Button EXTI Interrupt to the lowest priority */\n    /* PRESERVE CORE NVIC calls as required by classification rules */\n    HAL_NVIC_SetPriority((IRQn_Type)(BUTTON_IRQn[Button]), 0x0F, 0x0);\n    HAL_NVIC_EnableIRQ((IRQn_Type)(BUTTON_IRQn[Button]));\n  }\n}
```

=== 信息结束 ===
```

### FLASH_WaitForLastOperation

```text
=== FLASH_WaitForLastOperation 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash.c
- 行号：544
- 函数内容：HAL_StatusTypeDef FLASH_WaitForLastOperation(uint32_t Timeout)
{
  uint32_t tickstart = 0U;

  /* Clear Error Code */
  pFlash.ErrorCode = HAL_FLASH_ERROR_NONE;

  /* Wait for the FLASH operation to complete by polling on BUSY flag to be reset.
     Even if the FLASH operation fails, the BUSY flag will be reset and an error
     flag will be set */
  /* Get tick */
  tickstart = HAL_GetTick();

  while (__HAL_FLASH_GET_FLAG(FLASH_FLAG_BSY) != RESET)
  {
    if (Timeout != HAL_MAX_DELAY)
    {
      if ((Timeout == 0U) || ((HAL_GetTick() - tickstart) > Timeout))
      {
        return HAL_TIMEOUT;
      }
    }
  }

  /* Check FLASH End of Operation flag  */
  if (__HAL_FLASH_GET_FLAG(FLASH_FLAG_EOP) != RESET)
  {
    /* Clear FLASH End of Operation pending bit */
    __HAL_FLASH_CLEAR_FLAG(FLASH_FLAG_EOP);
  }
#if defined(FLASH_SR_RDERR)
  if (__HAL_FLASH_GET_FLAG((FLASH_FLAG_OPERR | FLASH_FLAG_WRPERR | FLASH_FLAG_PGAERR | \
                            FLASH_FLAG_PGPERR | FLASH_FLAG_PGSERR | FLASH_FLAG_RDERR)) != RESET)
#else
  if (__HAL_FLASH_GET_FLAG((FLASH_FLAG_OPERR | FLASH_FLAG_WRPERR | FLASH_FLAG_PGAERR | \
                            FLASH_FLAG_PGPERR | FLASH_FLAG_PGSERR)) != RESET)
#endif /* FLASH_SR_RDERR */
  {
    /*Save the error code*/
    FLASH_SetErrorCode();
    return HAL_ERROR;
  }

  /* If there is no error flag set */
  return HAL_OK;

}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for a FLASH operation to complete by polling the BUSY flag, checks completion status, and handles error flags
- 是否需要替换：是
- 分类/替换原因：Function contains a while loop that polls the __HAL_FLASH_GET_FLAG(FLASH_FLAG_BSY) hardware flag to wait for FLASH operation completion. GetMMIOFunctionInfo revealed multiple MMIO expressions including flag checks and clears. This matches the LOOP classification criteria: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags)'. The function is called by various FLASH programming/erase functions (HAL_FLASH_Program, HAL_FLASHEx_Erase, etc.) to wait for hardware operations to complete. Replacement strategy: skip the polling loop entirely and assume the condition is already met, while preserving error code initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  Wait for a FLASH operation to complete.\n* @param  Timeout maximum flash operationtimeout\n* @retval HAL Status\n*/\nHAL_StatusTypeDef FLASH_WaitForLastOperation(uint32_t Timeout)\n{\n  /* Clear Error Code */\n  pFlash.ErrorCode = HAL_FLASH_ERROR_NONE;\n\n  /* [LOOP REMOVED] Skip polling on BUSY flag - assume FLASH operation is complete */\n  /* Original: while (__HAL_FLASH_GET_FLAG(FLASH_FLAG_BSY) != RESET) */\n\n  /* Check FLASH End of Operation flag - assume it's set */\n  /* [LOOP REMOVED] Skip hardware flag check - assume EOP flag is set */\n  /* Original: if (__HAL_FLASH_GET_FLAG(FLASH_FLAG_EOP) != RESET) */\n  /* Clear FLASH End of Operation pending bit */\n  /* [LOOP REMOVED] Skip hardware flag clear */\n  /* Original: __HAL_FLASH_CLEAR_FLAG(FLASH_FLAG_EOP); */\n\n  /* Check error flags - assume no errors by default */\n  /* [LOOP REMOVED] Skip hardware error flag checks */\n  /* Original complex error flag checking removed */\n\n  /* If there is no error flag set */\n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### FSMC_BANK3_MspInit

```text
=== FSMC_BANK3_MspInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c
- 行号：675
- 函数内容：static void FSMC_BANK3_MspInit(void)
{
  GPIO_InitTypeDef GPIO_Init_Structure;
    
  /* Enable FSMC clock */
  __FSMC_CLK_ENABLE();

  /* Enable GPIOs clock */
  __GPIOD_CLK_ENABLE();
  __GPIOE_CLK_ENABLE();
  __GPIOF_CLK_ENABLE();
  __GPIOG_CLK_ENABLE();
  
  /* Common GPIO configuration */
  GPIO_Init_Structure.Mode      = GPIO_MODE_AF_PP;
  GPIO_Init_Structure.Pull      = GPIO_PULLUP;
  GPIO_Init_Structure.Speed     = GPIO_SPEED_HIGH;
  GPIO_Init_Structure.Alternate = GPIO_AF12_FSMC;
  
  /* GPIOD configuration */
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_4 | GPIO_PIN_5 | GPIO_PIN_8     |\
                              GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_11 | GPIO_PIN_12 | GPIO_PIN_13 |\
                              GPIO_PIN_14 | GPIO_PIN_15;
   
  HAL_GPIO_Init(GPIOD, &GPIO_Init_Structure);

  /* GPIOE configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_3| GPIO_PIN_4 | GPIO_PIN_7     |\
                              GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_11 | GPIO_PIN_12 |\
                              GPIO_PIN_13 | GPIO_PIN_14 | GPIO_PIN_15;
  HAL_GPIO_Init(GPIOE, &GPIO_Init_Structure);
  
  /* GPIOF configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_2| GPIO_PIN_3 | GPIO_PIN_4     |\
                              GPIO_PIN_5 | GPIO_PIN_12 | GPIO_PIN_13 | GPIO_PIN_14 | GPIO_PIN_15;
  HAL_GPIO_Init(GPIOF, &GPIO_Init_Structure);
  
  /* GPIOG configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_2| GPIO_PIN_3 | GPIO_PIN_4     |\
                              GPIO_PIN_5 | GPIO_PIN_10;
  
  HAL_GPIO_Init(GPIOG, &GPIO_Init_Structure);  
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the Microcontroller Specific Package (MSP) for FSMC Bank 3 by configuring GPIO pins for FSMC functionality
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is a static initialization function that enables FSMC and GPIO clocks, then configures GPIO pins for FSMC alternate function. GetMMIOFunctionInfo reveals multiple hardware register accesses through clock enable macros and GPIO initialization. The function follows the typical MSP initialization pattern for peripheral configuration. It's classified as INIT because it performs hardware initialization operations that need to be replaced while preserving structure initialization logic. The replacement removes all hardware-specific operations (clock enables and GPIO initialization calls) while keeping the structure configuration intact.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes FSMC_BANK3 MSP.
*/
static void FSMC_BANK3_MspInit(void)
{
  GPIO_InitTypeDef GPIO_Init_Structure;
    
  /* Enable FSMC clock - removed for simulation */
  /* __FSMC_CLK_ENABLE(); */

  /* Enable GPIOs clock - removed for simulation */
  /* __GPIOD_CLK_ENABLE(); */
  /* __GPIOE_CLK_ENABLE(); */
  /* __GPIOF_CLK_ENABLE(); */
  /* __GPIOG_CLK_ENABLE(); */
  
  /* Common GPIO configuration */
  GPIO_Init_Structure.Mode      = GPIO_MODE_AF_PP;
  GPIO_Init_Structure.Pull      = GPIO_PULLUP;
  GPIO_Init_Structure.Speed     = GPIO_SPEED_HIGH;
  GPIO_Init_Structure.Alternate = GPIO_AF12_FSMC;
  
  /* GPIOD configuration */
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_4 | GPIO_PIN_5 | GPIO_PIN_8     |\
                              GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_11 | GPIO_PIN_12 | GPIO_PIN_13 |\
                              GPIO_PIN_14 | GPIO_PIN_15;
   
  /* HAL_GPIO_Init(GPIOD, &GPIO_Init_Structure); - removed for simulation */

  /* GPIOE configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_3| GPIO_PIN_4 | GPIO_PIN_7     |\
                              GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_11 | GPIO_PIN_12 |\
                              GPIO_PIN_13 | GPIO_PIN_14 | GPIO_PIN_15;
  /* HAL_GPIO_Init(GPIOE, &GPIO_Init_Structure); - removed for simulation */
  
  /* GPIOF configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_2| GPIO_PIN_3 | GPIO_PIN_4     |\
                              GPIO_PIN_5 | GPIO_PIN_12 | GPIO_PIN_13 | GPIO_PIN_14 | GPIO_PIN_15;
  /* HAL_GPIO_Init(GPIOF, &GPIO_Init_Structure); - removed for simulation */
  
  /* GPIOG configuration */  
  GPIO_Init_Structure.Pin   = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_2| GPIO_PIN_3 | GPIO_PIN_4     |\
                              GPIO_PIN_5 | GPIO_PIN_10;

  /* HAL_GPIO_Init(GPIOG, &GPIO_Init_Structure); - removed for simulation */  
}
```

=== 信息结束 ===
```

### HAL_FLASHEx_Erase

```text
=== HAL_FLASHEx_Erase 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_flash_ex.c
- 行号：160
- 函数内容：HAL_StatusTypeDef HAL_FLASHEx_Erase(FLASH_EraseInitTypeDef *pEraseInit, uint32_t *SectorError)
{
  HAL_StatusTypeDef status = HAL_ERROR;
  uint32_t index = 0U;

  /* Process Locked */
  __HAL_LOCK(&pFlash);

  /* Check the parameters */
  assert_param(IS_FLASH_TYPEERASE(pEraseInit->TypeErase));

  /* Wait for last operation to be completed */
  status = FLASH_WaitForLastOperation((uint32_t)FLASH_TIMEOUT_VALUE);

  if (status == HAL_OK)
  {
    /*Initialization of SectorError variable*/
    *SectorError = 0xFFFFFFFFU;

    if (pEraseInit->TypeErase == FLASH_TYPEERASE_MASSERASE)
    {
      /*Mass erase to be done*/
      FLASH_MassErase((uint8_t) pEraseInit->VoltageRange, pEraseInit->Banks);

      /* Wait for last operation to be completed */
      status = FLASH_WaitForLastOperation((uint32_t)FLASH_TIMEOUT_VALUE);

      /* if the erase operation is completed, disable the MER Bit */
      FLASH->CR &= (~FLASH_MER_BIT);
    }
    else
    {
      /* Check the parameters */
      assert_param(IS_FLASH_NBSECTORS(pEraseInit->NbSectors + pEraseInit->Sector));

      /* Erase by sector by sector to be done*/
      for (index = pEraseInit->Sector; index < (pEraseInit->NbSectors + pEraseInit->Sector); index++)
      {
        FLASH_Erase_Sector(index, (uint8_t) pEraseInit->VoltageRange);

        /* Wait for last operation to be completed */
        status = FLASH_WaitForLastOperation((uint32_t)FLASH_TIMEOUT_VALUE);

        /* If the erase operation is completed, disable the SER and SNB Bits */
        CLEAR_BIT(FLASH->CR, (FLASH_CR_SER | FLASH_CR_SNB));

        if (status != HAL_OK)
        {
          /* In case of error, stop erase procedure and return the faulty sector*/
          *SectorError = index;
          break;
        }
      }
    }
    /* Flush the caches to be sure of the data consistency */
    FLASH_FlushCaches();
  }

  /* Process Unlocked */
  __HAL_UNLOCK(&pFlash);

  return status;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Performs mass erase or sector erase operations on FLASH memory with configuration parameters and error reporting
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a FLASH memory erase function that performs hardware initialization/configuration operations. GetMMIOFunctionInfo identified direct hardware register accesses (FLASH->CR operations) and calls to hardware-dependent functions (FLASH_MassErase, FLASH_Erase_Sector, FLASH_WaitForLastOperation, FLASH_FlushCaches). The function contains parameter validation, error handling through SectorError parameter, and locking mechanisms for process safety. It was classified as INIT because it performs FLASH memory initialization/configuration (erasing) operations, not as CORE (no NVIC/OS kernel/VTOR operations), not as RECV (not data I/O), not as IRQ (not interrupt-related), and not as LOOP (though it contains a loop, the primary purpose is initialization). The replacement preserves the logical flow, error handling, and parameter validation while removing all hardware-dependent operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_FLASHEx_Erase(FLASH_EraseInitTypeDef *pEraseInit, uint32_t *SectorError)
{
  HAL_StatusTypeDef status = HAL_ERROR;
  uint32_t index = 0U;

  /* Process Locked */
  __HAL_LOCK(&pFlash);

  /* Check the parameters */
  assert_param(IS_FLASH_TYPEERASE(pEraseInit->TypeErase));

  /* Wait for last operation to be completed - simulate success */
  status = HAL_OK; /* Assume FLASH_WaitForLastOperation would return HAL_OK */

  if (status == HAL_OK)
  {
    /*Initialization of SectorError variable*/
    *SectorError = 0xFFFFFFFFU;

    if (pEraseInit->TypeErase == FLASH_TYPEERASE_MASSERASE)
    {
      /*Mass erase to be done - skip hardware operation */
      /* FLASH_MassErase((uint8_t) pEraseInit->VoltageRange, pEraseInit->Banks); */

      /* Wait for last operation to be completed - simulate success */
      status = HAL_OK; /* Assume FLASH_WaitForLastOperation would return HAL_OK */

      /* if the erase operation is completed, disable the MER Bit - skip hardware register access */
      /* FLASH->CR &= (~FLASH_MER_BIT); */
    }
    else
    {
      /* Check the parameters */
      assert_param(IS_FLASH_NBSECTORS(pEraseInit->NbSectors + pEraseInit->Sector));

      /* Erase by sector by sector to be done*/
      for (index = pEraseInit->Sector; index < (pEraseInit->NbSectors + pEraseInit->Sector); index++)
      {
        /* FLASH_Erase_Sector(index, (uint8_t) pEraseInit->VoltageRange); */

        /* Wait for last operation to be completed - simulate success */
        status = HAL_OK; /* Assume FLASH_WaitForLastOperation would return HAL_OK */

        /* If the erase operation is completed, disable the SER and SNB Bits - skip hardware register access */
        /* CLEAR_BIT(FLASH->CR, (FLASH_CR_SER | FLASH_CR_SNB)); */

        if (status != HAL_OK)
        {
          /* In case of error, stop erase procedure and return the faulty sector*/
          *SectorError = index;
          break;
        }
      }
    }
    /* Flush the caches to be sure of the data consistency - skip hardware operation */
    /* FLASH_FlushCaches(); */
  }

  /* Process Unlocked */
  __HAL_UNLOCK(&pFlash);

  return status;
}
```

=== 信息结束 ===
```

### HAL_GPIO_Init

```text
=== HAL_GPIO_Init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c
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
- 函数用途/功能描述：Initializes GPIO peripheral pins according to specified configuration parameters including mode, speed, pull-up/down, alternate function, and external interrupt settings.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs extensive MMIO operations to configure GPIO registers (OSPEEDR, OTYPER, PUPDR, AFR, MODER, SYSCFG->EXTICR, EXTI registers). 2) It is a pure initialization function that sets up hardware configuration without data transfer. 3) It contains parameter validation and structure processing but no data reception/transmission, interrupt handling, or polling loops. 4) It is called from various MspInit functions and BSP initialization routines, confirming its role as a hardware initialization function. 5) It does not contain CORE operations (NVIC/OS kernel/VTOR). Therefore, it fits the INIT classification: functions that initialize peripheral/configurations where we should remove MMIO operations while preserving parameter validation and structure processing.
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
      if(((GPIO_Init->Mode & GPIO_MODE) == MODE_OUTPUT) || \
          (GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Speed parameter */
        assert_param(IS_GPIO_SPEED(GPIO_Init->Speed));
        /* Skip hardware-specific speed configuration */
      }

      if((GPIO_Init->Mode & GPIO_MODE) != MODE_ANALOG)
      {
        /* Check the parameters */
        assert_param(IS_GPIO_PULL(GPIO_Init->Pull));
        /* Skip hardware-specific pull-up/pull-down configuration */
      }

      /* In case of Alternate function mode selection */
      if((GPIO_Init->Mode & GPIO_MODE) == MODE_AF)
      {
        /* Check the Alternate function parameter */
        assert_param(IS_GPIO_AF(GPIO_Init->Alternate));
        /* Skip hardware-specific alternate function configuration */
      }

      /* Skip hardware-specific mode configuration */

      /*--------------------- EXTI Mode Configuration ------------------------*/
      /* Configure the External Interrupt or event for the current IO */
      if((GPIO_Init->Mode & EXTI_MODE) != 0x00U)
      {
        /* Skip SYSCFG Clock enable */
        /* Skip hardware-specific EXTI configuration */
      }
    }
  }
}
```

=== 信息结束 ===
```

### HAL_GPIO_ReadPin

```text
=== HAL_GPIO_ReadPin 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c
- 行号：375
- 函数内容：GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin)
{
  GPIO_PinState bitstatus;

  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));

  if((GPIOx->IDR & GPIO_Pin) != (uint32_t)GPIO_PIN_RESET)
  {
    bitstatus = GPIO_PIN_SET;
  }
  else
  {
    bitstatus = GPIO_PIN_RESET;
  }
  return bitstatus;
}


【替换更新】
- 更新代码：GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));

  /* In emulation mode, return a default value */
  /* The original code reads from GPIOx->IDR register */
  /* We preserve the parameter checking but return a safe default */
  
  /* Return PIN_RESET as a safe default in emulation */
  return GPIO_PIN_RESET;
}
- 更新原因：Fix potential emulator issues by avoiding hardware register reads in HAL_GPIO_ReadPin. The original function reads from GPIOx->IDR register which is a hardware operation. In emulation, reading from hardware registers that aren't properly handled can cause issues. The replacement preserves parameter checking but returns a safe default value (GPIO_PIN_RESET) instead of reading from hardware.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：GPIO_PinState HAL_GPIO_ReadPin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));

  /* In emulation mode, return a default value */
  /* The original code reads from GPIOx->IDR register */
  /* We preserve the parameter checking but return a safe default */
  
  /* Return PIN_RESET as a safe default in emulation */
  return GPIO_PIN_RESET;
}
    原因：Fix potential emulator issues by avoiding hardware register reads in HAL_GPIO_ReadPin. The original function reads from GPIOx->IDR register which is a hardware operation. In emulation, reading from hardware registers that aren't properly handled can cause issues. The replacement preserves parameter checking but returns a safe default value (GPIO_PIN_RESET) instead of reading from hardware.
    时间：

=== 信息结束 ===
```

### HAL_GPIO_WritePin

```text
=== HAL_GPIO_WritePin 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_gpio.c
- 行号：410
- 函数内容：void HAL_GPIO_WritePin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, GPIO_PinState PinState)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));
  assert_param(IS_GPIO_PIN_ACTION(PinState));

  if(PinState != GPIO_PIN_RESET)
  {
    GPIOx->BSRR = GPIO_Pin;
  }
  else
  {
    GPIOx->BSRR = (uint32_t)GPIO_Pin << 16U;
  }
}


【替换更新】
- 更新代码：void HAL_GPIO_WritePin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, GPIO_PinState PinState)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));
  assert_param(IS_GPIO_PIN_ACTION(PinState));

  /* In emulation mode, skip hardware register writes */
  /* The original code would write to GPIOx->BSRR register */
  /* We preserve the parameter checking but skip the actual hardware operation */
  
  /* No operation in emulation */
}
- 更新原因：Fix potential emulator issues by skipping hardware register writes in HAL_GPIO_WritePin. The original function writes to GPIOx->BSRR register which is a hardware operation. In emulation, writing to hardware registers that aren't properly handled can cause issues. The replacement preserves parameter checking but skips the actual hardware write operation. This function is called from BSP_LED_On in UART completion callbacks, so fixing it might resolve the exceptional loop issue.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void HAL_GPIO_WritePin(GPIO_TypeDef* GPIOx, uint16_t GPIO_Pin, GPIO_PinState PinState)
{
  /* Check the parameters */
  assert_param(IS_GPIO_PIN(GPIO_Pin));
  assert_param(IS_GPIO_PIN_ACTION(PinState));

  /* In emulation mode, skip hardware register writes */
  /* The original code would write to GPIOx->BSRR register */
  /* We preserve the parameter checking but skip the actual hardware operation */
  
  /* No operation in emulation */
}
    原因：Fix potential emulator issues by skipping hardware register writes in HAL_GPIO_WritePin. The original function writes to GPIOx->BSRR register which is a hardware operation. In emulation, writing to hardware registers that aren't properly handled can cause issues. The replacement preserves parameter checking but skips the actual hardware write operation. This function is called from BSP_LED_On in UART completion callbacks, so fixing it might resolve the exceptional loop issue.
    时间：

=== 信息结束 ===
```

### HAL_I2C_Master_Receive

```text
=== HAL_I2C_Master_Receive 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1177
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Receive(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BUSY, SET, I2C_TIMEOUT_BUSY_FLAG, tickstart) != HAL_OK)
    {
      return HAL_BUSY;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State       = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode        = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Send Slave Address */
    if (I2C_MasterRequestRead(hi2c, DevAddress, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    if (hi2c->XferSize == 0U)
    {
      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    else if (hi2c->XferSize == 1U)
    {
      /* Disable Acknowledge */
      CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    else if (hi2c->XferSize == 2U)
    {
      /* Disable Acknowledge */
      CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Enable Pos */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }
    else
    {
      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }

    while (hi2c->XferSize > 0U)
    {
      if (hi2c->XferSize <= 3U)
      {
        /* One byte */
        if (hi2c->XferSize == 1U)
        {
          /* Wait until RXNE flag is set */
          if (I2C_WaitOnRXNEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
        /* Two bytes */
        else if (hi2c->XferSize == 2U)
        {
          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
        /* 3 Last bytes */
        else
        {
          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
      }
      else
      {
        /* Wait until RXNE flag is set */
        if (I2C_WaitOnRXNEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
        {
          return HAL_ERROR;
        }

        /* Read data from DR */
        *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferSize--;
        hi2c->XferCount--;

        if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET)
        {

          if (hi2c->XferSize == 3U)
          {
            /* Disable Acknowledge */
            CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
          }

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
      }
    }

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receives data in master mode from I2C peripheral in blocking mode
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo shows this is an I2C master receive function that reads data from hardware registers (hi2c->Instance->DR). GetMMIOFunctionInfo confirms multiple hardware register accesses for data reception. The function's primary purpose is data reception from I2C peripheral, making it a RECV type. It contains polling loops waiting for hardware flags and manages buffer pointers and state machine, but the core functionality is data reception. According to priority order: NOT CORE (no NVIC/OS/VTOR), RECV (data reception), not IRQ/INIT/LOOP/RETURNOK/SKIP/NODRIVER.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Master_Receive(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait - assume bus is ready */
    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip I2C peripheral enable check */

    /* Disable Pos - skip hardware operation */

    hi2c->State       = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode        = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Skip slave address request - assume successful */

    /* Skip ADDR flag clearing and STOP generation for different transfer sizes */

    /* Simulate data reception for all bytes */
    if (hi2c->XferSize > 0U)
    {
      /* Use HAL_BE_In to simulate receiving data */
      HAL_BE_In(hi2c->pBuffPtr, hi2c->XferSize);
      
      /* Update buffer pointer and counters */
      hi2c->pBuffPtr += hi2c->XferSize;
      hi2c->XferCount = 0U;
      hi2c->XferSize = 0U;
    }

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Receive_DMA

```text
=== HAL_I2C_Master_Receive_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：2117
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Receive_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;
  HAL_StatusTypeDef dmaxferstatus;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferM1CpltCallback = NULL;
        hi2c->hdmarx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmarx, (uint32_t)&hi2c->Instance->DR, (uint32_t)hi2c->pBuffPtr, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        /* Generate Start */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */

        /* Enable EVT and ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

        /* Enable DMA Request */
        SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable EVT, BUF and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Generate Start */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initiates DMA-based I2C data reception in master mode, configuring DMA transfer, I2C registers, and starting the communication.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs hardware initialization (I2C register configuration, DMA setup, interrupt enabling). 2) Contains polling loop waiting for BUSY flag (LOOP characteristic). 3) Sets up DMA transfer parameters and callbacks. 4) Updates I2C handle state and transfer parameters. 5) Not CORE (no NVIC/OS operations). 6) Not pure RECV (initiates reception but doesn't perform actual data transfer). 7) Primary purpose is initialization and configuration of DMA-based reception. The function matches INIT classification: 'Functions that initialize peripheral/configurations or allocate resources.'
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Master_Receive_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef dmaxferstatus;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferM1CpltCallback = NULL;
        hi2c->hdmarx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Simulate DMA start - assume success */
        dmaxferstatus = HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Simulate data reception via HAL_BE_In for the expected data size */
        HAL_BE_In(hi2c->pBuffPtr, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Receive_IT

```text
=== HAL_I2C_Master_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1756
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Receive_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;


    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    /* Enable Acknowledge */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    /* Generate Start */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes I2C peripheral for interrupt-driven master mode data reception, setting up transfer parameters and enabling interrupts
- 是否需要替换：是
- 分类/替换原因：Function performs initialization of I2C peripheral for interrupt-driven reception: sets state to BUSY_RX, configures transfer parameters (buffer, size, device address), and contains hardware-dependent operations (BUSY flag polling, peripheral enable/disable, interrupt enable, ACK configuration, START generation) that need to be removed while preserving state management and parameter setup. Not CORE (no NVIC/OS/VTOR operations), not RECV (doesn't perform actual data reception), not IRQ (not an interrupt handler). Primary purpose is initialization for interrupt-driven operation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Receive in master mode an amount of data in non-blocking mode with Interrupt
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Receive_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Skip hardware-specific operations: 
       - BUSY flag polling loop
       - I2C peripheral enable/disable
       - POS bit configuration
       - Interrupt enable
       - ACK bit configuration
       - START generation
    */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Seq_Receive_DMA

```text
=== HAL_I2C_Master_Seq_Receive_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3964
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Seq_Receive_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  __IO uint32_t count = 0U;
  uint32_t enableIT = (I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* Wait until BUSY flag is reset */
      count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
      do
      {
        count--;
        if (count == 0U)
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          return HAL_BUSY;
        }
      }
      while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    /* Clear Last DMA bit */
    CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if (hi2c->XferSize > 0U)
    {
      if ((hi2c->XferCount == 2U) && ((XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP)))
      {
        if (Prev_State == I2C_STATE_MASTER_BUSY_RX)
        {
          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          /* Enable Pos */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

          /* Enable Last DMA bit */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);
        }
        else
        {
          /* Enable Acknowledge */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
        }
      }
      else
      {
        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        if ((XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_OTHER_AND_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP))
        {
          /* Enable Last DMA bit */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);
        }
      }
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmarx, (uint32_t)&hi2c->Instance->DR, (uint32_t)hi2c->pBuffPtr, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
      if (dmaxferstatus == HAL_OK)
      {
        /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
        /* Mean Previous state is same as current state */
        if ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
        {
          /* Generate Start */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

          /* Update interrupt for only EVT and ERR */
          enableIT = (I2C_IT_EVT | I2C_IT_ERR);
        }
        else
        {
          /* Update interrupt for only ERR */
          enableIT = I2C_IT_ERR;
        }

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */

        /* If XferOptions is not associated to a new frame, mean no start bit is request, enable directly the DMA request */
        /* In other cases, DMA request is enabled after Slave address treatment in IRQHandler */
        if ((XferOptions == I2C_NEXT_FRAME) || (XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP))
        {
          /* Enable DMA Request */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);
        }

        /* Enable EVT and ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, enableIT);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
      /* Mean Previous state is same as current state */
      if ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
      {
        /* Generate Start */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
      }

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable interrupts */
      __HAL_I2C_ENABLE_IT(hi2c, enableIT);
    }
    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Sequential data reception in I2C master mode using DMA with support for repeated start conditions and direction changes during transfer
- 是否需要替换：是
- 分类/替换原因：This function is classified as RECV because: 1) It performs data reception from I2C peripheral to memory buffer via DMA, 2) Contains hardware-dependent operations including polling loops for BUSY flag, I2C register accesses (CR1, CR2), and DMA setup, 3) Manages I2C state machine and transfer parameters, 4) Uses DMA for non-blocking data transfer, 5) GetFunctionInfo revealed the complete implementation with hardware dependencies, 6) GetMMIOFunctionInfo confirmed register accesses and polling loops, 7) GetStructOrEnumInfo showed the I2C_HandleTypeDef structure used for state management, 8) GetFunctionCallStack revealed calls to HAL_DMA_Start_IT. The function fits the RECV category as it handles data reception with hardware dependencies that need replacement while preserving state management and buffer handling logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential receive in master mode an amount of data in non-blocking mode with DMA
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Seq_Receive_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Simulate DMA data reception */
        HAL_BE_In(hi2c->pBuffPtr, hi2c->XferSize);
        dmaxferstatus = HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
      if (dmaxferstatus == HAL_OK)
      {
        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_OK;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Seq_Receive_IT

```text
=== HAL_I2C_Master_Seq_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3843
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Seq_Receive_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  __IO uint32_t count = 0U;
  uint32_t enableIT = (I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* Wait until BUSY flag is reset */
      count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
      do
      {
        count--;
        if (count == 0U)
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          return HAL_BUSY;
        }
      }
      while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if ((hi2c->XferCount == 2U) && ((XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP)))
    {
      if (Prev_State == I2C_STATE_MASTER_BUSY_RX)
      {
        /* Disable Acknowledge */
        CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        /* Enable Pos */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

        /* Remove Enabling of IT_BUF, mean RXNE treatment, treat the 2 bytes through BTF */
        enableIT &= ~I2C_IT_BUF;
      }
      else
      {
        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
      }
    }
    else
    {
      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
    }

    /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
    /* Mean Previous state is same as current state */
    if ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
    {
      /* Generate Start */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Enable interrupts */
    __HAL_I2C_ENABLE_IT(hi2c, enableIT);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Sequential receive in master I2C mode using interrupts - configures I2C peripheral for interrupt-driven data reception
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function configures I2C hardware for interrupt-driven sequential receive operations. GetMMIOFunctionInfo showed multiple hardware register accesses (CR1 register operations, BUSY flag polling, interrupt enabling). The function sets up transfer parameters, configures I2C control registers, enables interrupts, but doesn't actually perform data transfer - it prepares the hardware for reception. This matches INIT classification: initialization/configuration function that sets up peripheral for operation. It's not CORE (no NVIC/OS operations), not RECV (doesn't transfer data), not IRQ (not an interrupt handler), not LOOP (polling loop is minor). The function preserves state management, parameter setup, and locking mechanisms while removing hardware-specific operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential receive in master I2C mode an amount of data in non-blocking mode with Interrupt
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Seq_Receive_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  uint32_t enableIT = (I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* [LOOP REMOVED] Skip waiting for BUSY flag reset - assume bus is ready */
      /* Original loop: while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET); */
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware-specific I2C peripheral enable/disable */

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if ((hi2c->XferCount == 2U) && ((XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP)))
    {
      if (Prev_State == I2C_STATE_MASTER_BUSY_RX)
      {
        /* Skip hardware ACK/POS configuration */
        /* Remove Enabling of IT_BUF, mean RXNE treatment, treat the 2 bytes through BTF */
        enableIT &= ~I2C_IT_BUF;
      }
      else
      {
        /* Skip hardware ACK configuration */
      }
    }
    else
    {
      /* Skip hardware ACK configuration */
    }

    /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
    /* Mean Previous state is same as current state */
    if ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
    {
      /* Skip hardware START generation */
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Skip hardware interrupt enabling */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Seq_Transmit_DMA

```text
=== HAL_I2C_Master_Seq_Transmit_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3663
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Seq_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  __IO uint32_t count      = 0x00U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* Wait until BUSY flag is reset */
      count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
      do
      {
        count--;
        if (count == 0U)
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          return HAL_BUSY;
        }
      }
      while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmatx, (uint32_t)hi2c->pBuffPtr, (uint32_t)&hi2c->Instance->DR, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
        /* Mean Previous state is same as current state */
        if ((Prev_State != I2C_STATE_MASTER_BUSY_TX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
        {
          /* Generate Start */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
        }

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */

        /* If XferOptions is not associated to a new frame, mean no start bit is request, enable directly the DMA request */
        /* In other cases, DMA request is enabled after Slave address treatment in IRQHandler */
        if ((XferOptions == I2C_NEXT_FRAME) || (XferOptions == I2C_LAST_FRAME) || (XferOptions == I2C_LAST_FRAME_NO_STOP))
        {
          /* Enable DMA Request */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);
        }

        /* Enable EVT and ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
      /* Mean Previous state is same as current state */
      if ((Prev_State != I2C_STATE_MASTER_BUSY_TX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
      {
        /* Generate Start */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
      }

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable EVT, BUF and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Sequential transmit in master I2C mode using DMA for non-blocking data transmission with support for repeated start conditions
- 是否需要替换：是
- 分类/替换原因：This function initializes and configures I2C peripheral for DMA-based transmission. It contains hardware register accesses (CR1, CR2), polling loops for BUSY flag, DMA configuration, and interrupt enable operations. It manages I2C state machine transitions and maintains transfer parameters. According to classification priority: Not CORE (no NVIC/OS/VTOR), not RECV (transmit function), not IRQ (not an interrupt handler), not LOOP (more complex than simple loop). Best classified as INIT as it sets up peripheral for operation, configures DMA, and manages initialization state.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential transmit in master I2C mode an amount of data in non-blocking mode with DMA.
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Seq_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* Skip hardware busy flag wait loop - assume not busy */
      /* [LOOP REMOVED] Waited for hardware BUSY flag reset */
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Skip hardware DMA start - assume success */
        dmaxferstatus = HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Skip hardware acknowledge enable */
        /* Skip hardware start generation */
        
        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */

        /* Skip hardware DMA request enable */
        /* Skip hardware interrupt enable */

        /* Simulate data transmission */
        HAL_BE_Out(hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Skip hardware acknowledge enable */
      /* Skip hardware start generation */
      
      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Skip hardware interrupt enable */
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Seq_Transmit_IT

```text
=== HAL_I2C_Master_Seq_Transmit_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3568
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Seq_Transmit_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;
  __IO uint32_t count      = 0x00U;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* Wait until BUSY flag is reset */
      count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
      do
      {
        count--;
        if (count == 0U)
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          return HAL_BUSY;
        }
      }
      while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
    /* Mean Previous state is same as current state */
    if ((Prev_State != I2C_STATE_MASTER_BUSY_TX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
    {
      /* Generate Start */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Sequential transmit in master I2C mode using interrupts, handling repeated start conditions for direction changes during transfer
- 是否需要替换：是
- 分类/替换原因：Function performs I2C peripheral initialization and configuration for interrupt-driven sequential transmission. Contains hardware register accesses (I2C CR1 operations, BUSY flag polling loop, interrupt enablement) that need removal while preserving state management, transfer parameter setup, and lock/unlock mechanisms. Classified as INIT because it sets up the peripheral for operation rather than performing data transmission (which would be handled by interrupt handlers) or being a pure driver operation. The polling loop is handled within INIT classification by skipping the wait. No CORE operations (NVIC/OS/VTOR) present.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential transmit in master I2C mode an amount of data in non-blocking mode with Interrupt.
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Seq_Transmit_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  __IO uint32_t Prev_State = 0x00U;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Check Busy Flag only if FIRST call of Master interface */
    if ((READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP) || (XferOptions == I2C_FIRST_AND_LAST_FRAME) || (XferOptions == I2C_FIRST_FRAME))
    {
      /* [LOOP REMOVED] Skip waiting for BUSY flag reset - assume not busy */
      /* Original: Wait until BUSY flag is reset with timeout */
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled - skip hardware check */
    /* Original: if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE) */
    /* Assume peripheral is enabled for simulation */

    /* Skip hardware configuration: Disable Pos */
    /* Original: CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS); */

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;
    hi2c->Devaddress  = DevAddress;

    Prev_State = hi2c->PreviousState;

    /* If transfer direction not change and there is no request to start another frame, do not generate Restart Condition */
    /* Mean Previous state is same as current state */
    if ((Prev_State != I2C_STATE_MASTER_BUSY_TX) || (IS_I2C_TRANSFER_OTHER_OPTIONS_REQUEST(XferOptions) == 1))
    {
      /* Skip hardware: Generate Start */
      /* Original: SET_BIT(hi2c->Instance->CR1, I2C_CR1_START); */
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Skip hardware interrupt enablement */
    /* Original: __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR); */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Transmit

```text
=== HAL_I2C_Master_Transmit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1056
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Transmit(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BUSY, SET, I2C_TIMEOUT_BUSY_FLAG, tickstart) != HAL_OK)
    {
      return HAL_BUSY;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State       = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode        = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Send Slave Address */
    if (I2C_MasterRequestWrite(hi2c, DevAddress, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    while (hi2c->XferSize > 0U)
    {
      /* Wait until TXE flag is set */
      if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
      {
        if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
        {
          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
        }
        return HAL_ERROR;
      }

      /* Write data to DR */
      hi2c->Instance->DR = *hi2c->pBuffPtr;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
      hi2c->XferSize--;

      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET) && (hi2c->XferSize != 0U))
      {
        /* Write data to DR */
        hi2c->Instance->DR = *hi2c->pBuffPtr;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferCount--;
        hi2c->XferSize--;
      }

      /* Wait until BTF flag is set */
      if (I2C_WaitOnBTFFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
      {
        if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
        {
          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
        }
        return HAL_ERROR;
      }
    }

    /* Generate Stop */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits data in master mode over I2C interface in blocking mode
- 是否需要替换：是
- 分类/替换原因：This function performs data transmission (I/O operations) which falls under the RECV category. Analysis shows: 1) Contains hardware register accesses (hi2c->Instance->CR1, hi2c->Instance->DR), 2) Uses polling loops waiting for hardware flags (I2C_WaitOnFlagUntilTimeout, I2C_WaitOnTXEFlagUntilTimeout, I2C_WaitOnBTFFlagUntilTimeout), 3) Manages buffer pointers and transfer state, 4) Not a CORE function (no NVIC/OS/VTOR operations), 5) Not an IRQ handler, 6) Not an initialization function. The replacement removes hardware operations while preserving state management, buffer handling, and locking mechanisms.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Master_Transmit(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait */
    /* [LOOP REMOVED] Waited for hardware BUSY flag */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip I2C peripheral enable check */
    /* [HARDWARE REMOVED] Check if I2C is already enabled */

    /* Skip Disable Pos */
    /* [HARDWARE REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS); */

    hi2c->State       = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode        = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Skip sending slave address */
    /* [HARDWARE REMOVED] I2C_MasterRequestWrite */

    /* Skip clearing ADDR flag */
    /* [HARDWARE REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

    /* Simulate data transmission without hardware */
    while (hi2c->XferSize > 0U)
    {
      /* Skip waiting for TXE flag */
      /* [LOOP REMOVED] Waited for hardware TXE flag */

      /* Skip writing data to DR register */
      /* [HARDWARE REMOVED] hi2c->Instance->DR = *hi2c->pBuffPtr; */

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
      hi2c->XferSize--;

      if ((/* Simulate BTF flag as not set */ 0) && (hi2c->XferSize != 0U))
      {
        /* Skip writing second data to DR register */
        /* [HARDWARE REMOVED] hi2c->Instance->DR = *hi2c->pBuffPtr; */

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferCount--;
        hi2c->XferSize--;
      }

      /* Skip waiting for BTF flag */
      /* [LOOP REMOVED] Waited for hardware BTF flag */
    }

    /* Skip generating Stop condition */
    /* [HARDWARE REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP); */

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Transmit_DMA

```text
=== HAL_I2C_Master_Transmit_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1962
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;
  HAL_StatusTypeDef dmaxferstatus;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferM1CpltCallback = NULL;
        hi2c->hdmatx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmatx, (uint32_t)hi2c->pBuffPtr, (uint32_t)&hi2c->Instance->DR, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */

        /* Enable EVT and ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

        /* Enable DMA Request */
        SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        /* Generate Start */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Generate Start */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable EVT, BUF and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits data in I2C master mode using DMA for non-blocking communication
- 是否需要替换：是
- 分类/替换原因：This function performs critical data I/O operations (DMA-based transmission) and contains hardware register accesses for I2C configuration. GetFunctionInfo revealed the function sets up DMA transfer, manages I2C state machine, and contains polling loops for BUSY flag. GetMMIOFunctionInfo confirmed hardware register accesses. The function was classified as RECV because it handles data transmission (even though via DMA) and requires replacement of hardware operations while preserving state management, callback setup, and error handling. It's not CORE (no NVIC/OS operations), not IRQ (not an interrupt handler), not INIT (more than just initialization - actual data transfer), and not LOOP (has polling but main purpose is data transmission).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Transmit in master mode an amount of data in non-blocking mode with DMA
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef dmaxferstatus;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait loop - assume bus is ready */
    /* [LOOP REMOVED] Waited for hardware BUSY flag */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferM1CpltCallback = NULL;
        hi2c->hdmatx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Simulate DMA start - assume success */
        dmaxferstatus = HAL_OK;
        /* Simulate data transmission */
        HAL_BE_Out(Size);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Skip hardware interrupt enables - assume interrupts are handled by emulator */
        /* [HARDWARE REMOVED] Enabled I2C interrupts */
        /* [HARDWARE REMOVED] Enabled DMA Request */
        /* [HARDWARE REMOVED] Enabled Acknowledge */
        /* [HARDWARE REMOVED] Generated Start condition */
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Skip hardware operations for zero-size transfer */
      /* [HARDWARE REMOVED] Enabled Acknowledge */
      /* [HARDWARE REMOVED] Generated Start condition */

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Skip hardware interrupt enables */
      /* [HARDWARE REMOVED] Enabled I2C interrupts */
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Master_Transmit_IT

```text
=== HAL_I2C_Master_Transmit_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1679
- 函数内容：HAL_StatusTypeDef HAL_I2C_Master_Transmit_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */
    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    /* Generate Start */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initiates I2C master mode data transmission using interrupt-driven (non-blocking) communication by setting up transfer parameters, enabling interrupts, and generating start condition.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function sets up I2C transfer parameters (buffer, size, device address), manages state transitions, enables peripheral interrupts, and generates start condition but doesn't perform actual data transmission (which happens in interrupt handler). GetMMIOFunctionInfo identified hardware register accesses including polling BUSY flag, checking/enabling peripheral control registers, and setting START bit. The function is classified as INIT because: 1) It initializes transfer state and parameters in the handle structure, 2) It enables peripheral interrupts for the actual data transfer, 3) It generates the start condition to begin transmission, 4) It returns immediately (non-blocking) after setup. The replacement removes hardware-dependent operations (polling loop, register accesses) while preserving state management, buffer pointer assignment, and locking mechanisms.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Transmit in master mode an amount of data in non-blocking mode with Interrupt
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Master_Transmit_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size)
{
  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MASTER;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */
    /* Enable EVT, BUF and ERR interrupt */
    /* [HARDWARE REMOVED] __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR); */

    /* Generate Start */
    /* [HARDWARE REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_START); */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Read

```text
=== HAL_I2C_Mem_Read 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：2626
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Read(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BUSY, SET, I2C_TIMEOUT_BUSY_FLAG, tickstart) != HAL_OK)
    {
      return HAL_BUSY;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Send Slave Address and Memory Address */
    if (I2C_RequestMemoryRead(hi2c, DevAddress, MemAddress, MemAddSize, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    if (hi2c->XferSize == 0U)
    {
      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    else if (hi2c->XferSize == 1U)
    {
      /* Disable Acknowledge */
      CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    else if (hi2c->XferSize == 2U)
    {
      /* Disable Acknowledge */
      CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Enable Pos */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }
    else
    {
      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }

    while (hi2c->XferSize > 0U)
    {
      if (hi2c->XferSize <= 3U)
      {
        /* One byte */
        if (hi2c->XferSize == 1U)
        {
          /* Wait until RXNE flag is set */
          if (I2C_WaitOnRXNEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
        /* Two bytes */
        else if (hi2c->XferSize == 2U)
        {
          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
        /* 3 Last bytes */
        else
        {
          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Wait until BTF flag is set */
          if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BTF, RESET, Timeout, tickstart) != HAL_OK)
          {
            return HAL_ERROR;
          }

          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;

          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
      }
      else
      {
        /* Wait until RXNE flag is set */
        if (I2C_WaitOnRXNEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
        {
          return HAL_ERROR;
        }

        /* Read data from DR */
        *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferSize--;
        hi2c->XferCount--;

        if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET)
        {
          if (hi2c->XferSize == 3U)
          {
            /* Disable Acknowledge */
            CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
          }
          /* Read data from DR */
          *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

          /* Increment Buffer pointer */
          hi2c->pBuffPtr++;

          /* Update counter */
          hi2c->XferSize--;
          hi2c->XferCount--;
        }
      }
    }

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Reads data from a specific memory address of an I2C device in blocking mode
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) Function performs critical data I/O operations (reading from I2C device memory via hi2c->Instance->DR register); 2) Contains multiple hardware register accesses (CR1, DR registers) and polling loops for hardware flags (BUSY, RXNE, BTF); 3) Manages data buffers and transfer state; 4) Not CORE (no NVIC/OS/VTOR operations), not IRQ (not an interrupt handler), not INIT (not initialization), not LOOP (primary purpose is data reception, not just loop waiting). Fits RECV category as it performs data reception from peripheral with hardware dependencies that need simulation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Mem_Read(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Simulate data reception using HAL_BE_In */
    if (Size > 0)
    {
      HAL_BE_In(pData, Size);
    }

    /* Update buffer pointer and counters to match what would happen after reading */
    hi2c->pBuffPtr += Size;
    hi2c->XferSize = 0;
    hi2c->XferCount = 0;

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Read_DMA

```text
=== HAL_I2C_Mem_Read_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3236
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Read_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();
  __IO uint32_t count = 0U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferM1CpltCallback = NULL;
        hi2c->hdmarx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmarx, (uint32_t)&hi2c->Instance->DR, (uint32_t)hi2c->pBuffPtr, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Send Slave Address and Memory Address */
        if (I2C_RequestMemoryRead(hi2c, DevAddress, MemAddress, MemAddSize, I2C_TIMEOUT_FLAG, tickstart) != HAL_OK)
        {
          /* Abort the ongoing DMA */
          dmaxferstatus = HAL_DMA_Abort_IT(hi2c->hdmarx);

          /* Prevent unused argument(s) compilation and MISRA warning */
          UNUSED(dmaxferstatus);

          /* Set the unused I2C DMA transfer complete callback to NULL */
          hi2c->hdmarx->XferCpltCallback = NULL;

          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          hi2c->XferSize = 0U;
          hi2c->XferCount = 0U;

          /* Disable I2C peripheral to prevent dummy data in buffer */
          __HAL_I2C_DISABLE(hi2c);

          return HAL_ERROR;
        }

        if (hi2c->XferSize == 1U)
        {
          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
        }
        else
        {
          /* Enable Last DMA bit */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);
        }

        /* Clear ADDR flag */
        __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */
        /* Enable ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_ERR);

        /* Enable DMA Request */
        hi2c->Instance->CR2 |= I2C_CR2_DMAEN;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Send Slave Address and Memory Address */
      if (I2C_RequestMemoryRead(hi2c, DevAddress, MemAddress, MemAddSize, I2C_TIMEOUT_FLAG, tickstart) != HAL_OK)
      {
        return HAL_ERROR;
      }

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

      hi2c->State = HAL_I2C_STATE_READY;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Reads data from a specific memory address of an I2C device using DMA in non-blocking mode
- 是否需要替换：是
- 分类/替换原因：This function is classified as RECV because it performs critical data reception operations from I2C device memory using DMA. Analysis with GetFunctionInfo and GetMMIOFunctionInfo revealed hardware register accesses (I2C CR1, CR2, DR registers), polling loops for BUSY flag, DMA operations, and interrupt enables. The function's primary purpose is data reception with DMA buffer management, making it a RECV type. The replacement preserves state management, error handling, callback setup, and locking mechanisms while removing hardware dependencies and simulating data reception with HAL_BE_In().
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Reads an amount of data in non-blocking mode with DMA from a specific memory address.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  MemAddress Internal memory address
* @param  MemAddSize Size of internal memory address
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be read
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Mem_Read_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();
  __IO uint32_t count = 0U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* [LOOP REMOVED] Skip waiting for BUSY flag reset - assume not busy */
    /* Original: while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET); */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware enable check and peripheral enable */
    /* Original: if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE) { __HAL_I2C_ENABLE(hi2c); } */
    /* Original: CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS); */

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmarx->XferHalfCpltCallback = NULL;
        hi2c->hdmarx->XferM1CpltCallback = NULL;
        hi2c->hdmarx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmarx->XferAbortCallback = NULL;

        /* Simulate DMA start - skip hardware DMA operations */
        dmaxferstatus = HAL_OK; /* Assume DMA start succeeds */
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Simulate data reception using HAL_BE_In */
        if (hi2c->XferSize > 0)
        {
          HAL_BE_In(hi2c->pBuffPtr, hi2c->XferSize);
        }

        /* Skip hardware operations: I2C_RequestMemoryRead, flag clearing, interrupt enables */
        /* Original: if (I2C_RequestMemoryRead(hi2c, DevAddress, MemAddress, MemAddSize, I2C_TIMEOUT_FLAG, tickstart) != HAL_OK) */
        /* Original: CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK) or SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST) */
        /* Original: __HAL_I2C_CLEAR_ADDRFLAG(hi2c) */
        /* Original: __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_ERR) */
        /* Original: hi2c->Instance->CR2 |= I2C_CR2_DMAEN */

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Update transfer counters to indicate completion */
        hi2c->XferCount = 0U;
        hi2c->XferSize = 0U;
        
        /* Update state to indicate transfer is complete */
        hi2c->State = HAL_I2C_STATE_READY;
        hi2c->Mode = HAL_I2C_MODE_NONE;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Zero-size transfer case */
      /* Skip hardware operations: I2C_RequestMemoryRead, flag clearing, stop generation */
      /* Original: if (I2C_RequestMemoryRead(hi2c, DevAddress, MemAddress, MemAddSize, I2C_TIMEOUT_FLAG, tickstart) != HAL_OK) */
      /* Original: __HAL_I2C_CLEAR_ADDRFLAG(hi2c) */
      /* Original: SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) */

      hi2c->State = HAL_I2C_STATE_READY;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);
    }

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Read_IT

```text
=== HAL_I2C_Mem_Read_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：2963
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Read_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    /* Enable Acknowledge */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    /* Generate Start */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    if (hi2c->XferSize > 0U)
    {
      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable EVT, BUF and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);
    }
    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes I2C peripheral for reading data from a specific memory address using interrupt mode (non-blocking operation).
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) Function sets up I2C peripheral for memory read operation in interrupt mode, 2) Contains hardware register accesses (CR1 configuration, BUSY flag polling, interrupt enables) that need removal, 3) Preserves important state management (State, Mode, ErrorCode updates) and transfer parameter setup (pBuffPtr, XferCount, etc.), 4) Not a CORE function (no NVIC/OS/VTOR operations), 5) Not a RECV function (doesn't actually read data - sets up hardware for interrupt-driven reading), 6) Not an IRQ function (not an interrupt handler). Classification as INIT because it initializes peripheral for specific operation and contains hardware initialization logic that needs replacement.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Read an amount of data in non-blocking mode with Interrupt from a specific memory address
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address
* @param  MemAddress Internal memory address
* @param  MemAddSize Size of internal memory address
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Mem_Read_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    if (hi2c->XferSize > 0U)
    {
      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */

      /* Enable EVT, BUF and ERR interrupt */
      /* [INIT REMOVED] Hardware interrupt enable removed for simulation */
    }
    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Write

```text
=== HAL_I2C_Mem_Write 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：2503
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Write(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_BUSY, SET, I2C_TIMEOUT_BUSY_FLAG, tickstart) != HAL_OK)
    {
      return HAL_BUSY;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Send Slave Address and Memory Address */
    if (I2C_RequestMemoryWrite(hi2c, DevAddress, MemAddress, MemAddSize, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    while (hi2c->XferSize > 0U)
    {
      /* Wait until TXE flag is set */
      if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
      {
        if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
        {
          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
        }
        return HAL_ERROR;
      }

      /* Write data to DR */
      hi2c->Instance->DR = *hi2c->pBuffPtr;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferSize--;
      hi2c->XferCount--;

      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET) && (hi2c->XferSize != 0U))
      {
        /* Write data to DR */
        hi2c->Instance->DR = *hi2c->pBuffPtr;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferSize--;
        hi2c->XferCount--;
      }
    }

    /* Wait until BTF flag is set */
    if (I2C_WaitOnBTFFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
    {
      if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
      {
        /* Generate Stop */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
      }
      return HAL_ERROR;
    }

    /* Generate Stop */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Blocking mode I2C memory write function that writes data to a specific memory address of an I2C device
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a data transmission function that writes to I2C device memory. GetMMIOFunctionInfo identified hardware register accesses (writing to hi2c->Instance->DR) and polling loops waiting for hardware flags. The function performs critical data I/O operations with hardware dependencies but also manages I2C state machine and buffer pointers. Classification as RECV is appropriate because: 1) It performs data transmission (writing to I2C device), 2) Contains hardware-dependent data transfer operations, 3) Needs to preserve non-I/O logic (state updates, buffer management), 4) Not CORE (no NVIC/OS/VTOR operations), 5) Not IRQ (not an interrupt handler), 6) Not INIT (not initialization, though it does state initialization), 7) Contains LOOP elements but overall function purpose is data transmission.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Mem_Write(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait - assume I2C is not busy */
    /* [LOOP REMOVED] Waited for hardware BUSY flag */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware enable check and peripheral enable */
    /* [HARDWARE REMOVED] Check if I2C is already enabled and enable if needed */
    /* [HARDWARE REMOVED] Disable Pos */

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Skip hardware address request - assume successful */
    /* [HARDWARE REMOVED] Send Slave Address and Memory Address */

    /* Simulate data transmission by skipping hardware writes */
    /* Data would normally be written to hi2c->Instance->DR */
    /* Instead, we just update buffer pointers and counters */
    while (hi2c->XferSize > 0U)
    {
      /* Skip TXE flag wait - assume ready to transmit */
      /* [LOOP REMOVED] Waited for hardware TXE flag */

      /* Skip hardware data write */
      /* [HARDWARE REMOVED] Write data to DR: hi2c->Instance->DR = *hi2c->pBuffPtr; */

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferSize--;
      hi2c->XferCount--;

      /* Skip BTF flag check and additional write */
      /* [HARDWARE REMOVED] Check BTF flag and write additional data if needed */
    }

    /* Skip BTF flag wait - assume transfer complete */
    /* [LOOP REMOVED] Waited for hardware BTF flag */

    /* Skip hardware stop generation */
    /* [HARDWARE REMOVED] Generate Stop: SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP); */

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Write_DMA

```text
=== HAL_I2C_Mem_Write_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：3054
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Write_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;
  HAL_StatusTypeDef dmaxferstatus;

  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferM1CpltCallback = NULL;
        hi2c->hdmatx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Enable the DMA stream */
        dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmatx, (uint32_t)hi2c->pBuffPtr, (uint32_t)&hi2c->Instance->DR, hi2c->XferSize);
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Send Slave Address and Memory Address */
        if (I2C_RequestMemoryWrite(hi2c, DevAddress, MemAddress, MemAddSize, I2C_TIMEOUT_FLAG, tickstart) != HAL_OK)
        {
          /* Abort the ongoing DMA */
          dmaxferstatus = HAL_DMA_Abort_IT(hi2c->hdmatx);

          /* Prevent unused argument(s) compilation and MISRA warning */
          UNUSED(dmaxferstatus);

          /* Set the unused I2C DMA transfer complete callback to NULL */
          hi2c->hdmatx->XferCpltCallback = NULL;

          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          hi2c->XferSize = 0U;
          hi2c->XferCount = 0U;

          /* Disable I2C peripheral to prevent dummy data in buffer */
          __HAL_I2C_DISABLE(hi2c);

          return HAL_ERROR;
        }

        /* Clear ADDR flag */
        __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Note : The I2C interrupts must be enabled after unlocking current process
        to avoid the risk of I2C interrupt handle execution before current
        process unlock */
        /* Enable ERR interrupt */
        __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_ERR);

        /* Enable DMA Request */
        SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

        return HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_SIZE;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Writes data to a specific memory address of an I2C device using DMA in non-blocking mode
- 是否需要替换：是
- 分类/替换原因：This function performs data transmission (writing to I2C device memory) using DMA, which fits the RECV category for data transmission/reception functions. GetFunctionInfo revealed it handles DMA buffer management and data transfer. GetMMIOFunctionInfo showed hardware register accesses for I2C peripheral control, flag checking, and interrupt enabling. The function contains a polling loop waiting for BUSY flag, sets up DMA callbacks, and manages I2C state machine. It was classified as RECV rather than IRQ (not an interrupt handler) or INIT (not initialization). The replacement preserves all non-hardware logic including state machine updates, transfer parameter setup, DMA callback configuration, and error handling while removing hardware-specific operations and replacing them with simulation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Write an amount of data in non-blocking mode with DMA to a specific memory address
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  MemAddress Internal memory address
* @param  MemAddSize Size of internal memory address
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Mem_Write_DMA(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef dmaxferstatus;

  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait loop - assume I2C is ready */
    /* [LOOP REMOVED] Waited for hardware BUSY flag to clear */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    if (hi2c->XferSize > 0U)
    {
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA transfer complete callback */
        hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

        /* Set the DMA error callback */
        hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

        /* Set the unused DMA callbacks to NULL */
        hi2c->hdmatx->XferHalfCpltCallback = NULL;
        hi2c->hdmatx->XferM1CpltCallback = NULL;
        hi2c->hdmatx->XferM1HalfCpltCallback = NULL;
        hi2c->hdmatx->XferAbortCallback = NULL;

        /* Simulate DMA start - assume success */
        dmaxferstatus = HAL_OK;
        /* [HARDWARE REMOVED] HAL_DMA_Start_IT call removed */
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }

      if (dmaxferstatus == HAL_OK)
      {
        /* Simulate sending slave address and memory address - assume success */
        /* [HARDWARE REMOVED] I2C_RequestMemoryWrite call removed */

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        /* Simulate data transmission using HAL_BE_Out */
        if (Size > 0)
        {
          HAL_BE_Out(Size); /* Simulate data transmission */
        }

        return HAL_OK;
      }
      else
      {
        /* Update I2C state */
        hi2c->State     = HAL_I2C_STATE_READY;
        hi2c->Mode      = HAL_I2C_MODE_NONE;

        /* Update I2C error code */
        hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_SIZE;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Mem_Write_IT

```text
=== HAL_I2C_Mem_Write_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：2878
- 函数内容：HAL_StatusTypeDef HAL_I2C_Mem_Write_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  __IO uint32_t count = 0U;

  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Wait until BUSY flag is reset */
    count = I2C_TIMEOUT_BUSY_FLAG * (SystemCoreClock / 25U / 1000U);
    do
    {
      count--;
      if (count == 0U)
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        return HAL_BUSY;
      }
    }
    while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BUSY) != RESET);

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    /* Generate Start */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes and starts an I2C memory write operation in interrupt mode, setting up transfer parameters and enabling interrupts for non-blocking data transmission.
- 是否需要替换：是
- 分类/替换原因：This function initializes an I2C memory write operation in interrupt mode. It contains hardware register accesses (CR1 operations, BUSY flag polling) that need to be removed, while preserving the interrupt enabling for emulator simulation. The function sets up transfer parameters in the I2C handle structure, updates the state machine, and enables I2C interrupts. It is classified as INIT because it prepares the peripheral for operation rather than handling data transmission directly (which would happen in the interrupt handler). The replacement removes hardware-specific operations like register accesses and polling loops while preserving interrupt enabling and state management.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Write an amount of data in non-blocking mode with Interrupt to a specific memory address
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  MemAddress Internal memory address
* @param  MemAddSize Size of internal memory address
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Mem_Write_IT(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint8_t *pData, uint16_t Size)
{
  /* Check the parameters */
  assert_param(IS_I2C_MEMADD_SIZE(MemAddSize));

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    /* Skip BUSY flag wait loop - assume not busy in simulated environment */
    /* [LOOP REMOVED] Waited for hardware BUSY flag */

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware peripheral enable check and enable */
    /* Hardware peripheral configuration removed */

    hi2c->State     = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode      = HAL_I2C_MODE_MEM;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;
    hi2c->Devaddress  = DevAddress;
    hi2c->Memaddress  = MemAddress;
    hi2c->MemaddSize  = MemAddSize;
    hi2c->EventCount  = 0U;

    /* Skip hardware START generation */
    /* Hardware START generation removed */

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
    to avoid the risk of I2C interrupt handle execution before current
    process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Receive

```text
=== HAL_I2C_Slave_Receive 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1558
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Receive(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    if ((pData == NULL) || (Size == (uint16_t)0))
    {
      return HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State       = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode        = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Enable Address Acknowledge */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    /* Wait until ADDR flag is set */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, RESET, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    while (hi2c->XferSize > 0U)
    {
      /* Wait until RXNE flag is set */
      if (I2C_WaitOnRXNEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
      {
        /* Disable Address Acknowledge */
        CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        return HAL_ERROR;
      }

      /* Read data from DR */
      *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferSize--;
      hi2c->XferCount--;

      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET) && (hi2c->XferSize != 0U))
      {
        /* Read data from DR */
        *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferSize--;
        hi2c->XferCount--;
      }
    }

    /* Wait until STOP flag is set */
    if (I2C_WaitOnSTOPFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
    {
      /* Disable Address Acknowledge */
      CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      return HAL_ERROR;
    }

    /* Clear STOP flag */
    __HAL_I2C_CLEAR_STOPFLAG(hi2c);

    /* Disable Address Acknowledge */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receive data in slave mode using blocking mode for I2C communication
- 是否需要替换：是
- 分类/替换原因：This function performs critical data reception from I2C peripheral hardware. GetFunctionInfo shows it reads data from hi2c->Instance->DR register and contains hardware polling loops. GetMMIOFunctionInfo confirms register accesses. It manages buffer pointers, transfer counters, and state machine updates. According to classification priority, this is a RECV function because it performs data I/O operations with hardware dependencies that need to be replaced with simulation while preserving non-hardware logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_I2C_Slave_Receive(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    if ((pData == NULL) || (Size == (uint16_t)0))
    {
      return HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State       = HAL_I2C_STATE_BUSY_RX;
    hi2c->Mode        = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Simulate data reception */
    HAL_BE_In(pData, Size);

    /* Update buffer pointer and counters to match expected behavior */
    hi2c->pBuffPtr += Size;
    hi2c->XferSize = 0;
    hi2c->XferCount = 0;

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Seq_Receive_DMA

```text
=== HAL_I2C_Slave_Seq_Receive_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：4485
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Seq_Receive_DMA(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Disable Interrupts, to prevent preemption during treatment in case of multicall */
    __HAL_I2C_DISABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

    /* I2C cannot manage full duplex exchange so disable previous IT enabled if any */
    /* and then toggle the HAL slave RX state to TX state */
    if (hi2c->State == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
      {
        /* Abort DMA Xfer if any */
        if (hi2c->hdmarx != NULL)
        {
          CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

          /* Set the I2C DMA Abort callback :
           will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
          hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

          /* Abort DMA RX */
          if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
          {
            /* Call Directly XferAbortCallback function in case of error */
            hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
          }
        }
      }
    }
    else if (hi2c->State == HAL_I2C_STATE_BUSY_TX_LISTEN)
    {
      if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
      {
        CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

        /* Abort DMA Xfer if any */
        if (hi2c->hdmatx != NULL)
        {
          /* Set the I2C DMA Abort callback :
           will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
          hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

          /* Abort DMA TX */
          if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
          {
            /* Call Directly XferAbortCallback function in case of error */
            hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
          }
        }
      }
    }
    else
    {
      /* Nothing to do */
    }

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    if (hi2c->hdmarx != NULL)
    {
      /* Set the I2C DMA transfer complete callback */
      hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

      /* Set the DMA error callback */
      hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

      /* Set the unused DMA callbacks to NULL */
      hi2c->hdmarx->XferHalfCpltCallback = NULL;
      hi2c->hdmarx->XferAbortCallback = NULL;

      /* Enable the DMA stream */
      dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmarx, (uint32_t)&hi2c->Instance->DR, (uint32_t)hi2c->pBuffPtr, hi2c->XferSize);
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_LISTEN;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    if (dmaxferstatus == HAL_OK)
    {
      /* Enable Address Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Enable DMA Request */
      SET_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */
      /* Enable EVT and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

      return HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Sequential receive in slave mode using DMA for non-blocking data transfer with support for repeated start conditions during direction changes
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo, this function is primarily a data reception function (RECV) that receives data via I2C in slave mode using DMA. Key characteristics: 1) It receives data into a buffer (pData parameter), 2) Contains hardware register accesses (I2C CR1, CR2 registers, interrupt control), 3) Sets up DMA for data transfer, 4) Updates I2C handle state and transfer parameters. While it has some INIT characteristics (DMA setup, callback configuration), RECV takes priority according to the classification order (CORE > RECV > IRQ > INIT > LOOP). The function needs replacement to remove hardware-dependent operations while preserving data reception simulation, state updates, and callback configurations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential receive in slave mode an amount of data in non-blocking mode with DMA
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Slave_Seq_Receive_DMA(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Disable Interrupts, to prevent preemption during treatment in case of multicall */
    /* Hardware interrupt disable removed for simulation */

    /* I2C cannot manage full duplex exchange so disable previous IT enabled if any */
    /* and then toggle the HAL slave RX state to TX state */
    if (hi2c->State == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      /* Hardware register check removed for simulation */
      /* Abort DMA Xfer if any */
      if (hi2c->hdmarx != NULL)
      {
        /* Hardware register clear removed for simulation */

        /* Set the I2C DMA Abort callback :
         will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA RX */
        if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
        }
      }
    }
    else if (hi2c->State == HAL_I2C_STATE_BUSY_TX_LISTEN)
    {
      /* Hardware register check removed for simulation */
      /* Hardware register clear removed for simulation */

      /* Abort DMA Xfer if any */
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA Abort callback :
         will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA TX */
        if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
        }
      }
    }
    else
    {
      /* Nothing to do */
    }

    /* Check if the I2C is already enabled - hardware check removed for simulation */
    /* Hardware enable removed for simulation */

    /* Disable Pos - hardware operation removed for simulation */

    hi2c->State     = HAL_I2C_STATE_BUSY_RX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    if (hi2c->hdmarx != NULL)
    {
      /* Set the I2C DMA transfer complete callback */
      hi2c->hdmarx->XferCpltCallback = I2C_DMAXferCplt;

      /* Set the DMA error callback */
      hi2c->hdmarx->XferErrorCallback = I2C_DMAError;

      /* Set the unused DMA callbacks to NULL */
      hi2c->hdmarx->XferHalfCpltCallback = NULL;
      hi2c->hdmarx->XferAbortCallback = NULL;

      /* Simulate data reception */
      HAL_BE_In(pData, Size);
      
      /* Simulate DMA start success */
      dmaxferstatus = HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_LISTEN;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    if (dmaxferstatus == HAL_OK)
    {
      /* Enable Address Acknowledge - hardware operation removed for simulation */

      /* Clear ADDR flag - hardware operation removed for simulation */

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Enable DMA Request - hardware operation removed for simulation */

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */
      /* Enable EVT and ERR interrupt - hardware operation removed for simulation */

      return HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Seq_Receive_IT

```text
=== HAL_I2C_Slave_Seq_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：4419
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Seq_Receive_IT(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_RX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Sets up sequential receive in I2C slave mode using interrupts, configuring the peripheral and transfer parameters for interrupt-driven data reception.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs hardware initialization for I2C slave sequential receive with interrupts. Analysis from GetFunctionInfo and GetMMIOFunctionInfo shows it: 1) Configures hardware registers (checks/enables I2C peripheral, clears POS bit, clears ADDR flag, enables interrupts), 2) Sets up transfer parameters (buffer pointer, size, options), 3) Updates I2C handle state machine, 4) Does not perform actual data reception (just sets up for it), 5) Is not an interrupt handler itself, 6) Does not involve NVIC/OS/VTOR configuration (not CORE). The replacement preserves all non-hardware logic (state updates, parameter setup, lock/unlock) while removing hardware-specific operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential receive in slave mode an amount of data in non-blocking mode with Interrupt
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Slave_Seq_Receive_IT(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware enable check and peripheral enable */
    /* Original: if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE) { __HAL_I2C_ENABLE(hi2c); } */

    /* Skip POS bit clearing */
    /* Original: CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS); */

    hi2c->State     = HAL_I2C_STATE_BUSY_RX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    /* Skip ADDR flag clearing */
    /* Original: __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */

    /* Skip interrupt enable */
    /* Original: __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR); */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Seq_Transmit_DMA

```text
=== HAL_I2C_Slave_Seq_Transmit_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：4245
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Seq_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Disable Interrupts, to prevent preemption during treatment in case of multicall */
    __HAL_I2C_DISABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

    /* I2C cannot manage full duplex exchange so disable previous IT enabled if any */
    /* and then toggle the HAL slave RX state to TX state */
    if (hi2c->State == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
      {
        /* Abort DMA Xfer if any */
        if (hi2c->hdmarx != NULL)
        {
          CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

          /* Set the I2C DMA Abort callback :
           will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
          hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

          /* Abort DMA RX */
          if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
          {
            /* Call Directly XferAbortCallback function in case of error */
            hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
          }
        }
      }
    }
    else if (hi2c->State == HAL_I2C_STATE_BUSY_TX_LISTEN)
    {
      if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
      {
        CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

        /* Abort DMA Xfer if any */
        if (hi2c->hdmatx != NULL)
        {
          /* Set the I2C DMA Abort callback :
           will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
          hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

          /* Abort DMA TX */
          if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
          {
            /* Call Directly XferAbortCallback function in case of error */
            hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
          }
        }
      }
    }
    else
    {
      /* Nothing to do */
    }

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    if (hi2c->hdmatx != NULL)
    {
      /* Set the I2C DMA transfer complete callback */
      hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

      /* Set the DMA error callback */
      hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

      /* Set the unused DMA callbacks to NULL */
      hi2c->hdmatx->XferHalfCpltCallback = NULL;
      hi2c->hdmatx->XferAbortCallback = NULL;

      /* Enable the DMA stream */
      dmaxferstatus = HAL_DMA_Start_IT(hi2c->hdmatx, (uint32_t)hi2c->pBuffPtr, (uint32_t)&hi2c->Instance->DR, hi2c->XferSize);
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_LISTEN;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    if (dmaxferstatus == HAL_OK)
    {
      /* Enable Address Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Note : The I2C interrupts must be enabled after unlocking current process
      to avoid the risk of I2C interrupt handle execution before current
      process unlock */
      /* Enable EVT and ERR interrupt */
      __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_ERR);

      /* Enable DMA Request */
      hi2c->Instance->CR2 |= I2C_CR2_DMAEN;

      return HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Sequential transmit in slave mode using DMA for non-blocking data transfer with support for repeated start conditions during direction changes.
- 是否需要替换：是
- 分类/替换原因：This function is classified as RECV because: 1) It performs data transmission operations (slave transmit) using DMA, 2) It contains critical data I/O operations (DMA setup for transferring data from memory to I2C), 3) It manages buffer pointers, transfer sizes, and state machine updates, 4) GetMMIOFunctionInfo revealed multiple hardware register accesses (CR1, CR2, DR registers) that need to be removed, 5) It's not CORE (no NVIC/OS/VTOR operations), not IRQ (not an interrupt handler), not INIT (not initialization), and not LOOP (no polling loops). The function needs replacement to remove hardware dependencies while preserving data transfer logic, state management, and DMA callback configuration.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential transmit in slave mode an amount of data in non-blocking mode with DMA
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Slave_Seq_Transmit_DMA(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  HAL_StatusTypeDef dmaxferstatus;

  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Disable Interrupts, to prevent preemption during treatment in case of multicall */
    /* Hardware interrupt disable removed for simulation */

    /* I2C cannot manage full duplex exchange so disable previous IT enabled if any */
    /* and then toggle the HAL slave RX state to TX state */
    if (hi2c->State == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      /* Abort DMA Xfer if any */
      if (hi2c->hdmarx != NULL)
      {
        /* Set the I2C DMA Abort callback :
         will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA RX */
        if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
        }
      }
    }
    else if (hi2c->State == HAL_I2C_STATE_BUSY_TX_LISTEN)
    {
      /* Abort DMA Xfer if any */
      if (hi2c->hdmatx != NULL)
      {
        /* Set the I2C DMA Abort callback :
         will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA TX */
        if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
        }
      }
    }
    else
    {
      /* Nothing to do */
    }

    hi2c->State     = HAL_I2C_STATE_BUSY_TX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    if (hi2c->hdmatx != NULL)
    {
      /* Set the I2C DMA transfer complete callback */
      hi2c->hdmatx->XferCpltCallback = I2C_DMAXferCplt;

      /* Set the DMA error callback */
      hi2c->hdmatx->XferErrorCallback = I2C_DMAError;

      /* Set the unused DMA callbacks to NULL */
      hi2c->hdmatx->XferHalfCpltCallback = NULL;
      hi2c->hdmatx->XferAbortCallback = NULL;

      /* Simulate DMA start - assume success */
      dmaxferstatus = HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_LISTEN;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA_PARAM;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    if (dmaxferstatus == HAL_OK)
    {
      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      /* Simulate data transmission */
      HAL_BE_Out(Size);

      return HAL_OK;
    }
    else
    {
      /* Update I2C state */
      hi2c->State     = HAL_I2C_STATE_READY;
      hi2c->Mode      = HAL_I2C_MODE_NONE;

      /* Update I2C error code */
      hi2c->ErrorCode |= HAL_I2C_ERROR_DMA;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Seq_Transmit_IT

```text
=== HAL_I2C_Slave_Seq_Transmit_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：4179
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Seq_Transmit_IT(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State     = HAL_I2C_STATE_BUSY_TX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */

    /* Enable EVT, BUF and ERR interrupt */
    __HAL_I2C_ENABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes I2C peripheral for sequential slave transmission in interrupt mode, setting up transfer parameters and enabling interrupts for event, buffer, and error handling.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) The function performs peripheral initialization and configuration for I2C slave transmission. 2) It contains hardware register accesses (checking/enabling I2C peripheral, clearing ADDR flag, enabling interrupts) that need to be removed. 3) It updates the I2C state machine (State, Mode, ErrorCode) and sets up transfer parameters (pBuffPtr, XferCount, XferSize, XferOptions). 4) It includes process locking/unlocking for thread safety. 5) It's not a CORE function (no NVIC/OS kernel/VTOR operations), not a RECV function (no data reception), not an IRQ function (not an interrupt handler), and not a LOOP function (no polling loops). The function fits the INIT classification as it prepares the peripheral for operation while preserving the state management and parameter setup logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sequential transmit in slave mode an amount of data in non-blocking mode with Interrupt
* @note   This interface allow to manage repeated start condition when a direction change during transfer
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for the specified I2C.
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  XferOptions Options of Transfer, value of @ref I2C_XferOptions_definition
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Slave_Seq_Transmit_IT(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t XferOptions)
{
  /* Check the parameters */
  assert_param(IS_I2C_TRANSFER_OPTIONS_REQUEST(XferOptions));

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Skip hardware-specific configuration */
    /* Original: Check if I2C is enabled and enable if needed */
    /* Original: Disable Pos bit */
    /* Original: Clear ADDR flag */

    hi2c->State     = HAL_I2C_STATE_BUSY_TX_LISTEN;
    hi2c->Mode      = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = XferOptions;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Note : The I2C interrupts must be enabled after unlocking current process
              to avoid the risk of I2C interrupt handle execution before current
              process unlock */

    /* Skip hardware interrupt enable */
    /* Original: Enable EVT, BUF and ERR interrupt */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_I2C_Slave_Transmit

```text
=== HAL_I2C_Slave_Transmit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：1428
- 函数内容：HAL_StatusTypeDef HAL_I2C_Slave_Transmit(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    /* Check if the I2C is already enabled */
    if ((hi2c->Instance->CR1 & I2C_CR1_PE) != I2C_CR1_PE)
    {
      /* Enable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);
    }

    /* Disable Pos */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_POS);

    hi2c->State       = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode        = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Enable Address Acknowledge */
    SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    /* Wait until ADDR flag is set */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, RESET, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    /* If 10bit addressing mode is selected */
    if (hi2c->Init.AddressingMode == I2C_ADDRESSINGMODE_10BIT)
    {
      /* Wait until ADDR flag is set */
      if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, RESET, Timeout, tickstart) != HAL_OK)
      {
        return HAL_ERROR;
      }

      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }

    while (hi2c->XferSize > 0U)
    {
      /* Wait until TXE flag is set */
      if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, tickstart) != HAL_OK)
      {
        /* Disable Address Acknowledge */
        CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        return HAL_ERROR;
      }

      /* Write data to DR */
      hi2c->Instance->DR = *hi2c->pBuffPtr;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
      hi2c->XferSize--;

      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET) && (hi2c->XferSize != 0U))
      {
        /* Write data to DR */
        hi2c->Instance->DR = *hi2c->pBuffPtr;

        /* Increment Buffer pointer */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferCount--;
        hi2c->XferSize--;
      }
    }

    /* Wait until AF flag is set */
    if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_AF, RESET, Timeout, tickstart) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Clear AF flag */
    __HAL_I2C_CLEAR_FLAG(hi2c, I2C_FLAG_AF);

    /* Disable Address Acknowledge */
    CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits data in I2C slave mode in blocking mode, sending data from buffer when addressed as a slave device
- 是否需要替换：是
- 分类/替换原因：Function performs critical data transmission I/O with hardware dependencies: contains MMIO register accesses (CR1, DR), polling loops waiting for hardware flags (ADDR, TXE, AF), and manages I2C state machine. GetMMIOFunctionInfo revealed multiple register access operations. Classified as RECV because it handles data transmission (sending data from buffer) with hardware dependencies, requiring removal of hardware operations while preserving buffer management and state updates.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Transmits in slave mode an amount of data in blocking mode.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  pData Pointer to data buffer
* @param  Size Amount of data to be sent
* @param  Timeout Timeout duration
* @retval HAL status
*/
HAL_StatusTypeDef HAL_I2C_Slave_Transmit(I2C_HandleTypeDef *hi2c, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
  /* Init tickstart for timeout management*/
  uint32_t tickstart = HAL_GetTick();

  if (hi2c->State == HAL_I2C_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    /* Process Locked */
    __HAL_LOCK(hi2c);

    hi2c->State       = HAL_I2C_STATE_BUSY_TX;
    hi2c->Mode        = HAL_I2C_MODE_SLAVE;
    hi2c->ErrorCode   = HAL_I2C_ERROR_NONE;

    /* Prepare transfer parameters */
    hi2c->pBuffPtr    = pData;
    hi2c->XferCount   = Size;
    hi2c->XferSize    = hi2c->XferCount;
    hi2c->XferOptions = I2C_NO_OPTION_FRAME;

    /* Skip hardware-specific flag waiting and register writes */
    /* [LOOP REMOVED] Original waited for ADDR flag */
    /* [LOOP REMOVED] Original cleared ADDR flag */

    /* If 10bit addressing mode is selected */
    if (hi2c->Init.AddressingMode == I2C_ADDRESSINGMODE_10BIT)
    {
      /* Skip additional ADDR flag handling for 10-bit mode */
      /* [LOOP REMOVED] Original waited for ADDR flag */
      /* [LOOP REMOVED] Original cleared ADDR flag */
    }

    /* Simulate data transmission - update buffer pointer and counters */
    while (hi2c->XferSize > 0U)
    {
      /* Skip waiting for TXE flag */
      /* [LOOP REMOVED] Original waited for TXE flag */

      /* Simulate writing data to DR - just update buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
      hi2c->XferSize--;

      if (hi2c->XferSize != 0U)
      {
        /* Simulate additional write when BTF flag is set */
        hi2c->pBuffPtr++;

        /* Update counter */
        hi2c->XferCount--;
        hi2c->XferSize--;
      }
    }

    /* Skip waiting for AF flag */
    /* [LOOP REMOVED] Original waited for AF flag */
    /* [LOOP REMOVED] Original cleared AF flag */

    /* Skip disabling Address Acknowledge in hardware */
    /* [REGISTER WRITE REMOVED] Original: CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK) */

    hi2c->State = HAL_I2C_STATE_READY;
    hi2c->Mode = HAL_I2C_MODE_NONE;

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_RCC_OscConfig

```text
=== HAL_RCC_OscConfig 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_rcc.c
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


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes RCC oscillators (HSE, HSI, LSE, LSI, and PLL) according to specified parameters in RCC_OscInitTypeDef structure
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This is an initialization function that configures hardware oscillators and PLL; 2) Contains extensive MMIO operations (register writes to RCC and PWR peripherals, hardware configuration macros); 3) Has multiple polling loops waiting for hardware status flags; 4) Performs parameter validation and structure initialization that should be preserved; 5) Called from SystemClock_Config during system initialization; 6) Not CORE (no NVIC/OS/VTOR configuration), not RECV (no data I/O), not IRQ (not interrupt handler). Classification as INIT follows priority order: CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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
    /* When the HSE is used as system clock or clock source for PLL in these cases HSE will not disabled */
    /* Skip hardware-specific checks and configuration */
  }
  
  /*----------------------------- HSI Configuration --------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_HSI) == RCC_OSCILLATORTYPE_HSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_HSI(RCC_OscInitStruct->HSIState));
    assert_param(IS_RCC_CALIBRATION_VALUE(RCC_OscInitStruct->HSICalibrationValue));
    /* Skip hardware-specific checks and configuration */
  }
  
  /*------------------------------ LSI Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSI) == RCC_OSCILLATORTYPE_LSI)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSI(RCC_OscInitStruct->LSIState));
    /* Skip hardware-specific checks and configuration */
  }
  
  /*------------------------------ LSE Configuration -------------------------*/
  if (((RCC_OscInitStruct->OscillatorType) & RCC_OSCILLATORTYPE_LSE) == RCC_OSCILLATORTYPE_LSE)
  {
    /* Check the parameters */
    assert_param(IS_RCC_LSE(RCC_OscInitStruct->LSEState));
    /* Skip hardware-specific checks and configuration */
  }
  
  /*-------------------------------- PLL Configuration -----------------------*/
  /* Check the parameters */
  assert_param(IS_RCC_PLL(RCC_OscInitStruct->PLL.PLLState));
  if ((RCC_OscInitStruct->PLL.PLLState) != RCC_PLL_NONE)
  {
    /* Check if there is a request to disable the PLL used as System clock source */
    if ((RCC_OscInitStruct->PLL.PLLState) == RCC_PLL_OFF)
    {
      return HAL_ERROR;
    }
    else
    {
      /* Do not return HAL_ERROR if request repeats the current configuration */
      /* Skip hardware-specific PLL configuration */
    }
  }
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_UARTEx_ReceiveToIdle

```text
=== HAL_UARTEx_ReceiveToIdle 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1588
- 函数内容：HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint16_t *RxLen,
                                           uint32_t Timeout)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;
  uint32_t tickstart;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->RxXferSize  = Size;
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

    /* Initialize output number of received elements */
    *RxLen = 0U;

    /* as long as data have to be received */
    while (huart->RxXferCount > 0U)
    {
      /* Check if IDLE flag is set */
      if (__HAL_UART_GET_FLAG(huart, UART_FLAG_IDLE))
      {
        /* Clear IDLE flag in ISR */
        __HAL_UART_CLEAR_IDLEFLAG(huart);

        /* If Set, but no data ever received, clear flag without exiting loop */
        /* If Set, and data has already been received, this means Idle Event is valid : End reception */
        if (*RxLen > 0U)
        {
          huart->RxEventType = HAL_UART_RXEVENT_IDLE;
          huart->RxState = HAL_UART_STATE_READY;

          return HAL_OK;
        }
      }

      /* Check if RXNE flag is set */
      if (__HAL_UART_GET_FLAG(huart, UART_FLAG_RXNE))
      {
        if (pdata8bits == NULL)
        {
          *pdata16bits = (uint16_t)(huart->Instance->DR & (uint16_t)0x01FF);
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
        /* Increment number of received elements */
        *RxLen += 1U;
        huart->RxXferCount--;
      }

      /* Check for the Timeout */
      if (Timeout != HAL_MAX_DELAY)
      {
        if (((HAL_GetTick() - tickstart) > Timeout) || (Timeout == 0U))
        {
          huart->RxState = HAL_UART_STATE_READY;

          return HAL_TIMEOUT;
        }
      }
    }

    /* Set number of received elements in output parameter : RxLen */
    *RxLen = huart->RxXferSize - huart->RxXferCount;
    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receives data in blocking mode until either the expected number of data is received or an IDLE event occurs. Handles both 8-bit and 9-bit data formats with parity options.
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) Primary purpose is data reception from UART hardware (reads from huart->Instance->DR). 2) Contains hardware-dependent polling loops checking UART flags (IDLE and RXNE). 3) Performs critical data I/O operations. 4) Manages buffer pointers and state updates. 5) Not CORE (no NVIC/OS/VTOR operations), not IRQ (not an interrupt handler), not INIT (not initialization). According to priority order (CORE > RECV > IRQ > INIT > LOOP), RECV classification takes precedence over LOOP because it's fundamentally a data reception function with hardware polling.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint16_t *RxLen,
                                           uint32_t Timeout)
{
  uint8_t  *pdata8bits;
  uint16_t *pdata16bits;
  uint32_t tickstart;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return  HAL_ERROR;
    }

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    /* Init tickstart for timeout management */
    tickstart = HAL_GetTick();

    huart->RxXferSize  = Size;
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

    /* Initialize output number of received elements */
    *RxLen = 0U;

    /* Simulate data reception using HAL_BE_In */
    /* Replace hardware polling loop with simulated reception */
    if (pdata8bits == NULL)
    {
      /* For 16-bit data (9-bit mode) */
      HAL_BE_In(pdata16bits, Size * sizeof(uint16_t));
    }
    else
    {
      /* For 8-bit data */
      HAL_BE_In(pdata8bits, Size);
    }

    /* Set received count to full size (simulate all data received) */
    *RxLen = Size;
    huart->RxXferCount = 0U;

    /* Check for timeout (preserve timeout logic) */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - tickstart) > Timeout) || (Timeout == 0U))
      {
        huart->RxState = HAL_UART_STATE_READY;
        return HAL_TIMEOUT;
      }
    }

    /* Set number of received elements in output parameter : RxLen */
    *RxLen = huart->RxXferSize - huart->RxXferCount;
    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_UARTEx_ReceiveToIdle_DMA

```text
=== HAL_UARTEx_ReceiveToIdle_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1773
- 函数内容：HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef status;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to reception till IDLE Event*/
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    status =  UART_Start_Receive_DMA(huart, pData, Size);

    /* Check Rx process has been successfully started */
    if (status == HAL_OK)
    {
      if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
      {
        __HAL_UART_CLEAR_IDLEFLAG(huart);
        ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);
      }
      else
      {
        /* In case of errors already pending when reception is started,
           Interrupts may have already been raised and lead to reception abortion.
           (Overrun error for instance).
           In such case Reception Type has been reset to HAL_UART_RECEPTION_STANDARD. */
        status = HAL_ERROR;
      }
    }

    return status;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Initiates UART reception in DMA mode until either expected data amount is received or IDLE event occurs, managing buffer pointers and state machine
- 是否需要替换：是
- 分类/替换原因：Function performs data reception operations with DMA and IDLE event detection. GetFunctionInfo revealed it handles buffer management and state updates. GetMMIOFunctionInfo identified hardware register accesses for clearing IDLE flag and enabling IDLE interrupt. The function calls UART_Start_Receive_DMA which has additional hardware dependencies. This is classified as RECV because it's primarily a data reception function that needs hardware operations replaced with simulation while preserving state management and buffer handling logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Receive an amount of data in DMA mode till either the expected number of data is received or an IDLE event occurs.
* @note   Reception is initiated by this function call. Further progress of reception is achieved thanks
*         to DMA services, transferring automatically received data elements in user reception buffer and
*         calling registered callbacks at half/end of reception. UART IDLE events are also used to consider
*         reception phase as ended. In all cases, callback execution will indicate number of received data elements.
* @note   When the UART parity is enabled (PCE = 1), the received data contain
*         the parity bit (MSB position).
* @note   When UART parity is not enabled (PCE = 0), and Word Length is configured to 9 bits (M = 01),
*         the received data is handled as a set of uint16_t. In this case, Size must indicate the number
*         of uint16_t available through pData.
* @param huart UART handle.
* @param pData Pointer to data buffer (uint8_t or uint16_t data elements).
* @param Size  Amount of data elements (uint8_t or uint16_t) to be received.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef status;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to reception till IDLE Event*/
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    /* Simulate DMA reception by reading data into buffer */
    HAL_BE_In(pData, Size);
    
    /* Update state to indicate reception is in progress */
    huart->pRxBuffPtr = pData;
    huart->RxXferSize = Size;
    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;
    
    status = HAL_OK;

    /* Check Rx process has been successfully started */
    if (status == HAL_OK)
    {
      if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
      {
        /* Skip hardware-specific IDLE flag clearing and interrupt enabling */
        /* __HAL_UART_CLEAR_IDLEFLAG(huart); */
        /* ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_IDLEIE); */
      }
      else
      {
        /* In case of errors already pending when reception is started,
           Interrupts may have already been raised and lead to reception abortion.
           (Overrun error for instance).
           In such case Reception Type has been reset to HAL_UART_RECEPTION_STANDARD. */
        status = HAL_ERROR;
      }
    }

    return status;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_UARTEx_ReceiveToIdle_IT

```text
=== HAL_UARTEx_ReceiveToIdle_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1713
- 函数内容：HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef status;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to reception till IDLE Event*/
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    status =  UART_Start_Receive_IT(huart, pData, Size);

    /* Check Rx process has been successfully started */
    if (status == HAL_OK)
    {
      if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
      {
        __HAL_UART_CLEAR_IDLEFLAG(huart);
        ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);
      }
      else
      {
        /* In case of errors already pending when reception is started,
           Interrupts may have already been raised and lead to reception abortion.
           (Overrun error for instance).
           In such case Reception Type has been reset to HAL_UART_RECEPTION_STANDARD. */
        status = HAL_ERROR;
      }
    }

    return status;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Initiates UART reception in interrupt mode until either the expected amount of data is received or an IDLE event occurs
- 是否需要替换：是
- 分类/替换原因：This function is classified as RECV because: 1) It performs data reception operations by initiating UART reception in interrupt mode, 2) GetMMIOFunctionInfo revealed hardware register accesses including __HAL_UART_CLEAR_IDLEFLAG and ATOMIC_SET_BIT for enabling IDLE interrupt, 3) The function calls UART_Start_Receive_IT which also contains hardware interrupt enabling operations, 4) It's not an interrupt handler (IRQ) itself but sets up interrupt-based reception, 5) It's not an initialization function (INIT) as it doesn't initialize the peripheral from scratch, 6) It contains no NVIC/OS/VTOR operations, so it's not CORE, 7) The primary purpose is data reception initiation which aligns with the RECV category.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief Receive an amount of data in interrupt mode till either the expected number of data is received or an IDLE event occurs.
* @note   Reception is initiated by this function call. Further progress of reception is achieved thanks
*         to UART interrupts raised by RXNE and IDLE events. Callback is called at end of reception indicating
*         number of received data elements.
* @note   When UART parity is not enabled (PCE = 0), and Word Length is configured to 9 bits (M = 01),
*         the received data is handled as a set of uint16_t. In this case, Size must indicate the number
*         of uint16_t available through pData.
* @param huart UART handle.
* @param pData Pointer to data buffer (uint8_t or uint16_t data elements).
* @param Size  Amount of data elements (uint8_t or uint16_t) to be received.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_UARTEx_ReceiveToIdle_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  HAL_StatusTypeDef status;

  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to reception till IDLE Event*/
    huart->ReceptionType = HAL_UART_RECEPTION_TOIDLE;
    huart->RxEventType = HAL_UART_RXEVENT_TC;

    /* Simulate starting reception - preserve state updates */
    huart->pRxBuffPtr = pData;
    huart->RxXferSize = Size;
    huart->RxXferCount = Size;
    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->RxState = HAL_UART_STATE_BUSY_RX;

    /* Simulate data reception */
    HAL_BE_In(pData, Size);

    /* Check if reception was successfully started */
    if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
    {
      /* Skip hardware flag clearing and interrupt enabling */
      /* __HAL_UART_CLEAR_IDLEFLAG(huart); */
      /* ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_IDLEIE); */
      status = HAL_OK;
    }
    else
    {
      /* In case of errors already pending when reception is started,
         Interrupts may have already been raised and lead to reception abortion.
         (Overrun error for instance).
         In such case Reception Type has been reset to HAL_UART_RECEPTION_STANDARD. */
      status = HAL_ERROR;
    }

    return status;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_UART_Abort

```text
=== HAL_UART_Abort 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1859
- 函数内容：HAL_StatusTypeDef HAL_UART_Abort(UART_HandleTypeDef *huart)
{
  /* Disable TXEIE, TCIE, RXNE, PE and ERR (Frame error, noise error, overrun error) interrupts */
  ATOMIC_CLEAR_BIT(huart->Instance->CR1, (USART_CR1_RXNEIE | USART_CR1_PEIE | USART_CR1_TXEIE | USART_CR1_TCIE));
  ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_EIE);

  /* If Reception till IDLE event was ongoing, disable IDLEIE interrupt */
  if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
  {
    ATOMIC_CLEAR_BIT(huart->Instance->CR1, (USART_CR1_IDLEIE));
  }

  /* Disable the UART DMA Tx request if enabled */
  if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAT))
  {
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAT);

    /* Abort the UART DMA Tx stream: use blocking DMA Abort API (no callback) */
    if (huart->hdmatx != NULL)
    {
      /* Set the UART DMA Abort callback to Null.
         No call back execution at end of DMA abort procedure */
      huart->hdmatx->XferAbortCallback = NULL;

      if (HAL_DMA_Abort(huart->hdmatx) != HAL_OK)
      {
        if (HAL_DMA_GetError(huart->hdmatx) == HAL_DMA_ERROR_TIMEOUT)
        {
          /* Set error code to DMA */
          huart->ErrorCode = HAL_UART_ERROR_DMA;

          return HAL_TIMEOUT;
        }
      }
    }
  }

  /* Disable the UART DMA Rx request if enabled */
  if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAR))
  {
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAR);

    /* Abort the UART DMA Rx stream: use blocking DMA Abort API (no callback) */
    if (huart->hdmarx != NULL)
    {
      /* Set the UART DMA Abort callback to Null.
         No call back execution at end of DMA abort procedure */
      huart->hdmarx->XferAbortCallback = NULL;

      if (HAL_DMA_Abort(huart->hdmarx) != HAL_OK)
      {
        if (HAL_DMA_GetError(huart->hdmarx) == HAL_DMA_ERROR_TIMEOUT)
        {
          /* Set error code to DMA */
          huart->ErrorCode = HAL_UART_ERROR_DMA;

          return HAL_TIMEOUT;
        }
      }
    }
  }

  /* Reset Tx and Rx transfer counters */
  huart->TxXferCount = 0x00U;
  huart->RxXferCount = 0x00U;

  /* Reset ErrorCode */
  huart->ErrorCode = HAL_UART_ERROR_NONE;

  /* Restore huart->RxState and huart->gState to Ready */
  huart->RxState = HAL_UART_STATE_READY;
  huart->gState = HAL_UART_STATE_READY;
  huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Aborts ongoing UART transfers in blocking mode by disabling interrupts, stopping DMA transfers, and resetting the UART handle state to READY.
- 是否需要替换：是
- 分类/替换原因：Based on analysis: 1) GetFunctionInfo revealed the function performs peripheral configuration (disabling UART interrupts and DMA) and state management. 2) GetMMIOFunctionInfo identified multiple MMIO operations (CR1 and CR3 register writes via ATOMIC_CLEAR_BIT). 3) The function is not CORE (no NVIC/OS/VTOR operations), not RECV (no data transfer), not IRQ (not an interrupt handler), and not LOOP (no polling loops). It fits the INIT classification as it performs peripheral initialization/cleanup operations and state management that need hardware operations removed while preserving important state updates (transfer counters, error codes, state flags).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Abort ongoing transfers (blocking mode).
* @param  huart UART handle.
* @note   This procedure could be used for aborting any ongoing transfer started in Interrupt or DMA mode.
*         This procedure performs following operations :
*           - Disable UART Interrupts (Tx and Rx)
*           - Disable the DMA transfer in the peripheral register (if enabled)
*           - Abort DMA transfer by calling HAL_DMA_Abort (in case of transfer in DMA mode)
*           - Set handle State to READY
* @note   This procedure is executed in blocking mode : when exiting function, Abort is considered as completed.
* @retval HAL status
*/
HAL_StatusTypeDef HAL_UART_Abort(UART_HandleTypeDef *huart)
{
  /* If Reception till IDLE event was ongoing, disable IDLEIE interrupt */
  if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
  {
    /* Hardware interrupt disable removed for simulation */
  }

  /* Disable the UART DMA Tx request if enabled */
  if (huart->hdmatx != NULL)
  {
    /* Set the UART DMA Abort callback to Null.
       No call back execution at end of DMA abort procedure */
    huart->hdmatx->XferAbortCallback = NULL;

    if (HAL_DMA_Abort(huart->hdmatx) != HAL_OK)
    {
      if (HAL_DMA_GetError(huart->hdmatx) == HAL_DMA_ERROR_TIMEOUT)
      {
        /* Set error code to DMA */
        huart->ErrorCode = HAL_UART_ERROR_DMA;

        return HAL_TIMEOUT;
      }
    }
  }

  /* Disable the UART DMA Rx request if enabled */
  if (huart->hdmarx != NULL)
  {
    /* Set the UART DMA Abort callback to Null.
       No call back execution at end of DMA abort procedure */
    huart->hdmarx->XferAbortCallback = NULL;

    if (HAL_DMA_Abort(huart->hdmarx) != HAL_OK)
    {
      if (HAL_DMA_GetError(huart->hdmarx) == HAL_DMA_ERROR_TIMEOUT)
      {
        /* Set error code to DMA */
        huart->ErrorCode = HAL_UART_ERROR_DMA;

        return HAL_TIMEOUT;
      }
    }
  }

  /* Reset Tx and Rx transfer counters */
  huart->TxXferCount = 0x00U;
  huart->RxXferCount = 0x00U;

  /* Reset ErrorCode */
  huart->ErrorCode = HAL_UART_ERROR_NONE;

  /* Restore huart->RxState and huart->gState to Ready */
  huart->RxState = HAL_UART_STATE_READY;
  huart->gState = HAL_UART_STATE_READY;
  huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_UART_AbortTransmit_IT

```text
=== HAL_UART_AbortTransmit_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：2195
- 函数内容：HAL_StatusTypeDef HAL_UART_AbortTransmit_IT(UART_HandleTypeDef *huart)
{
  /* Disable TXEIE and TCIE interrupts */
  ATOMIC_CLEAR_BIT(huart->Instance->CR1, (USART_CR1_TXEIE | USART_CR1_TCIE));

  /* Disable the UART DMA Tx request if enabled */
  if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAT))
  {
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAT);

    /* Abort the UART DMA Tx stream : use blocking DMA Abort API (no callback) */
    if (huart->hdmatx != NULL)
    {
      /* Set the UART DMA Abort callback :
         will lead to call HAL_UART_AbortCpltCallback() at end of DMA abort procedure */
      huart->hdmatx->XferAbortCallback = UART_DMATxOnlyAbortCallback;

      /* Abort DMA TX */
      if (HAL_DMA_Abort_IT(huart->hdmatx) != HAL_OK)
      {
        /* Call Directly huart->hdmatx->XferAbortCallback function in case of error */
        huart->hdmatx->XferAbortCallback(huart->hdmatx);
      }
    }
    else
    {
      /* Reset Tx transfer counter */
      huart->TxXferCount = 0x00U;

      /* Restore huart->gState to Ready */
      huart->gState = HAL_UART_STATE_READY;

      /* As no DMA to be aborted, call directly user Abort complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
      /* Call registered Abort Transmit Complete Callback */
      huart->AbortTransmitCpltCallback(huart);
#else
      /* Call legacy weak Abort Transmit Complete Callback */
      HAL_UART_AbortTransmitCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
    }
  }
  else
  {
    /* Reset Tx transfer counter */
    huart->TxXferCount = 0x00U;

    /* Restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    /* As no DMA to be aborted, call directly user Abort complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /* Call registered Abort Transmit Complete Callback */
    huart->AbortTransmitCpltCallback(huart);
#else
    /* Call legacy weak Abort Transmit Complete Callback */
    HAL_UART_AbortTransmitCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Aborts ongoing UART transmit transfer in interrupt mode by disabling interrupts, stopping DMA if enabled, resetting transfer state, and calling user abort callback.
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this function performs UART peripheral configuration operations including disabling TX interrupts (TXEIE, TCIE) and DMA transfer requests. GetMMIOFunctionInfo identified MMIO operations accessing huart->Instance->CR1 and CR3 registers. The function sets driver state (gState = HAL_UART_STATE_READY), resets transfer counters, and calls user callbacks. It follows the INIT pattern: performs peripheral configuration/cleanup, manages driver state, and calls completion callbacks. Not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), not LOOP (no polling loops). Classified as INIT because it performs abort/cleanup operations similar to initialization functions.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Abort ongoing Transmit transfer (Interrupt mode).
* @param  huart UART handle.
* @note   This procedure could be used for aborting any ongoing Tx transfer started in Interrupt or DMA mode.
*         This procedure performs following operations :
*           - Disable UART Interrupts (Tx)
*           - Disable the DMA transfer in the peripheral register (if enabled)
*           - Abort DMA transfer by calling HAL_DMA_Abort_IT (in case of transfer in DMA mode)
*           - Set handle State to READY
*           - At abort completion, call user abort complete callback
* @note   This procedure is executed in Interrupt mode, meaning that abort procedure could be
*         considered as completed only when user abort complete callback is executed (not when exiting function).
* @retval HAL status
*/
HAL_StatusTypeDef HAL_UART_AbortTransmit_IT(UART_HandleTypeDef *huart)
{
  /* Skip hardware-specific interrupt disable operations */
  /* Original: ATOMIC_CLEAR_BIT(huart->Instance->CR1, (USART_CR1_TXEIE | USART_CR1_TCIE)); */

  /* Skip hardware-specific DMA disable check and operations */
  /* Original: if (HAL_IS_BIT_SET(huart->Instance->CR3, USART_CR3_DMAT)) */

  /* Abort the UART DMA Tx stream if DMA handle exists */
  if (huart->hdmatx != NULL)
  {
    /* Set the UART DMA Abort callback :
       will lead to call HAL_UART_AbortCpltCallback() at end of DMA abort procedure */
    huart->hdmatx->XferAbortCallback = UART_DMATxOnlyAbortCallback;

    /* Abort DMA TX */
    if (HAL_DMA_Abort_IT(huart->hdmatx) != HAL_OK)
    {
      /* Call Directly huart->hdmatx->XferAbortCallback function in case of error */
      huart->hdmatx->XferAbortCallback(huart->hdmatx);
    }
  }
  else
  {
    /* Reset Tx transfer counter */
    huart->TxXferCount = 0x00U;

    /* Restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    /* As no DMA to be aborted, call directly user Abort complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /* Call registered Abort Transmit Complete Callback */
    huart->AbortTransmitCpltCallback(huart);
#else
    /* Call legacy weak Abort Transmit Complete Callback */
    HAL_UART_AbortTransmitCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
  }

  return HAL_OK;
}
```

=== 信息结束 ===
```

### HAL_UART_GetState

```text
=== HAL_UART_GetState 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：2928
- 函数内容：HAL_UART_StateTypeDef HAL_UART_GetState(const UART_HandleTypeDef *huart)
{
  uint32_t temp1 = 0x00U, temp2 = 0x00U;
  temp1 = huart->gState;
  temp2 = huart->RxState;

  return (HAL_UART_StateTypeDef)(temp1 | temp2);
}


【替换更新】
- 更新代码：HAL_UART_StateTypeDef HAL_UART_GetState(const UART_HandleTypeDef *huart)
{
  /* In emulation mode, check the actual state */
  /* The original function returns (gState | RxState) */
  /* In our replacements, both states are set to READY immediately after operations complete */
  /* So we should return READY */
  return HAL_UART_STATE_READY;
}
- 更新原因：Revert to simple READY return for HAL_UART_GetState. The previous fix with a counter was too complex and might cause issues. Since HAL_UART_Transmit_IT and HAL_UART_Receive_IT immediately set state to READY after operations complete, HAL_UART_GetState should return READY. This allows wait loops to exit immediately.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：HAL_UART_StateTypeDef HAL_UART_GetState(const UART_HandleTypeDef *huart)
{
  static int call_count = 0;
  
  /* In emulation mode, return BUSY for first 3 calls, then READY */
  /* This allows wait loops to spin for a few iterations before exiting */
  /* This helps the emulator detect that progress is being made */
  if (call_count < 3)
  {
    call_count++;
    /* Return BUSY state to make wait loop spin */
    return HAL_UART_STATE_BUSY_TX; /* Or any BUSY state */
  }
  else
  {
    /* After 3 calls, return READY to allow wait loop to exit */
    return HAL_UART_STATE_READY;
  }
}
    原因：Fix exceptional loop detection by making HAL_UART_GetState return BUSY for first 3 calls, then READY. This causes wait loops to spin for a few iterations before exiting, which helps the emulator detect that progress is being made. The original replacement always returned READY immediately, which might cause the emulator to detect tight loops or exceptional behavior.
    时间：

  版本 2:
    替换代码：HAL_UART_StateTypeDef HAL_UART_GetState(const UART_HandleTypeDef *huart)
{
  /* In emulation mode, check the actual state */
  /* The original function returns (gState | RxState) */
  /* In our replacements, both states are set to READY immediately after operations complete */
  /* So we should return READY */
  return HAL_UART_STATE_READY;
}
    原因：Revert to simple READY return for HAL_UART_GetState. The previous fix with a counter was too complex and might cause issues. Since HAL_UART_Transmit_IT and HAL_UART_Receive_IT immediately set state to READY after operations complete, HAL_UART_GetState should return READY. This allows wait loops to exit immediately.
    时间：

=== 信息结束 ===
```

### HAL_UART_IRQHandler

```text
=== HAL_UART_IRQHandler 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
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


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：UART interrupt handler that processes various UART interrupt events including reception, transmission, errors, and IDLE events
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) This is an interrupt handler function called from USART3_IRQHandler; 2) It contains extensive MMIO operations reading from hardware registers (SR, CR1, CR3) and writing to clear interrupt flags; 3) It processes multiple interrupt conditions (RXNE, TXE, TC, error flags, IDLE); 4) It calls other interrupt-related functions like UART_Receive_IT and UART_Transmit_IT; 5) It is not a CORE function (doesn't configure NVIC/OS/VTOR), not a RECV function (though it handles reception, it's primarily an interrupt handler), not INIT or LOOP. According to classification priority (CORE > RECV > IRQ > INIT > LOOP), IRQ is the appropriate classification.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void HAL_UART_IRQHandler(UART_HandleTypeDef *huart)
{
  uint32_t errorflags = 0x00U;
  uint32_t dmarequest = 0x00U;

  /* If no error occurs */
  /* Simulate no errors by default */
  errorflags = 0U; /* Assume no error flags */
  
  if (errorflags == RESET)
  {
    /* UART in mode Receiver -------------------------------------------------*/
    /* Simulate RXNE interrupt condition */
    /* Assume RXNE flag is set and RXNEIE is enabled */
    UART_Receive_IT(huart);
    return;
  }

  /* If some errors occur */
  /* Skip error handling since we simulate no errors */
  
  /* Check current reception Mode :
     If Reception till IDLE event has been selected : */
  if ((huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE))
  {
    /* Check if DMA mode is enabled in UART */
    if (huart->hdmarx != NULL)
    {
      /* DMA mode enabled */
      /* Check received length : If all expected data are received, do nothing,
         (DMA cplt callback will be called).
         Otherwise, if at least one data has already been received, IDLE event is to be notified to user */
      uint16_t nb_remaining_rx_data = huart->RxXferCount;
      if ((nb_remaining_rx_data > 0U)
          && (nb_remaining_rx_data < huart->RxXferSize))
      {
        /* Reception is not complete */
        huart->RxXferCount = nb_remaining_rx_data;

        /* In Normal mode, end DMA xfer and HAL UART Rx process*/
        if (huart->hdmarx->Init.Mode != DMA_CIRCULAR)
        {
          /* At end of Rx process, restore huart->RxState to Ready */
          huart->RxState = HAL_UART_STATE_READY;
          huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

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
        /* Rx process is completed, restore huart->RxState to Ready */
        huart->RxState = HAL_UART_STATE_READY;
        huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

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
  /* Simulate TXE interrupt condition */
  UART_Transmit_IT(huart);
  return;

  /* UART in mode Transmitter end --------------------------------------------*/
  /* Simulate TC interrupt condition */
  UART_EndTransmit_IT(huart);
  return;
}
```

=== 信息结束 ===
```

### HAL_UART_Receive

```text
=== HAL_UART_Receive 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
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


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receives an amount of data in blocking mode from a UART peripheral
- 是否需要替换：是
- 分类/替换原因：Based on analysis using GetFunctionInfo and GetMMIOFunctionInfo: 1) Function performs critical data I/O (receiving data from UART hardware register DR); 2) Contains hardware-dependent operations including register reads (huart->Instance->DR) and polling loops (UART_WaitOnFlagUntilTimeout for RXNE flag); 3) Manages buffer pointers, state updates (RxState, ErrorCode, ReceptionType), and transfer counters (RxXferSize, RxXferCount); 4) Handles different UART configurations (word length, parity); 5) Not classified as CORE because no NVIC/OS/VTOR operations; 6) Primary purpose is data reception making it a clear RECV type.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)
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
      /* [LOOP REMOVED] Skip waiting for hardware RXNE flag - assume data is available */
      /* Original: if (UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_RXNE, RESET, tickstart, Timeout) != HAL_OK) */
      /* Simulate data reception using HAL_BE_In */
      if (pdata8bits == NULL)
      {
        /* For 9-bit no parity mode, read as uint16_t */
        HAL_BE_In(pdata16bits, sizeof(uint16_t));
        pdata16bits++;
      }
      else
      {
        /* For 8-bit or 7-bit with parity modes, read as uint8_t */
        HAL_BE_In(pdata8bits, sizeof(uint8_t));
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
```

=== 信息结束 ===
```

### HAL_UART_Receive_IT

```text
=== HAL_UART_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1347
- 函数内容：HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to Standard reception */
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    return (UART_Start_Receive_IT(huart, pData, Size));
  }
  else
  {
    return HAL_BUSY;
  }
}


【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to Standard reception */
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Call UART_Start_Receive_IT to set up buffers and state */
    /* This sets RxState to BUSY_RX and configures buffers */
    UART_Start_Receive_IT(huart, pData, Size);
    
    /* In emulation mode, simulate receiving all data immediately */
    /* Use HAL_BE_In to simulate receiving data from stdin */
    if (Size > 0)
    {
      HAL_BE_In(pData, Size);
    }
    
    /* Immediately complete the reception */
    /* Update state to indicate reception is complete */
    huart->RxState = HAL_UART_STATE_READY;
    huart->RxXferCount = 0U;
    
    /* Initialize type of RxEvent to Transfer Complete */
    huart->RxEventType = HAL_UART_RXEVENT_TC;
    
    /* Call the reception complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Rx complete callback*/
    huart->RxCpltCallback(huart);
#else
    /*Call legacy weak Rx complete callback*/
    HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
- 更新原因：Simplify HAL_UART_Receive_IT replacement by removing hardware interrupt disable macros that might cause emulator issues. The previous replacement used __HAL_UART_DISABLE_IT macros which might expand to hardware register writes. In emulation, we don't need to actually disable hardware interrupts - we just need to simulate the behavior. The simplified replacement immediately completes reception, updates state to READY, and calls the callback without touching hardware registers. Note: We still call UART_Start_Receive_IT to set up buffers, but that function also writes to hardware registers. We might need to fix that too if issues persist.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to Standard reception */
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Call UART_Start_Receive_IT to set up buffers and state */
    /* This sets RxState to BUSY_RX and configures buffers */
    UART_Start_Receive_IT(huart, pData, Size);
    
    /* In emulation mode, simulate receiving all data immediately */
    /* Use HAL_BE_In to simulate receiving data from stdin */
    if (Size > 0)
    {
      HAL_BE_In(pData, Size);
    }
    
    /* Immediately complete the reception */
    /* Disable the UART interrupts (preserved for NVIC operations) */
    __HAL_UART_DISABLE_IT(huart, UART_IT_RXNE);
    __HAL_UART_DISABLE_IT(huart, UART_IT_PE);
    __HAL_UART_DISABLE_IT(huart, UART_IT_ERR);
    
    /* Update state to indicate reception is complete */
    huart->RxState = HAL_UART_STATE_READY;
    huart->RxXferCount = 0U;
    
    /* Initialize type of RxEvent to Transfer Complete */
    huart->RxEventType = HAL_UART_RXEVENT_TC;
    
    /* Call the reception complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Rx complete callback*/
    huart->RxCpltCallback(huart);
#else
    /*Call legacy weak Rx complete callback*/
    HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Fix exceptional loop in main by completing UART reception immediately in emulation mode. The original code sets state to BUSY_RX and enables RX interrupts, but in emulation there are no hardware interrupts to trigger data reception. This causes HAL_UART_GetState to always return busy state, creating an infinite loop. The replacement simulates immediate reception completion: 1) Calls UART_Start_Receive_IT to set up buffers, 2) Uses HAL_BE_In to simulate receiving all data at once, 3) Updates state to READY, 4) Calls the reception complete callback. This ensures HAL_UART_GetState returns READY state, breaking the infinite loop.
    时间：

  版本 2:
    替换代码：HAL_StatusTypeDef HAL_UART_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  /* Check that a Rx process is not already ongoing */
  if (huart->RxState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    /* Set Reception type to Standard reception */
    huart->ReceptionType = HAL_UART_RECEPTION_STANDARD;

    /* Call UART_Start_Receive_IT to set up buffers and state */
    /* This sets RxState to BUSY_RX and configures buffers */
    UART_Start_Receive_IT(huart, pData, Size);
    
    /* In emulation mode, simulate receiving all data immediately */
    /* Use HAL_BE_In to simulate receiving data from stdin */
    if (Size > 0)
    {
      HAL_BE_In(pData, Size);
    }
    
    /* Immediately complete the reception */
    /* Update state to indicate reception is complete */
    huart->RxState = HAL_UART_STATE_READY;
    huart->RxXferCount = 0U;
    
    /* Initialize type of RxEvent to Transfer Complete */
    huart->RxEventType = HAL_UART_RXEVENT_TC;
    
    /* Call the reception complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Rx complete callback*/
    huart->RxCpltCallback(huart);
#else
    /*Call legacy weak Rx complete callback*/
    HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Simplify HAL_UART_Receive_IT replacement by removing hardware interrupt disable macros that might cause emulator issues. The previous replacement used __HAL_UART_DISABLE_IT macros which might expand to hardware register writes. In emulation, we don't need to actually disable hardware interrupts - we just need to simulate the behavior. The simplified replacement immediately completes reception, updates state to READY, and calls the callback without touching hardware registers. Note: We still call UART_Start_Receive_IT to set up buffers, but that function also writes to hardware registers. We might need to fix that too if issues persist.
    时间：

=== 信息结束 ===
```

### HAL_UART_Transmit

```text
=== HAL_UART_Transmit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
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


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits data in blocking mode via UART with timeout handling, supporting both 8-bit and 9-bit data formats
- 是否需要替换：是
- 分类/替换原因：Function performs critical data I/O operations (UART transmission) with direct MMIO register writes to huart->Instance->DR. Contains hardware-dependent polling loops waiting for TXE and TC flags. According to classification criteria, data transmission/reception functions are classified as RECV. The function manages UART state transitions (READY→BUSY_TX→READY) and transfer counters, which must be preserved while hardware operations are replaced with simulation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Sends an amount of data in blocking mode.
* @note   When UART parity is not enabled (PCE = 0), and Word Length is configured to 9 bits (M1-M0 = 01),
*         the sent data is handled as a set of u16. In this case, Size must indicate the number
*         of u16 provided through pData.
* @param  huart Pointer to a UART_HandleTypeDef structure that contains
*               the configuration information for the specified UART module.
* @param  pData Pointer to data buffer (u8 or u16 data elements).
* @param  Size  Amount of data elements (u8 or u16) to be sent
* @param  Timeout Timeout duration
* @retval HAL status
*/
HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size, uint32_t Timeout)
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

    /* Simulate data transmission - skip hardware polling and register writes */
    /* Original loop waited for TXE flag and wrote to DR register */
    /* Simulate by advancing pointers and decrementing count */
    while (huart->TxXferCount > 0U)
    {
      /* Skip hardware wait: UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_TXE, RESET, tickstart, Timeout) */
      /* Assume transmission ready immediately */
      if (pdata8bits == NULL)
      {
        /* Simulate 9-bit data transmission */
        pdata16bits++;
      }
      else
      {
        /* Simulate 8-bit data transmission */
        pdata8bits++;
      }
      huart->TxXferCount--;
    }

    /* Skip waiting for transmission complete flag */
    /* Original: if (UART_WaitOnFlagUntilTimeout(huart, UART_FLAG_TC, RESET, tickstart, Timeout) != HAL_OK) */
    /* Assume transmission completes successfully */

    /* At end of Tx process, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

=== 信息结束 ===
```

### HAL_UART_Transmit_DMA

```text
=== HAL_UART_Transmit_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1379
- 函数内容：HAL_StatusTypeDef HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  const uint32_t *tmp;

  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Set the UART DMA transfer complete callback */
    huart->hdmatx->XferCpltCallback = UART_DMATransmitCplt;

    /* Set the UART DMA Half transfer complete callback */
    huart->hdmatx->XferHalfCpltCallback = UART_DMATxHalfCplt;

    /* Set the DMA error callback */
    huart->hdmatx->XferErrorCallback = UART_DMAError;

    /* Set the DMA abort callback */
    huart->hdmatx->XferAbortCallback = NULL;

    /* Enable the UART transmit DMA stream */
    tmp = (const uint32_t *)&pData;
    HAL_DMA_Start_IT(huart->hdmatx, *(const uint32_t *)tmp, (uint32_t)&huart->Instance->DR, Size);

    /* Clear the TC flag in the SR register by writing 0 to it */
    __HAL_UART_CLEAR_FLAG(huart, UART_FLAG_TC);

    /* Enable the DMA transfer for transmit request by setting the DMAT bit
       in the UART CR3 register */
    ATOMIC_SET_BIT(huart->Instance->CR3, USART_CR3_DMAT);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits data using DMA for UART communication, setting up DMA transfer from memory buffer to UART data register
- 是否需要替换：是
- 分类/替换原因：This is a data transmission function that performs critical I/O operations (UART transmission via DMA). GetFunctionInfo revealed the function sets up DMA transfer, configures callbacks, and accesses hardware registers. GetMMIOFunctionInfo identified hardware register accesses including DMA start, flag clearing, and register bit setting. The function updates UART handle state and manages buffer pointers. According to classification priority (RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER), this fits the RECV category which handles data transmission/reception functions. The replacement preserves state management and callback setup while removing hardware dependencies.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Set the UART DMA transfer complete callback */
    huart->hdmatx->XferCpltCallback = UART_DMATransmitCplt;

    /* Set the UART DMA Half transfer complete callback */
    huart->hdmatx->XferHalfCpltCallback = UART_DMATxHalfCplt;

    /* Set the DMA error callback */
    huart->hdmatx->XferErrorCallback = UART_DMAError;

    /* Set the DMA abort callback */
    huart->hdmatx->XferAbortCallback = NULL;

    /* Simulate data transmission using HAL_BE_Out */
    HAL_BE_Out(Size);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
```

【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Set the UART DMA transfer complete callback */
    huart->hdmatx->XferCpltCallback = UART_DMATransmitCplt;

    /* Set the UART DMA Half transfer complete callback */
    huart->hdmatx->XferHalfCpltCallback = UART_DMATxHalfCplt;

    /* Set the DMA error callback */
    huart->hdmatx->XferErrorCallback = UART_DMAError;

    /* Set the DMA abort callback */
    huart->hdmatx->XferAbortCallback = NULL;

    /* Simulate data transmission using HAL_BE_Out */
    HAL_BE_Out(Size);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
- 更新原因：Fix syntax errors in HAL_UART_Transmit_DMA replacement code. The original errors suggest comment syntax issues and unexpected tokens. This cleaned version ensures proper C syntax with correct comment formatting and complete function structure.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Set the UART DMA transfer complete callback */
    huart->hdmatx->XferCpltCallback = UART_DMATransmitCplt;

    /* Set the UART DMA Half transfer complete callback */
    huart->hdmatx->XferHalfCpltCallback = UART_DMATxHalfCplt;

    /* Set the DMA error callback */
    huart->hdmatx->XferErrorCallback = UART_DMAError;

    /* Set the DMA abort callback */
    huart->hdmatx->XferAbortCallback = NULL;

    /* Simulate data transmission using HAL_BE_Out */
    HAL_BE_Out(Size);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Fix syntax errors in HAL_UART_Transmit_DMA replacement code. The original errors suggest comment syntax issues and unexpected tokens. This cleaned version ensures proper C syntax with correct comment formatting and complete function structure.
    时间：

=== 信息结束 ===
```

### HAL_UART_Transmit_IT

```text
=== HAL_UART_Transmit_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：1308
- 函数内容：HAL_StatusTypeDef HAL_UART_Transmit_IT(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* Enable the UART Transmit data register empty Interrupt */
    __HAL_UART_ENABLE_IT(huart, UART_IT_TXE);

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}


【替换更新】
- 更新代码：HAL_StatusTypeDef HAL_UART_Transmit_IT(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* In emulation mode, immediately simulate transmission completion */
    /* Simulate sending data using HAL_BE_Out */
    if (Size > 0)
    {
      HAL_BE_Out(Size);
    }
    
    /* Immediately complete transmission */
    huart->TxXferCount = 0U;
    
    /* Tx process is ended, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;
    
    /* Call the transmission complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Tx complete callback*/
    huart->TxCpltCallback(huart);
#else
    /*Call legacy weak Tx complete callback*/
    HAL_UART_TxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
- 更新原因：Simplify HAL_UART_Transmit_IT replacement by removing hardware interrupt enable/disable macros that might cause emulator issues. The previous replacement used __HAL_UART_ENABLE_IT and __HAL_UART_DISABLE_IT macros which might expand to hardware register writes. In emulation, we don't need to actually enable/disable hardware interrupts - we just need to simulate the behavior. The simplified replacement immediately completes transmission, updates state to READY, and calls the callback without touching hardware registers.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef HAL_UART_Transmit_IT(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* In emulation mode, immediately simulate transmission completion */
    /* Simulate sending data using HAL_BE_Out */
    if (Size > 0)
    {
      HAL_BE_Out(Size);
    }
    
    /* Immediately complete transmission */
    huart->TxXferCount = 0U;
    
    /* Disable the UART Transmit Data Register Empty Interrupt */
    /* Preserved for potential NVIC operations */
    __HAL_UART_DISABLE_IT(huart, UART_IT_TXE);
    
    /* Enable the UART Transmit Complete Interrupt */
    /* Preserved for potential NVIC operations */
    __HAL_UART_ENABLE_IT(huart, UART_IT_TC);
    
    /* Immediately complete transmission (simulating UART_EndTransmit_IT) */
    /* Disable the UART Transmit Complete Interrupt */
    __HAL_UART_DISABLE_IT(huart, UART_IT_TC);
    
    /* Tx process is ended, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;
    
    /* Call the transmission complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Tx complete callback*/
    huart->TxCpltCallback(huart);
#else
    /*Call legacy weak Tx complete callback*/
    HAL_UART_TxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Fix exceptional loop in main by completing UART transmission immediately in emulation mode. The original code sets state to BUSY_TX and enables TXE interrupt, but in emulation there are no hardware interrupts to trigger completion. This causes HAL_UART_GetState to always return busy state, creating an infinite loop. The replacement simulates immediate transmission completion: 1) Uses HAL_BE_Out to simulate sending data, 2) Updates state to READY, 3) Calls the transmission complete callback. This ensures HAL_UART_GetState returns READY state, breaking the infinite loop. Duplicated UART_EndTransmit_IT logic to avoid static function call issues.
    时间：

  版本 2:
    替换代码：HAL_StatusTypeDef HAL_UART_Transmit_IT(UART_HandleTypeDef *huart, const uint8_t *pData, uint16_t Size)
{
  /* Check that a Tx process is not already ongoing */
  if (huart->gState == HAL_UART_STATE_READY)
  {
    if ((pData == NULL) || (Size == 0U))
    {
      return HAL_ERROR;
    }

    huart->pTxBuffPtr = pData;
    huart->TxXferSize = Size;
    huart->TxXferCount = Size;

    huart->ErrorCode = HAL_UART_ERROR_NONE;
    huart->gState = HAL_UART_STATE_BUSY_TX;

    /* In emulation mode, immediately simulate transmission completion */
    /* Simulate sending data using HAL_BE_Out */
    if (Size > 0)
    {
      HAL_BE_Out(Size);
    }
    
    /* Immediately complete transmission */
    huart->TxXferCount = 0U;
    
    /* Tx process is ended, restore huart->gState to Ready */
    huart->gState = HAL_UART_STATE_READY;
    
    /* Call the transmission complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Tx complete callback*/
    huart->TxCpltCallback(huart);
#else
    /*Call legacy weak Tx complete callback*/
    HAL_UART_TxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */

    return HAL_OK;
  }
  else
  {
    return HAL_BUSY;
  }
}
    原因：Simplify HAL_UART_Transmit_IT replacement by removing hardware interrupt enable/disable macros that might cause emulator issues. The previous replacement used __HAL_UART_ENABLE_IT and __HAL_UART_DISABLE_IT macros which might expand to hardware register writes. In emulation, we don't need to actually enable/disable hardware interrupts - we just need to simulate the behavior. The simplified replacement immediately completes transmission, updates state to READY, and calls the callback without touching hardware registers.
    时间：

=== 信息结束 ===
```

### I2C_DMAAbort

```text
=== I2C_DMAAbort 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7122
- 函数内容：static void I2C_DMAAbort(DMA_HandleTypeDef *hdma)
{
  __IO uint32_t count = 0U;
  I2C_HandleTypeDef *hi2c = (I2C_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent; /* Derogation MISRAC2012-Rule-11.5 */

  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_StateTypeDef CurrentState = hi2c->State;

  /* During abort treatment, check that there is no pending STOP request */
  /* Wait until STOP flag is reset */
  count = I2C_TIMEOUT_FLAG * (SystemCoreClock / 25U / 1000U);
  do
  {
    if (count == 0U)
    {
      hi2c->ErrorCode |= HAL_I2C_ERROR_TIMEOUT;
      break;
    }
    count--;
  }
  while (READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP);

  /* Clear Complete callback */
  if (hi2c->hdmatx != NULL)
  {
    hi2c->hdmatx->XferCpltCallback = NULL;
  }
  if (hi2c->hdmarx != NULL)
  {
    hi2c->hdmarx->XferCpltCallback = NULL;
  }

  /* Disable Acknowledge */
  CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

  hi2c->XferCount = 0U;

  /* Reset XferAbortCallback */
  if (hi2c->hdmatx != NULL)
  {
    hi2c->hdmatx->XferAbortCallback = NULL;
  }
  if (hi2c->hdmarx != NULL)
  {
    hi2c->hdmarx->XferAbortCallback = NULL;
  }

  /* Disable I2C peripheral to prevent dummy data in buffer */
  __HAL_I2C_DISABLE(hi2c);

  /* Check if come from abort from user */
  if (hi2c->State == HAL_I2C_STATE_ABORT)
  {
    hi2c->State         = HAL_I2C_STATE_READY;
    hi2c->Mode          = HAL_I2C_MODE_NONE;
    hi2c->ErrorCode     = HAL_I2C_ERROR_NONE;

    /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->AbortCpltCallback(hi2c);
#else
    HAL_I2C_AbortCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
  else
  {
    if (((uint32_t)CurrentState & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
    {
      /* Renable I2C peripheral */
      __HAL_I2C_ENABLE(hi2c);

      /* Enable Acknowledge */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

      /* keep HAL_I2C_STATE_LISTEN */
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_LISTEN;
    }
    else
    {
      hi2c->State = HAL_I2C_STATE_READY;
      hi2c->Mode = HAL_I2C_MODE_NONE;
    }

    /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->ErrorCallback(hi2c);
#else
    HAL_I2C_ErrorCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：DMA I2C communication abort callback function that handles cleanup and state management after DMA abort procedures
- 是否需要替换：是
- 分类/替换原因：The function contains a peripheral-dependent polling loop waiting for the I2C STOP flag to clear (READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP)), which is a key characteristic of LOOP classification. Additionally, it performs hardware register writes (CLEAR_BIT, SET_BIT, __HAL_I2C_DISABLE, __HAL_I2C_ENABLE) that need to be removed. The function also manages significant state updates (State, Mode, ErrorCode, PreviousState) and callback logic that must be preserved. According to the classification priority order (CORE > RECV > IRQ > INIT > LOOP > ...), this function fits the LOOP category due to its hardware-dependent polling loop.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief DMA I2C communication abort callback
*        (To be called at end of DMA Abort procedure).
* @param hdma DMA handle.
* @retval None
*/
static void I2C_DMAAbort(DMA_HandleTypeDef *hdma)
{
  I2C_HandleTypeDef *hi2c = (I2C_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent; /* Derogation MISRAC2012-Rule-11.5 */

  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_StateTypeDef CurrentState = hi2c->State;

  /* During abort treatment, check that there is no pending STOP request */
  /* Wait until STOP flag is reset - LOOP REMOVED: Skip hardware polling */
  /* [LOOP REMOVED] Waited for hardware STOP flag to clear */

  /* Clear Complete callback */
  if (hi2c->hdmatx != NULL)
  {
    hi2c->hdmatx->XferCpltCallback = NULL;
  }
  if (hi2c->hdmarx != NULL)
  {
    hi2c->hdmarx->XferCpltCallback = NULL;
  }

  /* Disable Acknowledge - HARDWARE OPERATION REMOVED */
  /* CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

  hi2c->XferCount = 0U;

  /* Reset XferAbortCallback */
  if (hi2c->hdmatx != NULL)
  {
    hi2c->hdmatx->XferAbortCallback = NULL;
  }
  if (hi2c->hdmarx != NULL)
  {
    hi2c->hdmarx->XferAbortCallback = NULL;
  }

  /* Disable I2C peripheral to prevent dummy data in buffer - HARDWARE OPERATION REMOVED */
  /* __HAL_I2C_DISABLE(hi2c); */

  /* Check if come from abort from user */
  if (hi2c->State == HAL_I2C_STATE_ABORT)
  {
    hi2c->State         = HAL_I2C_STATE_READY;
    hi2c->Mode          = HAL_I2C_MODE_NONE;
    hi2c->ErrorCode     = HAL_I2C_ERROR_NONE;

    /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->AbortCpltCallback(hi2c);
#else
    HAL_I2C_AbortCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
  else
  {
    if (((uint32_t)CurrentState & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
    {
      /* Renable I2C peripheral - HARDWARE OPERATION REMOVED */
      /* __HAL_I2C_ENABLE(hi2c); */

      /* Enable Acknowledge - HARDWARE OPERATION REMOVED */
      /* SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

      /* keep HAL_I2C_STATE_LISTEN */
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_LISTEN;
    }
    else
    {
      hi2c->State = HAL_I2C_STATE_READY;
      hi2c->Mode = HAL_I2C_MODE_NONE;
    }

    /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->ErrorCallback(hi2c);
#else
    HAL_I2C_ErrorCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
}
```

=== 信息结束 ===
```

### I2C_Master_ADDR

```text
=== I2C_Master_ADDR 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：5852
- 函数内容：static void I2C_Master_ADDR(I2C_HandleTypeDef *hi2c)
{
  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_ModeTypeDef CurrentMode       = hi2c->Mode;
  uint32_t CurrentXferOptions           = hi2c->XferOptions;
  uint32_t Prev_State                   = hi2c->PreviousState;

  if (hi2c->State == HAL_I2C_STATE_BUSY_RX)
  {
    if ((hi2c->EventCount == 0U) && (CurrentMode == HAL_I2C_MODE_MEM))
    {
      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
    }
    else if ((hi2c->EventCount == 0U) && (hi2c->Init.AddressingMode == I2C_ADDRESSINGMODE_10BIT))
    {
      /* Clear ADDR flag */
      __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

      /* Generate Restart */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

      hi2c->EventCount++;
    }
    else
    {
      if (hi2c->XferCount == 0U)
      {
        /* Clear ADDR flag */
        __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

        /* Generate Stop */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
      }
      else if (hi2c->XferCount == 1U)
      {
        if (CurrentXferOptions == I2C_NO_OPTION_FRAME)
        {
          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
          {
            /* Disable Acknowledge */
            CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

            /* Clear ADDR flag */
            __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
          }
          else
          {
            /* Clear ADDR flag */
            __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

            /* Generate Stop */
            SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
          }
        }
        /* Prepare next transfer or stop current transfer */
        else if ((CurrentXferOptions != I2C_FIRST_AND_LAST_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME) \
                 && ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (CurrentXferOptions == I2C_FIRST_FRAME)))
        {
          if ((CurrentXferOptions != I2C_NEXT_FRAME) && (CurrentXferOptions != I2C_FIRST_AND_NEXT_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME_NO_STOP))
          {
            /* Disable Acknowledge */
            CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
          }
          else
          {
            /* Enable Acknowledge */
            SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
          }

          /* Clear ADDR flag */
          __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
        }
        else
        {
          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          /* Clear ADDR flag */
          __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

          /* Generate Stop */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
        }
      }
      else if (hi2c->XferCount == 2U)
      {
        if ((CurrentXferOptions != I2C_NEXT_FRAME) && (CurrentXferOptions != I2C_FIRST_AND_NEXT_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME_NO_STOP))
        {
          /* Disable Acknowledge */
          CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

          /* Enable Pos */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS);
        }
        else
        {
          /* Enable Acknowledge */
          SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);
        }

        if (((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN) && ((CurrentXferOptions == I2C_NO_OPTION_FRAME) || (CurrentXferOptions == I2C_FIRST_FRAME) || (CurrentXferOptions == I2C_FIRST_AND_LAST_FRAME) || (CurrentXferOptions == I2C_LAST_FRAME_NO_STOP) || (CurrentXferOptions == I2C_LAST_FRAME)))
        {
          /* Enable Last DMA bit */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);
        }

        /* Clear ADDR flag */
        __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
      }
      else
      {
        /* Enable Acknowledge */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

        if (((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN) && ((CurrentXferOptions == I2C_NO_OPTION_FRAME) || (CurrentXferOptions == I2C_FIRST_FRAME) || (CurrentXferOptions == I2C_FIRST_AND_LAST_FRAME) || (CurrentXferOptions == I2C_LAST_FRAME_NO_STOP) || (CurrentXferOptions == I2C_LAST_FRAME)))
        {
          /* Enable Last DMA bit */
          SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST);
        }

        /* Clear ADDR flag */
        __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
      }

      /* Reset Event counter  */
      hi2c->EventCount = 0U;
    }
  }
  else
  {
    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Handles ADDR flag for I2C master mode, called from interrupt handler to manage address acknowledgment and control operations
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed this is a static helper function called from HAL_I2C_EV_IRQHandler (interrupt handler). GetMMIOFunctionInfo identified multiple hardware register accesses including __HAL_I2C_CLEAR_ADDRFLAG, SET_BIT/CLEAR_BIT operations on CR1/CR2 registers for START/STOP generation, ACK control, and DMA configuration. The function maintains important state machine logic based on hi2c->State, hi2c->EventCount, hi2c->XferCount, and transfer options. Classified as IRQ because: 1) Called from interrupt context, 2) Handles interrupt flag clearing, 3) Performs interrupt-related control operations, 4) Contains hardware operations that need replacement while preserving state logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Handle ADDR flag for Master
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for I2C module
* @retval None
*/
static void I2C_Master_ADDR(I2C_HandleTypeDef *hi2c)
{
  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_ModeTypeDef CurrentMode       = hi2c->Mode;
  uint32_t CurrentXferOptions           = hi2c->XferOptions;
  uint32_t Prev_State                   = hi2c->PreviousState;

  if (hi2c->State == HAL_I2C_STATE_BUSY_RX)
  {
    if ((hi2c->EventCount == 0U) && (CurrentMode == HAL_I2C_MODE_MEM))
    {
      /* Clear ADDR flag - simulated */
      /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
    }
    else if ((hi2c->EventCount == 0U) && (hi2c->Init.AddressingMode == I2C_ADDRESSINGMODE_10BIT))
    {
      /* Clear ADDR flag - simulated */
      /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

      /* Generate Restart - simulated */
      /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_START); */

      hi2c->EventCount++;
    }
    else
    {
      if (hi2c->XferCount == 0U)
      {
        /* Clear ADDR flag - simulated */
        /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

        /* Generate Stop - simulated */
        /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP); */
      }
      else if (hi2c->XferCount == 1U)
      {
        if (CurrentXferOptions == I2C_NO_OPTION_FRAME)
        {
          /* Disable Acknowledge - simulated */
          /* [IRQ REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

          /* DMA check preserved for logic flow */
          if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
          {
            /* Disable Acknowledge - simulated */
            /* [IRQ REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

            /* Clear ADDR flag - simulated */
            /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
          }
          else
          {
            /* Clear ADDR flag - simulated */
            /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

            /* Generate Stop - simulated */
            /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP); */
          }
        }
        /* Prepare next transfer or stop current transfer */
        else if ((CurrentXferOptions != I2C_FIRST_AND_LAST_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME) \
                 && ((Prev_State != I2C_STATE_MASTER_BUSY_RX) || (CurrentXferOptions == I2C_FIRST_FRAME)))
        {
          if ((CurrentXferOptions != I2C_NEXT_FRAME) && (CurrentXferOptions != I2C_FIRST_AND_NEXT_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME_NO_STOP))
          {
            /* Disable Acknowledge - simulated */
            /* [IRQ REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */
          }
          else
          {
            /* Enable Acknowledge - simulated */
            /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */
          }

          /* Clear ADDR flag - simulated */
          /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
        }
        else
        {
          /* Disable Acknowledge - simulated */
          /* [IRQ REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

          /* Clear ADDR flag - simulated */
          /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

          /* Generate Stop - simulated */
          /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP); */
        }
      }
      else if (hi2c->XferCount == 2U)
      {
        if ((CurrentXferOptions != I2C_NEXT_FRAME) && (CurrentXferOptions != I2C_FIRST_AND_NEXT_FRAME) && (CurrentXferOptions != I2C_LAST_FRAME_NO_STOP))
        {
          /* Disable Acknowledge - simulated */
          /* [IRQ REMOVED] CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

          /* Enable Pos - simulated */
          /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_POS); */
        }
        else
        {
          /* Enable Acknowledge - simulated */
          /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */
        }

        /* DMA check preserved for logic flow */
        if (((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN) && ((CurrentXferOptions == I2C_NO_OPTION_FRAME) || (CurrentXferOptions == I2C_FIRST_FRAME) || (CurrentXferOptions == I2C_FIRST_AND_LAST_FRAME) || (CurrentXferOptions == I2C_LAST_FRAME_NO_STOP) || (CurrentXferOptions == I2C_LAST_FRAME)))
        {
          /* Enable Last DMA bit - simulated */
          /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST); */
        }

        /* Clear ADDR flag - simulated */
        /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
      }
      else
      {
        /* Enable Acknowledge - simulated */
        /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

        /* DMA check preserved for logic flow */
        if (((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN) && ((CurrentXferOptions == I2C_NO_OPTION_FRAME) || (CurrentXferOptions == I2C_FIRST_FRAME) || (CurrentXferOptions == I2C_FIRST_AND_LAST_FRAME) || (CurrentXferOptions == I2C_LAST_FRAME_NO_STOP) || (CurrentXferOptions == I2C_LAST_FRAME)))
        {
          /* Enable Last DMA bit - simulated */
          /* [IRQ REMOVED] SET_BIT(hi2c->Instance->CR2, I2C_CR2_LAST); */
        }

        /* Clear ADDR flag - simulated */
        /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
      }

      /* Reset Event counter  */
      hi2c->EventCount = 0U;
    }
  }
  else
  {
    /* Clear ADDR flag - simulated */
    /* [IRQ REMOVED] __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */
  }
}
```

=== 信息结束 ===
```

### I2C_RequestMemoryRead

```text
=== I2C_RequestMemoryRead 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：6827
- 函数内容：static HAL_StatusTypeDef I2C_RequestMemoryRead(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint32_t Timeout, uint32_t Tickstart)
{
  /* Enable Acknowledge */
  SET_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

  /* Generate Start */
  SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

  /* Wait until SB flag is set */
  if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_SB, RESET, Timeout, Tickstart) != HAL_OK)
  {
    if (READ_BIT(hi2c->Instance->CR1, I2C_CR1_START) == I2C_CR1_START)
    {
      hi2c->ErrorCode = HAL_I2C_WRONG_START;
    }
    return HAL_TIMEOUT;
  }

  /* Send slave address */
  hi2c->Instance->DR = I2C_7BIT_ADD_WRITE(DevAddress);

  /* Wait until ADDR flag is set */
  if (I2C_WaitOnMasterAddressFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, Timeout, Tickstart) != HAL_OK)
  {
    return HAL_ERROR;
  }

  /* Clear ADDR flag */
  __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

  /* Wait until TXE flag is set */
  if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, Tickstart) != HAL_OK)
  {
    if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
    {
      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    return HAL_ERROR;
  }

  /* If Memory address size is 8Bit */
  if (MemAddSize == I2C_MEMADD_SIZE_8BIT)
  {
    /* Send Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_LSB(MemAddress);
  }
  /* If Memory address size is 16Bit */
  else
  {
    /* Send MSB of Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_MSB(MemAddress);

    /* Wait until TXE flag is set */
    if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, Tickstart) != HAL_OK)
    {
      if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
      {
        /* Generate Stop */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
      }
      return HAL_ERROR;
    }

    /* Send LSB of Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_LSB(MemAddress);
  }

  /* Wait until TXE flag is set */
  if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, Tickstart) != HAL_OK)
  {
    if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
    {
      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    return HAL_ERROR;
  }

  /* Generate Restart */
  SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

  /* Wait until SB flag is set */
  if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_SB, RESET, Timeout, Tickstart) != HAL_OK)
  {
    if (READ_BIT(hi2c->Instance->CR1, I2C_CR1_START) == I2C_CR1_START)
    {
      hi2c->ErrorCode = HAL_I2C_WRONG_START;
    }
    return HAL_TIMEOUT;
  }

  /* Send slave address */
  hi2c->Instance->DR = I2C_7BIT_ADD_READ(DevAddress);

  /* Wait until ADDR flag is set */
  if (I2C_WaitOnMasterAddressFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, Timeout, Tickstart) != HAL_OK)
  {
    return HAL_ERROR;
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Static helper function that handles I2C memory read request sequence by sending device address and memory address with proper start/restart conditions
- 是否需要替换：是
- 分类/替换原因：Function contains multiple polling loops through timeout functions (I2C_WaitOnFlagUntilTimeout, I2C_WaitOnMasterAddressFlagUntilTimeout, I2C_WaitOnTXEFlagUntilTimeout) that wait for hardware status flags (SB, ADDR, TXE). It performs MMIO operations (SET_BIT on CR1, writes to DR) that need to be removed. According to LOOP strategy: skip polling loops entirely (assume conditions are met) and remove hardware register writes while preserving function structure and returning success.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Master sends target device address followed by internal memory address for read request.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for I2C module
* @param  DevAddress Target device address: The device 7 bits address value
*         in datasheet must be shifted to the left before calling the interface
* @param  MemAddress Internal memory address
* @param  MemAddSize Size of internal memory address
* @param  Timeout Timeout duration
* @param  Tickstart Tick start value
* @retval HAL status
*/
static HAL_StatusTypeDef I2C_RequestMemoryRead(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Skip hardware polling loops and register writes */
  
  /* Preserve error handling logic for timeout case */
  /* Original timeout check would return HAL_TIMEOUT if wait failed */
  /* We assume success, so skip timeout error path */
  
  /* Preserve error handling logic for address flag timeout */
  /* Original would return HAL_ERROR if wait failed */
  /* We assume success, so skip error path */
  
  /* Preserve error handling logic for TXE flag timeout */
  /* Original would check for ACK failure and generate STOP */
  /* We assume success, so skip error path */
  
  /* For 16-bit memory address, original would send MSB then LSB */
  /* We skip the actual hardware writes */
  
  /* Preserve the restart sequence logic */
  /* Skip actual hardware restart generation */
  
  /* Skip final address flag wait */
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_RequestMemoryWrite

```text
=== I2C_RequestMemoryWrite 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：6747
- 函数内容：static HAL_StatusTypeDef I2C_RequestMemoryWrite(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint32_t Timeout, uint32_t Tickstart)
{
  /* Generate Start */
  SET_BIT(hi2c->Instance->CR1, I2C_CR1_START);

  /* Wait until SB flag is set */
  if (I2C_WaitOnFlagUntilTimeout(hi2c, I2C_FLAG_SB, RESET, Timeout, Tickstart) != HAL_OK)
  {
    if (READ_BIT(hi2c->Instance->CR1, I2C_CR1_START) == I2C_CR1_START)
    {
      hi2c->ErrorCode = HAL_I2C_WRONG_START;
    }
    return HAL_TIMEOUT;
  }

  /* Send slave address */
  hi2c->Instance->DR = I2C_7BIT_ADD_WRITE(DevAddress);

  /* Wait until ADDR flag is set */
  if (I2C_WaitOnMasterAddressFlagUntilTimeout(hi2c, I2C_FLAG_ADDR, Timeout, Tickstart) != HAL_OK)
  {
    return HAL_ERROR;
  }

  /* Clear ADDR flag */
  __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

  /* Wait until TXE flag is set */
  if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, Tickstart) != HAL_OK)
  {
    if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
    {
      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
    }
    return HAL_ERROR;
  }

  /* If Memory address size is 8Bit */
  if (MemAddSize == I2C_MEMADD_SIZE_8BIT)
  {
    /* Send Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_LSB(MemAddress);
  }
  /* If Memory address size is 16Bit */
  else
  {
    /* Send MSB of Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_MSB(MemAddress);

    /* Wait until TXE flag is set */
    if (I2C_WaitOnTXEFlagUntilTimeout(hi2c, Timeout, Tickstart) != HAL_OK)
    {
      if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
      {
        /* Generate Stop */
        SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);
      }
      return HAL_ERROR;
    }

    /* Send LSB of Memory Address */
    hi2c->Instance->DR = I2C_MEM_ADD_LSB(MemAddress);
  }

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Performs I2C protocol sequence for initiating memory write operation by sending start condition, device address, and memory address
- 是否需要替换：是
- 分类/替换原因：Function contains multiple polling loops through wait functions (I2C_WaitOnFlagUntilTimeout, I2C_WaitOnMasterAddressFlagUntilTimeout, I2C_WaitOnTXEFlagUntilTimeout) that check hardware status flags (SB, ADDR, TXE). It performs MMIO operations to control I2C hardware registers (CR1, DR). According to classification priority, LOOP applies to functions with peripheral-dependent loops where conditions depend on hardware registers. The replacement skips polling loops and assumes conditions are met while preserving error handling and control flow.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static HAL_StatusTypeDef I2C_RequestMemoryWrite(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint16_t MemAddress, uint16_t MemAddSize, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Skip hardware start generation */
  
  /* [LOOP REMOVED] Skip waiting for SB flag */
  /* Simulate timeout check failure path */
  if (0)  /* Always false to skip timeout path */
  {
    if (0)  /* Always false to skip wrong start check */
    {
      hi2c->ErrorCode = HAL_I2C_WRONG_START;
    }
    return HAL_TIMEOUT;
  }

  /* [LOOP REMOVED] Skip sending slave address to hardware */
  
  /* [LOOP REMOVED] Skip waiting for ADDR flag */
  if (0)  /* Always false to skip error path */
  {
    return HAL_ERROR;
  }

  /* [LOOP REMOVED] Skip clearing ADDR flag */
  
  /* [LOOP REMOVED] Skip waiting for TXE flag */
  if (0)  /* Always false to skip error path */
  {
    if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
    {
      /* [LOOP REMOVED] Skip generating stop condition */
    }
    return HAL_ERROR;
  }

  /* If Memory address size is 8Bit */
  if (MemAddSize == I2C_MEMADD_SIZE_8BIT)
  {
    /* [LOOP REMOVED] Skip sending memory address to hardware */
  }
  /* If Memory address size is 16Bit */
  else
  {
    /* [LOOP REMOVED] Skip sending MSB of memory address */
    
    /* [LOOP REMOVED] Skip waiting for TXE flag */
    if (0)  /* Always false to skip error path */
    {
      if (hi2c->ErrorCode == HAL_I2C_ERROR_AF)
      {
        /* [LOOP REMOVED] Skip generating stop condition */
      }
      return HAL_ERROR;
    }

    /* [LOOP REMOVED] Skip sending LSB of memory address */
  }

  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_Slave_ADDR

```text
=== I2C_Slave_ADDR 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：6122
- 函数内容：static void I2C_Slave_ADDR(I2C_HandleTypeDef *hi2c, uint32_t IT2Flags)
{
  uint8_t TransferDirection = I2C_DIRECTION_RECEIVE;
  uint16_t SlaveAddrCode;

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    /* Disable BUF interrupt, BUF enabling is manage through slave specific interface */
    __HAL_I2C_DISABLE_IT(hi2c, (I2C_IT_BUF));

    /* Transfer Direction requested by Master */
    if (I2C_CHECK_FLAG(IT2Flags, I2C_FLAG_TRA) == RESET)
    {
      TransferDirection = I2C_DIRECTION_TRANSMIT;
    }

    if (I2C_CHECK_FLAG(IT2Flags, I2C_FLAG_DUALF) == RESET)
    {
      SlaveAddrCode = (uint16_t)hi2c->Init.OwnAddress1;
    }
    else
    {
      SlaveAddrCode = (uint16_t)hi2c->Init.OwnAddress2;
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Call Slave Addr callback */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->AddrCallback(hi2c, TransferDirection, SlaveAddrCode);
#else
    HAL_I2C_AddrCallback(hi2c, TransferDirection, SlaveAddrCode);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
  else
  {
    /* Clear ADDR flag */
    __HAL_I2C_CLEAR_ADDRFLAG(hi2c);

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Handles the ADD (address) flag for I2C slave mode, called from interrupt handler to process address matching and trigger callbacks
- 是否需要替换：是
- 分类/替换原因：Based on analysis: 1) Function is called from HAL_I2C_EV_IRQHandler (interrupt handler), 2) Contains hardware interrupt control operations (__HAL_I2C_DISABLE_IT, __HAL_I2C_CLEAR_ADDRFLAG), 3) Processes interrupt flags (IT2Flags) to determine transfer direction and address, 4) Triggers callback functions important for application logic, 5) Not a CORE function (no NVIC/OS/VTOR operations), 6) Not a data reception/transmission function, 7) Not an initialization or polling loop function. The function fits the IRQ classification as it handles interrupt-related operations and needs hardware operations removed while preserving callback logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Handle ADD flag for Slave
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for I2C module
* @param  IT2Flags Interrupt2 flags to handle.
* @retval None
*/
static void I2C_Slave_ADDR(I2C_HandleTypeDef *hi2c, uint32_t IT2Flags)
{
  uint8_t TransferDirection = I2C_DIRECTION_RECEIVE;
  uint16_t SlaveAddrCode;

  if (((uint32_t)hi2c->State & (uint32_t)HAL_I2C_STATE_LISTEN) == (uint32_t)HAL_I2C_STATE_LISTEN)
  {
    /* Disable BUF interrupt - hardware operation removed in simulation */
    /* __HAL_I2C_DISABLE_IT(hi2c, (I2C_IT_BUF)); */

    /* Transfer Direction requested by Master */
    if (I2C_CHECK_FLAG(IT2Flags, I2C_FLAG_TRA) == RESET)
    {
      TransferDirection = I2C_DIRECTION_TRANSMIT;
    }

    if (I2C_CHECK_FLAG(IT2Flags, I2C_FLAG_DUALF) == RESET)
    {
      SlaveAddrCode = (uint16_t)hi2c->Init.OwnAddress1;
    }
    else
    {
      SlaveAddrCode = (uint16_t)hi2c->Init.OwnAddress2;
    }

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);

    /* Call Slave Addr callback */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
    hi2c->AddrCallback(hi2c, TransferDirection, SlaveAddrCode);
#else
    HAL_I2C_AddrCallback(hi2c, TransferDirection, SlaveAddrCode);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
  }
  else
  {
    /* Clear ADDR flag - hardware operation removed in simulation */
    /* __HAL_I2C_CLEAR_ADDRFLAG(hi2c); */

    /* Process Unlocked */
    __HAL_UNLOCK(hi2c);
  }
}
```

=== 信息结束 ===
```

### I2C_Slave_STOPF

```text
=== I2C_Slave_STOPF 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：6173
- 函数内容：static void I2C_Slave_STOPF(I2C_HandleTypeDef *hi2c)
{
  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_StateTypeDef CurrentState = hi2c->State;

  /* Disable EVT, BUF and ERR interrupt */
  __HAL_I2C_DISABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR);

  /* Clear STOPF flag */
  __HAL_I2C_CLEAR_STOPFLAG(hi2c);

  /* Disable Acknowledge */
  CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK);

  /* If a DMA is ongoing, Update handle size context */
  if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
  {
    if ((CurrentState == HAL_I2C_STATE_BUSY_RX) || (CurrentState == HAL_I2C_STATE_BUSY_RX_LISTEN))
    {
      hi2c->XferCount = (uint16_t)(I2C_GET_DMA_REMAIN_DATA(hi2c->hdmarx));

      if (hi2c->XferCount != 0U)
      {
        /* Set ErrorCode corresponding to a Non-Acknowledge */
        hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
      }

      /* Disable, stop the current DMA */
      CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

      /* Abort DMA Xfer if any */
      if (HAL_DMA_GetState(hi2c->hdmarx) != HAL_DMA_STATE_READY)
      {
        /* Set the I2C DMA Abort callback :
        will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA RX */
        if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
        }
      }
    }
    else
    {
      hi2c->XferCount = (uint16_t)(I2C_GET_DMA_REMAIN_DATA(hi2c->hdmatx));

      if (hi2c->XferCount != 0U)
      {
        /* Set ErrorCode corresponding to a Non-Acknowledge */
        hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
      }

      /* Disable, stop the current DMA */
      CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN);

      /* Abort DMA Xfer if any */
      if (HAL_DMA_GetState(hi2c->hdmatx) != HAL_DMA_STATE_READY)
      {
        /* Set the I2C DMA Abort callback :
        will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA TX */
        if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
        }
      }
    }
  }

  /* All data are not transferred, so set error code accordingly */
  if (hi2c->XferCount != 0U)
  {
    /* Store Last receive data if any */
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET)
    {
      /* Read data from DR */
      *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
    }

    /* Store Last receive data if any */
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_RXNE) == SET)
    {
      /* Read data from DR */
      *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR;

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
    }

    if (hi2c->XferCount != 0U)
    {
      /* Set ErrorCode corresponding to a Non-Acknowledge */
      hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
    }
  }

  if (hi2c->ErrorCode != HAL_I2C_ERROR_NONE)
  {
    /* Call the corresponding callback to inform upper layer of End of Transfer */
    I2C_ITError(hi2c);
  }
  else
  {
    if (CurrentState == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      /* Set state at HAL_I2C_STATE_LISTEN */
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_LISTEN;

      /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
      hi2c->SlaveRxCpltCallback(hi2c);
#else
      HAL_I2C_SlaveRxCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
    }

    if (hi2c->State == HAL_I2C_STATE_LISTEN)
    {
      hi2c->XferOptions = I2C_NO_OPTION_FRAME;
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_READY;
      hi2c->Mode = HAL_I2C_MODE_NONE;

      /* Call the Listen Complete callback, to inform upper layer of the end of Listen usecase */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
      hi2c->ListenCpltCallback(hi2c);
#else
      HAL_I2C_ListenCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
    }
    else
    {
      if ((hi2c->PreviousState  == I2C_STATE_SLAVE_BUSY_RX) || (CurrentState == HAL_I2C_STATE_BUSY_RX))
      {
        hi2c->PreviousState = I2C_STATE_NONE;
        hi2c->State = HAL_I2C_STATE_READY;
        hi2c->Mode = HAL_I2C_MODE_NONE;

#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
        hi2c->SlaveRxCpltCallback(hi2c);
#else
        HAL_I2C_SlaveRxCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
      }
    }
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Handles STOP condition flag for I2C slave mode, manages DMA operations, updates state machine, and calls appropriate callbacks
- 是否需要替换：是
- 分类/替换原因：Function is called from HAL_I2C_EV_IRQHandler (interrupt handler), contains MMIO operations for interrupt control and flag management, handles interrupt-driven state transitions, and is part of the I2C interrupt handling flow. It's not CORE (no NVIC/OS kernel/VTOR operations), not purely RECV (though it does some data reading, primary purpose is interrupt handling), and fits the IRQ classification criteria.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Handle STOPF flag for Slave
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for I2C module
* @retval None
*/
static void I2C_Slave_STOPF(I2C_HandleTypeDef *hi2c)
{
  /* Declaration of temporary variable to prevent undefined behavior of volatile usage */
  HAL_I2C_StateTypeDef CurrentState = hi2c->State;

  /* Skip hardware interrupt disable operations */
  /* __HAL_I2C_DISABLE_IT(hi2c, I2C_IT_EVT | I2C_IT_BUF | I2C_IT_ERR); */

  /* Skip clearing STOPF flag */
  /* __HAL_I2C_CLEAR_STOPFLAG(hi2c); */

  /* Skip disabling Acknowledge */
  /* CLEAR_BIT(hi2c->Instance->CR1, I2C_CR1_ACK); */

  /* If a DMA is ongoing, Update handle size context */
  if ((hi2c->Instance->CR2 & I2C_CR2_DMAEN) == I2C_CR2_DMAEN)
  {
    if ((CurrentState == HAL_I2C_STATE_BUSY_RX) || (CurrentState == HAL_I2C_STATE_BUSY_RX_LISTEN))
    {
      /* Simulate getting remaining DMA data */
      hi2c->XferCount = 0U; /* Assume all data transferred */

      if (hi2c->XferCount != 0U)
      {
        /* Set ErrorCode corresponding to a Non-Acknowledge */
        hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
      }

      /* Skip disabling DMA hardware */
      /* CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN); */

      /* Abort DMA Xfer if any */
      if (HAL_DMA_GetState(hi2c->hdmarx) != HAL_DMA_STATE_READY)
      {
        /* Set the I2C DMA Abort callback :
        will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmarx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA RX */
        if (HAL_DMA_Abort_IT(hi2c->hdmarx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmarx->XferAbortCallback(hi2c->hdmarx);
        }
      }
    }
    else
    {
      /* Simulate getting remaining DMA data */
      hi2c->XferCount = 0U; /* Assume all data transferred */

      if (hi2c->XferCount != 0U)
      {
        /* Set ErrorCode corresponding to a Non-Acknowledge */
        hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
      }

      /* Skip disabling DMA hardware */
      /* CLEAR_BIT(hi2c->Instance->CR2, I2C_CR2_DMAEN); */

      /* Abort DMA Xfer if any */
      if (HAL_DMA_GetState(hi2c->hdmatx) != HAL_DMA_STATE_READY)
      {
        /* Set the I2C DMA Abort callback :
        will lead to call HAL_I2C_ErrorCallback() at end of DMA abort procedure */
        hi2c->hdmatx->XferAbortCallback = I2C_DMAAbort;

        /* Abort DMA TX */
        if (HAL_DMA_Abort_IT(hi2c->hdmatx) != HAL_OK)
        {
          /* Call Directly XferAbortCallback function in case of error */
          hi2c->hdmatx->XferAbortCallback(hi2c->hdmatx);
        }
      }
    }
  }

  /* All data are not transferred, so set error code accordingly */
  if (hi2c->XferCount != 0U)
  {
    /* Store Last receive data if any */
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == SET)
    {
      /* Simulate reading data from DR */
      /* *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR; */
      /* Use helper to simulate data reception */
      HAL_BE_In(hi2c->pBuffPtr, 1);

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
    }

    /* Store Last receive data if any */
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_RXNE) == SET)
    {
      /* Simulate reading data from DR */
      /* *hi2c->pBuffPtr = (uint8_t)hi2c->Instance->DR; */
      /* Use helper to simulate data reception */
      HAL_BE_In(hi2c->pBuffPtr, 1);

      /* Increment Buffer pointer */
      hi2c->pBuffPtr++;

      /* Update counter */
      hi2c->XferCount--;
    }

    if (hi2c->XferCount != 0U)
    {
      /* Set ErrorCode corresponding to a Non-Acknowledge */
      hi2c->ErrorCode |= HAL_I2C_ERROR_AF;
    }
  }

  if (hi2c->ErrorCode != HAL_I2C_ERROR_NONE)
  {
    /* Call the corresponding callback to inform upper layer of End of Transfer */
    I2C_ITError(hi2c);
  }
  else
  {
    if (CurrentState == HAL_I2C_STATE_BUSY_RX_LISTEN)
    {
      /* Set state at HAL_I2C_STATE_LISTEN */
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_LISTEN;

      /* Call the corresponding callback to inform upper layer of End of Transfer */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
      hi2c->SlaveRxCpltCallback(hi2c);
#else
      HAL_I2C_SlaveRxCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
    }

    if (hi2c->State == HAL_I2C_STATE_LISTEN)
    {
      hi2c->XferOptions = I2C_NO_OPTION_FRAME;
      hi2c->PreviousState = I2C_STATE_NONE;
      hi2c->State = HAL_I2C_STATE_READY;
      hi2c->Mode = HAL_I2C_MODE_NONE;

      /* Call the Listen Complete callback, to inform upper layer of the end of Listen usecase */
#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
      hi2c->ListenCpltCallback(hi2c);
#else
      HAL_I2C_ListenCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
    }
    else
    {
      if ((hi2c->PreviousState  == I2C_STATE_SLAVE_BUSY_RX) || (CurrentState == HAL_I2C_STATE_BUSY_RX))
      {
        hi2c->PreviousState = I2C_STATE_NONE;
        hi2c->State = HAL_I2C_STATE_READY;
        hi2c->Mode = HAL_I2C_MODE_NONE;

#if (USE_HAL_I2C_REGISTER_CALLBACKS == 1)
        hi2c->SlaveRxCpltCallback(hi2c);
#else
        HAL_I2C_SlaveRxCpltCallback(hi2c);
#endif /* USE_HAL_I2C_REGISTER_CALLBACKS */
      }
    }
  }
}
```

=== 信息结束 ===
```

### I2C_WaitOnBTFFlagUntilTimeout

```text
=== I2C_WaitOnBTFFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7357
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnBTFFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{
  while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == RESET)
  {
    /* Check if a NACK is detected */
    if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Check for the Timeout */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
      {
        if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_BTF) == RESET))
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          /* Process Unlocked */
          __HAL_UNLOCK(hi2c);

          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for I2C BTF (Byte Transfer Finished) flag to be set with timeout handling and NACK detection
- 是否需要替换：是
- 分类/替换原因：This function contains a while loop that polls the hardware BTF flag using __HAL_I2C_GET_FLAG macro (MMIO operations at lines 7359 and 7372). The loop condition depends on peripheral register status, making it a peripheral-dependent polling loop. According to the LOOP classification strategy, we should skip the polling loop entirely and assume the condition is already met (transfer complete), while preserving timeout logic, NACK detection, and state updates. The function is called by HAL_I2C_Mem_Write and HAL_I2C_Master_Transmit functions, indicating it's a helper function for I2C data transfer operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function handles I2C Communication Timeout for specific usage of BTF flag.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @param  Timeout Timeout duration
* @param  Tickstart Tick start value
* @retval HAL status
*/
static HAL_StatusTypeDef I2C_WaitOnBTFFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Skip polling for BTF flag, assume transfer is complete */
  
  /* Check if a NACK is detected */
  if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)
  {
    return HAL_ERROR;
  }

  /* Check for the Timeout */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      /* [LOOP REMOVED] Skip flag check, assume timeout occurred */
      hi2c->PreviousState       = I2C_STATE_NONE;
      hi2c->State               = HAL_I2C_STATE_READY;
      hi2c->Mode                = HAL_I2C_MODE_NONE;
      hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_WaitOnFlagUntilTimeout

```text
=== I2C_WaitOnFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7225
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Flag, FlagStatus Status, uint32_t Timeout, uint32_t Tickstart)
{
  /* Wait until flag is set */
  while (__HAL_I2C_GET_FLAG(hi2c, Flag) == Status)
  {
    /* Check for the Timeout */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
      {
        if ((__HAL_I2C_GET_FLAG(hi2c, Flag) == Status))
        {
          hi2c->PreviousState     = I2C_STATE_NONE;
          hi2c->State             = HAL_I2C_STATE_READY;
          hi2c->Mode              = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode         |= HAL_I2C_ERROR_TIMEOUT;

          /* Process Unlocked */
          __HAL_UNLOCK(hi2c);

          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for a specific I2C flag to reach desired status with timeout handling
- 是否需要替换：是
- 分类/替换原因：Function contains a polling loop that continuously checks I2C flag status using __HAL_I2C_GET_FLAG macro (which reads peripheral registers). The loop condition depends on hardware flag status, making it a peripheral-dependent loop. According to LOOP classification strategy, polling loops waiting for status flags should be skipped entirely, assuming the condition is already met. The function also contains timeout error handling that updates I2C handle state and error codes, which must be preserved. GetMMIOFunctionInfo revealed binary operations and variable accesses related to flag checking, confirming hardware register dependencies. The function is called by multiple I2C communication functions (HAL_I2C_Master_Transmit, HAL_I2C_Master_Receive, etc.) for waiting on various I2C flags.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static HAL_StatusTypeDef I2C_WaitOnFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Flag, FlagStatus Status, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Skip polling loop for I2C flag status, assume condition already met */
  
  /* Check for timeout condition - preserve error handling logic */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      /* Simulate flag check failure on timeout */
      hi2c->PreviousState     = I2C_STATE_NONE;
      hi2c->State             = HAL_I2C_STATE_READY;
      hi2c->Mode              = HAL_I2C_MODE_NONE;
      hi2c->ErrorCode         |= HAL_I2C_ERROR_TIMEOUT;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_WaitOnMasterAddressFlagUntilTimeout

```text
=== I2C_WaitOnMasterAddressFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7262
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnMasterAddressFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Flag, uint32_t Timeout, uint32_t Tickstart)
{
  while (__HAL_I2C_GET_FLAG(hi2c, Flag) == RESET)
  {
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_AF) == SET)
    {
      /* Generate Stop */
      SET_BIT(hi2c->Instance->CR1, I2C_CR1_STOP);

      /* Clear AF Flag */
      __HAL_I2C_CLEAR_FLAG(hi2c, I2C_FLAG_AF);

      hi2c->PreviousState       = I2C_STATE_NONE;
      hi2c->State               = HAL_I2C_STATE_READY;
      hi2c->Mode                = HAL_I2C_MODE_NONE;
      hi2c->ErrorCode           |= HAL_I2C_ERROR_AF;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    /* Check for the Timeout */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
      {
        if ((__HAL_I2C_GET_FLAG(hi2c, Flag) == RESET))
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          /* Process Unlocked */
          __HAL_UNLOCK(hi2c);

          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for a specific I2C flag to be set during master addressing phase with timeout handling
- 是否需要替换：是
- 分类/替换原因：This function contains a peripheral-dependent polling loop that waits for I2C hardware flags (__HAL_I2C_GET_FLAG). The while loop condition depends on peripheral register status, making it a LOOP type function. It performs hardware flag polling, timeout checking using HAL_GetTick(), and updates I2C handle state variables. According to the LOOP strategy, we should skip the wait loop entirely and assume the condition is already met, while preserving non-hardware logic. The function is static and called by various I2C master request functions (I2C_MasterRequestRead, I2C_MasterRequestWrite, etc.).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function handles I2C Communication Timeout for Master addressing phase.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*         the configuration information for I2C module
* @param  Flag specifies the I2C flag to check.
* @param  Timeout Timeout duration
* @param  Tickstart Tick start value
* @retval HAL status
*/
static HAL_StatusTypeDef I2C_WaitOnMasterAddressFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Flag, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Skip hardware polling loop, assume flag is already set */
  
  /* Check for Address Failure (AF) flag - simulate the condition */
  /* In simulation, we assume no address failure occurs */
  /* Original hardware check: if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_AF) == SET) */
  
  /* Skip timeout check since we're not actually waiting */
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_WaitOnRXNEFlagUntilTimeout

```text
=== I2C_WaitOnRXNEFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7463
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnRXNEFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{

  while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_RXNE) == RESET)
  {
    /* Check if a STOPF is detected */
    if (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_STOPF) == SET)
    {
      /* Clear STOP Flag */
      __HAL_I2C_CLEAR_FLAG(hi2c, I2C_FLAG_STOPF);

      hi2c->PreviousState       = I2C_STATE_NONE;
      hi2c->State               = HAL_I2C_STATE_READY;
      hi2c->Mode                = HAL_I2C_MODE_NONE;
      hi2c->ErrorCode           |= HAL_I2C_ERROR_NONE;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }

    /* Check for the Timeout */
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_RXNE) == RESET))
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for I2C RXNE (Receive Data Register Not Empty) flag to be set with timeout handling, used in I2C receive operations
- 是否需要替换：是
- 分类/替换原因：This function contains a polling loop that waits for hardware status flags (RXNE and STOPF) with timeout handling. GetMMIOFunctionInfo revealed multiple MMIO operations including __HAL_I2C_GET_FLAG and __HAL_I2C_CLEAR_FLAG. The function's primary purpose is to wait for peripheral hardware conditions, making it a LOOP type. According to LOOP strategy: 'If waiting for a status flag: Skip the loop entirely (assume the condition is already met)'. The replacement removes the hardware-dependent polling loop while preserving the function signature and returning HAL_OK immediately.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  This function handles I2C Communication Timeout for specific usage of RXNE flag.\n* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains\n*                the configuration information for the specified I2C.\n* @param  Timeout Timeout duration\n* @param  Tickstart Tick start value\n* @retval HAL status\n*/\nstatic HAL_StatusTypeDef I2C_WaitOnRXNEFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)\n{\n  /* [LOOP REMOVED] Waited for I2C RXNE flag */\n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### I2C_WaitOnSTOPFlagUntilTimeout

```text
=== I2C_WaitOnSTOPFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7398
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnSTOPFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{
  while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_STOPF) == RESET)
  {
    /* Check if a NACK is detected */
    if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Check for the Timeout */
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_STOPF) == RESET))
      {
        hi2c->PreviousState       = I2C_STATE_NONE;
        hi2c->State               = HAL_I2C_STATE_READY;
        hi2c->Mode                = HAL_I2C_MODE_NONE;
        hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

        /* Process Unlocked */
        __HAL_UNLOCK(hi2c);

        return HAL_ERROR;
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for I2C STOP flag to be set with timeout handling and NACK detection
- 是否需要替换：是
- 分类/替换原因：This function contains a while loop that polls the I2C STOP flag using __HAL_I2C_GET_FLAG (MMIO operation) and has timeout checking. GetMMIOFunctionInfo revealed binary MMIO expressions at lines 7400 and 7411 corresponding to the flag checks. The function is called by HAL_I2C_Slave_Receive and calls I2C_IsAcknowledgeFailed and HAL_GetTick. According to the LOOP classification criteria: 'If waiting for a status flag: Skip the loop entirely (assume the condition is already met)'. The function is not CORE (no NVIC/OS/VTOR), not RECV (no data I/O), not IRQ (not interrupt handler), not INIT (not initialization), but specifically fits LOOP due to its peripheral-dependent polling loop.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  This function handles I2C Communication Timeout for specific usage of STOP flag.\n* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains\n*                the configuration information for the specified I2C.\n* @param  Timeout Timeout duration\n* @param  Tickstart Tick start value\n* @retval HAL status\n*/\nstatic HAL_StatusTypeDef I2C_WaitOnSTOPFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)\n{\n  /* [LOOP REMOVED] Skip waiting for hardware STOP flag, assume condition is met */\n  \n  /* Check if a NACK is detected */\n  if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)\n  {\n    return HAL_ERROR;\n  }\n  \n  /* Check for the Timeout - preserve timeout logic but skip hardware check */\n  if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))\n  {\n    /* Assume STOP flag is already set, so skip timeout error handling */\n  }\n  \n  return HAL_OK;\n}
```

=== 信息结束 ===
```

### I2C_WaitOnSTOPRequestThroughIT

```text
=== I2C_WaitOnSTOPRequestThroughIT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7434
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnSTOPRequestThroughIT(I2C_HandleTypeDef *hi2c)
{
  __IO uint32_t count = 0U;

  /* Wait until STOP flag is reset */
  count = I2C_TIMEOUT_STOP_FLAG * (SystemCoreClock / 25U / 1000U);
  do
  {
    count--;
    if (count == 0U)
    {
      hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

      return HAL_ERROR;
    }
  }
  while (READ_BIT(hi2c->Instance->CR1, I2C_CR1_STOP) == I2C_CR1_STOP);

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for I2C STOP flag to be reset with timeout handling for interrupt-based STOP request usage
- 是否需要替换：是
- 分类/替换原因：This function contains a peripheral-dependent polling loop that waits for the I2C STOP flag (I2C_CR1_STOP) to clear. The loop condition depends on reading hardware register hi2c->Instance->CR1 through READ_BIT macro. According to the LOOP classification criteria: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags)'. The function implements timeout handling and error reporting but its core functionality is polling a hardware flag. It is not CORE (no NVIC/OS/VTOR operations), not RECV (no data transfer), not IRQ (not an interrupt handler), not INIT (not initialization). The replacement strategy for LOOP is to skip the polling loop entirely and assume the condition is met.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  This function handles I2C Communication Timeout for specific usage of STOP request through Interrupt.
* @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
*                the configuration information for the specified I2C.
* @retval HAL status
*/
static HAL_StatusTypeDef I2C_WaitOnSTOPRequestThroughIT(I2C_HandleTypeDef *hi2c)
{
  /* [LOOP REMOVED] Waited for hardware STOP flag to be reset */
  /* Assume STOP flag is already cleared */
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2C_WaitOnTXEFlagUntilTimeout

```text
=== I2C_WaitOnTXEFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_i2c.c
- 行号：7316
- 函数内容：static HAL_StatusTypeDef I2C_WaitOnTXEFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{
  while (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_TXE) == RESET)
  {
    /* Check if a NACK is detected */
    if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)
    {
      return HAL_ERROR;
    }

    /* Check for the Timeout */
    if (Timeout != HAL_MAX_DELAY)
    {
      if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
      {
        if ((__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_TXE) == RESET))
        {
          hi2c->PreviousState       = I2C_STATE_NONE;
          hi2c->State               = HAL_I2C_STATE_READY;
          hi2c->Mode                = HAL_I2C_MODE_NONE;
          hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

          /* Process Unlocked */
          __HAL_UNLOCK(hi2c);

          return HAL_ERROR;
        }
      }
    }
  }
  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for I2C TXE (Transmit Data Register Empty) flag to be set with timeout handling and NACK detection
- 是否需要替换：是
- 分类/替换原因：This function contains a peripheral-dependent polling loop that waits for the I2C TXE hardware flag (__HAL_I2C_GET_FLAG(hi2c, I2C_FLAG_TXE)). GetMMIOFunctionInfo confirmed MMIO operations through hardware register reads. The function is a static helper called by various I2C communication functions (HAL_I2C_Master_Transmit, HAL_I2C_Mem_Write, etc.) to wait for transmit readiness. According to the classification criteria, this matches LOOP type: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags)'. The strategy for LOOP functions is to skip the polling loop entirely while preserving non-hardware logic like timeout checking, NACK detection, and state updates.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static HAL_StatusTypeDef I2C_WaitOnTXEFlagUntilTimeout(I2C_HandleTypeDef *hi2c, uint32_t Timeout, uint32_t Tickstart)
{
  /* [LOOP REMOVED] Waited for hardware TXE (Transmit Data Register Empty) flag */
  
  /* Check if a NACK is detected - preserve error checking logic */
  if (I2C_IsAcknowledgeFailed(hi2c) != HAL_OK)
  {
    return HAL_ERROR;
  }

  /* Check for the Timeout - preserve timeout logic */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      /* [LOOP REMOVED] Original checked TXE flag here, assume timeout condition */
      hi2c->PreviousState       = I2C_STATE_NONE;
      hi2c->State               = HAL_I2C_STATE_READY;
      hi2c->Mode                = HAL_I2C_MODE_NONE;
      hi2c->ErrorCode           |= HAL_I2C_ERROR_TIMEOUT;

      /* Process Unlocked */
      __HAL_UNLOCK(hi2c);

      return HAL_ERROR;
    }
  }
  
  return HAL_OK;
}
```

=== 信息结束 ===
```

### I2Cx_MspInit

```text
=== I2Cx_MspInit 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/BSP/STM324xG_EVAL/stm324xg_eval.c
- 行号：465
- 函数内容：static void I2Cx_MspInit(void)
{
  GPIO_InitTypeDef  GPIO_InitStruct;  
  
  /*** Configure the GPIOs ***/
  /* Enable GPIO clock */
  EVAL_I2Cx_SCL_SDA_GPIO_CLK_ENABLE();
  
  /* Configure I2C Tx as alternate function */
  GPIO_InitStruct.Pin = EVAL_I2Cx_SCL_PIN;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_OD;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FAST;
  GPIO_InitStruct.Alternate = EVAL_I2Cx_SCL_SDA_AF;
  HAL_GPIO_Init(EVAL_I2Cx_SCL_SDA_GPIO_PORT, &GPIO_InitStruct);
  
  /* Configure I2C Rx as alternate function */
  GPIO_InitStruct.Pin = EVAL_I2Cx_SDA_PIN;
  HAL_GPIO_Init(EVAL_I2Cx_SCL_SDA_GPIO_PORT, &GPIO_InitStruct);
  
  /*** Configure the I2C peripheral ***/ 
  /* Enable I2C clock */
  EVAL_I2Cx_CLK_ENABLE();
  
  /* Force the I2C peripheral clock reset */
  EVAL_I2Cx_FORCE_RESET(); 
  
  /* Release the I2C peripheral clock reset */
  EVAL_I2Cx_RELEASE_RESET(); 
  
  /* Set priority and enable I2Cx event Interrupt */
  HAL_NVIC_SetPriority(EVAL_I2Cx_EV_IRQn, 0x0F, 0);
  HAL_NVIC_EnableIRQ(EVAL_I2Cx_EV_IRQn);
  
  /* Set priority and enable I2Cx error Interrupt */
  HAL_NVIC_SetPriority(EVAL_I2Cx_ER_IRQn, 0x0F, 0);
  HAL_NVIC_EnableIRQ(EVAL_I2Cx_ER_IRQn);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes I2C MSP (Microcontroller Specific Package) by configuring GPIO pins for I2C communication and setting up I2C interrupts
- 是否需要替换：是
- 分类/替换原因：This is an initialization function (MSP init pattern) that configures hardware for I2C communication. GetFunctionInfo shows it performs GPIO configuration (clock enable, pin mode setup) and I2C peripheral configuration (clock enable, reset operations). GetMMIOFunctionInfo reveals hardware register accesses through macros like EVAL_I2Cx_SCL_SDA_GPIO_CLK_ENABLE(), EVAL_I2Cx_CLK_ENABLE(), etc. GetFunctionCallStack shows it calls CORE functions (HAL_NVIC_SetPriority and HAL_NVIC_EnableIRQ) for interrupt configuration. According to classification rules, functions that call CORE functions may be classified as INIT, but their replacement must preserve those CORE calls. This function is not itself a CORE function (it doesn't directly write NVIC registers, it calls HAL_NVIC functions), so it's classified as INIT with the requirement to preserve NVIC configuration calls.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Initializes I2C MSP.
*/
static void I2Cx_MspInit(void)
{
  GPIO_InitTypeDef  GPIO_InitStruct;  
  
  /*** Configure the GPIOs ***/
  /* Skip GPIO clock enable and configuration for simulation */
  
  /*** Configure the I2C peripheral ***/ 
  /* Skip I2C clock enable and reset operations for simulation */
  
  /* Set priority and enable I2Cx event Interrupt */
  HAL_NVIC_SetPriority(EVAL_I2Cx_EV_IRQn, 0x0F, 0);
  HAL_NVIC_EnableIRQ(EVAL_I2Cx_EV_IRQn);
  
  /* Set priority and enable I2Cx error Interrupt */
  HAL_NVIC_SetPriority(EVAL_I2Cx_ER_IRQn, 0x0F, 0);
  HAL_NVIC_EnableIRQ(EVAL_I2Cx_ER_IRQn);
}
```

=== 信息结束 ===
```

### SystemClock_Config

```text
=== SystemClock_Config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Src/main.c
- 行号：193
- 函数内容：static void SystemClock_Config(void)
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct;
  RCC_OscInitTypeDef RCC_OscInitStruct;

  /* Enable Power Control clock */
  __HAL_RCC_PWR_CLK_ENABLE();

  /* The voltage scaling allows optimizing the power consumption when the device is 
     clocked below the maximum system frequency, to update the voltage scaling value 
     regarding system frequency refer to product datasheet.  */
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /* Enable HSE Oscillator and activate PLL with HSE as source */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  HAL_RCC_OscConfig(&RCC_OscInitStruct);
  
  /* Select PLL as system clock source and configure the HCLK, PCLK1 and PCLK2 
     clocks dividers */
  RCC_ClkInitStruct.ClockType = (RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2);
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;  
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;  
  HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_5);

  /* STM32F405x/407x/415x/417x Revision Z and upper devices: prefetch is supported  */
  if (HAL_GetREVID() >= 0x1001)
  {
    /* Enable the Flash prefetch */
    __HAL_FLASH_PREFETCH_BUFFER_ENABLE();
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures system clock, PLL, and bus dividers for STM32F4 microcontroller
- 是否需要替换：是
- 分类/替换原因：This function performs system clock initialization including enabling power control clock, configuring voltage scaling, setting up HSE oscillator and PLL, and configuring clock dividers. GetMMIOFunctionInfo revealed multiple MMIO operations including register accesses for clock configuration. The function is called from main() during system initialization and contains hardware-specific operations that need to be removed while preserving the logical initialization flow. It doesn't involve NVIC/OS/VTOR operations (not CORE), data transmission/reception (not RECV), interrupt handling (not IRQ), or polling loops (not LOOP).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void SystemClock_Config(void)
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct;
  RCC_OscInitTypeDef RCC_OscInitStruct;

  /* Skip hardware-specific clock configuration in emulation */
  /* Original: Enable Power Control clock */
  /* __HAL_RCC_PWR_CLK_ENABLE(); */

  /* Original: Configure voltage scaling */
  /* __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1); */

  /* Initialize structure members for documentation */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  /* Skip hardware oscillator configuration */
  /* HAL_RCC_OscConfig(&RCC_OscInitStruct); */
  
  /* Initialize clock configuration structure */
  RCC_ClkInitStruct.ClockType = (RCC_CLOCKTYPE_SYSCLK | RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2);
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;  
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;  
  /* Skip hardware clock configuration */
  /* HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_5); */

  /* STM32F405x/407x/415x/417x Revision Z and upper devices: prefetch is supported  */
  if (HAL_GetREVID() >= 0x1001)
  {
    /* Skip flash prefetch buffer enable in emulation */
    /* __HAL_FLASH_PREFETCH_BUFFER_ENABLE(); */
  }
}
```

=== 信息结束 ===
```

### UART_DMAReceiveCplt

```text
=== UART_DMAReceiveCplt 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：3042
- 函数内容：static void UART_DMAReceiveCplt(DMA_HandleTypeDef *hdma)
{
  UART_HandleTypeDef *huart = (UART_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent;

  /* DMA Normal mode*/
  if ((hdma->Instance->CR & DMA_SxCR_CIRC) == 0U)
  {
    huart->RxXferCount = 0U;

    /* Disable RXNE, PE and ERR (Frame error, noise error, overrun error) interrupts */
    ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_PEIE);
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_EIE);

    /* Disable the DMA transfer for the receiver request by setting the DMAR bit
       in the UART CR3 register */
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAR);

    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    /* If Reception till IDLE event has been selected, Disable IDLE Interrupt */
    if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
    {
      ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);
    }
  }

  /* Initialize type of RxEvent that correspond to RxEvent callback execution;
   In this case, Rx Event type is Transfer Complete */
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  /* Check current reception Mode :
     If Reception till IDLE event has been selected : use Rx Event callback */
  if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
  {
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
    /* In other cases : use Rx Complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Rx complete callback*/
    huart->RxCpltCallback(huart);
#else
    /*Call legacy weak Rx complete callback*/
    HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：DMA UART receive process complete callback function that handles DMA transfer completion for UART reception, updates UART state, and calls appropriate completion callbacks.
- 是否需要替换：是
- 分类/替换原因：Classified as IRQ because: 1) It's a callback function triggered by DMA interrupt completion (called from HAL_DMA_IRQHandler), 2) It contains interrupt-related operations (disabling UART interrupts via ATOMIC_CLEAR_BIT), 3) GetMMIOFunctionInfo revealed 4 MMIO operations accessing UART control registers, 4) It performs state updates and callback execution typical of interrupt service routines, 5) It's not CORE (no NVIC/OS/VTOR operations), not RECV (no data reception), not INIT (not initialization), not LOOP (no peripheral-dependent loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  DMA UART receive process complete callback.
* @param  hdma  Pointer to a DMA_HandleTypeDef structure that contains
*               the configuration information for the specified DMA module.
* @retval None
*/
static void UART_DMAReceiveCplt(DMA_HandleTypeDef *hdma)
{
  UART_HandleTypeDef *huart = (UART_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent;

  /* DMA Normal mode*/
  if ((hdma->Instance->CR & DMA_SxCR_CIRC) == 0U)
  {
    huart->RxXferCount = 0U;

    /* [IRQ REMOVED] Disable RXNE, PE and ERR (Frame error, noise error, overrun error) interrupts */
    /* [IRQ REMOVED] ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_PEIE); */
    /* [IRQ REMOVED] ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_EIE); */

    /* [IRQ REMOVED] Disable the DMA transfer for the receiver request by setting the DMAR bit
       in the UART CR3 register */
    /* [IRQ REMOVED] ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAR); */

    /* At end of Rx process, restore huart->RxState to Ready */
    huart->RxState = HAL_UART_STATE_READY;

    /* If Reception till IDLE event has been selected, Disable IDLE Interrupt */
    if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
    {
      /* [IRQ REMOVED] ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE); */
    }
  }

  /* Initialize type of RxEvent that correspond to RxEvent callback execution;
   In this case, Rx Event type is Transfer Complete */
  huart->RxEventType = HAL_UART_RXEVENT_TC;

  /* Check current reception Mode :
     If Reception till IDLE event has been selected : use Rx Event callback */
  if (huart->ReceptionType == HAL_UART_RECEPTION_TOIDLE)
  {
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
    /* In other cases : use Rx Complete callback */
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Rx complete callback*/
    huart->RxCpltCallback(huart);
#else
    /*Call legacy weak Rx complete callback*/
    HAL_UART_RxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
  }
}
```

=== 信息结束 ===
```

### UART_DMATransmitCplt

```text
=== UART_DMATransmitCplt 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：2988
- 函数内容：static void UART_DMATransmitCplt(DMA_HandleTypeDef *hdma)
{
  UART_HandleTypeDef *huart = (UART_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent;
  /* DMA Normal mode*/
  if ((hdma->Instance->CR & DMA_SxCR_CIRC) == 0U)
  {
    huart->TxXferCount = 0x00U;

    /* Disable the DMA transfer for transmit request by setting the DMAT bit
       in the UART CR3 register */
    ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAT);

    /* Enable the UART Transmit Complete Interrupt */
    ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_TCIE);

  }
  /* DMA Circular mode */
  else
  {
#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)
    /*Call registered Tx complete callback*/
    huart->TxCpltCallback(huart);
#else
    /*Call legacy weak Tx complete callback*/
    HAL_UART_TxCpltCallback(huart);
#endif /* USE_HAL_UART_REGISTER_CALLBACKS */
  }
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：DMA UART transmit process complete callback function that handles DMA transfer completion for UART transmission
- 是否需要替换：是
- 分类/替换原因：This function is classified as IRQ because: 1) It is called from the DMA interrupt handler (HAL_DMA_IRQHandler) via callback mechanism, 2) It contains interrupt-related operations (enables UART transmit complete interrupt USART_CR1_TCIE), 3) It handles DMA completion which is interrupt-driven, 4) GetMMIOFunctionInfo revealed two hardware register accesses (ATOMIC_CLEAR_BIT and ATOMIC_SET_BIT) that modify UART control registers, 5) The function updates driver state (TxXferCount) and calls application callbacks, making it part of the interrupt handling chain. Although not a direct IRQ handler, it operates in interrupt context and configures interrupt behavior.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**\n* @brief  DMA UART transmit process complete callback.\n* @param  hdma  Pointer to a DMA_HandleTypeDef structure that contains\n*               the configuration information for the specified DMA module.\n* @retval None\n*/\nstatic void UART_DMATransmitCplt(DMA_HandleTypeDef *hdma)\n{\n  UART_HandleTypeDef *huart = (UART_HandleTypeDef *)((DMA_HandleTypeDef *)hdma)->Parent;\n  /* DMA Normal mode*/\n  if ((hdma->Instance->CR & DMA_SxCR_CIRC) == 0U)\n  {\n    huart->TxXferCount = 0x00U;\n\n    /* Skip hardware register operations in simulation */\n    /* ATOMIC_CLEAR_BIT(huart->Instance->CR3, USART_CR3_DMAT); */\n    /* ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_TCIE); */\n\n  }\n  /* DMA Circular mode */\n  else\n  {\n#if (USE_HAL_UART_REGISTER_CALLBACKS == 1)\n    /*Call registered Tx complete callback*/\n    huart->TxCpltCallback(huart);\n#else\n    /*Call legacy weak Tx complete callback*/\n    HAL_UART_TxCpltCallback(huart);\n#endif /* USE_HAL_UART_REGISTER_CALLBACKS */\n  }\n}
```

=== 信息结束 ===
```

### UART_Receive_IT

```text
=== UART_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
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


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receives data from UART in interrupt mode, updates buffer pointers and transfer counts, manages UART state, and invokes completion callbacks
- 是否需要替换：是
- 分类/替换原因：Function performs critical data I/O operations (reading from UART data register via huart->Instance->DR), contains MMIO operations, manages buffer pointers (pRxBuffPtr) and transfer counters (RxXferCount), updates UART state machine (RxState, RxEventType), and calls completion callbacks. While it contains interrupt control operations (__HAL_UART_DISABLE_IT), its primary purpose is data reception in interrupt mode. It's called from HAL_UART_IRQHandler when data is available. Classified as RECV because it handles data reception flow with hardware dependencies that need replacement.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
* @brief  Receives an amount of data in non blocking mode
* @param  huart  Pointer to a UART_HandleTypeDef structure that contains
*                the configuration information for the specified UART module.
* @retval HAL status
*/
static HAL_StatusTypeDef UART_Receive_IT(UART_HandleTypeDef *huart)
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
      /* Simulate 16-bit data reception */
      HAL_BE_In(pdata16bits, 2);
      huart->pRxBuffPtr += 2U;
    }
    else
    {
      pdata8bits = (uint8_t *) huart->pRxBuffPtr;
      pdata16bits  = NULL;

      if ((huart->Init.WordLength == UART_WORDLENGTH_9B) || ((huart->Init.WordLength == UART_WORDLENGTH_8B) && (huart->Init.Parity == UART_PARITY_NONE)))
      {
        /* Simulate 8-bit data reception */
        HAL_BE_In(pdata8bits, 1);
      }
      else
      {
        /* Simulate 7-bit data reception */
        HAL_BE_In(pdata8bits, 1);
      }
      huart->pRxBuffPtr += 1U;
    }

    if (--huart->RxXferCount == 0U)
    {
      /* Disable the UART Data Register not empty Interrupt */
      /* Preserved for potential NVIC operations */
      __HAL_UART_DISABLE_IT(huart, UART_IT_RXNE);

      /* Disable the UART Parity Error Interrupt */
      /* Preserved for potential NVIC operations */
      __HAL_UART_DISABLE_IT(huart, UART_IT_PE);

      /* Disable the UART Error Interrupt: (Frame error, noise error, overrun error) */
      /* Preserved for potential NVIC operations */
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

        /* Disable IDLE interrupt - preserve atomic operation */
        ATOMIC_CLEAR_BIT(huart->Instance->CR1, USART_CR1_IDLEIE);

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
```

=== 信息结束 ===
```

### UART_Start_Receive_DMA

```text
=== UART_Start_Receive_DMA 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：3271
- 函数内容：HAL_StatusTypeDef UART_Start_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  uint32_t *tmp;

  huart->pRxBuffPtr = pData;
  huart->RxXferSize = Size;

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->RxState = HAL_UART_STATE_BUSY_RX;

  /* Set the UART DMA transfer complete callback */
  huart->hdmarx->XferCpltCallback = UART_DMAReceiveCplt;

  /* Set the UART DMA Half transfer complete callback */
  huart->hdmarx->XferHalfCpltCallback = UART_DMARxHalfCplt;

  /* Set the DMA error callback */
  huart->hdmarx->XferErrorCallback = UART_DMAError;

  /* Set the DMA abort callback */
  huart->hdmarx->XferAbortCallback = NULL;

  /* Enable the DMA stream */
  tmp = (uint32_t *)&pData;
  HAL_DMA_Start_IT(huart->hdmarx, (uint32_t)&huart->Instance->DR, *(uint32_t *)tmp, Size);

  /* Clear the Overrun flag just before enabling the DMA Rx request: can be mandatory for the second transfer */
  __HAL_UART_CLEAR_OREFLAG(huart);

  if (huart->Init.Parity != UART_PARITY_NONE)
  {
    /* Enable the UART Parity Error Interrupt */
    ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_PEIE);
  }

  /* Enable the UART Error Interrupt: (Frame error, noise error, overrun error) */
  ATOMIC_SET_BIT(huart->Instance->CR3, USART_CR3_EIE);

  /* Enable the DMA transfer for the receiver request by setting the DMAR bit
  in the UART CR3 register */
  ATOMIC_SET_BIT(huart->Instance->CR3, USART_CR3_DMAR);

  return HAL_OK;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Starts UART receive operation in DMA mode by configuring DMA callbacks, starting DMA transfer, and enabling necessary UART interrupts
- 是否需要替换：是
- 分类/替换原因：This function initializes and starts a DMA receive operation for UART. It configures DMA callbacks, sets up buffer pointers and state variables, and enables hardware interrupts for DMA reception. While it's related to data reception, it doesn't perform actual data I/O - it sets up the hardware to perform the reception. The function contains multiple hardware register accesses (CR1, CR3, DR registers) and DMA hardware operations that need to be removed while preserving the state initialization and callback setup. GetMMIOFunctionInfo revealed register accesses to huart->Instance->DR, CR1, and CR3. GetFunctionCallStack shows it's called by HAL_UART_Receive_DMA and HAL_UARTEx_ReceiveToIdle_DMA. This fits the INIT classification as it initializes peripheral configuration for DMA reception. The replacement code preserves all non-hardware operations including state setting, callback configuration, and returns HAL_OK to maintain the expected behavior.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
HAL_StatusTypeDef UART_Start_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  huart->pRxBuffPtr = pData;
  huart->RxXferSize = Size;

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->RxState = HAL_UART_STATE_BUSY_RX;

  /* Set the UART DMA transfer complete callback */
  huart->hdmarx->XferCpltCallback = UART_DMAReceiveCplt;

  /* Set the UART DMA Half transfer complete callback */
  huart->hdmarx->XferHalfCpltCallback = UART_DMARxHalfCplt;

  /* Set the DMA error callback */
  huart->hdmarx->XferErrorCallback = UART_DMAError;

  /* Set the DMA abort callback */
  huart->hdmarx->XferAbortCallback = NULL;

  /* Skip DMA hardware start and register operations in simulation */
  /* Original: HAL_DMA_Start_IT(huart->hdmarx, (uint32_t)&huart->Instance->DR, *(uint32_t *)tmp, Size); */
  /* Original: __HAL_UART_CLEAR_OREFLAG(huart); */
  /* Original: ATOMIC_SET_BIT(huart->Instance->CR1, USART_CR1_PEIE); */
  /* Original: ATOMIC_SET_BIT(huart->Instance->CR3, USART_CR3_EIE); */
  /* Original: ATOMIC_SET_BIT(huart->Instance->CR3, USART_CR3_DMAR); */

  return HAL_OK;
}
```

=== 信息结束 ===
```

### UART_Start_Receive_IT

```text
=== UART_Start_Receive_IT 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
- 行号：3236
- 函数内容：HAL_StatusTypeDef UART_Start_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  huart->pRxBuffPtr = pData;
  huart->RxXferSize = Size;
  huart->RxXferCount = Size;

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->RxState = HAL_UART_STATE_BUSY_RX;

  if (huart->Init.Parity != UART_PARITY_NONE)
  {
    /* Enable the UART Parity Error Interrupt */
    __HAL_UART_ENABLE_IT(huart, UART_IT_PE);
  }

  /* Enable the UART Error Interrupt: (Frame error, noise error, overrun error) */
  __HAL_UART_ENABLE_IT(huart, UART_IT_ERR);

  /* Enable the UART Data Register not empty Interrupt */
  __HAL_UART_ENABLE_IT(huart, UART_IT_RXNE);

  return HAL_OK;
}


【替换更新】
- 更新代码：HAL_StatusTypeDef UART_Start_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  huart->pRxBuffPtr = pData;
  huart->RxXferSize = Size;
  huart->RxXferCount = Size;

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->RxState = HAL_UART_STATE_BUSY_RX;

  /* In emulation mode, skip hardware interrupt enable operations */
  /* The original code enables UART interrupts (PE, ERR, RXNE) */
  /* We preserve the state setting but skip hardware operations */
  
  return HAL_OK;
}
- 更新原因：Fix UART_Start_Receive_IT by skipping hardware interrupt enable operations. The original function enables UART interrupts (PE, ERR, RXNE) by writing to hardware registers. In emulation, these hardware writes can cause issues. The replacement preserves the buffer setup and state management but skips the hardware interrupt enable operations.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：HAL_StatusTypeDef UART_Start_Receive_IT(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
{
  huart->pRxBuffPtr = pData;
  huart->RxXferSize = Size;
  huart->RxXferCount = Size;

  huart->ErrorCode = HAL_UART_ERROR_NONE;
  huart->RxState = HAL_UART_STATE_BUSY_RX;

  /* In emulation mode, skip hardware interrupt enable operations */
  /* The original code enables UART interrupts (PE, ERR, RXNE) */
  /* We preserve the state setting but skip hardware operations */
  
  return HAL_OK;
}
    原因：Fix UART_Start_Receive_IT by skipping hardware interrupt enable operations. The original function enables UART interrupts (PE, ERR, RXNE) by writing to hardware registers. In emulation, these hardware writes can cause issues. The replacement preserves the buffer setup and state management but skips the hardware interrupt enable operations.
    时间：

=== 信息结束 ===
```

### UART_WaitOnFlagUntilTimeout

```text
=== UART_WaitOnFlagUntilTimeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/posixGen_Demos/UART_Hyperterminal_IT/Drivers/STM32F4xx_HAL_Driver/Src/stm32f4xx_hal_uart.c
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


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for a UART hardware flag to reach specified status with timeout handling, used by UART transmit/receive functions
- 是否需要替换：是
- 分类/替换原因：The function contains a while loop that polls hardware flags (__HAL_UART_GET_FLAG) and waits for them to change state. This matches the LOOP classification criteria: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags).' GetMMIOFunctionInfo revealed register accesses through flag checking macros. The function is called by HAL_UART_Receive and HAL_UART_Transmit for polling operations. It also contains error handling for overrun conditions which must be preserved while removing the hardware-dependent polling loop.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static HAL_StatusTypeDef UART_WaitOnFlagUntilTimeout(UART_HandleTypeDef *huart, uint32_t Flag, FlagStatus Status,
                                                     uint32_t Tickstart, uint32_t Timeout)
{
  /* [LOOP REMOVED] Skip hardware flag polling loop - assume flag condition is met */
  
  /* Check for the Timeout */
  if (Timeout != HAL_MAX_DELAY)
  {
    if (((HAL_GetTick() - Tickstart) > Timeout) || (Timeout == 0U))
    {
      return HAL_TIMEOUT;
    }

    /* Preserve overrun error handling logic */
    if ((READ_BIT(huart->Instance->CR1, USART_CR1_RE) != 0U) && (Flag != UART_FLAG_TXE) && (Flag != UART_FLAG_TC))
    {
      /* Simulate overrun error check - assume no overrun in simulation */
      /* [HARDWARE REMOVED] Skip hardware flag check: __HAL_UART_GET_FLAG(huart, UART_FLAG_ORE) */
      
      /* Preserve error handling state updates */
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
  
  return HAL_OK;
}
```

=== 信息结束 ===
```
