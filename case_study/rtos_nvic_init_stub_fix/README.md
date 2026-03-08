# RTOS 调度/NVIC 初始化被桩化导致 HardFault 问题案例

## 问题背景

在 LwIP_StreamingServer（带 FreeRTOS）固件仿真过程中，固件执行到 `xPortStartScheduler` 后立刻退出，模拟器报错并返回非零退出码。

**现象**：
- `emulate/debug_output/stderr.txt` 中出现：`[-] NVIC INTR unhandled: intno=3 pc=0x0 lr=0x...`（intno=3 为 ARM HardFault）
- `emulate/debug_output/function.txt` 显示调用链在 `xPortStartScheduler` / `vTaskStartScheduler` 附近终止
- `lcmhal.txt` 可能为空或很短，说明在首次上下文切换（如 PendSV 返回）时就崩溃

## 根本原因分析

### 1. fuzzemu 与 NVIC/SysTick 的关系

fuzzemu 的 NVIC（中断控制器）模拟依赖**固件对寄存器的写入**来更新内部状态。当固件执行 `HAL_NVIC_SetPriority`、`HAL_InitTick`、`SystemInit` 中对 SCB->VTOR、NVIC、SysTick 的写操作时，模拟器通过 MMIO 钩子捕获这些写并更新自己的 NVIC/SysTick 状态。调度器首次切换（如 PendSV 返回）时，模拟器会依赖这些状态做异常返回和上下文恢复。

### 2. AI 替换导致的关键代码缺失

AI 在做「POSIX 兼容」替换时，将以下函数替换成了**不写任何寄存器的空桩**：

| 函数 | 替换后行为 | 应有行为（原始 HAL） |
|------|------------|----------------------|
| **SystemInit** | 空函数或注释掉所有写 | 写 SCB->CPACR、RCC、**SCB->VTOR** |
| **HAL_InitTick** | 仅 `return HAL_OK` | 配置 SysTick 周期/优先级、使能 SysTick 中断（或 TIM6） |
| **HAL_NVIC_SetPriorityGrouping** | 仅 `bx lr` | 写 SCB->AIRCR（优先级分组） |
| **HAL_NVIC_SetPriority** | 仅 `bx lr` | 写 NVIC->IPR[] |
| **HAL_NVIC_EnableIRQ** | 仅 `bx lr` | 写 NVIC->ISER[] |

**后果**：
- VTOR 未设置或错误 → 异常/中断时取到的向量表地址错误，可能取到 PC=0
- SysTick、NVIC 优先级与使能未配置 → 模拟器内部 NVIC 状态与 RTOS 预期不一致
- 首次 PendSV 返回时，模拟器按未配置状态恢复上下文 → PC 异常（如 0）→ **HardFault (intno=3, pc=0)**

### 3. 诊断依据（ELF vs al_log）

对当前 `output.elf` 反汇编可验证：

- **HAL_InitTick**（如 0x08001972）：仅 `movs r0, #0` + `bx lr`，无任何 NVIC/SysTick 写
- **HAL_NVIC_SetPriorityGrouping** 等：仅 `bx lr`
- **SystemInit**：若当前构建未应用替换，仍可见 `str r3, [r1, #8]`（即 SCB->VTOR = 0x08000000）；若应用了 al_log 中的替换，则 VTOR 也不会写

al_log（`replacement_update_SystemInit_*.json`、`replacement_update_HAL_InitTick_*.json` 等）中记录的 `replacement_code` 明确为「跳过所有硬件写、仅 return 成功」，与上述反汇编一致。

## 诊断过程（可复用）

1. **确认现象**：查看 `stderr.txt` 是否有 `intno=3`、`pc=0x0`；`function.txt` 是否停在 `xPortStartScheduler` 附近。
2. **查 AI 替换记录**：在 `DATABASE_PATH/lcmhal_ai_log/` 中搜索 `replacement_update_SystemInit_*`、`replacement_update_HAL_InitTick_*` 以及 session 中对 `HAL_NVIC_*` 的替换，查看 `replacement_code` 是否为空/仅 return。
3. **对照 ELF**：用 `syms.yml` 或 `arm-none-eabi-nm` 得到上述函数地址，对 `output.elf` 执行 `arm-none-eabi-objdump -d --start-address=... --stop-address=...`，若函数体只有 `bx lr` 或 `movs r0,#0; bx lr`，则确认为桩。
4. **结论**：若上述函数在 al_log 中被替换为不写 VTOR/NVIC/SysTick 的桩，则根因即为「调度/NVIC 相关操作被删」。

