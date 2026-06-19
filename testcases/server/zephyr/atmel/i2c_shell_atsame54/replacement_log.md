## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/atmel/i2c_shell_atsame54`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `arm_core_mpu_enable` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu.c` | 263 | 1 |
| `dfll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 79 | 1 |
| `dpll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 46 | 1 |
| `elapsed` | `/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c` | 119 | 1 |
| `gclk_connect` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 101 | 1 |
| `gclk_reset` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 94 | 1 |
| `i2c_sam0_initialize` | `/home/haojie/zephyrproject/zephyr/drivers/i2c/i2c_sam0.c` | 696 | 1 |
| `osc32k_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 23 | 1 |
| `region_init` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v7_internal.h` | 29 | 2 |
| `sam0_eic_acquire` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 96 | 1 |
| `sam0_eic_init` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 335 | 1 |
| `sam0_eic_interrupt_pending` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 297 | 1 |
| `sam0_eic_isr` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 51 | 2 |
| `sam0_eic_release` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 206 | 1 |
| `set_region_number` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/cortex_m/arm_mpu_internal.h` | 32 | 1 |
| `uart_sam0_init` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 505 | 1 |
| `uart_sam0_irq_rx_enable` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 834 | 1 |
| `uart_sam0_irq_tx_disable` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 808 | 1 |
| `uart_sam0_irq_tx_enable` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 799 | 1 |
| `uart_sam0_isr` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 711 | 2 |
| `uart_sam0_poll_in` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 639 | 1 |
| `uart_sam0_poll_out` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 653 | 1 |
| `wait_synchronization` | `/home/haojie/zephyrproject/zephyr/drivers/i2c/i2c_sam0.c` | 63 | 1 |
| `z_arm_platform_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 108 | 1 |

## 2. 各函数替换详情

### arm_core_mpu_enable

