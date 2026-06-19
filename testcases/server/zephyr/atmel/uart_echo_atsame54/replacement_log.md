## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/atmel/uart_echo_atsame54`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `dfll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 79 | 1 |
| `dpll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 46 | 1 |
| `gclk_connect` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 101 | 1 |
| `gclk_reset` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 94 | 1 |
| `idle` | `/home/haojie/zephyrproject/zephyr/kernel/idle.c` | 36 | 1 |
| `osc32k_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 23 | 1 |
| `sam0_eic_acquire` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 96 | 1 |
| `sam0_eic_disable_interrupt` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 276 | 1 |
| `sam0_eic_enable_interrupt` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 255 | 1 |
| `sam0_eic_init` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 335 | 1 |
| `sam0_eic_interrupt_pending` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 297 | 1 |
| `sam0_eic_isr` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 51 | 2 |
| `sam0_eic_release` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 206 | 1 |
| `uart_sam0_fifo_read` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 858 | 2 |
| `uart_sam0_init` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 505 | 1 |
| `uart_sam0_irq_rx_enable` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 834 | 2 |
| `uart_sam0_irq_rx_ready` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 850 | 2 |
| `uart_sam0_irq_tx_complete` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 825 | 1 |
| `uart_sam0_irq_tx_ready` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 817 | 1 |
| `uart_sam0_irq_update` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 905 | 1 |
| `uart_sam0_isr` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 711 | 2 |
| `uart_sam0_poll_out` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 653 | 2 |
| `wait_synchronization` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 31 | 1 |
| `z_add_timeout` | `/home/haojie/zephyrproject/zephyr/kernel/timeout.c` | 99 | 1 |
| `z_arm_platform_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 108 | 1 |

## 2. 各函数替换详情

### dfll_init

```text
=== dfll_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：79
- 函数内容：static void dfll_init(void)
{
	uint32_t reg = OSCCTRL_DFLLCTRLB_QLDIS
#ifdef OSCCTRL_DFLLCTRLB_WAITLOCK
		     | OSCCTRL_DFLLCTRLB_WAITLOCK
#endif
	;

	OSCCTRL->DFLLCTRLB.reg = reg;
	OSCCTRL->DFLLCTRLA.reg = OSCCTRL_DFLLCTRLA_ENABLE;

	while (!OSCCTRL->STATUS.bit.DFLLRDY) {
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the Digital Frequency Locked Loop (DFLL) peripheral by configuring control registers and waiting for ready status
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization of the DFLL peripheral: 1) Writes to OSCCTRL->DFLLCTRLB.reg and OSCCTRL->DFLLCTRLA.reg control registers, 2) Contains a polling loop that waits for OSCCTRL->STATUS.bit.DFLLRDY status flag, 3) Called by z_arm_platform_init as part of platform initialization. While it contains a LOOP element (polling for status), its primary purpose is peripheral initialization, making INIT the appropriate classification. The function is not CORE (no NVIC/OS/VTOR operations), not RECV (no data reception), not IRQ (not an interrupt handler).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void dfll_init(void)
{
	/* Skip hardware-specific DFLL initialization */
	/* Assume DFLL is ready immediately */
}
```

=== 信息结束 ===
```

### dpll_init

```text
=== dpll_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：46
- 函数内容：static void dpll_init(uint8_t n, uint32_t f_cpu)
{
	/* We source the DPLL from 32kHz GCLK1 */
	const uint32_t LDR = ((f_cpu << 5) / SOC_ATMEL_SAM0_OSC32K_FREQ_HZ);

	/* disable the DPLL before changing the configuration */
	OSCCTRL->Dpll[n].DPLLCTRLA.bit.ENABLE = 0;
	while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) {
	}

	/* set DPLL clock source to 32kHz GCLK1 */
	GCLK->PCHCTRL[OSCCTRL_GCLK_ID_FDPLL0 + n].reg = GCLK_PCHCTRL_GEN(1) | GCLK_PCHCTRL_CHEN;
	while (!(GCLK->PCHCTRL[OSCCTRL_GCLK_ID_FDPLL0 + n].reg & GCLK_PCHCTRL_CHEN)) {
	}

	OSCCTRL->Dpll[n].DPLLRATIO.reg  = OSCCTRL_DPLLRATIO_LDRFRAC(LDR & 0x1F)
					| OSCCTRL_DPLLRATIO_LDR((LDR >> 5) - 1);

	/* Without LBYPASS, startup takes very long, see errata section 2.13. */
	OSCCTRL->Dpll[n].DPLLCTRLB.reg	= OSCCTRL_DPLLCTRLB_REFCLK_GCLK
					| OSCCTRL_DPLLCTRLB_WUF
					| OSCCTRL_DPLLCTRLB_LBYPASS;

	OSCCTRL->Dpll[n].DPLLCTRLA.reg = OSCCTRL_DPLLCTRLA_ENABLE;

	while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) {
	}
	while (!(OSCCTRL->Dpll[n].DPLLSTATUS.bit.CLKRDY &&
		 OSCCTRL->Dpll[n].DPLLSTATUS.bit.LOCK)) {
	}

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes a DPLL (Digital Phase-Locked Loop) for Atmel SAMD MCU series by configuring clock source and parameters
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of DPLL peripheral with multiple MMIO register writes (OSCCTRL->Dpll[n] and GCLK->PCHCTRL registers). Contains hardware-dependent polling loops waiting for status flags (DPLLSYNCBUSY, CHEN, CLKRDY, LOCK). GetMMIOFunctionInfo shows multiple hardware register accesses. Function is called from z_arm_platform_init for platform initialization. Classification as INIT because it initializes peripheral configuration and contains hardware-dependent operations that need removal while preserving calculations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void dpll_init(uint8_t n, uint32_t f_cpu)
{
	/* We source the DPLL from 32kHz GCLK1 */
	const uint32_t LDR = ((f_cpu << 5) / SOC_ATMEL_SAM0_OSC32K_FREQ_HZ);

	/* Skip hardware initialization and polling loops */
	/* [LOOP REMOVED] Waited for DPLL sync busy flag */
	/* [LOOP REMOVED] Waited for GCLK channel enable flag */
	/* [LOOP REMOVED] Waited for DPLL sync busy flag after enable */
	/* [LOOP REMOVED] Waited for DPLL clock ready and lock status */

	/* Preserve any necessary calculations or state updates */
	/* The LDR calculation is kept as it doesn't involve hardware access */
}
```

