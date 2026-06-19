# LwIP StreamServer：ETH 收包为何未触发 —— 分析清单

模拟器本身有中断机制（NVIC、Systick、PendSV 等均会触发）。要正常走到收包逻辑，需要满足两点：

1. **ETH 相关中断已在 NVIC 中打开**
2. **ETH IRQ 触发后，IRQ 处理函数能执行到收包逻辑（如释放信号量 / 调 RxCpltCallback）**

下面只做「demo + 函数替换」侧的分析，不改模拟器。

---

## 一、ETH 中断是否被打开？

### 1.1 正常流程（未替换时）

- `ethernetif_init` → `HAL_ETH_Init(&EthHandle)`  
- `HAL_ETH_Init` 内部会调 **`HAL_ETH_MspInit(heth)`**  
- 在 STM32 工程里，**`HAL_ETH_MspInit`** 里会做：
  - GPIO/时钟等配置
  - **`HAL_NVIC_EnableIRQ(ETH_IRQn)`**（或 `HAL_NVIC_SetPriority` + `HAL_NVIC_EnableIRQ`）
- 只有执行到 `HAL_NVIC_EnableIRQ(ETH_IRQn)` 后，NVIC 里 ETH 才在「已使能」列表里，之后若有 pending 才会真正响应。

### 1.2 需要你确认的点（demo + 替换）

- **当前固件里 `HAL_ETH_Init` 是否仍会调用 `HAL_ETH_MspInit`？**  
  - 若替换时把 `HAL_ETH_Init` 改成了「只设状态、直接 return」而没有调 `HAL_ETH_MspInit`，则 **ETH 中断从未被 Enable**，这是「未打开」的典型原因。
- **若仍会调 `HAL_ETH_MspInit`，替换后的 `HAL_ETH_MspInit` 里是否还保留 `HAL_NVIC_EnableIRQ(ETH_IRQn)`？**  
  - 若替换时把 `HAL_ETH_MspInit` 改成空实现或只做部分初始化并删掉了 `HAL_NVIC_EnableIRQ(ETH_IRQn)`，同样会导致 **ETH 中断从未打开**。

**建议检查：**

- 在 **output.elf** 里看：
  - `HAL_ETH_Init` 的机器码/反汇编里是否还有对 `HAL_ETH_MspInit` 的调用；
  - 若有，再看 `HAL_ETH_MspInit` 里是否还有对 `HAL_NVIC_EnableIRQ` 的调用（或对 NVIC ISER 的写）。
- 或在 **function.txt** 里确认：在 `ethernetif_init` → `HAL_ETH_Init` 的**同一调用栈**下，是否出现过 **`HAL_ETH_MspInit`** 和 **`HAL_NVIC_EnableIRQ`**（且调用时使能的是 ETH 对应 IRQn）。  
  当前日志里只看到 `HAL_NVIC_EnableIRQ` 来自 `HAL_InitTick`，没有看到来自 `HAL_ETH_MspInit` 的 EnableIRQ，这与「ETH 未被 Enable」一致，需在 demo/替换代码里确认。

---

## 二、IRQ 触发后能否执行到收包逻辑？

### 2.1 正常流程

- 硬件产生 RX 完成 → NVIC 挂起 ETH IRQ → 进入 **`ETH_IRQHandler`** → **`HAL_ETH_IRQHandler`**  
- `HAL_ETH_IRQHandler` 读 ETH DMA/状态寄存器，若为 RX 完成则调 **`HAL_ETH_RxCpltCallback`**  
- 该回调里会 **释放 LwIP 用的信号量**，从而唤醒 **`ethernetif_input`**  
- `ethernetif_input` 里再调 `low_level_input` → `HAL_ETH_GetReceivedFrame` / 最终到 **`HAL_BE_ENET_ReadFrame`**（你的 `hal_read_frame`）

### 2.2 需要你确认的点（demo + 替换）

- **`ETH_IRQHandler` / `HAL_ETH_IRQHandler` 是否被替换成「直接 return」或等价空实现？**  
  - 若被替换成不做事，则即使 ETH 中断被挂起并响应，也**不会**执行到 `HAL_ETH_RxCpltCallback`，收包逻辑永远不会跑。  
  - 当前 **semu_config 的 handlers** 里**没有**对 `ETH_IRQHandler` / `HAL_ETH_IRQHandler` 的映射，所以是跑固件里编译进去的实现；若固件源码里这两者被替换成空实现，问题就在这里。