```text
=== arm_core_mpu_enable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu.c
- 行号：263
- 函数内容：void arm_core_mpu_enable(void)
{
	/* Enable MPU and use the default memory map as a
	 * background region for privileged software access if desired.
	 */
#if defined(CONFIG_MPU_DISABLE_BACKGROUND_MAP)
	MPU->CTRL = MPU_CTRL_ENABLE_Msk;
#else
	MPU->CTRL = MPU_CTRL_ENABLE_Msk | MPU_CTRL_PRIVDEFENA_Msk;
#endif

	/* Make sure that all the registers are set before proceeding */
	barrier_dsync_fence_full();
	barrier_isync_fence_full();
}


【替换更新】
- 更新代码：void arm_core_mpu_enable(void)
{
	/* Enable MPU and use the default memory map as a
	 * background region for privileged software access if desired.
	 */
#if defined(CONFIG_MPU_DISABLE_BACKGROUND_MAP)
	/* MPU->CTRL = MPU_CTRL_ENABLE_Msk; - Skip in emulation */
#else
	/* MPU->CTRL = MPU_CTRL_ENABLE_Msk | MPU_CTRL_PRIVDEFENA_Msk; - Skip in emulation */
#endif

	/* Make sure that all the registers are set before proceeding */
	barrier_dsync_fence_full();
	barrier_isync_fence_full();
}
- 更新原因：MPU hardware register write (MPU->CTRL) can cause hard faults in emulator environment. This function is called during system initialization. Stubbing out the hardware access prevents emulator faults while preserving the function interface and memory barriers. This is consistent with other MPU function replacements.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void arm_core_mpu_enable(void)
{
	/* Enable MPU and use the default memory map as a
	 * background region for privileged software access if desired.
	 */
#if defined(CONFIG_MPU_DISABLE_BACKGROUND_MAP)
	/* MPU->CTRL = MPU_CTRL_ENABLE_Msk; - Skip in emulation */
#else
	/* MPU->CTRL = MPU_CTRL_ENABLE_Msk | MPU_CTRL_PRIVDEFENA_Msk; - Skip in emulation */
#endif

	/* Make sure that all the registers are set before proceeding */
	barrier_dsync_fence_full();
	barrier_isync_fence_full();
}
    原因：MPU hardware register write (MPU->CTRL) can cause hard faults in emulator environment. This function is called during system initialization. Stubbing out the hardware access prevents emulator faults while preserving the function interface and memory barriers. This is consistent with other MPU function replacements.
    时间：

=== 信息结束 ===
```

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
- 函数用途/功能描述：Initializes the Digital Frequency Locked Loop (DFLL) hardware module by configuring control registers and waiting for the DFLL to become ready.
- 是否需要替换：是
- 分类/替换原因：The function is an initialization function (as indicated by the name 'dfll_init') that configures peripheral hardware (DFLL module). GetMMIOFunctionInfo revealed hardware register writes to OSCCTRL->DFLLCTRLB.reg and OSCCTRL->DFLLCTRLA.reg, and a polling loop that waits for the DFLLRDY status bit. The function is called by z_arm_platform_init as part of platform initialization. It fits the INIT category because it performs hardware initialization with MMIO operations and polling loops, but is not a CORE function (no NVIC/OS/VTOR operations), RECV (no data transfer), or IRQ (not an interrupt handler).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void dfll_init(void)
{
	/* Skip hardware-specific configuration */
	/* [LOOP REMOVED] Waited for hardware DFLL ready flag */
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
- 函数用途/功能描述：Initializes Digital Phase-Locked Loop (DPLL) for clock generation on Atmel SAMD MCUs by configuring clock source, frequency ratio, and enabling the DPLL hardware
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of clock generation peripherals (OSCCTRL and GCLK registers) with multiple MMIO writes and polling loops. It's called from z_arm_platform_init during system initialization. Contains peripheral register configuration (DPLLCTRLA, DPLLRATIO, DPLLCTRLB, GCLK PCHCTRL) and waits for hardware status flags (DPLLSYNCBUSY, CHEN, CLKRDY, LOCK). Classification as INIT because it sets up hardware clock generation infrastructure. Not CORE (no NVIC/OS/VTOR), not RECV (no data reception), not IRQ (no interrupt handling), not LOOP (more than just a loop).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void dpll_init(uint8_t n, uint32_t f_cpu)
{
	/* We source the DPLL from 32kHz GCLK1 */
	const uint32_t LDR = ((f_cpu << 5) / SOC_ATMEL_SAM0_OSC32K_FREQ_HZ);

	/* Skip hardware configuration for DPLL initialization */
	/* Original: disable DPLL, configure clock source, set ratio, enable DPLL */
	/* Original polling loops removed: while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) */
	/* Original polling loops removed: while (!(GCLK->PCHCTRL[OSCCTRL_GCLK_ID_FDPLL0 + n].reg & GCLK_PCHCTRL_CHEN)) */
	/* Original polling loops removed: while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) */
	/* Original polling loops removed: while (!(OSCCTRL->Dpll[n].DPLLSTATUS.bit.CLKRDY && OSCCTRL->Dpll[n].DPLLSTATUS.bit.LOCK)) */

	/* Keep LDR calculation as it's pure computation */
	(void)LDR;
	(void)n;
	(void)f_cpu;
}
```

=== 信息结束 ===
```

### elapsed

```text
=== elapsed 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c
- 行号：119
- 函数内容：static uint32_t elapsed(void)
{
	uint32_t val1 = SysTick->VAL;	/* A */
	uint32_t ctrl = SysTick->CTRL;	/* B */
	uint32_t val2 = SysTick->VAL;	/* C */

	/* SysTick behavior: The counter wraps after zero automatically.
	 * The COUNTFLAG field of the CTRL register is set when it
	 * decrements from 1 to 0. Reading the control register
	 * automatically clears that field. When a timer is started,
	 * count begins at zero then wraps after the first cycle.
	 * Reference:
	 *  Armv6-m (B3.3.1) https://developer.arm.com/documentation/ddi0419
	 *  Armv7-m (B3.3.1) https://developer.arm.com/documentation/ddi0403
	 *  Armv8-m (B11.1)  https://developer.arm.com/documentation/ddi0553
	 *
	 * First, manually wrap/realign val1 and val2 from [0:last_load-1]
	 * to [1:last_load]. This allows subsequent code to assume that
	 * COUNTFLAG and wrapping occur on the same cycle.
	 *
	 * If the count wrapped...
	 * 1) Before A then COUNTFLAG will be set and val1 >= val2
	 * 2) Between A and B then COUNTFLAG will be set and val1 < val2
	 * 3) Between B and C then COUNTFLAG will be clear and val1 < val2
	 * 4) After C we'll see it next time
	 *
	 * So the count in val2 is post-wrap and last_load needs to be
	 * added if and only if COUNTFLAG is set or val1 < val2.
	 */
	if (val1 == 0) {
		val1 = last_load;
	}
	if (val2 == 0) {
		val2 = last_load;
	}

	if ((ctrl & SysTick_CTRL_COUNTFLAG_Msk)
	    || (val1 < val2)) {
		overflow_cyc += last_load;

		/* We know there was a wrap, but we might not have
		 * seen it in CTRL, so clear it. */
		(void)SysTick->CTRL;
	}

	return (last_load - val2) + overflow_cyc;
}


【替换更新】
- 更新代码：static uint32_t elapsed(void)
{
	uint32_t val1 = SysTick->VAL;	/* A */
	uint32_t ctrl = SysTick->CTRL;	/* B */
	uint32_t val2 = SysTick->VAL;	/* C */

	/* In emulation, the SysTick registers might return 0 or other values.
	 * We need to handle this gracefully to avoid calculation errors.
	 */
	
	/* If val1 or val2 are 0 (common in emulation), set them to a reasonable value */
	if (val1 == 0) {
		val1 = last_load > 0 ? last_load : 1000;
	}
	if (val2 == 0) {
		val2 = last_load > 0 ? last_load : 1000;
	}

	/* SysTick behavior: The counter wraps after zero automatically.
	 * The COUNTFLAG field of the CTRL register is set when it
	 * decrements from 1 to 0. Reading the control register
	 * automatically clears that field. When a timer is started,
	 * count begins at zero then wraps after the first cycle.
	 * Reference:
	 *  Armv6-m (B3.3.1) https://developer.arm.com/documentation/ddi0419
	 *  Armv7-m (B3.3.1) https://developer.arm.com/documentation/ddi0403
	 *  Armv8-m (B11.1)  https://developer.arm.com/documentation/ddi0553
	 *
	 * First, manually wrap/realign val1 and val2 from [0:last_load-1]
	 * to [1:last_load]. This allows subsequent code to assume that
	 * COUNTFLAG and wrapping occur on the same cycle.
	 *
	 * If the count wrapped...
	 * 1) Before A then COUNTFLAG will be set and val1 >= val2
	 * 2) Between A and B then COUNTFLAG will be set and val1 < val2
	 * 3) Between B and C then COUNTFLAG will be clear and val1 < val2
	 * 4) After C we'll see it next time
	 *
	 * So the count in val2 is post-wrap and last_load needs to be
	 * added if and only if COUNTFLAG is set or val1 < val2.
	 */
	if (val1 == 0) {
		val1 = last_load;
	}
	if (val2 == 0) {
		val2 = last_load;
	}

	if ((ctrl & SysTick_CTRL_COUNTFLAG_Msk)
	    || (val1 < val2)) {
		overflow_cyc += last_load;

		/* We know there was a wrap, but we might not have
		 * seen it in CTRL, so clear it. */
		(void)SysTick->CTRL;
	}

	return (last_load - val2) + overflow_cyc;
}
- 更新原因：Preserve SysTick register reads for emulator hooks while handling potential emulation issues. The original function reads SysTick hardware registers which the emulator needs to see. However, in emulation these registers might return 0 or unexpected values, causing calculation errors. The replacement keeps all hardware register accesses but adds safety checks to handle 0 values gracefully, preventing potential overflow or incorrect calculations that could interfere with context switching.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static uint32_t elapsed(void)
{
	uint32_t val1 = SysTick->VAL;	/* A */
	uint32_t ctrl = SysTick->CTRL;	/* B */
	uint32_t val2 = SysTick->VAL;	/* C */

	/* In emulation, the SysTick registers might return 0 or other values.
	 * We need to handle this gracefully to avoid calculation errors.
	 */
	
	/* If val1 or val2 are 0 (common in emulation), set them to a reasonable value */
	if (val1 == 0) {
		val1 = last_load > 0 ? last_load : 1000;
	}
	if (val2 == 0) {
		val2 = last_load > 0 ? last_load : 1000;
	}

	/* SysTick behavior: The counter wraps after zero automatically.
	 * The COUNTFLAG field of the CTRL register is set when it
	 * decrements from 1 to 0. Reading the control register
	 * automatically clears that field. When a timer is started,
	 * count begins at zero then wraps after the first cycle.
	 * Reference:
	 *  Armv6-m (B3.3.1) https://developer.arm.com/documentation/ddi0419
	 *  Armv7-m (B3.3.1) https://developer.arm.com/documentation/ddi0403
	 *  Armv8-m (B11.1)  https://developer.arm.com/documentation/ddi0553
	 *
	 * First, manually wrap/realign val1 and val2 from [0:last_load-1]
	 * to [1:last_load]. This allows subsequent code to assume that
	 * COUNTFLAG and wrapping occur on the same cycle.
	 *
	 * If the count wrapped...
	 * 1) Before A then COUNTFLAG will be set and val1 >= val2
	 * 2) Between A and B then COUNTFLAG will be set and val1 < val2
	 * 3) Between B and C then COUNTFLAG will be clear and val1 < val2
	 * 4) After C we'll see it next time
	 *
	 * So the count in val2 is post-wrap and last_load needs to be
	 * added if and only if COUNTFLAG is set or val1 < val2.
	 */
	if (val1 == 0) {
		val1 = last_load;
	}
	if (val2 == 0) {
		val2 = last_load;
	}

	if ((ctrl & SysTick_CTRL_COUNTFLAG_Msk)
	    || (val1 < val2)) {
		overflow_cyc += last_load;

		/* We know there was a wrap, but we might not have
		 * seen it in CTRL, so clear it. */
		(void)SysTick->CTRL;
	}

	return (last_load - val2) + overflow_cyc;
}
    原因：Preserve SysTick register reads for emulator hooks while handling potential emulation issues. The original function reads SysTick hardware registers which the emulator needs to see. However, in emulation these registers might return 0 or unexpected values, causing calculation errors. The replacement keeps all hardware register accesses but adds safety checks to handle 0 values gracefully, preventing potential overflow or incorrect calculations that could interfere with context switching.
    时间：

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
- 函数用途/功能描述：Configures a generic clock (GCLK) by connecting it to a specific clock source with a divider value
- 是否需要替换：是
- 分类/替换原因：The function performs hardware register writes to GCLK->GENCTRL[gclk].reg to configure clock sources and dividers. It is called from z_arm_platform_init during system initialization, making it an initialization function. GetMMIOFunctionInfo confirms hardware register access, and the function's purpose is to set up clock configuration which is part of peripheral initialization. Since it's not CORE (not NVIC/OS/VTOR), not RECV/IRQ/LOOP, and clearly performs hardware initialization, it's classified as INIT.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void gclk_connect(uint8_t gclk, uint8_t src, uint8_t div)
{
	/* Skip hardware-specific clock configuration */
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
- 函数用途/功能描述：Resets the GCLK (Generic Clock Controller) peripheral by setting software reset bit and waiting for synchronization
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization/reset operations: 1) Sets GCLK->CTRLA.bit.SWRST = 1 to trigger software reset, 2) Contains polling loop while(GCLK->SYNCBUSY.bit.SWRST) waiting for reset completion. This is a peripheral initialization function called by z_arm_platform_init during platform initialization. GetMMIOFunctionInfo revealed two MMIO register accesses (write to CTRLA.SWRST and read from SYNCBUSY.SWRST). Classified as INIT because it initializes/resets peripheral hardware configuration, not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (not interrupt handler). Contains LOOP element but primary purpose is initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void gclk_reset(void)
{
	/* Hardware reset removed for emulation */
	/* Skip waiting for synchronization busy flag */
}
```

=== 信息结束 ===
```

### i2c_sam0_initialize

```text
=== i2c_sam0_initialize 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/i2c/i2c_sam0.c
- 行号：696
- 函数内容：static int i2c_sam0_initialize(const struct device *dev)
{
	struct i2c_sam0_dev_data *data = dev->data;
	const struct i2c_sam0_dev_config *const cfg = dev->config;
	SercomI2cm *i2c = cfg->regs;
	int retval;

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
	/* Disable all I2C interrupts */
	i2c->INTENCLR.reg = SERCOM_I2CM_INTENCLR_MASK;

	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	/* I2C mode, enable timeouts */
	i2c->CTRLA.reg = SERCOM_I2CM_CTRLA_MODE_I2C_MASTER |
#ifdef SERCOM_I2CM_CTRLA_LOWTOUTEN
			 SERCOM_I2CM_CTRLA_LOWTOUTEN |
#endif
			 SERCOM_I2CM_CTRLA_INACTOUT(0x3);
	wait_synchronization(i2c);

	/* Enable smart mode (auto ACK) */
	i2c->CTRLB.reg = SERCOM_I2CM_CTRLB_SMEN;
	wait_synchronization(i2c);

	retval = i2c_sam0_set_apply_bitrate(dev,
					    i2c_map_dt_bitrate(cfg->bitrate));
	if (retval != 0) {
		return retval;
	}

	k_sem_init(&data->lock, 1, 1);
	k_sem_init(&data->sem, 0, 1);

	cfg->irq_config_func(dev);

#ifdef CONFIG_I2C_SAM0_DMA_DRIVEN
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}
#endif

	i2c->CTRLA.bit.ENABLE = 1;
	wait_synchronization(i2c);

	/* Force bus idle */
	i2c->STATUS.bit.BUSSTATE = 1;
	wait_synchronization(i2c);

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the SAM0 I2C hardware peripheral by configuring clocks, pins, registers, and initializing semaphores
- 是否需要替换：是
- 分类/替换原因：This function is a hardware initialization routine that configures the I2C peripheral registers (CTRLA, CTRLB, STATUS, INTENCLR), sets up clock sources (GCLK, MCLK/PM), applies pin configurations, and initializes OS resources (semaphores). It contains multiple MMIO register writes to hardware peripherals but no data transmission/reception, interrupt handling, or polling loops. The function follows the INIT pattern: it sets up hardware configuration and resources but does not perform ongoing I/O operations. GetFunctionInfo shows hardware register accesses to SercomI2cm structure members, and GetMMIOFunctionInfo confirms hardware dependencies. The replacement removes hardware-specific register writes while preserving non-hardware operations like semaphore initialization, pin control, and function calls.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
* 48 is just from the app notes, but the datasheet says
* it's ignored
*/
static int i2c_sam0_initialize(const struct device *dev)
{
	struct i2c_sam0_dev_data *data = dev->data;
	const struct i2c_sam0_dev_config *const cfg = dev->config;
	SercomI2cm *i2c = cfg->regs;
	int retval;

	/* Skip hardware clock configuration */
	/* Skip hardware register writes */

	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	/* Skip I2C mode and timeout configuration */
	/* Skip smart mode configuration */

	retval = i2c_sam0_set_apply_bitrate(dev,
					    i2c_map_dt_bitrate(cfg->bitrate));
	if (retval != 0) {
		return retval;
	}

	k_sem_init(&data->lock, 1, 1);
	k_sem_init(&data->sem, 0, 1);

	cfg->irq_config_func(dev);

#ifdef CONFIG_I2C_SAM0_DMA_DRIVEN
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}
#endif

	/* Skip hardware enable */
	/* Skip force bus idle */

	return 0;
}
```

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
- 函数用途/功能描述：Initializes the 32kHz oscillator on Atmel SAMD MCUs by configuring the XOSC32K oscillator, waiting for it to become ready, and setting up clock generator 1 to use it as source.
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of oscillator and clock peripherals with MMIO register writes (OSC32KCTRL->XOSC32K.reg and GCLK->GENCTRL[1].reg) and contains a polling loop waiting for hardware status flag (OSC32KCTRL->STATUS.bit.XOSC32KRDY). GetMMIOFunctionInfo confirmed MMIO operations. This is a peripheral initialization function called from platform initialization (z_arm_platform_init). According to priority order, INIT classification takes precedence over LOOP when both apply.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void osc32k_init(void)
{
    /* Hardware initialization removed for simulation */
}
```

