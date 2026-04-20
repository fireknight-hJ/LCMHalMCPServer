# Case 04 - Boot Critical: `SystemInit`

## 背景

- Demo: `nxp/NXP_FATFS_BareMetal`
- Function: `SystemInit`
- 分类状态（触发 RU 时）:
  - `function_type=CORE`
  - `has_replacement=false`
  - `in_baseline=false`
- 归类: `A_RU_only_not_replaced`

## 触发问题

`SystemInit` 属于启动关键路径，涉及向量表/时钟/SysTick 等关键初始化。过度替换会破坏引导流程，替换不足又可能残留硬件依赖。

## ReplacementUpdate 动作

- 修正替换策略，保留仿真中必须可见的关键初始化语义（例如与 SysTick/VTOR 相关行为）
- 删除或收敛会导致硬件依赖的问题片段

## 结果意义

- 这是“启动关键路径”专门场景
- RU 在此类函数上承担“正确性保护”角色，而不只是覆盖扩展

## 证据

- `replacement_update` 日志：`/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal/lcmhal_ai_log/replacement_update_SystemInit_20260317174728.json`
- 关键 reason 摘要：
  - “...preserve SysTick disable operation as required by CRITICAL rules ...”
