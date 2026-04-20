# Case 25 - uart_sam0_poll_out

## 背景

- Demo: `zephyr/atmel/fs_littlefs_atsame54`
- Function: `uart_sam0_poll_out`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang`

## 触发原因（ReplacementUpdate reason）

Fix infinite loop by removing putchar output. The previous replacement used putchar(c) which triggers the stdout hook (console_out), creating an infinite loop: console_out -> uart_sam0_poll_out -> putchar -> fputc -> picolibc_put -> z_impl_zephyr_fputc -> console_out. Removing output breaks the loop while still skipping hardware operations.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c`
- 行号: `653`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_Zephyr_atmel_fs_littlefs_atsame54/lcmhal_ai_log/replacement_update_uart_sam0_poll_out_20260406202524.json`

### 原函数源码片段（定位到行号附近）

```c

	*c = (unsigned char)usart->DATA.reg;
	return 0;
}

static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
{
	const struct uart_sam0_dev_cfg *config = dev->config;

	SercomUsart * const usart = config->regs;

	while (!usart->INTFLAG.bit.DRE) {
	}

	/* send a character */
	usart->DATA.reg = c;
}

```

### ReplacementUpdate 代码片段（最新版本）

```c
static void uart_sam0_poll_out(const struct device *dev, unsigned char c)
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
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `loop/hang` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