=== 信息结束 ===
```

### region_init

```text
=== region_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v7_internal.h
- 行号：29
- 函数内容：static void region_init(const uint32_t index,
	const struct arm_mpu_region *region_conf)
{
	/* Select the region you want to access */
	set_region_number(index);

	/* Configure the region */
#if defined(CONFIG_CPU_AARCH32_CORTEX_R)
	/*
	 * Clear size register, which disables the entry.  It cannot be
	 * enabled as we reconfigure it.
	 */
	set_region_size(0);

	set_region_base_address(region_conf->base & MPU_RBAR_ADDR_Msk);
	set_region_attributes(region_conf->attr.rasr);
	set_region_size(region_conf->size | MPU_RASR_ENABLE_Msk);
#else
	MPU->RBAR = (region_conf->base & MPU_RBAR_ADDR_Msk)
				| MPU_RBAR_VALID_Msk | index;
	MPU->RASR = region_conf->attr.rasr | MPU_RASR_ENABLE_Msk;
	LOG_DBG("[%d] 0x%08x 0x%08x",
		index, region_conf->base, region_conf->attr.rasr);
#endif
}


【替换更新】
- 更新代码：static void region_init(const uint32_t index,
	const struct arm_mpu_region *region_conf)
{
	/* Select the region you want to access */
	/* set_region_number(index); - Skip hardware access in emulation */

	/* Configure the region */
#if defined(CONFIG_CPU_AARCH32_CORTEX_R)
	/*
	 * Clear size register, which disables the entry.  It cannot be
	 * enabled as we reconfigure it.
	 */
	/* set_region_size(0); - Skip hardware access in emulation */

	/* set_region_base_address(region_conf->base & MPU_RBAR_ADDR_Msk); - Skip */
	/* set_region_attributes(region_conf->attr.rasr); - Skip */
	/* set_region_size(region_conf->size | MPU_RASR_ENABLE_Msk); - Skip */
#else
	/* Skip MPU register writes in emulation to avoid hardware faults */
	/* MPU->RBAR = (region_conf->base & MPU_RBAR_ADDR_Msk)
			| MPU_RBAR_VALID_Msk | index; */
	/* MPU->RASR = region_conf->attr.rasr | MPU_RASR_ENABLE_Msk; */
	/* LOG_DBG("[%d] 0x%08x 0x%08x",
		index, region_conf->base, region_conf->attr.rasr); */
#endif
}
- 更新原因：The LOG_DBG macro call in region_init replacement could be causing hard faults if logging subsystem tries to access hardware (UART) or if region_conf pointer is invalid. Commenting out the LOG_DBG call prevents potential memory access violations during MPU configuration in context switching. This is consistent with stubbing out all hardware-dependent operations in MPU configuration functions.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void region_init(const uint32_t index,
	const struct arm_mpu_region *region_conf)
{
	/* Select the region you want to access */
	/* set_region_number(index); - Skip hardware access in emulation */

	/* Configure the region */
#if defined(CONFIG_CPU_AARCH32_CORTEX_R)
	/*
	 * Clear size register, which disables the entry.  It cannot be
	 * enabled as we reconfigure it.
	 */
	/* set_region_size(0); - Skip hardware access in emulation */

	/* set_region_base_address(region_conf->base & MPU_RBAR_ADDR_Msk); - Skip */
	/* set_region_attributes(region_conf->attr.rasr); - Skip */
	/* set_region_size(region_conf->size | MPU_RASR_ENABLE_Msk); - Skip */
#else
	/* Skip MPU register writes in emulation to avoid hardware faults */
	/* MPU->RBAR = (region_conf->base & MPU_RBAR_ADDR_Msk)
			| MPU_RBAR_VALID_Msk | index; */
	/* MPU->RASR = region_conf->attr.rasr | MPU_RASR_ENABLE_Msk; */
	LOG_DBG("[%d] 0x%08x 0x%08x",
		index, region_conf->base, region_conf->attr.rasr);
#endif
}
    原因：MPU hardware register writes (MPU->RBAR, MPU->RASR) are causing hard faults in emulator environment during context switch. The function region_init is called during MPU configuration in z_arm_configure_dynamic_mpu_regions which is part of context switching. While OS core functions shouldn't be modified, the actual hardware access to MPU registers needs to be stubbed out to prevent emulator faults. This preserves the MPU configuration logic while removing hardware-dependent operations.
    时间：

  版本 2:
    替换代码：static void region_init(const uint32_t index,
	const struct arm_mpu_region *region_conf)
{
	/* Select the region you want to access */
	/* set_region_number(index); - Skip hardware access in emulation */

	/* Configure the region */
#if defined(CONFIG_CPU_AARCH32_CORTEX_R)
	/*
	 * Clear size register, which disables the entry.  It cannot be
	 * enabled as we reconfigure it.
	 */
	/* set_region_size(0); - Skip hardware access in emulation */

	/* set_region_base_address(region_conf->base & MPU_RBAR_ADDR_Msk); - Skip */
	/* set_region_attributes(region_conf->attr.rasr); - Skip */
	/* set_region_size(region_conf->size | MPU_RASR_ENABLE_Msk); - Skip */
#else
	/* Skip MPU register writes in emulation to avoid hardware faults */
	/* MPU->RBAR = (region_conf->base & MPU_RBAR_ADDR_Msk)
			| MPU_RBAR_VALID_Msk | index; */
	/* MPU->RASR = region_conf->attr.rasr | MPU_RASR_ENABLE_Msk; */
	/* LOG_DBG("[%d] 0x%08x 0x%08x",
		index, region_conf->base, region_conf->attr.rasr); */
#endif
}
    原因：The LOG_DBG macro call in region_init replacement could be causing hard faults if logging subsystem tries to access hardware (UART) or if region_conf pointer is invalid. Commenting out the LOG_DBG call prevents potential memory access violations during MPU configuration in context switching. This is consistent with stubbing out all hardware-dependent operations in MPU configuration functions.
    时间：

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
- 函数用途/功能描述：Acquires and configures an external interrupt line on SAM0 EIC (External Interrupt Controller) with specified trigger conditions and callback
- 是否需要替换：是
- 分类/替换原因：Function initializes and configures the SAM0 EIC peripheral hardware: accesses EIC configuration registers (EIC->CONFIG[config_index].reg), enables/disables EIC via set_eic_enable(), waits for hardware synchronization, clears interrupt flags (EIC->INTFLAG.reg), and configures interrupt trigger conditions. It manages software data structures for line assignment tracking. Classified as INIT because it performs peripheral initialization and configuration operations. Not CORE (doesn't configure NVIC/OS/VTOR), not IRQ (not an interrupt handler), not RECV (no data I/O), not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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
	/* config &= ~(0xF << config_shift); */
	/* switch (trigger) { ... } */
	/* if (filter) { ... } */
	/* EIC->CONFIG[config_index].reg = config; */

	/* Skip hardware enable and synchronization */
	/* set_eic_enable(1); */
	/* wait_synchronization(); */
	/* Skip clearing hardware interrupt flags */
	/* EIC->INTFLAG.reg = mask; */
	irq_unlock(key);
	return 0;

err_in_use:
	/* Skip hardware enable and synchronization */
	/* set_eic_enable(1); */
	/* wait_synchronization(); */
	irq_unlock(key);
	return -EBUSY;
}
```

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
- 函数用途/功能描述：Initializes the SAM0 External Interrupt Controller (EIC) peripheral by enabling clocks, configuring interrupts, and enabling the EIC module.
- 是否需要替换：是
- 分类/替换原因：Function is a peripheral initialization routine that: 1) Enables EIC clock via MCLK/PM registers, 2) Configures GCLK for EIC, 3) Calls SAM0_EIC_IRQ_CONNECT macros (which expand to arch_irq_enable and z_arm_irq_priority_set - NVIC/CORE functions), 4) Calls set_eic_enable() to enable EIC hardware, 5) Calls wait_synchronization(). GetMMIOFunctionInfo showed hardware register accesses. The function calls CORE functions (NVIC configuration) which must be preserved in replacement. Classification as INIT follows strategy: remove hardware register accesses but preserve CORE function calls and return success.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Clear any pending interrupt for it */
static int sam0_eic_init(const struct device *dev)
{
	ARG_UNUSED(dev);

	/* Skip hardware-specific clock configuration */
	/* Original: MCLK->APBAMASK.reg |= MCLK_APBAMASK_EIC; or PM->APBAMASK.bit.EIC_ = 1; */
	/* Original: GCLK->PCHCTRL[EIC_GCLK_ID].reg = ... or GCLK->CLKCTRL.reg = ... */

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

	/* Skip hardware enable and synchronization wait */
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
- 函数类型：LOOP
- 函数用途/功能描述：Reads EIC interrupt flag register and returns bitmask of pending interrupts for a specific port
- 是否需要替换：是
- 分类/替换原因：This function contains a hardware-dependent loop that reads from the EIC->INTFLAG.reg register to check for pending interrupts. The for loop iterates through EIC lines and checks if interrupt flags are set in the hardware register. According to the classification criteria, functions with loops that depend on peripheral register values (polling status flags) are classified as LOOP. The function reads hardware interrupt status but doesn't perform data transmission/reception, isn't an interrupt handler, and isn't an initialization function.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
uint32_t sam0_eic_interrupt_pending(int port)
{
	const struct device *const dev = DEVICE_DT_INST_GET(0);
	struct sam0_eic_data *dev_data = dev->data;
	struct sam0_eic_line_assignment *line_assignment;
	uint32_t mask = 0;

	/* [LOOP REMOVED] Original loop checked EIC->INTFLAG.reg for pending interrupts */
	/* Simulating no pending interrupts by returning 0 */
	return 0;
}
```

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
- 函数用途/功能描述：Interrupt Service Routine for SAM0 External Interrupt Controller (EIC) that processes pending external interrupts and calls registered callback functions for each triggered interrupt line.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt handler (ISR) for the SAM0 EIC peripheral. GetFunctionInfo shows it reads from EIC->INTFLAG.reg to get pending interrupts and writes back to acknowledge them. GetMMIOFunctionInfo confirms hardware register accesses. The function processes interrupt bits, maps them to port/pin assignments, and calls callback functions. It fits the IRQ classification as it contains interrupt handling logic with hardware operations that need to be removed while preserving the callback execution flow. It is not CORE (not NVIC/OS kernel/VTOR related), not RECV (no data reception), not INIT (not initialization), not LOOP (though it has a loop, it's for processing interrupts, not peripheral-dependent polling).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits;
	uint32_t line_index;

	/* Simulate interrupt flag being set - read simulated interrupt bits */
	bits = HAL_BE_return_1() ? 0x0001 : 0x0000; /* Simulate at least one interrupt pending */

	/* Skip hardware interrupt acknowledgment (EIC->INTFLAG.reg = bits) */

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
- 更新代码：static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits;
	uint32_t line_index;

	/* In emulation, we don't simulate any EIC interrupts by default.
	 * This prevents accessing potentially uninitialized callback data
	 * for interrupt lines that haven't been configured.
	 */
	bits = 0x0000; /* No interrupts pending in emulation */

	/* Skip hardware interrupt acknowledgment (EIC->INTFLAG.reg = bits) */

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

		/* Check if callback is registered before calling */
		if (port_data->cb) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
}
- 更新原因：Fix potential hard fault in sam0_eic_isr by not simulating any interrupts by default. The previous replacement was simulating an interrupt on line 0 (bits = 0x0001), which could cause the ISR to access uninitialized or invalid callback data if line 0 was not configured. This could lead to memory corruption and subsequent hard faults during context switching. By setting bits = 0x0000 (no interrupts pending), we avoid accessing potentially invalid memory while still preserving the ISR structure for compilation.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits;
	uint32_t line_index;

	/* Simulate interrupt flag being set - simulate at least one interrupt pending */
	/* In emulation, we can simulate that interrupt 0 is pending */
	bits = 0x0001; /* Simulate interrupt on line 0 */

	/* Skip hardware interrupt acknowledgment (EIC->INTFLAG.reg = bits) */

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

		/* Check if callback is registered before calling */
		if (port_data->cb) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
}
    原因：Fix null function pointer issue by removing call to non-existent HAL_BE_return_1(). The replacement was calling HAL_BE_return_1() which doesn't exist in the codebase, causing the emulator to crash when trying to call a null function pointer. Updated replacement simulates interrupt bits directly (0x0001 for line 0) and adds safety check for callback pointer before calling it.
    时间：

  版本 2:
    替换代码：static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits;
	uint32_t line_index;

	/* In emulation, we don't simulate any EIC interrupts by default.
	 * This prevents accessing potentially uninitialized callback data
	 * for interrupt lines that haven't been configured.
	 */
	bits = 0x0000; /* No interrupts pending in emulation */

	/* Skip hardware interrupt acknowledgment (EIC->INTFLAG.reg = bits) */

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

		/* Check if callback is registered before calling */
		if (port_data->cb) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
}
    原因：Fix potential hard fault in sam0_eic_isr by not simulating any interrupts by default. The previous replacement was simulating an interrupt on line 0 (bits = 0x0001), which could cause the ISR to access uninitialized or invalid callback data if line 0 was not configured. This could lead to memory corruption and subsequent hard faults during context switching. By setting bits = 0x0000 (no interrupts pending), we avoid accessing potentially invalid memory while still preserving the ISR structure for compilation.
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
- 函数用途/功能描述：Releases/clears an external interrupt line configuration in the SAM0 EIC (External Interrupt Controller) peripheral
- 是否需要替换：是
- 分类/替换原因：This function performs peripheral initialization/configuration operations: it disables the EIC, clears configuration registers (EIC->CONFIG), clears interrupt enable and flag registers (EIC->INTENCLR, EIC->INTFLAG), and updates software state. It contains hardware register accesses that need to be removed but preserves OS operations (irq_lock/irq_unlock) and software state updates. The function is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler), and fits the INIT classification as it configures peripheral hardware.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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
	/* Disable the EIC - hardware operation removed */
	/* set_eic_enable(0); */
	/* wait_synchronization(); */

	/*
	 * Check to make sure the requesting actually owns the line and do
	 * nothing if it does not.
	 */
	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		goto done;
	}

	dev_data->lines[line_index].enabled = 0;

	/* Clear the EIC config, including the trigger condition - hardware operation removed */
	/* EIC->CONFIG[config_index].reg &= ~(0xF << config_shift); */

	/* Clear any pending interrupt for it - hardware operation removed */
	/* EIC->INTENCLR.reg = mask; */
	/* EIC->INTFLAG.reg = mask; */

