# 驱动函数替换策略设计
日期：2026-03-18

## 适用范围
- 覆盖 LwIP/ENET（尤其 `NXP_LwIP_BareMetal` 的 ENET DMA + RingBuffer 接收路径）
- 覆盖一般 UART/IRQ/INIT 等驱动函数的替换策略（以 `FunctionClassifier` / `code_generation_rules` 为准）
- 适用在本项目的“驱动函数替换”流程中：由 `FunctionClassifier` 给出分类，再依据分类生成/不生成 replacement 代码，并由 rubric 强制保持仿真所需语义不变量

## 证据来源范围
- 主线代码/提示证据：
  - `prompts/function_classifier.py`
  - `prompts/replacement_rubric_checker.py`
  - `prompts/code_generation_rules.md`
- 现有分析文档证据：
  - `doc/lwip_eth_irq_analysis.md`
  - `doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`

---

## 1. 分类（当前实现：FunctionClassifier）

### 1.1 分类集合与优先级顺序
本项目当前实现中，`FunctionClassifier` 的 `function_type` 允许集合为：
`CORE / RECV / IRQ / INIT / LOOP / RETURNOK / SKIP / NODRIVER`  
（来源：`prompts/function_classifier.py` -> 输出格式 `function_type` 枚举位置：`function_type` 字段在 `CORE_RECV_IRQ_INIT_LOOP_RETURNOK_SKIP_NODRIVER` 中给出，见该文件输出模型相关区段）

分类优先级顺序（apply first match）为：
`CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER`  
（来源：`prompts/function_classifier.py`：分类优先级 `CORE > RECV > IRQ > INIT > LOOP ...` 段落）

### 1.2 “会生成替换代码”的类型范围
按当前 prompt 约定：
- `CORE`：只输出分类与推理，不生成 replacement（`has_replacement: false`）
- `RECV / IRQ / INIT / LOOP`：会生成 replacement code（`has_replacement: true`）
- `RETURNOK / SKIP / NODRIVER`：只输出分类与推理，不生成 replacement（除非后续工具显式再触发）

（来源：`prompts/function_classifier.py`：`CORE` / `RECV, IRQ, INIT, LOOP` / `RETURNOK, SKIP, NODRIVER` 对应的“生成输出规则”与 `has_replacement` 说明）

---

## 2. 对齐检查：用户表（INIT/SEND/RECV/IRQ/CTRL/POLL/DMA）到当前实现分类/策略的“修正后映射”

你给定的用户表（可能与代码不完全一致）：
- INIT：Skip
- SEND：Strip/Redirect
- RECV：Redirect
- IRQ：Event
- CTRL：Skip
- POLL：Redirect
- DMA：Redirect

为避免歧义，下面给出“修正前（用户语义）→ 修正后（FunctionClassifier 实际分类与 strategy 落点）”的对照表：

| 函数类别（用户语义） | 修正后落点（FunctionClassifier 类型） | 推荐策略（对齐实现） | 关键说明 |
|---|---|---|---|
| INIT | `INIT` | 去掉 MMIO/寄存器写，但保留结构初始化、默认值与必要 state；必要时保留 `*_MspInit` / CORE 调用或寄存器写 | INIT 不是空替换 |
| SEND（发送/写） | `RECV` 的 transmission 分支 | 可重定向到 `stdout`，或在不影响状态时跳过写操作；保留非 I/O 逻辑 | SEND 不单独作为 `function_type` |
| RECV（接收/读） | `RECV` 的 reception 分支 | 用 `HAL_BE_In`（定长）/ `HAL_BE_ENET_ReadFrame`（变长）注入数据；保留 buffer 管理与状态迁移 | 依赖接收协议/长度语义 |
| IRQ（中断） | `IRQ` | 移除真实硬件 IRQ 操作（寄存器写），保留 OS 通知/条件分支/状态迁移，确保执行流可达数据处理或任务触发路径 | IRQ 的“Event”体现在 OS 通知/回调触发分支 |
| CTRL | `RETURNOK` / `SKIP` | 进入 “classification only” 或安全跳过（空实现），仅当确认不影响关键初始化/状态迁移 | CTRL 不单独作为 `function_type` |
| POLL（轮询等待） | `LOOP` | 等待硬件标志：跳过整个循环；FIFO 读直到 empty：改为单次读/单次仿真接收 | POLL 通常被 LOOP 接住 |
| DMA | 通常落到 `RECV`（若是收/传数据路径）或 `INIT`（若主要是 DMA 初始化/资源分配） | 对 DMA+RingBuffer（如 ENET）使用“单包模式”硬约束：禁止 while/do-while 环扫描，确保一次 `HAL_BE_ENET_ReadFrame` + 一次 Ring 前进后立即返回 | DMA 的特殊性主要在 RECV+RingBuffer 的结构约束 |

在当前实现里，`SEND / CTRL / POLL / DMA` 都不是 `FunctionClassifier` 的直接 `function_type`。它们需要**落到**以下实际分类：`RECV/IRQ/INIT/LOOP/RETURNOK/SKIP`。因此存在需要“修正”的部分，修正原因是：当前实现的策略由“函数语义识别标准”驱动（哪些属于 RECV/IRQ/INIT/LOOP、哪些属于 RETURNOK/SKIP），并且只有 `RECV/IRQ/INIT/LOOP` 生成替换代码。

### 2.1 修正后的映射（与当前实现策略对齐）

1. **INIT（用户）→ INIT（当前分类），但不是“空替换”**
   - 修正后含义：在 `INIT` 类里要“去掉硬件寄存器/MMIO访问”，但保留结构初始化、默认值设置与必要 state；replacement 仍应保证“逻辑上处于硬件 init 之后的期望状态”
   - 证据：`INIT` 策略要求 “Remove all MMIO/register access operations” + “Preserve resource allocation / structure initialization / default value setting … logical post-initialization state matches expected state”（来源：`prompts/function_classifier.py` 的 `INIT` strategy 段落）
   - 额外约束：若 INIT 函数属于/调用 `CORE`（NVIC/OS/VTOR），则 replacement **不能**删掉对应 `CORE` 调用或寄存器写（来源：`prompts/function_classifier.py` 的 `INIT` EXCEPTION 段落；以及 rubric 对 NVIC/SysTick/VTOR 的强制保留规则，见第 4 节）

