# Fuzzemu VFP 指令跳过设计文档

本文档描述 fuzzemu 中针对 Unicorn 不支持的 VFP/浮点指令所采用的**软件层跳过（VFP Skip）**设计，用于在模拟执行时遇到 `UC_ERR_INSN_INVALID` 时尽量延续执行而非直接崩溃，从而支持带 VFP 的固件（如 LwIP、libjpeg 等）。

---

## 1. 背景与问题

### 1.1 Unicorn 与 VFP

- fuzzemu 使用 **Unicorn Engine** 做 ARM Cortex-M（Thumb）指令模拟，**未使用 QEMU**。
- 在 `uc.py` 中已通过写 CPACR / FPEXC 尝试启用 VFP：
  - `uc.reg_write(UC_ARM_REG_FPEXC, 0x40000000)`（FPEXC.EN）
  - `uc.reg_write(UC_ARM_REG_C1_C0_2, 0x00f00000)`（CPACR：cp10/cp11 全权限）
- 即便如此，Unicorn 对部分 VFP/Thumb-2 浮点编码仍**未实现**，执行到该类指令时会抛出 `UcError`，`errno == UC_ERR_INSN_INVALID`，导致整次模拟被判定为崩溃。

### 1.2 业务需求

- 部分 demo（如 **STM32 + FreeRTOS + LwIP StreamingServer**）或带 libjpeg 的固件会生成 VFP 指令（如 `vmov.f64` 等）。
- 若不做处理，这些固件在 fuzzemu 中会因一条不支持的 VFP 指令而直接失败，不利于做 LCMHAL 的端到端模拟与调试。
- 目标：在**不修改 Unicorn 源码**的前提下，在 **Python 层**对“可识别的、不支持的 VFP 指令”做**单条跳过**，使模拟继续从下一条指令执行。

---

## 2. 设计目标

- **触发条件**：仅在 `uc.emu_start()` 抛出 `UcError` 且 `errno == UC_ERR_INSN_INVALID` 时尝试“VFP 跳过”。
- **策略**：若可认定当前 fault PC 处为 VFP 指令，则：
  - 将 PC 推进到该指令之后（下一条指令），
  - 记录一次跳过（便于调试与统计），
  - 在同一轮模拟中再次调用 `uc.emu_start()` 继续执行。
- **非 VFP 或无法识别**：不跳过，按原有逻辑报错、写 debug 日志并 `force_crash`，保证非 VFP 的非法指令仍被当作崩溃处理。

---

## 3. 方案概览

- **层级**：在 fuzzemu 的 **emulate 模式** 下，在 `uc_emulate()` 的**主循环**内实现。
- **流程**：
  1. 使用 `while True` 循环反复调用 `uc.emu_start(...)`。
  2. 若正常结束（命中退出地址或 count 等），则跳出循环，正常返回。
  3. 若捕获到 `UcError`：
     - 若 `errno != UC_ERR_INSN_INVALID`：按原逻辑打印/写日志并 `force_crash`，退出。
     - 若 `errno == UC_ERR_INSN_INVALID`：调用 **VFP 跳过逻辑**：
       - 若判定为“可跳过的 VFP 指令”：将 PC 设为下一条指令，打 `[VFP-SKIP]` 日志，`continue` 继续循环（再次 `emu_start`）。
       - 若判定为“非 VFP”或无法读取/解码：按崩溃处理，打印/写日志并 `force_crash`，退出。

这样，**同一次模拟**中可多次遇到不支持的 VFP 指令时，会逐条跳过并继续执行，直到正常结束或遇到真正的非法指令/内存错误等。

---

## 4. 核心逻辑：VFP 跳过

### 4.1 触发与入口

- **位置**：`fuzzemu/emulate/fuzz.py` 中 `Fuzz.uc_emulate()` 的 `while True` 循环内，在 `except UcError as e` 分支中。
- **条件**：`e.errno == UC_ERR_INSN_INVALID` 时调用 `_try_skip_invalid_vfp(uc, e)`；其余 `UcError` 直接走原有崩溃路径。

### 4.2 取指：当前 PC 的指令字节

- 优先使用 `uc.mem_read(thumb_pc, 4)` 读取 4 字节（Thumb 可能 2 或 4 字节）。
- **异常后 Unicorn 状态**：发生 `UC_ERR_INSN_INVALID` 后，部分环境下对 fault PC 的 `mem_read` 可能失败，因此需要**回退**：
  - 使用 **ELF 回退**：从当前工程配置的 `output.elf`（或 `memory_map['flash']['file']` 等）中，根据 PT_LOAD 段找到覆盖该 PC 的段，再根据 `p_offset`/`p_vaddr` 从文件中读出对应 4 字节。
- 实现上可封装为 `_read_elf_bytes_at_pc(pc, size)`，供 VFP 跳过与后续反汇编共用。

### 4.3 解码与 VFP 判定

