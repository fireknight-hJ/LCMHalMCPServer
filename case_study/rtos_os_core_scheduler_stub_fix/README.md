## RTOS 调度核心函数被桩化 + NVIC 异常返回导致首任务启动失败案例

### 1. 问题背景（与 SystemInit 案例的区别）

这是独立于 `rtos_nvic_init_stub_fix` 的**第二个 RTOS 调度问题案例**。

- Demo：`testcases/server/stm32/LwIP_StreamingServer/`（FreeRTOS + LwIP）
- 现象（在已修好 SystemInit / HAL_InitTick / HAL_NVIC\_* 之后）：
  - `emulate/debug_output/stderr.txt` 中出现：`[-] NVIC INTR unhandled: intno=3 pc=0x0 lr=0x80055xx`（HardFault，pc=0）
  - `function.txt` 显示已执行到：`main -> HAL_Init(...) -> osKernelStart -> vTaskStartScheduler -> xTaskCreate -> pxPortInitialiseStack -> xPortStartScheduler`
  - `lcmhal.txt` 较短，在**首任务切换阶段**就退出。
  - `debug.txt` 尾部显示 NVIC 在返回时从 0x20080000 一带读“任务栈帧”，数据全是 0，恢复出 `pc=0`。

与 `rtos_nvic_init_stub_fix` 不同之处在于：这里 **SystemInit / HAL_InitTick / HAL_NVIC\_* 初始化已经是正确实现**，VTOR/NVIC/SysTick 都正常，问题来自 **FreeRTOS 端口层的 OS 调度核心函数被桩化，以及 NVIC 异常返回对 PSP/MSP 的处理不完善**。

---

### 2. 现象与关键信息

#### 2.1 调度入口已被正常执行

从 `function.txt` 可以看到完整的启动和调度入口链路：

- `Reset_Handler -> LoopCopyDataInit -> CopyDataInit -> SystemInit -> __libc_init_array -> main`
- `main -> HAL_MPU_* -> HAL_Init -> HAL_NVIC_SetPriorityGrouping -> HAL_InitTick -> HAL_NVIC_SetPriority/EnableIRQ -> HAL_RCC_* -> BSP_* init ...`
- `main -> osKernelStart -> vTaskStartScheduler -> xTaskCreate -> pxPortInitialiseStack -> vPortEnterCritical / vPortExitCritical -> xPortStartScheduler`

说明：

- HAL 层（SystemInit / HAL_InitTick / HAL_NVIC\_* / SystemClock_Config）初始化已经按预期执行；
- FreeRTOS 调度器也已经进入 `vTaskStartScheduler`，并通过 `xTaskCreate` 调用了 `pxPortInitialiseStack` 为首任务准备栈帧。

#### 2.2 debug.txt 中的关键内存访问

`debug.txt` 显示：

- 在 `pxPortInitialiseStack` 中，首任务的异常帧被写入 **0x20016e44–0x20016e64** 一带（PSP 任务栈区域）：
  - 写入 xPSR = 0x01000000
  - 写入任务入口 PC（例如 0x08000870）
  - 写入 LR（prvTaskExitError 的地址）
  - 写入 EXC_RETURN = 0xFFFFFFFD 等
- 在 `osKernelStart`/`vTaskStartScheduler` 返回路径上，NVIC 异常返回时：
  - 从 **0x2007ff9x / 0x20080000**（MSP 顶）读取“任务栈帧”，数据全部是 0；
  - 最终恢复出的 PC=0，触发 `UC_ERR_READ_UNMAPPED (pc=0)`；崩溃时寄存器快照中：
    - `msp ≈ 0x20080008`
    - `psp = 0x0`
    - `r1 = 0x20016e7c`（指向 TCB/任务栈相关结构）

这说明：**首任务的 PSP 栈帧已经准备好，但 PSP 本身一直是 0，NVIC 退出异常时依然从 MSP 顶部弹栈，把一坨 0 当作任务帧，导致 PC=0。**

---

### 3. 根本原因分析

#### 3.1 阶段一已经解决：NVIC/SysTick/VTOR 初始化问题

前一案例 `rtos_nvic_init_stub_fix` 已经说明并修复：

- `SystemInit` / `HAL_InitTick` / `HAL_NVIC_SetPriorityGrouping` / `HAL_NVIC_SetPriority` / `HAL_NVIC_EnableIRQ` 等被误桩化为不写 VTOR/NVIC/SysTick 的空函数，会直接导致首次 PendSV 返回时异常。
- 通过：
  - 删除错误替换日志（`replacement_update_SystemInit_*`, `replacement_update_HAL_InitTick_*`, `replacement_update_HAL_NVIC_*`）；
  - 修改 `function_fixer.py` / `function_classifier.py` 的 prompt，禁止对这些函数做空桩替换；
  - 更新 `conf_generator.py` 中的 `RTOS_CRITICAL_INIT_FUNCS`；
