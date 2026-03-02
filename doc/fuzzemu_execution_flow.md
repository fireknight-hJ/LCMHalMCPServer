## LCMHalMCP 项目执行流程与 fuzzemu 联动机制

本文档梳理从固件 `main` 函数开始，到通过弱符号 `HAL_BE_*` 与 fuzzemu 工具联动、并在关键函数上注入行为的完整执行链路，便于后续维护和扩展。

---

### 1. 从固件 `main` 开始的执行路径

以 `testcases/zephyr_uart_official/src/main.c` 为代表，固件本身是一个「去掉 OS/框架依赖，仅保留 MMIO」的简化工程：

- `main` 中依次调用多个 UART/外设相关函数，例如：
  - `mmio_uart_init_direct`
  - `conditional_mmio_operation`
  - `mixed_uart_operation`
  - `loop_mmio_operation`
  - `struct_mmio_operation`
  - `complex_mmio_operation`
  - `mmio_uart_send_string_direct`
- 这些函数内部原始实现都是直接寄存器读写与轮询，例如：
  - `USARTx->CR1 = ...`
  - `while (!(USART1->SR & 0x0080)) { ... }`
  - `USART1->DR = data;`

在 LCMHalMCP 的自动化处理链路下，这些直接 MMIO 函数会被分析并替换，使其不再直接访问真实寄存器，而是统一通过 `HAL_BE_*` 系列钩子函数与 fuzzemu 交互。

---

### 2. 弱符号 `HAL_BE_*` 的定义与注入

#### 2.1 弱函数模板定义

`utils/src_ops.py` 中定义了一段统一的弱函数实现模板 `weak_funcdef`，核心内容类似：

- `int __attribute__((noinline, used, __weak__)) HAL_BE_return_0(void);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_return_1(void);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_Out(int len);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_In(void* buf, int len);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_ENET_ReadFrame(void* buf, int length);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Write(void* buf, int block_size, int block_num);`
- `int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Read(void* buf, int block_size, int block_num);`

这些弱函数具备以下属性：

- **`__weak`**：允许用户工程在别处定义同名强符号覆盖默认实现，避免冲突。
- **`used`**：即使编译器认为没有引用，也不会被优化掉，保证符号会出现在最终 ELF 中。
- **`noinline`**：禁止内联，确保每个 `HAL_BE_*` 都有独立的函数入口地址，便于 fuzzemu 在入口位置挂钩。

#### 2.2 源码替换与弱函数插入

源码修改的核心入口是 `utils/src_ops.py` 中的 `src_replace`：

1. 从指定的 `.c` 文件读取完整内容。
2. 如该文件尚未包含 `weak_funcdef` 串、且不是头文件（非 `.h`）：
   - 将整段 `weak_funcdef` 直接前插到文件顶部，注入所有 `HAL_BE_*` 的弱实现。
3. 将 CodeQL + LLM 分析得到的原函数实现 `old_code` 替换为新实现 `replace_code`。

调用链为：

- `tools/replacer/code_replacer.py` 中的 `function_replace(...)`：
  - 利用 `FunctionInfo` 拼出目标函数的完整代码文本 `old_code`。
  - 通过 `file_convert_proj2src` 将 DB 中的路径映射到真实源文件路径。
  - 调用 `src_replace(src_file, old_code, replacement_code)` 完成替换。

#### 2.3 关键 I/O 函数如何被改写

上游的 `agents/analyzer_agent.py` 会结合 MCP 工具（CodeQL collector）和大模型：

- 识别哪些函数是 MMIO/驱动相关函数。
- 将原始寄存器访问逻辑改写为对 `HAL_BE_*` 的调用，例如：
  - 原来通过轮询寄存器等待发送 FIFO 空 → 改写为直接调用 `HAL_BE_Out(len)`。
  - 原来从 UART/ETH 寄存器读取数据 → 改写为 `HAL_BE_In(buf, len)` 或 `HAL_BE_ENET_ReadFrame(buf, length)`。
  - 原来对 Flash/存储块读写 → 改写为 `HAL_BE_Block_Read/Write(...)`。
  - 仅需成功/失败返回值 → 使用 `HAL_BE_return_0()` / `HAL_BE_return_1()`。

**最终效果**：  
从 `main` 往下，所有关键外设操作不再直接访问硬件寄存器，而是统一“汇聚”到一小撮 `HAL_BE_*` 弱符号函数上。

---

### 3. fuzzemu 侧：从符号表到 Python handler

弱符号本身只是 C 里的一层“默认实现”，真实的行为注入发生在 fuzzemu 中。整个流程由 `tools/emulator` 模块驱动。

#### 3.1 执行入口：`emulate_proj` 与结果读取

`tools/emulator/core.py` 中，供上层调用的主要接口包括：

- `emulate_proj()`：直接运行一次模拟器，返回 `stdout/stderr/exit_code`。
- `mmio_function_emulate_info()`：确保有最新的模拟输出后，读取 `emulate/debug_output/lcmhal.txt`。
- `function_calls_emulate_info()`：读取并压缩 `emulate/debug_output/function.txt` 中的函数调用序列。
- `check_emulation_success()`：根据输出判断是否：
  - 出现异常循环（`exceptional loop`）。
  - 成功到达 `main()` 函数。
  - 存在其他错误。

上述函数都会通过 `ensure_emulator_output_exists()` 保证：

- 当 `output.elf` 较新，或调试输出文件缺失时，重新调用 `emulate_proj()` 重跑 fuzzemu。

#### 3.2 提取 ELF 符号：`extract_syms`

在 `conf_generator.extract_syms()` 中：

- 使用 `pyelftools` 打开 `emulate/output.elf`。
- 遍历所有符号表 section，将名字中不包含 `$` 的符号收集为 `{地址: 名称}`。
- 将结果写入 `emulate/syms.yml`：
  - 其中就包含了前面注入的所有 `HAL_BE_*` 函数符号。

这一步的意义：

- **保证 fuzzemu 可以通过 `syms.yml` 知道“某个地址对应 `HAL_BE_Out` / `HAL_BE_In` / …”**，为后续挂接 Python handler 提供基础。

#### 3.3 生成 fuzzemu 配置：`base_config.yml` 与 `semu_config.yml`