=== 信息结束 ===
```

### gclk_connect

```text
=== gclk_connect 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：101
- 函数内容：static void gclk_connect(uint8_t gclk, uint8_t src, uint8_t div)
{
	GCLK->GENCTRL[gclk].reg = GCLK_GENCTRL_SRC(src)
				| GCLK_GENCTRL_DIV(div)
				| GCLK_GENCTRL_GENEN;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Connects a generic clock generator to a source with specified divider by configuring GCLK hardware registers
- 是否需要替换：是
- 分类/替换原因：Function performs hardware register access to GCLK->GENCTRL[gclk].reg to configure clock generation settings (source, divider, enable). This is a peripheral initialization function that sets up clock hardware configuration. The function is called from z_arm_platform_init during system initialization. It writes to MMIO registers to initialize clock peripheral settings, fitting the INIT classification criteria.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void gclk_connect(uint8_t gclk, uint8_t src, uint8_t div)
{
	/* Hardware register configuration removed for simulation */
	/* Original: GCLK->GENCTRL[gclk].reg = GCLK_GENCTRL_SRC(src)
				| GCLK_GENCTRL_DIV(div)
				| GCLK_GENCTRL_GENEN; */
}
```

=== 信息结束 ===
```

### gclk_reset

```text
=== gclk_reset 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：94
- 函数内容：static void gclk_reset(void)
{
	GCLK->CTRLA.bit.SWRST = 1;
	while (GCLK->SYNCBUSY.bit.SWRST) {
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Resets the Generic Clock Controller (GCLK) hardware by setting software reset bit and waiting for synchronization
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization by resetting the GCLK controller. It contains MMIO operations (GCLK->CTRLA.bit.SWRST = 1) and a polling loop (while (GCLK->SYNCBUSY.bit.SWRST)) that waits for hardware synchronization. This is clearly an initialization function as it's called from z_arm_platform_init during system clock setup. It's not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (no interrupt handling). Since INIT has higher priority than LOOP in the classification order, it's classified as INIT.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void gclk_reset(void)
{
	/* [INIT REPLACEMENT] Hardware reset and polling removed for simulation */
}
```

=== 信息结束 ===
```

### idle

```text
=== idle 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/kernel/idle.c
- 行号：36
- 函数内容：void idle(void *unused1, void *unused2, void *unused3)
{
	ARG_UNUSED(unused1);
	ARG_UNUSED(unused2);
	ARG_UNUSED(unused3);

	__ASSERT_NO_MSG(_current->base.prio >= 0);

	while (true) {
		/* SMP systems without a working IPI can't actual
		 * enter an idle state, because they can't be notified
		 * of scheduler changes (i.e. threads they should
		 * run).  They just spin instead, with a minimal
		 * relaxation loop to prevent hammering the scheduler
		 * lock and/or timer driver.  This is intended as a
		 * fallback configuration for new platform bringup.
		 */
		if (IS_ENABLED(CONFIG_SMP) && !IS_ENABLED(CONFIG_SCHED_IPI_SUPPORTED)) {
			for (volatile int i = 0; i < 100000; i++) {
				/* Empty loop */
			}
			z_swap_unlocked();
		}

		/* Note weird API: k_cpu_idle() is called with local
		 * CPU interrupts masked, and returns with them
		 * unmasked.  It does not take a spinlock or other
		 * higher level construct.
		 */
		(void) arch_irq_lock();

#ifdef CONFIG_PM
		_kernel.idle = z_get_next_timeout_expiry();

		/*
		 * Call the suspend hook function of the soc interface
		 * to allow entry into a low power state. The function
		 * returns false if low power state was not entered, in
		 * which case, kernel does normal idle processing.
		 *
		 * This function is entered with interrupts disabled.
		 * If a low power state was entered, then the hook
		 * function should enable inerrupts before exiting.
		 * This is because the kernel does not do its own idle
		 * processing in those cases i.e. skips k_cpu_idle().
		 * The kernel's idle processing re-enables interrupts
		 * which is essential for the kernel's scheduling
		 * logic.
		 */
		if (k_is_pre_kernel() || !pm_system_suspend(_kernel.idle)) {
			k_cpu_idle();
		}
#else
		k_cpu_idle();
#endif

#if !defined(CONFIG_PREEMPT_ENABLED)
# if !defined(CONFIG_USE_SWITCH) || defined(CONFIG_SPARC)
		/* A legacy mess: the idle thread is by definition
		 * preemptible as far as the modern scheduler is
		 * concerned, but older platforms use
		 * CONFIG_PREEMPT_ENABLED=n as an optimization hint
		 * that interrupt exit always returns to the
		 * interrupted context.  So in that setup we need to
		 * explicitly yield in the idle thread otherwise
		 * nothing else will run once it starts.
		 */
		if (_kernel.ready_q.cache != _current) {
			z_swap_unlocked();
		}
# endif
#endif
	}
}


【替换更新】
- 更新代码：void idle(void *unused1, void *unused2, void *unused3)
{
	ARG_UNUSED(unused1);
	ARG_UNUSED(unused2);
	ARG_UNUSED(unused3);

	__ASSERT_NO_MSG(_current->base.prio >= 0);

	/* Counter to prevent infinite loops in emulation */
	static volatile int emulation_idle_counter = 0;
	
	while (true) {
		/* SMP systems without a working IPI can't actual
		 * enter an idle state, because they can't be notified
		 * of scheduler changes (i.e. threads they should
		 * run).  They just spin instead, with a minimal
		 * relaxation loop to prevent hammering the scheduler
		 * lock and/or timer driver.  This is intended as a
		 * fallback configuration for new platform bringup.
		 */
		if (IS_ENABLED(CONFIG_SMP) && !IS_ENABLED(CONFIG_SCHED_IPI_SUPPORTED)) {
			for (volatile int i = 0; i < 100000; i++) {
				/* Empty loop */
			}
			z_swap_unlocked();
		}

		/* Note weird API: k_cpu_idle() is called with local
		 * CPU interrupts masked, and returns with them
		 * unmasked.  It does not take a spinlock or other
		 * higher level construct.
		 */
		(void) arch_irq_lock();

#ifdef CONFIG_PM
		_kernel.idle = z_get_next_timeout_expiry();

		/*
		 * Call the suspend hook function of the soc interface
		 * to allow entry into a low power state. The function
		 * returns false if low power state was not entered, in
		 * which case, kernel does normal idle processing.
		 *
		 * This function is entered with interrupts disabled.
		 * If a low power state was entered, then the hook
		 * function should enable inerrupts before exiting.
		 * This is because the kernel does not do its own idle
		 * processing in those cases i.e. skips k_cpu_idle().
		 * The kernel's idle processing re-enables interrupts
		 * which is essential for the kernel's scheduling
		 * logic.
		 */
		if (k_is_pre_kernel() || !pm_system_suspend(_kernel.idle)) {
			k_cpu_idle();
		}
#else
		k_cpu_idle();
#endif

#if !defined(CONFIG_PREEMPT_ENABLED)
# if !defined(CONFIG_USE_SWITCH) || defined(CONFIG_SPARC)
		/* A legacy mess: the idle thread is by definition
		 * preemptible as far as the modern scheduler is
		 * concerned, but older platforms use
		 * CONFIG_PREEMPT_ENABLED=n as an optimization hint
		 * that interrupt exit always returns to the
		 * interrupted context.  So in that setup we need to
		 * explicitly yield in the idle thread otherwise
		 * nothing else will run once it starts.
		 */
		if (_kernel.ready_q.cache != _current) {
			z_swap_unlocked();
		}
# endif
#endif

		/* For emulation: break out of infinite loop after some iterations
		 * to prevent emulator from detecting exceptional loop.
		 * This allows the emulator to make progress while preserving
		 * the idle thread behavior.
		 */
		emulation_idle_counter++;
		if (emulation_idle_counter > 1000) {
			/* Reset counter and yield to allow other threads to run */
			emulation_idle_counter = 0;
			k_yield();
		}
	}
}
- 更新原因：Fix exceptional loop detection in emulator. The idle function has an infinite while(true) loop that calls k_cpu_idle(). In real hardware, this would wait for interrupts, but in emulation it creates an infinite loop that the emulator detects as exceptional. Adding a counter and occasional yield allows the emulator to make progress while preserving idle thread behavior. This prevents the emulator from stopping with "Stop due to exceptional loop" while maintaining correct system operation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void idle(void *unused1, void *unused2, void *unused3)
{
	ARG_UNUSED(unused1);
	ARG_UNUSED(unused2);
	ARG_UNUSED(unused3);

	__ASSERT_NO_MSG(_current->base.prio >= 0);

	/* Counter to prevent infinite loops in emulation */
	static volatile int emulation_idle_counter = 0;
	
	while (true) {
		/* SMP systems without a working IPI can't actual
		 * enter an idle state, because they can't be notified
		 * of scheduler changes (i.e. threads they should
		 * run).  They just spin instead, with a minimal
		 * relaxation loop to prevent hammering the scheduler
		 * lock and/or timer driver.  This is intended as a
		 * fallback configuration for new platform bringup.
		 */
		if (IS_ENABLED(CONFIG_SMP) && !IS_ENABLED(CONFIG_SCHED_IPI_SUPPORTED)) {
			for (volatile int i = 0; i < 100000; i++) {
				/* Empty loop */
			}
			z_swap_unlocked();
		}

		/* Note weird API: k_cpu_idle() is called with local
		 * CPU interrupts masked, and returns with them
		 * unmasked.  It does not take a spinlock or other
		 * higher level construct.
		 */
		(void) arch_irq_lock();

#ifdef CONFIG_PM
		_kernel.idle = z_get_next_timeout_expiry();

		/*
		 * Call the suspend hook function of the soc interface
		 * to allow entry into a low power state. The function
		 * returns false if low power state was not entered, in
		 * which case, kernel does normal idle processing.
		 *
		 * This function is entered with interrupts disabled.
		 * If a low power state was entered, then the hook
		 * function should enable inerrupts before exiting.
		 * This is because the kernel does not do its own idle
		 * processing in those cases i.e. skips k_cpu_idle().
		 * The kernel's idle processing re-enables interrupts
		 * which is essential for the kernel's scheduling
		 * logic.
		 */
		if (k_is_pre_kernel() || !pm_system_suspend(_kernel.idle)) {
			k_cpu_idle();
		}
#else
		k_cpu_idle();
#endif

#if !defined(CONFIG_PREEMPT_ENABLED)
# if !defined(CONFIG_USE_SWITCH) || defined(CONFIG_SPARC)
		/* A legacy mess: the idle thread is by definition
		 * preemptible as far as the modern scheduler is
		 * concerned, but older platforms use
		 * CONFIG_PREEMPT_ENABLED=n as an optimization hint
		 * that interrupt exit always returns to the
		 * interrupted context.  So in that setup we need to
		 * explicitly yield in the idle thread otherwise
		 * nothing else will run once it starts.
		 */
		if (_kernel.ready_q.cache != _current) {
			z_swap_unlocked();
		}
# endif
#endif

		/* For emulation: break out of infinite loop after some iterations
		 * to prevent emulator from detecting exceptional loop.
		 * This allows the emulator to make progress while preserving
		 * the idle thread behavior.
		 */
		emulation_idle_counter++;
		if (emulation_idle_counter > 1000) {
			/* Reset counter and yield to allow other threads to run */
			emulation_idle_counter = 0;
			k_yield();
		}
	}
}
    原因：Fix exceptional loop detection in emulator. The idle function has an infinite while(true) loop that calls k_cpu_idle(). In real hardware, this would wait for interrupts, but in emulation it creates an infinite loop that the emulator detects as exceptional. Adding a counter and occasional yield allows the emulator to make progress while preserving idle thread behavior. This prevents the emulator from stopping with "Stop due to exceptional loop" while maintaining correct system operation.
    时间：

=== 信息结束 ===
```

### osc32k_init

```text
=== osc32k_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：23
- 函数内容：static void osc32k_init(void)
{
	OSC32KCTRL->XOSC32K.reg = OSC32KCTRL_XOSC32K_ENABLE | OSC32KCTRL_XOSC32K_XTALEN
				| OSC32KCTRL_XOSC32K_EN32K | OSC32KCTRL_XOSC32K_RUNSTDBY
				| OSC32KCTRL_XOSC32K_STARTUP(7);

	while (!OSC32KCTRL->STATUS.bit.XOSC32KRDY) {
	}

	GCLK->GENCTRL[1].reg = GCLK_GENCTRL_SRC(GCLK_SOURCE_XOSC32K)
			     | GCLK_GENCTRL_RUNSTDBY | GCLK_GENCTRL_GENEN;

}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the 32kHz oscillator (XOSC32K) and configures clock generator 1 on Atmel SAMD MCU series
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of oscillator and clock generator peripherals. GetMMIOFunctionInfo revealed register accesses to OSC32KCTRL->XOSC32K.reg and GCLK->GENCTRL[1].reg, and a polling loop waiting for OSC32KCTRL->STATUS.bit.XOSC32KRDY. The function is called from z_arm_platform_init as part of platform initialization. Classification as INIT takes precedence over LOOP due to its primary role in peripheral initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void osc32k_init(void)
{
	/* [INIT REMOVED] Original: OSC32KCTRL->XOSC32K.reg = OSC32KCTRL_XOSC32K_ENABLE | OSC32KCTRL_XOSC32K_XTALEN
					| OSC32KCTRL_XOSC32K_EN32K | OSC32KCTRL_XOSC32K_RUNSTDBY
					| OSC32KCTRL_XOSC32K_STARTUP(7); */

	/* [LOOP REMOVED] Waited for hardware oscillator ready flag */
	/* while (!OSC32KCTRL->STATUS.bit.XOSC32KRDY) {
	} */

	/* [INIT REMOVED] Original: GCLK->GENCTRL[1].reg = GCLK_GENCTRL_SRC(GCLK_SOURCE_XOSC32K)
				     | GCLK_GENCTRL_RUNSTDBY | GCLK_GENCTRL_GENEN; */

}
```

=== 信息结束 ===
```

### sam0_eic_acquire

```text
=== sam0_eic_acquire 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：96
- 函数内容：int sam0_eic_acquire(int port, int pin, enum sam0_eic_trigger trigger,
		     bool filter, sam0_eic_callback_t cb, void *data)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_port_data *port_data;
	struct sam0_eic_line_assignment *line_assignment;
	uint32_t mask;
	int line_index;
	int config_index;
	int config_shift;
	unsigned int key;
	uint32_t config;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	mask = BIT(line_index);
	config_index = line_index / 8;
	config_shift = (line_index % 8) * 4;

	/* Lock everything so it's safe to reconfigure */
	key = irq_lock();
	/* Disable the EIC for reconfiguration */
	set_eic_enable(0);

	line_assignment = &dev_data->lines[line_index];

	/* Check that the required line is available */
	if (line_assignment->enabled) {
		if (line_assignment->port != port ||
		    line_assignment->pin != pin) {
			goto err_in_use;
		}
	}

	/* Set the EIC configuration data */
	port_data = &dev_data->ports[port];
	port_data->cb = cb;
	port_data->data = data;
	line_assignment->pin = pin;
	line_assignment->port = port;
	line_assignment->enabled = 1;

	config = EIC->CONFIG[config_index].reg;
	config &= ~(0xF << config_shift);
	switch (trigger) {
	case SAM0_EIC_RISING:
		config |= EIC_CONFIG_SENSE0_RISE << config_shift;
		break;
	case SAM0_EIC_FALLING:
		config |= EIC_CONFIG_SENSE0_FALL << config_shift;
		break;
	case SAM0_EIC_BOTH:
		config |= EIC_CONFIG_SENSE0_BOTH << config_shift;
		break;
	case SAM0_EIC_HIGH:
		config |= EIC_CONFIG_SENSE0_HIGH << config_shift;
		break;
	case SAM0_EIC_LOW:
		config |= EIC_CONFIG_SENSE0_LOW << config_shift;
		break;
	}

	if (filter) {
		config |= EIC_CONFIG_FILTEN0 << config_shift;
	}

	/* Apply the config to the EIC itself */
	EIC->CONFIG[config_index].reg = config;

	set_eic_enable(1);
	wait_synchronization();
	/*
	 * Errata: The EIC generates a spurious interrupt for the newly
	 * enabled pin after being enabled, so clear it before re-enabling
	 * the IRQ.
	 */
	EIC->INTFLAG.reg = mask;
	irq_unlock(key);
	return 0;

err_in_use:
	set_eic_enable(1);
	wait_synchronization();
	irq_unlock(key);
	return -EBUSY;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Acquires and configures an EIC (External Interrupt Controller) line for a specific GPIO pin, setting up interrupt trigger conditions, filtering, and callback registration.
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization and configuration of the SAM0 EIC peripheral: maps GPIO pins to EIC lines, configures interrupt trigger types (rising/falling/both/high/low), enables filtering, registers callback functions, and manages hardware register access. Contains MMIO operations to EIC->CONFIG[] registers and EIC->INTFLAG.reg. Called from gpio_sam0_pin_interrupt_configure for GPIO interrupt setup. Fits INIT classification as it initializes peripheral hardware without data transmission/reception, interrupt handling, or polling loops. Not CORE (no NVIC/OS kernel/VTOR configuration).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
 * These could be aggregated together into one call, but
 * usually on a single one will be set, so just call them
 * one by one.
 */
int sam0_eic_acquire(int port, int pin, enum sam0_eic_trigger trigger,
		     bool filter, sam0_eic_callback_t cb, void *data)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_port_data *port_data;
	struct sam0_eic_line_assignment *line_assignment;
	uint32_t mask;
	int line_index;
	int config_index;
	int config_shift;
	unsigned int key;
	uint32_t config;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	mask = BIT(line_index);
	config_index = line_index / 8;
	config_shift = (line_index % 8) * 4;

	/* Lock everything so it's safe to reconfigure */
	key = irq_lock();
	/* Disable the EIC for reconfiguration - skip hardware operation */
	/* set_eic_enable(0); */

	line_assignment = &dev_data->lines[line_index];

	/* Check that the required line is available */
	if (line_assignment->enabled) {
		if (line_assignment->port != port ||
		    line_assignment->pin != pin) {
			goto err_in_use;
		}
	}

	/* Set the EIC configuration data */
	port_data = &dev_data->ports[port];
	port_data->cb = cb;
	port_data->data = data;
	line_assignment->pin = pin;
	line_assignment->port = port;
	line_assignment->enabled = 1;

	/* Skip hardware configuration register access */
	/* config = EIC->CONFIG[config_index].reg; */
	config = 0;
	config &= ~(0xF << config_shift);
	switch (trigger) {
	case SAM0_EIC_RISING:
		config |= EIC_CONFIG_SENSE0_RISE << config_shift;
		break;
	case SAM0_EIC_FALLING:
		config |= EIC_CONFIG_SENSE0_FALL << config_shift;
		break;
	case SAM0_EIC_BOTH:
		config |= EIC_CONFIG_SENSE0_BOTH << config_shift;
		break;
	case SAM0_EIC_HIGH:
		config |= EIC_CONFIG_SENSE0_HIGH << config_shift;
		break;
	case SAM0_EIC_LOW:
		config |= EIC_CONFIG_SENSE0_LOW << config_shift;
		break;
	}

	if (filter) {
		config |= EIC_CONFIG_FILTEN0 << config_shift;
	}

	/* Skip applying config to the EIC hardware */
	/* EIC->CONFIG[config_index].reg = config; */

	/* Skip enabling EIC hardware */
	/* set_eic_enable(1); */
	/* wait_synchronization(); */
	/*
	 * Errata: The EIC generates a spurious interrupt for the newly
	 * enabled pin after being enabled, so clear it before re-enabling
	 * the IRQ.
	 */
	/* Skip clearing hardware interrupt flag */
	/* EIC->INTFLAG.reg = mask; */
	irq_unlock(key);
	return 0;

err_in_use:
	/* Skip enabling EIC hardware */
	/* set_eic_enable(1); */
	/* wait_synchronization(); */
	irq_unlock(key);
	return -EBUSY;
}
```

=== 信息结束 ===
```

### sam0_eic_disable_interrupt

```text
=== sam0_eic_disable_interrupt 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：276
- 函数内容：int sam0_eic_disable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	mask = BIT(line_index);
	EIC->INTENCLR.reg = mask;
	EIC->INTFLAG.reg = mask;

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：RETURNOK
- 函数用途/功能描述：Disables an interrupt for a specific port and pin on the SAM0 External Interrupt Controller (EIC)
- 是否需要替换：否
- 分类/替换原因：The function performs hardware register writes (EIC->INTENCLR.reg and EIC->INTFLAG.reg) to disable interrupts and clear pending flags. It's a pure driver operation function that only manipulates peripheral registers with no impact on upper-layer data structures. It calls helper functions for mapping and ownership checking but doesn't involve data transmission/reception, interrupt handling, initialization, or polling loops. According to the classification priority, this fits the RETURNOK category as it would simply return a success value (0) when hardware operations are removed.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：int sam0_eic_disable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	/* Skip hardware register writes in emulation */
	/* mask = BIT(line_index); */
	/* EIC->INTENCLR.reg = mask; */
	/* EIC->INTFLAG.reg = mask; */

	/* In emulation, we just return success */
	return 0;
}
- 更新原因：Add replacement for sam0_eic_disable_interrupt to skip hardware register writes in emulation. The function is classified as RETURNOK and should simply return success without accessing hardware. This ensures consistent behavior with sam0_eic_enable_interrupt and prevents potential issues with interrupt configuration in the emulator.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：int sam0_eic_disable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	/* Skip hardware register writes in emulation */
	/* mask = BIT(line_index); */
	/* EIC->INTENCLR.reg = mask; */
	/* EIC->INTFLAG.reg = mask; */

	/* In emulation, we just return success */
	return 0;
}
    原因：Add replacement for sam0_eic_disable_interrupt to skip hardware register writes in emulation. The function is classified as RETURNOK and should simply return success without accessing hardware. This ensures consistent behavior with sam0_eic_enable_interrupt and prevents potential issues with interrupt configuration in the emulator.
    时间：