2. **SEND（用户）→ RECV（当前分类）的“数据 transmission（写）分支”**
   - 修正后含义：用户表的 SEND=“Strip/Redirect”应落到 `RECV` 的 strategy：对 `TX/TRANSMIT` 这类“数据传输/写”可以将输出重定向到 `stdout`，或在不影响状态时跳过
   - 证据：`RECV` 策略明确区分 “For data reception … / For data transmission … Redirect output to stdout (e.g. using printf) or, if non-critical and does not affect state, skip”（来源：`prompts/function_classifier.py`：`RECV` strategy 中 data reception 与 data transmission 两段）

3. **RECV（用户）→ RECV（当前分类）的“数据 reception（读/收包）分支”**
   - 修正后含义：RECV=使用仿真注入函数：
     - 固定长度：`HAL_BE_In(void* buf, int len)`
     - 变长报文（如 ENET）：`HAL_BE_ENET_ReadFrame(void* buf, int length)`
   - 证据：`RECV` 策略中 “For data reception: Replace with calls to HAL_BE_In … or HAL_BE_ENET_ReadFrame …”（来源：`prompts/function_classifier.py` 的 `RECV` strategy 段落）

4. **IRQ（用户）→ IRQ（当前分类）：Event=保留 OS 通知/状态迁移**
   - 修正后含义：在 `IRQ` replacement 中移除真实硬件操作（尤其硬件中断控制寄存器写），但保留 IRQ 内的 OS 通知调用、条件分支与状态机更新，使执行流仍能触发到原本的“数据处理/任务唤醒”分支
   - 证据：`IRQ` 策略要求 “Remove actual hardware operations … Preserve: Interrupt flag checks, OS interrupt notifications, state machine updates … Ensure flow can reach original data handling or task triggering branches”（来源：`prompts/function_classifier.py`：`IRQ` strategy 段落）

5. **CTRL（用户）→ RETURNOK / SKIP（当前分类）：replacement 阶段等价“Skip”**
   - 修正后含义：当前实现没有独立 `CTRL` 类型；用户表的 CTRL=Skip，需要映射到两类“不会产出 replacement code”的分类：
     - `RETURNOK`：纯 driver operation（策略说明为“返回成功/安全默认”，但当前 classifier 阶段不生成 replacement）
     - `SKIP`：非关键可忽略操作（同样只分类不生成 replacement）
   - 证据：
     - `RETURNOK` / `SKIP` 属于 “Priority 2: Classification Only（Do Not Generate Code Now）”并明确 “only provide classification and reasoning … Do not generate replacement code”（来源：`prompts/function_classifier.py`：`RETURNOK` 与 `SKIP` 段落以及其“classification only”说明）
     - `SKIP` 的定义包含“minor configuration, debug output … can be safely ignored”（来源：`prompts/function_classifier.py`：`SKIP` Identification 段落）

6. **POLL（用户）→ LOOP（当前分类）：避免等待硬件标志死循环**
   - 修正后含义：用户表的 POLL=Redirect，需要落到 `LOOP`：当循环是“等待状态标志”时应直接跳过循环；当是 FIFO 直到 empty 的读取时改为单次读/单次仿真接收
   - 证据：`LOOP` strategy：
     - “If waiting for a status flag: Skip the loop entirely”
     - “If reading data from a FIFO until empty: Replace with a single read or a call to a simulation receive function”
     （来源：`prompts/function_classifier.py` 的 `LOOP` strategy 段落）

7. **DMA（用户）→ RECV（当前分类）或 INIT（当前分类），取决于 DMA 语义是否在“真正收/传数据”还是“DMA 初始化配置”**
   - 修正后含义（落地准则）：
     - 若函数属于“DMA buffer management / peripheral data transfer (read/write)”这类收/传数据路径，则归到 `RECV`，并走 `RECV` 的仿真注入策略（`HAL_BE_In` / `HAL_BE_ENET_ReadFrame`）
     - 若函数主要是在“初始化/配置/分配资源”DMA，则归到 `INIT`，走 INIT 去寄存器写但保留结构 state 的策略
   - 证据：
     - `RECV` 的 identification 明确包含 “DMA buffer management”（来源：`prompts/function_classifier.py`：`RECV` Identification 段落）
     - `INIT` 的 identification 明确包含 “initialize peripheral/configurations or allocate resources”（来源：`prompts/function_classifier.py`：`INIT` Identification 段落）

   - ENET DMA + RingBuffer 接收的额外修正（单包模式硬约束）：
     - 当 DMA+RingBuffer 的 RECV 函数被替换时，必须遵循“单次收一包”的强约束，禁止保留依赖 `LAST/EMPTY` 等硬件 flag 的多帧/环扫描 while/do-while 结构，并在“当前 BD 有效 buffer 指针且将视为本次帧缓存”的插入点调用 `HAL_BE_ENET_ReadFrame(buffer, length)`，完成一次 BD 更新后立即返回
     - 证据：`prompts/code_generation_rules.md` 对 “RECV with复杂 DMA+RingBuffer 控制流（网络收帧）” 的硬约束条款（来源：`prompts/code_generation_rules.md` 同名节选，见第 5 节引用）

### 2.2 `HAL_BE_*` 弱符号接口表：与 fuzzemu 仿真系统的对接

`HAL_BE_*` 这组函数是替换代码中的“硬件 I/O 汇聚点”：固件侧调用它们后，fuzzemu 不执行 C 中弱实现，而是根据 `semu_config.yml` 中的 `handlers` 映射，跳到对应的 Python handler（再从 `input.bin` / fuzzer 输入读数据、或简化为固定返回值以推动执行继续）。

该对接链路在仓库中可追溯到：
- 弱符号的默认实现（`utils/src_ops.py` 里 `__weak` + `noinline` 定义）
- `syms.yml`：保证 fuzzemu 知道每个 `HAL_BE_*` 符号地址
- `semu_config.yml handlers`：把 `HAL_BE_*` 函数名映射到 `fuzzemu.handlers.common.*`（见 `doc/fuzzemu_execution_flow.md`）