## 解决方案

### 1. 原则

**涉及调度、尤其 NVIC/VTOR/SysTick 的操作不能删**，AI 做函数替换时必须严格遵守：要么不替换（保留原实现），要么在替换中**保留**对 VTOR、NVIC 优先级/使能、SysTick 的寄存器写（或等价行为）。

### 2. Prompt 修改（仅增不删）

#### a) `prompts/function_fixer.py`

- **英文**：在签名规则后增加 **CRITICAL - RTOS/NVIC/SCHEDULING - DO NOT REMOVE OR STUB** 段落，明确禁止对 `SystemInit`、`HAL_InitTick`、`HAL_NVIC_SetPriorityGrouping`、`HAL_NVIC_SetPriority`、`HAL_NVIC_EnableIRQ` 及任何写 SCB->VTOR/NVIC/SysTick 的函数做纯桩替换；INIT 策略中增加**例外**：上述函数不得用空桩替换，要么不替换要么保留 VTOR/NVIC/SysTick 写。
- **中文**：在 Step 2 后增加同样的「关键约束 - 调度/NVIC 相关操作不得删除」；在 INIT（初始化）策略中增加「例外（必须遵守）」说明。

#### b) `prompts/function_classifier.py`

- 在 Role 后增加 **CRITICAL - RTOS/NVIC/Scheduling must not be stubbed**：禁止对上述函数生成移除/桩化 VTOR/NVIC/SysTick 写的替换。
- 在 **INIT** 分类的 Strategy 中增加 **EXCEPTION - RTOS-critical init (strictly enforced)**。
- 在 General Replacement Rules 的「Preserve OS Operations」中补充：不得移除或桩化 NVIC/SCB/SysTick 的寄存器写。
- 在 **Step 5: Apply Replacement Strategy** 的 INIT 条下，为「Remove all register writes」增加例外：对 VTOR/NVIC/SysTick 的写不删、不桩化。

### 3. 配置侧

- `tools/emulator/conf_generator.py` 中已用常量 **RTOS_CRITICAL_INIT_FUNCS** 标明不宜被纯桩替换的函数（如 `HAL_InitTick`、`HAL_NVIC_SetPriority`、`HAL_NVIC_SetPriorityGrouping`、`SystemInit`），便于后续扩展与排查。
- 启动阶段仅对合法循环函数（如 FillZerobss、LoopCopyDataInit）做 **loop_whitelist**，不为其配置 **do_return** handler，避免 bx lr 时 LR=0 导致 UC_ERR_READ_UNMAPPED（参见其他 case_study 与 skill）。

## 经验总结

1. **RTOS 类 demo**：调度器启动前必须完成 NVIC/SysTick/VTOR 相关初始化，且这些初始化通过**写寄存器**被 fuzzemu 钩子看到；若被替换成不写寄存器的桩，首次上下文切换必然异常。
2. **替换前必须区分「外设 MMIO」与「调度相关 MMIO」**：前者可替换为 HAL_BE_* 或跳过，后者（SCB->VTOR、NVIC、SysTick）不得删除或桩化。
3. **诊断顺序**：先看 stderr/function 确认现象 → 再查 al_log 的 replacement_code → 必要时用 objdump 对照 ELF，可快速判断是否为「调度/NVIC 被桩化」导致。

## 相关文件与延伸阅读

- **Prompt**：`prompts/function_fixer.py`、`prompts/function_classifier.py`
- **配置**：`tools/emulator/conf_generator.py`（RTOS_CRITICAL_INIT_FUNCS、loop_whitelist）
- **文档**：`doc/fuzzemu_execution_flow.md` 第 6 节（RTOS 类 demo 初始化注意）、第 7 节（LwIP_StreamingServer 关键初始化函数对比：ELF vs al_log vs 原始 HAL）
- **Skill**：`debug-lcmhal-failure` 中「错误分析能力沉淀」与「遇到调度/启动即崩时的快速检查清单」
- **Demo**：`testcases/server/stm32/LwIP_StreamingServer/`，日志目录 `emulate/debug_output/`（stderr.txt、function.txt、lcmhal.txt、debug.txt）