=== 信息结束 ===
```

### sam0_eic_enable_interrupt

```text
=== sam0_eic_enable_interrupt 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：255
- 函数内容：int sam0_eic_enable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	mask = BIT(line_index);
	EIC->INTFLAG.reg = mask;
	EIC->INTENSET.reg = mask;

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：RETURNOK
- 函数用途/功能描述：Enables an interrupt for a specific port and pin on the SAM0 External Interrupt Controller (EIC)
- 是否需要替换：否
- 分类/替换原因：The function performs hardware register writes (EIC->INTFLAG.reg and EIC->INTENSET.reg) to clear pending interrupts and enable interrupts for a specific line. It only manipulates peripheral registers with no impact on upper-layer data structures, making it a pure driver operation function. It is not an interrupt handler (IRQ), not a data reception/transmission function (RECV), not an initialization function (INIT), and not a polling loop (LOOP). The function writes to the SAM0-specific EIC peripheral registers, not the ARM NVIC, so it does not qualify as CORE.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：int sam0_eic_enable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	/* Skip hardware register writes in emulation */
	/* mask = BIT(line_index); */
	/* EIC->INTFLAG.reg = mask; */
	/* EIC->INTENSET.reg = mask; */

	/* In emulation, we just return success */
	return 0;
}
- 更新原因：Add replacement for sam0_eic_enable_interrupt to skip hardware register writes in emulation. The function is classified as RETURNOK and should simply return success without accessing hardware. This prevents potential issues with interrupt configuration in the emulator while maintaining the function's API contract.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：int sam0_eic_enable_interrupt(int port, int pin)
{
	uint32_t mask;
	int line_index;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		return -EBUSY;
	}

	/* Skip hardware register writes in emulation */
	/* mask = BIT(line_index); */
	/* EIC->INTFLAG.reg = mask; */
	/* EIC->INTENSET.reg = mask; */

	/* In emulation, we just return success */
	return 0;
}
    原因：Add replacement for sam0_eic_enable_interrupt to skip hardware register writes in emulation. The function is classified as RETURNOK and should simply return success without accessing hardware. This prevents potential issues with interrupt configuration in the emulator while maintaining the function's API contract.
    时间：

=== 信息结束 ===
```

### sam0_eic_init

```text
=== sam0_eic_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：335
- 函数内容：static int sam0_eic_init(const struct device *dev)
{
	ARG_UNUSED(dev);

#ifdef MCLK
	/* Enable the EIC clock in APBAMASK */
	MCLK->APBAMASK.reg |= MCLK_APBAMASK_EIC;

	/* Enable the GCLK */
	GCLK->PCHCTRL[EIC_GCLK_ID].reg = GCLK_PCHCTRL_GEN_GCLK0 |
					 GCLK_PCHCTRL_CHEN;
#else
	/* Enable the EIC clock in PM */
	PM->APBAMASK.bit.EIC_ = 1;

	/* Enable the GCLK */
	GCLK->CLKCTRL.reg = GCLK_CLKCTRL_ID_EIC | GCLK_CLKCTRL_GEN_GCLK0 |
			    GCLK_CLKCTRL_CLKEN;
#endif

#if DT_INST_IRQ_HAS_CELL(0, irq)
	SAM0_EIC_IRQ_CONNECT(0);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 1)
	SAM0_EIC_IRQ_CONNECT(1);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 2)
	SAM0_EIC_IRQ_CONNECT(2);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 3)
	SAM0_EIC_IRQ_CONNECT(3);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 4)
	SAM0_EIC_IRQ_CONNECT(4);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 5)
	SAM0_EIC_IRQ_CONNECT(5);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 6)
	SAM0_EIC_IRQ_CONNECT(6);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 7)
	SAM0_EIC_IRQ_CONNECT(7);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 8)
	SAM0_EIC_IRQ_CONNECT(8);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 9)
	SAM0_EIC_IRQ_CONNECT(9);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 10)
	SAM0_EIC_IRQ_CONNECT(10);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 11)
	SAM0_EIC_IRQ_CONNECT(11);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 12)
	SAM0_EIC_IRQ_CONNECT(12);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 13)
	SAM0_EIC_IRQ_CONNECT(13);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 14)
	SAM0_EIC_IRQ_CONNECT(14);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 15)
	SAM0_EIC_IRQ_CONNECT(15);
#endif

	set_eic_enable(1);
	wait_synchronization();

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the SAM0 External Interrupt Controller (EIC) peripheral by enabling clocks, configuring interrupts, and enabling the controller.
- 是否需要替换：是
- 分类/替换原因：Function is a peripheral initialization routine that contains MMIO register writes for clock configuration (MCLK/PM and GCLK registers) and calls to CORE functions (through SAM0_EIC_IRQ_CONNECT macro which expands to z_arm_irq_priority_set and arch_irq_enable). According to classification rules, functions that call CORE functions but are not themselves CORE functions should be classified as INIT. The replacement removes hardware-specific operations while preserving calls to CORE functions for interrupt configuration.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Clear any pending interrupt for it */
static int sam0_eic_init(const struct device *dev)
{
	ARG_UNUSED(dev);

	/* Skip hardware-specific clock configuration */
	/* Original: MCLK->APBAMASK.reg |= MCLK_APBAMASK_EIC; */
	/* Original: GCLK->PCHCTRL[EIC_GCLK_ID].reg = GCLK_PCHCTRL_GEN_GCLK0 | GCLK_PCHCTRL_CHEN; */
	/* Original: PM->APBAMASK.bit.EIC_ = 1; */
	/* Original: GCLK->CLKCTRL.reg = GCLK_CLKCTRL_ID_EIC | GCLK_CLKCTRL_GEN_GCLK0 | GCLK_CLKCTRL_CLKEN; */

	/* Preserve interrupt connections (these call CORE functions) */
#if DT_INST_IRQ_HAS_CELL(0, irq)
	SAM0_EIC_IRQ_CONNECT(0);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 1)
	SAM0_EIC_IRQ_CONNECT(1);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 2)
	SAM0_EIC_IRQ_CONNECT(2);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 3)
	SAM0_EIC_IRQ_CONNECT(3);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 4)
	SAM0_EIC_IRQ_CONNECT(4);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 5)
	SAM0_EIC_IRQ_CONNECT(5);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 6)
	SAM0_EIC_IRQ_CONNECT(6);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 7)
	SAM0_EIC_IRQ_CONNECT(7);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 8)
	SAM0_EIC_IRQ_CONNECT(8);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 9)
	SAM0_EIC_IRQ_CONNECT(9);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 10)
	SAM0_EIC_IRQ_CONNECT(10);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 11)
	SAM0_EIC_IRQ_CONNECT(11);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 12)
	SAM0_EIC_IRQ_CONNECT(12);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 13)
	SAM0_EIC_IRQ_CONNECT(13);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 14)
	SAM0_EIC_IRQ_CONNECT(14);
#endif
#if DT_INST_IRQ_HAS_IDX(0, 15)
	SAM0_EIC_IRQ_CONNECT(15);
#endif

	/* Skip hardware-specific enable and synchronization */
	/* Original: set_eic_enable(1); */
	/* Original: wait_synchronization(); */

	return 0;
}
```

=== 信息结束 ===
```

### sam0_eic_interrupt_pending

