# Code Generation Rules for Function Replacement

**Authority**: All replacement code MUST satisfy these rules. Any type, member, macro, or function that appears in the replacement MUST be traceable to tool results or project headers; otherwise it is invalid.

---

## MUST OBEY (hard constraints)

### Information source
- **DO** use ONLY the following to generate replacement code:
  - Code and types returned by `GetFunctionInfo`, `GetMMIOFunctionInfo`, `GetStructOrEnumInfo`, and other tools.
  - Symbols that exist in the project / target BSP and HAL headers for the **current** chip.
- **DO NOT** invent types, struct members, macros, addresses, or global variables that do not appear in tool results or in the target chip’s headers.

### Function signature (first line of replacement)
- **MUST** match the **original** or **header declaration** exactly:
  - Same storage class: if the original or header has `void Foo(void);` (no `static`), the replacement MUST be `void Foo(void)` — **DO NOT** write `static void Foo(void)`.
  - Same return type, same function name, same parameter list.
- **Violation** causes: `"static declaration of 'X' follows non-static declaration"`.

### HAL / struct members
- **DO** use ONLY members that:
  - Appear in the **original function**, or
  - Exist in the **target chip’s HAL** (e.g. STM32F401 has a different set than F446).
- **DO NOT** use members from other chip families or series.
- **Typical violations** (DO NOT use on STM32F401):
  - `RCC_PLLInitTypeDef.PLLR` — exists only on F410/F446/F469/F479/F412/F413/F423, **not** on F401.
  - `RCC_PeriphCLKInitTypeDef.Sai1ClockSelection`, `Sai2ClockSelection`, `I2sClockSelection` — F401 uses a different struct; these cause `"has no member named 'X'"`.
  - `TIM_HandleTypeDef.ErrorCode` — not in STM32F4 HAL.
- **Violation** causes: `"'SomeType' has no member named 'X'"`.

### No fabrication
- **DO NOT** invent:
  - Address constants (e.g. 0x20000000, 0x40000000) unless they come from tool/context.
  - Undeclared globals, macros, or functions.
- **DO NOT** add `#include` or `extern` in the replacement.

### Other invariants
- **DO NOT** change the function’s return type.
- **DO NOT** modify OS-related calls (scheduling, semaphores, queues, interrupt notifications).
- **Preprocessor**: Keep existing OEM `#if` / `#ifdef` **unchanged**. **Do not** add new `#if` / `#ifdef` / project-specific compile macros for simulation (no `LCMHAL_*` steering guards in generated replacement).
- **DO** use only the provided helper functions (e.g. `HAL_BE_In`, `HAL_BE_Out`, `HAL_BE_Block_Read`); do not introduce other stdio/stdlib I/O (e.g. `fflush`, `read`, `write`) unless already in context.

---

## Pattern: mixed software state + MMIO-gated control flow (MSMF)

**When it applies**: The function **both** (a) updates **caller-visible or handle-owned RAM state** — queues, indices, linked descriptors, shadow registers, software flags — **and** (b) uses **MMIO reads** mainly to **choose branches** (busy / retry / which descriptor is “live” / early `return`), not only to stream payload bytes.

**Classification (for the agent)**: Prefer **INIT** (or RECV/IRQ only if the dominant behavior is clearly I/O or ISR semantics) with structured replacement — **not** **RETURNOK** / **SKIP** “success-only stub” when (a) is non-trivial. `GetMMIOFunctionInfo` alone must not justify stripping all RAM-side effects.

**Replacement methodology (execution-flow, no new `#ifdef`)**:

1. **Preserve OEM skeleton**: same **order** of updates to RAM structures, same delegate calls (`*_Install*`, `*_Set*Config`, enqueue/dequeue), same OS/RTOS calls. Do not hand-roll a second state machine.
2. **Separate “data uses of MMIO” vs “branch uses”**: keep **read-modify-write** and values that feed **non-branch** logic on real reads where needed; for **predicate** reads that only gate control flow in emulation, steer with **locals + constants**, **`goto`**, or **`if (0)`** / inverted guards — same family as RECV “skip hardware flag + goto” (see execution steps below).
3. **Anti-pattern**: `return HAL_OK` / `return kStatus_Success` **only**, while the original advanced a queue, linked nodes, or descriptor memory.

**Examples** (non-exhaustive): eDMA submit with TCD pool (`EDMA_SubmitTransfer` — see `doc/replacement_update_cases/case_20_edma_submittransfer.md` appendix); similar **submit / arm / kick** paths for other DMA engines; some **SPI/I2C** transaction submitters that branch on peripheral busy flags but still mutate driver handle state.

---

## Execution steps (brief)

Base every step on **tool-returned** original code, struct definitions, and MMIO information.

