# 驱动函数替换策略设计

日期：2026-03-18

## 适用范围

- 覆盖 LwIP/ENET（尤其 `NXP_LwIP_BareMetal` 的 ENET DMA + RingBuffer 接收路径）
- 覆盖一般 UART/IRQ/INIT 等驱动函数的替换策略（以 `FunctionClassifier` / `code_generation_rules` 为准）
- 适用在本项目的"驱动函数替换"流程中：由 `FunctionClassifier` 给出分类，再依据分类生成/不生成 replacement 代码，并由 rubric 强制保持仿真所需语义不变量

## 证据来源范围

- 主线代码/提示证据：`prompts/function_classifier.py`、`prompts/replacement_rubric_checker.py`、`prompts/code_generation_rules.md`
- 现有分析文档证据：`doc/lwip_eth_irq_analysis.md`、`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`
- 替换日志证据：`testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md`

---

## 1. 分类（当前实现：FunctionClassifier）

### 1.1 分类集合与优先级顺序

`function_type` 允许集合：`CORE / RECV / IRQ / INIT / LOOP / RETURNOK / SKIP / NODRIVER`  
（来源：`prompts/function_classifier.py` 第 255 行附近）

分类优先级顺序：`CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER`  
（来源：`prompts/function_classifier.py` 第 68 行）

### 1.2 "会生成替换代码"的类型范围

- `CORE`：`has_replacement: false`
- `RECV / IRQ / INIT / LOOP`：`has_replacement: true`
- `RETURNOK / SKIP / NODRIVER`：只分类，不生成 replacement

（来源：`prompts/function_classifier.py` 第 17–20 行、第 243–245 行）

---

## 2. Steering（执行流导向）策略

### 2.1 Steering 的目的与 SKIP 的区别

**Steering 的目的**：通过 **control-flow 旁路/短路**，把执行流导向仿真环境下可正确到达的分支。在无真实硬件时，原始代码中依赖硬件状态（寄存器、BD 标志、中断标志等）的条件分支往往永远不成立，导致永远进不到"有数据/有帧/初始化完成"的分支，或陷入"等待硬件标志"的死循环。Steering 通过**替换前 → 替换后**的代码改写，**旁路或短路**这些硬件依赖分支，使执行流能到达原本"正确路径"上的逻辑。

**Steering 与 SKIP 不是一回事**：

- **SKIP**：FunctionClassifier 的**分类名**，表示"非关键可忽略操作"，对应 `has_replacement: false`，**不生成替换代码**。
- **Steering**：是 **RECV / IRQ / INIT / LOOP** 四类替换策略的**共同执行手段**——在生成 replacement 时，通过控制流改写实现"导向正确分支"，而不是简单"跳过函数"。

（来源：`prompts/function_classifier.py` 第 206–209 行 SKIP 定义；第 79–201 行 RECV/IRQ/INIT/LOOP 策略）

### 2.2 四类 Steering 子策略：INIT / IRQ / RECV / LOOP

去掉用户表中的 Strip 后，本项目实际落地的四类 Steering 策略为：

| 策略 | 含义 | 修复的问题类型 |
|------|------|----------------|
| **INIT** | 去掉 MMIO/寄存器写，保留结构初始化与必要 state | 初始化路径依赖硬件配置完成，仿真中"配置完成"分支永远不成立 |
| **IRQ** | 移除硬件操作，保留 OS 通知与状态迁移 | IRQ 内依赖读硬件中断标志才能走到数据处理/任务唤醒分支 |
| **RECV** | 跳过硬件 Flag 扫描，用 HAL_BE 注入数据 | 收包路径依赖 EMPTY/LAST 等 BD 标志，仿真中永远"无帧"或死循环 |
| **LOOP** | 跳过等待硬件标志的循环，或改为单次仿真读 | 轮询等待 status flag 或 FIFO until empty 导致死循环 |

---

### 2.3 INIT Steering

**含义**：原始 INIT 函数依赖"硬件配置完成"后的状态；仿真中若保留 MMIO 写，要么不可用要么无意义。Steering 通过**去掉寄存器写**、**保留结构初始化与默认值**，使替换后的逻辑后置状态与"硬件 init 完成"一致。

**替换前（原始关键逻辑）**——来源：`prompts/function_classifier.py` 第 157–168 行

```c
HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
    __HAL_RCC_USART1_CLK_ENABLE();
    huart->Instance->CR1 = USART_CR1_UE | USART_CR1_TE | USART_CR1_RE;
    huart->Instance->BRR = UART_BRR_SAMPLING16(HAL_RCC_GetPCLK2Freq(), huart->Init.BaudRate);
    huart->State = HAL_UART_STATE_READY;
    return HAL_OK;
}
```

**替换后（Steering 落地）**——来源：`prompts/function_classifier.py` 第 170–178 行

