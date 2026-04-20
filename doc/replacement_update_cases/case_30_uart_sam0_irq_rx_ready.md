# Case 30 - uart_sam0_irq_rx_ready

## 背景

- Demo: `zephyr/atmel/fs_littlefs_atsame54`
- Function: `uart_sam0_irq_rx_ready`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `restore`

## 触发原因（ReplacementUpdate reason）

Replace hardware flag check with false return for emulation. The original function checks the RXC (Receive Complete) hardware flag which may not be properly set in emulation. Returning false prevents the system from trying to read non-existent data from the UART hardware.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/zephyrproject/zephyr/drivers/serial/uart_sam0.c`
- 行号: `850`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_Zephyr_atmel_fs_littlefs_atsame54/lcmhal_ai_log/replacement_update_uart_sam0_irq_rx_ready_20260406194346.json`

### 原函数源码片段（定位到行号附近）

```c
	SercomUsart * const regs = config->regs;

	regs->INTENCLR.reg = SERCOM_USART_INTENCLR_RXC;
}

static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;

	return regs->INTFLAG.bit.RXC != 0;
}

static int uart_sam0_fifo_read(const struct device *dev, uint8_t *rx_data,
			       const int size)
{
	const struct uart_sam0_dev_cfg *config = dev->config;
	SercomUsart * const regs = config->regs;
```

### ReplacementUpdate 代码片段（最新版本）

```c
static int uart_sam0_irq_rx_ready(const struct device *dev)
{
	/* In emulation, return false (no data available) by default */
	return 0;
}
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