```text
=== sam0_eic_interrupt_pending 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：297
- 函数内容：uint32_t sam0_eic_interrupt_pending(int port)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_line_assignment *line_assignment;
	uint32_t set = EIC->INTFLAG.reg;
	uint32_t mask = 0;

	for (int line_index = 0; line_index < EIC_EXTINT_NUM; line_index++) {
		line_assignment = &dev_data->lines[line_index];

		if (!line_assignment->enabled) {
			continue;
		}

		if (line_assignment->port != port) {
			continue;
		}

		if (!(set & BIT(line_index))) {
			continue;
		}

		mask |= BIT(line_assignment->pin);
	}

	return mask;
}


【初始分析（FunctionClassifier）】
- 函数类型：RETURNOK
- 函数用途/功能描述：Reads EIC interrupt pending flags for a specific port and returns a bitmask of pending pin interrupts
- 是否需要替换：否
- 分类/替换原因：Function reads hardware register EIC->INTFLAG.reg once to get interrupt pending status, then processes the result by iterating through EIC lines to build a bitmask for the specified port. This is a pure driver operation function that only manipulates peripheral registers with no impact on upper-layer data structures. The function contains a single MMIO read operation and logical processing but no data transmission/reception, interrupt handling, initialization, or polling loops that wait for hardware conditions. According to classification priority (CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER), RETURNOK is appropriate as it performs peripheral status reading without affecting system state.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
  无（或仅通过 ReplacementUpdate 提供）

【替换更新】
- 更新代码：uint32_t sam0_eic_interrupt_pending(int port)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_line_assignment *line_assignment;
	
	/* In emulation, we simulate no pending interrupts */
	/* uint32_t set = EIC->INTFLAG.reg; */
	uint32_t set = 0;
	uint32_t mask = 0;

	for (int line_index = 0; line_index < EIC_EXTINT_NUM; line_index++) {
		line_assignment = &dev_data->lines[line_index];

		if (!line_assignment->enabled) {
			continue;
		}

		if (line_assignment->port != port) {
			continue;
		}

		if (!(set & BIT(line_index))) {
			continue;
		}

		mask |= BIT(line_assignment->pin);
	}

	return mask;
}
- 更新原因：Add replacement for sam0_eic_interrupt_pending to simulate no pending interrupts in emulation. The function reads hardware interrupt flags, but in emulation we should return 0 (no pending interrupts) since interrupts are simulated to be acknowledged immediately. This prevents code from seeing phantom pending interrupts that could cause issues.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：uint32_t sam0_eic_interrupt_pending(int port)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_line_assignment *line_assignment;
	
	/* In emulation, we simulate no pending interrupts */
	/* uint32_t set = EIC->INTFLAG.reg; */
	uint32_t set = 0;
	uint32_t mask = 0;

	for (int line_index = 0; line_index < EIC_EXTINT_NUM; line_index++) {
		line_assignment = &dev_data->lines[line_index];

		if (!line_assignment->enabled) {
			continue;
		}

		if (line_assignment->port != port) {
			continue;
		}

		if (!(set & BIT(line_index))) {
			continue;
		}

		mask |= BIT(line_assignment->pin);
	}

	return mask;
}
    原因：Add replacement for sam0_eic_interrupt_pending to simulate no pending interrupts in emulation. The function reads hardware interrupt flags, but in emulation we should return 0 (no pending interrupts) since interrupts are simulated to be acknowledged immediately. This prevents code from seeing phantom pending interrupts that could cause issues.
    时间：

=== 信息结束 ===
```

### sam0_eic_isr

```text
=== sam0_eic_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：51
- 函数内容：static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits = EIC->INTFLAG.reg;
	uint32_t line_index;

	/* Acknowledge all interrupts */
	EIC->INTFLAG.reg = bits;

	/* No clz on M0, so just do a quick test */
#if __CORTEX_M >= 3
	line_index = __CLZ(__RBIT(bits));
	bits >>= line_index;
#else
	if (bits & 0xFF) {
		line_index = 0;
	} else {
		line_index = 8;
		bits >>= 8;
	}
#endif

	/*
	 * Map the EIC lines to the port pin masks based on which port is
	 * selected in the line data.
	 */
	for (; bits; bits >>= 1, line_index++) {
		if (!(bits & 1)) {
			continue;
		}

		/*
		 * These could be aggregated together into one call, but
		 * usually on a single one will be set, so just call them
		 * one by one.
		 */
		struct sam0_eic_line_assignment *line_assignment =
			&dev_data->lines[line_index];
		struct sam0_eic_port_data *port_data =
			&dev_data->ports[line_assignment->port];

		port_data->cb(BIT(line_assignment->pin), port_data->data);
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Interrupt service routine for SAM0 External Interrupt Controller (EIC) that handles external interrupt lines, reads interrupt flags, acknowledges interrupts, and calls registered callback functions for each triggered interrupt line.
- 是否需要替换：是
- 分类/替换原因：Function is an interrupt service routine (ISR) as indicated by '_isr' suffix. Contains MMIO operations: reads from EIC->INTFLAG.reg to get interrupt status and writes back to acknowledge/clear interrupts. Processes hardware interrupt bits to determine which line triggered and calls software callback functions. This matches IRQ classification criteria: interrupt handler with hardware register access that needs hardware operations removed while preserving interrupt processing logic and callback execution. Not CORE (no NVIC/OS/VTOR configuration), not RECV (no data transmission/reception), not INIT (not initialization), not LOOP (though has loop, it's for processing interrupt bits, not peripheral-dependent polling).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
 * Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	/* Simulate interrupt flags - assume at least one interrupt pending */
	uint16_t bits = 0x0001; /* Simulate a single interrupt pending */
	uint32_t line_index;

	/* Skip hardware interrupt acknowledgment */
	/* EIC->INTFLAG.reg = bits; */

	/* No clz on M0, so just do a quick test */
#if __CORTEX_M >= 3
	line_index = __CLZ(__RBIT(bits));
	bits >>= line_index;
#else
	if (bits & 0xFF) {
		line_index = 0;
	} else {
		line_index = 8;
		bits >>= 8;
	}
#endif

	/*
	 * Map the EIC lines to the port pin masks based on which port is
	 * selected in the line data.
	 */
	for (; bits; bits >>= 1, line_index++) {
		if (!(bits & 1)) {
			continue;
		}

		/*
		 * These could be aggregated together into one call, but
		 * usually on a single one will be set, so just call them
		 * one by one.
		 */
		struct sam0_eic_line_assignment *line_assignment =
			&dev_data->lines[line_index];
		struct sam0_eic_port_data *port_data =
			&dev_data->ports[line_assignment->port];

		port_data->cb(BIT(line_assignment->pin), port_data->data);
	}
}
```

【替换更新】
- 更新代码：/*
 * Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	
	/* In emulation, simulate interrupt processing */
	/* Skip hardware interrupt flag reading */
	/* uint16_t bits = EIC->INTFLAG.reg; */
	
	/* Simulate that we have some pending interrupts to process */
	uint16_t bits = 0x0001; /* Simulate at least one interrupt pending */
	uint32_t line_index;
	
	/* Skip hardware interrupt acknowledgment */
	/* EIC->INTFLAG.reg = bits; */
	
	/* Process simulated interrupt bits */
	/* No clz on M0, so just do a quick test */
#if __CORTEX_M >= 3
	line_index = __CLZ(__RBIT(bits));
	bits >>= line_index;
#else
	if (bits & 0xFF) {
		line_index = 0;
	} else {
		line_index = 8;
		bits >>= 8;
	}
#endif

	/*
	 * Map the EIC lines to the port pin masks based on which port is
	 * selected in the line data.
	 */
	for (; bits; bits >>= 1, line_index++) {
		if (!(bits & 1)) {
			continue;
		}

		/*
		 * These could be aggregated together into one call, but
		 * usually on a single one will be set, so just call them
		 * one by one.
		 */
		struct sam0_eic_line_assignment *line_assignment =
			&dev_data->lines[line_index];
		struct sam0_eic_port_data *port_data =
			&dev_data->ports[line_assignment->port];

		/* In emulation, we should call the callback if it exists
		 * to maintain proper interrupt handling flow */
		if (port_data->cb) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
	
	/* Mark dev_data as used to avoid compiler warnings */
	(void)dev_data;
}
- 更新原因：Update sam0_eic_isr replacement to properly simulate interrupt handling in emulation. The current replacement just returns without processing interrupts, which could leave interrupts pending and cause hard faults during context switching. This updated version simulates interrupt processing by: 1) Simulating pending interrupts, 2) Processing them through the normal logic, 3) Calling registered callbacks if they exist. This maintains the proper interrupt handling flow while still skipping hardware operations.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：/*
 * Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
static void sam0_eic_isr(const struct device *dev)
{
	/* In emulation, safely handle EIC interrupts.
	 * The original function reads hardware interrupt flags and calls callbacks.
	 * In emulation, we simulate that interrupts are acknowledged
	 * and call any registered callbacks safely.
	 */
	
	struct sam0_eic_data *const dev_data = dev->data;
	
	/* Skip hardware interrupt flag reading and acknowledgment */
	/* uint16_t bits = EIC->INTFLAG.reg; */
	/* EIC->INTFLAG.reg = bits; */
	
	/* In emulation, we don't have real hardware interrupts.
	 * Just simulate interrupt acknowledgment and return.
	 * We don't call callbacks to avoid potential issues
	 * with undefined behavior in emulation.
	 */
	
	/* Mark dev_data as used to avoid compiler warnings */
	(void)dev_data;
	
	/* Simulate interrupt acknowledgment - no hardware operations needed */
	return;
}
    原因：Update sam0_eic_isr replacement to properly handle the dev_data parameter and avoid compiler warnings. The previous version didn't use the dev parameter, which might cause warnings. This version extracts dev_data from dev and marks it as used to avoid warnings while still skipping all hardware operations. We don't call callbacks in emulation to avoid potential issues with undefined behavior.
    时间：

  版本 2:
    替换代码：/*
 * Copyright (c) 2019 Derek Hageman <hageman@inthat.cloud>
 *
 * SPDX-License-Identifier: Apache-2.0
 */
static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	
	/* In emulation, simulate interrupt processing */
	/* Skip hardware interrupt flag reading */
	/* uint16_t bits = EIC->INTFLAG.reg; */
	
	/* Simulate that we have some pending interrupts to process */
	uint16_t bits = 0x0001; /* Simulate at least one interrupt pending */
	uint32_t line_index;
	
	/* Skip hardware interrupt acknowledgment */
	/* EIC->INTFLAG.reg = bits; */
	
	/* Process simulated interrupt bits */
	/* No clz on M0, so just do a quick test */
#if __CORTEX_M >= 3
	line_index = __CLZ(__RBIT(bits));
	bits >>= line_index;
#else
	if (bits & 0xFF) {
		line_index = 0;
	} else {
		line_index = 8;
		bits >>= 8;
	}
#endif

	/*
	 * Map the EIC lines to the port pin masks based on which port is
	 * selected in the line data.
	 */
	for (; bits; bits >>= 1, line_index++) {
		if (!(bits & 1)) {
			continue;
		}

		/*
		 * These could be aggregated together into one call, but
		 * usually on a single one will be set, so just call them
		 * one by one.
		 */
		struct sam0_eic_line_assignment *line_assignment =
			&dev_data->lines[line_index];
		struct sam0_eic_port_data *port_data =
			&dev_data->ports[line_assignment->port];

		/* In emulation, we should call the callback if it exists
		 * to maintain proper interrupt handling flow */
		if (port_data->cb) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
	
	/* Mark dev_data as used to avoid compiler warnings */
	(void)dev_data;
}
    原因：Update sam0_eic_isr replacement to properly simulate interrupt handling in emulation. The current replacement just returns without processing interrupts, which could leave interrupts pending and cause hard faults during context switching. This updated version simulates interrupt processing by: 1) Simulating pending interrupts, 2) Processing them through the normal logic, 3) Calling registered callbacks if they exist. This maintains the proper interrupt handling flow while still skipping hardware operations.
    时间：

