# Case 07 - CLOCK_SetMux

## 背景

- Demo: `nxp/NXP_I2C_BareMetal`
- Function: `CLOCK_SetMux`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NODRIVER`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang + mmio/hw`

## 触发原因（ReplacementUpdate reason）

Remove hardware-dependent wait loop that causes emulation issues. Similar to CLOCK_SetDiv, this function writes to clock mux registers and waits for hardware handshake. In emulation, we remove the wait loop while keeping the register write operation.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/devices/RT/RT1050/MIMXRT1052/drivers/fsl_clock.h`
- 行号: `1377`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_SetMux_20260218192237.json`

### 原函数源码片段（定位到行号附近）

```c
 * @brief Set CCM MUX node to certain value.
 *
 * @param mux   Which mux node to set, see \ref clock_mux_t.
 * @param value Clock mux value to set, different mux has different value range.
 */
static inline void CLOCK_SetMux(clock_mux_t mux, uint32_t value)
{
    uint32_t busyShift;

    busyShift               = (uint32_t)CCM_TUPLE_BUSY_SHIFT(mux);
    CCM_TUPLE_REG(CCM, mux) = (CCM_TUPLE_REG(CCM, mux) & (~CCM_TUPLE_MASK(mux))) |
                              (((uint32_t)((value) << CCM_TUPLE_SHIFT(mux))) & CCM_TUPLE_MASK(mux));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
```

### ReplacementUpdate 代码片段（最新版本）

```c
static inline void CLOCK_SetMux(clock_mux_t mux, uint32_t value)
{
    uint32_t busyShift;

    busyShift               = (uint32_t)CCM_TUPLE_BUSY_SHIFT(mux);
    CCM_TUPLE_REG(CCM, mux) = (CCM_TUPLE_REG(CCM, mux) & (~CCM_TUPLE_MASK(mux))) |
                              (((uint32_t)((value) << CCM_TUPLE_SHIFT(mux))) & CCM_TUPLE_MASK(mux));

    assert(busyShift <= CCM_NO_BUSY_WAIT);

    /* Clock switch need Handshake? */
    if (CCM_NO_BUSY_WAIT != busyShift)
    {
        /* Wait until CCM internal handshake finish. */
        /* Remove hardware-dependent wait loop for emulation */
        /* while ((CCM->CDHIPR & ((1UL << busyShift))) != 0UL)
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