`tools/emulator/conf_generator.py` 中的关键流程：

1. `baseconfig_dict` 中预定义了 `output.elf` 对应的基础配置，包括：
   - `rules`、`emulate_mode`、`loop_whitelist` 等。
   - 最关键的是 `handlers` 字段：
     - `HAL_BE_ENET_ReadFrame` → `fuzzemu.handlers.common.hal_read_frame`
     - `HAL_BE_In`             → `fuzzemu.handlers.common.hal_in`
     - `HAL_BE_Out`            → `fuzzemu.handlers.common.hal_out`
     - `HAL_BE_return_0`       → `fuzzemu.handlers.common.return_zero`
     - `HAL_BE_return_1`       → `fuzzemu.handlers.common.return_true`
     - `HAL_BE_Block_Read`     → `fuzzemu.handlers.common.hal_block_in`
     - `HAL_BE_Block_Write`    → `fuzzemu.handlers.common.hal_block_out`
2. `mmio_funcs_emulate_config()`：
   - 从 CodeQL DB 中获取 MMIO 函数列表，写入 `baseconfig_dict['output.elf']["mmio_funcs"]`，为 fuzzemu 提供额外参考信息。
3. `generate_base_config()`：
   - 将 `baseconfig_dict` dump 为 `emulate/base_config.yml`。
4. `generate_semu_config()`：
   - 如有需要，生成 `base_config.yml`、`semu_rule.txt`、`base_input/input.bin`。
   - 调用外部命令：
     - `fuzzemu-helper config base_config.yml -s`
   - 在 `emulate/` 下生成最终的 `semu_config.yml` 和内存映射。
   - `fix_flash_size()` 再根据 `output.bin` 实际大小修正 `memory_map.flash` 的起始地址和大小，使其按 4KB 对齐。

到此为止，fuzzemu 已经：

- 知道 `output.elf` 中每个符号（包括所有 `HAL_BE_*`）对应的地址（来自 `syms.yml`）。
- 知道遇到特定函数名时该跳转到哪个 Python handler（来自 `handlers` 映射）。

#### 3.4 真正执行：`emulate_runner.run_emulator()`

`tools/emulator/emulate_runner.py` 中：

- 构造输入文件路径：
  - `emulate/base_input/input.bin`
  - `emulate/semu_config.yml`
- 通过 `subprocess.run` 调用：

  - `python -m fuzzemu.harness input.bin semu_config.yml -d 5 --skip-mmio-hook`
  - `cwd` 设为 `globs.script_path + "/emulate"`。

fuzzemu harness 的行为概要：

- 根据 `semu_config.yml` 和 `syms.yml`：
  - 装载 `output.elf` / `output.bin` 到 Unicorn 等模拟器中。
  - 配置内存映射、MMIO 区域和中断向量。
  - 在 ELF 入口（或配置的 entry_point）开始执行固件，即从 `main`（或启动代码）开始跑。
- 当固件执行到 `HAL_BE_*` 调用点时：
  - 并不执行 C 中的弱实现。
  - 而是根据 `handlers` 映射，跳转到对应的 Python 函数，例如：
    - `fuzzemu.handlers.common.hal_in`
    - `fuzzemu.handlers.common.hal_out`
    - `fuzzemu.handlers.common.hal_block_in`
    - `fuzzemu.handlers.common.hal_block_out`
    - `fuzzemu.handlers.common.return_zero/return_true`
- 这些 Python handler 负责：
  - 从 `input.bin` / fuzzer 输入中读取数据，填充到缓冲区。
  - 记录和检查输出行为。
  - 或者简化成固定返回值以保持执行向前推进。

运行结束后，fuzzemu 会将执行摘要和调用栈写入：

- `emulate/debug_output/lcmhal.txt`
- `emulate/debug_output/function.txt`

`core.py` 中的接口再对这些输出做格式化和压缩，供前端或其他组件展示。

---

### 4. 从 `main` 到 fuzzemu handler 的完整链路总结

从宏观角度看，项目通过以下步骤完成从固件到 fuzzemu 的联动，并在关键函数上注入行为：

1. **静态分析与分类**
   - 通过 MCP + CodeQL collector，结合 `agents/analyzer_agent.py` 和 LLM，对 DB 中的函数进行 MMIO/驱动分类。
2. **源码改写与弱函数注入**
   - 使用 `tools/replacer/code_replacer.py` + `utils/src_ops.py`：
     - 在每个相关 `.c` 文件顶部插入带 `__weak` / `used` / `noinline` 的 `HAL_BE_*` 默认实现。
     - 将原始 MMIO 函数实现改写为调用 `HAL_BE_*`，从而把所有关键 I/O 操作汇聚到少数几个统一的钩子函数上。
3. **符号与配置生成**
   - 编译得到 `emulate/output.elf` / `output.bin`。
   - `conf_generator.extract_syms()` 从 ELF 中提取所有符号，生成 `syms.yml`。
   - `generate_base_config()` / `generate_semu_config()` 生成 `base_config.yml` 和最终的 `semu_config.yml`：
     - 在 `handlers` 中把 `HAL_BE_*` 绑定到 `fuzzemu.handlers.common.*` 等 Python 实现。
4. **模拟执行与行为注入**
   - `emulate_runner.run_emulator()` 通过 `python -m fuzzemu.harness` 启动 fuzzemu。
   - 固件从启动入口（最终到达 `main`）正常执行。
   - 当执行到 `HAL_BE_*` 时，由 fuzzemu 将控制权切换到对应的 Python handler：
     - 从而在不依赖真实硬件的前提下，实现数据注入、行为模拟和输出观测。
5. **结果收集与诊断**
   - fuzzemu 输出调试信息与函数调用栈到 `debug_output` 目录。
   - `core.py` 提供 `mmio_function_emulate_info` / `function_calls_emulate_info` / `check_emulation_success` 等接口，对是否到达 `main`、是否存在异常循环等进行自动诊断。

通过以上链路，LCMHalMCP 将「静态分析 + 源码改写 + 模拟执行」有机结合起来，实现从 `main` 出发的可控、可观察、可 fuzz 的驱动执行环境。

---

### 6. RTOS 类 demo（如 FreeRTOS / LwIP StreamServer）的初始化注意