- 该阶段的问题已经修复，`output.elf` 里 HAL 初始化逻辑是完整的：可以在 SystemInit 中看到对 SCB->VTOR 的写，在 HAL_InitTick/NVIC 中看到对 SysTick/NVIC 的配置。

本案例关注的是 **在上述初始化正确的前提下，首任务启动仍失败** 的剩余根因。

#### 3.2 FreeRTOS 端口层 OS 核心函数被桩化

在 `DATABASE_LwIP_StreamingServer/lcmhal_ai_log` 中，搜索 `replacement_update_*.json`，发现以下 **OS 调度核心函数** 被替换为“POSIX 兼容”空壳实现：

- `prvPortStartFirstTask`：
  - `replacement_code` 中明确写道：
    > *Skip all hardware-specific assembly code: NVIC offset register access (0xE000ED08), MSP setup, CONTROL 清零, cpsie i/f, dsb/isb, SVC 0...*
  - 实际替换后的函数体只保留注释，不再执行 `msr PSP, pxTopOfStack`、`svc 0` 等首任务启动关键指令。
- `vTaskStartScheduler` / `xPortStartScheduler`：
  - 多个 `replacement_update_vTaskStartScheduler_*` 和 `replacement_update_xPortStartScheduler_*` 把它们改成“POSIX-compatible scheduler start”，仅做少量逻辑或直接返回。
- `vPortSetupTimerInterrupt` / `vPortEnterCritical` / `vPortExitCritical` / `prvTaskExitError` / `vPortEnableVFP`：
  - 不同程度被替换为跳过硬件访问的桩，弱化了端口层对 OS tick / 临界区 / FPU 的控制。

这些函数在 FreeRTOS Cortex-M 端口中属于**调度和上下文切换的核心**：

- `prvPortStartFirstTask`：
  - 从 `pxCurrentTCB->pxTopOfStack` 恢复寄存器到 PSP；
  - 设置 CONTROL 以使用 PSP 作为线程栈；
  - 通过 `SVC 0` 触发异常返回，让硬件/NVIC 从 PSP 弹出首任务栈帧，真正切换到第一个任务。
- `vTaskStartScheduler` / `xPortStartScheduler`：
  - 创建/准备首任务和 idle 任务；
  - 最终调用上述端口层函数启动调度。

**一旦把这些函数替换成“POSIX 兼容空壳”，首任务 PSP 初始化与 SVC/异常返回链路全部被掐断**：

- `pxPortInitialiseStack` 虽然写好了任务栈帧，但 PSP 永远没有被设置到该地址（始终为 0）；
- `SVC_Handler` / `PendSV_Handler` 的首次返回不再按 FreeRTOS 端口假设的路径执行；
- fuzzemu 的 NVIC 实现只能看到「异常从 MSP 进出」，最终从 MSP 顶 0x20080000 弹出一坨 0，当作任务帧，PC=0。

#### 3.3 fuzzemu NVIC 异常返回对 PSP/MSP 的处理需要配合

同时，在 fuzzemu 的 `nvic.py` 中，异常进入/退出的实现最初也存在对 PSP/MSP 弹栈的不完善。

- `_enter_exception`：
  - 使用当前 SP 压栈（若在线程模式+PSP，则压在 PSP 上），然后根据 CONTROL 切换到 MSP，并在 LR 上设置 `NVIC_INTERRUPT_ENTRY_LR_PSPSWITCH_FLAG`。
- `_exit_exception`（原始实现）：
  - 无论是否需要从 PSP 返回，都简单地从当前 SP（通常是 MSP）调用 `_pop_state()` 弹栈。

这导致即使后续修复了 OS 端口层，若 NVIC 异常返回仍从错误栈弹帧，也会出现 PC=0 问题。

在本次案例中，最终的解决方案分为两步并行：

1. **恢复 FreeRTOS 端口层的 OS 调度核心函数为原始实现**（见下节）；
2. **在 `nvic.py` 中补全 PSP/MSP 异常返回路径**：当 EXC_RETURN/CONTROL 表示「从 Thread+PSP 返回」时，从 PSP 弹栈并把恢复出的 SP 写回 PSP，同时保持 Unicorn 的 SP 与 PSP 一致。

只有两者都正确，首任务才能通过 SVC/PendSV + PSP 异常返回链路被成功切换。

---

### 4. 解决方案与防再发措施

#### 4.1 删除调度核心函数的错误替换日志

在 `DATABASE_LwIP_StreamingServer/lcmhal_ai_log` 中，使用 `main.py clean` 对以下函数执行日志清理（`--type all` 或至少 `--type replacement`）：

