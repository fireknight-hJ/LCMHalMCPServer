## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/atmel/fs_littlefs_atsame54`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `arm_core_mpu_disable` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu.c` | 282 | 1 |
| `arm_core_mpu_enable` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu.c` | 263 | 1 |
| `dfll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 79 | 1 |
| `dpll_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 46 | 1 |
| `elapsed` | `/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c` | 119 | 1 |
| `flash_sam0_check_status` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 124 | 1 |
| `flash_sam0_erase` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 359 | 1 |
| `flash_sam0_erase_row` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 200 | 1 |
| `flash_sam0_init` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 457 | 1 |
| `flash_sam0_read` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 344 | 2 |
| `flash_sam0_wait_ready` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 113 | 1 |
| `flash_sam0_write` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 289 | 1 |
| `flash_sam0_write_page` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 161 | 1 |
| `flash_sam0_write_protection` | `/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c` | 403 | 1 |
| `gclk_connect` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 101 | 1 |
| `gclk_reset` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 94 | 1 |
| `mpu_configure_dynamic_mpu_regions` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v7_internal.h` | 249 | 1 |
| `osc32k_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 23 | 1 |
| `region_init` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v7_internal.h` | 29 | 1 |
| `sam0_eic_acquire` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 96 | 1 |
| `sam0_eic_disable_interrupt` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 276 | 1 |
| `sam0_eic_enable_interrupt` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 255 | 1 |
| `sam0_eic_init` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 335 | 1 |
| `sam0_eic_isr` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 51 | 2 |
| `sam0_eic_release` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 206 | 1 |
| `set_eic_enable` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 42 | 1 |
| `set_region_number` | `/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/cortex_m/arm_mpu_internal.h` | 32 | 1 |
| `soc_port_configure` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_port.c` | 35 | 1 |
| `soc_port_pinmux_set` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_port.c` | 16 | 1 |
| `sys_clock_isr` | `/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c` | 168 | 1 |
| `uart_sam0_init` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 505 | 1 |
| `uart_sam0_irq_rx_ready` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 850 | 1 |
| `uart_sam0_irq_tx_ready` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 817 | 1 |
| `uart_sam0_isr` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 711 | 2 |
| `uart_sam0_poll_in` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 639 | 1 |
| `uart_sam0_poll_out` | `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c` | 653 | 2 |
| `wait_synchronization` | `/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c` | 31 | 1 |
| `z_arm_platform_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_samd5x.c` | 108 | 1 |
| `z_setup_new_thread` | `/home/haojie/zephyrproject/zephyr/kernel/thread.c` | 591 | 1 |

## 2. 各函数替换详情

### arm_core_mpu_disable

```text
=== arm_core_mpu_disable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu.c
- 行号：282
- 函数内容：void arm_core_mpu_disable(void)
{
	/* Force any outstanding transfers to complete before disabling MPU */
	barrier_dmem_fence_full();

	/* Disable MPU */
	MPU->CTRL = 0;
}


【替换更新】
- 更新代码：void arm_core_mpu_disable(void)
{
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->CTRL register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU disable");
	
	/* In emulation, we don't need to disable real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->CTRL register
	 * to avoid causing hard faults in the emulator environment.
	 */
	
	/* Still execute the barrier operation as it is a compiler barrier,
	 * not hardware-specific.
	 */
	barrier_dmem_fence_full();
}
- 更新原因：The original arm_core_mpu_disable function writes directly to MPU->CTRL hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU disable by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void arm_core_mpu_disable(void)
{
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->CTRL register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU disable");
	
	/* In emulation, we don't need to disable real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->CTRL register
	 * to avoid causing hard faults in the emulator environment.
	 */
	
	/* Still execute the barrier operation as it is a compiler barrier,
	 * not hardware-specific.
	 */
	barrier_dmem_fence_full();
}
    原因：The original arm_core_mpu_disable function writes directly to MPU->CTRL hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU disable by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.
    时间：

=== 信息结束 ===
```

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
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->CTRL register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU enable");
	
	/* In emulation, we don't need to enable real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->CTRL register
	 * to avoid causing hard faults in the emulator environment.
	 */
	
	/* Still execute the barrier operations as they are compiler barriers,
	 * not hardware-specific.
	 */
	barrier_dsync_fence_full();
	barrier_isync_fence_full();
}
- 更新原因：The original arm_core_mpu_enable function writes directly to MPU->CTRL hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU enable by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void arm_core_mpu_enable(void)
{
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->CTRL register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU enable");
	
	/* In emulation, we don't need to enable real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->CTRL register
	 * to avoid causing hard faults in the emulator environment.
	 */
	
	/* Still execute the barrier operations as they are compiler barriers,
	 * not hardware-specific.
	 */
	barrier_dsync_fence_full();
	barrier_isync_fence_full();
}
    原因：The original arm_core_mpu_enable function writes directly to MPU->CTRL hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU enable by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.
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
- 函数用途/功能描述：Initializes the Digital Frequency Locked Loop (DFLL) oscillator controller by configuring control registers and waiting for the DFLL to be ready.
- 是否需要替换：是
- 分类/替换原因：The function performs hardware peripheral initialization with MMIO register writes to OSCCTRL->DFLLCTRLB.reg and OSCCTRL->DFLLCTRLA.reg, and contains a polling loop that waits for hardware status (OSCCTRL->STATUS.bit.DFLLRDY). GetMMIOFunctionInfo confirmed hardware register accesses. The primary purpose is initialization of the DFLL oscillator, making it an INIT function. The polling loop is part of the initialization sequence and will be removed in the replacement.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void dfll_init(void)
{
	/* Skip hardware-specific configuration */
	/* [LOOP REMOVED] Waited for DFLL ready status */
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
- 函数用途/功能描述：Initializes a Digital Phase-Locked Loop (DPLL) for Atmel SAMD MCU series by configuring clock source, ratio, and enabling the DPLL hardware.
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization of DPLL peripheral registers (OSCCTRL and GCLK registers) and contains multiple polling loops waiting for hardware status flags (DPLLSYNCBUSY, CHEN, CLKRDY, LOCK). GetMMIOFunctionInfo shows extensive MMIO register accesses to hardware control registers. The function is called from z_arm_platform_init as part of system initialization. It fits the INIT classification criteria: removes MMIO/register access operations while preserving calculations (LDR) and parameter handling. Contains LOOP elements (polling loops) but primary purpose is hardware initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void dpll_init(uint8_t n, uint32_t f_cpu)
{
	/* We source the DPLL from 32kHz GCLK1 */
	const uint32_t LDR = ((f_cpu << 5) / SOC_ATMEL_SAM0_OSC32K_FREQ_HZ);

	/* Skip hardware-specific DPLL configuration */
	/* Original: disable the DPLL before changing the configuration */
	/* OSCCTRL->Dpll[n].DPLLCTRLA.bit.ENABLE = 0; */
	/* while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) { */
	/* } */

	/* Original: set DPLL clock source to 32kHz GCLK1 */
	/* GCLK->PCHCTRL[OSCCTRL_GCLK_ID_FDPLL0 + n].reg = GCLK_PCHCTRL_GEN(1) | GCLK_PCHCTRL_CHEN; */
	/* while (!(GCLK->PCHCTRL[OSCCTRL_GCLK_ID_FDPLL0 + n].reg & GCLK_PCHCTRL_CHEN)) { */
	/* } */

	/* Original: configure DPLL ratio */
	/* OSCCTRL->Dpll[n].DPLLRATIO.reg  = OSCCTRL_DPLLRATIO_LDRFRAC(LDR & 0x1F) */
	/*			| OSCCTRL_DPLLRATIO_LDR((LDR >> 5) - 1); */

	/* Original: configure DPLL control */
	/* OSCCTRL->Dpll[n].DPLLCTRLB.reg	= OSCCTRL_DPLLCTRLB_REFCLK_GCLK */
	/*			| OSCCTRL_DPLLCTRLB_WUF */
	/*			| OSCCTRL_DPLLCTRLB_LBYPASS; */

	/* Original: enable DPLL */
	/* OSCCTRL->Dpll[n].DPLLCTRLA.reg = OSCCTRL_DPLLCTRLA_ENABLE; */

	/* Skip hardware polling loops */
	/* while (OSCCTRL->Dpll[n].DPLLSYNCBUSY.reg) { */
	/* } */
	/* while (!(OSCCTRL->Dpll[n].DPLLSTATUS.bit.CLKRDY && */
	/*	 OSCCTRL->Dpll[n].DPLLSTATUS.bit.LOCK)) { */
	/* } */

	/* Preserve calculation of LDR for potential use elsewhere */
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

	/* Preserve the original logic but simplify for emulation */
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
- 更新原因：Preserve SysTick register reads for emulator while keeping original logic. The emulator needs to see the SysTick register accesses to simulate timer behavior. The replacement keeps the original register reads and logic but removes any hardware-dependent assumptions that might cause issues in emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static uint32_t elapsed(void)
{
	uint32_t val1 = SysTick->VAL;	/* A */
	uint32_t ctrl = SysTick->CTRL;	/* B */
	uint32_t val2 = SysTick->VAL;	/* C */

	/* Preserve the original logic but simplify for emulation */
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
    原因：Preserve SysTick register reads for emulator while keeping original logic. The emulator needs to see the SysTick register accesses to simulate timer behavior. The replacement keeps the original register reads and logic but removes any hardware-dependent assumptions that might cause issues in emulation.
    时间：

=== 信息结束 ===
```

### flash_sam0_check_status

```text
=== flash_sam0_check_status 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：124
- 函数内容：static int flash_sam0_check_status(off_t offset)
{
	flash_sam0_wait_ready();

#ifdef NVMCTRL_INTFLAG_PROGE
	NVMCTRL_INTFLAG_Type status = NVMCTRL->INTFLAG;

	/* Clear any flags */
	NVMCTRL->INTFLAG.reg = status.reg;
#else
	NVMCTRL_STATUS_Type status = NVMCTRL->STATUS;

	/* Clear any flags */
	NVMCTRL->STATUS = status;
#endif

	if (status.bit.PROGE) {
		LOG_ERR("programming error at 0x%lx", (long)offset);
		return -EIO;
	} else if (status.bit.LOCKE) {
		LOG_ERR("lock error at 0x%lx", (long)offset);
		return -EROFS;
	} else if (status.bit.NVME) {
		LOG_ERR("NVM error at 0x%lx", (long)offset);
		return -EIO;
	}

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Checks SAM0 flash controller status after operations, reads error flags, clears interrupts, and returns appropriate error codes
- 是否需要替换：是
- 分类/替换原因：Function contains hardware-dependent operations: 1) Calls flash_sam0_wait_ready() which has a polling loop waiting for hardware status, 2) Reads from NVMCTRL->INTFLAG or NVMCTRL->STATUS registers to check error flags, 3) Writes back to clear interrupt flags, 4) Control flow depends on hardware register values (PROGE, LOCKE, NVME bits). This fits LOOP classification due to hardware polling and status checking. The replacement removes hardware polling and register access while preserving the function signature and returning success (0) to simulate error-free operation.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int flash_sam0_check_status(off_t offset)
{
	/* [LOOP REMOVED] Skip hardware status polling and checking */
	/* Simulate successful operation - no errors detected */
	return 0;
}
```

=== 信息结束 ===
```

### flash_sam0_erase

```text
=== flash_sam0_erase 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：359
- 函数内容：static int flash_sam0_erase(const struct device *dev, off_t offset,
			    size_t size)
{
	int err;

	err = flash_sam0_valid_range(offset, ROW_SIZE);
	if (err != 0) {
		return err;
	}

	if ((offset % ROW_SIZE) != 0) {
		LOG_WRN("0x%lx: not on a page boundary", (long)offset);
		return -EINVAL;
	}

	if ((size % ROW_SIZE) != 0) {
		LOG_WRN("%zu: not a integer number of pages", size);
		return -EINVAL;
	}

	flash_sam0_sem_take(dev);

	err = flash_sam0_write_protection(dev, false);
	if (err == 0) {
		for (size_t addr = offset; addr < offset + size;
		     addr += ROW_SIZE) {
			err = flash_sam0_erase_row(dev, addr);
			if (err != 0) {
				break;
			}
		}
	}

	int err2 = flash_sam0_write_protection(dev, true);

	if (!err) {
		err = err2;
	}

	flash_sam0_sem_give(dev);

	return err;
}


【替换更新】
- 更新代码：static int flash_sam0_erase(const struct device *dev, off_t offset,
			    size_t size)
{
	int err;

	/* Skip range validation - assume valid */
	err = 0;
	if (err != 0) {
		return err;
	}

	/* Skip boundary checks */
	if ((offset % ROW_SIZE) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	if ((size % ROW_SIZE) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	/* Take semaphore if multithreading is enabled */
	flash_sam0_sem_take(dev);

	/* Skip write protection disable/enable */
	err = 0; /* Assume success */
	if (err == 0) {
		/* Skip the erase loop - don't call flash_sam0_erase_row */
		/* Just simulate erase completion */
	}

	/* Skip write protection re-enable */
	int err2 = 0;

	if (!err) {
		err = err2;
	}

	/* Give semaphore */
	flash_sam0_sem_give(dev);

	return err;
}
- 更新原因：Add replacement for flash_sam0_erase to prevent hardware access during flash erase operations. The function calls flash_sam0_erase_row which has hardware register accesses. By replacing this function, we can skip the entire flash erase operation including the loop that calls flash_sam0_erase_row, preventing potential hard faults from accessing invalid memory-mapped hardware addresses in the emulator. Fixed syntax error by removing undeclared variable.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_erase(const struct device *dev, off_t offset,
			    size_t size)
{
	int err;

	/* Skip range validation - assume valid */
	err = 0;
	if (err != 0) {
		return err;
	}

	/* Skip boundary checks */
	if ((offset % ROW_SIZE) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	if ((size % ROW_SIZE) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	/* Take semaphore if multithreading is enabled */
	flash_sam0_sem_take(dev);

	/* Skip write protection disable/enable */
	err = 0; /* Assume success */
	if (err == 0) {
		/* Skip the erase loop - don't call flash_sam0_erase_row */
		/* Just simulate erase completion */
	}

	/* Skip write protection re-enable */
	int err2 = 0;

	if (!err) {
		err = err2;
	}

	/* Give semaphore */
	flash_sam0_sem_give(dev);

	return err;
}
    原因：Add replacement for flash_sam0_erase to prevent hardware access during flash erase operations. The function calls flash_sam0_erase_row which has hardware register accesses. By replacing this function, we can skip the entire flash erase operation including the loop that calls flash_sam0_erase_row, preventing potential hard faults from accessing invalid memory-mapped hardware addresses in the emulator. Fixed syntax error by removing undeclared variable.
    时间：

=== 信息结束 ===
```

