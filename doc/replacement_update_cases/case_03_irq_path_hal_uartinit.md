# Case 03 - IRQ Path: `HAL_UartInit`

## 背景

- Demo: `nxp/NXP_FATFS_FreeRTOS`
- Function: `HAL_UartInit`
- 分类状态（触发 RU 时）:
  - `function_type=NA`
  - `has_replacement=false`
  - `in_baseline=false`
- 归类: `A_RU_only_not_replaced`

## 触发问题

UART 初始化过程既包含硬件寄存器初始化，也涉及中断相关配置。若简单全部 stub，可能让仿真丢失必要 IRQ 行为；若完全保留硬件逻辑，又会引入寄存器访问风险。

## ReplacementUpdate 动作

- 保留对仿真必要的中断相关路径（如 NVIC 使能语义）
- 移除/弱化硬件专有 UART 初始化细节，避免仿真访问真实硬件寄存器

## 结果意义

- 这是“中断路径 + MMIO隔离”的混合修复
- 表明 RU 不仅是“删循环”，还会做“保留关键行为、删除硬件依赖”的平衡替换

## 证据

- `replacement_update` 日志：`/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_HAL_UartInit_20260406203820.json`
- 关键 reason 摘要：
  - “...preserves NVIC interrupt enabling ... while removing hardware-specific UART initialization ...”
