## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/nxp/i2c_fxos8700_lpc55`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `mpu_init` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v8_internal.h` | 138 | 1 |
| `nxp_lpc55xxx_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/nxp_lpc/lpc55xxx/soc.c` | 362 | 1 |
| `z_add_timeout` | `/home/haojie/zephyrproject/zephyr/kernel/timeout.c` | 99 | 1 |

## 2. 各函数替换详情

### mpu_init

```text
=== mpu_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v8_internal.h
- 行号：138
- 函数内容：static void mpu_init(void)
{
	/* Configure the cache-ability attributes for all the
	 * different types of memory regions.
	 */
	mpu_set_mair0(MPU_MAIR_ATTRS);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures cache-ability attributes for different types of memory regions in the MPU (Memory Protection Unit)
- 是否需要替换：是
- 分类/替换原因：The function is part of system initialization that configures MPU memory attributes. It calls mpu_set_mair0 which writes to the MPU->MAIR0 hardware register. This is an initialization function that sets up hardware configuration (MPU cache attributes) and should have hardware operations removed. It does not fit CORE classification as it's not NVIC, OS kernel/scheduler, or VTOR configuration - MPU is a memory protection feature, not interrupt controller or OS core functionality.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void mpu_init(void)
{
    /* Configure the cache-ability attributes for all the
     * different types of memory regions.
     */
    /* [INIT REPLACEMENT] Removed hardware register write: mpu_set_mair0(MPU_MAIR_ATTRS); */
}
```

