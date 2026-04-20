# Case 29 - sys_clock_isr

## 背景

- Demo: `zephyr/atmel/fs_littlefs_atsame54`
- Function: `sys_clock_isr`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `mmio/hw,irq,boot-critical,restore`

## 触发原因（ReplacementUpdate reason）

Preserve sys_clock_isr functionality without modification. This is a critical OS timer interrupt handler that drives the scheduler. The function calls elapsed() which already has a replacement that preserves SysTick register reads for emulator. Other functions called (sys_clock_announce, z_arm_int_exit) are OS scheduler functions that should not be modified according to the rules. Keeping the original implementation ensures proper OS scheduling in emulation.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/zephyrproject/zephyr/drivers/timer/cortex_m_systick.c`
- 行号: `168`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_Zephyr_atmel_fs_littlefs_atsame54/lcmhal_ai_log/replacement_update_sys_clock_isr_20260406202258.json`

### 原函数源码片段（定位到行号附近）

```c

	return (last_load - val2) + overflow_cyc;
}

/* Callout out of platform assembly, not hooked via IRQ_CONNECT... */
void sys_clock_isr(void *arg)
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
```

### ReplacementUpdate 代码片段（最新版本）

```c
void sys_clock_isr(void *arg)
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
// ... truncated ...
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `mmio/hw,irq,boot-critical,restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