| helper 函数 | 签名 | 语义定位（replacement 用途） | fuzzemu 侧对接方式（handlers） |
|---|---|---|---|
| `HAL_BE_return_0()` | `int HAL_BE_return_0()` | 用于“只需要成功/失败返回值”的替换（典型场景：原函数不参与上层状态机/数据结构关键逻辑，只要求返回一个固定 success） | `fuzzemu.handlers.common.return_zero`（来自 `doc/fuzzemu_execution_flow.md`） |
| `HAL_BE_return_1()` | `int HAL_BE_return_1()` | 同上，用于需要返回 `1` 的情况 | `fuzzemu.handlers.common.return_true` |
| `HAL_BE_Out(int len)` | `int HAL_BE_Out(int len)` | 用于“发送/写出数据”类替换：表示一次传输动作；策略允许在不影响状态时跳过具体传递细节（保留非 I/O 逻辑由 replacement 代码自己完成） | `fuzzemu.handlers.common.hal_out` |
| `HAL_BE_In(void* buf, int len)` | `int HAL_BE_In(void* buf, int len)` | 用于“固定长度接收”：把仿真输入数据填充到 `buf` 对应的缓冲区（并让上层继续按原逻辑读取处理） | `fuzzemu.handlers.common.hal_in` |
| `HAL_BE_ENET_ReadFrame(void* buf, int length)` | `int HAL_BE_ENET_ReadFrame(void* buf, int length)` | 用于 ENET/变长报文接收：将一个“帧/报文”的字节流写入 `buf`，其中 `length` 表示该次接收的长度上限/期望长度（用于 RECV + DMA + RingBuffer 的单包模式插入点） | `fuzzemu.handlers.common.hal_read_frame` |
| `HAL_BE_Block_Write(void* buf, int block_size, int block_num)` | `int HAL_BE_Block_Write(void* buf, int block_size, int block_num)` | 用于块设备写：把 `buf` 中的数据按 block 的语义提交给仿真存储后端（不再直接访问真实存储 MMIO/flash） | `fuzzemu.handlers.common.hal_block_out` |
| `HAL_BE_Block_Read(void* buf, int block_size, int block_num)` | `int HAL_BE_Block_Read(void* buf, int block_size, int block_num)` | 用于块设备读：从仿真存储后端把指定 block 读入 `buf` | `fuzzemu.handlers.common.hal_block_in` |

补充说明（如何用于语义保持，不替代你后续的 RECV/IRQ/INIT/LOOP 策略）：
- `RECV` 策略的“数据 reception”替换点就是这些 `HAL_BE_*_In/ReadFrame` 接口（固定长度用 `HAL_BE_In`，ENET 变长用 `HAL_BE_ENET_ReadFrame`），并要求“Critical: Preserve all non-I/O logic（buffer pointer updates / state flags / data processing）”（来源：`prompts/function_classifier.py` 的 RECV strategy 段落）
- `RECV` 策略的“发送/写出”替换点通常落在 `HAL_BE_Out` 或在不影响状态时跳过（来源：`prompts/function_classifier.py` 的 RECV strategy 段落）
- “只需要返回值”的函数替换则用 `HAL_BE_return_0/1`，从而让执行流能继续到原本的上层逻辑分支（来源：`prompts/function_classifier.py` / `doc/fuzzemu_execution_flow.md` 的 handler 固定返回语义）

---

## 2.3 四类策略：Steering / Event / Skip / Redirect

去掉 Strip 后，本项目将替换策略聚合为四类：**Steering（执行流导向）**、**Event（事件触发/回调可达）**、**Skip（安全跳过/最小化 stub）**、**Redirect（输入/输出重定向/数据注入）**。每类对应不同的 control-flow 改写方式与落点，最终仍由 FunctionClassifier 的 `INIT/IRQ/RECV/LOOP` 或 `SKIP` 类型触发生成。

### 2.3.1 Steering（执行流导向）

**含义**：通过控制流旁路/短路，把依赖硬件条件的执行路径导向到仿真可达的分支。典型场景是“等待硬件标志”的轮询循环在仿真中永远不满足，导致死循环；replacement 将循环整体短路，用单次仿真动作替代，使执行能继续到后续上层逻辑。

**来源**：`prompts/function_classifier.py`（LOOP strategy 示例）

**替换前（Original）**：
```c
/* Read to clear overrun flag */
while ((base->S1 & UART_S1_RDRF_MASK) != 0U)
{
    (void)base->D;
}
```

**替换后（Replacement）**：
```c
/* [LOOP REMOVED] Waited for hardware transmission complete flag */
(void)HAL_BE_In(NULL, 1); /* Simulate reading to clear overrun flag */
```

**Original → Replacement 如何实现该策略目标**：原循环依赖 `base->S1` 的 `UART_S1_RDRF_MASK` 硬件标志，仿真中该位不会更新，导致死循环。Replacement 直接移除 while 循环，用一次 `HAL_BE_In(NULL, 1)` 模拟“读一次清标志”的语义，使函数能立即返回并把执行导向到后续逻辑。

---

### 2.3.2 Event（事件触发/回调可达）

**含义**：移除硬件中断标志的 gating，让执行必然进入原本“中断条件满足时才会执行”的处理分支，从而保证 OS 通知/回调触发路径在仿真中可达。若原 IRQ 依赖 `UART0->S1 & UART_S1_RDRF_MASK` 等硬件条件，仿真中该条件永远不成立，则回调/`xSemaphoreGiveFromISR` 等分支不可达。

**来源**：`prompts/function_classifier.py`（IRQ strategy 示例 `UART0_IRQHandler`）

**替换前（Original）**：
```c
void UART0_IRQHandler(void)
{
    if ((UART0->S1 & UART_S1_RDRF_MASK) != 0U) {
        data = UART0->D;
        process_data(data);
        xSemaphoreGiveFromISR(semaphore, &xHigherPriorityTaskWoken);
    }
    /* Clear interrupt flags */
    UART0->S1 |= UART_S1_TDRE_MASK;
}
```

