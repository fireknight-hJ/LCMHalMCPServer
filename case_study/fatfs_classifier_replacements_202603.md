# Case Study: FATFS 用例中 FunctionClassifier 替换严重错误的两例

**场景**：RT-Thread stm32f401-st-nucleo fatfs demo，清空 ai_log 后首次跑；替换代码全部来自 FunctionClassifier，未经过 ReplacementUpdate。  
**结果**：首次构建失败，Builder 修编卡在两类错误上。本文对导致失败的两个函数做替换前后对比与根因分析。

---

## 1. SystemClock_Config（board.c）

### 1.1 原始代码（board.c + board.h）

**board.h 声明（不可改）：**
```c
void SystemClock_Config(void);   // 非 static，在头文件中声明
```

**board.c 实现：**
```c
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2);

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
```

### 1.2 Classifier 生成的替换代码（错误版本）

```c
static void SystemClock_Config(void)   // 错误 1：多了 static
{
  RCC_ClkInitTypeDef RCC_ClkInitStruct;
  RCC_OscInitTypeDef RCC_OscInitStruct;
  HAL_StatusTypeDef ret = HAL_OK;

  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 400;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 9;
  RCC_OscInitStruct.PLL.PLLR = 7;   // 错误 2：STM32F401 的 RCC_PLLInitTypeDef 无 PLLR 成员

  RCC_ClkInitStruct.ClockType = (RCC_CLOCKTYPE_SYSCLK | ...);
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;

  if(ret != HAL_OK) { Error_Handler(); }
}
```

### 1.3 编译报错

- `static declaration of 'SystemClock_Config' follows non-static declaration`  
  → board.h 里是 `void SystemClock_Config(void);`，实现不能加 `static`。
- `'RCC_PLLInitTypeDef' has no member named 'PLLR'`  
  → 在 STM32F401 的 HAL 里，`RCC_PLLInitTypeDef` 只有 PLLM/PLLN/PLLP/PLLQ；PLLR 仅在 F410/F446/F469/F479/F412 等子系列中存在（见 `stm32f4xx_hal_rcc.h` 中 `#if defined(STM32F446xx) || ...` 分支）。

### 1.4 根因简述

- **签名**：模型按“内部实现”习惯加了 `static`，没有对照头文件声明，导致与 board.h 的**非 static** 声明冲突。
- **HAL 成员**：模型使用了“通用 F4”或 F446 等子系列的 PLL 模板（HSE + PLLR），没有按**当前芯片 F401** 的 HAL 裁剪，用了 F401 不存在的 `PLLR`。

---

## 2. HAL_RCCEx_PeriphCLKConfig（stm32f4xx_hal_rcc_ex.c）

### 2.1 目标芯片（STM32F401）下的定义

在 `stm32f4xx_hal_rcc_ex.h` 中，**STM32F401xC / STM32F401xE** 使用的 `RCC_PeriphCLKInitTypeDef` 为：

```c
typedef struct
{
  uint32_t PeriphClockSelection;
  RCC_PLLI2SInitTypeDef PLLI2S;
  uint32_t RTCClockSelection;
  uint8_t TIMPresSelection;
} RCC_PeriphCLKInitTypeDef;
```

即：只有 **PeriphClockSelection、PLLI2S、RTCClockSelection、TIMPresSelection**。  
F401 没有 SAI、没有 I2S 的独立时钟选择成员、没有 SPDIFRX、没有 I2C1~I2C4、没有 USART1 等外设时钟配置字段。

### 2.2 Classifier 生成的替换代码（片段，错误版本）

模型生成的是**一整套“通用 F4 / F446 风格”**的 `HAL_RCCEx_PeriphCLKConfig`，例如：

```c
  /* I2S */
  if(((PeriphClkInit->PeriphClockSelection) & RCC_PERIPHCLK_I2S) == (RCC_PERIPHCLK_I2S))
  {
    assert_param(IS_RCC_I2SCLKSOURCE(PeriphClkInit->I2sClockSelection));  // F401 无此成员
    if(PeriphClkInit->I2sClockSelection == RCC_I2SCLKSOURCE_PLLI2S) ...
  }
  /* SAI1 */
  if(... & RCC_PERIPHCLK_SAI1) ...   // F401 无 RCC_PERIPHCLK_SAI1
    PeriphClkInit->Sai1ClockSelection ...
  /* SAI2 */
  if(... & RCC_PERIPHCLK_SAI2) ...
  /* SPDIF-RX */
  if(... & RCC_PERIPHCLK_SPDIFRX) ...
  /* I2C1, I2C2, I2C3, I2C4 */
  if(... & RCC_PERIPHCLK_I2C1) ...
  /* USART1 */
  if(... & RCC_PERIPHCLK_USART1) ...
```