=== 信息结束 ===
```

### nxp_lpc55xxx_init

```text
=== nxp_lpc55xxx_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/nxp_lpc/lpc55xxx/soc.c
- 行号：362
- 函数内容：static int nxp_lpc55xxx_init(void)
{
	z_arm_clear_faults();

	/* Initialize FRO/system clock to 96 MHz */
	clock_init();

#ifdef CONFIG_GPIO_MCUX_LPC
	/* Turn on PINT device*/
	PINT_Init(PINT);
#endif

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Performs basic hardware initialization for NXP LPC55xxx SOCs including clearing ARM faults, initializing system clocks, and setting up pin interrupt controller.
- 是否需要替换：是
- 分类/替换原因：Function is a hardware initialization routine that calls z_arm_clear_faults() (which writes to ARM SCB fault registers), clock_init() (extensive clock hardware configuration), and conditionally PINT_Init() (pin interrupt peripheral initialization). While it calls a function that writes to SCB registers, these are fault status registers (CFSR, HFSR) not NVIC/OS/VTOR configuration, so it does not qualify as CORE. The function's primary purpose is peripheral hardware initialization, fitting the INIT classification. GetMMIOFunctionInfo showed no direct MMIO accesses in this function itself, but analysis of called functions reveals hardware dependencies.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/**
*
* @brief Perform basic hardware initialization
*
* Initialize the interrupt controller device drivers.
* Also initialize the timer device driver, if required.
*
* @return 0
*/
static int nxp_lpc55xxx_init(void)
{
	/* Skip hardware-specific fault clearing */
	/* z_arm_clear_faults(); */

	/* Skip hardware clock initialization */
	/* clock_init(); */

#ifdef CONFIG_GPIO_MCUX_LPC
	/* Skip PINT device initialization */
	/* PINT_Init(PINT); */
#endif

	return 0;
}
```

=== 信息结束 ===
```

### z_add_timeout

```text
=== z_add_timeout 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/kernel/timeout.c
- 行号：99
- 函数内容：void z_add_timeout(struct _timeout *to, _timeout_func_t fn,
		   k_timeout_t timeout)
{
	if (K_TIMEOUT_EQ(timeout, K_FOREVER)) {
		return;
	}

#ifdef CONFIG_KERNEL_COHERENCE
	__ASSERT_NO_MSG(arch_mem_coherent(to));
#endif

	__ASSERT(!sys_dnode_is_linked(&to->node), "");
	to->fn = fn;

	K_SPINLOCK(&timeout_lock) {
		struct _timeout *t;

		if (IS_ENABLED(CONFIG_TIMEOUT_64BIT) &&
		    Z_TICK_ABS(timeout.ticks) >= 0) {
			k_ticks_t ticks = Z_TICK_ABS(timeout.ticks) - curr_tick;

			to->dticks = MAX(1, ticks);
		} else {
			to->dticks = timeout.ticks + 1 + elapsed();
		}

		for (t = first(); t != NULL; t = next(t)) {
			if (t->dticks > to->dticks) {
				t->dticks -= to->dticks;
				sys_dlist_insert(&t->node, &to->node);
				break;
			}
			to->dticks -= t->dticks;
		}

		if (t == NULL) {
			sys_dlist_append(&timeout_list, &to->node);
		}

		if (to == first()) {
			sys_clock_set_timeout(next_timeout(), false);
		}
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Adds a timeout to the kernel's timeout list, managing timeout scheduling and interacting with hardware timers
- 是否需要替换：是
- 分类/替换原因：Function initializes timeout structures and manages kernel timeout scheduling. It has hardware dependencies through calls to elapsed() (which reads SysTick registers) and sys_clock_set_timeout() (which programs hardware timers). GetMMIOFunctionInfo shows it's in the CodeQL MMIOFunction set. Classification as INIT is appropriate because the function sets up timeout entries in kernel data structures. The replacement removes hardware-dependent operations while preserving timeout list management logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
void z_add_timeout(struct _timeout *to, _timeout_func_t fn,
		   k_timeout_t timeout)
{
	if (K_TIMEOUT_EQ(timeout, K_FOREVER)) {
		return;
	}

#ifdef CONFIG_KERNEL_COHERENCE
	__ASSERT_NO_MSG(arch_mem_coherent(to));
#endif

	__ASSERT(!sys_dnode_is_linked(&to->node), "");
	to->fn = fn;

	K_SPINLOCK(&timeout_lock) {
		struct _timeout *t;

		/* Simplified timeout calculation without hardware dependency */
		if (IS_ENABLED(CONFIG_TIMEOUT_64BIT) &&
		    Z_TICK_ABS(timeout.ticks) >= 0) {
			/* Use absolute timeout value directly */
			to->dticks = MAX(1, Z_TICK_ABS(timeout.ticks));
		} else {
			/* Use relative timeout value with a small offset */
			to->dticks = timeout.ticks + 1;
		}

		/* Preserve timeout list insertion logic */
		for (t = first(); t != NULL; t = next(t)) {
			if (t->dticks > to->dticks) {
				t->dticks -= to->dticks;
				sys_dlist_insert(&t->node, &to->node);
				break;
			}
			to->dticks -= t->dticks;
		}

		if (t == NULL) {
			sys_dlist_append(&timeout_list, &to->node);
		}

		/* Skip hardware timer programming */
		/* Original: if (to == first()) { sys_clock_set_timeout(next_timeout(), false); } */
	}
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**150** 个；CodeQL `MMIOFunction`：**150** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **13** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `CLOCK_AttachClk` | INIT | False | Configures clock selection muxes to route clock signals based on connection parameter |
| `CLOCK_EnableOstimer32kClock` | RETURNOK | False | Enables the OSTIMER 32k clock by setting the clock enable bit in the PMC (Power Management Controller) register. |
| `CLOCK_EnableUsbfs0DeviceClock` | INIT | False | Enables USB Full Speed device clock by configuring clock sources (FRO or external XTAL32M+PLL1) and setting appropria... |
| `CLOCK_EnableUsbfs0HostClock` | INIT | False | Enables and configures the USB Full Speed Host clock on NXP LPC55S69 microcontroller, selecting between FRO or extern... |
| `CLOCK_EnableUsbhs0DeviceClock` | INIT | False | Enables USB high-speed device clock for USB1 on LPC55S69 microcontroller |
| `CLOCK_EnableUsbhs0HostClock` | INIT | False | Enables USB HOST HIGH SPEED clock by configuring SYSCON and ANACTRL registers for USB1 RAM, USB1 HOST, clock_in, and ... |
| `CLOCK_EnableUsbhs0PhyPllClock` | INIT | False | Enables and configures the USB PHY PLL clock for USB HS0 based on requested frequency |
| `CLOCK_GetAdcClkFreq` | RETURNOK | False | Returns the ADC clock frequency based on system clock configuration registers |
| `CLOCK_GetCTimerClkFreq` | INIT | False | Returns the frequency of CTimer functional clock based on clock selection register configuration |
| `CLOCK_GetClockAttachId` | LOOP | False | Gets the actual clock attach ID by reading hardware registers to determine current clock source configuration |
| `CLOCK_GetClockOutClkFreq` | RETURNOK | False | Returns the frequency of the ClockOut signal based on system clock configuration selection and divider settings |
| `CLOCK_GetCoreSysClkFreq` | RETURNOK | False | Returns the frequency of the core system clock by reading clock source selection registers and calling appropriate fr... |
| `CLOCK_GetExtClkFreq` | RETURNOK | False | Returns the frequency of the external clock if enabled, otherwise returns 0 |
| `CLOCK_GetFlexCommClkFreq` | RETURNOK | False | Calculates and returns the clock frequency for FLEXCOMM peripherals by reading hardware register values and performin... |
| `CLOCK_GetFlexCommInputClock` | RETURNOK | False | Returns the frequency of flexcomm input clock based on the selected clock source by reading hardware configuration re... |
| `CLOCK_GetFreq` | RETURNOK | False | Returns the frequency of a selected clock source based on the input clock name |
| `CLOCK_GetFro12MFreq` | RETURNOK | False | Returns the frequency of the FRO 12MHz clock source by checking if the 12MHz clock is enabled in hardware registers |
| `CLOCK_GetFro1MFreq` | RETURNOK | False | Returns the frequency of the FRO 1MHz clock source (1 MHz if enabled, 0 Hz if disabled) |
| `CLOCK_GetFroHfFreq` | RETURNOK | False | Returns the frequency of the high-frequency FRO (FRO192M) output, checking if the 96MHz clock is enabled by reading t... |
| `CLOCK_GetHsLspiClkFreq` | RETURNOK | False | Returns the frequency of the HS_LPSI clock based on the current clock source selection in hardware registers |
| `CLOCK_GetMclkClkFreq` | RETURNOK | False | Returns the frequency of the MClk (Master Clock) by reading clock selection and divider registers |
| `CLOCK_GetOsc32KFreq` | RETURNOK | False | Returns the frequency of the 32kHz oscillator by reading hardware configuration registers to determine which oscillat... |
| `CLOCK_GetPLL0InClockRate` | INIT | False | Reads the PLL0 input clock selection register and returns the corresponding input clock frequency based on the config... |
| `CLOCK_GetPLL0OutClockRate` | RETURNOK | False | Returns the PLL0 output clock rate, with optional recomputation from hardware registers |
| `CLOCK_GetPLL0OutFromSetup` | RETURNOK | False | Calculates and returns the PLL0 output clock rate from a given PLL setup structure configuration |
| `CLOCK_GetPLL1InClockRate` | RETURNOK | False | Returns the PLL1 input clock rate by reading the PLL1 clock source selection register and determining the correspondi... |
| `CLOCK_GetSctClkFreq` | RETURNOK | False | Returns the frequency of the SCTimer clock based on system configuration registers |
| `CLOCK_GetSdioClkFreq` | RETURNOK | False | Returns the frequency of the SDIO clock by reading hardware configuration registers and computing based on selected c... |
| `CLOCK_GetSystickClkFreq` | RETURNOK | False | Returns the frequency of the SysTick clock based on clock source selection and divider configuration |
| `CLOCK_GetUsb0ClkFreq` | RETURNOK | False | Returns the frequency of the USB0 clock by reading clock selection and divider registers from the system controller |
| `CLOCK_GetUsb1ClkFreq` | RETURNOK | False | Returns the frequency of the USB1 clock by checking if the USB PLL output is enabled in the analog control register. |
| `CLOCK_GetWdtClkFreq` | RETURNOK | False | Returns the watchdog clock frequency by reading the WDT clock divider register and calculating based on the FRO 1MHz ... |
| `CLOCK_SetClkDiv` | INIT | False | Sets up peripheral clock dividers by writing to system control registers |
| `CLOCK_SetFLASHAccessCyclesForFreq` | INIT | False | Sets flash wait states based on input frequency to ensure proper flash memory access timing |
| `CLOCK_SetFlexCommClock` | RETURNOK | False | Configures FlexComm clock frequency by setting hardware registers |
| `CLOCK_SetPLL0Freq` | INIT | False | Configures PLL0 (Phase-Locked Loop 0) with specific frequency settings from a PLL setup structure, including power ma... |
| `CLOCK_SetPLL1Freq` | INIT | False | Configures PLL1 frequency by writing to PLL control registers and waiting for lock if requested |
| `CLOCK_SetRtc1hzClkDiv` | INIT | False | Sets up the RTC 1Hz clock divider by configuring the PMC RTCOSC32K register |
| `CLOCK_SetRtc1khzClkDiv` | INIT | False | Sets up the RTC 1kHz clock divider by configuring the PMC peripheral register |
| `CLOCK_SetupExtClocking` | INIT | False | Initializes the external oscillator clock to a specified frequency, powers up the crystal oscillator, and enables clo... |
| `CLOCK_SetupFROClocking` | INIT | False | Initializes the Core clock to specified frequency (12, 48, or 96 MHz) by configuring the Free Running Oscillator (FRO... |
| `CLOCK_SetupPLL0Mult` | INIT | False | Configures PLL0 (Phase-Locked Loop 0) output frequency based on multiplier and input frequency parameters by setting ... |
| `CLOCK_SetupPLL0Prec` | INIT | False | Configures PLL0 (Phase-Locked Loop) with precise frequency settings, including power control, register configuration,... |
| `FLEXCOMM_Init` | INIT | False | Initializes FLEXCOMM peripheral and selects operating mode (I2C, USART, SPI, etc.) based on the peripheral parameter |
| `GPIO_EnablePortClock` | INIT | False | Enables clock gating for a specific GPIO port by calling clock control functions |
| `GetExtClkFreq` | RETURNOK | False | Returns the frequency of the external clock if enabled, otherwise returns 0 by checking the ANACTRL_XO32M_CTRL register. |
| `GetFro12MFreq` | RETURNOK | False | Returns the frequency of the FRO 12MHz clock by checking if the 12MHz clock is enabled in the ANACTRL hardware register. |
| `GetFro1MFreq` | RETURNOK | False | Returns the frequency of the FRO 1MHz clock based on whether it's enabled in the system control register |
| `GetFroHfFreq` | INIT | False | Returns the frequency of the High-Frequency output of FRO (96MHz or 0) based on ANACTRL register configuration |
| `GetOsc32KFreq` | INIT | False | Returns the frequency of the 32kHz oscillator by reading PMC power configuration and oscillator selection registers |
| `INPUTMUX_Deinit` | SKIP | False | Deinitializes the INPUTMUX peripheral by disabling its clock source |
| `INPUTMUX_Init` | INIT | False | Initializes the INPUTMUX peripheral by enabling its clock |
| `PINT0_DriverIRQHandler` | IRQ | False | Pin Interrupt (PINT) handler that processes pin interrupts and pattern match interrupts, calling registered user call... |
| `PINT_Deinit` | INIT | False | Deinitializes the PINT (Pin Interrupt) peripheral by disabling clocks, resetting the module, and clearing callback ar... |
| `PINT_Init` | INIT | False | Initializes the PINT (Pin Interrupt) peripheral by enabling clocks, resetting the module, clearing callback arrays, a... |
| `PINT_PatternMatchConfig` | INIT | False | Configures PINT pattern match bit slice with source selection, configuration, and callback storage |
| `PINT_PatternMatchGetConfig` | RETURNOK | False | Reads PINT (Pin Interrupt) pattern match configuration from hardware registers for a specific bit slice and populates... |
| `PINT_PatternMatchResetDetectLogic` | RETURNOK | False | Resets pattern match detection logic if any product term is matching, returns match status |
| `PINT_PinInterruptClrStatus` | IRQ | False | Clears selected pin interrupt status for edge-sensitive interrupts by checking interrupt mode and status registers, t... |
| `PINT_PinInterruptClrStatusAll` | INIT | False | Clears the status of all pin interrupts that were triggered by edge-sensitive interrupts by reading interrupt mode an... |
| `PINT_PinInterruptConfig` | INIT | False | Configures PINT peripheral pin interrupt detection logic and callback storage |
| `PINT_PinInterruptGetConfig` | RETURNOK | False | Reads the configuration of a pin interrupt from PINT peripheral registers (ISEL, IENR, IENF) and returns the interrup... |
| `PIN_INT0_DriverIRQHandler` | IRQ | False | Interrupt handler for Pin Interrupt 0 that handles pin interrupt events, calls user callbacks, and clears interrupt s... |
| `PIN_INT1_DriverIRQHandler` | IRQ | False | Interrupt handler for pin interrupt 1, handles pattern match detection and calls user callback functions |
| `PIN_INT2_DriverIRQHandler` | IRQ | False | Interrupt handler for Pin Interrupt 2, handles pattern match detection and clears interrupt status for edge-sensitive... |
| `PIN_INT3_DriverIRQHandler` | IRQ | False | Interrupt handler for Pin Interrupt 3 that handles pattern match detection and calls user callback functions |
| `PIN_INT4_DriverIRQHandler` | IRQ | False | Interrupt handler for pin interrupt 4 that resets pattern match detection, calls user callback, and clears interrupt ... |
| `PIN_INT5_DriverIRQHandler` | IRQ | False | Interrupt handler for pin interrupt 5, handles pattern match detection reset and calls user callback |
| `PIN_INT6_DriverIRQHandler` | IRQ | False | Interrupt handler for Pin Interrupt 6, handles pattern match detection and calls user callback functions |
| `PIN_INT7_DriverIRQHandler` | IRQ | False | Interrupt handler for Pin Interrupt 7, handles pin interrupt events, resets pattern match detection, calls user callb... |
| `POWER_CycleCpuAndFlash` | SKIP | False | Puts CPU and flash into low power mode (WFI) and powers them back up after wake-up event |
| `POWER_EnterDeepPowerDown` | CORE | False | Configures the system for deep power down mode by setting up power control, SRAM retention, wakeup sources, and manag... |
| `POWER_EnterDeepSleep` | CORE | False | Puts the MCU into deep sleep mode by configuring power domains, saving interrupt states, and entering low power mode |
| `POWER_EnterLowPower` | INIT | False | Configures and enters low power mode by setting up power management registers, switching clocks, and calling low-powe... |
| `POWER_EnterPowerDown` | CORE | False | Enters power down mode by configuring low power settings, saving system state (including NVIC interrupts), entering l... |
| `POWER_GetWakeUpCause` | NODRIVER | False | Reads reset causes and wake-up sources from power management controller registers and returns them through output par... |
| `POWER_SetXtal16mhzLdo` | INIT | False | Configures and enables the LDO (Low Dropout Regulator) for the 32MHz crystal oscillator on NXP LPC55S69 MCU |
| `POWER_Xtal16mhzCapabankTrim` | INIT | False | Configures the 16MHz crystal oscillator capacitor bank trimming based on calibration values and input parameters |
| `POWER_Xtal32khzCapabankTrim` | INIT | False | Trims the 32kHz crystal oscillator capacitor bank by calculating appropriate capacitor values based on calibration da... |
| `RESET_ClearPeripheralReset` | INIT | False | Clears reset signal to specified peripheral module, allowing it to operate by writing to SYSCON reset control registers. |
| `RESET_SetPeripheralReset` | LOOP | False | Asserts reset signal to a specified peripheral module by setting the appropriate bit in the system control reset regi... |
| `SEC_GPIO_INT0_IRQ0_DriverIRQHandler` | IRQ | False | Interrupt handler for secure GPIO pin interrupt 0, handles pattern match detection and clears interrupt status |
| `SEC_GPIO_INT0_IRQ1_DriverIRQHandler` | IRQ | False | Interrupt handler for secure GPIO pin interrupt 1, handles pattern match detection reset and calls user callback func... |
| `SystemCoreClockUpdate` | INIT | False | Reads clock configuration registers to determine and update the system core clock frequency |
| `USART_TransferReceiveNonBlocking` | RECV | False | Receives data using interrupt method (non-blocking), either from ring buffer or by enabling RX interrupts for direct ... |
| `USART_TransferSendNonBlocking` | INIT | False | Initiates non-blocking USART data transmission using interrupts by setting up transfer parameters and enabling transm... |
| `add_to_waitq_locked` | CORE | False | Adds a thread to a wait queue while holding scheduler spinlock, marking it as pending and unready |
| `adjust_owner_prio` | CORE | False | Adjusts the priority of a mutex owner thread as part of mutex lock/unlock operations |
| `arch_new_thread` | CORE | False | Initializes a new thread context for ARM Cortex-M architecture by setting up the initial exception stack frame and th... |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating point values to text format with various format specifiers (f, e, g,... |
| `findPll0MMult` | RETURNOK | False | Reads PLL0 multiplier configuration from SYSCON registers and calculates the multiplier value for clock generation |
| `findPll0PostDiv` | RETURNOK | False | Reads PLL0 post-divider settings from hardware registers to determine the post-divider value for clock configuration |
| `findPll0PreDiv` | RETURNOK | False | Reads PLL0 pre-divider (N) value from hardware registers to determine current clock configuration |
| `findPll1MMult` | RETURNOK | False | Reads the PLL1 M multiplier value from the SYSCON PLL1MDEC hardware register |
| `findPll1PostDiv` | INIT | False | Reads PLL1 configuration registers to determine the post-divider value for PLL1 clock configuration |
| `findPll1PreDiv` | RETURNOK | False | Reads PLL1 pre-divider configuration from hardware registers to determine the current NDEC setting |
| `first` | NODRIVER | False | Returns the first timeout structure from the kernel's timeout linked list |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (_THREAD_DEAD or _THREAD_SUSPENDED) as part of kernel threa... |
| `init_ready_q` | CORE | False | Initializes the ready queue data structure for the kernel scheduler |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap structure with provided memory region, setting up wait queue and system heap |
| `k_mbox_get` | NODRIVER | False | Zephyr RTOS mailbox receive function that retrieves messages from a mailbox queue, searching for compatible senders a... |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox data structure for inter-thread communication |
| `k_mem_slab_init` | NODRIVER | False | Initializes a memory slab object in Zephyr RTOS kernel by setting up metadata, creating free list, and registering wi... |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a Zephyr message queue by checking for waiting threads and freeing allocated buffer if dynamically allocated |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr kernel message queue data structure by setting up buffer pointers, size parameters, and internal... |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated memory if needed |
| `k_stack_init` | NODRIVER | False | Initializes a fixed-size stack object in the Zephyr kernel by setting up wait queue, spinlock, and stack pointers. |
| `k_timer_init` | NODRIVER | False | Initializes a kernel timer structure by setting callback functions, status, wait queue, timeout structure, and perfor... |
| `k_work_cancel_delayable_sync` | NODRIVER | False | Cancels a delayed work item synchronously in Zephyr RTOS, checking if work is pending and waiting for cancellation co... |
| `k_work_cancel_sync` | NODRIVER | False | Synchronously cancels a work item in Zephyr RTOS, waiting for completion if the work is currently running |
| `k_work_flush` | NODRIVER | False | Flushes a work item, waiting for completion if the work is queued or running |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item, waiting for it to complete if necessary in Zephyr RTOS kernel work queue system |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item in the Zephyr RTOS kernel by setting up the work structure with handler and flags, ... |
| `k_work_queue_start` | CORE | False | Starts a work queue thread in Zephyr RTOS by initializing work queue data structures and creating/starting a kernel t... |
| `lf_get_deepsleep_core_supply_cfg` | INIT | False | Configures digital core logic supply source for deep sleep mode, setting DCDC voltage based on whether USB High Speed... |
| `lf_set_dcdc_power_profile_low` | INIT | False | Configures DCDC power profile for low power mode by reading trim values from flash/OTP and applying them to DCDC regi... |
| `lf_wakeup_io_ctrl` | INIT | False | Configures wake-up I/O control for low-power modes by setting pull-up/pull-down resistors on specific GPIO pins based... |
| `lowpower_set_dcdc_power_profile` | INIT | False | Sets DCDC power profile by configuring PMC registers for low, medium, or high power modes |
| `lowpower_set_system_voltage` | INIT | False | Sets system voltage levels for power management by configuring LDO and DCDC voltage regulators based on input voltage... |
| `mbox_message_put` | NODRIVER | False | Helper function for sending mailbox messages that handles both synchronous and asynchronous sends by managing thread ... |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the Zephyr RTOS scheduler |
| `mpu_init` | INIT | True | Configures cache-ability attributes for different types of memory regions in the MPU (Memory Protection Unit) |
| `next` | NODRIVER | False | Returns the next timeout structure in the kernel's timeout linked list |
| `nxp_lpc55xxx_init` | INIT | True | Performs basic hardware initialization for NXP LPC55xxx SOCs including clearing ARM faults, initializing system clock... |
| `pinctrl_clock_init` | INIT | False | Enables the IOCon clock for LPC family microcontrollers (except 11u6x) during system initialization |
| `pllFindSel` | INIT | False | Calculates SELP, SELI, and SELR values for PLL configuration based on multiplier M and PLL operating mode |
| `ready_thread` | CORE | False | Marks a thread as ready to run by adding it to the run queue if not already queued and in ready state |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout linked list and adjusts delta ticks of the next timeout if pres... |
| `timeout_rem` | NODRIVER | False | Calculates remaining ticks for a timeout by traversing the timeout list and subtracting elapsed time from the SysTick... |
| `update_cache` | NODRIVER | False | Updates the scheduler's cache of the next thread to run based on preemption decisions in the Zephyr RTOS kernel. |
| `z_abort_timeout` | NODRIVER | False | Cancels/aborts a timeout from the kernel's timeout queue by removing it if it's currently scheduled |
| `z_add_timeout` | INIT | True | Adds a timeout to the kernel's timeout list, managing timeout scheduling and interacting with hardware timers |
| `z_arm_platform_init` | CORE | False | Initializes ARM platform by calling system initialization and optionally disabling trace clock when SWO logging backe... |
| `z_cbvprintf_impl` | NODRIVER | False | Formatted output implementation function that processes format strings and variable arguments, converting them to cha... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr RTOS condition variable by setting up its wait queue and kernel object tracking. |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a Zephyr RTOS mutex structure by setting owner to NULL, lock count to 0, initializing wait queue, and per... |
| `z_impl_k_mutex_lock` | NODRIVER | False | Zephyr RTOS mutex lock implementation with priority inheritance, handles thread synchronization and waiting |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a Zephyr kernel queue data structure by setting up internal lists, locks, wait queues, and kernel object ... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a Zephyr RTOS semaphore object by setting its count, limit, and initializing associated data structures |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Zephyr RTOS kernel timer synchronization function that waits for timer expiration and returns status |
| `z_impl_k_yield` | CORE | False | Zephyr RTOS kernel function that implements thread yielding by triggering a PendSV exception for context switching |
| `z_init_thread_base` | NODRIVER | False | Initializes the basic thread control block structure (_thread_base) with priority, state, options, and other thread m... |
| `z_priq_dumb_best` | CORE | False | Returns the best thread from a priority queue for scheduler decisions |
| `z_priq_dumb_remove` | NODRIVER | False | Removes a thread from a priority queue by removing it from a doubly-linked list |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue for the scheduler |
| `z_sched_waitq_walk` | CORE | False | Walks through a wait queue and invokes a callback function on each waiting thread in the scheduler |
| `z_set_prio` | CORE | False | Thread priority set utility that changes run queue state without rescheduling, returning true if rescheduling is need... |
| `z_setup_new_thread` | NODRIVER | False | Sets up a new thread by initializing thread data structures, configuring the stack, and calling architecture-specific... |
| `z_timer_expiration_handler` | CORE | False | Handles kernel timer expiration events, restarts periodic timers, invokes user expiry callbacks, and wakes up waiting... |
| `z_unpend_all` | CORE | False | Kernel scheduler function that removes all threads from a wait queue, marks them as ready, and returns whether schedu... |

## 附录：interesting MMIO expr 子集（共 13 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `CLOCK_AttachClk`
- `CLOCK_GetClockAttachId`
- `CLOCK_SetFLASHAccessCyclesForFreq`
- `CLOCK_SetPLL0Freq`
- `CLOCK_SetPLL1Freq`
- `CLOCK_SetupPLL0Prec`
- `PINT0_DriverIRQHandler`
- `PINT_DisableCallback`
- `PINT_EnableCallback`
- `PINT_PinInterruptClrStatusAll`
- `RESET_ClearPeripheralReset`
- `RESET_SetPeripheralReset`
- `nxp_pint_pin_enable`