**替换后（Replacement）**：
```c
void UART0_IRQHandler(void)
{
    /* Simulate interrupt flag being set */
    data = HAL_BE_In(&data, 1);
    process_data(data);
    xSemaphoreGiveFromISR(semaphore, &xHigherPriorityTaskWoken);
    /* No need to clear hardware interrupt flags */
}
```

**Original → Replacement 如何实现该策略目标**：原代码用 `if ((UART0->S1 & UART_S1_RDRF_MASK) != 0U)` 作为 gate，仿真中该条件不成立则不会进入处理分支。Replacement 去掉该 gate，用 `HAL_BE_In(&data, 1)` 模拟“读到数据”，直接执行 `process_data` 与 `xSemaphoreGiveFromISR`，保证 OS 通知/任务唤醒分支在仿真中可达。

---

### 2.3.3 Skip（安全跳过/最小化 stub）

**含义**：对纯硬件配置、无上层状态依赖的函数，用最小化 stub 替换：仅保留函数签名与参数使用（避免未使用参数告警），移除所有 MMIO/寄存器写与轮询等待。仿真中这些配置可安全忽略，不影响功能正确性。

**来源**：`testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md`（`CLOCK_SetDiv` 的 replacement_update）

**替换前（Original）**：
```c
static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift                   = CCM_TUPLE_BUSY_SHIFT(divider);
    CCM_TUPLE_REG(CCM, divider) = (CCM_TUPLE_REG(CCM, divider) & (~CCM_TUPLE_MASK(divider))) |
                                  (((uint32_t)((value) << CCM_TUPLE_SHIFT(divider))) & CCM_TUPLE_MASK(divider));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* Wait until CCM internal handshake finish. */
        while ((CCM->CDHIPR & ((uint32_t)(1UL << busyShift))) != 0UL)
        {
        }
    }
}
```

**替换后（Replacement）**：
```c
static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    /* [HARDWARE REMOVED] Skip clock divider configuration */
    (void)divider;
    (void)value;
}
```

**Original → Replacement 如何实现该策略目标**：原函数写入 CCM 寄存器并轮询 `CCM->CDHIPR` 等待 handshake 完成，仿真中既不需要时钟配置，handshake 也不会完成。Replacement 移除所有 MMIO 与 while 循环，仅用 `(void)divider; (void)value;` 满足参数使用要求，实现最小化 stub，避免未定义宏/assert 等编译问题。

---

### 2.3.4 Redirect（输入/输出重定向/数据注入）

**含义**：在接收路径中，跳过依赖硬件 empty/LAST 等标志的 gate，让执行进入“处理帧/BD”分支；在注入落点调用 `HAL_BE_ENET_ReadFrame` 将仿真数据写入 buffer；同时保留 Ring 推进语句（如 `rxBdRing->rxGenIdx = ENET_IncreaseIndex(...)`），保证 buffer 管理与上层可消费。

**来源**：`testcases/server/nxp/NXP_LwIP_BareMetal/replacement_log.md`（`ENET_GetRxFrame` 的 original 与 replacement）

**替换前（Original：empty-flag while gate 段 + do-while 内无注入）**：
```c
/* Check the current buffer descriptor's empty flag. If empty means there is no frame received. */
index = rxBdRing->rxGenIdx;
while (0U == (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK))
{
    /* Find the last buffer descriptor. */
    if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
    {
        result = ENET_GetRxFrameErr((enet_rx_bd_struct_t *)(uintptr_t)curBuffDescrip, &rxFrame->rxFrameError);
        break;
    }
    index          = ENET_IncreaseIndex(index, rxBdRing->rxRingLen);
    curBuffDescrip = rxBdRing->rxBdBase + index;
    if (index == rxBdRing->rxGenIdx)
    {
        break;
    }
}

/* Get the valid frame */
curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
index          = 0;
do
{
    newBuff = (uintptr_t)(uint8_t *)handle->rxBuffAlloc(base, handle->userData, ringId);
    if (newBuff != 0U)
    {
        rxBuffer = &rxFrame->rxBuffArray[index];
        rxBuffer->buffer = (void *)(uint8_t *)address;
        if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
        {
            isLastBuff       = true;
            rxFrame->totLen  = curBuffDescrip->length;
            rxBuffer->length = curBuffDescrip->length - buffLen;
        }
        else
        {
            rxBuffer->length = curBuffDescrip->length;
            buffLen += rxBuffer->length;
        }
        curBuffDescrip->buffer = (uint32_t)buffer;
        curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
        curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;
        index++;
        rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
        curBuffDescrip     = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    }
} while (!isLastBuff);
```

**替换后（Replacement：短路 empty gate + HAL_BE_ENET_ReadFrame 注入 + 保留 ring 推进）**：
```c
/* Check the current buffer descriptor's empty flag. If empty means there is no frame received. */
index = rxBdRing->rxGenIdx;
/* Skip hardware-dependent empty flag check - simulate that we have a frame */
if (1) /* Always enter the frame processing path for simulation */
{
    if (1) /* Simulate that we found the last BD */
    {
        result = ENET_GetRxFrameErr((enet_rx_bd_struct_t *)(uintptr_t)curBuffDescrip, &rxFrame->rxFrameError);
        result = kStatus_Success;
    }
}

/* Get the valid frame */
curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
index          = 0;
do
{
    newBuff = (uintptr_t)(uint8_t *)handle->rxBuffAlloc(base, handle->userData, ringId);
    if (newBuff != 0U)
    {
        rxBuffer = &rxFrame->rxBuffArray[index];
        rxBuffer->buffer = (void *)(uint8_t *)address;
        if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
        {
            isLastBuff       = true;
            rxFrame->totLen  = curBuffDescrip->length;
            rxBuffer->length = curBuffDescrip->length - buffLen;
        }
        else
        {
            rxBuffer->length = curBuffDescrip->length;
            buffLen += rxBuffer->length;
        }
        /* Simulate receiving data into the buffer */
        if (rxBuffer->buffer != NULL && rxBuffer->length > 0)
        {
            HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length);
        }
        curBuffDescrip->buffer = (uint32_t)buffer;
        curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
        curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;
        index++;
        rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
        curBuffDescrip     = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    }
} while (!isLastBuff);
```