done:
	/* Re-enable the EIC - hardware operation removed */
	/* set_eic_enable(1); */
	/* wait_synchronization(); */
	irq_unlock(key);
	return 0;
}
```

=== 信息结束 ===
```

### set_region_number

```text
=== set_region_number 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/cortex_m/arm_mpu_internal.h
- 行号：32
- 函数内容：static inline void set_region_number(uint32_t index)
{
	MPU->RNR = index;
}


【替换更新】
- 更新代码：static inline void set_region_number(uint32_t index)
{
	/* Skip MPU register write in emulation to avoid hardware faults */
	/* MPU->RNR = index; */
}
- 更新原因：MPU hardware register write (MPU->RNR) can cause hard faults in emulator environment. This function is called by region_init during MPU configuration in context switching. Stubbing out the hardware access prevents emulator faults while preserving the function interface.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline void set_region_number(uint32_t index)
{
	/* Skip MPU register write in emulation to avoid hardware faults */
	/* MPU->RNR = index; */
}
    原因：MPU hardware register write (MPU->RNR) can cause hard faults in emulator environment. This function is called by region_init during MPU configuration in context switching. Stubbing out the hardware access prevents emulator faults while preserving the function interface.
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
- 函数用途/功能描述：Initializes the SAM0 UART peripheral hardware, configuring clocks, pins, baudrate, interrupts, and DMA (if enabled).
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization with multiple MMIO register writes (GCLK clock control, PM clock enable, UART interrupt disable, CTRLA/CTRLB configuration, UART enable). It configures the UART peripheral for operation, sets up data structures, and calls interrupt configuration function (which may configure NVIC). Classified as INIT because it initializes peripheral hardware and contains hardware-specific register access operations that need to be removed in replacement while preserving non-hardware logic and calls to CORE functions (irq_config_func).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	SercomUsart * const usart = cfg->regs;

	/* Skip hardware clock configuration */
	/* Skip hardware register writes */

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Skip hardware baudrate configuration, but preserve baudrate in cache */
	dev_data->config_cache.baudrate = cfg->baudrate;

#if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_SAM0_ASYNC
	/* Preserve interrupt configuration function call (may configure NVIC) */
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

	/* Skip hardware enable */
	/* Set device state to ready */
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
	/* In emulation, RX interrupts are not needed.
	 * We don't simulate RX data arrival.
	 */
	ARG_UNUSED(dev);
}
- 更新原因：Replace hardware-dependent UART RX interrupt enable function with empty implementation. The original function writes to hardware interrupt enable registers (INTENSET) which won't work in emulation. Since we're not simulating RX data in the emulator, this function can be a no-op.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_irq_rx_enable(const struct device *dev)
{
	/* In emulation, RX interrupts are not needed.
	 * We don't simulate RX data arrival.
	 */
	ARG_UNUSED(dev);
}
    原因：Replace hardware-dependent UART RX interrupt enable function with empty implementation. The original function writes to hardware interrupt enable registers (INTENSET) which won't work in emulation. Since we're not simulating RX data in the emulator, this function can be a no-op.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_tx_disable

```text
=== uart_sam0_irq_tx_disable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：808
- 函数内容：static void uart_sam0_irq_tx_disable(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	regs->INTENCLR.reg = SERCOM_USART_INTENCLR_DRE
			   | SERCOM_USART_INTENCLR_TXC;
}