- `prvPortStartFirstTask`
- `vTaskStartScheduler`
- `xPortStartScheduler`
- `vPortSetupTimerInterrupt`
- `vPortEnterCritical`
- `vPortExitCritical`
- `prvTaskExitError`
- `vPortEnableVFP`
- **`prvInitialiseNewTask`**（任务创建/栈初始化，若被桩化会破坏任务创建；建议一并加入 prompt 的 OS CORE 列表）

示例（在项目根目录执行）：
```bash
python main.py clean testcases/server/stm32/LwIP_StreamingServer -f xPortStartScheduler -t replacement
python main.py clean testcases/server/stm32/LwIP_StreamingServer -f vPortSetupTimerInterrupt -t replacement
python main.py clean testcases/server/stm32/LwIP_StreamingServer -f prvInitialiseNewTask -t replacement
```

这会删除所有 `replacement_update_*` 对这些函数的记录，让后续构建时直接使用原始 FreeRTOS 端口实现。若问题复现，可再次执行上述 clean 并检查是否又生成了新的 replacement 文件。

#### 4.2 Prompt 侧增加「OS CORE」保护层（FunctionClassifier）

在 `prompts/function_classifier.py` 中新增：

- **OS CORE（RTOS 调度/上下文切换核心函数）** 的概念：
  - 识别这类函数：`vTaskStartScheduler`, `xPortStartScheduler`, `prvPortStartFirstTask`, `vPortStartFirstTask`, `pxPortInitialiseStack`, `vPortSetupTimerInterrupt`, `vPortSVCHandler`, `SVC_Handler`, `PendSV_Handler`, `prvTaskExitError` 等；
  - 要求对这些函数 **一律按 NODRIVER 处理**：
    - `function_type = "NODRIVER"`
    - `has_replacement = false`
    - `function_replacement = ""`
  - 在 `classification_reason` 中明确标记它们为 **OS core / 调度核心函数**，方便后续逻辑识别。
- 更新分类优先级：
  - 一旦识别为 OS CORE，则优先按 OS CORE（视为 NODRIVER）处理，禁止 RECV/IRQ/INIT/LOOP 替换策略命中。

#### 4.3 Prompt 侧增加「OS CORE 不可修改」规则（FunctionFixer）

在 `prompts/function_fixer.py` 中新增一段强约束：

- **CRITICAL - OS SCHEDULER / CONTEXT-SWITCH CORE FUNCTIONS (STRICT NO-MODIFY RULE)**：
  - 这些函数必须视为**不可动**：
    - 不允许生成替换；
    - 不允许“POSIX-化”；
    - 不允许删除/跳过其中的汇编和关键逻辑。
  - 若发现 `replacement_update_*` 已把这些函数改成桩：
    - Fixer 的工作应是 **删除这些替换日志**，恢复原始实现，而不是在上面叠加新的替换。
  - 当错误 callstack 落在 `vTaskStartScheduler` / `prvPortStartFirstTask` 等位置时：
    - 指导 Fixer：**真正的根因要在周边 HAL/驱动替换或 NVIC 配置中查找，而不是修改 OS 核心函数自身**。

这样 Classifier + Fixer 形成双重保护：**OS 调度核心函数只能看、不能改**。

#### 4.4 修复 fuzzemu 的 NVIC 异常返回 PSP/MSP 处理

在 `fuzzemu/fuzzemu/emulate/nvic.py` 中，对 `_pop_state` / `_exit_exception` 做了增强：

- `_pop_state` 增加参数：
  - `frameptr_override`：可显式指定从哪根栈指针读异常帧（例如 PSP）；
  - `sp_dest_reg`：指定恢复后的 SP 应写入的寄存器（例如 `UC_ARM_REG_PSP`），并在结束时同步 Unicorn 的 `UC_ARM_REG_SP`。
- `_exit_exception` 中：
  - 当 EXC_RETURN 表示「从线程模式返回」，且带有 `NVIC_INTERRUPT_ENTRY_LR_PSPSWITCH_FLAG` 时：
    - 先根据 CONTROL 切回使用 PSP；
    - 然后调用 `_pop_state(frameptr_override=uc.reg_read(UC_ARM_REG_PSP), sp_dest_reg=UC_ARM_REG_PSP)`，从 PSP 弹栈并把恢复的 SP 写回 PSP。
  - 其它情况（返回线程但未切 PSP、或返回 handler 模式）仍从当前 SP 弹栈。

这一步保证：**一旦 FreeRTOS 端口层正确设置了 PSP 和 EXC_RETURN，fuzzemu 的 NVIC 异常返回能从 PSP 弹出首任务栈帧，而不是错误地从 MSP 顶部读出一坨 0。**