**Original → Replacement 如何实现该策略目标**：原 `while (0U == EMPTY)` 依赖硬件更新 BD 的 empty 标志，仿真中该条件永远成立（或永远不成立），导致无法进入帧处理路径。Replacement 用 `if (1)` 旁路该 gate，强制进入处理分支；在拿到 `rxBuffer->buffer` 与 `rxBuffer->length` 后插入 `HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length)` 注入仿真数据；同时保留 `rxBdRing->rxGenIdx = ENET_IncreaseIndex(...)` 等 Ring 推进语句，使上层协议栈能正确消费数据且 RingBuffer 状态机前进。

---

## 3. 各类型对应的替换策略（Strategy）

> 说明：以下策略要点均来自 `prompts/function_classifier.py` 的 “Function Classification and Replacement Strategy” 及 `prompts/code_generation_rules.md` 的硬约束条款。

### 3.1 CORE（NVIC / OS kernel / VTOR）：不生成 replacement，且必须保留可观察寄存器写/CORE 调用
- `CORE`：不生成 replacement（来源：`prompts/function_classifier.py`：`CORE (NVIC / OS kernel / VTOR only; SysTick is *not* CORE)` + “Strategy: Do not generate a replacement”段落）

### 3.2 RECV：用仿真注入替代硬件数据读，并保留非 I/O 逻辑与 buffer 管理
- RECV 策略核心：
  - 数据 reception：替换为 `HAL_BE_In`（固定长度）或 `HAL_BE_ENET_ReadFrame`（变长报文）
  - 数据 transmission：重定向到 `stdout` 或跳过非关键写
  - 保留所有非 I/O 逻辑：例如 Rx 指针更新、状态标志、rxFrame 填充等
（来源：`prompts/function_classifier.py` 的 `RECV` strategy 段落 + 示例 replacement 片段）

Prompt 原文辅助（来自 `prompts/function_classifier.py` 的 RECV strategy）：

```text
For data reception: Replace with calls to `HAL_BE_In(void* buf, int len)` (fixed size) or `HAL_BE_ENET_ReadFrame(void* buf, int length)` (variable length packet).
For data transmission: Redirect output to `stdout` (e.g., using `printf`) or, if non-critical and does not affect state, skip the operation.
Critical: Preserve all non-I/O logic (buffer pointer updates, state flags, data processing).
```

下面是 `HAL_UART_Receive` 的 prompt replacement 示例（作为策略证据）：

来源：`prompts/function_classifier.py`：`HAL_UART_Receive` strategy example（该示例 replacement code 段落）

```c
HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size, uint32_t Timeout)
{
    // Simulate data reception
    HAL_BE_In(pData, Size);
    // Preserve non-I/O logic
    huart->RxXferCount = 0;
    huart->RxXferSize = Size;
    huart->RxState = HAL_UART_STATE_READY;
    return HAL_OK;
}
```

### 3.3 IRQ：移除真实硬件操作但保留 OS 通知/状态迁移
- IRQ 策略核心：
  - 移除硬件中断控制寄存器写等真实硬件操作
  - 保留中断标志检查、OS 通知（如 `xSemaphoreGiveFromISR`）、状态机更新
  - 保证仍能走到原本的数据处理或任务触发分支
（来源：`prompts/function_classifier.py` 的 `IRQ` strategy 段落）

Prompt 原文辅助（来自 `prompts/function_classifier.py` 的 IRQ strategy）：

```text
Remove actual hardware operations (e.g., writing to interrupt control registers).
Preserve: Interrupt flag checks, OS interrupt notifications (e.g., `xSemaphoreGiveFromISR`), state machine updates.
Ensure the execution flow can reach the original data handling or task triggering branches.
```

下面是 prompt 示例（作为策略证据）：

来源：`doc/lwip_eth_irq_analysis.md`：ETH 网络 IRQ 替换示例（确保到达 Rx callback/OS 通知分支）

```c
void HAL_ETH_IRQHandler(ETH_HandleTypeDef *heth)
{
    // IRQ replacement:
    // - remove real hardware operations / DMA status MMIO reads
    // - force the "RX complete" path to reach HAL_ETH_RxCpltCallback(heth)
    HAL_ETH_RxCpltCallback(heth);
}
```

### 3.4 INIT：去掉 MMIO/寄存器写，同时保留结构初始化与必要 state（并处理 CORE/调用者例外）
- INIT 策略核心：
  - 移除所有 MMIO/register access operations
  - 保留结构初始化与资源分配（如 `malloc`）、默认值设置
  - 保证替换后的“逻辑后置状态”与硬件 init 后期望一致
  - EXCEPTION：如果函数属于 `CORE`，或函数调用了 `CORE`，则 replacement 必须保留 CORE 调用/等价写； rubric 阶段会强制检查（来源：`prompts/function_classifier.py` 的 INIT EXCEPTION + rubric 强制保留规则见第 4 节）
（来源：`prompts/function_classifier.py` 的 `INIT` strategy 段落）

Prompt 原文辅助（来自 `prompts/function_classifier.py` 的 INIT strategy）：

```text
Remove all MMIO/register access operations.
Preserve resource allocation (e.g., `malloc`), structure initialization, and default value setting.
Ensure the logical post-initialization state matches the expected state after hardware init.
EXCEPTION — CORE and callers of CORE ... replacement must not remove those CORE calls; ... preserve calls to NVIC/OS/VTOR primitives (the rubric will check this).
```

下面是 `HAL_UART_Init` prompt 示例：

来源：`prompts/function_classifier.py`：`HAL_UART_Init` strategy example replacement code 段落

```c
HAL_StatusTypeDef HAL_UART_Init(UART_HandleTypeDef *huart)
{
    // Preserve structure initialization
    huart->State = HAL_UART_STATE_READY;
    huart->ErrorCode = HAL_UART_ERROR_NONE;
    // Skip hardware-specific configuration
    return HAL_OK;
}
```

### 3.5 LOOP：避免等待硬件标志的死循环（Skip 或改为单次仿真读）
- LOOP 策略核心：
  - 等待状态标志：跳过整个循环（假设条件已满足）
  - FIFO until empty：替换为单次读或单次仿真接收
  - 增加注释解释原循环目的