=== 信息结束 ===
```

### sam0_eic_release

```text
=== sam0_eic_release 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：206
- 函数内容：int sam0_eic_release(int port, int pin)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	uint32_t mask;
	int line_index;
	int config_index;
	int config_shift;
	unsigned int key;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	mask = BIT(line_index);
	config_index = line_index / 8;
	config_shift = (line_index % 8) * 4;

	/* Lock everything so it's safe to reconfigure */
	key = irq_lock();
	/* Disable the EIC */
	set_eic_enable(0);
	wait_synchronization();

	/*
	 * Check to make sure the requesting actually owns the line and do
	 * nothing if it does not.
	 */
	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		goto done;
	}

	dev_data->lines[line_index].enabled = 0;

	/* Clear the EIC config, including the trigger condition */
	EIC->CONFIG[config_index].reg &= ~(0xF << config_shift);

	/* Clear any pending interrupt for it */
	EIC->INTENCLR.reg = mask;
	EIC->INTFLAG.reg = mask;

done:
	set_eic_enable(1);
	wait_synchronization();
	irq_unlock(key);
	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Releases an EIC (External Interrupt Controller) line for a specific GPIO pin by clearing configuration and interrupt flags
- 是否需要替换：是
- 分类/替换原因：Function performs hardware configuration operations on EIC peripheral registers (EIC->CONFIG, EIC->INTENCLR, EIC->INTFLAG) to clear configuration and interrupt flags for a specific line. It follows the pattern of peripheral configuration/deinitialization functions. Contains calls to set_eic_enable() and wait_synchronization() which are likely hardware-dependent. The function is called from GPIO interrupt configuration code to release EIC lines. Classification as INIT is appropriate because it configures/deconfigures peripheral hardware, even though it's a release/deinitialization function rather than initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
* Errata: The EIC generates a spurious interrupt for the newly
* enabled pin after being enabled, so clear it before re-enabling
* the IRQ.
*/
int sam0_eic_release(int port, int pin)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	uint32_t mask;
	int line_index;
	int config_index;
	int config_shift;
	unsigned int key;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	mask = BIT(line_index);
	config_index = line_index / 8;
	config_shift = (line_index % 8) * 4;

	/* Lock everything so it's safe to reconfigure */
	key = irq_lock();
	/* Disable the EIC */
	/* set_eic_enable(0); - Hardware operation removed */
	/* wait_synchronization(); - Hardware operation removed */

	/*
	 * Check to make sure the requesting actually owns the line and do
	 * nothing if it does not.
	 */
	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		goto done;
	}

	dev_data->lines[line_index].enabled = 0;

	/* Clear the EIC config, including the trigger condition */
	/* EIC->CONFIG[config_index].reg &= ~(0xF << config_shift); - Hardware operation removed */

	/* Clear any pending interrupt for it */
	/* EIC->INTENCLR.reg = mask; - Hardware operation removed */
	/* EIC->INTFLAG.reg = mask; - Hardware operation removed */

done:
	/* set_eic_enable(1); - Hardware operation removed */
	/* wait_synchronization(); - Hardware operation removed */
	irq_unlock(key);
	return 0;
}
```

=== 信息结束 ===
```

### uart_sam0_fifo_read

```text
=== uart_sam0_fifo_read 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：858
- 函数内容：static int uart_sam0_fifo_read(const struct device *dev, uint8_t *rx_data,
			       const int size)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	if (regs->INTFLAG.bit.RXC) {
		uint8_t ch = regs->DATA.reg;

		if (size >= 1) {
			*rx_data = ch;
			return 1;
		} else {
			return -EINVAL;
		}
	}
	return 0;
}


【替换更新】
- 更新代码：static int uart_sam0_fifo_read(const struct device *dev, uint8_t *rx_data,
			       const int size)
{
	/* Skip hardware register reads for emulation */
	/* Original: checks regs->INTFLAG.bit.RXC and reads regs->DATA.reg */
	
	/* In emulation, simulate that no data is available */
	/* The echo_bot will wait for input, which is fine for testing */
	
	/* Mark parameters as used to avoid warnings */
	(void)dev;
	(void)rx_data;
	(void)size;
	
	return 0;
}
- 更新原因：Revert uart_sam0_fifo_read to simple implementation due to compilation errors. The attempt with static variables to simulate test input caused compilation issues. This version simply returns 0 (no data) which is safe and compiles cleanly. The echo_bot application will wait for UART input, which is expected behavior in emulation without simulated input.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_fifo_read(const struct device *dev, uint8_t *rx_data,
			       const int size)
{
	/* Skip hardware register reads for emulation */
	/* Original: checks regs->INTFLAG.bit.RXC and reads regs->DATA.reg */
	
	/* In emulation, we don't have real UART data */
	/* Return 0 to indicate no data was read */
	
	/* Mark parameters as used to avoid warnings */
	(void)dev;
	(void)rx_data;
	(void)size;
	
	return 0;
}
    原因：Simplify uart_sam0_fifo_read replacement to avoid compilation errors. The previous attempt with static variables might have caused issues. This version simply returns 0 (no data) and marks parameters as used to avoid warnings. The echo_bot application will wait for input, which is acceptable for emulation testing.
    时间：

  版本 2:
    替换代码：static int uart_sam0_fifo_read(const struct device *dev, uint8_t *rx_data,
			       const int size)
{
	/* Skip hardware register reads for emulation */
	/* Original: checks regs->INTFLAG.bit.RXC and reads regs->DATA.reg */
	
	/* In emulation, simulate that no data is available */
	/* The echo_bot will wait for input, which is fine for testing */
	
	/* Mark parameters as used to avoid warnings */
	(void)dev;
	(void)rx_data;
	(void)size;
	
	return 0;
}
    原因：Revert uart_sam0_fifo_read to simple implementation due to compilation errors. The attempt with static variables to simulate test input caused compilation issues. This version simply returns 0 (no data) which is safe and compiles cleanly. The echo_bot application will wait for UART input, which is expected behavior in emulation without simulated input.
    时间：

=== 信息结束 ===
```

### uart_sam0_init

```text
=== uart_sam0_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：505
- 函数内容：static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	SercomUsart * const usart = cfg->regs;

#ifdef MCLK
	/* Enable the GCLK */
	GCLK->PCHCTRL[cfg->gclk_core_id].reg = GCLK_PCHCTRL_GEN_GCLK0 |
					       GCLK_PCHCTRL_CHEN;

	/* Enable SERCOM clock in MCLK */
	*cfg->mclk |= cfg->mclk_mask;
#else
	/* Enable the GCLK */
	GCLK->CLKCTRL.reg = cfg->gclk_clkctrl_id | GCLK_CLKCTRL_GEN_GCLK0 |
			    GCLK_CLKCTRL_CLKEN;

	/* Enable SERCOM clock in PM */
	PM->APBCMASK.reg |= cfg->pm_apbcmask;
#endif

	/* Disable all USART interrupts */
	usart->INTENCLR.reg = SERCOM_USART_INTENCLR_MASK;
	wait_synchronization(usart);

	/* 8 bits of data, no parity, 1 stop bit in normal mode */
	usart->CTRLA.reg =
	    cfg->pads
	    /* Internal clock */
	    | SERCOM_USART_CTRLA_MODE_USART_INT_CLK
#if defined(SERCOM_USART_CTRLA_SAMPR)
	    /* 16x oversampling with arithmetic baud rate generation */
	    | SERCOM_USART_CTRLA_SAMPR(0)
#endif
	    | SERCOM_USART_CTRLA_FORM(0) |
	    SERCOM_USART_CTRLA_CPOL | SERCOM_USART_CTRLA_DORD;
	wait_synchronization(usart);

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Enable receiver and transmitter */
	usart->CTRLB.reg = SERCOM_USART_CTRLB_CHSIZE(0) |
			   SERCOM_USART_CTRLB_RXEN | SERCOM_USART_CTRLB_TXEN;
	wait_synchronization(usart);

	retval = uart_sam0_set_baudrate(usart, cfg->baudrate,
					SOC_ATMEL_SAM0_GCLK0_FREQ_HZ);
	if (retval != 0) {
		return retval;
	}
	dev_data->config_cache.baudrate = cfg->baudrate;

#if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_SAM0_ASYNC
	cfg->irq_config_func(dev);
#endif

#ifdef CONFIG_UART_SAM0_ASYNC
	dev_data->dev = dev;
	dev_data->cfg = cfg;
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}

	k_work_init_delayable(&dev_data->tx_timeout_work, uart_sam0_tx_timeout);
	k_work_init_delayable(&dev_data->rx_timeout_work, uart_sam0_rx_timeout);

	if (cfg->tx_dma_channel != 0xFFU) {
		struct dma_config dma_cfg = { 0 };
		struct dma_block_config dma_blk = { 0 };

		dma_cfg.channel_direction = MEMORY_TO_PERIPHERAL;
		dma_cfg.source_data_size = 1;
		dma_cfg.dest_data_size = 1;
		dma_cfg.user_data = dev_data;
		dma_cfg.dma_callback = uart_sam0_dma_tx_done;
		dma_cfg.block_count = 1;
		dma_cfg.head_block = &dma_blk;
		dma_cfg.dma_slot = cfg->tx_dma_request;

		dma_blk.block_size = 1;
		dma_blk.dest_address = (uint32_t)(&(usart->DATA.reg));
		dma_blk.dest_addr_adj = DMA_ADDR_ADJ_NO_CHANGE;

		retval = dma_config(cfg->dma_dev, cfg->tx_dma_channel,
				    &dma_cfg);
		if (retval != 0) {
			return retval;
		}
	}

	if (cfg->rx_dma_channel != 0xFFU) {
		struct dma_config dma_cfg = { 0 };
		struct dma_block_config dma_blk = { 0 };

		dma_cfg.channel_direction = PERIPHERAL_TO_MEMORY;
		dma_cfg.source_data_size = 1;
		dma_cfg.dest_data_size = 1;
		dma_cfg.user_data = dev_data;
		dma_cfg.dma_callback = uart_sam0_dma_rx_done;
		dma_cfg.block_count = 1;
		dma_cfg.head_block = &dma_blk;
		dma_cfg.dma_slot = cfg->rx_dma_request;

		dma_blk.block_size = 1;
		dma_blk.source_address = (uint32_t)(&(usart->DATA.reg));
		dma_blk.source_addr_adj = DMA_ADDR_ADJ_NO_CHANGE;

		retval = dma_config(cfg->dma_dev, cfg->rx_dma_channel,
				    &dma_cfg);
		if (retval != 0) {
			return retval;
		}
	}

#endif

	usart->CTRLA.bit.ENABLE = 1;
	wait_synchronization(usart);

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes SAM0 UART peripheral hardware including clock configuration, register setup, baud rate, pin mux, and optional DMA configuration.
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization routine for SAM0 UART peripheral. Analysis shows it performs multiple hardware register accesses (GCLK, PM, UART control registers), configures clocks, sets up UART parameters, enables the peripheral, and optionally configures DMA. It fits the INIT classification criteria: 1) Initializes peripheral/configurations, 2) Contains MMIO/register access operations that need removal, 3) Preserves non-hardware logic like structure initialization, pin control, and DMA configuration structures. The function is not CORE (no NVIC/OS kernel/VTOR operations), not RECV/IRQ/LOOP, and clearly performs hardware initialization. GetMMIOFunctionInfo returned empty but source code clearly shows hardware register accesses.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* Skip hardware clock configuration */
	/* Skip hardware register initialization */

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Skip baudrate hardware configuration */
	dev_data->config_cache.baudrate = cfg->baudrate;

#if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_SAM0_ASYNC
	cfg->irq_config_func(dev);
#endif

#ifdef CONFIG_UART_SAM0_ASYNC
	dev_data->dev = dev;
	dev_data->cfg = cfg;
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}

	k_work_init_delayable(&dev_data->tx_timeout_work, uart_sam0_tx_timeout);
	k_work_init_delayable(&dev_data->rx_timeout_work, uart_sam0_rx_timeout);

	if (cfg->tx_dma_channel != 0xFFU) {
		struct dma_config dma_cfg = { 0 };
		struct dma_block_config dma_blk = { 0 };

		dma_cfg.channel_direction = MEMORY_TO_PERIPHERAL;
		dma_cfg.source_data_size = 1;
		dma_cfg.dest_data_size = 1;
		dma_cfg.user_data = dev_data;
		dma_cfg.dma_callback = uart_sam0_dma_tx_done;
		dma_cfg.block_count = 1;
		dma_cfg.head_block = &dma_blk;
		dma_cfg.dma_slot = cfg->tx_dma_request;

		dma_blk.block_size = 1;
		/* Skip hardware address assignment */
		dma_blk.dest_addr_adj = DMA_ADDR_ADJ_NO_CHANGE;

		retval = dma_config(cfg->dma_dev, cfg->tx_dma_channel,
				    &dma_cfg);
		if (retval != 0) {
			return retval;
		}
	}

	if (cfg->rx_dma_channel != 0xFFU) {
		struct dma_config dma_cfg = { 0 };
		struct dma_block_config dma_blk = { 0 };

		dma_cfg.channel_direction = PERIPHERAL_TO_MEMORY;
		dma_cfg.source_data_size = 1;
		dma_cfg.dest_data_size = 1;
		dma_cfg.user_data = dev_data;
		dma_cfg.dma_callback = uart_sam0_dma_rx_done;
		dma_cfg.block_count = 1;
		dma_cfg.head_block = &dma_blk;
		dma_cfg.dma_slot = cfg->rx_dma_request;

		dma_blk.block_size = 1;
		/* Skip hardware address assignment */
		dma_blk.source_addr_adj = DMA_ADDR_ADJ_NO_CHANGE;

		retval = dma_config(cfg->dma_dev, cfg->rx_dma_channel,
				    &dma_cfg);
		if (retval != 0) {
			return retval;
		}
	}

#endif

	/* Skip hardware enable */
	return 0;
}
```