1. **Parameter and return type** — From `GetFunctionInfo` output, identify types and whether parameters are in/out; do not assume types not present there.
2. **Data structures and globals** — List structs, enums, macros used; assume they are defined elsewhere; do not redefine. Note globals only if present in the original.
3. **MMIO and hardware** — Locate register accesses, polling loops, and interrupt control from `GetMMIOFunctionInfo` and the original snippet.
4. **Non-driver logic** — Preserve buffer handling, state updates, OS/RTOS calls, callbacks; remove or replace only hardware-dependent parts.
5. **Apply strategy** — RECV: use `HAL_BE_In`/`HAL_BE_ENET_ReadFrame` for reads; IRQ: remove register writes, keep condition branches and OS calls; INIT: remove register writes, keep struct init and state; LOOP: remove or comment polling loops, keep data flow.
   - **INIT — MSMF (see section “Pattern: mixed software state + MMIO-gated control flow”)**: Apply the MSMF methodology. **Concrete instance** — eDMA submit + software TCD queue (`EDMA_SubmitTransfer`): **Do not** replace with `return kStatus_Success` / empty stub. **Preserve** OEM statement order: queue counters (`tcdUsed`, `tail`), `EDMA_TcdReset` / `EDMA_TcdSetTransferConfig` (or `*Ext` variants), descriptor link fields, `EDMA_InstallTCD`, and optional `SERQ` writes unless a callee is already a no-op stub for simulation. **Execution-flow steering only (no new `#ifdef`)**: when MMIO reads used **only** in `if` / `else if` would mis-steer emulation, use **control-flow rewrites** — locals for conditions initialized to **constants**, **`if (0)`** / inverted condition to skip an early `return`, or **`goto`** into the OEM block that matches the intended path. **Keep** read-modify-write RHS reads on real registers (e.g. `csr = tcdRegs->CSR | ...`) unless you can prove a literal is equivalent. Appendix walkthrough: `doc/replacement_update_cases/case_20_edma_submittransfer.md`.
   - **RECV with复杂 DMA+RingBuffer 控制流（网络收帧）**：默认采用“**单次收一包**”的仿真思路，在保证 RingBuffer 状态正确的前提下，**禁止保留原始按 LAST/EMPTY 扫环的多帧状态机**：
     - **只收一包（强约束）**：本次调用只模拟接收一帧数据，最多处理一个“当前 BD 所在的帧”，**不得实现多 BD/多帧遍历逻辑**；生成代码中 **不允许出现 `while` / `do { ... } while` 这类以 `isLastBuff`、`ENET_BUFFDESCRIPTOR_RX_LAST_MASK`、`ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK` 为退出条件的环扫描结构。
     - **跳过硬件 Flag + while 状态机**：依赖 `EMPTY/LAST/OWN` 等硬件写入标志位的“找帧” while/for 循环必须整体**删除或短路**，使用条件判断+`goto` 或直接重排控制流，让代码从入口尽快跳到“已经有一个当前 BD/缓冲区可以用”的分支，且该分支内部不再通过循环扫描 Ring。
     - **保留 Ring 关键操作（单次）**：必须保留**一次** `rxBuffAlloc`/buffer 分配、**一次**从 BD 取 buffer/length/totLen 填充 `rxFrame` 的逻辑，以及**一次**完整的 BD 消费+`rxGenIdx`/下标推进+BD 归还操作，保证描述符环在“单包模式”下前进一步；禁止在同一调用内多次连续调用 `ENET_IncreaseIndex` 形成扫描式循环。
     - **HAL_BE 插入点（单包模式）**：在“当前 BD 已有有效 buffer 指针、且即将把该 buffer 视为本次帧缓存”这一点调用 `HAL_BE_ENET_ReadFrame(buffer, length)`，一次性写入本次要模拟的网络帧；之后沿用原函数的 `rxFrame` 填充和 Ring 更新逻辑，并在完成一次 BD 更新后立即返回，不再继续循环。
     - **修正 buffer/标志有效性**：如果落到“取 buffer/alloc”路径时发现 BD 的 `buffer` 字段仍为 0，可在本次 `rxBuffAlloc` 成功后，将 `curBuffDescrip->buffer = (uint32_t)newBuff` 一次，并在同一位置显式设置本帧结束标志（例如置位 `ENET_BUFFDESCRIPTOR_RX_LAST_MASK`、填写 `length`），使得本次调用能够在**单次路径内**完成一帧处理并退出；禁止再依赖后续循环去等待硬件修改这些标志。
   - **RECV with complex control flow（非 DMA/RingBuffer 特例）**（例如通用 BD/描述符收包：先根据硬件状态“找帧”，再取 buffer、填 rxFrame、推进 Ring 下标）：不要在函数顶部新插一整段仿真路径，而是最小化修改控制流：
     - **Skip** 仅依赖硬件写 BD 的“找帧”逻辑（如扫描 EMPTY/LAST 的 while），用条件+`goto` 直接跳转到“get_valid_frame/取 BD 的 buffer”代码块，让执行能抵达原本的 buffer 使用位置。
     - **Keep** 分配失败返回（例如 `return Drop`）、从 BD 取 buffer/length/totLen 填充 `rxFrame` 的逻辑、以及 BD 归还和 `rxGenIdx` 等 Ring 下标推进逻辑，保证 Ring 一致性。
     - **Insert HAL_BE** 在“已经拿到 BD buffer 指针、尚未填充 rxFrame”这一点调用 `HAL_BE_ENET_ReadFrame(rxBuffer->buffer, rxBuffer->length)` 等，让仿真数据写入 buffer 后继续走原有填充与 Ring 更新。
     - **Ensure buffer valid**：如果通过条件跳转绕过了硬件写 BD 的路径，且在进入“取 buffer”逻辑前发现 `curBuffDescrip->buffer == 0`，允许在本次 `rxBuffAlloc` 成功后补一次 `curBuffDescrip->buffer = (uint32_t)newBuff`，但不要复制出另一套仿真专用循环。
6. **Final check** — Return value consistent with success path; no unreachable branches; every variable/constant has a defined source (parameter, struct field, or allowed helper).

---

## Summary

Every type, member, macro, and function in the replacement MUST be findable in the tool results or in the target project’s headers. If it cannot be traced there, it is forbidden.
