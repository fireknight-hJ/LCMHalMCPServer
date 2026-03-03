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
- **DO** keep preprocessor directives (`#ifdef`, `#if`, etc.) unchanged; do not add new ones.
- **DO** use only the provided helper functions (e.g. `HAL_BE_In`, `HAL_BE_Out`, `HAL_BE_Block_Read`); do not introduce other stdio/stdlib I/O (e.g. `fflush`, `read`, `write`) unless already in context.

---

## Execution steps (brief)

Base every step on **tool-returned** original code, struct definitions, and MMIO information.

1. **Parameter and return type** — From `GetFunctionInfo` output, identify types and whether parameters are in/out; do not assume types not present there.
2. **Data structures and globals** — List structs, enums, macros used; assume they are defined elsewhere; do not redefine. Note globals only if present in the original.
3. **MMIO and hardware** — Locate register accesses, polling loops, and interrupt control from `GetMMIOFunctionInfo` and the original snippet.
4. **Non-driver logic** — Preserve buffer handling, state updates, OS/RTOS calls, callbacks; remove or replace only hardware-dependent parts.
5. **Apply strategy** — RECV: use `HAL_BE_In`/`HAL_BE_ENET_ReadFrame` for reads; IRQ: remove register writes, keep condition branches and OS calls; INIT: remove register writes, keep struct init and state; LOOP: remove or comment polling loops, keep data flow.
6. **Final check** — Return value consistent with success path; no unreachable branches; every variable/constant has a defined source (parameter, struct field, or allowed helper).

---

## Summary

Every type, member, macro, and function in the replacement MUST be findable in the tool results or in the target project’s headers. If it cannot be traced there, it is forbidden.