- **若未被替换，`HAL_ETH_IRQHandler` 是否依赖「读 ETH 外设状态/ DMA 寄存器」才能走到 Rx 分支？**  
  - 若是，在仿真里这些寄存器通常不会被「硬件」置位，所以条件不成立，不会调 `HAL_ETH_RxCpltCallback`，同样走不到收包逻辑。  
  - 这种情况属于「IRQ 会进，但逻辑分支不到收包」，需要在替换策略里考虑：要么在 IRQ 里模拟「有 RX 完成」，要么用别的方式（如 stub）保证能执行到释放信号量 / 调 RxCpltCallback 的路径。

**建议检查：**

- 在固件源码或 output.elf 里确认：
  - `ETH_IRQHandler` / `HAL_ETH_IRQHandler` 的**当前实现**（是否被替换、是否为空）。
  - `HAL_ETH_IRQHandler` 内判断「RX 完成」的分支依赖哪些读寄存器；在无真实 ETH 硬件时，这些读是否永远为 0，导致从不进入 Rx 分支。

---

## 三、小结：优先在 demo/替换侧核对的项

| 检查项 | 结论方式 |
|--------|----------|
| **1. ETH 中断是否打开** | 确认 `HAL_ETH_Init` 仍调 `HAL_ETH_MspInit`，且 `HAL_ETH_MspInit` 里仍保留 `HAL_NVIC_EnableIRQ(ETH_IRQn)`（或等价 NVIC 使能）。可在 ELF 反汇编或 function 调用栈里验证。 |
| **2. IRQ 能否执行到收包** | 确认 `ETH_IRQHandler` / `HAL_ETH_IRQHandler` 未被替换成空；若依赖读 ETH 状态寄存器，需在替换策略里保证该路径可到达（例如在 IRQ 里模拟 RX 完成或 stub 状态位）。 |

先按上面两项在「当前 demo + 函数替换」上做确认，再根据结果决定是改替换代码（保留 MspInit 里 EnableIRQ、或调整 IRQ 实现）而不是改模拟器。

---

## 四、基于 output.elf + function.txt 的核查结果（已做）

### 4.1 ETH 中断是否被打开？—— **未打开**

- **ELF 反汇编 `HAL_ETH_Init`（0x0800358a）**  
  - 整段函数内**没有任何 `bl`/`blx`**，只有对 heth 结构体、描述符和 ETH 外设寄存器的读写。  
  - **结论：当前固件里的 `HAL_ETH_Init` 未调用 `HAL_ETH_MspInit`**（且 `nm` 显示 ELF 中**没有**符号 `HAL_ETH_MspInit`），因此不会执行到 `HAL_NVIC_EnableIRQ(ETH_IRQn)`，**ETH 中断在 NVIC 中从未被使能**。

- **`HAL_ETH_Start_IT`（0x0800364e）**  
  - 反汇编中同样**没有**对 `HAL_NVIC_EnableIRQ` 的调用，只有状态和使能位的设置。  
  - 通常 NVIC 使能在 `HAL_ETH_MspInit` 里完成，当前二进制里这条路径不存在。

- **function.txt 调用栈**  
  - `ethernetif_init` → `HAL_ETH_Init` 的调用链下，只看到 `HAL_ETH_Init` 直接做 memset/描述符等逻辑，**没有**出现 `HAL_ETH_MspInit` 或来自 ETH 路径的 `HAL_NVIC_EnableIRQ`。  
  - `HAL_NVIC_EnableIRQ` 仅在 `HAL_InitTick`（SysTick）等其它路径出现，与文档 1.2 的推断一致。

**结论（A）：demo/替换后的 `HAL_ETH_Init` 未调用 `HAL_ETH_MspInit`，ETH 相关中断在 NVIC 中未被打开，这是收包 IRQ 从未触发的直接原因之一。**

**说明**：若你当前 run 的 function.txt 里已出现 `HAL_ETH_MspInit` 和来自 `HAL_ETH_MspInit` 的 `HAL_NVIC_EnableIRQ`，则固件侧「调用链」已通，需继续看 4.5 节——很可能是 **`HAL_NVIC_EnableIRQ` 的替换体未写 NVIC**，导致模拟器侧 ETH 仍未打开。

---

### 4.5 根因：`HAL_NVIC_EnableIRQ` 被替换为「不写 NVIC」的桩（模拟器侧 ETH 未打开）

