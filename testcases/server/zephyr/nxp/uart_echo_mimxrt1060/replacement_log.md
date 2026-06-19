## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/nxp/uart_echo_mimxrt1060`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `imx_pinctrl_init` | `/home/haojie/zephyrproject/zephyr/drivers/pinctrl/pinctrl_imx.c` | 66 | 1 |
| `imxrt_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c` | 317 | 1 |

## 2. 各函数替换详情

### imx_pinctrl_init

```text
=== imx_pinctrl_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/pinctrl/pinctrl_imx.c
- 行号：66
- 函数内容：static int imx_pinctrl_init(void)
{
#ifdef CONFIG_SOC_SERIES_IMX_RT
	CLOCK_EnableClock(kCLOCK_Iomuxc);
#ifdef CONFIG_SOC_SERIES_IMX_RT10XX
	CLOCK_EnableClock(kCLOCK_IomuxcSnvs);
	CLOCK_EnableClock(kCLOCK_IomuxcGpr);
#elif defined(CONFIG_SOC_SERIES_IMX_RT11XX)
	CLOCK_EnableClock(kCLOCK_Iomuxc_Lpsr);
#endif /* CONFIG_SOC_SERIES_IMX_RT10XX */
#elif defined(CONFIG_SOC_MIMX8MQ6)
	CLOCK_EnableClock(kCLOCK_Iomux);
#endif /* CONFIG_SOC_SERIES_IMX_RT */

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes i.MX pin control hardware by enabling clock gates for IOMUXC (I/O Multiplexer Controller) peripherals
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization function that calls CLOCK_EnableClock to enable clock gates for pin control hardware. Analysis shows it calls CLOCK_ControlGate which performs MMIO operations to write to CCM->CCGR0 registers. It fits the INIT classification as it performs peripheral initialization with hardware register writes. The function is static and returns 0, indicating successful initialization. GetMMIOFunctionInfo showed no direct MMIO expressions but the call chain reveals hardware dependencies through CLOCK_ControlGate.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Set or clear specified GPR bit for this mux */
static int imx_pinctrl_init(void)
{
	/* Skip hardware clock enable operations */
	return 0;
}
```

