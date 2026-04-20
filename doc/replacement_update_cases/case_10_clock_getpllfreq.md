# Case 10 - CLOCK_GetPllFreq

## 背景

- Demo: `nxp/NXP_UART_BareMetal`
- Function: `CLOCK_GetPllFreq`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=RETURNOK`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang + mmio/hw`

## 触发原因（ReplacementUpdate reason）

Fixing exceptional loop error in CLOCK_GetPllFreq. The function reads hardware registers (CCM_ANALOG->PLL_ARM, CCM_ANALOG->PLL_SYS, etc.) to calculate PLL frequencies. In emulation, these registers have unpredictable values which could cause infinite loops or incorrect calculations. The replacement returns reasonable default frequencies for each PLL type without reading hardware registers, preserving the original function signature and return type.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/devices/RT/RT1050/MIMXRT1052/drivers/fsl_clock.c`
- 行号: `939`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_NXP_UART_BareMetal/lcmhal_ai_log/replacement_update_CLOCK_GetPllFreq_20260223155704.json`

### 原函数源码片段（定位到行号附近）

```c
/*!
 * brief Get current PLL output frequency.
 */
uint32_t CLOCK_GetPllFreq(clock_pll_t pll)
{
    uint32_t freq;
    uint32_t divSelect;
    clock_64b_t freqTmp;
    /* check if PLL is enabled */
    if (!CLOCK_IsPllEnabled(CCM_ANALOG, pll))
    {
        return 0U;
    }
    /* get pll reference clock */
    freq = CLOCK_GetPllBypassRefClk(CCM_ANALOG, pll);
    // ... source omitted ...
}
```

### ReplacementUpdate 代码片段（最新版本）

```c
uint32_t CLOCK_GetPllFreq(clock_pll_t pll)
{
    /* For emulation, return reasonable default frequencies for each PLL type */
    /* This avoids reading hardware registers that would have unpredictable values in emulation */
    
    switch (pll)
    {
        case kCLOCK_PllArm:
            /* Typical ARM PLL frequency for RT1050 */
            return 528000000U; /* 528 MHz */
            
        case kCLOCK_PllSys:
            /* Typical System PLL frequency */
            return 528000000U; /* 528 MHz */
            
        case kCLOCK_PllUsb1:
            /* USB1 PLL frequency */
            return 480000000U; /* 480 MHz */
            
        case kCLOCK_PllAudio:
            /* Audio PLL frequency */
            return 196608000U; /* 196.608 MHz */
            
        case kCLOCK_PllVideo:
            /* Video PLL frequency */
            return 594000000U; /* 594 MHz */
// ... truncated ...
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `loop/hang + mmio/hw` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