```c
HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
    huart->State = HAL_UART_STATE_READY;
    huart->ErrorCode = HAL_UART_ERROR_NONE;
    return HAL_OK;
}
```

**Steering 实现方式**：删除所有 MMIO 写，直接执行"逻辑后置状态"的赋值，使调用者认为初始化已完成。

---

### 2.4 IRQ Steering

**含义**：IRQ 处理函数通常先读硬件中断标志，再决定是否进入数据处理/任务唤醒分支。仿真中这些寄存器不会被硬件置位，导致永远进不到"有数据"的分支。Steering 通过**移除硬件读/写**、**保留 OS 通知**，并**模拟"条件已满足"**（如用 `HAL_BE_In` 注入数据），使执行流能到达原本的数据处理或任务触发路径。

**替换前（原始关键逻辑）**——来源：`prompts/function_classifier.py` 第 124–133 行

```c
void UART0_IRQHandler(void)
{
    if ((UART0->S1 & UART_S1_RDRF_MASK) != 0U) {
        data = UART0->D;
        process_data(data);
        xSemaphoreGiveFromISR(semaphore, &xHigherPriorityTaskWoken);
    }
    UART0->S1 |= UART_S1_TDRE_MASK;
}
```

**替换后（Steering 落地）**——来源：`prompts/function_classifier.py` 第 136–143 行

```c
void UART0_IRQHandler(void)
{
    data = HAL_BE_In(&data, 1);
    process_data(data);
    xSemaphoreGiveFromISR(semaphore, &xHigherPriorityTaskWoken);
}
```

**Steering 实现方式**：旁路 `if ((UART0->S1 & UART_S1_RDRF_MASK) != 0U)`，用 `HAL_BE_In` 直接注入数据并执行 `process_data` 与 `xSemaphoreGiveFromISR`。

---

### 2.5 RECV Steering（含 ENET DMA + RingBuffer 单包模式）

**含义**：收包函数依赖硬件在 BD 上写入 EMPTY/LAST 等标志来"找帧"；仿真中这些标志不会被置位，导致要么永远返回"无帧"，要么在 `while/do-while` 中死循环。Steering 通过**跳过硬件 Flag 判定**、**短路环扫描**，在"已有有效 BD/buffer"的插入点调用 `HAL_BE_ENET_ReadFrame` 注入数据，并保证**单次处理 + 状态前进**后立即返回。

**替换前（原始关键逻辑）**——来源：`testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md` 第 1953–2027 行

```c
index = rxBdRing->rxGenIdx;
while (0U == (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK))
{
    if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
    {
        result = ENET_GetRxFrameErr((enet_rx_bd_struct_t *)(uintptr_t)curBuffDescrip, &rxFrame->rxFrameError);
        break;
    }
    index = ENET_IncreaseIndex(index, rxBdRing->rxRingLen);
    curBuffDescrip = rxBdRing->rxBdBase + index;
    if (index == rxBdRing->rxGenIdx) { break; }
}

curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
index = 0;
do
{
    newBuff = (uintptr_t)(uint8_t *)handle->rxBuffAlloc(base, handle->userData, ringId);
    if (newBuff != 0U)
    {
        rxBuffer = &rxFrame->rxBuffArray[index];
        rxBuffer->buffer = (void *)(uint8_t *)address;
        if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
        {
            isLastBuff = true;
            rxFrame->totLen = curBuffDescrip->length;
            rxBuffer->length = curBuffDescrip->length - buffLen;
            /* HAL_BE_ENET_ReadFrame 插入点 */
        }
    }
} while (!isLastBuff);
```

**替换后（Steering 落地）**——来源：`testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md` 第 2184–2198 行、第 2282–2297 行

```c
if (1)
{
    if (1)
    {
        result = ENET_GetRxFrameErr((enet_rx_bd_struct_t *)(uintptr_t)curBuffDescrip, &rxFrame->rxFrameError);
        result = kStatus_Success;
    }
}

if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
{
    isLastBuff = true;
    rxFrame->totLen = curBuffDescrip->length;
    rxBuffer->length = curBuffDescrip->length - buffLen;
    if (rxBuffer->buffer != NULL && rxBuffer->length > 0)
    {
        HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length);
    }
}
else
{
    rxBuffer->length = curBuffDescrip->length;
    buffLen += rxBuffer->length;
    if (rxBuffer->buffer != NULL && rxBuffer->length > 0)
    {
        HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length);
    }
}
```

**Steering 实现方式**：(1) 旁路 `while (0U == (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK))`，用 `if (1)` 强制进入"有帧"路径；(2) 旁路 LAST 判定，设 `result = kStatus_Success`；(3) 在取得 `rxBuffer->buffer`、`rxBuffer->length` 后调用 `HAL_BE_ENET_ReadFrame`；(4) 按 `code_generation_rules.md` 单包模式，理想情况下应进一步删除以 `isLastBuff` 为条件的 `do-while`（见 `doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md` 第 3–4 节）。