- **解码**：用 **Capstone**（Thumb 模式：`CS_ARCH_ARM` + `CS_MODE_MCLASS | CS_MODE_THUMB`）对取到的 2/4 字节做单条指令解码，得到 mnemonic + operands。
- **VFP 判定（满足其一即可视为 VFP 并执行跳过）**：
  1. **助记符**：`mnemonic.lower().startswith('v')`（VFP/NEON 指令通常以 `v` 开头，如 `vmov`、`vldr`、`vadd` 等）。
  2. **编码启发式**：若 Capstone 解码失败或需兜底，可用 Thumb-2 中 VFP 常见编码判断——首半字为 32 位 Thumb-2 且次字节为 `0xEE` 或 `0xEF`（即 `raw[1] in (0xEE, 0xEF)`），视为 VFP 编码。

这样可覆盖如 `vmov.f64` 等在实际固件中触发 `UC_ERR_INSN_INVALID` 的指令。

### 4.4 执行“跳过”

- **步进 PC**：根据解码结果得到指令长度 `size`（Thumb 下为 2 或 4）；若解码失败则保守使用 4。
  - `new_pc = thumb_pc + (size if size > 0 else 4)`
- **保持 Thumb 模式**：写回 PC 时保留 Thumb 位：`uc.reg_write(UC_ARM_REG_PC, (new_pc | 1))`。
- **日志**：向 debug 日志写入一条 `[VFP-SKIP]` 记录（建议使用 `debug_info(..., level=3)`，便于在较高 debug 等级下查看，又不至于刷屏）。
- **返回值**：`_try_skip_invalid_vfp` 返回 `True` 表示已跳过，调用方 `continue`；返回 `False` 表示未跳过，调用方按崩溃处理。

### 4.5 与其它错误的区分

- **仅对 `UC_ERR_INSN_INVALID` 做 VFP 跳过**；对 `UC_ERR_READ_UNMAPPED`、`UC_ERR_WRITE_*`、`UC_ERR_FETCH_*` 等不做跳过，仍按原有逻辑记录 fault PC/LR、反汇编并 `force_crash`（参见 `debug.py` 中 fault 上下文与 `exit.py` 的崩溃处理）。

---

## 5. 实现要点小结

| 项目         | 说明 |
|--------------|------|
| **适用模式** | 仅 **emulate 模式**（`uc_emulate()`）；fuzz 模式（AFL）仍按原逻辑将 `UC_ERR_INSN_INVALID` 视为崩溃。 |
| **取指回退** | 先 `uc.mem_read`，失败则从 ELF 的 PT_LOAD 段按 PC 读 4 字节。 |
| **解码**     | Capstone Thumb 单条解码，得到 mnemonic 与长度。 |
| **VFP 判定** | mnemonic 以 `v` 开头，或 raw 满足 Thumb-2 VFP 编码（如次字节 0xEE/0xEF）。 |
| **跳过**     | PC += 指令长度，写回 `new_pc \| 1`，打 `[VFP-SKIP]`（level=3），返回 True。 |
| **日志**     | 使用现有 `debug_info`，不新增日志文件；与既有 debug_level 行为一致。 |

---

## 6. 与现有模块的关系

- **uc.py**：负责在初始化时启用 VFP（FPEXC/CPACR）；VFP 跳过不修改这些设置，仅在不支持的具体指令上做“单条跳过”。
- **exit.py**：仍负责将 `UC_ERR_INSN_INVALID` 映射为 SIGILL 等；在 emulate 模式下，若 VFP 跳过成功则不会走到 `force_crash`，只有未跳过或非 VFP 的非法指令才会触发 exit 逻辑。
- **debug.py**：可复用 ELF 取指/反汇编（若已有 `_read_elf_bytes_at_pc`、`_disasm_at_pc_from_elf` 等），用于崩溃时的 fault PC/LR 与指令展示；VFP 跳过仅写一条简短 `[VFP-SKIP]`，不重复完整反汇编。

---

## 7. 限制与后续可选改进

- **语义正确性**：跳过即不执行该条 VFP 指令，浮点寄存器/内存状态与真实硬件可能不一致；当前目标是在 LCMHAL 场景下“能跑通”而非完全等价执行。
- **范围**：仅针对 Unicorn 报出的 `UC_ERR_INSN_INVALID`；若未来 Unicorn 增加更多 VFP 支持，可逐步减少被跳过的指令种类。
- **fuzz 模式**：若将来需要在 AFL 路径下也做 VFP 跳过，可在 `fuzz_emulate` 的 `validate_crash_callback` 或 Unicorn 异常处理中增加与 `_try_skip_invalid_vfp` 类似的判断与 PC 推进逻辑，并注意与 AFL 的 crash 判定一致。

---

## 8. 参考

- **VFP 启用**：`fuzzemu/emulate/uc.py` 中 FPEXC/CPACR 设置。
- **非法指令退出**：`fuzzemu/exit.py` 中 `UC_ERR_INSN_INVALID` → SIGILL。
- **执行流程与调试**：`doc/fuzzemu_execution_flow.md`；整体设计可参考 `fuzzemu/fuzzemu_lcmhal_design_doc.md` 中 VFP 支持一节。