对带 RTOS 的固件（如 `LwIP_StreamingServer`），调度器启动前必须完成与 NVIC/SysTick 相关的初始化，且这些初始化会通过**写寄存器**被 fuzzemu 的 NVIC 钩子看到并更新内部状态。若这些函数被分析器**替换成不写寄存器的桩**，模拟器侧的 NVIC/SysTick 状态会保持默认或未配置，导致第一次上下文切换（如 PendSV 返回）时出现 HardFault（如 intno=3、pc=0）。

**不宜被替换为“纯桩”或必须保留对 NVIC/SysTick 写操作的关键初始化函数包括：**

- **HAL_InitTick**：配置 SysTick 周期并使能，供 OS tick 使用。若被替换为不写 `SYSTICK_LOAD` / `SYSTICK_CTRL` 等，fuzzemu 的 `deal_systick` 与 NVIC 状态会异常。
- **HAL_NVIC_SetPriority** / **HAL_NVIC_SetPriorityGrouping**：设置 PendSV、SysTick 等优先级。若被替换为不写 NVIC 优先级寄存器，`_find_pending` 等逻辑可能不符合 RTOS 预期。
- **SystemInit**（若其中设置 **VTOR**）：向量表基址必须正确，否则 `_enter_exception` 读到的 handler 地址会错。

**建议：**

- 在分析/替换策略中，将上述函数列为「RTOS 关键初始化」：要么不替换、保留原实现（让真实代码写 NVIC/SysTick 寄存器，由 fuzzemu 钩子处理），要么替换实现中仍通过写同一批寄存器或调用与 NVIC/SysTick 等价的逻辑，以保证模拟器 NVIC 状态与固件预期一致。
- 若出现「执行到 xPortStartScheduler 后立刻 HardFault / intno=3、pc=0」，优先排查上述初始化是否被错误替换或未执行到（如被 do_return 等跳过）。

---

### 7. LwIP_StreamingServer 关键初始化函数对比（ELF vs al_log 替换 vs 原始 HAL）

本节对 **当前固件 ELF 中实际指令**、**al_log 中记录的替换后源码**、以及 **原始 STM32 HAL 典型行为** 做对比，便于定位「是源码/替换问题还是固件本身问题」。

**说明**：以下反汇编基于 `testcases/server/stm32/LwIP_StreamingServer/emulate/output.elf`；替换内容来自 `lcmhal_ai_log/replacement_update_*.json`；原始 HAL 行为参考 ST 官方 `system_stm32f7xx.c` / `stm32f7xx_hal.c` 等。符号地址来自同目录 `syms.yml`（十进制转 Flash 地址：SystemInit 0x080031e0、HAL_InitTick 0x08001972、HAL_NVIC_SetPriorityGrouping 0x0800326e）。

#### 7.1 SystemInit

