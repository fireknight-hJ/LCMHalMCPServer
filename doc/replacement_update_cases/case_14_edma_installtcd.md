# Case 14 - EDMA_InstallTCD

## 背景

- Demo: `rtthread/imxrt1052-nxp-evk/uart`
- Function: `EDMA_InstallTCD`
- 归类: `C_already_replaced_refined`
- 分类状态: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- 关注问题: `restore`

## 触发原因（ReplacementUpdate reason）

Restoring original function implementation to fix verification failure. The previous replacement had comments about skipping hardware writes which may have caused verification issues.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/drivers/edma4/fsl_edma.c`
- 行号: `121`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_InstallTCD_20260407041149.json`

### 原函数源码片段（定位到行号附近）

```c
*
 * param base EDMA peripheral base address.
 * param channel EDMA channel number.
 * param tcd Point to TCD structure.
 */
void EDMA_InstallTCD(EDMA_Type *base, uint32_t channel, edma_tcd_t *tcd)
{
    assert(channel < (uint32_t)FSL_FEATURE_EDMA_INSTANCE_CHANNELn(base));
    assert(tcd != NULL);

    edma_tcd_t *tcdRegs = EDMA_TCD_BASE(base, channel);
    /* Avoiding misra_c_2012_rule_13_5_violation event */
    status_t errataStatus = EDMA_CheckErrata(base, tcd);
    uint32_t esgStatus = EDMA_TCD_CSR(tcd, EDMA_TCD_TYPE(base)) & (uint16_t)DMA_CSR_ESG_MASK;

#if defined FSL_FEATURE_EDMA_HAS_ERRATA_51327
    if ((EDMA_TCD_DLAST_SGA(tcd, EDMA_TCD_TYPE(base)) != 0U) && ((esgStatus) != 0U) &&
        (errataStatus != kStatus_Success))
```

### ReplacementUpdate 代码片段（最新版本）

```c
void EDMA_InstallTCD(DMA_Type *base, uint32_t channel, edma_tcd_t *tcd)
{
    assert(channel < FSL_FEATURE_EDMA_MODULE_CHANNEL);
    assert(tcd != NULL);
    assert(((uint32_t)tcd & 0x1FU) == 0);

    /* Push tcd into hardware TCD register */
    base->TCD[channel].SADDR = tcd->SADDR;
    base->TCD[channel].SOFF = tcd->SOFF;
    base->TCD[channel].ATTR = tcd->ATTR;
    base->TCD[channel].NBYTES_MLNO = tcd->NBYTES;
    base->TCD[channel].SLAST = tcd->SLAST;
    base->TCD[channel].DADDR = tcd->DADDR;
    base->TCD[channel].DOFF = tcd->DOFF;
    base->TCD[channel].CITER_ELINKNO = tcd->CITER;
    base->TCD[channel].DLAST_SGA = tcd->DLAST_SGA;
    /* Clear DONE bit first, otherwise ESG cannot be set */
    base->TCD[channel].CSR = 0;
    base->TCD[channel].CSR = tcd->CSR;
    base->TCD[channel].BITER_ELINKNO = tcd->BITER;
}
```

## 替换历史（首版 vs 最新版）

- 历史条目数: **1**
- 首次替换日志: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_InstallTCD_20260407041149.json`
- 最新替换日志: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_InstallTCD_20260407041149.json`

### 时间线

- 1. `unknown_ts` - `replacement_update_EDMA_InstallTCD_20260407041149.json`\n   - reason: Restoring original function implementation to fix verification failure. The previous replacement had comments about skipping hardware writes which may have caused verification issues.

### 首次替换代码片段

```c
void EDMA_InstallTCD(DMA_Type *base, uint32_t channel, edma_tcd_t *tcd)
{
    assert(channel < FSL_FEATURE_EDMA_MODULE_CHANNEL);
    assert(tcd != NULL);
    assert(((uint32_t)tcd & 0x1FU) == 0);

    /* Push tcd into hardware TCD register */
    base->TCD[channel].SADDR = tcd->SADDR;
    base->TCD[channel].SOFF = tcd->SOFF;
    base->TCD[channel].ATTR = tcd->ATTR;
    base->TCD[channel].NBYTES_MLNO = tcd->NBYTES;
    base->TCD[channel].SLAST = tcd->SLAST;
    base->TCD[channel].DADDR = tcd->DADDR;
    base->TCD[channel].DOFF = tcd->DOFF;
    base->TCD[channel].CITER_ELINKNO = tcd->CITER;
    base->TCD[channel].DLAST_SGA = tcd->DLAST_SGA;
    /* Clear DONE bit first, otherwise ESG cannot be set */
    base->TCD[channel].CSR = 0;
    base->TCD[channel].CSR = tcd->CSR;
    base->TCD[channel].BITER_ELINKNO = tcd->BITER;
}
```

### 最新替换代码片段

```c
void EDMA_InstallTCD(DMA_Type *base, uint32_t channel, edma_tcd_t *tcd)
{
    assert(channel < FSL_FEATURE_EDMA_MODULE_CHANNEL);
    assert(tcd != NULL);
    assert(((uint32_t)tcd & 0x1FU) == 0);

    /* Push tcd into hardware TCD register */
    base->TCD[channel].SADDR = tcd->SADDR;
    base->TCD[channel].SOFF = tcd->SOFF;
    base->TCD[channel].ATTR = tcd->ATTR;
    base->TCD[channel].NBYTES_MLNO = tcd->NBYTES;
    base->TCD[channel].SLAST = tcd->SLAST;
    base->TCD[channel].DADDR = tcd->DADDR;
    base->TCD[channel].DOFF = tcd->DOFF;
    base->TCD[channel].CITER_ELINKNO = tcd->CITER;
    base->TCD[channel].DLAST_SGA = tcd->DLAST_SGA;
    /* Clear DONE bit first, otherwise ESG cannot be set */
    base->TCD[channel].CSR = 0;
    base->TCD[channel].CSR = tcd->CSR;
    base->TCD[channel].BITER_ELINKNO = tcd->BITER;
}
```

### 变化要点

- 首版通常优先“先跑通”（快速规避硬件依赖/异常路径）。
- 最新版通常修复编译验证问题、补全签名一致性或回退过激替换。

## 前因后果解读

- 前因: 该函数在仿真中触发了 `restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的质量增量贡献，可用于论文中的定性论证。
