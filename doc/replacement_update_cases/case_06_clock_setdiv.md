# Case 06 - CLOCK_SetDiv

## 背景

- Demo: `nxp/NXP_I2C_BareMetal`
- Function: `CLOCK_SetDiv`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NODRIVER`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang + mmio/hw`

## 触发原因（ReplacementUpdate reason）

Remove hardware-dependent wait loop that causes emulation issues. The function writes to clock divider registers and then waits for hardware handshake completion. In emulation, we can't wait for hardware signals, so we remove the wait loop while preserving the register write operation.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/devices/RT/RT1050/MIMXRT1052/drivers/fsl_clock.h`
- 行号: `1429`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SetDiv_20260218192229.json`

### 原函数源码片段（定位到行号附近）

```c
 * @param divider Which divider node to set.
 * @param value   Clock div value to set, different divider has different value range. See @ref clock_div_value_t
 *                for details.
 *                Divided clock frequency = Undivided clock frequency / (value + 1)
 */
static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift                   = CCM_TUPLE_BUSY_SHIFT(divider);
    CCM_TUPLE_REG(CCM, divider) = (CCM_TUPLE_REG(CCM, divider) & (~CCM_TUPLE_MASK(divider))) |
                                  (((uint32_t)((value) << CCM_TUPLE_SHIFT(divider))) & CCM_TUPLE_MASK(divider));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
```

### ReplacementUpdate 代码片段（最新版本）

```c
static inline void CLOCK_SetDiv(clock_div_t divider, uint32_t value)
{
    uint32_t busyShift;

    busyShift                   = CCM_TUPLE_BUSY_SHIFT(divider);
    CCM_TUPLE_REG(CCM, divider) = (CCM_TUPLE_REG(CCM, divider) & (~CCM_TUPLE_MASK(divider))) |
                                  (((uint32_t)((value) << CCM_TUPLE_SHIFT(divider))) & CCM_TUPLE_MASK(divider));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* Wait until CCM internal handshake finish. */
        /* Remove hardware-dependent wait loop for emulation */
        /* while ((CCM->CDHIPR & ((uint32_t)(1UL << busyShift))) != 0UL)
        {
        } */
        /* Simply return without waiting for hardware */
    }
}
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `loop/hang + mmio/hw` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
