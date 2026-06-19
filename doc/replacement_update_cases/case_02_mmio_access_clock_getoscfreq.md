# Case 02 - MMIO Access: `CLOCK_GetOscFreq`

## 背景

- Demo: `nxp/NXP_UART_BareMetal`
- Function: `CLOCK_GetOscFreq`
- 分类状态（触发 RU 时）:
  - `function_type=NA`
  - `has_replacement=false`
  - `in_baseline=false`
- 归类: `A_RU_only_not_replaced`

## 触发问题

原函数直接读取硬件寄存器（例如时钟相关寄存器）。在仿真环境里这些寄存器值可能不可靠，导致后续时钟分支判断异常。

## ReplacementUpdate 动作

- 将硬件寄存器读替换为仿真可用的稳定返回值（如默认时钟频率）
- 保持函数签名和调用接口不变

## 结果意义

- 这是“MMIO/硬件访问不兼容”驱动的替换，不是死循环场景
- 通过隔离硬件读，减少不确定分支和仿真偏差

## 证据

- `replacement_update` 日志：`/home/haojie/workspace/dbs_server/DATABASE_NXP_UART_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetOscFreq_20260223155713.json`
- 关键 reason 摘要：
  - “...reads hardware register ... unpredictable values in emulation ... returns default 24MHz ...”