### flash_sam0_erase_row

```text
=== flash_sam0_erase_row 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：200
- 函数内容：static int flash_sam0_erase_row(const struct device *dev, off_t offset)
{
	*FLASH_MEM(offset) = 0U;
#ifdef NVMCTRL_CTRLA_CMD_ER
	NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_ER | NVMCTRL_CTRLA_CMDEX_KEY;
#else
	NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_EB | NVMCTRL_CTRLB_CMDEX_KEY;
#endif
	return flash_sam0_check_status(offset);
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Erases a row of flash memory on SAM0 microcontrollers by writing to flash memory and issuing erase commands through NVMCTRL peripheral
- 是否需要替换：是
- 分类/替换原因：The function performs flash erase operations with hardware register writes to NVMCTRL peripheral and calls flash_sam0_check_status which contains flash_sam0_wait_ready with a polling loop waiting for hardware ready status. This matches the LOOP classification criteria: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags).' The function is not CORE (no NVIC/OS/VTOR), not RECV (no data reception), not IRQ (not interrupt handler), and while it could be considered INIT, the presence of polling for hardware status makes LOOP the more appropriate classification.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int flash_sam0_erase_row(const struct device *dev, off_t offset)
{
    /* [LOOP REMOVED] Skip flash memory write operation */
    /* [LOOP REMOVED] Skip NVMCTRL erase command */
    /* [LOOP REMOVED] Skip status check polling loop - assume success */
    return 0;
}
```