=== 信息结束 ===
```

### imxrt_init

```text
=== imxrt_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c
- 行号：317
- 函数内容：static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	SCB_DisableICache();
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	SCB_EnableICache();
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		if ((SCB->CCR & SCB_CCR_DC_Msk) == 0) {
			SCB_EnableDCache();
		}
	} else {
		SCB_DisableDCache();
	}

	/* Initialize system clock */
	clock_init();

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Performs basic hardware initialization for i.MX RT SoC including cache configuration and system clock initialization
- 是否需要替换：是
- 分类/替换原因：The function is a hardware initialization function that configures cache (instruction and data cache via SCB registers) and calls clock_init() which contains MMIO operations (DCDC->REG3, DCDC->REG0). GetMMIOFunctionInfo shows MMIO operations in clock_init(), and GetFunctionInfo reveals SCB register accesses for cache control. This matches INIT classification criteria: functions that initialize peripheral/configurations with hardware register accesses that need to be removed while preserving non-hardware logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	/* [INIT REMOVED] SCB_DisableICache(); */
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	/* [INIT REMOVED] SCB_EnableICache(); */
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		/* [INIT REMOVED] Hardware cache check and enable removed */
		/* Assume cache is enabled if configured */
	} else {
		/* [INIT REMOVED] SCB_DisableDCache(); */
	}

	/* Initialize system clock */
	/* [INIT REMOVED] clock_init(); - Hardware clock initialization removed */

	return 0;
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**103** 个；CodeQL `MMIOFunction`：**103** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **11** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `CLOCK_DeinitArmPll` | INIT | False | De-initializes the ARM PLL by powering it down |
| `CLOCK_DeinitAudioPll` | INIT | False | De-initializes the Audio PLL by writing a power-down mask to the PLL_AUDIO register |
| `CLOCK_DeinitEnetPll` | INIT | False | Deinitializes the ENET PLL by disabling it through hardware register access |
| `CLOCK_DeinitExternalClk` | INIT | False | Deinitializes the external 24MHz clock by powering it down |
| `CLOCK_DeinitRcOsc24M` | RETURNOK | False | Powers down the RCOSC 24M clock by clearing the RC_OSC_EN bit in the XTALOSC24M peripheral's LOWPWR_CTRL register. |
| `CLOCK_DeinitSysPfd` | RETURNOK | False | De-initializes (disables) the System PLL PFD clock based on the provided PFD parameter |
| `CLOCK_DeinitSysPll` | RETURNOK | False | De-initializes the System PLL by powering it down through hardware register access. |
| `CLOCK_DeinitUsb1Pfd` | RETURNOK | False | De-initializes (disables) the USB1 PLL PFD (Phase Frequency Detector) clock. |
| `CLOCK_DeinitUsb1Pll` | INIT | False | Deinitializes the USB1 PLL by writing zero to the PLL_USB1 register |
| `CLOCK_DeinitUsb2Pll` | INIT | False | Deinitializes the USB2 PLL by disabling it through hardware register access |
| `CLOCK_DeinitVideoPll` | INIT | False | De-initializes (powers down) the Video PLL by writing to the PLL control register |
| `CLOCK_DisableUsbhs0PhyPllClock` | RETURNOK | False | Disables the USB HS PHY PLL clock by clearing clock enable bits and setting clock gate bits in hardware registers. |
| `CLOCK_DisableUsbhs1PhyPllClock` | RETURNOK | False | Disables the USB HS PHY PLL clock by clearing clock enable bits in PLL_USB2 register and setting clock gating in USB ... |
| `CLOCK_EnableUsbhs0Clock` | INIT | False | Enables USB HS clock by configuring clock gating, resetting USB controller, and setting up PMU regulator |
| `CLOCK_EnableUsbhs0PhyPllClock` | INIT | False | Enables the internal 480MHz USB HS PHY PLL clock by configuring clock control and USB PHY hardware registers. |
| `CLOCK_EnableUsbhs1Clock` | INIT | False | Enables USB HS clock by configuring clock gating, resetting USB, and setting up power management registers with a har... |
| `CLOCK_EnableUsbhs1PhyPllClock` | INIT | False | Enables the USB HS PHY PLL clock by initializing the USB2 PLL and configuring USB PHY control registers |
| `CLOCK_GetAhbFreq` | RETURNOK | False | Calculates and returns the AHB (Advanced High-performance Bus) clock frequency by reading clock control registers and... |
| `CLOCK_GetClockOutCLKO1Freq` | RETURNOK | False | Reads clock output1 configuration from CCM register and calculates output frequency based on selected clock source an... |
| `CLOCK_GetClockOutClkO2Freq` | RETURNOK | False | Reads the clock output 2 configuration from CCM register and returns the calculated frequency based on selected clock... |
| `CLOCK_GetFreq` | NODRIVER | False | Returns the frequency for a specific clock name by dispatching to appropriate clock frequency calculation functions b... |
| `CLOCK_GetIpgFreq` | RETURNOK | False | Calculates and returns the IPG (IP Bus) clock frequency by reading clock divider configuration from hardware registers |
| `CLOCK_GetPerClkFreq` | RETURNOK | False | Gets the PER (Peripheral) clock frequency by reading clock configuration registers and applying division factors |
| `CLOCK_GetPeriphClkFreq` | RETURNOK | False | Reads clock configuration registers to determine the current peripheral clock frequency based on multiplexer and divi... |
| `CLOCK_GetPllFreq` | RETURNOK | False | Reads PLL configuration registers and calculates the current output frequency for a specific PLL |
| `CLOCK_GetPllUsb1SWFreq` | RETURNOK | False | Reads the CCM register to determine which clock source is selected for PLL3 (USB1 PLL) and returns the corresponding ... |
| `CLOCK_GetSemcFreq` | RETURNOK | False | Reads SEMC (Smart External Memory Controller) clock configuration registers to determine and return the current clock... |
| `CLOCK_GetSysPfdFreq` | RETURNOK | False | Gets the current System PLL PFD (Phase Fractional Divider) output frequency based on PFD selection |
| `CLOCK_GetUsb1PfdFreq` | RETURNOK | False | Reads USB1 PLL PFD hardware registers to calculate and return the current PFD output frequency based on the selected ... |
| `CLOCK_InitArmPll` | INIT | False | Initializes the ARM PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider selec... |
| `CLOCK_InitAudioPll` | INIT | False | Initializes the Audio PLL with specific configuration settings including bypass, numerator/denominator values, post-d... |
| `CLOCK_InitEnetPll` | INIT | False | Initializes the ENET (Ethernet) PLL with specific divider settings, clock outputs, and bypass configuration |
| `CLOCK_InitExternalClk` | INIT | False | Initializes the external 24MHz clock by configuring hardware registers and waiting for oscillator power-up and freque... |
| `CLOCK_InitRcOsc24M` | INIT | False | Initializes the RC oscillator 24MHz clock by enabling it through hardware register access |
| `CLOCK_InitSysPfd` | INIT | False | Initializes the System PLL PFD (Phase Fractional Divider) clock settings by configuring hardware registers to set PFD... |
| `CLOCK_InitSysPll` | INIT | False | Initializes the System PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider, f... |
| `CLOCK_InitUsb1Pfd` | INIT | False | Initializes the USB1 PLL PFD (Phase Fractional Divider) clock configuration |
| `CLOCK_InitUsb1Pll` | INIT | False | Initializes the USB1 PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, divider sele... |
| `CLOCK_InitUsb2Pll` | INIT | False | Initializes the USB2 PLL (Phase-Locked Loop) with specific configuration settings for clock generation |
| `CLOCK_InitVideoPll` | INIT | False | Initializes the video PLL (Phase-Locked Loop) with specific configuration settings including bypass, divider, numerat... |
| `CLOCK_IsSysPfdEnabled` | RETURNOK | False | Checks if a System Phase-Locked Loop Frequency Divider (PFD) is enabled by reading the hardware register status. |
| `CLOCK_IsUsb1PfdEnabled` | RETURNOK | False | Checks if USB1 Phase Frequency Detector (PFD) is enabled by reading hardware register status |
| `CLOCK_SetClockOutput1` | RETURNOK | False | Sets the clock source and divider for clock output 1 on the NXP MIMXRT1062 microcontroller |
| `CLOCK_SetClockOutput2` | INIT | False | Configures the clock source and divider for clock output 2 on the NXP MIMXRT1062 microcontroller |
| `CLOCK_SwitchOsc` | RETURNOK | False | Switches the OSC (oscillator) source for the SoC based on the input parameter |
| `GPIO_PinInit` | INIT | False | Initializes a GPIO pin with specified configuration including direction, output logic, and interrupt mode |
| `LPUART_Deinit` | INIT | False | Deinitializes an LPUART instance by waiting for transmission to complete, disabling TX/RX, clearing status flags, and... |
| `LPUART_Init` | INIT | False | Initializes an LPUART (Low Power UART) peripheral with user-defined configuration including baud rate, parity, data b... |
| `LPUART_TransferReceiveNonBlocking` | RECV | False | Receives data from LPUART using interrupt method, manages ring buffer if enabled, and handles asynchronous data trans... |
| `LPUART_TransferSendNonBlocking` | RETURNOK | False | Non-blocking UART transmission function that sets up transfer parameters and enables transmitter interrupt for interr... |
| `SystemCoreClockUpdate` | INIT | False | Calculates and updates the system core clock frequency by reading hardware clock configuration registers |
| `SystemInit` | CORE | False | System initialization function that configures core system components including FPU, vector table, watchdogs, SysTick... |
| `add_to_waitq_locked` | NODRIVER | False | Kernel scheduler function that adds a thread to a wait queue, marking it as pending and removing it from ready queues |
| `adjust_owner_prio` | NODRIVER | False | Adjusts the priority of a mutex owner thread in the Zephyr RTOS kernel |
| `arch_new_thread` | NODRIVER | False | Initializes architectural context for a new thread by setting up the initial exception stack frame and thread archite... |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating-point values to text format with various format specifiers (f, e, g,... |
| `first` | NODRIVER | False | Returns the first timeout structure from the kernel's timeout list |
| `halt_thread` | CORE | False | Dequeues a thread and moves it into a new state (dead or suspended), performing thread cleanup operations |
| `imx_pinctrl_init` | INIT | True | Initializes i.MX pin control hardware by enabling clock gates for IOMUXC (I/O Multiplexer Controller) peripherals |
| `imxrt_init` | INIT | True | Performs basic hardware initialization for i.MX RT SoC including cache configuration and system clock initialization |
| `init_ready_q` | CORE | False | Initializes the scheduler's ready queue data structure based on scheduler configuration (SCALABLE, MULTIQ, or DUMB) |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap structure by setting up wait queue and system heap |
| `k_mbox_get` | NODRIVER | False | Zephyr RTOS mailbox receive function that retrieves messages from a mailbox by searching for compatible senders and h... |
| `k_mbox_init` | NODRIVER | False | Initializes a kernel mailbox structure by setting up wait queues, spinlock, and optional object tracking |
| `k_mem_slab_init` | NODRIVER | False | Initializes a memory slab (kernel memory allocator) by setting up data structures, creating free lists, and initializ... |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a message queue by checking for waiting threads and freeing allocated buffer if dynamically allocated |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting up buffer pointers, size limits, and internal state. |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated memory if the stack was dynamic... |
| `k_stack_init` | NODRIVER | False | Initializes a kernel stack data structure by setting up wait queue, lock, and buffer pointers |
| `k_timer_init` | NODRIVER | False | Initializes a Zephyr kernel timer structure with callback functions and internal data structures |
| `k_work_cancel_delayable_sync` | CORE | False | Cancels a delayed work item synchronously in the Zephyr RTOS kernel, checking pending status and waiting for cancella... |
| `k_work_cancel_sync` | NODRIVER | False | Cancels a work item synchronously, waiting for completion if the work is already running |
| `k_work_flush` | NODRIVER | False | Flushes a work item, waiting for it to complete if necessary, as part of Zephyr RTOS work queue subsystem |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item, waiting for it to complete execution and potentially resubmitting it if needed |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item structure with a handler function for kernel work queue subsystem |
| `k_work_queue_start` | NODRIVER | False | Starts a work queue thread in Zephyr RTOS by initializing data structures and creating/starting a thread |
| `mbox_message_put` | NODRIVER | False | Helper routine for sending mailbox messages in Zephyr RTOS, handling both synchronous and asynchronous sends by searc... |
| `mcux_ccm_get_subsys_rate` | RETURNOK | False | Reads clock configuration registers to determine the current clock rate for various peripheral subsystems (I2C, SPI, ... |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the kernel scheduler |
| `next` | NODRIVER | False | Returns the next timeout structure in the kernel's timeout linked list |
| `ready_thread` | CORE | False | Marks a thread as ready to run and adds it to the run queue if not already queued and in ready state |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout linked list and adjusts the delta ticks of the next timeout in ... |
| `timeout_rem` | NODRIVER | False | Calculates remaining ticks for a timeout by traversing the timeout queue and subtracting elapsed time |
| `update_cache` | CORE | False | Updates the scheduler's cache of the next thread to run, determining whether to preempt the current thread based on t... |
| `z_abort_timeout` | NODRIVER | False | Aborts/cancels a scheduled timeout by removing it from the kernel timeout queue if it's currently linked. |
| `z_add_timeout` | NODRIVER | False | Adds a timeout to the kernel's timeout scheduling system, calculating when it should fire and inserting it into a sor... |
| `z_cbvprintf_impl` | NODRIVER | False | Callback-based printf implementation that processes format strings and arguments, converting them to character output... |
| `z_impl_k_condvar_init` | CORE | False | Initializes a condition variable kernel object by setting up its wait queue and kernel object metadata |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a mutex data structure in the Zephyr RTOS kernel by setting owner to NULL, lock count to 0, initializing ... |
| `z_impl_k_mutex_lock` | NODRIVER | False | Implements mutex locking functionality in Zephyr RTOS with thread priority inheritance and wait queue management |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a Zephyr kernel queue data structure by setting up its internal linked list, spinlock, wait queue, and op... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a Zephyr kernel semaphore by setting its count, limit, and initializing associated data structures like w... |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Kernel timer synchronization function that waits for a timer to expire and returns its status |
| `z_impl_k_yield` | CORE | False | Kernel scheduler function that implements thread yielding by dequeuing and re-queuing the current thread, then perfor... |
| `z_init_thread_base` | NODRIVER | False | Initializes the base thread structure with priority, state, and options for Zephyr kernel thread management |
| `z_priq_dumb_best` | CORE | False | Retrieves the highest priority thread from a scheduler priority queue |
| `z_priq_dumb_remove` | NODRIVER | False | Removes a thread from a priority queue by removing it from the thread's doubly-linked list node |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue for scheduler operations |
| `z_sched_waitq_walk` | CORE | False | Walks through a wait queue and invokes a callback function on each waiting thread as part of OS scheduler operations |
| `z_set_prio` | CORE | False | Sets thread priority in the scheduler run queue and returns whether rescheduling is needed |
| `z_setup_new_thread` | CORE | False | Initializes and sets up a new thread structure in the Zephyr RTOS kernel, preparing it for execution. |
| `z_timer_expiration_handler` | CORE | False | Handles expiration of kernel timer objects, updates timer status, invokes expiry callbacks, and manages threads waiti... |
| `z_unpend_all` | CORE | False | Un-pends all threads from a wait queue and marks them as ready for scheduling in the Zephyr RTOS kernel |

## 附录：interesting MMIO expr 子集（共 11 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `CLOCK_InitArmPll`
- `CLOCK_InitAudioPll`
- `CLOCK_InitEnetPll`
- `CLOCK_InitExternalClk`
- `CLOCK_InitSysPll`
- `CLOCK_InitUsb1Pll`
- `CLOCK_InitUsb2Pll`
- `CLOCK_InitVideoPll`
- `CLOCK_SetDiv`
- `CLOCK_SetMux`
- `clock_init`
