function_analyze_stretegy = """
Function Classification and Rewriting Strategies:

1. RECV (Data Transmission/Reception Functions) (Priority Replacement)
  * Identification: Functions performing critical data I/O operations, DMA ring buffer management, or peripheral data transfer (data read).
  * Example: HAL_Eth_ReadFrame, Uart_Receive, Flash_Read
  * Strategy: Redirect I/O operations to POSIX-equivalent interfaces.
    ◦ When receiving data: Use `int HAL_BE_ENET_ReadFrame(void* buf, int length)` (for receiving data packets, where `length` indicates the maximum length of the receive buffer) or `int HAL_BE_In(void* buf, int len)` (for receiving fixed-length bytes, where `len` indicates the number of bytes to read from stdin). These functions are defined in `HAL_BE.h` (ensure to include this header file before use to avoid errors).
    ◦ When sending data: Output to `HAL_BE_Out` (e.g., using ``) or other appropriate output streams; can be skipped if not essential.

2. IRQ (Interrupt Service Functions) (Priority Replacement)
  • Identification: Functions handling hardware interrupts (e.g., `IRQHandler`) or enabling interrupts (IRQ) (e.g., `IRQ_Enable` or IRQ enable operation in function body).
  • Strategy: Preserve interrupt-related operations, remove actual IRQ operations.

(! IT'S IMPORTANT THAT Do make sure that the function is not RECV or IRQ type, then the function can be classified as other types.)  

3. INIT (Function for initialization) (Priority Replacement)
  * Identification: Functions that initialize driver/peripheral resources, set up initial configurations, or perform other setup tasks.
  * Strategy: Remove mmio or register access operations. Preserve initialization logic for other structures (especially resource allocation and configuration) and try your best to keep the original functionality, keep the state machine correct after the initialization.

4. LOOP (Functions that contains loops influenced by mmio or peripheral operations) (Priority Replacement, skip the loop if necessary)
  * Identification: Functions that contain loops where the loop condition or body is influenced by mmio or peripheral operations.
  * Strategy: Modify the loop to avoid infinite loops or blocking behavior. If necessary, skip the loop entirely while preserving the overall function structure.
  cases:
  ```c
    /* Wait last char shoft out */
    while (0U == (base->S1 & UART_S1_TC_MASK))
    {
    }

    /* Read base->D to clear overrun flag, otherwise the RX does not work. */
    while ((base->S1 & UART_S1_RDRF_MASK) != 0U)
    {
        (void)base->D;
    }
  ```
  these case has a loop that waits for a peripheral flag to clear. You can modify the loop to avoid waiting on the hardware flag, or skip the loop entirely if it's not necessary for emulation without hardware envolving.

5. RETURNOK (Driver-Only Functionality Functions)
  * Identification: Functions that only perform driver/peripheral operations and do not affect upper-layer data structures.
  * Strategy: Return success status or appropriate default values.
    ◦ For HAL functions: Return success flags (e.g., `HAL_OK` or `0`).
    ◦ For functions with return values: Return appropriate default values.

6. SKIP (Non-Critical Driver Functions)
  * Identification: Functions performing non-critical driver operations that can be safely ignored.
  * Strategy: Completely remove or use empty implementations (e.g., keep empty function bodies for void functions).

7. NODRIVER (Non-Driver / Ambiguous Mixed Cases)
  • Identification: Functions incorrectly marked as driver-dependent, no real peripheral semantics, or mixed/unclear cases that do not fit other types.
  • Strategy: Preserve original implementation without changes; document ambiguity when needed.
"""

# Shared replacement taxonomy and hard constraints.
# Reused by FunctionClassifier prompt and VerifyReplacement rubric prompt/check.
FUNCTION_REPLACEMENT_SHARED_RULES = """
Shared Function Replacement Taxonomy and Hard Constraints:

Type taxonomy (for replacement-related decisions):
- CORE / RECV / IRQ / INIT / LOOP / RETURNOK / SKIP / NODRIVER

INIT hard constraints (anti-stub):
1) Do NOT replace INIT with an empty stub when original has semantic-bridging behavior.
2) For thin-wrapper INIT functions (argument checks + key delegate call), prefer NO replacement:
   keep function_type=INIT, set has_replacement=false, function_replacement="",
   and preserve original implementation.
3) Only replace thin-wrapper INIT when there is concrete runtime/build evidence that
   the wrapper itself is the fault point. In that case, replacement must preserve an
   equivalent semantic path and key delegate semantics.
4) Preserve critical parameter semantics (e.g., nextTcd scatter/gather semantics, address-domain conversion).
5) If hardware writes are removed, keep minimal upper-layer-visible semantics (state propagation, linkage semantics).
6) If replacement is intentionally degraded (compile-only fallback), explicitly mark semantic degradation in reason.

Thin-wrapper INIT concrete examples:
- Example A (should NOT replace wrapper itself):
  Original:
  ```c
  void EDMA_SetTransferConfig(EDMA_Type *base, uint32_t channel,
                              const edma_transfer_config_t *config, edma_tcd_t *nextTcd)
  {
      assert(config != NULL);
      if (nextTcd != NULL) {
          nextTcd = (edma_tcd_t *)CONVERT_TO_DMA_ADDRESS(nextTcd);
      }
      EDMA_TcdSetTransferConfigExt(base, EDMA_TCD_BASE(base, channel), config, nextTcd);
  }
  ```
  Expected decision:
  - function_type=INIT
  - has_replacement=false
  - keep original wrapper; if needed, process callee `EDMA_TcdSetTransferConfigExt`.

- Example B (replace only with concrete evidence, preserve bridge semantics):
  If runtime evidence proves wrapper is fault point, replacement must still keep:
  - argument validation
  - `nextTcd`/address-domain conversion semantics
  - equivalent delegate path (direct call or semantically-equivalent logic)
  Forbidden fallback:
  ```c
  (void)base; (void)channel; (void)config; (void)nextTcd; return;
  ```

Verifier-oriented rejection hints:
- Reject replacement if original contains a key delegate call but replacement removes it without equivalent logic.
- Reject replacement if original contains nextTcd + address conversion semantics but replacement drops both.

Pattern — **MSMF** (mixed software state + MMIO-gated control flow; see `prompts/code_generation_rules.md`):
1) **Identification**: function updates **handle/queue/descriptor/list state in RAM** and uses **MMIO reads** largely to **gate** branches (busy, which link is active, early returns), not only as payload I/O.
2) **Forbidden**: replacement that is **only** `return HAL_OK` / `return kStatus_Success` / empty while the original performed non-trivial RAM-side updates or delegate calls those layers depend on.
3) **Required**: preserve OEM **ordering** of RAM updates and delegate calls; steer emulation by **execution-flow rewrites** for branch-only MMIO predicates (constants, `goto`, `if (0)`). **No** new `#ifdef` / project macros in replacement text; keep OEM `#if` as-is.
4) **Not RETURNOK**: do not classify MSMF functions as RETURNOK/SKIP success stubs solely because register traffic appears high — classify per **RAM semantics** (usually INIT with structured replacement, or another type if I/O/IRQ dominates).

**Examples** (illustrative): `EDMA_SubmitTransfer` (Case 20 appendix); other DMA **submit/arm** paths; peripheral **start transfer** helpers that update software rings and branch on `BUSY`/`READY` MMIO.
"""