【替换更新】
- 更新代码：static void uart_sam0_irq_tx_disable(const struct device *dev)
{
	/* In emulation, we don't have hardware interrupts to disable */
	ARG_UNUSED(dev);
}
- 更新原因：Replace hardware-dependent UART TX interrupt disable function with empty implementation. The original function writes to hardware interrupt clear registers (INTENCLR) which won't work in emulation. Since we're not using real hardware interrupts, this function can be a no-op.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_irq_tx_disable(const struct device *dev)
{
	/* In emulation, we don't have hardware interrupts to disable */
	ARG_UNUSED(dev);
}
    原因：Replace hardware-dependent UART TX interrupt disable function with empty implementation. The original function writes to hardware interrupt clear registers (INTENCLR) which won't work in emulation. Since we're not using real hardware interrupts, this function can be a no-op.
    时间：

=== 信息结束 ===
```

### uart_sam0_irq_tx_enable

```text
=== uart_sam0_irq_tx_enable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：799
- 函数内容：static void uart_sam0_irq_tx_enable(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	regs->INTENSET.reg = SERCOM_USART_INTENSET_DRE
			   | SERCOM_USART_INTENSET_TXC;
}


【替换更新】
- 更新代码：static void uart_sam0_irq_tx_enable(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* In emulation, we don't actually enable hardware interrupts.
	 * Instead, we simulate that the transmit buffer is ready
	 * by immediately calling the callback if one is registered.
	 */
#if CONFIG_UART_INTERRUPT_DRIVEN
	if (dev_data->cb) {
		/* Simulate Data Register Empty (DRE) interrupt */
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif
}
- 更新原因：Replace hardware-dependent UART interrupt enable function with POSIX-compatible implementation. The original function writes to hardware interrupt enable registers (INTENSET) which won't work in emulation. This causes UART transmission to stall because interrupts never fire. The replacement simulates immediate interrupt callback invocation to allow data transmission to proceed without waiting for hardware interrupts.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_irq_tx_enable(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* In emulation, we don't actually enable hardware interrupts.
	 * Instead, we simulate that the transmit buffer is ready
	 * by immediately calling the callback if one is registered.
	 */
#if CONFIG_UART_INTERRUPT_DRIVEN
	if (dev_data->cb) {
		/* Simulate Data Register Empty (DRE) interrupt */
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif
}
    原因：Replace hardware-dependent UART interrupt enable function with POSIX-compatible implementation. The original function writes to hardware interrupt enable registers (INTENSET) which won't work in emulation. This causes UART transmission to stall because interrupts never fire. The replacement simulates immediate interrupt callback invocation to allow data transmission to proceed without waiting for hardware interrupts.
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
	struct uart_sam0_dev_data *const dev_data = dev->data;

#if CONFIG_UART_INTERRUPT_DRIVEN
	/* In emulation, immediately call the callback to simulate
	 * transmission completion. This prevents the shell from
	 * waiting forever for UART interrupts.
	 */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif

#if CONFIG_UART_SAM0_ASYNC
	/* For async mode, simulate TX completion */
	if (dev_data->tx_len) {
		/* Simulate TX complete interrupt */
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

	/* For async RX, we don't simulate RX in emulation */
#endif
}
- 更新原因：Add safety NULL check for callback in uart_sam0_isr replacement. The replacement already had a check for dev_data->cb in the CONFIG_UART_INTERRUPT_DRIVEN section, but we should ensure the code is safe. This prevents potential null pointer dereference if the callback is not registered, which could cause hard faults during interrupt handling.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_isr(const struct device *dev)
{
	struct uart_sam0_dev_data *const dev_data = dev->data;

#if CONFIG_UART_INTERRUPT_DRIVEN
	/* In emulation, immediately call the callback to simulate
	 * transmission completion. This prevents the shell from
	 * waiting forever for UART interrupts.
	 */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif

#if CONFIG_UART_SAM0_ASYNC
	/* For async mode, simulate TX completion */
	if (dev_data->tx_len) {
		/* Simulate TX complete interrupt */
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

	/* For async RX, we don't simulate RX in emulation */
#endif
}
    原因：Replace hardware-dependent UART ISR with POSIX-compatible implementation. The original function checks hardware interrupt flags (INTFLAG.bit.TXC, INTFLAG.bit.RXC) which won't be set in emulation. This causes the shell to wait forever for UART transmission completion interrupts. The replacement simulates immediate transmission completion by calling callbacks directly, allowing the shell to continue execution instead of blocking indefinitely in k_poll.
    时间：

  版本 2:
    替换代码：static void uart_sam0_isr(const struct device *dev)
{
	struct uart_sam0_dev_data *const dev_data = dev->data;

#if CONFIG_UART_INTERRUPT_DRIVEN
	/* In emulation, immediately call the callback to simulate
	 * transmission completion. This prevents the shell from
	 * waiting forever for UART interrupts.
	 */
	if (dev_data->cb) {
		dev_data->cb(dev, dev_data->cb_data);
	}
#endif

#if CONFIG_UART_SAM0_ASYNC
	/* For async mode, simulate TX completion */
	if (dev_data->tx_len) {
		/* Simulate TX complete interrupt */
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

	/* For async RX, we don't simulate RX in emulation */
#endif
}
    原因：Add safety NULL check for callback in uart_sam0_isr replacement. The replacement already had a check for dev_data->cb in the CONFIG_UART_INTERRUPT_DRIVEN section, but we should ensure the code is safe. This prevents potential null pointer dereference if the callback is not registered, which could cause hard faults during interrupt handling.
    时间：

=== 信息结束 ===
```

### uart_sam0_poll_in

```text
=== uart_sam0_poll_in 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c
- 行号：639
- 函数内容：static int uart_sam0_poll_in(const struct device *dev, unsigned char *c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	if (!usart->INTFLAG.bit.RXC) {
		return -EBUSY;
	}

	*c = (unsigned char)usart->DATA.reg;
	return 0;
}


【替换更新】
- 更新代码：static int uart_sam0_poll_in(const struct device *dev, unsigned char *c)
{
	/* In emulation, we don't have real UART input.
	 * Return -EBUSY to indicate no data available.
	 */
	ARG_UNUSED(dev);
	ARG_UNUSED(c);
	
	return -EBUSY;
}
- 更新原因：Replace hardware-dependent UART poll in function with POSIX-compatible implementation. The original function checks hardware receive flag (INTFLAG.bit.RXC) and reads from hardware data register, which won't work in emulation. The replacement returns -EBUSY to indicate no data available, simulating an empty UART receive buffer.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_poll_in(const struct device *dev, unsigned char *c)
{
	/* In emulation, we don't have real UART input.
	 * Return -EBUSY to indicate no data available.
	 */
	ARG_UNUSED(dev);
	ARG_UNUSED(c);
	
	return -EBUSY;
}
    原因：Replace hardware-dependent UART poll in function with POSIX-compatible implementation. The original function checks hardware receive flag (INTFLAG.bit.RXC) and reads from hardware data register, which won't work in emulation. The replacement returns -EBUSY to indicate no data available, simulating an empty UART receive buffer.
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
	/* In emulation, skip hardware wait loop and register write.
	 * We can optionally output the character for debugging.
	 */
	ARG_UNUSED(dev);
	ARG_UNUSED(c);
	
	/* Character sent (simulated) */
}
- 更新原因：Replace hardware-dependent UART poll out function with POSIX-compatible implementation. The original function has a busy-wait loop checking hardware flag (INTFLAG.bit.DRE) which will never be true in emulation, causing infinite loop. It also writes to hardware data register. The replacement removes the wait loop and hardware write while preserving the function signature.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	/* In emulation, skip hardware wait loop and register write.
	 * We can optionally output the character for debugging.
	 */
	ARG_UNUSED(dev);
	ARG_UNUSED(c);
	
	/* Character sent (simulated) */
}
    原因：Replace hardware-dependent UART poll out function with POSIX-compatible implementation. The original function has a busy-wait loop checking hardware flag (INTFLAG.bit.DRE) which will never be true in emulation, causing infinite loop. It also writes to hardware data register. The replacement removes the wait loop and hardware write while preserving the function signature.
    时间：

=== 信息结束 ===
```

### wait_synchronization

```text
=== wait_synchronization 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/i2c/i2c_sam0.c
- 行号：63
- 函数内容：static void wait_synchronization(SercomI2cm *regs)
{
#if defined(SERCOM_I2CM_SYNCBUSY_MASK)
	/* SYNCBUSY is a register */
	while ((regs->SYNCBUSY.reg & SERCOM_I2CM_SYNCBUSY_MASK) != 0) {
	}
#elif defined(SERCOM_I2CM_STATUS_SYNCBUSY)
	/* SYNCBUSY is a bit */
	while ((regs->STATUS.reg & SERCOM_I2CM_STATUS_SYNCBUSY) != 0) {
	}
#else
#error Unsupported device
#endif
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for hardware synchronization by polling SYNCBUSY or STATUS register flags until synchronization is complete
- 是否需要替换：是
- 分类/替换原因：The function contains peripheral-dependent polling loops that wait for hardware synchronization flags (SYNCBUSY or STATUS bits) to clear. GetMMIOFunctionInfo confirmed MMIO operations in while loops accessing hardware registers. The function is called from multiple driver initialization and configuration functions (i2c_sam0_initialize, uart_sam0_init, etc.) to ensure hardware is ready before proceeding. This matches the LOOP classification criteria: loops where the condition depends on peripheral registers. It's not CORE (no NVIC/OS/VTOR), not RECV (no data transfer), not IRQ (not an interrupt handler), not INIT (doesn't initialize hardware), not RETURNOK/SKIP (critical for synchronization), and not NODRIVER (clearly interacts with hardware).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void wait_synchronization(SercomI2cm *regs)
{
#if defined(SERCOM_I2CM_SYNCBUSY_MASK)
	/* SYNCBUSY is a register */
	/* [LOOP REMOVED] Waited for hardware synchronization busy flag to clear */
#elif defined(SERCOM_I2CM_STATUS_SYNCBUSY)
	/* SYNCBUSY is a bit */
	/* [LOOP REMOVED] Waited for hardware synchronization busy flag to clear */
#else
#error Unsupported device
#endif
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
- 函数用途/功能描述：Initializes ARM platform hardware including clock systems (DFLL, DPLL, GCLK) and disables Cortex-M cache controller
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization for the ARM platform: 1) Disables Cortex-M cache controller via direct register access (CMCC->CTRL.bit.CEN = 0), 2) Calls multiple hardware initialization functions (gclk_reset, osc32k_init, dfll_init, dpll_init, gclk_connect) to set up clock systems. It contains clear hardware register access and peripheral initialization operations, fitting the INIT category definition. It is not CORE (no NVIC/OS kernel/VTOR operations), not RECV (no data I/O), not IRQ (not an interrupt handler). The function is purely hardware initialization with no upper-layer data structures to preserve.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
void z_arm_platform_init(void)
{
	/* Hardware initialization removed for simulation */
	/* Original function disabled cache controller and initialized clock systems */
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**79** 个；CodeQL `MMIOFunction`：**79** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **7** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `add_to_head` | NODRIVER | False | Adds a shell history item to the head of a doubly linked list by copying data and updating list pointers |
| `add_to_waitq_locked` | CORE | False | Adds a thread to a wait queue while holding the scheduler spinlock, marking the thread as unready and pending. |
| `adjust_owner_prio` | NODRIVER | False | Adjusts the priority of a mutex owner thread when the mutex priority changes |
| `arch_new_thread` | INIT | False | Initializes architecture-specific thread context including stack frame setup, program counter, arguments, and process... |
| `dfll_init` | INIT | True | Initializes the Digital Frequency Locked Loop (DFLL) hardware module by configuring control registers and waiting for... |
| `dpll_init` | INIT | True | Initializes Digital Phase-Locked Loop (DPLL) for clock generation on Atmel SAMD MCUs by configuring clock source, fre... |
| `encode_float` | NODRIVER | False | Converts a double-precision floating-point value to text format according to printf-style formatting specifications |
| `first` | NODRIVER | False | Returns the first timeout structure from the kernel's timeout linked list |
| `gclk_connect` | INIT | True | Configures a generic clock (GCLK) by connecting it to a specific clock source with a divider value |
| `gclk_reset` | INIT | True | Resets the GCLK (Generic Clock Controller) peripheral by setting software reset bit and waiting for synchronization |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (THREAD_DEAD or THREAD_SUSPENDED), performing thread state ... |
| `i2c_sam0_initialize` | INIT | True | Initializes the SAM0 I2C hardware peripheral by configuring clocks, pins, registers, and initializing semaphores |
| `init_ready_q` | CORE | False | Initializes the scheduler's ready queue data structure based on the configured scheduler type (SCALABLE, MULTIQ, or D... |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap data structure by setting up wait queue and system heap with provided memory region |
| `k_mbox_get` | NODRIVER | False | Retrieves a message from a Zephyr RTOS mailbox by searching for matching senders or waiting for one to appear |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox data structure by setting up wait queues and spinlock for inter-thread communication. |
| `k_mem_slab_init` | NODRIVER | False | Initializes a memory slab allocator by setting up data structures, creating free lists, and initializing wait queues |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a Zephyr kernel message queue by checking for waiting threads and freeing allocated buffer if dynamically a... |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting up buffer pointers, size parameters, and internal d... |
| `k_poll_event_init` | NODRIVER | False | Initializes a Zephyr RTOS poll event structure with provided parameters and default values |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated memory if needed |
| `k_stack_init` | NODRIVER | False | Initializes a Zephyr RTOS kernel stack data structure with buffer pointers, wait queue, and lock |
| `k_timer_init` | NODRIVER | False | Initializes a Zephyr kernel timer object by setting callback functions and internal data structures |
| `k_work_cancel_delayable_sync` | NODRIVER | False | Cancels a delayable work item synchronously in Zephyr RTOS, checking if work is pending and waiting for cancellation ... |
| `k_work_cancel_sync` | NODRIVER | False | Cancels a work item synchronously in Zephyr RTOS, waiting for completion if the work is currently executing |
| `k_work_flush` | NODRIVER | False | Flushes a work item, waiting for it to complete if it's currently queued or running in the Zephyr RTOS work queue sub... |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item, waiting for any pending or executing work to complete in the Zephyr RTOS kernel |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item in the Zephyr kernel work queue system |
| `k_work_poll_init` | INIT | False | Initializes a pollable work structure in Zephyr RTOS kernel for polling operations with timeout support |
| `k_work_poll_submit_to_queue` | NODRIVER | False | Submits pollable work to a work queue in Zephyr RTOS, managing poll events, timeouts, and work submission |
| `k_work_queue_start` | NODRIVER | False | Starts a work queue thread in Zephyr RTOS by initializing data structures and creating/starting the work queue thread |
| `mbox_message_put` | NODRIVER | False | Helper routine that handles both synchronous and asynchronous mailbox message sends in Zephyr RTOS kernel |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the Zephyr RTOS scheduler |
| `next` | NODRIVER | False | Returns the next timeout entry in the kernel's timeout linked list |
| `osc32k_init` | INIT | True | Initializes the 32kHz oscillator on Atmel SAMD MCUs by configuring the XOSC32K oscillator, waiting for it to become r... |
| `ready_thread` | CORE | False | Adds a thread to the run queue if it's ready and not already queued, performing scheduler operations like cache updat... |
| `remove_from_tail` | NODRIVER | False | Removes the oldest item from shell history buffer by removing it from the linked list and freeing space from the ring... |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout linked list and adjusts delta ticks of the next timeout |
| `sam0_eic_acquire` | INIT | True | Acquires and configures an external interrupt line on SAM0 EIC (External Interrupt Controller) with specified trigger... |
| `sam0_eic_disable_interrupt` | CORE | False | Disables an interrupt for a specific port and pin on the SAM0 External Interrupt Controller (EIC) |
| `sam0_eic_enable_interrupt` | CORE | False | Enables an interrupt on the SAM0 External Interrupt Controller (EIC) for a specific GPIO port and pin |
| `sam0_eic_init` | INIT | True | Initializes the SAM0 External Interrupt Controller (EIC) peripheral by enabling clocks, configuring interrupts, and e... |
| `sam0_eic_interrupt_pending` | LOOP | True | Reads EIC interrupt flag register and returns bitmask of pending interrupts for a specific port |
| `sam0_eic_isr` | IRQ | True | Interrupt Service Routine for SAM0 External Interrupt Controller (EIC) that processes pending external interrupts and... |
| `sam0_eic_release` | INIT | True | Releases/clears an external interrupt line configuration in the SAM0 EIC (External Interrupt Controller) peripheral |
| `signal_poller` | CORE | False | Signals a poller thread when a poll event occurs, managing thread state transitions (pending/unpending/ready). |
| `timeout_rem` | NODRIVER | False | Calculates remaining ticks for a timeout in the kernel's timeout queue by traversing the queue and subtracting elapse... |
| `triggered_work_cancel` | NODRIVER | False | Cancels a polled work item by removing its timeout, clearing event registrations, and resetting state if the work is ... |
| `triggered_work_handler` | NODRIVER | False | Kernel work handler for triggered poll events that clears event registrations and executes the real handler |
| `uart_sam0_init` | INIT | True | Initializes the SAM0 UART peripheral hardware, configuring clocks, pins, baudrate, interrupts, and DMA (if enabled). |
| `update_cache` | CORE | False | Scheduler function that updates the ready queue cache based on preemption decisions, determining whether to cache the... |
| `wait_synchronization` | LOOP | True | Waits for hardware synchronization by polling SYNCBUSY or STATUS register flags until synchronization is complete |
| `z_abort_timeout` | NODRIVER | False | Aborts/cancels a kernel timeout by removing it from the timeout queue if it's currently scheduled. |
| `z_add_timeout` | NODRIVER | False | Adds a timeout to the kernel's sorted timeout list and updates system clock timeout if needed |
| `z_arm_platform_init` | INIT | True | Initializes ARM platform hardware including clock systems (DFLL, DPLL, GCLK) and disables Cortex-M cache controller |
| `z_cbvprintf_impl` | NODRIVER | False | Core printf-style formatting implementation that processes format strings, extracts arguments from va_list, and outpu... |
| `z_handle_obj_poll_events` | NODRIVER | False | Zephyr RTOS kernel function that handles poll events by retrieving events from a list and signaling them with a given... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr kernel condition variable by setting up its wait queue and kernel object tracking |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a Zephyr kernel mutex structure by setting owner to NULL, lock count to 0, initializing wait queue, and c... |
| `z_impl_k_mutex_lock` | CORE | False | Zephyr RTOS mutex lock implementation with priority inheritance and timeout support |
| `z_impl_k_poll` | CORE | False | Zephyr RTOS kernel poll system call implementation that waits for events (semaphores, FIFOs, queues, etc.) to become ... |
| `z_impl_k_poll_signal_init` | NODRIVER | False | Initializes a Zephyr RTOS poll signal object by setting up its internal data structures and state |
| `z_impl_k_poll_signal_raise` | NODRIVER | False | Raises a poll signal in Zephyr RTOS, setting the signal result and signaled flag, then signals any waiting poll event... |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a Zephyr kernel queue data structure by setting up its internal linked lists, spinlock, wait queue, and k... |
| `z_impl_k_sem_init` | CORE | False | Initializes a Zephyr RTOS semaphore object by setting initial count and limit values, initializing wait queue, and pe... |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Implements timer status synchronization in Zephyr RTOS kernel, waiting for timer expiration and returning status |
| `z_impl_k_yield` | CORE | False | Kernel scheduler function that implements thread yielding by moving the current thread in the scheduler queue and tri... |
| `z_init_thread_base` | NODRIVER | False | Initializes the base structure of a Zephyr kernel thread with priority, state, and options |
| `z_priq_dumb_best` | NODRIVER | False | Retrieves the highest priority thread from a scheduler priority queue by peeking at the head of a doubly-linked list. |
| `z_priq_dumb_remove` | CORE | False | Removes a thread from a priority queue (doubly-linked list) in the Zephyr RTOS scheduler |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue for the Zephyr kernel scheduler |
| `z_sched_waitq_walk` | CORE | False | Walks through a wait queue and invokes a callback function on each waiting thread, used by the OS scheduler. |
| `z_set_prio` | CORE | False | Priority set utility that changes thread priority in the scheduler's run queue state without performing rescheduling,... |
| `z_setup_new_thread` | CORE | False | Initializes a new thread structure and sets up its stack and architectural context for the Zephyr RTOS kernel |
| `z_shell_history_get` | NODRIVER | False | Retrieves command history items from shell history buffer, navigating through a doubly-linked list based on direction... |
| `z_shell_history_init` | NODRIVER | False | Initializes shell history data structures by setting up a doubly linked list and resetting the current pointer |
| `z_shell_history_put` | NODRIVER | False | Adds a command line to the shell history buffer using ring buffer and linked list management |
| `z_timer_expiration_handler` | NODRIVER | False | Handles expiration of kernel timer objects, manages periodic timer restart, invokes user expiry functions, and wakes ... |
| `z_unpend_all` | CORE | False | Un-pends all threads from a wait queue and marks them as ready for scheduling |

## 附录：interesting MMIO expr 子集（共 7 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `dfll_init`
- `dpll_init`
- `gclk_reset`
- `osc32k_init`
- `sam0_eic_interrupt_pending`
- `sam0_eic_isr`
- `wait_synchronization`