| 维度 | 内容 |
|------|------|
| **当前 ELF 反汇编** | 函数内有多条 MMIO 写：<br>• `r1=[0x8003220]` → SCB 基址 0xE000ED00；`[r1,#0x88]` 即 CPACR，`orr 0xf00000` 后写回（FPU 使能）。<br>• `r3=[0x8003224]` → RCC 基址 0x40023800；对 RCC->CR 置位 1（HSI）、RCC->CFGR=0、RCC->CR 清 HSEON/PLLON、RCC->PLLCFGR=0x24003010、RCC->CR 清 HSEBYP、RCC->CIR=0。<br>• **最后 `r3=0x08000000`，`str r3,[r1,#8]` → SCB->VTOR = 0x08000000**（向量表在 Flash）。<br>结论：**当前 ELF 中 SystemInit 仍是完整实现**（FPU + RCC + VTOR），并非空桩。<br><br>关键片段：<br><code>80031e0: ldr r1,[pc,#60]  ; SCB<br>...<br>8003216: mov.w r3,#0x08000000<br>800321a: str r3,[r1,#8]   ; SCB->VTOR<br>800321c: bx lr</code> |
| **al_log 替换说明** | `replacement_update_SystemInit_*.json` 中替换为「POSIX 兼容」：注释掉 FPU(CPACR)、RCC 全部写、以及 **VTOR 设置**（`SCB->VTOR = FLASH_BASE \| VECT_TAB_OFFSET`），函数体为空。若该替换被编译进当前 ELF，则不应出现上述 VTOR 写；当前 ELF 仍含 VTOR 写，说明此 ELF 可能未应用该次替换或来自未替换的构建。 |
| **原始 HAL 典型行为** | 在 `system_stm32f7xx.c` 中：① 配置 FPU（CPACR）；② 配置 RCC（HSI、CFGR、PLL 等）；③ **设置 VTOR**：`SCB->VTOR = FLASH_BASE \| VECT_TAB_OFFSET`（或 RAM 版本）。VTOR 必须正确，否则异常/中断时 CPU 取到的向量表地址错误，会导致 Handler 取到错误 PC（如 0）或未映射访问。 |

**VTOR 被错误移除时的影响**：若 SystemInit 的 VTOR 设置被替换/注释掉（例如「POSIX 兼容」替换中一并去掉 `SCB->VTOR = FLASH_BASE | VECT_TAB_OFFSET`），则复位后 VTOR 保持默认 0。发生异常/中断时，fuzzemu 与硬件会从 **VTOR + 4×异常号** 取 handler 地址；VTOR=0 时若 0x0 未映射或内容为 0，则取到 **PendSV_Handler = 0**，跳转后即 HardFault，或返回时恢复的 PC 异常。因此 **VTOR 被错误移除** 是导致 intno=3、pc=0 的常见原因之一，必须保留或等价设置。

**如何确认当前构建**：对 `output.elf` 执行 `objdump -d`，在 `SystemInit` 内查找对 **SCB (0xE000ED00)** 的 **偏移 #8** 的写（即 VTOR）。例如：`mov.w r3, #0x08000000` 与 `str r3, [r1, #8]`（r1 为 0xe000ed00）。当前仓库中该 ELF 含有上述 VTOR 写；若某次构建应用了移除 VTOR 的 SystemInit 替换，则需删除该替换或改为保留 VTOR 写后再建。

#### 7.2 HAL_InitTick

| 维度 | 内容 |
|------|------|
| **当前 ELF 反汇编** | 仅两条指令：`movs r0, #0`（返回值 HAL_OK）、`bx lr`。**无任何 NVIC/TIM6/SysTick 相关读写**。<br><br><code>08001972 &lt;HAL_InitTick&gt;:<br> 8001972: movs r0, #0<br> 8001974: bx lr</code> |
| **al_log 替换说明** | `replacement_update_HAL_InitTick_*.json`：替换为「POSIX 兼容」，跳过所有硬件操作（NVIC 配置、TIM6 使能、HAL_TIM_Base_Init/Start_IT 等），直接 `return HAL_OK`。与当前 ELF 一致。 |
| **原始 HAL 典型行为** | 在 `stm32f7xx_hal.c` 中：配置 SysTick 周期（通常 1ms）、设置 SysTick 优先级（`HAL_NVIC_SetPriority(SysTick_IRQn, ...)`）、使能 SysTick 中断；部分实现用 TIM6 作 tick 源时还会配置 RCC、TIM6 并启动定时器中断。这些会写入 NVIC/SYSTICK（或 TIM6）相关寄存器，fuzzemu 的 NVIC 钩子依赖这些写来更新内部状态。 |

**小结**：**当前 ELF 中 HAL_InitTick 已是纯桩**，不写 SysTick/NVIC，导致 fuzzemu 侧 tick 与优先级状态未初始化，与「xPortStartScheduler 后首次切换即 HardFault」现象吻合。

#### 7.3 HAL_NVIC_SetPriorityGrouping（及 HAL_NVIC_SetPriority / HAL_NVIC_EnableIRQ）

| 维度 | 内容 |
|------|------|
| **当前 ELF 反汇编** | `HAL_NVIC_SetPriorityGrouping`：仅 `bx lr`。<br>紧随其后的 `HAL_NVIC_SetPriority`、`HAL_NVIC_EnableIRQ` 同样仅 `bx lr`，无寄存器写。 |
| **al_log 替换说明** | session 日志中这些函数被替换为「不写硬件」的桩，与 ELF 一致。 |
| **原始 HAL 典型行为** | `HAL_NVIC_SetPriorityGrouping` 写 **SCB->AIRCR**（优先级分组）；`HAL_NVIC_SetPriority` 写 **NVIC->IPR[]**；`HAL_NVIC_EnableIRQ` 写 **NVIC->ISER[]**。FreeRTOS 启动前会设置 PendSV、SysTick 等优先级，若这些写被去掉，NVIC 内部状态与 RTOS 预期不一致，首次 PendSV 或 tick 时行为可能异常。 |

**小结**：**当前 ELF 中 NVIC 相关调用均为空桩**，与 HAL_InitTick 一起导致「调度相关 NVIC/SysTick 未配置」，是 RTOS 首次切换崩溃的重要成因。

#### 7.4 对比结论（与本 demo 的关系）

- **若 output.elf 中上述函数仍为空桩**：SystemInit 可能完整（含 VTOR），但 HAL_InitTick、HAL_NVIC_SetPriorityGrouping/SetPriority/EnableIRQ 仅为 `bx lr`/`movs r0,#0; bx lr`，则 **SysTick 与 NVIC 优先级/使能未写入**，fuzzemu 的 NVIC 状态与固件预期不一致，首次 PendSV 返回时出现 HardFault（intno=3、pc=0）可由此解释。
- **若已按第 6 节修复并重新构建**：当前仓库中的 `output.elf` 经 `arm-none-eabi-objdump -d` 确认，**HAL_InitTick** 已为完整实现（含 `bl HAL_NVIC_SetPriority`、`bl HAL_NVIC_EnableIRQ` 以及对 SysTick 相关地址的 `str`）；**HAL_NVIC_SetPriorityGrouping** 已含对 SCB 的 `ldr`/`bic`/`orr` 等写操作。此时「前面没初始化好」的根因可能已消除；若仍崩溃，需确认本次运行的 ELF 是否就是该版本，并参考下文「调度前初始化链」与 §8 继续排查。
- **修复方向**：对 RTOS 关键初始化函数（见第 6 节列表）不做「纯 return 型」替换，或替换时保留对 SCB->VTOR、NVIC、SysTick 的等价写，以保证模拟器状态与固件一致。

#### 7.5 调度前初始化链（为何调度这块出问题）

从复位到首次上下文切换，**必须完成的初始化**及典型调用顺序如下；任一步被桩掉且不写寄存器，fuzzemu 侧都会处于未配置状态，可能导致首次 PendSV 返回异常。

| 阶段 | 函数/动作 | 作用 | 若被桩掉的后果 |
|------|------------|------|----------------|
| 启动 | **SystemInit** | 写 VTOR、RCC、CPACR | 向量表地址错误或未设置 |
| main 内 | **HAL_Init** | 调用下列 NVIC/Tick 初始化 | 后续都不执行则 NVIC/Tick 全未配置 |
| ↑ | **HAL_NVIC_SetPriorityGrouping** | 写 SCB->AIRCR（优先级分组） | 优先级分组为默认，可能影响 PendSV 选择 |
| ↑ | **HAL_InitTick** | 写 SysTick 周期/使能，并调用 SetPriority(SysTick)、EnableIRQ(SysTick) | fuzzemu 的 SysTick 与 NVIC 状态未更新 |
| ↑ | **HAL_NVIC_SetPriority** / **HAL_NVIC_EnableIRQ** | 写 NVIC->IPR[]、ISER[] | PendSV/SysTick 等优先级与使能未设置 |
| 调度器启动前 | Port 层（如 **vPortValidateInterruptPriority** / **vPortSetupTimerInterrupt**） | 常再次写 PendSV、SVC、SysTick 优先级 | 若被桩掉，仅依赖 HAL_Init 的写；若 HAL 已桩则完全未配置 |
| 首次切换 | **xPortStartScheduler** → 触发 **PendSV** → 异常返回 | 从当前栈弹回 PC/LR 等 | 若弹栈用错栈（见 §8）或栈上帧本身 PC=0，则 pc=0 → HardFault |

**排查建议**：

1. **确认当前 ELF**：对 `emulate/output.elf` 执行 `objdump -d`，看 HAL_InitTick、HAL_NVIC_SetPriorityGrouping、HAL_NVIC_SetPriority 是否为多指令实现（含 `bl`、`str`/`ldr` 到 MMIO），而非单条 `bx lr`。
2. **确认本次 run 使用的就是该 ELF**：若 `debug_output/stderr.txt`、`function.txt` 来自**未重新 build** 的一次 run，则可能当时 ELF 仍是桩版本；用当前 ELF 再跑一次 `main.py run --config ...`，看是否仍出现 intno=3、pc=0。
3. **若 ELF 已是完整实现且重跑仍崩溃**：则更可能是（a）首次 PendSV 返回时使用的栈与 nvic 弹栈使用的栈不一致（见 §8.0.2），或（b）首任务栈帧在创建时被写成 PC=0（如 pxPortInitialiseStack 或 TCB 相关逻辑受替换影响）。可尝试在崩溃点 dump PSP、MSP 及两栈顶 32 字节，对比哪边是合法异常帧。

#### 7.6 fatfs 用例：SysTick_Config 被桩导致无 tick（2026-02 检查结果）

**现象**：RT-Thread fatfs 用例仿真能进 `main`（function.txt 可见 `main` → `rt_thread_create`），但随后停在 `idle_thread_entry`，被 exceptional loop 检测结束；`debug.txt` 中无 `[SysTick_Handler]` 调用。

**检查结果**：

| 函数 | 当前 output.elf 反汇编 | 说明 |
|------|------------------------|------|
| **HAL_InitTick** | `bl rt_hw_systick_init` + `movs r0,#0` + `bx lr` | 未用「纯 return HAL_OK」桩，仍调 RT-Thread 的 `rt_hw_systick_init`。 |
| **rt_hw_systick_init** | 调 `SystemCoreClockUpdate`、`HAL_SYSTICK_Config`、`__NVIC_SetPriority` 等 | 正常，会调到 `SysTick_Config`。 |
| **SysTick_Config** | 仅参数检查（`ticks-1`、`cmp 0x1000000`）+ `mov r0, r3` + `bx lr`，**无任何对 0xE000E010/14/18 的写** | 已被替换为「仿真用桩」：只返回 0/1，不写 SysTick 寄存器。 |
| **SysTick_Handler** | 完整：`rt_interrupt_enter` → `HAL_IncTick` → `rt_tick_increase` → `rt_interrupt_leave` | 未被桩；若被调用会正常推进 tick。 |

**根因**：fuzzemu 的 SysTick 使能依赖**固件对 SysTick 寄存器的写**（见 `nvic.py` 中 `_handler_nvic_regs_rw`：只有在对 SYSTICK_CTRL/LOAD/VAL 写时才调用 `deal_with_systick_regs` 更新 `nvic.systick`）。`SysTick_Config` 被替换为不写寄存器的桩后，fuzzemu 侧 `enable_systick` 始终为 false，`deal_systick()` 每 block 直接 return，从不 pend SysTick 中断，故 `SysTick_Handler` 从未被调用，调度器无 tick，一直停在 idle。

**修复方向**：对 **SysTick_Config** 的替换需**保留对 SysTick 寄存器的写**（或等价地让 fuzzemu 认为 SysTick 已配置），例如在替换体中写 `*(volatile uint32_t*)0xE000E014 = ticks-1` 与 `*(volatile uint32_t*)0xE000E010 = 7` 等，使 fuzzemu 的 MMIO 钩子执行 `deal_with_systick_regs`，从而打开 `nvic.enable_systick`，后续 block 钩子才会在 `deal_systick()` 里周期 pend SysTick，进而进入 `SysTick_Handler` 推进 `rt_tick_increase()`。

### 8. 首次调度切换 HardFault（intno=3, pc=0）— 可能成因

#### 8.0 现象与 lr 对照

- **现象**：执行到 `xPortStartScheduler` 后立刻崩溃，`stderr.txt` 为 `[-] NVIC INTR unhandled: intno=3 pc=0x0 lr=0x800548b`。
- **lr=0x800548b** 对应 **osKernelStart** 中 `vTaskStartScheduler()` 返回后的下一条指令（`movs r0, #0`），说明逻辑上应从 PendSV 返回到该处，但实际恢复的 **PC=0**，导致取指 0 触发 HardFault。

#### 8.0.1 若 NVIC 已在其他 demo 验证（MSP/PSP 换栈正常）

则不应优先假定 nvic 弹栈有误，而应在本 demo 侧排查：

- **栈上被恢复的上下文本身是否就带有 PC=0**  
  第一次上下文切换时，恢复的是「被调度到的任务」的栈帧。若该任务的**初始上下文**在创建时就被写成 PC=0（例如任务入口/函数指针未正确写入、或某处 stub/替换导致初始化不完整），则无论从 MSP 还是 PSP 弹栈，恢复出的 PC 都会是 0。可排查：
  - 本 demo 的 FreeRTOS 任务创建（如 `xTaskCreate`）是否被替换/跳过，或任务栈初始化的布局是否与预期一致；
  - 本构建中是否有 HAL/RTOS 相关初始化被替换成空桩，导致与「已在其他 demo 验证」的环境不一致（见第 6、7 节）。
- **本 demo 的 VTOR / 向量表 / 内存布局**  
  若向量表或 RAM 布局与其它已验证 demo 不同，也可能导致第一次切换时用的栈或帧地址异常，从而出现“恢复出 0”的现象。

#### 8.0.2 若仍怀疑 NVIC 侧（仅作参考）

Cortex-M 从 Thread（PSP）进异常时现场压在 **PSP**，返回时应从 **PSP** 弹栈。若在其它 demo 中 NVIC 未改过且调度正常，则通常说明当前 nvic 的 MSP/PSP 处理已正确；若将来在**未改 NVIC** 的同一套代码下仍出现仅本 demo pc=0，则更应优先从上述「栈上上下文内容」与「本 demo 初始化/替换差异」排查。

---

### 9. UNMAPPED Mem Read at 0x0 与 isr_vector 的位置

#### 9.1 现象

模拟器 stdout 出现：`[-] UNMAPPED Mem Read: addr= 0x0000000000000000 size=4`，随后退出。

#### 9.2 isr_vector 到底在哪里（概念澄清）

- **向量表在固件里的位置**：在 RTOS/嵌入式镜像里，向量表（初始 SP、Reset 向量、各异常入口）在 **linker 里通常放在 flash 的起始**，即 ELF 中 **0x08000000**（Flash 基址）。也就是说：**isr_vector 的“内容”在镜像里 = flash 开头**，不是“在 0x0 地址”。`.isr_vector` 段在 ld 里一般放在 `FLASH` 最前面，所以 bin 文件开头就是向量表。
- **0x0 是什么**：Cortex-M 里 VTOR 复位后为 0，所以**硬件**取向量时用的“逻辑地址”是 0x0/0x4。在**真实 STM32** 上，0x0 往往通过芯片的 **remap** 指向 flash 开头（即 0x0 和 0x08000000 看到同一块内容），所以“读 0x0”实际读到的是 flash 开头的向量表。**并不是**在镜像里再放一份“0x0 处的向量表”。
- **semu 配置里的含义**：`semu_config.yml` 里 `initial_sp`、`entry_point` 已显式给出，模拟器很可能**直接用这两项**做初始 SP/PC，而**不**从内存读 0x0。顶层的 `isr_vector: 0x0` 多半表示“向量表逻辑地址是 0x0”（VTOR 的默认），和“向量表内容在 flash 开头”不矛盾。

#### 9.3 UNMAPPED at 0x0 可能来自哪里

- **若模拟器启动时不读 0x0**（用 config 的 initial_sp/entry_point）：那么对 0x0 的读一定来自**某条指令**，例如：
  - 未初始化的结构体里的**指针为 NULL**，后面 `*ptr` 或 `ptr->xxx` 导致读 0x0；
  - 函数指针、回调、设备句柄等未赋值就使用。
  这类情况更符合“结构体/指针未初始化”的假设，需要根据**发生 0x0 读时的 PC** 反查是哪个函数、哪块结构体。
- **若模拟器启动时确实按 Cortex-M 从 0x0 取向量**：则需要在 memory_map 里把 0x0 映射到**和 flash 开头相同的内容**（即向量表在镜像里还是在 flash 开头，只是多映射一份到 0x0）。是否如此需看 fuzzemu/semu 的启动实现。

#### 9.4 本 demo 的 debug 信息

- debug 里第一条是 `[Reset_Handler]` 在 `pc=0x08014bd8` 时 **Read: addr= 0x08014c10**（在 flash 里），读到的 data=0x20000874（即 initial_sp）。说明**这条固件**里，Reset_Handler 第一条指令是从 **0x08014c10** 取 SP，而不是从 0x0。向量表在这份 ELF 里是放在 0x08014c10 附近（flash 内一段），不是 0x08000000 也不是 0x0。若要在 0x0 做映射，应映射的是**实际向量表所在的那段 flash 内容**（对应 ELF 里 0x08014c10 起的一段），不能简单用 output.bin 的 file offset 0。

#### 9.5 建议的排查步骤

1. **确认 0x0 读发生的时机**：若 stdout 在“skip mmio hook”后立刻报 UNMAPPED，且 debug 几乎没有日志，则可能是模拟器启动时读 0x0；若 debug 已有大量执行（如已跑完 CopyDataInit/FillZerobss 等），则 0x0 读更可能是**后续业务/驱动代码**里的空指针访问。
2. **若判定为“业务/驱动里读 0x0”**：需要拿到**触发该读的 PC**（若模拟器或 harness 能打出 PC），再用 syms/ELF 反查函数与源码，重点查该函数内未初始化的指针、结构体成员、回调等。
3. **isr_vector 的结论**：向量表**内容**在固件里 = **flash 开头**（或本构建里 0x08014c10 这类 flash 内地址）；**0x0** 只是 VTOR=0 时的取指/取向量地址，真实设备上常通过 remap 指向同一块 flash。修复 UNMAPPED 时需先分清是“启动时从 0x0 取向量”还是“运行中某条指令读 0x0”，再决定是改 memory_map 还是改代码/初始化。

#### 9.6 本 demo debug 日志的卡点与“读 0x0”的指令分析（stm32f401 rtthread base）

- **卡点（最后一条日志对应的执行位置）**  
  - debug.txt 共约 80375 行，最后出现的是：`[FillZerobss] Basic Block: addr= 0x08014bfe`、`>>> Write: ... pc=0x08014bfe`、`Basic Block: addr= 0x08014c00 , size=6`。  
  - 即最后执行到的**固件指令**在块 **0x08014c00**（FillZerobss/LoopFillZerobss 循环内），块内指令为：  
    - `0x08014c00`: `adds r2, #4`  
    - `0x08014c02`: `cmp r2, r4`  
    - `0x08014c04`: `bcc.n 0x08014bfe`（若 r2 < r4 则继续循环）  
  - 循环退出后下一条指令为 **0x08014c06**: `bl __libc_init_array`，随后 0x08014c0a `bl entry`，进入 `entry` → `rtthread_startup` → `rt_hw_interrupt_disable` → `rt_hw_board_init`（HAL_Init、SystemClock_Config、rt_system_heap_init、rt_hw_pin_init、rt_hw_usart_init、rt_console_set_device、rt_components_board_init）等。  
  - debug 中**没有任何** `Read: addr= 0x0` 的记录，说明对 0x0 的访问发生在某条指令执行时，且该次访问未被记入 log（通常为随后一次取指或数据访问）。

- **“读 0x0”对应的实际行为**  
  - UNMAPPED 报的是 **Mem Read addr=0x0 size=4**。可能有两种情况：  
    1. **数据读**：某条 `LDR`/`LDRB` 等从 `[Rn]` 读，且 Rn=0。  
    2. **取指**：某条 **BLX rn**（或 BX）用 rn=0 作为目标地址，CPU 到 0x0 取指令，模拟器把这次取指报成“从 0x0 读 4 字节”。  
  - 在启动链里，**通过函数指针调用**非常常见（如 `rt_components_board_init` / `rt_components_init` 里 `ldr r3,[r3,#0]` + `blx r3`）。若表中或结构体里某个**函数指针为 0**，就会发生 **blx 0**，随后在 0x0 取指 → 触发对 0x0 的“读”。  
  - 因此，“到底是读哪个数据读出的 0x00”更准确的说法是：**不是“某次数据读读到了数值 0”**，而是**用作调用目标的“数据”（函数指针）为 0**，导致**跳转到 0x0 后的取指**触发了对 0x0 的读。

- **ELF 上已核对的启动路径**  
  - `__libc_init_array`（0x080019b0）：空实现，直接返回。  
  - `entry` → `rtthread_startup` → `rt_hw_board_init`：依次调用 HAL_Init、SystemClock_Config、rt_system_heap_init、rt_hw_pin_init、rt_hw_usart_init、rt_console_set_device、**rt_components_board_init**、**rt_components_init**。  
  - `rt_components_board_init`（0x0801b14c）：从表 **0x0802734c..0x08027350** 取函数指针并 `blx r3`。表中内容在 ELF 中为有效指针（如 0x0801b11b），**不是 0**。  
  - `rt_components_init`（0x0801b180）：从表 **0x08027350..0x0802735c** 取指针并 `blx r3`，表中为 lwip_system_init、finsh_system_init 等，**也不是 0**。  
  因此，若 0x0 来自“函数指针调用”，更可能出现在 **rt_hw_board_init 所调用的某一层**里（例如某个设备/驱动的 ops 或 init 回调来自未初始化的结构体），而不是上述两个 init 表本身。

- **结论与建议**  
  - **执行卡点**：debug 显示最后执行到 **0x08014c00**（FillZerobss 循环），下一次会执行 0x08014c06 起的 `__libc_init_array` → `entry` → … → `rt_hw_board_init` 及其子调用。  
  - **读 0x0 的成因**：很大概率是**某次通过函数指针调用（blx）时目标为 0**，导致在 0x0 取指被报成 UNMAPPED Mem Read；即“读出的 0x00”指的是**作为跳转目标的函数指针值为 0**，而非某次数据负载读到 0。  
  - **精确定位**：需要在模拟器/harness 在报 UNMAPPED 时**同时打出 fault 时的 PC**（以及可选的 lr），再用 syms/ELF 反汇编该 PC 附近的指令，看是否为 `blx rn`/`bx rn` 或 `ldr pc,[rn]`，并反推是哪个结构体/表项的函数指针未初始化。  
  - **代码侧排查**：在 `rt_hw_board_init` 调用链中重点检查：控制台设备、串口设备、pin 等驱动的 **ops 或 init 回调**是否依赖在 BSS/未初始化内存中的结构体，其函数指针是否可能为 0。

#### 9.7 澄清：不是 FillZerobss 的“写”导致 0x0 UNMAPPED；责任归属

- **报错类型**：stdout 明确是 **UNMAPPED Mem Read: addr=0x0**，是**读**，不是写。
- **FillZerobss 在做什么**：  
  - 反汇编可见：BSS 起止来自 `0x08014c20`/`0x08014c24` 的常量，即 **r2=0x20000878、r4=0x2000b838**（RAM 里的 BSS）。  
  - 循环里只有 **`str r3, [r2, #0]`**（写 0 到 [r2]），然后 `adds r2, #4`。即写的是 **0x20000878～0x2000b838** 这段 RAM，**不会写 0x0**。  
  - 所以“要写 0 初始化的地址根本没有开辟映射”**不能**解释成 FillZerobss 在写 0x0：它写的区间是已映射的 RAM，且固件里 BSS 起止也不是 0。
- **是否“初次运行 FillZerobss 就遇到”**：  
  - 若指**同一次 run**：debug 里已有大量 FillZerobss 的 Write（0x20000878 起），说明零初始化循环已跑了很多次；UNMAPPED 出现在**之后**某次对 0x0 的**读**（取指或 LDR），不是 FillZerobss 的某次写触发的。  
  - 若指**另一次 run**（例如几乎没有 log、一启动就崩）：那可能是模拟器在**第一条指令之前**从 0x0 读初始 SP/向量，0x0 未映射 → 属于“0x0 这块地址本该开辟但是没有”。
- **责任归属（谁的原因）**  
  - **“0x0 这块地址本该开辟但是没有”**：若对 0x0 的读发生在**启动瞬间**（模拟器按 Cortex-M 从 0x0 取 SP/向量），则 0x0 在 memory_map 里**应该被映射**（例如映射成与 flash 开头相同内容的向量表），没映射就是**模拟器/配置**的责任，应在 semu 的 memory_map 里为 0x0 开辟映射。  
  - **“地址错了不该是 0x00”**：若对 0x0 的读发生在**运行中**（某条指令 LDR [r0] 且 r0=0，或 blx 0），则**不该**去访问 0，是**固件/数据**的问题（例如未初始化的函数指针、空指针解引用），应在代码/初始化上修，而不是去映射 0x0。  
  - 总结：**该不该访问 0** 在固件侧；**0x0 该不该被映射**在模拟器/配置侧。先根据“何时发生 0x0 读”（启动瞬间 vs 跑了一段后）判断属于哪一种，再决定是改 memory_map 还是改固件/初始化。

#### 9.9 实测 fault PC/LR 定位（stm32f401 rtthread base，带 PC/LR 输出的一次 run）

- **stdout 中的 fault 信息**（用户增加输出后）：  
  `fault PC: 0x08000268`，`LR (caller): 0x0801e7d9`。

- **触发 0x0 读的指令**（反汇编 output.elf）：  
  - **0x08000268**: `ldr r0, [r0, #0]`  
  即：以 r0 为基址、偏移 0 做一次 load。执行时 **r0=0**，因此实际访问的是 **0x0**，触发 UNMAPPED Mem Read。

- **所在函数与上下文**：  
  - 该指令属于 **rt_hw_context_switch_to**（0x0800022e 起）。  
  - 前序指令（反汇编常量池 0x80002f0 处为 **0xe000ed08 = SCB->VTOR**）：  
    - 0x8000264 `ldr r0, [pc, #136]` → r0 = **VTOR 寄存器地址** (0xe000ed08)  
    - 0x8000266 `ldr r0, [r0, #0]` → r0 = **VTOR 的值**（向量表基址；若未设置则为 0）  
    - 0x8000268 `ldr r0, [r0, #0]` → r0 = 向量表首字（初始 SP）；若上一步 r0=0，则从 **0x0** 读 → UNMAPPED。  
  - 即：本实现用 **VTOR → [VTOR]（向量表首字）** 作为首次切换时的初始 MSP。若 **VTOR 未被写入**（仍为 0），就会对 0x0 做数据读。

- **调用者**：  
  - LR 0x0801e7d9 对应 **rt_system_scheduler_start** 内 0x801e7d4 的 `bl rt_hw_context_switch_to`。  
  - 即：调度器启动时调用 `rt_hw_context_switch_to`，其内部通过 VTOR 取“向量表首字”作初始 SP；VTOR=0 导致读 [0]。

- **结论**：  
  - **读 0x0 的指令**：**0x08000268** 的 `ldr r0, [r0, #0]`（数据读）。  
  - **根因**：**VTOR 未被设置**（通常由 **SystemInit** 在启动时写入）。若 SystemInit 被替换成不写 VTOR 的桩，VTOR 保持 0，rt_hw_context_switch_to 按 VTOR → [VTOR] 取初始 SP 时就会读 [0]。  
  - **修复方向**：不要替换 **SystemInit**（或替换时保留对 SCB->VTOR 的写入）。`conf_generator.RTOS_CRITICAL_INIT_FUNCS` 与 `tools/builder/core._skip_replacement_critical_init` 已包含 SystemInit，若当前 ELF 仍是“被替换后的 SystemInit”，需确认构建流水线中确实启用了该 skip。

#### 9.10 从 Reset_Handler 到 rt_system_scheduler_start 的调用顺序与“是否被替换”

以下为 **stm32f401-st-nucleo base** 上从 Reset_Handler 执行开始、到崩溃点 rt_hw_context_switch_to 的**顺序调用表**。  
“被替换？”列：**Y** = 若走“可替换列表”且未跳过则会被替换（当前 ELF 中该函数已是桩）；**N** = 不在替换列表或属 RTOS 关键初始化被跳过；**-** = 汇编/启动内联，不参与替换。

| 序号 | 函数名 | 调用来自 | 被替换？ | 说明 |
|-----|--------|----------|----------|------|
| 1 | Reset_Handler | 向量表/上电 | - | 启动入口 |
| 2 | **SystemInit** | Reset_Handler | **Y（当前 ELF 已为桩）** | 应设置 VTOR/时钟等；桩不写 VTOR → VTOR=0 → 后续读 [0] |
| 3 | LoopCopyDataInit | Reset_Handler | - | 拷贝 .data |
| 4 | LoopFillZerobss | Reset_Handler | - | 清零 .bss |
| 5 | __libc_init_array | Reset_Handler | - | 本构建为空 |
| 6 | entry | __libc_init_array 返回后 | - | C 入口 |
| 7 | rtthread_startup | entry | N | RTOS 启动 |
| 8 | rt_hw_interrupt_disable | rtthread_startup | N | 关中断 |
| 9 | rt_hw_board_init | rtthread_startup | N | 板级初始化 |
| 10 | **HAL_Init** | rt_hw_board_init | **Y（当前 ELF 已为桩）** | 若被桩掉，HAL 状态/NVIC 等可能未设，通常不直接导致 0x0 读 |
| 11 | **SystemClock_Config** | rt_hw_board_init | 关键初始化应跳过 | 若被替换且未跳过，只影响时钟，不直接导致本 crash |
| 12 | rt_system_heap_init | rt_hw_board_init | N | 堆初始化 |
| 13 | **rt_hw_pin_init** | rt_hw_board_init | Y（在 24 个替换名单） | GPIO 初始化，不直接导致 VTOR/0x0 |
| 14 | rt_hw_usart_init | rt_hw_board_init | N | 串口初始化 |
| 15 | rt_console_set_device | rt_hw_board_init | N | 控制台设备 |
| 16 | rt_components_board_init | rt_hw_board_init | N | 组件板级初始化 |
| 17 | rt_show_version | rtthread_startup | N | 版本打印 |
| 18 | rt_system_timer_init | rtthread_startup | N | 系统定时器 |
| 19 | rt_system_scheduler_init | rtthread_startup | N | 调度器初始化 |
| 20 | rt_application_init | rtthread_startup | N | 创建 main 线程等 |
| 21 | rt_system_timer_thread_init | rtthread_startup | N | 定时器线程 |
| 22 | rt_thread_idle_init | rtthread_startup | N | 空闲线程 |
| 23 | rt_thread_defunct_init | rtthread_startup | N |  defunct 初始化 |
| 24 | rt_system_scheduler_start | rtthread_startup | N | 启动调度 |
| 25 | **rt_hw_context_switch_to** | rt_system_scheduler_start | N | 用 VTOR→[VTOR] 取初始 SP；VTOR=0 → 读 [0] 崩溃 |

- **是否可能是“某些函数被错误替换”导致**：**是**。  
  - **直接原因**：**SystemInit** 被替换成不写 VTOR 的桩。Reset_Handler 最早调用 SystemInit（序号 2），若此处未写 VTOR，后续 rt_hw_context_switch_to（序号 25）按 VTOR 取向量表首字作初始 SP 时就会读 [0]。  
  - **建议**：确保 SystemInit 在流水线中**不被替换**（已列入 `RTOS_CRITICAL_INIT_FUNCS`，需确认 builder 的 replace 阶段确实执行了 `_skip_replacement_critical_init`）；若当前 ELF 是旧构建，用“不替换 SystemInit”的配置重新构建并再测。
- **清除旧的 Classifier / ReplacementUpdate**：之前若对 SystemInit 做过 FunctionClassifier 或 ReplacementUpdate，这些结果会以 `function_classify_SystemInit_*.json`、`replacement_update_SystemInit_*.json` 形式存在，后续 `init_builder` / `replace_funcs` 会加载并参与替换逻辑。应一次性清除两类日志并恢复源码，再重跑：
  - `python main.py clean <script_path> --func-name SystemInit --type all --recover`
  - `--type all` 会删除该函数的 replacement_update、function_classify、function_analysis 三类日志；`--recover` 会从 DB 恢复该函数所在源文件。

