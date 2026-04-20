# Case 28 - sam0_eic_disable_interrupt

## 背景

- Demo: `zephyr/atmel/fs_littlefs_atsame54`
- Function: `sam0_eic_disable_interrupt`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=RETURNOK`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `mmio/hw,irq,restore`

## 触发原因（ReplacementUpdate reason）

Preserve interrupt disable register writes for emulator. This function disables interrupts on the EIC peripheral by writing to EIC->INTENCLR.reg and clears pending interrupts via EIC->INTFLAG.reg. While classified as RETURNOK, these register writes should be preserved so the emulator can properly simulate interrupt controller behavior. The replacement keeps the original hardware register writes while preserving the function signature and logic.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/zephyrproject/zephyr/include/zephyr/drivers/interrupt_controller/sam0_eic.h`
- 行号: `76`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_Zephyr_atmel_fs_littlefs_atsame54/lcmhal_ai_log/replacement_update_sam0_eic_disable_interrupt_20260406195239.json`

### 原函数源码片段（定位到行号附近）

```c
 * @brief Disable the EIC interrupt for a specific port and pin combination
 *
 * @param port port index (A=0, etc)
 * @param pin pin in the port
 */
int sam0_eic_disable_interrupt(int port, int pin);

/**
 * @brief Test if there is an EIC interrupt pending for a port
 *
 * @param port port index (A=0, etc)
 */
uint32_t sam0_eic_interrupt_pending(int port);

#endif /* ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_SAM0_EIC_H_ */
```

### ReplacementUpdate 代码片段（最新版本）

```c
int sam0_eic_disable_interrupt(int port, int pin)
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
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `mmio/hw,irq,restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