---

### 2.6 LOOP Steering

**含义**：轮询等待硬件 status flag 或 FIFO until empty 的循环，在仿真中条件永远不满足，导致死循环。Steering 通过**跳过整个循环**或**改为单次仿真读**，使执行流不再卡在等待硬件的位置。

**替换前（原始关键逻辑）**——来源：`prompts/function_classifier.py` 第 187–198 行

```c
while (0U == (base->S1 & UART_S1_TC_MASK)) { }

while ((base->S1 & UART_S1_RDRF_MASK) != 0U)
{
    (void)base->D;
}
```

**替换后（Steering 落地）**——来源：`prompts/function_classifier.py` 第 190–198 行

```c
/* [LOOP REMOVED] Waited for hardware transmission complete flag */

(void)HAL_BE_In(NULL, 1); /* Simulate reading to clear overrun flag */
```

**Steering 实现方式**：等待 status flag 的循环直接删除；FIFO until empty 的循环改为单次 `HAL_BE_In` 调用。

---

## 3. 对齐检查：用户表到当前实现分类/策略的"修正后映射"

- INIT（用户）→ INIT（当前分类）
- SEND（用户）→ RECV（当前分类）的"数据 transmission"分支
- RECV（用户）→ RECV（当前分类）的"数据 reception"分支
- IRQ（用户）→ IRQ（当前分类）
- CTRL（用户）→ RETURNOK / SKIP
- POLL（用户）→ LOOP（当前分类）
- DMA（用户）→ RECV 或 INIT

（详细证据见 `prompts/function_classifier.py` 各类型 strategy 段落）

---

## 4. 各类型对应的替换策略与 HAL_BE Helper 表

### 4.1 CORE

不生成 replacement（来源：`prompts/function_classifier.py` 第 74–76 行）

### 4.2 RECV / IRQ / INIT / LOOP

见第 2 节 Steering 子策略

### 4.3 HAL_BE Helper 表

来源：`prompts/function_classifier.py` 第 223–231 行

```c
int HAL_BE_return_0();
int HAL_BE_return_1();
int HAL_BE_Out(int len);
int HAL_BE_In(void* buf, int len);
int HAL_BE_ENET_ReadFrame(void* buf, int length);
int HAL_BE_Block_Write(void* buf, int block_size, int block_num);
int HAL_BE_Block_Read(void* buf, int block_size, int block_num);
```

### 4.4 RETURNOK / SKIP / NODRIVER

只分类，不生成 replacement。**SKIP** 与 **Steering 策略 LOOP** 不同：前者是 FunctionClassifier 类型，后者是四类 Steering 之一。

---

## 5. 实现语义保持不变量（Invariants）

- CORE/NVIC/SysTick/VTOR：必须保留可观察寄存器写（`prompts/replacement_rubric_checker.py`）
- INIT：去掉寄存器写，保留结构初始化与必要 state
- IRQ：移除硬件操作，保留 OS 通知与状态机更新
- RECV：通过 `HAL_BE_In` / `HAL_BE_ENET_ReadFrame` 注入数据，保留 buffer 管理
- LOOP：避免等待硬件标志的死循环

---

## 6. 具体例子（ETH / ENET / UART）

### 6.1 ETH（LwIP）

- 现象：收包 IRQ 不触发。
- 根因：`HAL_ETH_Init` 未调用 `HAL_ETH_MspInit`，或 `HAL_NVIC_EnableIRQ` 被替换为不写 NVIC 的桩。
- 证据：`doc/lwip_eth_irq_analysis.md`

### 6.2 NXP ENET

- 现象：`ENET_GetRxFrame` 内反复调用 `ENET_IncreaseIndex`，`ethernetif_linkinput` 阻塞。
- 根因：依赖 EMPTY/LAST 等硬件 Flag 的 while/do-while 在仿真中永不退出。
- 单包模式硬约束：`prompts/code_generation_rules.md` 第 49–55 行；`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`

### 6.3 UART

- `HAL_UART_Init`：见第 2.3 节 INIT Steering。
- `HAL_UART_Receive`：见 `prompts/function_classifier.py` 第 88–112 行 RECV 示例。

---

## 7. 证据索引（Evidence Index）

| 文件 | 引用内容 |
|------|----------|
| `prompts/function_classifier.py` | 分类优先级、各类型 strategy、Original/Replacement 示例、HAL_BE Helper 表、SKIP 定义 |
| `prompts/replacement_rubric_checker.py` | CORE/NVIC/SysTick/VTOR 必须保留规则 |
| `prompts/code_generation_rules.md` | RECV + DMA+RingBuffer 单包模式硬约束 |
| `testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md` | ENET_GetRxFrame 原始代码与推荐替换代码 |
| `doc/lwip_eth_irq_analysis.md` | ETH 初始化/IRQ 失效分析 |
| `doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md` | ENET 卡死根因、单包模式目标行为 |