即使固件已执行 `HAL_ETH_MspInit` → `HAL_NVIC_EnableIRQ(ETH_IRQn)`，**模拟器**只有在**捕获到对 NVIC 寄存器的写**时才会更新内部「某 IRQ 已使能」的状态。fuzzemu 通过 **MMIO 钩子** 监听对 `NVIC->ISER[]` 等的写操作。

当前 `lcmhal_ai_log/replacement_update_HAL_NVIC_EnableIRQ_*.json` 中的替换实现为：

- **仅做参数校验 + `(void)IRQn`，显式注释掉 `NVIC_EnableIRQ(IRQn)`，不写 NVIC->ISER。**

因此：

1. 固件侧：`HAL_NVIC_EnableIRQ(ETH_IRQn)` 会被调用（来自 `HAL_ETH_MspInit`）。
2. 替换侧：被调用的函数体内**没有任何对 NVIC 的写**。
3. 模拟器侧：从未收到「使能 IRQ 61（ETH）」的 MMIO 写，**在模拟器内部 ETH 中断始终处于未打开状态**，即使后续有 ETH pending 也不会响应。

**结论**：**ETH 中断号在模拟器侧未打开**的直接原因是：**`HAL_NVIC_EnableIRQ` 的替换实现是「跳过硬件写」的桩**，未保留对 `NVIC->ISER` 的写，导致 fuzzemu 无法记录 ETH（及所有其它外设）IRQ 的使能。

**修复**：修改 `HAL_NVIC_EnableIRQ` 的替换，**必须保留对 NVIC 的写**，使模拟器能通过 MMIO 钩子看到使能动作。例如在替换体中调用 CMSIS `NVIC_EnableIRQ(IRQn)`，或直接写：

```c
NVIC->ISER[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F));
```

修改后需删除或更新 `replacement_update_HAL_NVIC_EnableIRQ_*.json`，重新构建并跑仿真，模拟器侧才会把 ETH（及 SysTick 以外的其它外设）IRQ 记为已打开。

---

### 4.6 为何会触发 ReplacementUpdate？原文会死循环吗？

**ReplacementUpdate 的触发时机**：只有 **Builder Agent**（构建失败后修代码）或 **Fixer Agent**（根据模拟器错误修代码）**调用工具** `update_function_replacement` 时，才会写出 `replacement_update_*.json`。FunctionClassifier 只写 `function_classify_*.json`，不会直接写 replacement_update。

**可能触发场景**：
1. **构建失败** → 跑 Builder Agent → 模型对部分函数（含 HAL_NVIC_EnableIRQ）给出“POSIX 兼容”替换并调用 `update_function_replacement`。
2. **模拟器报错/超时** → 跑 Fixer Agent → 模型根据错误或上下文，对 HAL_NVIC_EnableIRQ 给出“跳过硬件写”的替换并调用 `update_function_replacement`。
3. **沿用 Classifier 的 INIT 策略**：Classifier 对 INIT 类要求“Remove all register writes”；若 HAL_NVIC_EnableIRQ 被分为 INIT，会生成“去掉 NVIC 写”的替换。该替换先出现在 `function_classify_*.json`；若之后某次 Builder/Fixer 运行时的上下文中包含该函数，模型可能再次给出相同或类似替换并调用 `update_function_replacement`，从而写成 `replacement_update_*.json`。

**原文是否会导致死循环或错误**：**不会**。ST 的 `HAL_NVIC_EnableIRQ` 实现就是一次对 `NVIC->ISER[]` 的写，没有循环。在模拟器里这只是被 MMIO 钩子捕获的一次写，也不会引入死循环。因此当前这份“不写 NVIC”的替换**不是**为了修死循环或运行错误，而是为了“POSIX 兼容 / 去掉硬件写”（与 Classifier 的 INIT 策略一致），但该策略对 NVIC 使能不适用——模拟器依赖看到这次写才能记录 ETH 等 IRQ 已打开。现有 Fixer prompt 已规定不得对 `HAL_NVIC_EnableIRQ` 做空桩，当前 replacement_update 内容与之**不符**，需按 4.5 节修复。

---

### 4.7 为何 Prompt 强调了 NVIC 仍没生效？已做修复

**原因归纳**：