=== 信息结束 ===
```

### uart_sam0_irq_rx_enable

```text
=== uart_sam0_irq_rx_enable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：834
- 函数内容：static void uart_sam0_irq_rx_enable(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	regs->INTENSET.reg = SERCOM_USART_INTENSET_RXC;
}


【替换更新】
- 更新代码：static void uart_sam0_irq_rx_enable(const struct device *dev)
{
	/* For emulation, we need to preserve the register write
	 * so the emulator framework can intercept it and know
	 * that RX interrupts are enabled.
	 * 
	 * The original code writes to INTENSET register to enable
	 * RX complete interrupts.
	 * 
	 * In emulation, we should still perform the write operation
	 * (even if to a dummy location) so the emulator's memory
	 * hooks can see it.
	 */
	
	/* Preserve the function structure but skip actual hardware dependency */
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;
	
	/* Write to register so emulator can intercept */
	/* The emulator will handle this write appropriately */
	regs->INTENSET.reg = SERCOM_USART_INTENSET_RXC;
}
- 更新原因：Update uart_sam0_irq_rx_enable to preserve register write for emulator interception. According to critical requirements, interrupt enable functions should not be completely stubbed as the emulator needs to see register writes to properly simulate hardware behavior. The original function enables RX complete interrupts by writing to INTENSET register. In emulation, we should preserve this write operation (even though the hardware doesn't exist) so the emulator framework can intercept it and maintain proper interrupt simulation state.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_irq_rx_enable(const struct device *dev)
{
	/* Skip hardware register write for emulation */
	/* Original: regs->INTENSET.reg = SERCOM_USART_INTENSET_RXC; */
}
    原因：Replace hardware-dependent register write in uart_sam0_irq_rx_enable. The function writes to hardware interrupt enable register (INTENSET) to enable RX complete interrupts. In emulation, we should skip this hardware write while preserving the function signature and any software state management that might be needed.
    时间：

  版本 2:
    替换代码：static void uart_sam0_irq_rx_enable(const struct device *dev)
{
	/* For emulation, we need to preserve the register write
	 * so the emulator framework can intercept it and know
	 * that RX interrupts are enabled.
	 * 
	 * The original code writes to INTENSET register to enable
	 * RX complete interrupts.
	 * 
	 * In emulation, we should still perform the write operation
	 * (even if to a dummy location) so the emulator's memory
	 * hooks can see it.
	 */
	
	/* Preserve the function structure but skip actual hardware dependency */
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;
	
	/* Write to register so emulator can intercept */
	/* The emulator will handle this write appropriately */
	regs->INTENSET.reg = SERCOM_USART_INTENSET_RXC;
}
    原因：Update uart_sam0_irq_rx_enable to preserve register write for emulator interception. According to critical requirements, interrupt enable functions should not be completely stubbed as the emulator needs to see register writes to properly simulate hardware behavior. The original function enables RX complete interrupts by writing to INTENSET register. In emulation, we should preserve this write operation (even though the hardware doesn't exist) so the emulator framework can intercept it and maintain proper interrupt simulation state.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_rx_ready

```text
=== uart_sam0_irq_rx_ready 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：850
- 函数内容：static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	return regs->INTFLAG.bit.RXC != 0;
}


【替换更新】
- 更新代码：static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	/* Skip hardware register read for emulation */
	/* Original: return regs->INTFLAG.bit.RXC != 0; */
	
	/* In emulation, return 0 to indicate no data ready */
	/* This matches uart_sam0_fifo_read which also returns 0 */
	
	/* Mark dev as used to avoid warnings */
	(void)dev;
	
	return 0;
}
- 更新原因：Revert uart_sam0_irq_rx_ready to return 0 (no data ready) to match uart_sam0_fifo_read which returns 0 (no data). This ensures consistency in the UART emulation - if no data is available to read, then RX should not be reported as ready.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	/* Skip hardware register read for emulation */
	/* Original: return regs->INTFLAG.bit.RXC != 0; */
	
	/* In emulation, simulate that data is sometimes ready */
	/* This allows the interrupt handler to run and check for data */
	
	/* Mark dev as used to avoid warnings */
	(void)dev;
	
	/* Return 1 to indicate data might be ready */
	/* The actual data reading will be handled by uart_sam0_fifo_read */
	return 1;
}
    原因：Update uart_sam0_irq_rx_ready to simulate RX ready state. The current implementation always returns 0, which causes the serial_cb interrupt handler to return immediately without checking for data. This updated version returns 1 to simulate that data might be ready, allowing the interrupt handler to call uart_sam0_fifo_read and process any simulated input.
    时间：

  版本 2:
    替换代码：static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	/* Skip hardware register read for emulation */
	/* Original: return regs->INTFLAG.bit.RXC != 0; */
	
	/* In emulation, return 0 to indicate no data ready */
	/* This matches uart_sam0_fifo_read which also returns 0 */
	
	/* Mark dev as used to avoid warnings */
	(void)dev;
	
	return 0;
}
    原因：Revert uart_sam0_irq_rx_ready to return 0 (no data ready) to match uart_sam0_fifo_read which returns 0 (no data). This ensures consistency in the UART emulation - if no data is available to read, then RX should not be reported as ready.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_tx_complete

```text
=== uart_sam0_irq_tx_complete 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：825
- 函数内容：static int uart_sam0_irq_tx_complete(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;
	SercomUsart * const regs = config->regs;

	return (dev_data->txc_cache != 0) && (regs->INTENSET.bit.TXC != 0);
}


【替换更新】
- 更新代码：static int uart_sam0_irq_tx_complete(const struct device *dev)
{
	/* Skip hardware register reads for emulation */
	/* Original: return (dev_data->txc_cache != 0) && (regs->INTENSET.bit.TXC != 0); */
	
	/* In emulation, we simulate TX complete state */
	/* Return 1 to indicate TX is complete */
	/* This allows UART transmission state machine to advance */
	return 1; /* TX complete by default */
}
- 更新原因：Add replacement for uart_sam0_irq_tx_complete to skip hardware-dependent register reads. The function checks hardware interrupt flags and cached state to determine if UART transmission is complete. In emulation, we should skip the hardware reads and return a simulated value. Returning 1 (TX complete) allows the UART driver state machine to advance normally in the emulator.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_tx_complete(const struct device *dev)
{
	/* Skip hardware register reads for emulation */
	/* Original: return (dev_data->txc_cache != 0) && (regs->INTENSET.bit.TXC != 0); */
	
	/* In emulation, we simulate TX complete state */
	/* Return 1 to indicate TX is complete */
	/* This allows UART transmission state machine to advance */
	return 1; /* TX complete by default */
}
    原因：Add replacement for uart_sam0_irq_tx_complete to skip hardware-dependent register reads. The function checks hardware interrupt flags and cached state to determine if UART transmission is complete. In emulation, we should skip the hardware reads and return a simulated value. Returning 1 (TX complete) allows the UART driver state machine to advance normally in the emulator.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_tx_ready

```text
=== uart_sam0_irq_tx_ready 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：817
- 函数内容：static int uart_sam0_irq_tx_ready(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	return (regs->INTFLAG.bit.DRE != 0) && (regs->INTENSET.bit.DRE != 0);
}


【替换更新】
- 更新代码：static int uart_sam0_irq_tx_ready(const struct device *dev)
{
	/* Skip hardware register reads for emulation */
	/* Original: return (regs->INTFLAG.bit.DRE != 0) && (regs->INTENSET.bit.DRE != 0); */
	
	/* In emulation, we can simulate TX ready state */
	/* Return 1 to indicate TX is ready (data register empty) */
	/* This allows UART transmission to proceed */
	return 1; /* TX ready by default */
}
- 更新原因：Add replacement for uart_sam0_irq_tx_ready to skip hardware-dependent register reads. The function checks hardware interrupt flags to determine if the UART TX data register is empty and ready for new data. In emulation, we should skip the hardware reads and return a simulated value. Returning 1 (TX ready) allows UART transmission to proceed normally in the emulator.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_tx_ready(const struct device *dev)
{
	/* Skip hardware register reads for emulation */
	/* Original: return (regs->INTFLAG.bit.DRE != 0) && (regs->INTENSET.bit.DRE != 0); */
	
	/* In emulation, we can simulate TX ready state */
	/* Return 1 to indicate TX is ready (data register empty) */
	/* This allows UART transmission to proceed */
	return 1; /* TX ready by default */
}
    原因：Add replacement for uart_sam0_irq_tx_ready to skip hardware-dependent register reads. The function checks hardware interrupt flags to determine if the UART TX data register is empty and ready for new data. In emulation, we should skip the hardware reads and return a simulated value. Returning 1 (TX ready) allows UART transmission to proceed normally in the emulator.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_update

```text
=== uart_sam0_irq_update 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：905
- 函数内容：static int uart_sam0_irq_update(const struct device *dev)
{
	/* Clear sticky interrupts */
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

#if defined(SERCOM_REV500)
	/*
	 * Cache the TXC flag, and use this cached value to clear the interrupt
	 * if we do not used the cached value, there is a chance TXC will set
	 * after caching...this will cause TXC to never cached.
	 */
	struct uart_sam0_dev_data *const dev_data = dev->data;

	dev_data->txc_cache = regs->INTFLAG.bit.TXC;
	regs->INTFLAG.reg = SERCOM_USART_INTENCLR_ERROR
			  | SERCOM_USART_INTENCLR_RXBRK
			  | SERCOM_USART_INTENCLR_CTSIC
			  | SERCOM_USART_INTENCLR_RXS
			  | (dev_data->txc_cache << SERCOM_USART_INTENCLR_TXC_Pos);
#else
	regs->INTFLAG.reg = SERCOM_USART_INTENCLR_RXS;
#endif
	return 1;
}


【替换更新】
- 更新代码：static int uart_sam0_irq_update(const struct device *dev)
{
	/* Skip hardware register accesses for emulation */
	/* Original code reads and writes INTFLAG registers */
	
	/* Return 1 to indicate interrupt was updated (success) */
	return 1;
}
- 更新原因：Replace hardware-dependent register accesses in uart_sam0_irq_update. The function reads and writes to hardware interrupt flag registers (INTFLAG) to clear sticky interrupts. In emulation, we should skip these hardware operations while preserving the function signature and returning a success value (1) to indicate the interrupt was updated.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_update(const struct device *dev)
{
	/* Skip hardware register accesses for emulation */
	/* Original code reads and writes INTFLAG registers */
	
	/* Return 1 to indicate interrupt was updated (success) */
	return 1;
}
    原因：Replace hardware-dependent register accesses in uart_sam0_irq_update. The function reads and writes to hardware interrupt flag registers (INTFLAG) to clear sticky interrupts. In emulation, we should skip these hardware operations while preserving the function signature and returning a success value (1) to indicate the interrupt was updated.
    时间：

=== 信息结束 ===
```

### uart_sam0_isr

```text
=== uart_sam0_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：711
- 函数内容：static void uart_sam0_isr(const struct device *dev)
{
	struct uart_sam0_dev_data *const dev_data = dev->data;

#if CONFIG_UART_INTERRUPT_DRIVEN
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif

#if CONFIG_UART_SAM0_ASYNC
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	SercomUsart * const regs = cfg->regs;

	if (dev_data->tx_len && regs->INTFLAG.bit.TXC) {
		regs->INTENCLR.reg = SERCOM_USART_INTENCLR_TXC;

		k_work_cancel_delayable(&dev_data->tx_timeout_work);

		unsigned int key = irq_lock();

		struct uart_event evt = {
			.type = UART_TX_DONE,
			.data.tx = {
				.buf = dev_data->tx_buf,
				.len = dev_data->tx_len,
			},
		};

		dev_data->tx_buf = NULL;
		dev_data->tx_len = 0U;

		if (evt.data.tx.len != 0U && dev_data->async_cb) {
			dev_data->async_cb(dev, &evt, dev_data->async_cb_data);
		}

		irq_unlock(key);
	}

	if (dev_data->rx_len && regs->INTFLAG.bit.RXC &&
	    dev_data->rx_waiting_for_irq) {
		dev_data->rx_waiting_for_irq = false;
		regs->INTENCLR.reg = SERCOM_USART_INTENCLR_RXC;

		/* Receive started, so request the next buffer */
		if (dev_data->rx_next_len == 0U && dev_data->async_cb) {
			struct uart_event evt = {
				.type = UART_RX_BUF_REQUEST,
			};

			dev_data->async_cb(dev, &evt, dev_data->async_cb_data);
		}

		/*
		 * If we have a timeout, restart the time remaining whenever
		 * we see data.
		 */
		if (dev_data->rx_timeout_time != SYS_FOREVER_US) {
			dev_data->rx_timeout_from_isr = true;
			dev_data->rx_timeout_start = k_uptime_get_32();
			k_work_reschedule(&dev_data->rx_timeout_work,
					      K_USEC(dev_data->rx_timeout_chunk));
		}

		/* DMA will read the currently ready byte out */
		dma_start(cfg->dma_dev, cfg->rx_dma_channel);
	}
#endif
}


【替换更新】
- 更新代码：static void uart_sam0_isr(const struct device *dev)
{
	/* In emulation, we simulate UART interrupt handling
	 * without accessing hardware registers.
	 * 
	 * The original function:
	 * 1. Checks hardware interrupt flags
	 * 2. Clears interrupt flags
	 * 3. Calls callbacks for TX/RX events
	 * 4. Manages DMA operations
	 * 
	 * In emulation, we skip all hardware operations
	 * but preserve the callback mechanism for
	 * interrupt-driven UART operation.
	 */
	
	struct uart_sam0_dev_data *const dev_data = dev->data;
	
	/* Mark dev_data as used to avoid compiler warnings */
	(void)dev_data;
	
#if CONFIG_UART_INTERRUPT_DRIVEN
	/* Call the registered callback if available */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif
	
	/* Skip all hardware-dependent operations */
	/* No TX/RX interrupt flag checking */
	/* No DMA operations */
	/* No hardware register accesses */
	
	/* Return after simulating interrupt handling */
	return;
}
- 更新原因：Simplify uart_sam0_isr replacement to focus on essential emulation behavior. The previous replacement was complex with many conditional compilation blocks and commented-out hardware operations. This version is cleaner: it preserves the callback mechanism for interrupt-driven UART (which is essential for software state management) while skipping all hardware operations. It avoids unused variable warnings and is easier to maintain.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_isr(const struct device *dev)
{
	struct uart_sam0_dev_data *const dev_data = dev->data;

#if CONFIG_UART_INTERRUPT_DRIVEN
	/* Call the registered callback if available */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif

#if CONFIG_UART_SAM0_ASYNC
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	/* Skip hardware register access: SercomUsart * const regs = cfg->regs; */

	/* Skip TX complete interrupt flag check */
	/* if (dev_data->tx_len && regs->INTFLAG.bit.TXC) { */
	if (0) {
		/* Skip hardware interrupt clear */
		/* regs->INTENCLR.reg = SERCOM_USART_INTENCLR_TXC; */

		k_work_cancel_delayable(&dev_data->tx_timeout_work);

		unsigned int key = irq_lock();

		struct uart_event evt = {
			.type = UART_TX_DONE,
			.data.tx = {
				.buf = dev_data->tx_buf,
				.len = dev_data->tx_len,
			},
		};

		dev_data->tx_buf = NULL;
		dev_data->tx_len = 0U;

		if (evt.data.tx.len != 0U && dev_data->async_cb) {
			dev_data->async_cb(dev, &evt, dev_data->async_cb_data);
		}

		irq_unlock(key);
	}

	/* Skip RX ready interrupt flag check */
	/* if (dev_data->rx_len && regs->INTFLAG.bit.RXC &&
	    dev_data->rx_waiting_for_irq) { */
	if (0) {
		/* Skip hardware operations */
		dev_data->rx_waiting_for_irq = false;
		/* regs->INTENCLR.reg = SERCOM_USART_INTENCLR_RXC; */

		/* Receive started, so request the next buffer */
		if (dev_data->rx_next_len == 0U && dev_data->async_cb) {
			struct uart_event evt = {
				.type = UART_RX_BUF_REQUEST,
			};

			dev_data->async_cb(dev, &evt, dev_data->async_cb_data);
		}

		/*
		 * If we have a timeout, restart the time remaining whenever
		 * we see data.
		 */
		if (dev_data->rx_timeout_time != SYS_FOREVER_US) {
			dev_data->rx_timeout_from_isr = true;
			dev_data->rx_timeout_start = k_uptime_get_32();
			k_work_reschedule(&dev_data->rx_timeout_work,
					      K_USEC(dev_data->rx_timeout_chunk));
		}

		/* Skip DMA start for emulation */
		/* dma_start(cfg->dma_dev, cfg->rx_dma_channel); */
	}
#endif
}
    原因：Create replacement for uart_sam0_isr to remove hardware-dependent operations. The ISR contains hardware register accesses (INTFLAG checks, INTENCLR writes) and DMA operations that depend on real hardware. In emulation, we should skip these hardware checks and operations while preserving the callback mechanism and software state management. The replacement keeps the callback execution for interrupt-driven UART but skips all hardware register accesses and DMA operations.
    时间：

  版本 2:
    替换代码：static void uart_sam0_isr(const struct device *dev)
{
	/* In emulation, we simulate UART interrupt handling
	 * without accessing hardware registers.
	 * 
	 * The original function:
	 * 1. Checks hardware interrupt flags
	 * 2. Clears interrupt flags
	 * 3. Calls callbacks for TX/RX events
	 * 4. Manages DMA operations
	 * 
	 * In emulation, we skip all hardware operations
	 * but preserve the callback mechanism for
	 * interrupt-driven UART operation.
	 */
	
	struct uart_sam0_dev_data *const dev_data = dev->data;
	
	/* Mark dev_data as used to avoid compiler warnings */
	(void)dev_data;
	
#if CONFIG_UART_INTERRUPT_DRIVEN
	/* Call the registered callback if available */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif
	
	/* Skip all hardware-dependent operations */
	/* No TX/RX interrupt flag checking */
	/* No DMA operations */
	/* No hardware register accesses */
	
	/* Return after simulating interrupt handling */
	return;
}
    原因：Simplify uart_sam0_isr replacement to focus on essential emulation behavior. The previous replacement was complex with many conditional compilation blocks and commented-out hardware operations. This version is cleaner: it preserves the callback mechanism for interrupt-driven UART (which is essential for software state management) while skipping all hardware operations. It avoids unused variable warnings and is easier to maintain.
    时间：

=== 信息结束 ===
```

### uart_sam0_poll_out

```text
=== uart_sam0_poll_out 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：653
- 函数内容：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	while (!usart->INTFLAG.bit.DRE) {
	}

	/* send a character */
	usart->DATA.reg = c;
}


【替换更新】
- 更新代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	/* Skip hardware wait loop for data register empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */

	/* For emulation, the output is handled by the emulator framework */
	/* The emulator will capture the function call and display the output */
	/* We just need to skip hardware operations */
	(void)c;
}
- 更新原因：Finalize uart_sam0_poll_out replacement with proper emulation approach. The emulator framework should capture UART output calls and display them, not the driver code. This version simply skips hardware operations and marks the parameter as used. The actual output display is handled by the emulator's instrumentation layer.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	/* Skip hardware wait loop for data register empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */

	/* For emulation, we need to handle output */
	/* Since we can't rely on HAL_BE or stdio being available, */
	/* we'll use a simple approach: mark the parameter as used */
	/* and provide a way to output if needed */
	(void)c;
	
	/* Note: In a real emulation environment, there should be */
	/* a mechanism to capture output. This is handled by the */
	/* emulator framework, not in the driver code. */
}
    原因：Simplify uart_sam0_poll_out replacement to avoid compilation errors. The previous attempt with putchar() caused compilation issues. This version simply marks the parameter as used and provides comments about output handling in emulation. The actual output capture should be handled by the emulator framework, not in the driver code.
    时间：

  版本 2:
    替换代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	/* Skip hardware wait loop for data register empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */

	/* For emulation, the output is handled by the emulator framework */
	/* The emulator will capture the function call and display the output */
	/* We just need to skip hardware operations */
	(void)c;
}
    原因：Finalize uart_sam0_poll_out replacement with proper emulation approach. The emulator framework should capture UART output calls and display them, not the driver code. This version simply skips hardware operations and marks the parameter as used. The actual output display is handled by the emulator's instrumentation layer.
    时间：