（来源：`prompts/function_classifier.py` 的 `LOOP` strategy 段落）

Prompt 原文辅助（来自 `prompts/function_classifier.py` 的 LOOP strategy）：

```text
If waiting for a status flag: Skip the loop entirely (assume the condition is already met).
If reading data from a FIFO until empty: Replace with a single read or a call to a simulation receive function.
Add a comment explaining the original loop's purpose.
```

下面是 prompt 示例（作为证据）：

来源：`prompts/function_classifier.py`：`LOOP` example replacement code 段落

```c
/* [LOOP REMOVED] Waited for hardware transmission complete flag */
(void)HAL_BE_In(NULL, 1); /* Simulate reading to clear overrun flag */
```

### 3.6 RETURNOK / SKIP / NODRIVER：只分类，不生成 replacement（“Skip 类语义”体现在 has_replacement=false）
- 这些类型属于 “Priority 2: Classification Only（Do Not Generate Code Now）”
- 对它们：只输出 classification 与推理，不生成 replacement code（来源：`prompts/function_classifier.py` 对 RETURNOK / SKIP / NODRIVER 的“classification only”声明）

---

## 4. 实现语义保持不变量（Invariants）

本节把“为什么必须这样替换”的关键语义保持点明确为不变量。它们是本项目在仿真环境中不出错的必要条件（尤其与 MMIO hook、OS调度/中断模拟有关）。

### 4.1 CORE / NVIC / SysTick / VTOR 写入不变量：必须保留可观察寄存器写（仿真依赖寄存器写钩子）
不变量表述：
- 仿真器在拦截某些寄存器写（例如 SysTick、NVIC、VTOR）后，才会更新内部“中断/时钟/向量表模拟”的状态
- 因此：任何包含/配置 VTOR、SysTick、NVIC 的 replacement，都不得把这些写删除或替换成简单 return
- 对 CORE：若原函数调用了 CORE primitives（NVIC 配置、OS 调度、VTOR setup），replacement 必须保留这些调用；否则 rubric 必须拒绝该 replacement

证据：
- `prompts/replacement_rubric_checker.py` 明确指出 emulator 依赖 “seeing these register writes in the replacement code” 来模拟 interrupts/tick/vector table，并列出 VTOR、SysTick、NVIC 规则（来源：`prompts/replacement_rubric_checker.py` 对 CORE 与强制保留规则的条款）

引用要点（原文规则摘要，来自 rubric）：
- “VTOR must still contain the write to VTOR… Removing it causes emulator to read from 0x0 and crash.”（来源：`prompts/replacement_rubric_checker.py` 的 VTOR 规则段落）
- “If original configures the system tick… replacement must still contain those register writes… A stub that only returns success is not acceptable.”（来源：同文件 SysTick 规则段落）
- “If original configures NVIC… replacement must still contain corresponding NVIC writes or API calls. Removing them breaks interrupt simulation.”（来源：同文件 NVIC 规则段落）

### 4.2 INIT 替换不变量：去寄存器写，但必须保留结构初始化与必要 state
不变量表述：
- INIT 替换的目标是“消除硬件寄存器/MMIO依赖”，但不能把初始化语义整体丢掉
- 替换后的函数必须至少完成：
  - 必要的结构字段初始化（如 `State`、`ErrorCode` 等）
  - 资源/分配/默认值设置
  - 保证逻辑上处于硬件 init 之后的期望状态，以便后续收发/IRQ 分支能按正确条件运行

证据：
- `prompts/function_classifier.py` 对 INIT strategy 明确要求 Preserve resource allocation / structure initialization / default value setting，并“Ensure logical post-initialization state matches expected”（来源：`prompts/function_classifier.py` 的 INIT strategy 段落）

### 4.3 IRQ 替换不变量：移除真实硬件操作但保留 OS 通知/状态迁移
不变量表述：
- IRQ replacement 不应破坏“仿真时任务调度/同步对象状态迁移”
- 必须保留：
  - OS 通知调用（例如 semaphore/queue 等 ISR 语义）
  - 状态机更新与条件分支（保证仍可触发到数据处理路径或任务触发路径）

证据：
- `prompts/function_classifier.py` 的 IRQ strategy 明确：Preserve OS interrupt notifications and state machine updates，并确保 flow 能到达原数据处理或任务触发分支（来源：`prompts/function_classifier.py` 的 IRQ strategy 段落）

### 4.4 RECV 替换不变量：通过 HAL_BE 注入数据，并保持 buffer 管理与上层状态一致
不变量表述：
- 数据 reception 必须通过：
  - `HAL_BE_In`（固定长度）或
  - `HAL_BE_ENET_ReadFrame`（变长 packet）
  注入到原函数期望写入的 buffer
- 同时必须保持 buffer 管理/状态同步（例如 Rx 指针计数、RxState、rxFrame 填充、Ring 更新等），否则上层协议栈无法正确消费数据

证据：
- `prompts/function_classifier.py` 的 RECV strategy 明确规定 HAL_BE_In / HAL_BE_ENET_ReadFrame 的使用位置，并要求 “Critical: Preserve all non-I/O logic (buffer pointer updates, state flags, data processing)”（来源：`prompts/function_classifier.py` 的 RECV strategy 段落）

### 4.5 LOOP 替换不变量：避免等待硬件标志的死循环（特别是仿真无真实硬件写时）
不变量表述：
- LOOP 替换应防止“等待外设状态位”的条件在仿真环境永远不满足
- 因此：
  - 若原循环在等待 status flag：跳过循环
  - 若原循环在从 FIFO 读取直到 empty：改为单次仿真读

证据：
- `prompts/function_classifier.py` 的 LOOP strategy 明确给出这两条规则（来源：`prompts/function_classifier.py` 的 LOOP strategy 段落）

---

## 5. 具体例子（用现有分析文档做证据支撑）