这些分支里用到的：

- 结构体成员：`I2sClockSelection`, `Sai1ClockSelection`, `Sai2ClockSelection` 等  
- 宏：`RCC_PERIPHCLK_SAI1`, `RCC_PERIPHCLK_SAI2`, `RCC_PERIPHCLK_SPDIFRX`, `RCC_PERIPHCLK_I2C1`～`I2C4`, `RCC_PERIPHCLK_USART1` 等  

在 **STM32F401 的 HAL 中均不存在**，对应的是 F446/其他子系列的 `RCC_PeriphCLKInitTypeDef` 和 RCCEx 宏定义。

### 2.3 编译报错（摘录）

- `'RCC_PeriphCLKInitTypeDef' has no member named 'I2sClockSelection'`（以及 Sai1ClockSelection, Sai2ClockSelection 等）
- `'RCC_PERIPHCLK_SAI1' undeclared`（以及 SAI2, SPDIFRX, I2C1~I2C4, USART1 等）

### 2.4 根因简述

- 模型没有区分**具体芯片/子系列**，把“另一子系列（如 F446）的 `HAL_RCCEx_PeriphCLKConfig` 实现”当成通用模板整段生成。
- 目标工程是 **STM32F401**，只应使用 F401 的 `RCC_PeriphCLKInitTypeDef` 和 RCCEx 宏；当前生成代码完全基于更大型号的 HAL，导致大量成员与宏在 F401 下不存在。

---

## 3. 为什么错得这么离谱？

### 3.1 共性原因

1. **没有“目标芯片/目标 HAL”约束**  
   Classifier 或底层训练数据里，没有明确“当前工程是 STM32F401”“只允许使用 F401 的 HAL 类型与宏”，导致生成的是“通用 F4”或“F446 风格”实现。

2. **没有“与现有声明一致”的硬性规则**  
   SystemClock_Config 在 board.h 中已声明为**非 static**，生成时仍按“本文件内部函数”加了 `static`，说明没有把“与头文件声明一致”作为必须满足的约束。

3. **单函数编译校验未强制生效**  
   流程上存在 VerifyReplacement（rubric + 单函数编译），但若模型未在结束前调用或未得到 pass=true，最终仍会采纳未验证的 `function_replacement` 并参与 replace_funcs。未验证代码一旦写进 mmio_info_list，就会直接导致本次构建失败。

### 3.2 两例各自的特点

| 函数 | 错误类型 | 本质 |
|------|----------|------|
| **SystemClock_Config** | 声明不一致 + 使用了本芯片 HAL 不存在的成员 | 签名未对齐头文件；PLL 配置照抄了带 PLLR 的子系列。 |
| **HAL_RCCEx_PeriphCLKConfig** | 整段逻辑属于另一子系列 | 把 F446 等“大而全”的 PeriphCLK 实现当成通用实现，未按 F401 的极小 RCCEx 集合裁剪。 |

### 3.3 改进方向（与现有措施对应）

- **Prompt / 规则**：在 FunctionClassifier 中明确“目标芯片为 STM32F401”“替换代码中仅允许使用本工程已包含头文件里存在的类型、成员与宏”；“函数签名（含是否 static）必须与声明一致”。
- **强制校验**：仅在存在“某次 VerifyReplacement 返回 pass=true”的 replace_code 时采纳替换，否则不写 `function_replacement`（已在 respond 中做“无验证则清空替换”的强制逻辑）。
- **单函数编译**：保持并依赖 VerifyReplacement 的单函数编译环节，确保只有能通过目标工程编译的替换才会被采纳。

---

## 4. 小结

- **SystemClock_Config**：多了 `static`、使用了 F401 不存在的 `PLLR`，导致声明冲突与类型错误。
- **HAL_RCCEx_PeriphCLKConfig**：整段替换基于 F446 等子系列的 RCCEx HAL，在 F401 下大量成员与宏未定义，错误面极大。

两例共同暴露的问题是：**生成时缺乏“目标芯片 + 当前头文件”的强约束，且未保证“单函数编译通过才采纳”**。后续通过“无 VerifyReplacement 通过则不写替换”的强制逻辑，可避免未验证的 Classifier 产出再次进入构建；长期仍需在 Prompt 与规则中明确芯片与 HAL 边界，减少此类跨子系列混用。