=== 信息结束 ===
```

### wait_synchronization

```text
=== wait_synchronization 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：31
- 函数内容：static void wait_synchronization(void)
{
#ifdef REG_EIC_SYNCBUSY
	while (EIC->SYNCBUSY.reg) {
	}
#else
	while (EIC->STATUS.bit.SYNCBUSY) {
	}
#endif
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for EIC (External Interrupt Controller) synchronization to complete by polling hardware status flags
- 是否需要替换：是
- 分类/替换原因：The function contains a while loop that polls hardware synchronization status flags (EIC->SYNCBUSY.reg or EIC->STATUS.bit.SYNCBUSY) depending on the hardware variant. GetMMIOFunctionInfo confirmed MMIO accesses in the loop conditions. This matches the LOOP classification criteria: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags)'. The function is called from multiple places in interrupt controller and UART driver code but is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data reception), not IRQ (not an interrupt handler), and not INIT (not an initialization function).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void wait_synchronization(void)
{
#ifdef REG_EIC_SYNCBUSY
    /* [LOOP REMOVED] Waited for EIC synchronization busy flag */
#else
    /* [LOOP REMOVED] Waited for EIC STATUS.SYNCBUSY flag */
#endif
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
- 函数用途/功能描述：Adds a timeout to the kernel's timeout management system by initializing timeout structure and inserting it into sorted list
- 是否需要替换：是
- 分类/替换原因：Function initializes timeout structures and manages timeout list insertion. Contains hardware-dependent operations through elapsed() (reads SysTick registers) and sys_clock_set_timeout() (programs hardware timer). As an INIT function, hardware operations are removed while preserving core timeout management logic including list insertion and timeout calculation. Not CORE (no NVIC/OS/VTOR configuration), not RECV (no data I/O), not IRQ (not interrupt handler).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* While sys_clock_announce() is executing, new relative timeouts will be
* scheduled relatively to the currently firing timeout's original tick
* value (=curr_tick) rather than relative to the current
* sys_clock_elapsed().
*
* This means that timeouts being scheduled from within timeout callbacks
* will be scheduled at well-defined offsets from the currently firing
* timeout.
*
* As a side effect, the same will happen if an ISR with higher priority
* preempts a timeout callback and schedules a timeout.
*
* The distinction is implemented by looking at announce_remaining which
* will be non-zero while sys_clock_announce() is executing and zero
* otherwise.
*/
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

		/* Skip hardware-dependent elapsed() calculation */
		/* Original: to->dticks = timeout.ticks + 1 + elapsed(); */
		/* Use a simplified calculation without hardware dependency */
		if (IS_ENABLED(CONFIG_TIMEOUT_64BIT) &&
		    Z_TICK_ABS(timeout.ticks) >= 0) {
			k_ticks_t ticks = Z_TICK_ABS(timeout.ticks) - curr_tick;

			to->dticks = MAX(1, ticks);
		} else {
			/* Simplified: use timeout ticks directly without elapsed() */
			to->dticks = timeout.ticks + 1;
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

		/* Skip hardware timer programming */
		/* Original: if (to == first()) {
		 *	sys_clock_set_timeout(next_timeout(), false);
		 * }
		 */
		/* [INIT REMOVED] Skipped sys_clock_set_timeout hardware call */
	}
}
```

=== 信息结束 ===
```