### 5.1 ETH（LwIP StreamServer）：初始化问题——未保留 `HAL_ETH_MspInit` / NVIC 使能导致收包 IRQ 不触发
现象与原因（证据来自 `doc/lwip_eth_irq_analysis.md`）：
- 正常走到收包逻辑需要两个条件：
  1) ETH 相关中断已在 NVIC 中打开  
  2) ETH IRQ 触发后，IRQ 处理函数能执行到收包逻辑（释放信号量/触发 RxCpltCallback）  
  （来源：`doc/lwip_eth_irq_analysis.md`：`模拟器本身有中断机制...需要满足两点` 段落）
- 文档指出典型“初始化侧”失效原因：替换后的 `HAL_ETH_Init` 没有调用 `HAL_ETH_MspInit`，因此 `HAL_NVIC_EnableIRQ(ETH_IRQn)` 从未执行，ETH 中断在 NVIC 中未被使能，收包 IRQ 不触发
  （来源：`doc/lwip_eth_irq_analysis.md`：`根因：HAL_ETH_Init 未调用 HAL_ETH_MspInit` 相关段落）
- 文档同时给出了更深一层的“分类/Prompt 误判”根因：`Classifier` 的 no-stub 列表在起初没有包含 `HAL_ETH_MspInit`，使得模型把 `HAL_ETH_MspInit` 当作可 `SKIP` 的函数；此外 SKIP 示例曾写过 `HAL_UART_MspInit`，导致模型对 `HAL_ETH_MspInit` 做了类推，从而错误地把 `HAL_ETH_MspInit` 变成空实现，最终 `HAL_NVIC_EnableIRQ(ETH_IRQn)` 未发生。
  （来源：`doc/lwip_eth_irq_analysis.md`：`根因：Classifier / Fixer 的 Prompt 导致误删` 以及其下 `Classifier` 的 Prompt 问题段落，包含 “HAL_ETH_MspInit 被当成可 SKIP 的函数” 与 “SKIP 示例类推到 HAL_ETH_MspInit” 的描述）
- 该文档进一步归纳：即使调用链存在，若替换后的 `HAL_NVIC_EnableIRQ` 是“跳过硬件写”的桩，仿真侧无法通过 MMIO hook 记录“IRQ 已使能”，也会导致 ETH IRQ 永远不真正响应
  （来源：`doc/lwip_eth_irq_analysis.md`：`根因：HAL_NVIC_EnableIRQ 被替换为“不写 NVIC”的桩` 相关段落）

如何映射回本文的策略设计：
- 这直接对应第 4 节不变量 `CORE / NVIC / SysTick / VTOR 写入不变量`：在替换策略设计里，`INIT` 不是“纯粹空替换”，而必须保留与 `*_MspInit` / NVIC 使能相关的可观察写/调用
- 同时对应第 2 节的修正：用户 INIT=Skip 不能误解为“删掉寄存器写并忽略 MspInit/NVIC”；正确含义是“去掉外设配置 MMIO 但保留仿真必须看到的 CORE/NVIC/VTOR/SysTick 相关写与调用”
（证据链接：`doc/lwip_eth_irq_analysis.md` 的初始化失效分析；以及 `prompts/replacement_rubric_checker.py` 的强制保留规则）

补充：与 ETH 相关的 Prompt 原文约束（用于避免 NVIC 使能被误删）

1) `SKIP` 不允许把“会使能中断”的 `*_MspInit` 当作可跳过函数（否则 ETH IRQ 永远不触发）

```text
Do not treat any `*_MspInit` that enables interrupts (e.g. `HAL_ETH_MspInit` calling `HAL_NVIC_EnableIRQ(ETH_IRQn)`) as SKIP — those must preserve NVIC writes or be SKIP with no replacement (see INIT Exception above).
```

2) `INIT` 必须保留调用 CORE 的路径（否则替换会破坏“初始化后置状态”与仿真中断/调度语义）

```text
EXCEPTION — CORE and callers of CORE ... replacement must not remove those CORE calls; ... preserve calls to NVIC/OS/VTOR primitives (the rubric will check this).
```

ETH 关键代码片段（证据：替换体必须能让仿真器捕获到 NVIC 使能写）

```c
NVIC->ISER[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F));
```

（来源：`doc/lwip_eth_irq_analysis.md`：关于 `HAL_NVIC_EnableIRQ` 被替换为“不写 NVIC”桩导致 ETH 中断未使能的分析）

### 5.2 NXP + LwIP + ENET：接收问题——ENET RX 卡死在 `ENET_GetRxFrame / ENET_IncreaseIndex`；Prompt 单包模式硬约束保证 RingBuffer 状态机可前进
问题现象与根因（证据来自 `doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`）：
- 文档描述最初 fuzzemu 仿真中 ENET 接收卡死：`ENET_GetRxFrame -> ENET_IncreaseIndex` 重复调用几十/上百次，`ethernetif_linkinput` 一直阻塞  
  （来源：`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`：`问题现象：卡死...` 段落）
- 根因是 `ENET_GetRxFrame` 的“依赖硬件 Flag 扫描 BD Ring 找帧”的状态机在仿真环境无法完成退出条件，因为 `LAST/EMPTY/OWN` 等标志位不会被真实硬件更新  
  （来源：同文档：`根因：... LAST/EMPTY/OWN ... 导致死循环` 段落）
- 初版替换若保留 `do { ... } while (!isLastBuff);` 这类多 BD/多帧扫描状态机，就会出现 `curBuffDescrip->control` 的 `LAST_MASK` 在仿真中不被置位，`isLastBuff` 永远 false，从而 `do-while` 永不退出  
  （来源：同文档：`初版替换...仍保留 do-while 状态机（失败方案）` 及 `isLastBuff 永远不置位` 相关段落）

关键 C 片段（证据：HAL_BE 插入点与“多 BD 扫描 do-while”导致的死循环形态）

1) `HAL_BE_ENET_ReadFrame` 插入点（原始 do-while 中在拿到 buffer/length 后注入）

```c
if (rxBuffer->buffer != NULL && rxBuffer->length > 0)
{
    HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length);
}
```

（来源：`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`：do-while 内插入点）

2) 失败形态（仿真无真实硬件更新时，`isLastBuff` 永远 false）

```c
do
{
    ...
    if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
    {
        isLastBuff = true;
        ...
        HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length);
    }
    ...
    rxBdRing->rxGenIdx = ENET_IncreaseIndex(...);
}
while (!isLastBuff);
```