1. **Classifier 没有 NVIC 例外**  
   Fixer/Builder 的 prompt 里有「不得对 HAL_NVIC_EnableIRQ 做空桩」等规则，但 **FunctionClassifier 的 prompt 里没有**。Classifier 对 INIT 类的策略是「Remove all register writes」，因此会把 `HAL_NVIC_EnableIRQ` 分成 INIT 并生成「去掉 NVIC 写」的替换。该替换先进入 `function_classify_*.json`；若之后 Builder/Fixer 在上下文中看到这份替换并调用 `update_function_replacement`，就会写成 `replacement_update_*.json`，从而覆盖/绕过 Fixer 的约束。

2. **Rubric 仅靠 LLM，且异常时 fail-open**  
   落盘前会调 `check_replacement_rubric`，但该检查是 **LLM 判断**，可能误判为通过。且代码里 **异常时返回 `pass: True`**（例如网络/超时），导致一旦 rubric 报错就**接受**当前替换，坏替换仍被写入。

3. **没有确定性兜底**  
   没有在代码里对「NVIC 相关函数必须含 NVIC 写」做硬编码校验，完全依赖 prompt + LLM，一旦模型或异常处理放行就会生效。

**已做修改**：

| 位置 | 修改 |
|------|------|
| **prompts/function_classifier.py** | 为 INIT 增加 **EXCEPTION**：列出 `HAL_NVIC_EnableIRQ`、`HAL_NVIC_SetPriority`、`HAL_ETH_MspInit` 等，规定不得应用「Remove all register writes」；要么 SKIP 且不生成替换，要么替换中**保留** NVIC/SysTick/VTOR 写。并修正 SKIP 示例，避免模型类推到 `HAL_ETH_MspInit`。 |
| **utils/replacement_rubric.py** | **确定性预检**：对 `HAL_NVIC_EnableIRQ`、`HAL_NVIC_SetPriority`、`HAL_ETH_MspInit` 等，若替换体中不包含规定子串（如 `NVIC_EnableIRQ`、`ISER[`），直接返回 `pass: False`，不依赖 LLM。**异常时改为 fail-closed**：rubric 调用异常时返回 `pass: False`，不再接受替换。 |

这样即使 LLM 或 Classifier 仍产出违规替换，**确定性规则会拦截**，且异常时不会误放行。

### 4.8 引入 CORE 类别：从源头避免误替换

已引入 **CORE** 分类（仅 NVIC/OS 内核/VTOR，**不包含 SysTick**），从分类阶段杜绝对这类函数本身的替换：

- **定义**：CORE 仅包含 **(1) NVIC 配置**（如 `HAL_NVIC_EnableIRQ`、`HAL_NVIC_SetPriority`、`HAL_NVIC_SetPriorityGrouping`）、**(2) OS 内核/调度/上下文切换**（如 `PendSV_Handler`、`SVC_Handler`、`vTaskSwitchContext`、`portYIELD_FROM_ISR`）、**(3) 向量表/VTOR 配置**（如 `SystemInit` 写 `SCB->VTOR`）。**SysTick** 相关（如 `SysTick_Config`、`HAL_InitTick`）**不属于** CORE，由其他策略/ rubric 单独约束。
- **策略**：CORE 类**一律不生成替换**（`has_replacement: false`），分类时 **CORE 优先级最高**。非 CORE 函数（如某 INIT）若**调用了** CORE 函数，可以做修改，但**替换体不能简单删掉对 CORE 的调用**，由 **rubric 阶段**（LLM 评审，传入原始代码与替换代码对比）统一检查并拒绝违规替换。
- **实现**：Classifier 中 CORE 定义与优先级；`replace_funcs()` 对 CORE 跳过替换；rubric 使用通用 LLM prompt（无确定性硬编码列表），在提供 `original_code` 时强制「caller 必须保留对 CORE 的调用」。

---

### 4.2 IRQ 触发后能否执行到收包逻辑？—— **即使触发也走不到 Rx 分支**

- **`ETH_IRQHandler`（0x080019b4）**  
  - 实现为：取 heth 指针（0x200004d4），然后 `b.w HAL_ETH_IRQHandler`。  
  - **未被替换成空**，会正常跳转到 `HAL_ETH_IRQHandler`。

- **`HAL_ETH_IRQHandler`（0x0800378c）**  
  - 会读 ETH 外设寄存器（如 ETH 基址 +0x1000 的 DMA 状态，对应约 0x40013c00 区）。  
  - 进入 **RX 完成分支** 并调用 `HAL_ETH_RxCpltCallback`（0x08000788）的条件是：  
    - `r5` 的某位（来自 `[r3,#20]`，即 DMA 状态）被置位；且  
    - `r8`（来自 `[r3,#28]`）与 `0x40` 相与非零。  
  - 在无真实 ETH 硬件、且模拟器未对上述 MMIO 做「收包完成」模拟的情况下，这些寄存器读出来一般为 0，**条件不成立，不会执行 `bl 8000788 <HAL_ETH_RxCpltCallback>`**。