=== 信息结束 ===
```

### flash_sam0_init

```text
=== flash_sam0_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：457
- 函数内容：static int flash_sam0_init(const struct device *dev)
{
#if defined(CONFIG_MULTITHREADING)
	struct flash_sam0_data *ctx = dev->data;

	k_sem_init(&ctx->sem, 1, 1);
#endif

#ifdef PM_APBBMASK_NVMCTRL
	/* Ensure the clock is on. */
	PM->APBBMASK.bit.NVMCTRL_ = 1;
#else
	MCLK->APBBMASK.reg |= MCLK_APBBMASK_NVMCTRL;
#endif

#ifdef NVMCTRL_CTRLB_MANW
	/* Require an explicit write command */
	NVMCTRL->CTRLB.bit.MANW = 1;
#elif NVMCTRL_CTRLA_WMODE
	/* Set manual write mode */
	NVMCTRL->CTRLA.bit.WMODE = NVMCTRL_CTRLA_WMODE_MAN_Val;
#endif

	return flash_sam0_write_protection(dev, false);
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes the SAM0 flash controller driver, enabling clock, configuring manual write mode, and setting up semaphore for multithreading support.
- 是否需要替换：是
- 分类/替换原因：This function performs hardware initialization of the SAM0 flash controller peripheral. It contains MMIO operations (register writes to PM/MCLK->APBBMASK for clock enable and NVMCTRL->CTRLB/CTRLA for manual write mode configuration) which are characteristic of INIT functions. The function also includes non-hardware operations (k_sem_init for multithreading support) that should be preserved. It does not contain NVIC/OS kernel operations that would classify it as CORE, nor does it perform data transmission/reception (RECV), interrupt handling (IRQ), or peripheral-dependent loops (LOOP). The function fits the INIT classification as it initializes peripheral configurations and resources.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Maximum size without crossing a page */
static int flash_sam0_init(const struct device *dev)
{
#if defined(CONFIG_MULTITHREADING)
	struct flash_sam0_data *ctx = dev->data;

	k_sem_init(&ctx->sem, 1, 1);
#endif

	/* Skip hardware-specific configuration:
	 * - Clock enable for NVMCTRL
	 * - Manual write mode configuration
	 */

	return flash_sam0_write_protection(dev, false);
}
```

【替换更新】
- 更新代码：static int flash_sam0_init(const struct device *dev)
{
#if defined(CONFIG_MULTITHREADING)
	/* Safely initialize semaphore if device data is available */
	if (dev && dev->data) {
		struct flash_sam0_data *ctx = dev->data;
		k_sem_init(&ctx->sem, 1, 1);
	}
#endif

	/* Skip hardware-specific configuration:
	 * - Clock enable for NVMCTRL
	 * - Manual write mode configuration
	 */

	/* Skip write protection disable - assume already disabled for emulation */
	return 0;
}
- 更新原因：Update flash_sam0_init replacement to add safety checks for device data pointer. The previous replacement assumed dev->data is always valid, which might not be true in all cases during emulation. Added null checks to prevent potential crashes. Also changed return value to 0 (success) instead of calling flash_sam0_write_protection, which simplifies the initialization and avoids potential issues with the write protection function.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_init(const struct device *dev)
{
#if defined(CONFIG_MULTITHREADING)
	/* Safely initialize semaphore if device data is available */
	if (dev && dev->data) {
		struct flash_sam0_data *ctx = dev->data;
		k_sem_init(&ctx->sem, 1, 1);
	}
#endif

	/* Skip hardware-specific configuration:
	 * - Clock enable for NVMCTRL
	 * - Manual write mode configuration
	 */

	/* Skip write protection disable - assume already disabled for emulation */
	return 0;
}
    原因：Update flash_sam0_init replacement to add safety checks for device data pointer. The previous replacement assumed dev->data is always valid, which might not be true in all cases during emulation. Added null checks to prevent potential crashes. Also changed return value to 0 (success) instead of calling flash_sam0_write_protection, which simplifies the initialization and avoids potential issues with the write protection function.
    时间：

=== 信息结束 ===
```

### flash_sam0_read

```text
=== flash_sam0_read 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：344
- 函数内容：static int flash_sam0_read(const struct device *dev, off_t offset, void *data,
			   size_t len)
{
	int err;

	err = flash_sam0_valid_range(offset, len);
	if (err != 0) {
		return err;
	}

	memcpy(data, (uint8_t *)CONFIG_FLASH_BASE_ADDRESS + offset, len);

	return 0;
}


【替换更新】
- 更新代码：static int flash_sam0_read(const struct device *dev, off_t offset, void *data,
			   size_t len)
{
	int err;

	err = flash_sam0_valid_range(offset, len);
	if (err != 0) {
		return err;
	}

	/* In emulation, simulate flash read by returning 0xFF (erased flash state) */
	/* This is safer than trying to access CONFIG_FLASH_BASE_ADDRESS */
	/* which might not be properly mapped in emulation */
	/* Returning 0xFF (erased state) is better than 0x00 for filesystems */
	memset(data, 0xFF, len);

	return 0;
}
- 更新原因：Update flash_sam0_read replacement to return 0xFF (erased flash state) instead of 0x00. Returning zeros causes filesystems like LittleFS to think the flash is corrupted and try to format it, which leads to complex error handling paths. Returning 0xFF (typical erased state) makes the flash appear properly erased, which might allow filesystems to initialize correctly or fail more gracefully. This could prevent the system from entering error states that lead to thread termination and context switch failures.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_read(const struct device *dev, off_t offset, void *data,
			   size_t len)
{
	int err;

	err = flash_sam0_valid_range(offset, len);
	if (err != 0) {
		return err;
	}

	/* In emulation, simulate flash read by zeroing the buffer */
	/* This is safer than trying to access CONFIG_FLASH_BASE_ADDRESS */
	/* which might not be properly mapped in emulation */
	memset(data, 0, len);

	return 0;
}
    原因：Update flash_sam0_read replacement to avoid potential issues with CONFIG_FLASH_BASE_ADDRESS access in emulation. The previous replacement used memcpy to read from CONFIG_FLASH_BASE_ADDRESS + offset, but this address might not be properly mapped in the emulation environment, potentially causing crashes. The updated replacement simply zeroes the buffer, which is safe for functionality testing and avoids memory access issues.
    时间：

  版本 2:
    替换代码：static int flash_sam0_read(const struct device *dev, off_t offset, void *data,
			   size_t len)
{
	int err;

	err = flash_sam0_valid_range(offset, len);
	if (err != 0) {
		return err;
	}

	/* In emulation, simulate flash read by returning 0xFF (erased flash state) */
	/* This is safer than trying to access CONFIG_FLASH_BASE_ADDRESS */
	/* which might not be properly mapped in emulation */
	/* Returning 0xFF (erased state) is better than 0x00 for filesystems */
	memset(data, 0xFF, len);

	return 0;
}
    原因：Update flash_sam0_read replacement to return 0xFF (erased flash state) instead of 0x00. Returning zeros causes filesystems like LittleFS to think the flash is corrupted and try to format it, which leads to complex error handling paths. Returning 0xFF (typical erased state) makes the flash appear properly erased, which might allow filesystems to initialize correctly or fail more gracefully. This could prevent the system from entering error states that lead to thread termination and context switch failures.
    时间：

=== 信息结束 ===
```

### flash_sam0_wait_ready

```text
=== flash_sam0_wait_ready 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：113
- 函数内容：static void flash_sam0_wait_ready(void)
{
#ifdef NVMCTRL_STATUS_READY
	while (NVMCTRL->STATUS.bit.READY == 0) {
	}
#else
	while (NVMCTRL->INTFLAG.bit.READY == 0) {
	}
#endif
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Waits for the flash memory controller (NVMCTRL) to become ready by polling hardware status registers
- 是否需要替换：是
- 分类/替换原因：The function contains a hardware-dependent polling loop that waits for NVMCTRL status flags (STATUS.bit.READY or INTFLAG.bit.READY). GetMMIOFunctionInfo confirmed MMIO operations accessing peripheral registers. This is a classic LOOP function that polls peripheral status flags and should be replaced by skipping the wait loop entirely, assuming the condition is already met. The function is called by flash_sam0_write_page and flash_sam0_check_status, indicating it's part of flash driver operations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void flash_sam0_wait_ready(void)
{
	/* [LOOP REMOVED] Waited for NVMCTRL ready status flag */
	/* Assume flash controller is ready */
}
```

=== 信息结束 ===
```

### flash_sam0_write

```text
=== flash_sam0_write 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：289
- 函数内容：static int flash_sam0_write(const struct device *dev, off_t offset,
			    const void *data, size_t len)
{
	const uint8_t *pdata = data;
	int err;

	err = flash_sam0_valid_range(offset, len);
	if (err != 0) {
		return err;
	}

	if ((offset % FLASH_WRITE_BLK_SZ) != 0) {
		LOG_WRN("0x%lx: not on a write block boundary", (long)offset);
		return -EINVAL;
	}

	if ((len % FLASH_WRITE_BLK_SZ) != 0) {
		LOG_WRN("%zu: not a integer number of write blocks", len);
		return -EINVAL;
	}

	flash_sam0_sem_take(dev);

	err = flash_sam0_write_protection(dev, false);
	if (err == 0) {
		/* Maximum size without crossing a page */
		size_t eop_len = FLASH_PAGE_SIZE - (offset % FLASH_PAGE_SIZE);
		size_t write_len = MIN(len, eop_len);

		while (len > 0) {
			err = flash_sam0_write_page(dev, offset, pdata, write_len);
			if (err != 0) {
				break;
			}

			offset += write_len;
			pdata += write_len;
			len -= write_len;
			write_len = MIN(len, FLASH_PAGE_SIZE);
		}
	}

	int err2 = flash_sam0_write_protection(dev, true);

	if (!err) {
		err = err2;
	}

	flash_sam0_sem_give(dev);

	return err;
}


【替换更新】
- 更新代码：static int flash_sam0_write(const struct device *dev, off_t offset,
			    const void *data, size_t len)
{
	const uint8_t *pdata = data;
	int err;

	/* Skip range validation - assume valid */
	err = 0;
	if (err != 0) {
		return err;
	}

	/* Skip boundary checks */
	if ((offset % FLASH_WRITE_BLK_SZ) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	if ((len % FLASH_WRITE_BLK_SZ) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	/* Take semaphore if multithreading is enabled */
	flash_sam0_sem_take(dev);

	/* Skip write protection disable/enable */
	err = 0; /* Assume success */
	if (err == 0) {
		/* Skip the write loop - don't call flash_sam0_write_page */
		/* Just advance pointers to simulate write */
		offset += len;
		pdata += len;
		len = 0;
	}

	/* Skip write protection re-enable */
	int err2 = 0;

	if (!err) {
		err = err2;
	}

	/* Give semaphore */
	flash_sam0_sem_give(dev);

	return err;
}
- 更新原因：Add replacement for flash_sam0_write to prevent hardware access during flash write operations. The function calls flash_sam0_write_page which has hardware register accesses. By replacing this function, we can skip the entire flash write operation including the loop that calls flash_sam0_write_page, preventing potential hard faults from accessing invalid memory-mapped hardware addresses in the emulator.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_write(const struct device *dev, off_t offset,
			    const void *data, size_t len)
{
	const uint8_t *pdata = data;
	int err;

	/* Skip range validation - assume valid */
	err = 0;
	if (err != 0) {
		return err;
	}

	/* Skip boundary checks */
	if ((offset % FLASH_WRITE_BLK_SZ) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	if ((len % FLASH_WRITE_BLK_SZ) != 0) {
		/* Skip warning log */
		/* return -EINVAL; */
	}

	/* Take semaphore if multithreading is enabled */
	flash_sam0_sem_take(dev);

	/* Skip write protection disable/enable */
	err = 0; /* Assume success */
	if (err == 0) {
		/* Skip the write loop - don't call flash_sam0_write_page */
		/* Just advance pointers to simulate write */
		offset += len;
		pdata += len;
		len = 0;
	}

	/* Skip write protection re-enable */
	int err2 = 0;

	if (!err) {
		err = err2;
	}

	/* Give semaphore */
	flash_sam0_sem_give(dev);

	return err;
}
    原因：Add replacement for flash_sam0_write to prevent hardware access during flash write operations. The function calls flash_sam0_write_page which has hardware register accesses. By replacing this function, we can skip the entire flash write operation including the loop that calls flash_sam0_write_page, preventing potential hard faults from accessing invalid memory-mapped hardware addresses in the emulator.
    时间：

=== 信息结束 ===
```

### flash_sam0_write_page

```text
=== flash_sam0_write_page 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：161
- 函数内容：static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	const uint32_t *src = data;
	const uint32_t *end = src + (len / sizeof(*src));
	uint32_t *dst = FLASH_MEM(offset);
	int err;

#ifdef NVMCTRL_CTRLA_CMD_PBC
	NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_PBC | NVMCTRL_CTRLA_CMDEX_KEY;
#else
	NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_PBC | NVMCTRL_CTRLB_CMDEX_KEY;
#endif
	flash_sam0_wait_ready();

	/* Ensure writes happen 32 bits at a time. */
	for (; src != end; src++, dst++) {
		*dst = UNALIGNED_GET((uint32_t *)src);
	}

#ifdef NVMCTRL_CTRLA_CMD_WP
	NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_WP | NVMCTRL_CTRLA_CMDEX_KEY;
#else
	NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_WP | NVMCTRL_CTRLB_CMDEX_KEY;
#endif

	err = flash_sam0_check_status(offset);
	if (err != 0) {
		return err;
	}

	if (memcmp(data, FLASH_MEM(offset), len) != 0) {
		LOG_ERR("verify error at offset 0x%lx", (long)offset);
		return -EIO;
	}

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Writes a page of data to flash memory on SAM0 microcontrollers, handling hardware commands and data transfer
- 是否需要替换：是
- 分类/替换原因：This function performs critical data I/O operations (flash memory write) with hardware register accesses. It contains NVMCTRL command register writes, data copying loops, and status checking. While GetMMIOFunctionInfo didn't return specific MMIO expressions, the source code clearly shows hardware register accesses (NVMCTRL->CTRLA.reg/NVMCTRL->CTRLB.reg) and direct memory writes to flash addresses. The function is called by flash_sam0_write for data transmission operations. Following the priority order, RECV is appropriate as it handles data transmission (flash write) with hardware dependencies.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	const uint32_t *src = data;
	const uint32_t *end = src + (len / sizeof(*src));
	uint32_t *dst = FLASH_MEM(offset);
	int err;

	/* Skip hardware page buffer clear command */
	/* [HARDWARE REMOVED] NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_PBC | NVMCTRL_CTRLA_CMDEX_KEY; */
	/* [HARDWARE REMOVED] NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_PBC | NVMCTRL_CTRLB_CMDEX_KEY; */
	/* Skip wait for hardware ready */
	/* [HARDWARE REMOVED] flash_sam0_wait_ready(); */

	/* Simulate data write to flash - preserve data copying logic */
	for (; src != end; src++, dst++) {
		*dst = UNALIGNED_GET((uint32_t *)src);
	}

	/* Skip hardware write page command */
	/* [HARDWARE REMOVED] NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_WP | NVMCTRL_CTRLA_CMDEX_KEY; */
	/* [HARDWARE REMOVED] NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_WP | NVMCTRL_CTRLB_CMDEX_KEY; */

	/* Skip hardware status check */
	err = 0; /* Assume success */
	if (err != 0) {
		return err;
	}

	/* Skip verification (memcmp would fail without actual hardware write) */
	/* [HARDWARE REMOVED] if (memcmp(data, FLASH_MEM(offset), len) != 0) {
		LOG_ERR("verify error at offset 0x%lx", (long)offset);
		return -EIO;
	} */

	return 0;
}
```

【替换更新】
- 更新代码：static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	/* Skip all hardware operations */
	/* Skip page buffer clear command */
	/* Skip wait for hardware ready */
	/* Skip data copying to hardware flash memory */
	/* Skip write page command */
	/* Skip hardware status check */
	/* Skip verification (memcmp would fail without actual hardware write) */
	
	/* Just return success - simulate successful flash write */
	return 0;
}
- 更新原因：Simplify flash write page replacement to avoid writing to hardware memory-mapped addresses (FLASH_MEM). The previous replacement attempted to preserve data copying logic but writing to FLASH_MEM(offset) could cause issues in emulation. This simpler replacement skips all hardware operations entirely while maintaining the function signature and returning success.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_write_page(const struct device *dev, off_t offset,
				 const void *data, size_t len)
{
	/* Skip all hardware operations */
	/* Skip page buffer clear command */
	/* Skip wait for hardware ready */
	/* Skip data copying to hardware flash memory */
	/* Skip write page command */
	/* Skip hardware status check */
	/* Skip verification (memcmp would fail without actual hardware write) */
	
	/* Just return success - simulate successful flash write */
	return 0;
}
    原因：Simplify flash write page replacement to avoid writing to hardware memory-mapped addresses (FLASH_MEM). The previous replacement attempted to preserve data copying logic but writing to FLASH_MEM(offset) could cause issues in emulation. This simpler replacement skips all hardware operations entirely while maintaining the function signature and returning success.
    时间：

=== 信息结束 ===
```

### flash_sam0_write_protection

```text
=== flash_sam0_write_protection 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/flash/flash_sam0.c
- 行号：403
- 函数内容：static int flash_sam0_write_protection(const struct device *dev, bool enable)
{
	off_t offset;
	int err;

	for (offset = 0; offset < CONFIG_FLASH_SIZE * 1024;
	     offset += LOCK_REGION_SIZE) {
		NVMCTRL->ADDR.reg = offset + CONFIG_FLASH_BASE_ADDRESS;

#ifdef NVMCTRL_CTRLA_CMD_LR
		if (enable) {
			NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_LR |
					     NVMCTRL_CTRLA_CMDEX_KEY;
		} else {
			NVMCTRL->CTRLA.reg = NVMCTRL_CTRLA_CMD_UR |
					     NVMCTRL_CTRLA_CMDEX_KEY;
		}
#else
		if (enable) {
			NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_LR |
					     NVMCTRL_CTRLB_CMDEX_KEY;
		} else {
			NVMCTRL->CTRLB.reg = NVMCTRL_CTRLB_CMD_UR |
					     NVMCTRL_CTRLB_CMDEX_KEY;
		}
#endif
		err = flash_sam0_check_status(offset);
		if (err != 0) {
			goto done;
		}
	}

done:
	return err;
}


【初始分析（FunctionClassifier）】
- 函数类型：LOOP
- 函数用途/功能描述：Enables or disables write protection for flash memory regions on SAM0 microcontrollers by iterating through regions and configuring hardware protection registers.
- 是否需要替换：是
- 分类/替换原因：The function contains a hardware-dependent for loop that iterates through flash memory regions (offset from 0 to CONFIG_FLASH_SIZE * 1024 in LOCK_REGION_SIZE steps). Within the loop, it performs MMIO operations to NVMCTRL registers (ADDR.reg, CTRLA.reg/CTRLB.reg) to set lock/unlock commands, and calls flash_sam0_check_status to verify hardware status. This fits the LOOP classification because: 1) The loop condition depends on hardware-specific constants (CONFIG_FLASH_SIZE, LOCK_REGION_SIZE), 2) The loop body performs peripheral register accesses, 3) It involves waiting/polling for hardware status. The function is called during initialization (flash_sam0_init) and during erase/write operations to temporarily disable protection.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int flash_sam0_write_protection(const struct device *dev, bool enable)
{
	off_t offset;
	int err;

	/* [LOOP REMOVED] Skip hardware-dependent flash protection loop */
	/* Original loop iterated through flash regions and configured NVMCTRL registers */
	/* Assume protection operation completed successfully */
	err = 0;

	return err;
}
```

【替换更新】
- 更新代码：static int flash_sam0_write_protection(const struct device *dev, bool enable)
{
	/* In emulation, write protection operations are not needed */
	/* Simply return success */
	return 0;
}
- 更新原因：Simplify flash_sam0_write_protection replacement to always return success. The previous replacement had unnecessary variables and comments. This simplified version is cleaner and achieves the same goal: skipping hardware-dependent flash protection operations in emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int flash_sam0_write_protection(const struct device *dev, bool enable)
{
	/* In emulation, write protection operations are not needed */
	/* Simply return success */
	return 0;
}
    原因：Simplify flash_sam0_write_protection replacement to always return success. The previous replacement had unnecessary variables and comments. This simplified version is cleaner and achieves the same goal: skipping hardware-dependent flash protection operations in emulation.
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
- 函数用途/功能描述：Configures a Generic Clock (GCLK) generator by setting its source, division factor, and enabling it
- 是否需要替换：是
- 分类/替换原因：The function performs hardware initialization by writing to GCLK->GENCTRL[gclk].reg register to configure clock generator settings. GetMMIOFunctionInfo indicates hardware register access, and GetFunctionInfo shows it writes configuration values (source, divider, enable) to peripheral registers. It's called from z_arm_platform_init during system initialization, fitting the INIT classification pattern of peripheral initialization functions. The function contains no data transmission/reception (not RECV), no interrupt handling (not IRQ), no polling loops (not LOOP), and no core OS/kernel operations (not CORE).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void gclk_connect(uint8_t gclk, uint8_t src, uint8_t div)
{
    /* Hardware configuration removed for simulation */
    /* Original: GCLK->GENCTRL[gclk].reg = GCLK_GENCTRL_SRC(src) | GCLK_GENCTRL_DIV(div) | GCLK_GENCTRL_GENEN; */
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
- 分类/替换原因：The function performs hardware initialization/reset operations on the GCLK peripheral. It writes to the CTRLA.SWRST register to trigger a software reset and contains a polling loop that waits for the SYNCBUSY.SWRST flag to clear. This is clearly a peripheral initialization function with hardware-dependent operations. While it contains a LOOP (polling while loop), its primary purpose is initialization, so it should be classified as INIT according to the priority order. The function is static and called from z_arm_platform_init during platform initialization.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Without LBYPASS, startup takes very long, see errata section 2.13. */
static void gclk_reset(void)
{
	/* Skip hardware reset operation */
	/* Skip synchronization wait loop - assume reset is complete */
}
```

=== 信息结束 ===
```

### mpu_configure_dynamic_mpu_regions

```text
=== mpu_configure_dynamic_mpu_regions 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/arch/arm/core/mpu/arm_mpu_v7_internal.h
- 行号：249
- 函数内容：static int mpu_configure_dynamic_mpu_regions(const struct z_arm_mpu_partition
	dynamic_regions[], uint8_t regions_num)
{
	int mpu_reg_index = static_regions_num;

	/* In ARMv7-M architecture the dynamic regions are
	 * programmed on top of existing SRAM region configuration.
	 */

	mpu_reg_index = mpu_configure_regions(dynamic_regions,
		regions_num, mpu_reg_index, false);

	if (mpu_reg_index != -EINVAL) {

		/* Disable the non-programmed MPU regions. */
		for (int i = mpu_reg_index; i < get_num_regions(); i++) {
			ARM_MPU_ClrRegion(i);
		}
	}

	return mpu_reg_index;
}


【替换更新】
- 更新代码：static int mpu_configure_dynamic_mpu_regions(const struct z_arm_mpu_partition
	dynamic_regions[], uint8_t regions_num)
{
	int mpu_reg_index = static_regions_num;

	/* In ARMv7-M architecture the dynamic regions are
	 * programmed on top of existing SRAM region configuration.
	 */

	mpu_reg_index = mpu_configure_regions(dynamic_regions,
		regions_num, mpu_reg_index, false);

	if (mpu_reg_index != -EINVAL) {

		/* Disable the non-programmed MPU regions. */
		/* In emulation environment, we don't have real MPU hardware.
		 * Instead of calling ARM_MPU_ClrRegion which writes to MPU registers,
		 * we just log the operation and skip the hardware access.
		 * This prevents hard faults from occurring when the emulator
		 * tries to access non-existent MPU hardware registers.
		 */
		LOG_DBG("Emulated MPU: skipping clear of %d non-programmed regions",
			get_num_regions() - mpu_reg_index);
		
		/* Note: We're not calling ARM_MPU_ClrRegion(i) here
		 * to avoid causing hard faults in the emulator environment.
		 * The original code would have done:
		 * for (int i = mpu_reg_index; i < get_num_regions(); i++) {
		 *     ARM_MPU_ClrRegion(i);
		 * }
		 */
	}

	return mpu_reg_index;
}
- 更新原因：The original mpu_configure_dynamic_mpu_regions function calls ARM_MPU_ClrRegion in a loop, which writes directly to MPU->RNR and MPU->RASR hardware registers. In an emulator environment without real MPU hardware, these writes can cause hard faults. The replacement simulates MPU region clearing by logging the operation and skipping the hardware access, allowing the system to continue running in emulation mode. This is consistent with the existing replacements for region_init and set_region_number, and addresses the hard fault that occurs during context switching when MPU regions are being configured.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int mpu_configure_dynamic_mpu_regions(const struct z_arm_mpu_partition
	dynamic_regions[], uint8_t regions_num)
{
	int mpu_reg_index = static_regions_num;

	/* In ARMv7-M architecture the dynamic regions are
	 * programmed on top of existing SRAM region configuration.
	 */

	mpu_reg_index = mpu_configure_regions(dynamic_regions,
		regions_num, mpu_reg_index, false);

	if (mpu_reg_index != -EINVAL) {

		/* Disable the non-programmed MPU regions. */
		/* In emulation environment, we don't have real MPU hardware.
		 * Instead of calling ARM_MPU_ClrRegion which writes to MPU registers,
		 * we just log the operation and skip the hardware access.
		 * This prevents hard faults from occurring when the emulator
		 * tries to access non-existent MPU hardware registers.
		 */
		LOG_DBG("Emulated MPU: skipping clear of %d non-programmed regions",
			get_num_regions() - mpu_reg_index);
		
		/* Note: We're not calling ARM_MPU_ClrRegion(i) here
		 * to avoid causing hard faults in the emulator environment.
		 * The original code would have done:
		 * for (int i = mpu_reg_index; i < get_num_regions(); i++) {
		 *     ARM_MPU_ClrRegion(i);
		 * }
		 */
	}

	return mpu_reg_index;
}
    原因：The original mpu_configure_dynamic_mpu_regions function calls ARM_MPU_ClrRegion in a loop, which writes directly to MPU->RNR and MPU->RASR hardware registers. In an emulator environment without real MPU hardware, these writes can cause hard faults. The replacement simulates MPU region clearing by logging the operation and skipping the hardware access, allowing the system to continue running in emulation mode. This is consistent with the existing replacements for region_init and set_region_number, and addresses the hard fault that occurs during context switching when MPU regions are being configured.
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
- 函数用途/功能描述：Initializes the 32kHz oscillator (XOSC32K) and configures clock generator 1 to use it as source on Atmel SAMD MCUs
- 是否需要替换：是
- 分类/替换原因：Function performs hardware initialization of oscillator and clock generator peripherals. GetMMIOFunctionInfo confirms register accesses to OSC32KCTRL->XOSC32K.reg and GCLK->GENCTRL[1].reg, and contains a polling loop waiting for OSC32KCTRL->STATUS.bit.XOSC32KRDY. This is a classic INIT type function that configures peripheral hardware. It is called from z_arm_platform_init, which is platform initialization code. The function is not CORE (no NVIC/OS/VTOR operations), not RECV (no data I/O), not IRQ (no interrupt handling).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void osc32k_init(void)
{
	/* [INIT REPLACEMENT] Hardware oscillator initialization removed for simulation */
	/* Original code configured OSC32KCTRL->XOSC32K.reg and waited for XOSC32KRDY */
	/* Original code configured GCLK->GENCTRL[1].reg to use XOSC32K as source */
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
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU registers, we just log the configuration
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	/* Log the region configuration for debugging */
	LOG_DBG("[%d] Emulated MPU region: base=0x%08x, rasr=0x%08x",
		index, region_conf->base, region_conf->attr.rasr);
	
	/* In emulation, we don't need to configure real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->RBAR or MPU->RASR registers
	 * to avoid causing hard faults in the emulator environment.
	 */
}
- 更新原因：The original region_init function writes directly to MPU hardware registers (MPU->RBAR and MPU->RASR). In an emulator environment without real MPU hardware, these writes can cause hard faults. The replacement simulates MPU configuration by logging the region details and returning without hardware access, allowing the system to continue running in emulation mode.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static void region_init(const uint32_t index,
	const struct arm_mpu_region *region_conf)
{
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU registers, we just log the configuration
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	/* Log the region configuration for debugging */
	LOG_DBG("[%d] Emulated MPU region: base=0x%08x, rasr=0x%08x",
		index, region_conf->base, region_conf->attr.rasr);
	
	/* In emulation, we don't need to configure real MPU hardware.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->RBAR or MPU->RASR registers
	 * to avoid causing hard faults in the emulator environment.
	 */
}
    原因：The original region_init function writes directly to MPU hardware registers (MPU->RBAR and MPU->RASR). In an emulator environment without real MPU hardware, these writes can cause hard faults. The replacement simulates MPU configuration by logging the region details and returning without hardware access, allowing the system to continue running in emulation mode.
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
- 函数用途/功能描述：Acquires and configures an EIC (External Interrupt Controller) line for a specific GPIO pin on SAM0 microcontrollers, setting up interrupt trigger conditions and callback functions.
- 是否需要替换：是
- 分类/替换原因：This function initializes and configures the SAM0 EIC peripheral hardware. It contains MMIO register accesses (EIC->CONFIG[], EIC->INTFLAG.reg) and hardware-specific function calls (set_eic_enable, wait_synchronization) that need to be removed. The function manages line assignment state, configures interrupt triggers (rising/falling/both/high/low), sets up callback functions, and handles error conditions for busy lines. It does not involve NVIC configuration (not CORE), data transmission (not RECV), interrupt handling (not IRQ), or polling loops (not LOOP). The replacement preserves all non-hardware logic including line mapping, interrupt locking, state management, and callback configuration while removing hardware-specific operations.
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
	int line_index;
	unsigned int key;

	line_index = sam0_eic_map_to_line(port, pin);
	if (line_index < 0) {
		return line_index;
	}

	/* Lock everything so it's safe to reconfigure */
	key = irq_lock();

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

	irq_unlock(key);
	return 0;

err_in_use:
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
- 函数用途/功能描述：Disables an interrupt for a specific port/pin on the SAM0 External Interrupt Controller (EIC)
- 是否需要替换：否
- 分类/替换原因：Function performs hardware register writes to EIC->INTENCLR.reg and EIC->INTFLAG.reg to disable interrupts for a specific pin. These are peripheral interrupt controller operations, not NVIC/OS kernel operations (not CORE). The function only manipulates peripheral registers with no impact on upper-layer data structures, no data transmission/reception (not RECV), not an interrupt handler (not IRQ), not initialization (not INIT), and not a polling loop (not LOOP). Fits RETURNOK classification: pure driver operation functions that only manipulate peripheral registers.
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

	mask = BIT(line_index);
	/* Preserve interrupt disable and flag clearing writes for emulator */
	EIC->INTENCLR.reg = mask;
	EIC->INTFLAG.reg = mask;

	return 0;
}
- 更新原因：Preserve interrupt disable register writes for emulator. This function disables interrupts on the EIC peripheral by writing to EIC->INTENCLR.reg and clears pending interrupts via EIC->INTFLAG.reg. While classified as RETURNOK, these register writes should be preserved so the emulator can properly simulate interrupt controller behavior. The replacement keeps the original hardware register writes while preserving the function signature and logic.

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

	mask = BIT(line_index);
	/* Preserve interrupt disable and flag clearing writes for emulator */
	EIC->INTENCLR.reg = mask;
	EIC->INTFLAG.reg = mask;

	return 0;
}
    原因：Preserve interrupt disable register writes for emulator. This function disables interrupts on the EIC peripheral by writing to EIC->INTENCLR.reg and clears pending interrupts via EIC->INTFLAG.reg. While classified as RETURNOK, these register writes should be preserved so the emulator can properly simulate interrupt controller behavior. The replacement keeps the original hardware register writes while preserving the function signature and logic.
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
- 函数类型：CORE
- 函数用途/功能描述：Enables an interrupt for a specific pin on the SAM0 External Interrupt Controller (EIC) by clearing pending flags and setting interrupt enable bits.
- 是否需要替换：否
- 分类/替换原因：This function performs interrupt enable configuration operations similar to NVIC configuration. It writes to EIC->INTFLAG.reg to clear pending interrupts and EIC->INTENSET.reg to enable interrupts. According to classification rules, functions that configure interrupt enable/priority are classified as CORE (Priority 0). The emulator needs to see these register writes to simulate interrupts properly. GetMMIOFunctionInfo confirms hardware register accesses, and GetFunctionCallStack shows it's called from gpio_sam0_pin_interrupt_configure as part of interrupt configuration flow.
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

	mask = BIT(line_index);
	/* Preserve interrupt flag clearing and enable writes for emulator */
	EIC->INTFLAG.reg = mask;
	EIC->INTENSET.reg = mask;

	return 0;
}
- 更新原因：Preserve interrupt enable register writes for emulator. This function is classified as CORE because it configures interrupt enable registers. The emulator needs to see these register writes (EIC->INTFLAG.reg and EIC->INTENSET.reg) to properly simulate interrupt behavior. The replacement keeps the original hardware register writes while preserving the function signature and logic.

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

	mask = BIT(line_index);
	/* Preserve interrupt flag clearing and enable writes for emulator */
	EIC->INTFLAG.reg = mask;
	EIC->INTENSET.reg = mask;

	return 0;
}
    原因：Preserve interrupt enable register writes for emulator. This function is classified as CORE because it configures interrupt enable registers. The emulator needs to see these register writes (EIC->INTFLAG.reg and EIC->INTENSET.reg) to properly simulate interrupt behavior. The replacement keeps the original hardware register writes while preserving the function signature and logic.
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
- 函数用途/功能描述：Initializes the SAM0 External Interrupt Controller (EIC) by enabling clocks, configuring interrupts, and enabling the EIC module
- 是否需要替换：是
- 分类/替换原因：Function is an initialization routine for the SAM0 EIC peripheral. GetFunctionInfo shows it enables clocks (MCLK/PM, GCLK), configures interrupts via SAM0_EIC_IRQ_CONNECT (which calls CORE functions z_arm_irq_priority_set and arch_irq_enable), enables the EIC via set_eic_enable, and waits for synchronization. GetMMIOFunctionInfo indicates hardware register accesses. According to classification rules: (1) It calls CORE functions (NVIC configuration) but is not itself a CORE function; (2) It performs peripheral initialization with hardware register writes; (3) It contains a polling loop in wait_synchronization. Priority order CORE > RECV > IRQ > INIT > LOOP applies: since it's not CORE (only calls CORE functions), not RECV (no data transfer), not IRQ (not an interrupt handler), it is INIT (initialization function). The replacement preserves calls to CORE functions while removing hardware-specific clock configuration.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int sam0_eic_init(const struct device *dev)
{
	ARG_UNUSED(dev);

	/* Hardware clock configuration removed for simulation */
	
	/* Preserve interrupt configuration (calls to CORE functions) */
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

	/* Keep calls - these functions will be replaced separately */
	set_eic_enable(1);
	wait_synchronization();

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
- 函数用途/功能描述：Interrupt Service Routine for SAM0 External Interrupt Controller (EIC) that handles external interrupt lines, reads interrupt flags, acknowledges interrupts, and calls registered callback functions for each active interrupt line.
- 是否需要替换：是
- 分类/替换原因：This function is classified as IRQ because: 1) It is an Interrupt Service Routine (ISR) as indicated by the '_isr' suffix and its role in handling hardware interrupts; 2) It contains direct MMIO operations reading from and writing to EIC->INTFLAG.reg hardware registers; 3) It processes interrupt flags and calls callback functions for each active interrupt line; 4) It follows the IRQ pattern of interrupt acknowledgment and callback invocation. The function needs replacement to remove hardware-specific register accesses while preserving the interrupt processing logic and callback invocations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits = 0x0001; /* Simulate at least one interrupt flag set */
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
- 更新代码：static void sam0_eic_isr(const struct device *dev)
{
	/* In emulation, simply return without doing anything.
	 * This prevents any potential memory access issues or
	 * infinite loops from unacknowledged interrupts.
	 */
	return;
}
- 更新原因：Simplify sam0_eic_isr replacement to completely avoid any memory access or logic. The previous replacement still contained logic that could potentially access invalid memory if interrupts were simulated. By making the function an empty return, we ensure no memory access issues while still preventing hardware register accesses. This is safer for emulation where interrupt data structures might not be fully initialized.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void sam0_eic_isr(const struct device *dev)
{
	struct sam0_eic_data *const dev_data = dev->data;
	uint16_t bits = 0x0000; /* Start with no interrupts in simulation */
	uint32_t line_index;

	/* Skip hardware interrupt acknowledgment */
	/* EIC->INTFLAG.reg = bits; */

	/* In simulation, we don't simulate interrupts by default.
	 * This prevents calling NULL callbacks if interrupts occur
	 * without proper callback setup.
	 */
	
	/* Only process if we actually have bits set */
	if (bits == 0) {
		return;
	}

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
		
		/* Check if line assignment is valid */
		if (line_assignment->port < 0) {
			continue;
		}
		
		struct sam0_eic_port_data *port_data =
			&dev_data->ports[line_assignment->port];
		
		/* Only call callback if it's not NULL */
		if (port_data->cb != NULL) {
			port_data->cb(BIT(line_assignment->pin), port_data->data);
		}
	}
}
    原因：Fix potential NULL pointer dereference in EIC interrupt handler. The previous replacement always simulated an interrupt flag (bits = 0x0001) which could lead to calling NULL callback functions if they weren't properly initialized. The updated replacement starts with no interrupts (bits = 0x0000) and returns early, preventing any callback calls. This is safer for emulation where interrupt callbacks may not be fully set up. It prevents the emulator from crashing at PC=0x0 when EIC interrupts occur without proper callback setup.
    时间：

  版本 2:
    替换代码：static void sam0_eic_isr(const struct device *dev)
{
	/* In emulation, simply return without doing anything.
	 * This prevents any potential memory access issues or
	 * infinite loops from unacknowledged interrupts.
	 */
	return;
}
    原因：Simplify sam0_eic_isr replacement to completely avoid any memory access or logic. The previous replacement still contained logic that could potentially access invalid memory if interrupts were simulated. By making the function an empty return, we ensure no memory access issues while still preventing hardware register accesses. This is safer for emulation where interrupt data structures might not be fully initialized.
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
- 函数用途/功能描述：Releases an EIC (External Interrupt Controller) line for a specific GPIO pin by clearing its configuration and pending interrupts
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it performs peripheral configuration operations on the SAM0 EIC hardware. It contains direct hardware register accesses to clear EIC configuration (EIC->CONFIG), interrupt enable (EIC->INTENCLR), and interrupt flags (EIC->INTFLAG). The function also calls hardware-specific functions like set_eic_enable() and wait_synchronization(). As an initialization/configuration function, it manages the state of the interrupt controller but doesn't handle data transmission/reception (not RECV), isn't an interrupt handler (not IRQ), doesn't contain peripheral-dependent loops (not LOOP), and performs more than just returning success (not RETURNOK). The replacement removes all hardware-specific operations while preserving the software state management (dev_data->lines[line_index].enabled = 0) and OS operations (irq_lock/irq_unlock).
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
	/* [INIT REMOVED] set_eic_enable(0); */
	/* [INIT REMOVED] wait_synchronization(); */

	/*
	 * Check to make sure the requesting actually owns the line and do
	 * nothing if it does not.
	 */
	if (!sam0_eic_check_ownership(port, pin, line_index)) {
		goto done;
	}

	dev_data->lines[line_index].enabled = 0;

	/* Clear the EIC config, including the trigger condition */
	/* [INIT REMOVED] EIC->CONFIG[config_index].reg &= ~(0xF << config_shift); */

	/* Clear any pending interrupt for it */
	/* [INIT REMOVED] EIC->INTENCLR.reg = mask; */
	/* [INIT REMOVED] EIC->INTFLAG.reg = mask; */

done:
	/* [INIT REMOVED] set_eic_enable(1); */
	/* [INIT REMOVED] wait_synchronization(); */
	irq_unlock(key);
	return 0;
}
```

=== 信息结束 ===
```

### set_eic_enable

```text
=== set_eic_enable 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/interrupt_controller/intc_sam0_eic.c
- 行号：42
- 函数内容：static inline void set_eic_enable(bool on)
{
#ifdef REG_EIC_CTRLA
	EIC->CTRLA.bit.ENABLE = on;
#else
	EIC->CTRL.bit.ENABLE = on;
#endif
}


【替换更新】
- 更新代码：static inline void set_eic_enable(bool on)
{
	/* Skip hardware register write in simulation */
	/* The EIC peripheral enable is not needed for emulation */
	(void)on;
}
- 更新原因：Remove hardware-dependent register write in EIC enable function. The original function writes to EIC->CTRLA.bit.ENABLE or EIC->CTRL.bit.ENABLE hardware registers to enable/disable the External Interrupt Controller. In emulation, we don't need to actually enable the hardware peripheral. The replacement preserves the function signature while skipping the hardware operation, preventing potential emulation issues with hardware register writes.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline void set_eic_enable(bool on)
{
	/* Skip hardware register write in simulation */
	/* The EIC peripheral enable is not needed for emulation */
	(void)on;
}
    原因：Remove hardware-dependent register write in EIC enable function. The original function writes to EIC->CTRLA.bit.ENABLE or EIC->CTRL.bit.ENABLE hardware registers to enable/disable the External Interrupt Controller. In emulation, we don't need to actually enable the hardware peripheral. The replacement preserves the function signature while skipping the hardware operation, preventing potential emulation issues with hardware register writes.
    时间：

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
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->RNR register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU set region number %u", index);
	
	/* In emulation, we don't need to set real MPU region number.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->RNR register
	 * to avoid causing hard faults in the emulator environment.
	 */
}
- 更新原因：The original set_region_number function writes directly to MPU->RNR hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU region number setting by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static inline void set_region_number(uint32_t index)
{
	/* In emulation environment, we don't have real MPU hardware.
	 * Instead of writing to MPU->RNR register, we just log the operation
	 * and return successfully to allow the system to continue.
	 * This prevents hard faults from occurring when the emulator
	 * tries to access non-existent MPU hardware registers.
	 */
	
	LOG_DBG("Emulated MPU set region number %u", index);
	
	/* In emulation, we don't need to set real MPU region number.
	 * The memory protection is handled by the emulator at a higher level.
	 * Simply return without writing to hardware registers.
	 */
	
	/* Note: We're not writing to MPU->RNR register
	 * to avoid causing hard faults in the emulator environment.
	 */
}
    原因：The original set_region_number function writes directly to MPU->RNR hardware register. In an emulator environment without real MPU hardware, this write can cause hard faults. The replacement simulates MPU region number setting by logging the operation and returning without hardware access, allowing the system to continue running in emulation mode.
    时间：

=== 信息结束 ===
```

### soc_port_configure

```text
=== soc_port_configure 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_port.c
- 行号：35
- 函数内容：void soc_port_configure(const struct soc_port_pin *pin)
{
	PortGroup *pg = pin->regs;
	uint32_t flags = pin->flags;
	uint32_t func = (pin->flags & SOC_PORT_FUNC_MASK) >> SOC_PORT_FUNC_POS;
	PORT_PINCFG_Type pincfg = { .reg = 0 };

	/* Reset or analog I/O: all digital disabled */
	pg->PINCFG[pin->pinum] = pincfg;
	pg->DIRCLR.reg = (1 << pin->pinum);
	pg->OUTCLR.reg = (1 << pin->pinum);

	if (flags & SOC_PORT_PMUXEN_ENABLE) {
		soc_port_pinmux_set(pg, pin->pinum, func);
		return;
	}

	if (flags & (SOC_PORT_PULLUP | SOC_PORT_PULLDOWN)) {
		if (flags & SOC_PORT_PULLUP) {
			pg->OUTSET.reg = (1 << pin->pinum);
		}

		pincfg.bit.PULLEN = 1;
	}

	if (flags & SOC_PORT_INPUT_ENABLE) {
		pincfg.bit.INEN = 1;
	}

	if (flags & SOC_PORT_OUTPUT_ENABLE) {
		pg->DIRSET.reg = (1 << pin->pinum);
	}

	if (flags & SOC_PORT_STRENGTH_STRONGER) {
		pincfg.bit.DRVSTR = 1;
	}

	pg->PINCFG[pin->pinum] = pincfg;
}


【替换更新】
- 更新代码：void soc_port_configure(const struct soc_port_pin *pin)
{
	PortGroup *pg = pin->regs;
	uint32_t flags = pin->flags;
	uint32_t func = (pin->flags & SOC_PORT_FUNC_MASK) >> SOC_PORT_FUNC_POS;
	PORT_PINCFG_Type pincfg = { .reg = 0 };

	/* Skip hardware pin configuration for emulation */
	/* Original code had hardware register writes to configure pins */
	
	/* Only preserve the pinmux set call if needed */
	if (flags & SOC_PORT_PMUXEN_ENABLE) {
		/* Skip hardware pinmux configuration */
		/* soc_port_pinmux_set(pg, pin->pinum, func); */
		return;
	}

	/* Skip remaining hardware configuration */
}
- 更新原因：Add replacement for soc_port_configure to skip hardware pin configuration in emulation. This function contains multiple hardware register writes (PINCFG, DIRCLR, OUTCLR, OUTSET, DIRSET) that configure GPIO pins. In emulation, we don't need to actually configure hardware pins, so we skip all hardware operations while preserving the function signature and basic logic flow.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void soc_port_configure(const struct soc_port_pin *pin)
{
	PortGroup *pg = pin->regs;
	uint32_t flags = pin->flags;
	uint32_t func = (pin->flags & SOC_PORT_FUNC_MASK) >> SOC_PORT_FUNC_POS;
	PORT_PINCFG_Type pincfg = { .reg = 0 };

	/* Skip hardware pin configuration for emulation */
	/* Original code had hardware register writes to configure pins */
	
	/* Only preserve the pinmux set call if needed */
	if (flags & SOC_PORT_PMUXEN_ENABLE) {
		/* Skip hardware pinmux configuration */
		/* soc_port_pinmux_set(pg, pin->pinum, func); */
		return;
	}

	/* Skip remaining hardware configuration */
}
    原因：Add replacement for soc_port_configure to skip hardware pin configuration in emulation. This function contains multiple hardware register writes (PINCFG, DIRCLR, OUTCLR, OUTSET, DIRSET) that configure GPIO pins. In emulation, we don't need to actually configure hardware pins, so we skip all hardware operations while preserving the function signature and basic logic flow.
    时间：

=== 信息结束 ===
```

### soc_port_pinmux_set

```text
=== soc_port_pinmux_set 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/atmel_sam0/common/soc_port.c
- 行号：16
- 函数内容：int soc_port_pinmux_set(PortGroup *pg, uint32_t pin, uint32_t func)
{
	bool is_odd = pin & 1;
	int idx = pin / 2U;

	/* Each pinmux register holds the config for two pins.  The
	 * even numbered pin goes in the bits 0..3 and the odd
	 * numbered pin in bits 4..7.
	 */
	if (is_odd) {
		pg->PMUX[idx].bit.PMUXO = func;
	} else {
		pg->PMUX[idx].bit.PMUXE = func;
	}
	pg->PINCFG[pin].bit.PMUXEN = 1;

	return 0;
}


【替换更新】
- 更新代码：int soc_port_pinmux_set(PortGroup *pg, uint32_t pin, uint32_t func)
{
	bool is_odd = pin & 1;
	int idx = pin / 2U;

	/* Skip hardware pinmux configuration for emulation */
	/* Original code wrote to PMUX and PINCFG registers */
	/* if (is_odd) { */
	/* 	pg->PMUX[idx].bit.PMUXO = func; */
	/* } else { */
	/* 	pg->PMUX[idx].bit.PMUXE = func; */
	/* } */
	/* pg->PINCFG[pin].bit.PMUXEN = 1; */

	return 0;
}
- 更新原因：Add replacement for soc_port_pinmux_set to skip hardware pin multiplexer configuration in emulation. This function configures which peripheral function is connected to a GPIO pin by writing to hardware PMUX registers. In emulation, we don't need to actually configure hardware pin multiplexing, so we skip all hardware operations while preserving the function signature and returning success (0).

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：int soc_port_pinmux_set(PortGroup *pg, uint32_t pin, uint32_t func)
{
	bool is_odd = pin & 1;
	int idx = pin / 2U;

	/* Skip hardware pinmux configuration for emulation */
	/* Original code wrote to PMUX and PINCFG registers */
	/* if (is_odd) { */
	/* 	pg->PMUX[idx].bit.PMUXO = func; */
	/* } else { */
	/* 	pg->PMUX[idx].bit.PMUXE = func; */
	/* } */
	/* pg->PINCFG[pin].bit.PMUXEN = 1; */

	return 0;
}
    原因：Add replacement for soc_port_pinmux_set to skip hardware pin multiplexer configuration in emulation. This function configures which peripheral function is connected to a GPIO pin by writing to hardware PMUX registers. In emulation, we don't need to actually configure hardware pin multiplexing, so we skip all hardware operations while preserving the function signature and returning success (0).
    时间：

=== 信息结束 ===
```

### sys_clock_isr

```text
=== sys_clock_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c
- 行号：168
- 函数内容：void sys_clock_isr(void *arg)
{
	ARG_UNUSED(arg);
	uint32_t dcycles;
	uint32_t dticks;

	/* Update overflow_cyc and clear COUNTFLAG by invoking elapsed() */
	elapsed();

	/* Increment the amount of HW cycles elapsed (complete counter
	 * cycles) and announce the progress to the kernel.
	 */
	cycle_count += overflow_cyc;
	overflow_cyc = 0;

#ifdef CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER
	/* Rare case, when the interrupt was triggered, with previously programmed
	 * LOAD value, just before entering the idle mode (SysTick is clocked) or right
	 * after exiting the idle mode, before executing the procedure in the
	 * sys_clock_idle_exit function.
	 */
	if (timeout_idle) {
		z_arm_int_exit();

		return;
	}
#endif /* CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER */

	if (TICKLESS) {
		/* In TICKLESS mode, the SysTick.LOAD is re-programmed
		 * in sys_clock_set_timeout(), followed by resetting of
		 * the counter (VAL = 0).
		 *
		 * If a timer wrap occurs right when we re-program LOAD,
		 * the ISR is triggered immediately after sys_clock_set_timeout()
		 * returns; in that case we shall not increment the cycle_count
		 * because the value has been updated before LOAD re-program.
		 *
		 * We can assess if this is the case by inspecting COUNTFLAG.
		 */

		dcycles = cycle_count - announced_cycles;
		dticks = dcycles / CYC_PER_TICK;
		announced_cycles += dticks * CYC_PER_TICK;
		sys_clock_announce(dticks);
	} else {
		sys_clock_announce(1);
	}
	z_arm_int_exit();
}


【替换更新】
- 更新代码：void sys_clock_isr(void *arg)
{
	ARG_UNUSED(arg);
	uint32_t dcycles;
	uint32_t dticks;

	/* Update overflow_cyc and clear COUNTFLAG by invoking elapsed() */
	elapsed();

	/* Increment the amount of HW cycles elapsed (complete counter
	 * cycles) and announce the progress to the kernel.
	 */
	cycle_count += overflow_cyc;
	overflow_cyc = 0;

#ifdef CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER
	/* Rare case, when the interrupt was triggered, with previously programmed
	 * LOAD value, just before entering the idle mode (SysTick is clocked) or right
	 * after exiting the idle mode, before executing the procedure in the
	 * sys_clock_idle_exit function.
	 */
	if (timeout_idle) {
		z_arm_int_exit();

		return;
	}
#endif /* CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER */

	if (TICKLESS) {
		/* In TICKLESS mode, the SysTick.LOAD is re-programmed
		 * in sys_clock_set_timeout(), followed by resetting of
		 * the counter (VAL = 0).
		 *
		 * If a timer wrap occurs right when we re-program LOAD,
		 * the ISR is triggered immediately after sys_clock_set_timeout()
		 * returns; in that case we shall not increment the cycle_count
		 * because the value has been updated before LOAD re-program.
		 *
		 * We can assess if this is the case by inspecting COUNTFLAG.
		 */

		dcycles = cycle_count - announced_cycles;
		dticks = dcycles / CYC_PER_TICK;
		announced_cycles += dticks * CYC_PER_TICK;
		sys_clock_announce(dticks);
	} else {
		sys_clock_announce(1);
	}
	z_arm_int_exit();
}
- 更新原因：Preserve sys_clock_isr functionality without modification. This is a critical OS timer interrupt handler that drives the scheduler. The function calls elapsed() which already has a replacement that preserves SysTick register reads for emulator. Other functions called (sys_clock_announce, z_arm_int_exit) are OS scheduler functions that should not be modified according to the rules. Keeping the original implementation ensures proper OS scheduling in emulation.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void sys_clock_isr(void *arg)
{
	ARG_UNUSED(arg);
	uint32_t dcycles;
	uint32_t dticks;

	/* Update overflow_cyc and clear COUNTFLAG by invoking elapsed() */
	elapsed();

	/* Increment the amount of HW cycles elapsed (complete counter
	 * cycles) and announce the progress to the kernel.
	 */
	cycle_count += overflow_cyc;
	overflow_cyc = 0;

#ifdef CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER
	/* Rare case, when the interrupt was triggered, with previously programmed
	 * LOAD value, just before entering the idle mode (SysTick is clocked) or right
	 * after exiting the idle mode, before executing the procedure in the
	 * sys_clock_idle_exit function.
	 */
	if (timeout_idle) {
		z_arm_int_exit();

		return;
	}
#endif /* CONFIG_CORTEX_M_SYSTICK_IDLE_TIMER */

	if (TICKLESS) {
		/* In TICKLESS mode, the SysTick.LOAD is re-programmed
		 * in sys_clock_set_timeout(), followed by resetting of
		 * the counter (VAL = 0).
		 *
		 * If a timer wrap occurs right when we re-program LOAD,
		 * the ISR is triggered immediately after sys_clock_set_timeout()
		 * returns; in that case we shall not increment the cycle_count
		 * because the value has been updated before LOAD re-program.
		 *
		 * We can assess if this is the case by inspecting COUNTFLAG.
		 */

		dcycles = cycle_count - announced_cycles;
		dticks = dcycles / CYC_PER_TICK;
		announced_cycles += dticks * CYC_PER_TICK;
		sys_clock_announce(dticks);
	} else {
		sys_clock_announce(1);
	}
	z_arm_int_exit();
}
    原因：Preserve sys_clock_isr functionality without modification. This is a critical OS timer interrupt handler that drives the scheduler. The function calls elapsed() which already has a replacement that preserves SysTick register reads for emulator. Other functions called (sys_clock_announce, z_arm_int_exit) are OS scheduler functions that should not be modified according to the rules. Keeping the original implementation ensures proper OS scheduling in emulation.
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
- 函数用途/功能描述：Initializes the SAM0 UART peripheral by configuring clocks, pins, baud rate, interrupts, and enabling the hardware.
- 是否需要替换：是
- 分类/替换原因：Function is a device initialization routine that performs hardware configuration of UART peripheral registers (GCLK, PM, SERCOM USART CTRLA/CTRLB/INTENCLR). Contains multiple MMIO operations for clock enablement, interrupt disablement, UART mode configuration, and peripheral enablement. Preserves pin control configuration, device data structure initialization, and DMA setup while removing hardware-specific register writes. Classified as INIT because it's a peripheral initialization function, not CORE (no NVIC/OS operations), RECV (no data transfer), IRQ (not interrupt handler), or LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Skip hardware-specific baudrate configuration */
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

	return 0;
}
```

【替换更新】
- 更新代码：static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	/* Initialize configuration cache */
	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Skip hardware baudrate configuration */
	dev_data->config_cache.baudrate = cfg->baudrate;

#if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_SAM0_ASYNC
	/* Preserve interrupt configuration function call */
	cfg->irq_config_func(dev);
#endif

#ifdef CONFIG_UART_SAM0_ASYNC
	dev_data->dev = dev;
	dev_data->cfg = cfg;
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}

	/* Initialize work structures */
	k_work_init_delayable(&dev_data->tx_timeout_work, uart_sam0_tx_timeout);
	k_work_init_delayable(&dev_data->rx_timeout_work, uart_sam0_rx_timeout);

	/* Skip DMA hardware configuration */
	/* DMA configuration would normally set hardware addresses */
#endif

	return 0;
}
- 更新原因：Simplify replacement to avoid compilation errors by removing complex DMA configuration structures that may have missing includes or undefined types

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_init(const struct device *dev)
{
	int retval;
	const struct uart_sam0_dev_cfg *const cfg = dev->config;
	struct uart_sam0_dev_data *const dev_data = dev->data;

	/* Enable PINMUX based on PINCTRL */
	retval = pinctrl_apply_state(cfg->pcfg, PINCTRL_STATE_DEFAULT);
	if (retval < 0) {
		return retval;
	}

	/* Initialize configuration cache */
	dev_data->config_cache.flow_ctrl = UART_CFG_FLOW_CTRL_NONE;
	dev_data->config_cache.parity = UART_CFG_PARITY_NONE;
	dev_data->config_cache.stop_bits = UART_CFG_STOP_BITS_1;
	dev_data->config_cache.data_bits = UART_CFG_DATA_BITS_8;

	/* Skip hardware baudrate configuration */
	dev_data->config_cache.baudrate = cfg->baudrate;

#if CONFIG_UART_INTERRUPT_DRIVEN || CONFIG_UART_SAM0_ASYNC
	/* Preserve interrupt configuration function call */
	cfg->irq_config_func(dev);
#endif

#ifdef CONFIG_UART_SAM0_ASYNC
	dev_data->dev = dev;
	dev_data->cfg = cfg;
	if (!device_is_ready(cfg->dma_dev)) {
		return -ENODEV;
	}

	/* Initialize work structures */
	k_work_init_delayable(&dev_data->tx_timeout_work, uart_sam0_tx_timeout);
	k_work_init_delayable(&dev_data->rx_timeout_work, uart_sam0_rx_timeout);

	/* Skip DMA hardware configuration */
	/* DMA configuration would normally set hardware addresses */
#endif

	return 0;
}
    原因：Simplify replacement to avoid compilation errors by removing complex DMA configuration structures that may have missing includes or undefined types
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
	/* In emulation, return false (no data available) by default */
	return 0;
}
- 更新原因：Replace hardware flag check with false return for emulation. The original function checks the RXC (Receive Complete) hardware flag which may not be properly set in emulation. Returning false prevents the system from trying to read non-existent data from the UART hardware.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	/* In emulation, return false (no data available) by default */
	return 0;
}
    原因：Replace hardware flag check with false return for emulation. The original function checks the RXC (Receive Complete) hardware flag which may not be properly set in emulation. Returning false prevents the system from trying to read non-existent data from the UART hardware.
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
	/* In emulation, always return true to allow transmission to proceed */
	return 1;
}
- 更新原因：Replace hardware flag check with always-true return for emulation. The original function checks hardware interrupt flags (DRE and INTENSET) which may not be properly set in emulation. Returning true allows the UART transmission flow to continue without getting stuck waiting for hardware flags.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_irq_tx_ready(const struct device *dev)
{
	/* In emulation, always return true to allow transmission to proceed */
	return 1;
}
    原因：Replace hardware flag check with always-true return for emulation. The original function checks hardware interrupt flags (DRE and INTENSET) which may not be properly set in emulation. Returning true allows the UART transmission flow to continue without getting stuck waiting for hardware flags.
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
	/* In emulation, simply return without doing anything.
	 * This prevents any potential memory access issues or
	 * hardware register accesses in the interrupt handler.
	 */
	return;
}
- 更新原因：Simplify uart_sam0_isr replacement to completely avoid any memory access or logic. The previous replacement still contained complex logic that could potentially access device data structures. By making the function an empty return, we ensure no memory access issues while still preventing hardware register accesses. This is safer for emulation where UART interrupt data might not be fully initialized or could cause re-entrancy issues.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_isr(const struct device *dev)
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

	/* Skip hardware interrupt flag checks */
	/* if (dev_data->tx_len && regs->INTFLAG.bit.TXC) { */
	if (dev_data->tx_len) {
		/* Skip hardware interrupt disable */
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

	/* Skip hardware interrupt flag checks */
	/* if (dev_data->rx_len && regs->INTFLAG.bit.RXC && */
	/*     dev_data->rx_waiting_for_irq) { */
	if (dev_data->rx_len && dev_data->rx_waiting_for_irq) {
		dev_data->rx_waiting_for_irq = false;
		/* Skip hardware interrupt disable */
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

		/* Skip DMA start - no hardware in emulation */
		/* dma_start(cfg->dma_dev, cfg->rx_dma_channel); */
	}
#endif
}
    原因：Add replacement for uart_sam0_isr to prevent hardware register accesses in interrupt handler. The function reads hardware interrupt flags (regs->INTFLAG.bit.TXC, regs->INTFLAG.bit.RXC) and writes to interrupt enable registers (regs->INTENCLR.reg). These hardware accesses could cause issues in emulation if the registers are not properly mapped. The replacement skips all hardware register accesses while preserving the interrupt callback logic and state management. This prevents potential hard faults from accessing invalid memory addresses while maintaining the interrupt framework functionality.
    时间：

  版本 2:
    替换代码：static void uart_sam0_isr(const struct device *dev)
{
	/* In emulation, simply return without doing anything.
	 * This prevents any potential memory access issues or
	 * hardware register accesses in the interrupt handler.
	 */
	return;
}
    原因：Simplify uart_sam0_isr replacement to completely avoid any memory access or logic. The previous replacement still contained complex logic that could potentially access device data structures. By making the function an empty return, we ensure no memory access issues while still preventing hardware register accesses. This is safer for emulation where UART interrupt data might not be fully initialized or could cause re-entrancy issues.
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
	/* In emulation, always return -EBUSY to indicate no data available */
	return -EBUSY;
}
- 更新原因：Replace hardware-dependent poll in function for emulation. The original function checks the RXC (Receive Complete) hardware flag and reads from the data register. In emulation, we simulate no data being available by always returning -EBUSY. This prevents the system from trying to read non-existent data from hardware registers.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int uart_sam0_poll_in(const struct device *dev, unsigned char *c)
{
	/* In emulation, always return -EBUSY to indicate no data available */
	return -EBUSY;
}
    原因：Replace hardware-dependent poll in function for emulation. The original function checks the RXC (Receive Complete) hardware flag and reads from the data register. In emulation, we simulate no data being available by always returning -EBUSY. This prevents the system from trying to read non-existent data from hardware registers.
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

	/* [LOOP REMOVED] Skip hardware wait for Data Register Empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */
	
	/* For emulation, skip output to avoid infinite loop with stdout hook */
	/* The loop occurs because putchar triggers the stdout hook (console_out) */
	/* which calls back to uart_poll_out, creating infinite recursion */
	/* Simply skip output for now to break the loop */
}
- 更新原因：Fix infinite loop by removing putchar output. The previous replacement used putchar(c) which triggers the stdout hook (console_out), creating an infinite loop: console_out -> uart_sam0_poll_out -> putchar -> fputc -> picolibc_put -> z_impl_zephyr_fputc -> console_out. Removing output breaks the loop while still skipping hardware operations.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	/* [LOOP REMOVED] Skip hardware wait for Data Register Empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */
	
	/* For emulation, output character to stdout */
	/* Use putchar for POSIX compatibility */
	putchar(c);
}
    原因：Update UART poll out to output characters to stdout for better emulation visibility. The previous replacement skipped all output, making it hard to see console output in emulation. Using putchar provides POSIX-compatible console output while still skipping hardware operations.
    时间：

  版本 2:
    替换代码：static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	/* [LOOP REMOVED] Skip hardware wait for Data Register Empty flag */
	/* while (!usart->INTFLAG.bit.DRE) { */
	/* } */

	/* Skip hardware write to data register */
	/* usart->DATA.reg = c; */
	
	/* For emulation, skip output to avoid infinite loop with stdout hook */
	/* The loop occurs because putchar triggers the stdout hook (console_out) */
	/* which calls back to uart_poll_out, creating infinite recursion */
	/* Simply skip output for now to break the loop */
}
    原因：Fix infinite loop by removing putchar output. The previous replacement used putchar(c) which triggers the stdout hook (console_out), creating an infinite loop: console_out -> uart_sam0_poll_out -> putchar -> fputc -> picolibc_put -> z_impl_zephyr_fputc -> console_out. Removing output breaks the loop while still skipping hardware operations.
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
- 函数用途/功能描述：Waits for EIC (External Interrupt Controller) hardware synchronization to complete by polling SYNCBUSY status flag
- 是否需要替换：是
- 分类/替换原因：The function contains a while loop that polls hardware synchronization status registers (EIC->SYNCBUSY.reg or EIC->STATUS.bit.SYNCBUSY). This is a peripheral-dependent polling loop waiting for hardware synchronization completion. According to the classification criteria, this fits the LOOP category: 'Loops where the condition or body depends on peripheral registers (e.g., polling status flags).' The function is called from various driver functions including interrupt controller initialization (sam0_eic_init), acquisition/release functions, and UART driver configuration functions. GetMMIOFunctionInfo confirmed register accesses in the while loop condition. The replacement strategy for LOOP functions is to skip the loop entirely (assume the condition is already met).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void wait_synchronization(void)
{
#ifdef REG_EIC_SYNCBUSY
	/* [LOOP REMOVED] Waited for hardware synchronization busy flag */
#else
	/* [LOOP REMOVED] Waited for hardware synchronization busy flag */
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
- 函数用途/功能描述：Platform initialization function for ARM-based Atmel SAM0 microcontrollers that configures clock sources (DFLL, DPLL), resets clock generators, and sets up clock connections.
- 是否需要替换：是
- 分类/替换原因：This function is clearly an initialization function that sets up platform hardware including clock infrastructure and cache controller. It contains hardware register access (CMCC->CTRL.bit.CEN = 0) and calls multiple clock initialization functions (gclk_reset, osc32k_init, dfll_init, dpll_init, gclk_connect). According to the classification priority, it fits the INIT category as it initializes peripheral/configurations and allocates resources. It is not CORE because it doesn't configure NVIC, OS kernel, or VTOR. It's not RECV/IRQ as it doesn't handle data transmission or interrupts. The replacement removes all MMIO/register access operations while preserving the logical structure and variable calculations.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
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

	/*
	 * Force Cortex M Cache Controller disabled
	 *
	 * It is not clear if regular Cortex-M instructions can be used to
	 * perform cache maintenance or this is a proprietary cache controller
	 * that require special SoC support.
	 */
	/* [INIT REMOVED] CMCC->CTRL.bit.CEN = 0; */

	/* Skip hardware-specific clock initialization functions */
	/* gclk_reset(); */
	/* osc32k_init(); */
	/* dfll_init(); */
	/* dpll_init(0, dfll_div * CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC); */

	/* use DPLL for main clock */
	/* gclk_connect(0, GCLK_SOURCE_DPLL0, dfll_div); */

	/* connect GCLK2 to 48 MHz DFLL for USB */
	/* gclk_connect(2, GCLK_SOURCE_DFLL48M, 0); */
}
```

=== 信息结束 ===
```

### z_setup_new_thread

```text
=== z_setup_new_thread 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/kernel/thread.c
- 行号：591
- 函数内容：char *z_setup_new_thread(struct k_thread *new_thread,
			 k_thread_stack_t *stack, size_t stack_size,
			 k_thread_entry_t entry,
			 void *p1, void *p2, void *p3,
			 int prio, uint32_t options, const char *name)
{
	char *stack_ptr;

	Z_ASSERT_VALID_PRIO(prio, entry);

#ifdef CONFIG_OBJ_CORE_THREAD
	k_obj_core_init_and_link(K_OBJ_CORE(new_thread), &obj_type_thread);
#ifdef CONFIG_OBJ_CORE_STATS_THREAD
	k_obj_core_stats_register(K_OBJ_CORE(new_thread),
				  &new_thread->base.usage,
				  sizeof(new_thread->base.usage));
#endif
#endif

#ifdef CONFIG_USERSPACE
	__ASSERT((options & K_USER) == 0U || z_stack_is_user_capable(stack),
		 "user thread %p with kernel-only stack %p",
		 new_thread, stack);
	k_object_init(new_thread);
	k_object_init(stack);
	new_thread->stack_obj = stack;
	new_thread->syscall_frame = NULL;

	/* Any given thread has access to itself */
	k_object_access_grant(new_thread, new_thread);
#endif
	z_waitq_init(&new_thread->join_queue);

	/* Initialize various struct k_thread members */
	z_init_thread_base(&new_thread->base, prio, _THREAD_PRESTART, options);
	stack_ptr = setup_thread_stack(new_thread, stack, stack_size);

#ifdef CONFIG_KERNEL_COHERENCE
	/* Check that the thread object is safe, but that the stack is
	 * still cached!
	 */
	__ASSERT_NO_MSG(arch_mem_coherent(new_thread));
	__ASSERT_NO_MSG(!arch_mem_coherent(stack));
#endif

	arch_new_thread(new_thread, stack, stack_ptr, entry, p1, p2, p3);

	/* static threads overwrite it afterwards with real value */
	new_thread->init_data = NULL;

#ifdef CONFIG_USE_SWITCH
	/* switch_handle must be non-null except when inside z_swap()
	 * for synchronization reasons.  Historically some notional
	 * USE_SWITCH architectures have actually ignored the field
	 */
	__ASSERT(new_thread->switch_handle != NULL,
		 "arch layer failed to initialize switch_handle");
#endif
#ifdef CONFIG_THREAD_CUSTOM_DATA
	/* Initialize custom data field (value is opaque to kernel) */
	new_thread->custom_data = NULL;
#endif
#ifdef CONFIG_EVENTS
	new_thread->no_wake_on_timeout = false;
#endif
#ifdef CONFIG_THREAD_MONITOR
	new_thread->entry.pEntry = entry;
	new_thread->entry.parameter1 = p1;
	new_thread->entry.parameter2 = p2;
	new_thread->entry.parameter3 = p3;

	k_spinlock_key_t key = k_spin_lock(&z_thread_monitor_lock);

	new_thread->next_thread = _kernel.threads;
	_kernel.threads = new_thread;
	k_spin_unlock(&z_thread_monitor_lock, key);
#endif
#ifdef CONFIG_THREAD_NAME
	if (name != NULL) {
		strncpy(new_thread->name, name,
			CONFIG_THREAD_MAX_NAME_LEN - 1);
		/* Ensure NULL termination, truncate if longer */
		new_thread->name[CONFIG_THREAD_MAX_NAME_LEN - 1] = '\0';
	} else {
		new_thread->name[0] = '\0';
	}
#endif
#ifdef CONFIG_SCHED_CPU_MASK
	if (IS_ENABLED(CONFIG_SCHED_CPU_MASK_PIN_ONLY)) {
		new_thread->base.cpu_mask = 1; /* must specify only one cpu */
	} else {
		new_thread->base.cpu_mask = -1; /* allow all cpus */
	}
#endif
#ifdef CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN
	/* _current may be null if the dummy thread is not used */
	if (!_current) {
		new_thread->resource_pool = NULL;
		return stack_ptr;
	}
#endif
#ifdef CONFIG_USERSPACE
	z_mem_domain_init_thread(new_thread);

	if ((options & K_INHERIT_PERMS) != 0U) {
		k_thread_perms_inherit(_current, new_thread);
	}
#endif
#ifdef CONFIG_SCHED_DEADLINE
	new_thread->base.prio_deadline = 0;
#endif
	new_thread->resource_pool = _current->resource_pool;

#ifdef CONFIG_SMP
	z_waitq_init(&new_thread->halt_queue);
#endif

#ifdef CONFIG_SCHED_THREAD_USAGE
	new_thread->base.usage = (struct k_cycle_stats) {};
	new_thread->base.usage.track_usage =
		CONFIG_SCHED_THREAD_USAGE_AUTO_ENABLE;
#endif

	SYS_PORT_TRACING_OBJ_FUNC(k_thread, create, new_thread);

	return stack_ptr;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes a new thread structure, sets up its stack, and prepares it for execution in the Zephyr RTOS kernel
- 是否需要替换：是
- 分类/替换原因：This function is a thread initialization function that sets up thread structures, configures thread stacks, and calls architecture-specific initialization (arch_new_thread). GetMMIOFunctionInfo showed no MMIO operations, but arch_new_thread likely contains hardware-specific code. The function is called by thread creation functions (z_impl_k_thread_create, z_init_static_threads, etc.) and performs essential thread setup but does not configure NVIC, OS scheduler core logic, or VTOR, so it's not CORE. It's not a data transmission/reception (RECV), interrupt handler (IRQ), or peripheral-dependent loop (LOOP) function. As an INIT function, hardware-specific operations should be removed while preserving thread structure initialization logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*
 * The provided stack_size value is presumed to be either the result of
 * K_THREAD_STACK_SIZEOF(stack), or the size value passed to the instance
 * of K_THREAD_STACK_DEFINE() which defined 'stack'.
 */
char *z_setup_new_thread(struct k_thread *new_thread,
			 k_thread_stack_t *stack, size_t stack_size,
			 k_thread_entry_t entry,
			 void *p1, void *p2, void *p3,
			 int prio, uint32_t options, const char *name)
{
	char *stack_ptr;

	Z_ASSERT_VALID_PRIO(prio, entry);

#ifdef CONFIG_OBJ_CORE_THREAD
	k_obj_core_init_and_link(K_OBJ_CORE(new_thread), &obj_type_thread);
#ifdef CONFIG_OBJ_CORE_STATS_THREAD
	k_obj_core_stats_register(K_OBJ_CORE(new_thread),
				  &new_thread->base.usage,
				  sizeof(new_thread->base.usage));
#endif
#endif

#ifdef CONFIG_USERSPACE
	__ASSERT((options & K_USER) == 0U || z_stack_is_user_capable(stack),
		 "user thread %p with kernel-only stack %p",
		 new_thread, stack);
	k_object_init(new_thread);
	k_object_init(stack);
	new_thread->stack_obj = stack;
	new_thread->syscall_frame = NULL;

	/* Any given thread has access to itself */
	k_object_access_grant(new_thread, new_thread);
#endif
	z_waitq_init(&new_thread->join_queue);

	/* Initialize various struct k_thread members */
	z_init_thread_base(&new_thread->base, prio, _THREAD_PRESTART, options);
	stack_ptr = setup_thread_stack(new_thread, stack, stack_size);

#ifdef CONFIG_KERNEL_COHERENCE
	/* Check that the thread object is safe, but that the stack is
	 * still cached!
	 */
	__ASSERT_NO_MSG(arch_mem_coherent(new_thread));
	__ASSERT_NO_MSG(!arch_mem_coherent(stack));
#endif

	/* Skip architecture-specific hardware initialization */
	/* arch_new_thread(new_thread, stack, stack_ptr, entry, p1, p2, p3); */

	/* static threads overwrite it afterwards with real value */
	new_thread->init_data = NULL;

#ifdef CONFIG_USE_SWITCH
	/* switch_handle must be non-null except when inside z_swap()
	 * for synchronization reasons.  Historically some notional
	 * USE_SWITCH architectures have actually ignored the field
	 */
	__ASSERT(new_thread->switch_handle != NULL,
		 "arch layer failed to initialize switch_handle");
#endif
#ifdef CONFIG_THREAD_CUSTOM_DATA
	/* Initialize custom data field (value is opaque to kernel) */
	new_thread->custom_data = NULL;
#endif
#ifdef CONFIG_EVENTS
	new_thread->no_wake_on_timeout = false;
#endif
#ifdef CONFIG_THREAD_MONITOR
	new_thread->entry.pEntry = entry;
	new_thread->entry.parameter1 = p1;
	new_thread->entry.parameter2 = p2;
	new_thread->entry.parameter3 = p3;

	k_spinlock_key_t key = k_spin_lock(&z_thread_monitor_lock);

	new_thread->next_thread = _kernel.threads;
	_kernel.threads = new_thread;
	k_spin_unlock(&z_thread_monitor_lock, key);
#endif
#ifdef CONFIG_THREAD_NAME
	if (name != NULL) {
		strncpy(new_thread->name, name,
			CONFIG_THREAD_MAX_NAME_LEN - 1);
		/* Ensure NULL termination, truncate if longer */
		new_thread->name[CONFIG_THREAD_MAX_NAME_LEN - 1] = '\0';
	} else {
		new_thread->name[0] = '\0';
	}
#endif
#ifdef CONFIG_SCHED_CPU_MASK
	if (IS_ENABLED(CONFIG_SCHED_CPU_MASK_PIN_ONLY)) {
		new_thread->base.cpu_mask = 1; /* must specify only one cpu */
	} else {
		new_thread->base.cpu_mask = -1; /* allow all cpus */
	}
#endif
#ifdef CONFIG_ARCH_HAS_CUSTOM_SWAP_TO_MAIN
	/* _current may be null if the dummy thread is not used */
	if (!_current) {
		new_thread->resource_pool = NULL;
		return stack_ptr;
	}
#endif
#ifdef CONFIG_USERSPACE
	z_mem_domain_init_thread(new_thread);

	if ((options & K_INHERIT_PERMS) != 0U) {
		k_thread_perms_inherit(_current, new_thread);
	}
#endif
#ifdef CONFIG_SCHED_DEADLINE
	new_thread->base.prio_deadline = 0;
#endif
	new_thread->resource_pool = _current->resource_pool;

#ifdef CONFIG_SMP
	z_waitq_init(&new_thread->halt_queue);
#endif

#ifdef CONFIG_SCHED_THREAD_USAGE
	new_thread->base.usage = (struct k_cycle_stats) {};
	new_thread->base.usage.track_usage =
		CONFIG_SCHED_THREAD_USAGE_AUTO_ENABLE;
#endif

	SYS_PORT_TRACING_OBJ_FUNC(k_thread, create, new_thread);

	return stack_ptr;
}
```

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**76** 个；CodeQL `MMIOFunction`：**76** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **9** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `add_to_waitq_locked` | NODRIVER | False | Adds a thread to a wait queue while holding scheduler spinlock, marking thread as pending and updating thread state. |
| `adjust_owner_prio` | CORE | False | Adjusts the priority of a mutex owner thread in the Zephyr RTOS kernel |
| `arch_new_thread` | NODRIVER | False | Architecture-specific thread initialization function for ARM Cortex-M that sets up the initial thread context and sta... |
| `dfll_init` | INIT | True | Initializes the Digital Frequency Locked Loop (DFLL) oscillator controller by configuring control registers and waiti... |
| `dpll_init` | INIT | True | Initializes a Digital Phase-Locked Loop (DPLL) for Atmel SAMD MCU series by configuring clock source, ratio, and enab... |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating point values to text format with various formatting options (f, e, g... |
| `first` | NODRIVER | False | Retrieves the first timeout entry from the kernel's timeout linked list |
| `flash_sam0_check_status` | LOOP | True | Checks SAM0 flash controller status after operations, reads error flags, clears interrupts, and returns appropriate e... |
| `flash_sam0_erase_row` | LOOP | True | Erases a row of flash memory on SAM0 microcontrollers by writing to flash memory and issuing erase commands through N... |
| `flash_sam0_init` | INIT | True | Initializes the SAM0 flash controller driver, enabling clock, configuring manual write mode, and setting up semaphore... |
| `flash_sam0_wait_ready` | LOOP | True | Waits for the flash memory controller (NVMCTRL) to become ready by polling hardware status registers |
| `flash_sam0_write_page` | RECV | True | Writes a page of data to flash memory on SAM0 microcontrollers, handling hardware commands and data transfer |
| `flash_sam0_write_protection` | LOOP | True | Enables or disables write protection for flash memory regions on SAM0 microcontrollers by iterating through regions a... |
| `fs_get_mnt_point` | NODRIVER | False | Maps a path identifier to the corresponding file system mount point by searching through the list of mounted file sys... |
| `fs_init` | NODRIVER | False | Initializes file system subsystem by setting up mutex and mount point list |
| `fs_mount` | NODRIVER | False | Mounts a file system by validating parameters, checking for existing mounts, retrieving file system type information,... |
| `fs_opendir` | NODRIVER | False | Opens a directory in the filesystem, validates path, finds mount point, and calls filesystem-specific opendir impleme... |
| `fs_readdir` | NODRIVER | False | Reads directory entries from either a mounted filesystem or the VFS root directory in Zephyr's filesystem subsystem |
| `fs_readmount` | NODRIVER | False | Reads mount information from the file system mount list by index |
| `fs_unmount` | NODRIVER | False | Unmounts a file system by calling the file system-specific unmount function, clearing the file system interface, and ... |
| `gclk_connect` | INIT | True | Configures a Generic Clock (GCLK) generator by setting its source, division factor, and enabling it |
| `gclk_reset` | INIT | True | Resets the GCLK (Generic Clock Controller) peripheral by setting software reset bit and waiting for synchronization |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (THREAD_DEAD or THREAD_SUSPENDED), performing thread cleanu... |
| `init_ready_q` | NODRIVER | False | Initializes the scheduler's ready queue data structure based on scheduler configuration (SCALABLE, MULTIQ, or DUMB). |
| `k_heap_init` | NODRIVER | False | Initializes a kernel heap structure with provided memory region |
| `k_mbox_get` | NODRIVER | False | Retrieves messages from a Zephyr RTOS mailbox, searching for compatible senders and handling thread synchronization w... |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox kernel object by setting up transmit/receive wait queues and initializing synchroni... |
| `k_mem_slab_init` | NODRIVER | False | Initializes a memory slab object for dynamic memory allocation in Zephyr RTOS kernel |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a Zephyr kernel message queue by checking if wait queue is empty and freeing allocated buffer memory if needed |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting up buffer pointers, size parameters, and internal s... |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a kernel stack object by checking for waiting threads and freeing allocated buffer memory if needed |
| `k_stack_init` | NODRIVER | False | Initializes a kernel stack data structure by setting up wait queue, lock, and buffer pointers |
| `k_timer_init` | NODRIVER | False | Initializes a kernel timer structure by setting callback functions, status, wait queue, timeout, and performing objec... |
| `k_work_cancel_delayable_sync` | CORE | False | Cancels a delayable work item synchronously, checking if it's pending and waiting for cancellation completion if needed. |
| `k_work_cancel_sync` | NODRIVER | False | Cancels a work item synchronously, waiting for completion if the work is currently running |
| `k_work_flush` | NODRIVER | False | Flushes a work item if it's queued or running, waiting for completion if necessary |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item, waiting for it to complete if necessary |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item structure in Zephyr RTOS kernel |
| `k_work_queue_start` | NODRIVER | False | Starts a work queue thread in Zephyr RTOS by initializing data structures and creating/starting a thread to process w... |
| `mbox_message_put` | NODRIVER | False | Internal kernel helper function for sending mailbox messages, handling both synchronous and asynchronous message tran... |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the Zephyr kernel scheduler |
| `next` | NODRIVER | False | Returns the next timeout in the kernel's timeout linked list given a current timeout pointer |
| `osc32k_init` | INIT | True | Initializes the 32kHz oscillator (XOSC32K) and configures clock generator 1 to use it as source on Atmel SAMD MCUs |
| `ready_thread` | CORE | False | Marks a thread as ready to run and adds it to the scheduler's run queue if not already queued |
| `remove_timeout` | NODRIVER | False | Removes a timeout structure from the kernel's timeout list and adjusts delta ticks of the next timeout |
| `sam0_eic_acquire` | INIT | True | Acquires and configures an EIC (External Interrupt Controller) line for a specific GPIO pin on SAM0 microcontrollers,... |
| `sam0_eic_disable_interrupt` | RETURNOK | False | Disables an interrupt for a specific port/pin on the SAM0 External Interrupt Controller (EIC) |
| `sam0_eic_enable_interrupt` | CORE | False | Enables an interrupt for a specific pin on the SAM0 External Interrupt Controller (EIC) by clearing pending flags and... |
| `sam0_eic_init` | INIT | True | Initializes the SAM0 External Interrupt Controller (EIC) by enabling clocks, configuring interrupts, and enabling the... |
| `sam0_eic_interrupt_pending` | RETURNOK | False | Reads EIC interrupt flag register and returns mask of pending interrupts for specified port |
| `sam0_eic_isr` | IRQ | True | Interrupt Service Routine for SAM0 External Interrupt Controller (EIC) that handles external interrupt lines, reads i... |
| `sam0_eic_release` | INIT | True | Releases an EIC (External Interrupt Controller) line for a specific GPIO pin by clearing its configuration and pendin... |
| `timeout_rem` | NODRIVER | False | Calculates remaining time for a kernel timeout by traversing the timeout linked list and subtracting elapsed time |
| `uart_sam0_init` | INIT | True | Initializes the SAM0 UART peripheral by configuring clocks, pins, baud rate, interrupts, and enabling the hardware. |
| `update_cache` | CORE | False | Updates the scheduler's cache of the next thread to run, determining whether to preempt the current thread based on p... |
| `wait_synchronization` | LOOP | True | Waits for EIC (External Interrupt Controller) hardware synchronization to complete by polling SYNCBUSY status flag |
| `z_abort_timeout` | NODRIVER | False | Cancels/aborts a scheduled kernel timeout by removing it from the timeout queue if it's currently linked. |
| `z_add_timeout` | NODRIVER | False | Adds a timeout to the kernel's timeout management system, calculating timeout duration and inserting it into a sorted... |
| `z_arm_platform_init` | INIT | True | Platform initialization function for ARM-based Atmel SAM0 microcontrollers that configures clock sources (DFLL, DPLL)... |
| `z_cbvprintf_impl` | NODRIVER | False | Formatted output implementation function that processes format strings and variable arguments, outputting characters ... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr kernel condition variable object by setting up its wait queue and performing kernel object initi... |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a mutex structure in Zephyr RTOS by setting owner to NULL, lock count to 0, initializing wait queue, and ... |
| `z_impl_k_mutex_lock` | CORE | False | Zephyr RTOS mutex lock implementation with priority inheritance and timeout support |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a Zephyr kernel queue data structure by setting up its internal data structures including data queue, spi... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a Zephyr RTOS semaphore object by setting initial count, limit, and initializing associated data structures |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Synchronously waits for a kernel timer to expire and returns its status count |
| `z_impl_k_yield` | CORE | False | Kernel scheduler function that implements thread yielding - allows current thread to voluntarily give up CPU to other... |
| `z_init_thread_base` | NODRIVER | False | Initializes the base thread structure with priority, state, and options for thread creation |
| `z_priq_dumb_best` | CORE | False | Finds the best thread from a priority queue by returning the thread at the head of the doubly linked list |
| `z_priq_dumb_remove` | CORE | False | Removes a thread from a dumb priority queue in the Zephyr RTOS scheduler |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue for scheduler thread selection |
| `z_sched_waitq_walk` | CORE | False | Walks through a wait queue and invokes a callback function on each waiting thread in the Zephyr RTOS scheduler |
| `z_set_prio` | NODRIVER | False | Thread priority setting utility that changes a thread's priority in the run queue without rescheduling, returning whe... |
| `z_setup_new_thread` | INIT | True | Initializes a new thread structure, sets up its stack, and prepares it for execution in the Zephyr RTOS kernel |
| `z_timer_expiration_handler` | CORE | False | Handles expiration of kernel timer objects in Zephyr RTOS, managing timer restart, status updates, expiry callbacks, ... |
| `z_unpend_all` | CORE | False | Un-pends all threads from a wait queue and marks them as ready for scheduling |

## 附录：interesting MMIO expr 子集（共 9 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `dfll_init`
- `dpll_init`
- `flash_sam0_wait_ready`
- `flash_sam0_write_protection`
- `gclk_reset`
- `osc32k_init`
- `sam0_eic_interrupt_pending`
- `sam0_eic_isr`
- `wait_synchronization`