#### 3.4 复现时发现：xPortStartScheduler / vPortSetupTimerInterrupt 的 replacement 被重新生成

在后续排查「仍出现 unmapped read (pc=0, 从 0x20080000 弹栈)」时，再次检查 `lcmhal_ai_log` 发现：

- **xPortStartScheduler** 仍有大量 `replacement_update_xPortStartScheduler_*.json`（例如 20260226 的 9 个文件）。
  - 替换内容为「POSIX 兼容」实现：只调用 `vPortSetupTimerInterrupt()`、设 `uxCriticalNesting = 0`，然后 **直接 `return pdTRUE`**。
  - **未调用 `prvPortStartFirstTask()`**，因此 **PSP 从未被设置**，首任务切换链路被掐断，与 3.2 节现象一致。
- **vPortSetupTimerInterrupt** 也有多份 `replacement_update_*.json`，替换后不再写 SysTick 相关寄存器，可能影响 tick 与调度。
- **prvInitialiseNewTask** 存在 1 份 `replacement_update_*.json`（仅去掉 memset 填栈，其余逻辑保留），为保险起见也建议清理，避免后续被改成空桩。

结论：**即使 prompt 已禁止对 OS CORE 做替换，Fixer/分析流程仍可能再次为这些函数生成并写入 replacement_update**。出现「首任务启动阶段 pc=0 / unmapped read」时，应**优先检查 ai_log 中是否又出现了上述函数名的 replacement_update**，并再次执行 clean（见下）。

---

### 5. 经验总结与快速检查清单（针对 OS 调度核心替换问题）

1. **看到首任务启动阶段 HardFault (intno=3, pc=0) 时**，优先按两步排查：
   - 步骤 1：按 `rtos_nvic_init_stub_fix` 检查 HAL/SystemInit/NVIC/SysTick 是否被桩化。
   - 步骤 2：若 HAL 初始化正确，再检查 OS 端口层核心函数（`prvPortStartFirstTask`, `vTaskStartScheduler`, `xPortStartScheduler`, `vPortSetupTimerInterrupt`, `vPortSVCHandler`, `SVC_Handler`, `PendSV_Handler`, `pxPortInitialiseStack` 等）是否被替换成“POSIX 兼容”空壳。
2. **区分「驱动 init」与「OS 调度核心」的职责边界**：
   - 前者（HAL_Init\* / SystemInit / HAL_NVIC\* / SysTick init）可以通过谨慎替换来屏蔽硬件，但必须保留对 VTOR/NVIC/SysTick 的等价配置；
   - 后者（FreeRTOS 端口层 / SVC / PendSV / 首任务启动）**是 OS 的一部分**，不能被当成普通 driver 函数去“POSIX-化”，否则调度链路会彻底断裂。
3. **调试时结合 debug.txt 看「栈帧写在哪、从哪弹出来」**：
   - 若 `pxPortInitialiseStack` 把帧写在 0x20016e4x 一带，而 NVIC/异常返回从 0x20080000 顶部读出来的是 0，则说明 PSP 没设好或异常返回没用 PSP。
   - 再对照 lcmhal_ai_log 看 `prvPortStartFirstTask` / `SVC_Handler` 是否被替换过，可以快速锁定是「OS 端口层被桩化」的问题。
4. **Prompt 层必须有「OS CORE」保护规则**：
   - Classifier：识别 OS 核心函数并一律标为 NODRIVER，不生成替换。
   - Fixer：遇到 OS 核心函数时只允许删除错误替换、恢复原实现，不允许提出新的替换方案。

---

### 6. 相关文件与延伸阅读

- **本案例**：`case_study/rtos_os_core_scheduler_stub_fix/README.md`（当前文件）
- **前置案例**：`case_study/rtos_nvic_init_stub_fix/README.md`（HAL/SystemInit/NVIC/SysTick 被桩化导致首次 PendSV 返回失败）
- **Prompt**：
  - `prompts/function_classifier.py`：新增 OS CORE / NODRIVER 保护逻辑和分类优先级调整。
  - `prompts/function_fixer.py`：新增「OS SCHEDULER / CONTEXT-SWITCH CORE FUNCTIONS (STRICT NO-MODIFY RULE)」段。
- **fuzzemu NVIC 实现**：`fuzzemu/fuzzemu/emulate/nvic.py`，查看 `_push_state` / `_pop_state` / `_enter_exception` / `_exit_exception` 对 PSP/MSP 的处理。
- **日志路径**：`testcases/server/stm32/LwIP_StreamingServer/emulate/debug_output/`（`stderr.txt` / `debug.txt` / `function.txt` / `lcmhal.txt`）。