**结论（B）：即使之后在 NVIC 中打开了 ETH 中断并人为挂起 ETH IRQ，当前 `HAL_ETH_IRQHandler` 仍依赖 ETH DMA 状态位；仿真里这些位未被置位，因此不会进入 Rx 分支，收包逻辑（含 `HAL_ETH_RxCpltCallback`）仍然不会执行。**

---

### 4.3 建议的修改方向（demo/替换侧）

| 问题 | 建议 |
|------|------|
| **（A）ETH 中断未打开** | 在 **替换/弱符号** 的 `HAL_ETH_Init` 中恢复对 `HAL_ETH_MspInit` 的调用，或在 `ethernetif_init` 调用 `HAL_ETH_Init`/`HAL_ETH_Start_IT` 之后，**显式调用一次 `HAL_NVIC_EnableIRQ(ETH_IRQn)`**（STM32F4/F7 上多为 61）。若使用替换的 `HAL_ETH_MspInit`，需保证其内部包含 `HAL_NVIC_EnableIRQ(ETH_IRQn)`。 |
| **（B）IRQ 进但走不到 Rx** | 在仿真侧二选一或组合：① 对 ETH DMA 状态相关 MMIO（如 0x40013c00 区）做 hook，在「有注入包」时写入 RX 完成位，让现有 `HAL_ETH_IRQHandler` 自然走到 `HAL_ETH_RxCpltCallback`；② 或提供 **`ETH_IRQHandler`/`HAL_ETH_IRQHandler` 的替换实现**，在仿真时直接调 `HAL_ETH_RxCpltCallback` 或等效的释放信号量逻辑，而不依赖读 DMA 状态。 |

以上均可在不改动模拟器核心中断机制的前提下，通过「demo 源码/替换 + 可选 MMIO 或 handler 替换」完成。

---

### 4.4 根因：Classifier / Fixer 的 Prompt 导致误删

**谁在做「删除」：** 替换代码由 **Classifier**（分类 + 生成初始替换）和 **Fixer**（根据错误日志修替换）共同产生；二者都可能生成「不调用 `HAL_ETH_MspInit`」的 `HAL_ETH_Init` 或把 `HAL_ETH_MspInit` 替成空桩。

**Prompt 问题（已修正）：**

1. **Classifier**
   - no-stub 列表原先只有 `HAL_MspInit`（通用），没有 **`HAL_ETH_MspInit`** 和「任何会调 `HAL_NVIC_EnableIRQ` 的 `*_MspInit`」，导致 `HAL_ETH_MspInit` 被当成可 SKIP 的函数并生成空实现。
   - SKIP 的示例里曾写 **`HAL_UART_MspInit`**，模型容易类推到 `HAL_ETH_MspInit`，而 ETH MspInit 里包含 `HAL_NVIC_EnableIRQ(ETH_IRQn)`，不能 SKIP。
   - INIT 策略里未明确「**不得删除对 `*_MspInit` 的调用**」，替换 `HAL_ETH_Init` 时可能去掉对 `HAL_ETH_MspInit` 的调用。

2. **Fixer**
   - 同样的 no-stub 未包含 `HAL_ETH_MspInit` 和「含中断使能的 `*_MspInit`」，修错时也可能把这些函数修成空桩或删掉 MspInit 调用。

**已做修改（避免再犯）：**

- **`prompts/function_classifier.py`**：no-stub 列表加入 **`HAL_ETH_MspInit`** 与「任何含 `HAL_NVIC_EnableIRQ` 的 `*_MspInit`」；SKIP 示例去掉 `HAL_UART_MspInit`，并注明「会使能中断的 MspInit 不得标为 SKIP」；INIT 策略增加「**不得删除对 `*_MspInit` 的调用**，替换中须保留该调用或等价的中断使能」。
- **`prompts/function_fixer.py`**：同上 no-stub 扩展；INIT 例外中增加「不得在替换中删除对 `*_MspInit` 的调用」。
- **`tools/emulator/conf_generator.py`**：`RTOS_CRITICAL_INIT_FUNCS` 增加 **`HAL_ETH_MspInit`**，与其它不宜被桩的初始化函数一致。