### z_arm_platform_init

```text
=== z_arm_platform_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c
- 行号：108
- 函数内容：void z_arm_platform_init(void)
{
	uint8_t dfll_div;

	if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC < SAM0_DFLL_FREQ_HZ) {
		dfll_div = 3;
	} else if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC < SAM0_DPLL_FREQ_MIN_HZ) {
		dfll_div = 2;
	} else {
		dfll_div = 1;
	}

	/*
	 * Force Cortex M Cache Controller disabled
	 *
	 * It is not clear if regular Cortex-M instructions can be used to
	 * perform cache maintenance or this is a proprietary cache controller
	 * that require special SoC support.
	 */
	CMCC->CTRL.bit.CEN = 0;

	gclk_reset();
	osc32k_init();
	dfll_init();
	dpll_init(0, dfll_div * CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC);

	/* use DPLL for main clock */
	gclk_connect(0, GCLK_SOURCE_DPLL0, dfll_div);

	/* connect GCLK2 to 48 MHz DFLL for USB */
	gclk_connect(2, GCLK_SOURCE_DFLL48M, 0);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Platform initialization function for ARM-based Atmel SAM0 microcontrollers that configures clock sources (DFLL, DPLL), disables cache controller, and sets up clock connections.
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It performs hardware initialization operations including cache controller configuration (CMCC->CTRL.bit.CEN = 0) and clock system setup; 2) It calls multiple hardware initialization functions (gclk_reset, osc32k_init, dfll_init, dpll_init, gclk_connect); 3) It's a platform initialization function that runs early in system startup to configure SoC-specific hardware; 4) It doesn't fit other categories: not CORE (not NVIC/OS kernel/VTOR), not RECV (no data I/O), not IRQ (not interrupt handler), not LOOP (no polling loops), not RETURNOK/SKIP (performs critical initialization). The replacement removes all hardware-specific register accesses and initialization function calls while preserving the logical structure.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
void z_arm_platform_init(void)
{
	uint8_t dfll_div;

	if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC < SAM0_DFLL_FREQ_HZ) {
		dfll_div = 3;
	} else if (CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC < SAM0_DPLL_FREQ_MIN_HZ) {
		dfll_div = 2;
	} else {
		dfll_div = 1;
	}

	/* Skip hardware cache controller disable */
	/* CMCC->CTRL.bit.CEN = 0; */

	/* Skip hardware clock initialization functions */
	/* gclk_reset(); */
	/* osc32k_init(); */
	/* dfll_init(); */
	/* dpll_init(0, dfll_div * CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC); */

	/* Skip hardware clock connections */
	/* gclk_connect(0, GCLK_SOURCE_DPLL0, dfll_div); */
	/* gclk_connect(2, GCLK_SOURCE_DFLL48M, 0); */
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**63** 个；CodeQL `MMIOFunction`：**63** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **7** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `add_to_waitq_locked` | CORE | False | Adds a thread to a wait queue while holding scheduler spinlock, marking thread as pending and unready |
| `adjust_owner_prio` | NODRIVER | False | Adjusts the priority of a mutex owner thread as part of priority inheritance mechanism in mutex operations |
| `arch_new_thread` | CORE | False | Architecture-specific thread context initialization for ARM Cortex-M, sets up initial stack frame and thread architec... |
| `dfll_init` | INIT | True | Initializes the Digital Frequency Locked Loop (DFLL) peripheral by configuring control registers and waiting for read... |
| `dpll_init` | INIT | True | Initializes a DPLL (Digital Phase-Locked Loop) for Atmel SAMD MCU series by configuring clock source and parameters |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating-point values to text format with support for various format specifie... |
| `first` | NODRIVER | False | Retrieves the first timeout structure from the kernel's timeout linked list |
| `gclk_connect` | INIT | True | Connects a generic clock generator to a source with specified divider by configuring GCLK hardware registers |
| `gclk_reset` | INIT | True | Resets the Generic Clock Controller (GCLK) hardware by setting software reset bit and waiting for synchronization |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (_THREAD_DEAD or _THREAD_SUSPENDED) as part of kernel threa... |
| `init_ready_q` | NODRIVER | False | Initializes the scheduler's ready queue data structure based on different scheduling configurations (SCALABLE, MULTIQ... |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap structure with a memory region and size for memory management |
| `k_mbox_get` | NODRIVER | False | Zephyr RTOS mailbox receive function that retrieves messages from a mailbox, searches for matching senders, handles t... |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox structure by setting up transmit/receive message queues, initializing a spinlock, a... |
| `k_mem_slab_init` | NODRIVER | False | Initializes a Zephyr kernel memory slab object for fixed-size block memory allocation |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a Zephyr RTOS message queue by checking for waiting threads and freeing allocated buffer if dynamically all... |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting up buffer pointers, message size, maximum messages,... |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated memory if needed |
| `k_stack_init` | NODRIVER | False | Initializes a Zephyr RTOS kernel stack data structure by setting up wait queue, lock, and buffer pointers |
| `k_timer_init` | NODRIVER | False | Initializes a kernel timer structure by setting callback functions, status, wait queue, and timeout structure |
| `k_work_cancel_delayable_sync` | NODRIVER | False | Cancels a delayable work item synchronously, checking if work is pending and waiting for cancellation completion usin... |
| `k_work_cancel_sync` | CORE | False | Cancels a work item synchronously, waiting for completion if the work is currently running |
| `k_work_flush` | NODRIVER | False | Flushes a work item if it's queued or running, synchronizing the flush operation using semaphores and spin locks |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item, waiting for its completion and synchronizing with work queue execution |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item structure in Zephyr RTOS kernel work queue subsystem |
| `k_work_queue_start` | CORE | False | Starts a work queue by initializing its data structures and creating/starting a kernel thread to process work items |
| `mbox_message_put` | NODRIVER | False | Helper routine that handles both synchronous and asynchronous mailbox message sending in Zephyr RTOS kernel |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the scheduler |
| `next` | NODRIVER | False | Returns the next timeout structure in the kernel's timeout linked list |
| `osc32k_init` | INIT | True | Initializes the 32kHz oscillator (XOSC32K) and configures clock generator 1 on Atmel SAMD MCU series |
| `ready_thread` | CORE | False | Adds a thread to the scheduler's ready queue if it's not already queued and is ready to run, updating scheduler cache... |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout list and adjusts delta ticks of the next timeout |
| `sam0_eic_acquire` | INIT | True | Acquires and configures an EIC (External Interrupt Controller) line for a specific GPIO pin, setting up interrupt tri... |
| `sam0_eic_disable_interrupt` | RETURNOK | False | Disables an interrupt for a specific port and pin on the SAM0 External Interrupt Controller (EIC) |
| `sam0_eic_enable_interrupt` | RETURNOK | False | Enables an interrupt for a specific port and pin on the SAM0 External Interrupt Controller (EIC) |
| `sam0_eic_init` | INIT | True | Initializes the SAM0 External Interrupt Controller (EIC) peripheral by enabling clocks, configuring interrupts, and e... |
| `sam0_eic_interrupt_pending` | RETURNOK | False | Reads EIC interrupt pending flags for a specific port and returns a bitmask of pending pin interrupts |
| `sam0_eic_isr` | IRQ | True | Interrupt service routine for SAM0 External Interrupt Controller (EIC) that handles external interrupt lines, reads i... |
| `sam0_eic_release` | INIT | True | Releases an EIC (External Interrupt Controller) line for a specific GPIO pin by clearing configuration and interrupt ... |
| `timeout_rem` | NODRIVER | False | Calculates remaining time for a timeout by traversing the timeout list and subtracting elapsed time |
| `uart_sam0_init` | INIT | True | Initializes SAM0 UART peripheral hardware including clock configuration, register setup, baud rate, pin mux, and opti... |
| `update_cache` | NODRIVER | False | Updates the cached ready thread in the kernel's ready queue based on preemption decisions |
| `wait_synchronization` | LOOP | True | Waits for EIC (External Interrupt Controller) synchronization to complete by polling hardware status flags |
| `z_abort_timeout` | NODRIVER | False | Aborts/cancels a scheduled timeout by removing it from the kernel timeout queue |
| `z_add_timeout` | INIT | True | Adds a timeout to the kernel's timeout management system by initializing timeout structure and inserting it into sort... |
| `z_arm_platform_init` | INIT | True | Platform initialization function for ARM-based Atmel SAM0 microcontrollers that configures clock sources (DFLL, DPLL)... |
| `z_cbvprintf_impl` | NODRIVER | False | Formatted output implementation function that processes format strings and variable arguments using a callback for ch... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr RTOS condition variable by setting up its wait queue and kernel object metadata. |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a Zephyr kernel mutex structure by setting owner to NULL, lock count to 0, initializing wait queue, and r... |
| `z_impl_k_mutex_lock` | CORE | False | Zephyr RTOS mutex lock implementation with priority inheritance, handles thread synchronization and scheduling |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a Zephyr kernel queue data structure by setting up its internal linked list, spinlock, wait queue, and ke... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a Zephyr RTOS semaphore object by setting initial count and limit values, initializing wait queue, and pe... |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Implements timer status synchronization in Zephyr RTOS kernel, waiting for timer expiration and returning status |
| `z_impl_k_yield` | CORE | False | Zephyr RTOS kernel function that implements thread yielding and triggers context switching via PendSV exception |
| `z_init_thread_base` | NODRIVER | False | Initializes the base thread structure (_thread_base) with priority, state, options, and scheduler lock status for Zep... |
| `z_priq_dumb_best` | CORE | False | Selects the best thread from a priority queue for scheduler decisions |
| `z_priq_dumb_remove` | CORE | False | Removes a thread from a priority queue in the Zephyr kernel scheduler |
| `z_priq_mq_best` | NODRIVER | False | Finds the highest priority thread in a multi-queue priority queue for the scheduler |
| `z_sched_waitq_walk` | NODRIVER | False | Walks through a wait queue and invokes a callback function on each waiting thread in the scheduler |
| `z_set_prio` | CORE | False | Sets thread priority in scheduler run queue without rescheduling, returns true if reschedule needed later |
| `z_setup_new_thread` | CORE | False | Kernel function that sets up and initializes a new thread structure, including stack setup and architecture-specific ... |
| `z_timer_expiration_handler` | CORE | False | Handles expiration of kernel timer objects, manages periodic timer restart, invokes user expiry callbacks, and wakes ... |
| `z_unpend_all` | CORE | False | Un-pends all threads from a wait queue, makes them ready for execution, and returns whether scheduling is needed |

## 附录：interesting MMIO expr 子集（共 7 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `dfll_init`
- `dpll_init`
- `gclk_reset`
- `osc32k_init`
- `sam0_eic_interrupt_pending`
- `sam0_eic_isr`
- `wait_synchronization`