（来源：同文档：初版替换失败样例代码）

Prompt 的单包模式硬约束（必须摘取的条款，来源 `prompts/code_generation_rules.md`）：

来源：`prompts/code_generation_rules.md`：`RECV with复杂 DMA+RingBuffer 控制流（网络收帧）` 强约束条款（节选）

```markdown
- **RECV with复杂 DMA+RingBuffer 控制流（网络收帧）**：默认采用“**单次收一包**”的仿真思路，在保证 RingBuffer 状态正确的前提下，**禁止保留原始按 LAST/EMPTY 扫环的多帧状态机**：
  - **只收一包（强约束）**：本次调用只模拟接收一帧数据，最多处理一个“当前 BD 所在的帧”，**不得实现多 BD/多帧遍历逻辑**；生成代码中 **不允许出现 `while` / `do { ... } while` 这类以 `isLastBuff`、`ENET_BUFFDESCRIPTOR_RX_LAST_MASK`、`ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK` 为退出条件的环扫描结构。
  - **跳过硬件 Flag + while 状态机**：依赖 `EMPTY/LAST/OWN` 等硬件写入标志位的“找帧” while/for 循环必须整体**删除或短路**，使用条件判断+`goto` 或直接重排控制流，让代码从入口尽快跳到“已经有一个当前 BD/缓冲区可以用”的分支，且该分支内部不再通过循环扫描 Ring。
  - **保留 Ring 关键操作（单次）**：必须保留**一次** `rxBuffAlloc`/buffer 分配、**一次**从 BD 取 buffer/length/totLen 填充 `rxFrame` 的逻辑，以及**一次**完整的 BD 消费+`rxGenIdx`/下标推进+BD 归还操作，保证描述符环在“单包模式”下前进一步；禁止在同一调用内多次连续调用 `ENET_IncreaseIndex` 形成扫描式循环。
  - **HAL_BE 插入点（单包模式）**：在“当前 BD 已有有效 buffer 指针、且即将把该 buffer 视为本次帧缓存”这一点调用 `HAL_BE_ENET_ReadFrame(buffer, length)`，一次性写入本次要模拟的网络帧；之后沿用原函数的 `rxFrame` 填充和 Ring 更新逻辑，并在完成一次 BD 更新后立即返回，不再继续循环。
```

单包模式为何能避免死循环（与 ENET 分析文档的闭环一致）：
- ENET 文档明确目标行为是：每次调用只收一帧，进行一次 `HAL_BE_ENET_ReadFrame` 注入、一次 BD 消费与 `rxGenIdx` 推进，并立即返回，从而在无硬件更新 `LAST/EMPTY` 的仿真环境下保证 RingBuffer 状态机前进  
  （来源：`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`：`目标行为：... 单次收一帧... 一次 HAL_BE + 一次 Ring 前进一步` 段落）
- 与上面的代码生成硬约束在逻辑上互相印证：通过“禁止保留环扫描结构”把“不变量：避免等待硬件标志死循环”从策略层强制落地到 ENET RECV 替换代码结构中  
  （来源：`doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md` 与 `prompts/code_generation_rules.md` 单包模式条款）

### 5.3 UART：初始化问题 + 接收问题——分别对应 `INIT` 与 `RECV` 的策略示例（以 `HAL_UART_Init`/`HAL_UART_Receive` 为证据）
UART 的“初始化问题”：
- `function_classifier.py` 的 `HAL_UART_Init` replacement 示例说明：INIT 替换要保留结构初始化（例如 `huart->State`、`huart->ErrorCode`），并跳过硬件特定配置，返回成功  
  （来源：`prompts/function_classifier.py`：`HAL_UART_Init` strategy example 段落）

UART 的“接收问题”：
- 同文件的 `HAL_UART_Receive` replacement 示例说明：RECV 替换通过 `HAL_BE_In(pData, Size)` 注入仿真数据，同时保留非 I/O 逻辑（例如 Rx 计数/状态字段更新）并返回 `HAL_OK`  
  （来源：`prompts/function_classifier.py`：`HAL_UART_Receive` strategy example 段落）

把 UART 例子映射回本文修正后的映射：
- INIT（用户 Skip）应理解为：skip 硬件寄存器写，但不能丢初始化语义与必要 state（对应本文第 2 节“INIT 修正为 INIT 类但保留结构初始化/necessary state”）
- RECV（用户 Redirect）应理解为：走 RECV 的数据注入路径，并保留 buffer 管理与状态字段更新（对应本文第 2 节“RECV→RECV reception 分支，使用 HAL_BE_In/ENET_ReadFrame”）

---

## 6. 证据索引（Evidence Index）

本文直接引用（或基于其中策略/分析推导关键规则）的仓库文件：
- `prompts/function_classifier.py`
  - 分类优先级与分类集合：`CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER`
  - 各类型 strategy：`CORE / RECV / IRQ / INIT / LOOP` 以及 `RETURNOK/SKIP/...` 的 “classification only”
  - UART 策略示例：`HAL_UART_Init`、`HAL_UART_Receive`、`UART0_IRQHandler`、`LOOP` 示例片段
- `prompts/replacement_rubric_checker.py`
  - CORE/NVIC/SysTick/VTOR 必须保留可观察寄存器写与 API calls 的 rubric 规则
- `prompts/code_generation_rules.md`
  - NXP ENET DMA + RingBuffer 接收路径的“单包模式”硬约束条款（禁止 while/do-while 环扫描、单次 `HAL_BE_ENET_ReadFrame`、一次 BD 前进等）
- `doc/lwip_eth_irq_analysis.md`
  - ETH 初始化侧失败分析（NVIC 未使能、`HAL_ETH_MspInit`/`HAL_NVIC_EnableIRQ` 相关替换失效模式）
- `doc/NXP_LwIP_BareMetal_ENET_DMA_RingBuffer_recv.md`
  - ENET RX 卡死分析、初版 do-while 失败原因、单包模式目标行为与验证闭环

行为与验证闭环

ET_DMA_RingBuffer_recv.md`
  - ENET RX 卡死分析、初版 do-while 失败原因、单包模式目标行为与验证闭环

