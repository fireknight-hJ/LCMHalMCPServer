# Case 20 - EDMA_SubmitTransfer

## 背景

- Demo: `rtthread/imxrt1052-nxp-evk/uart`
- Function: `EDMA_SubmitTransfer`
- 归类: `C_already_replaced_refined`
- 分类状态: `function_type=RETURNOK`, `has_replacement=True`, `in_baseline=True`
- 关注问题: `compile,restore`

## 触发原因（ReplacementUpdate reason）

Restoring original function to fix compilation warnings and ensure proper functionality

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/drivers/edma4/fsl_edma.c`
- 行号: `2136`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_SubmitTransfer_20260407041638.json`

### 原函数源码片段（定位到行号附近）

```c
/*!
 * brief Submits the eDMA transfer request.
 *
 * This function submits the eDMA transfer request according to the transfer configuration structure.
 * In scatter gather mode, call this function will add a configured tcd to the circular list of tcd pool.
 * The tcd pools is setup by call function EDMA_InstallTCDMemory before.
 *
 * param handle eDMA handle pointer.
 * param config Pointer to eDMA transfer configuration structure.
 * retval kStatus_EDMA_Success It means submit transfer request succeed.
 * retval kStatus_EDMA_QueueFull It means TCD queue is full. Submit transfer request is not allowed.
 * retval kStatus_EDMA_Busy It means the given channel is busy, need to submit request later.
 */
status_t EDMA_SubmitTransfer(edma_handle_t *handle, const edma_transfer_config_t *config)
{
    assert(handle != NULL);
    assert(config != NULL);
    assert(handle->tcdBase != NULL);
#if (defined(FSL_FEATURE_EDMA_SUPPORT_128_BYTES_TRANSFER) && FSL_FEATURE_EDMA_SUPPORT_128_BYTES_TRANSFER)
    assert(((config->srcTransferSize != kEDMA_TransferSize128Bytes) &&
            (config->destTransferSize != kEDMA_TransferSize128Bytes)) ||
           (FSL_FEATURE_EDMA_INSTANCE_SUPPORT_128_BYTES_TRANSFERn(handle->base) == 1));
#endif
    edma_tcd_t *tcdRegs = handle->tcdBase;

    if (handle->tcdPool == NULL)
    {
        /* Avoiding misra_c_2012_rule_13_5_violation event */
        uint16_t citerStatus = EDMA_TCD_CITER(tcdRegs, EDMA_TCD_TYPE(handle->base)) & DMA_CITER_ELINKNO_CITER_MASK;
        uint16_t biterStatus = EDMA_TCD_BITER(tcdRegs, EDMA_TCD_TYPE(handle->base)) & DMA_BITER_ELINKNO_BITER_MASK;
        /*
         *    Check if EDMA channel is busy:
         *    1. if channel active bit is set, it implies that minor loop is executing, then channel is busy
         *    2. if channel active bit is not set and BITER not equal to CITER, it implies that major loop is executing,
         * then channel is busy
         *
         *    There is one case can not be covered in below condition:
         *    When transfer request is submitted, but no request from peripheral, that is to say channel sevice doesn't
         *    begin, if application would like to submit another transfer , then the TCD will be overwritten, since the
         *    ACTIVE is 0 and BITER = CITER, for such case, it is a scatter gather(link TCD) case actually, so
         *    application should enabled TCD pool for dynamic scatter gather mode by calling EDMA_InstallTCDMemory.
         */
#if defined FSL_EDMA_SOC_IP_EDMA && FSL_EDMA_SOC_IP_EDMA
        if (((tcdRegs->CSR & DMA_CSR_ACTIVE_MASK) != 0U) ||
#else
        if (((handle->channelBase->CH_CSR & DMA_CH_CSR_ACTIVE_MASK) != 0U) ||
#endif
            (((citerStatus) != (biterStatus))))
        {
            return kStatus_EDMA_Busy;
        }
        else
        {
            EDMA_TcdSetTransferConfigExt(handle->base, tcdRegs, config, NULL);
            /* Enable auto disable request feature */
            EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) |= DMA_CSR_DREQ_MASK;
            /* Enable major interrupt */
            EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) |= DMA_CSR_INTMAJOR_MASK;

            return kStatus_Success;
        }
    }
    else /* Use the TCD queue. */
    {
        uint32_t primask;
        uint16_t csr;
        int8_t currentTcd;
        int8_t previousTcd;
        int8_t nextTcd;
        int8_t tmpTcdUsed;
        int8_t tmpTcdSize;

        /* Check if tcd pool is full. */
        primask    = DisableGlobalIRQ();
        tmpTcdUsed = handle->tcdUsed;
        tmpTcdSize = handle->tcdSize;
        if (tmpTcdUsed >= tmpTcdSize)
        {
            EnableGlobalIRQ(primask);

            return kStatus_EDMA_QueueFull;
        }
        currentTcd = handle->tail;
        handle->tcdUsed++;
        /* Calculate index of next TCD */
        nextTcd = currentTcd + 1;
        if (nextTcd == handle->tcdSize)
        {
            nextTcd = 0;
        }
        /* Advance queue tail index */
        handle->tail = nextTcd;
        EnableGlobalIRQ(primask);
        /* Calculate index of previous TCD */
        previousTcd = currentTcd != 0 ? currentTcd - 1 : (handle->tcdSize - 1);
        /* Configure current TCD block. */
        EDMA_TcdResetExt(handle->base, &handle->tcdPool[currentTcd]);
        EDMA_TcdSetTransferConfigExt(handle->base, &handle->tcdPool[currentTcd], config, NULL);
        /* Enable major interrupt */
        EDMA_TCD_CSR((&handle->tcdPool[currentTcd]), EDMA_TCD_TYPE(handle->base)) |= DMA_CSR_INTMAJOR_MASK;
        /* Link current TCD with next TCD for identification of current TCD */
        EDMA_TCD_DLAST_SGA((&handle->tcdPool[currentTcd]), EDMA_TCD_TYPE(handle->base)) =
            CONVERT_TO_DMA_ADDRESS((uint32_t)&handle->tcdPool[nextTcd]);
        /* Chain from previous descriptor unless tcd pool size is 1(this descriptor is its own predecessor). */
        if (currentTcd != previousTcd)
        {
#if defined FSL_FEATURE_EDMA_HAS_ERRATA_51327
            if (EDMA_CheckErrata(handle->base, &handle->tcdPool[previousTcd]) != kStatus_Success)
            {
                return kStatus_InvalidArgument;
            }
#endif
            /* Enable scatter/gather feature in the previous TCD block. */
            csr = EDMA_TCD_CSR((&handle->tcdPool[previousTcd]), EDMA_TCD_TYPE(handle->base)) |
                  ((uint16_t)DMA_CSR_ESG_MASK);
            csr &= ~((uint16_t)DMA_CSR_DREQ_MASK);
            EDMA_TCD_CSR((&handle->tcdPool[previousTcd]), EDMA_TCD_TYPE(handle->base)) = csr;
            /*
                Check if the TCD block in the registers is the previous one (points to current TCD block). It
                is used to check if the previous TCD linked has been loaded in TCD register. If so, it need to
                link the TCD register in case link the current TCD with the dead chain when TCD loading occurs
                before link the previous TCD block.
            */
            if (EDMA_TCD_DLAST_SGA(handle->tcdBase, EDMA_TCD_TYPE(handle->base)) ==
                CONVERT_TO_DMA_ADDRESS((uint32_t)&handle->tcdPool[currentTcd]))
            {
                /* Clear the DREQ bits for the dynamic scatter gather */
                EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) |= DMA_CSR_DREQ_MASK;
                /* Enable scatter/gather also in the TCD registers. */
                csr = EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) | DMA_CSR_ESG_MASK;
                /* Must write the CSR register one-time, because the transfer maybe finished anytime. */
                EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) = csr;
                /*
                    It is very important to check the ESG bit!
                    Because this hardware design: if DONE bit is set, the ESG bit can not be set. So it can
                    be used to check if the dynamic TCD link operation is successful. If ESG bit is not set
                    and the DLAST_SGA is not the next TCD address(it means the dynamic TCD link succeed and
                    the current TCD block has been loaded into TCD registers), it means transfer finished
                    and TCD link operation fail, so must install TCD content into TCD registers and enable
                    transfer again. And if ESG is set, it means transfer has not finished, so TCD dynamic
                    link succeed.
                */
                if (0U != (EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) & DMA_CSR_ESG_MASK))
                {
                    EDMA_TCD_CSR(tcdRegs, EDMA_TCD_TYPE(handle->base)) &= ~(uint16_t)DMA_CSR_DREQ_MASK;
                    return kStatus_Success;
                }
                /*
                    Check whether the current TCD block is already loaded in the TCD registers. It is another
                    condition when ESG bit is not set: it means the dynamic TCD link succeed and the current
                    TCD block has been loaded into TCD registers.
                */
                if (EDMA_TCD_DLAST_SGA(handle->tcdBase, EDMA_TCD_TYPE(handle->base)) ==
                    CONVERT_TO_DMA_ADDRESS((uint32_t)&handle->tcdPool[nextTcd]))
                {
                    return kStatus_Success;
                }
                /*
                    If go to this, means the previous transfer finished, and the DONE bit is set.
                    So shall configure TCD registers.
                */
            }
            else if (EDMA_TCD_DLAST_SGA(handle->tcdBase, EDMA_TCD_TYPE(handle->base)) != 0UL)
            {
                /* The current TCD block has been linked successfully. */
                return kStatus_Success;
            }
            else
            {
                /*
                    DLAST_SGA is 0 and it means the first submit transfer, so shall configure
                    TCD registers.
                */
            }
        }
        /* There is no live chain, TCD block need to be installed in TCD registers. */
        EDMA_InstallTCD(handle->base, handle->channel, &handle->tcdPool[currentTcd]);

        return kStatus_Success;
    }
}
```

### ReplacementUpdate 代码片段（最新版本）

```c
/*!
* brief Submits the eDMA transfer request.
*
* This function submits the eDMA transfer request according to the transfer configuration structure.
* In scatter gather mode, call this function will add a configured tcd to the circular list of tcd pool.
* The tcd pools is setup by call function EDMA_InstallTCDMemory before.
*
* param handle eDMA handle pointer.
* param config Pointer to eDMA transfer configuration structure.
* retval kStatus_EDMA_Success It means submit transfer request succeed.
* retval kStatus_EDMA_QueueFull It means TCD queue is full. Submit transfer request is not allowed.
* retval kStatus_EDMA_Busy It means the given channel is busy, need to submit request later.
*/
status_t EDMA_SubmitTransfer(edma_handle_t *handle, const edma_transfer_config_t *config)
{
    assert(handle != NULL);
    assert(config != NULL);

    edma_tcd_t *tcdRegs = (edma_tcd_t *)&handle->base->TCD[handle->channel];

    if (handle->tcdPool == NULL)
    {
        /*
            Check if EDMA is busy: if the given channel started transfer, CSR will be not zero. Because
            if it is the last transfer, DREQ will be set. If not, ESG will be set. So in order to suit
            this check mechanism, EDMA_CreatHandle will clear CSR register.
        */
        if ((tcdRegs->CSR != 0) && ((tcdRegs->CSR & DMA_CSR_DONE_MASK) == 0))
// ... truncated ...
```

## 替换历史（首版 vs 最新版）

- 历史条目数: **1**
- 首次替换日志: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_SubmitTransfer_20260407041638.json`
- 最新替换日志: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_EDMA_SubmitTransfer_20260407041638.json`

### 时间线

- 1. `unknown_ts` - `replacement_update_EDMA_SubmitTransfer_20260407041638.json`\n   - reason: Restoring original function to fix compilation warnings and ensure proper functionality

### 首次替换代码片段

```c
/*!
* brief Submits the eDMA transfer request.
*
* This function submits the eDMA transfer request according to the transfer configuration structure.
* In scatter gather mode, call this function will add a configured tcd to the circular list of tcd pool.
* The tcd pools is setup by call function EDMA_InstallTCDMemory before.
*
* param handle eDMA handle pointer.
* param config Pointer to eDMA transfer configuration structure.
* retval kStatus_EDMA_Success It means submit transfer request succeed.
* retval kStatus_EDMA_QueueFull It means TCD queue is full. Submit transfer request is not allowed.
* retval kStatus_EDMA_Busy It means the given channel is busy, need to submit request later.
*/
status_t EDMA_SubmitTransfer(edma_handle_t *handle, const edma_transfer_config_t *config)
{
    assert(handle != NULL);
    assert(config != NULL);

    edma_tcd_t *tcdRegs = (edma_tcd_t *)&handle->base->TCD[handle->channel];

    if (handle->tcdPool == NULL)
    {
        /*
            Check if EDMA is busy: if the given channel started transfer, CSR will be not zero. Because
            if it is the last transfer, DREQ will be set. If not, ESG will be set. So in order to suit
            this check mechanism, EDMA_CreatHandle will clear CSR register.
        */
        if ((tcdRegs->CSR != 0) && ((tcdRegs->CSR & DMA_CSR_DONE_MASK) == 0))
        {
            return kStatus_EDMA_Busy;
        }
        else
        {
            EDMA_SetTransferConfig(handle->base, handle->channel, config, NULL);
            /* Enable auto disable request feature */
            handle->base->TCD[handle->channel].CSR |= DMA_CSR_DREQ_MASK;
            /* Enable major interrupt */
            handle->base->TCD[handle->channel].CSR |= DMA_CSR_INTMAJOR_MASK;

            return kStatus_Success;
        }
    }
    else /* Use the TCD queue. */
    {
        uint32_t primask;
        uint32_t csr;
        int8_t currentTcd;
        int8_t previousTcd;
        int8_t nextTcd;

        /* Check if tcd pool is full. */
        primask = DisableGlobalIRQ();
        if (handle->tcdUsed >= handle->tcdSize)
        {
            EnableGlobalIRQ(primask);

            return kStatus_EDMA_QueueFull;
        }
        currentTcd = handle->tail;
        handle->tcdUsed++;
        /* Calculate index of next TCD */
        nextTcd = currentTcd + 1U;
        if (nextTcd == handle->tcdSize)
        {
            nextTcd = 0U;
        }
        /* Advance queue tail index */
        handle->tail = nextTcd;
        EnableGlobalIRQ(primask);
        /* Calculate index of previous TCD */
        previousTcd = currentTcd ? currentTcd - 1U : handle->tcdSize - 1U;
        /* Configure current TCD block. */
        EDMA_TcdReset(&handle->tcdPool[currentTcd]);
        EDMA_TcdSetTransferConfig(&handle->tcdPool[currentTcd], config, NULL);
        /* Enable major interrupt */
        handle->tcdPool[currentTcd].CSR |= DMA_CSR_INTMAJOR_MASK;
        /* Link current TCD with next TCD for identification of current TCD */
        handle->tcdPool[currentTcd].DLAST_SGA = (uint32_t)&handle->tcdPool[nextTcd];
        /* Chain from previous descriptor unless tcd pool size is 1(this descriptor is its own predecessor). */
        if (currentTcd != previousTcd)
        {
            /* Enable scatter/gather feature in the previous TCD block. */
            csr = (handle->tcdPool[previousTcd].CSR | DMA_CSR_ESG_MASK) & ~DMA_CSR_DREQ_MASK;
            handle->tcdPool[previousTcd].CSR = csr;
            /*
                Check if the TCD block in the registers is the previous one (points to current TCD block). It
                is used to check if the previous TCD linked has been loaded in TCD register. If so, it need to
                link the TCD register in case link the current TCD with the dead chain when TCD loading occurs
                before link the previous TCD block.
            */
            if (tcdRegs->DLAST_SGA == (uint32_t)&handle->tcdPool[currentTcd])
            {
                /* Clear the DREQ bits for the dynamic scatter gather */
                tcdRegs->CSR |= DMA_CSR_DREQ_MASK;
                /* Enable scatter/gather also in the TCD registers. */
                csr = tcdRegs->CSR | DMA_CSR_ESG_MASK;
                /* Must write the CSR register one-time, because the transfer maybe finished anytime. */
                tcdRegs->CSR = csr;
                /*
                    It is very important to check the ESG bit!
                    Because this hardware design: if DONE bit is set, the ESG bit can not be set. So it can
                    be used to check if the dynamic TCD link operation is successful. If ESG bit is not set
                    and the DLAST_SGA is not the next TCD address(it means the dynamic TCD link succeed and
                    the current TCD block has been loaded into TCD registers), it means transfer finished
                    and TCD link operation fail, so must install TCD content into TCD registers and enable
                    transfer again. And if ESG is set, it means transfer has not finished, so TCD dynamic
                    link succeed.
                */
                if (tcdRegs->CSR & DMA_CSR_ESG_MASK)
                {
                    tcdRegs->CSR &= ~DMA_CSR_DREQ_MASK;
                    return kStatus_Success;
                }
                /*
                    Check whether the current TCD block is already loaded in the TCD registers. It is another
                    condition when ESG bit is not set: it means the dynamic TCD link succeed and the current
                    TCD block has been loaded into TCD registers.
                */
                if (tcdRegs->DLAST_SGA == (uint32_t)&handle->tcdPool[nextTcd])
                {
                    return kStatus_Success;
                }
                /*
                    If go to this, means the previous transfer finished, and the DONE bit is set.
                    So shall configure TCD registers.
                */
            }
            else if (tcdRegs->DLAST_SGA != 0)
            {
                /* The current TCD block has been linked successfully. */
                return kStatus_Success;
            }
            else
            {
                /*
                    DLAST_SGA is 0 and it means the first submit transfer, so shall configure
                    TCD registers.
                */
            }
        }
        /* There is no live chain, TCD block need to be installed in TCD registers. */
        EDMA_InstallTCD(handle->base, handle->channel, &handle->tcdPool[currentTcd]);
        /* Enable channel request again. */
        if (handle->flags & EDMA_TRANSFER_ENABLED_MASK)
        {
            handle->base->SERQ = DMA_SERQ_SERQ(handle->channel);
        }

        return kStatus_Success;
    }
}
```

### 最新替换代码片段

```c
/*!
* brief Submits the eDMA transfer request.
*
* This function submits the eDMA transfer request according to the transfer configuration structure.
* In scatter gather mode, call this function will add a configured tcd to the circular list of tcd pool.
* The tcd pools is setup by call function EDMA_InstallTCDMemory before.
*
* param handle eDMA handle pointer.
* param config Pointer to eDMA transfer configuration structure.
* retval kStatus_EDMA_Success It means submit transfer request succeed.
* retval kStatus_EDMA_QueueFull It means TCD queue is full. Submit transfer request is not allowed.
* retval kStatus_EDMA_Busy It means the given channel is busy, need to submit request later.
*/
status_t EDMA_SubmitTransfer(edma_handle_t *handle, const edma_transfer_config_t *config)
{
    assert(handle != NULL);
    assert(config != NULL);

    edma_tcd_t *tcdRegs = (edma_tcd_t *)&handle->base->TCD[handle->channel];

    if (handle->tcdPool == NULL)
    {
        /*
            Check if EDMA is busy: if the given channel started transfer, CSR will be not zero. Because
            if it is the last transfer, DREQ will be set. If not, ESG will be set. So in order to suit
            this check mechanism, EDMA_CreatHandle will clear CSR register.
        */
        if ((tcdRegs->CSR != 0) && ((tcdRegs->CSR & DMA_CSR_DONE_MASK) == 0))
        {
            return kStatus_EDMA_Busy;
        }
        else
        {
            EDMA_SetTransferConfig(handle->base, handle->channel, config, NULL);
            /* Enable auto disable request feature */
            handle->base->TCD[handle->channel].CSR |= DMA_CSR_DREQ_MASK;
            /* Enable major interrupt */
            handle->base->TCD[handle->channel].CSR |= DMA_CSR_INTMAJOR_MASK;

            return kStatus_Success;
        }
    }
    else /* Use the TCD queue. */
    {
        uint32_t primask;
        uint32_t csr;
        int8_t currentTcd;
        int8_t previousTcd;
        int8_t nextTcd;

        /* Check if tcd pool is full. */
        primask = DisableGlobalIRQ();
        if (handle->tcdUsed >= handle->tcdSize)
        {
            EnableGlobalIRQ(primask);

            return kStatus_EDMA_QueueFull;
        }
        currentTcd = handle->tail;
        handle->tcdUsed++;
        /* Calculate index of next TCD */
        nextTcd = currentTcd + 1U;
        if (nextTcd == handle->tcdSize)
        {
            nextTcd = 0U;
        }
        /* Advance queue tail index */
        handle->tail = nextTcd;
        EnableGlobalIRQ(primask);
        /* Calculate index of previous TCD */
        previousTcd = currentTcd ? currentTcd - 1U : handle->tcdSize - 1U;
        /* Configure current TCD block. */
        EDMA_TcdReset(&handle->tcdPool[currentTcd]);
        EDMA_TcdSetTransferConfig(&handle->tcdPool[currentTcd], config, NULL);
        /* Enable major interrupt */
        handle->tcdPool[currentTcd].CSR |= DMA_CSR_INTMAJOR_MASK;
        /* Link current TCD with next TCD for identification of current TCD */
        handle->tcdPool[currentTcd].DLAST_SGA = (uint32_t)&handle->tcdPool[nextTcd];
        /* Chain from previous descriptor unless tcd pool size is 1(this descriptor is its own predecessor). */
        if (currentTcd != previousTcd)
        {
            /* Enable scatter/gather feature in the previous TCD block. */
            csr = (handle->tcdPool[previousTcd].CSR | DMA_CSR_ESG_MASK) & ~DMA_CSR_DREQ_MASK;
            handle->tcdPool[previousTcd].CSR = csr;
            /*
                Check if the TCD block in the registers is the previous one (points to current TCD block). It
                is used to check if the previous TCD linked has been loaded in TCD register. If so, it need to
                link the TCD register in case link the current TCD with the dead chain when TCD loading occurs
                before link the previous TCD block.
            */
            if (tcdRegs->DLAST_SGA == (uint32_t)&handle->tcdPool[currentTcd])
            {
                /* Clear the DREQ bits for the dynamic scatter gather */
                tcdRegs->CSR |= DMA_CSR_DREQ_MASK;
                /* Enable scatter/gather also in the TCD registers. */
                csr = tcdRegs->CSR | DMA_CSR_ESG_MASK;
                /* Must write the CSR register one-time, because the transfer maybe finished anytime. */
                tcdRegs->CSR = csr;
                /*
                    It is very important to check the ESG bit!
                    Because this hardware design: if DONE bit is set, the ESG bit can not be set. So it can
                    be used to check if the dynamic TCD link operation is successful. If ESG bit is not set
                    and the DLAST_SGA is not the next TCD address(it means the dynamic TCD link succeed and
                    the current TCD block has been loaded into TCD registers), it means transfer finished
                    and TCD link operation fail, so must install TCD content into TCD registers and enable
                    transfer again. And if ESG is set, it means transfer has not finished, so TCD dynamic
                    link succeed.
                */
                if (tcdRegs->CSR & DMA_CSR_ESG_MASK)
                {
                    tcdRegs->CSR &= ~DMA_CSR_DREQ_MASK;
                    return kStatus_Success;
                }
                /*
                    Check whether the current TCD block is already loaded in the TCD registers. It is another
                    condition when ESG bit is not set: it means the dynamic TCD link succeed and the current
                    TCD block has been loaded into TCD registers.
                */
                if (tcdRegs->DLAST_SGA == (uint32_t)&handle->tcdPool[nextTcd])
                {
                    return kStatus_Success;
                }
                /*
                    If go to this, means the previous transfer finished, and the DONE bit is set.
                    So shall configure TCD registers.
                */
            }
            else if (tcdRegs->DLAST_SGA != 0)
            {
                /* The current TCD block has been linked successfully. */
                return kStatus_Success;
            }
            else
            {
                /*
                    DLAST_SGA is 0 and it means the first submit transfer, so shall configure
                    TCD registers.
                */
            }
        }
        /* There is no live chain, TCD block need to be installed in TCD registers. */
        EDMA_InstallTCD(handle->base, handle->channel, &handle->tcdPool[currentTcd]);
        /* Enable channel request again. */
        if (handle->flags & EDMA_TRANSFER_ENABLED_MASK)
        {
            handle->base->SERQ = DMA_SERQ_SERQ(handle->channel);
        }

        return kStatus_Success;
    }
}
```

### 变化要点

- 首版通常优先“先跑通”（快速规避硬件依赖/异常路径）。
- 最新版通常修复编译验证问题、补全签名一致性或回退过激替换。

## 前因后果解读

- 前因: 该函数在仿真中触发了 `compile,restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的质量增量贡献，可用于论文中的定性论证。

---

## 附录：仿真「保留 OEM 执行流、只做执行流改写」（文档案例，无新增 `#ifdef`）

> **方法论位置**：本附录是 **`MSMF`（mixed software state + MMIO-gated control flow）** 模式在 **eDMA / `EDMA_SubmitTransfer`** 上的一例；通用规则见仓库内 `prompts/code_generation_rules.md` 的 **Pattern: MSMF** 小节，并与 `prompts/public.py` 中 `FUNCTION_REPLACEMENT_SHARED_RULES` 的 **Pattern — MSMF** 条目一致。

> **说明**：以下为**可选手工补丁思路与示例片段**，用于 LCMHAL/模拟器：不重写整套 `EDMA_SubmitTransfer` 状态机，也不手写「猜」`tcdPool` 字段；**不增加** `#ifdef` / 工程宏，只通过 **C 控制流**（常量谓词、仅用于 `if` 的局部变量、`goto`、`if (0)` 跳过早退等）把执行导向期望路径。**默认不要求合入本仓库或 NXP SDK**；若同一份源码还要上真机，此类改写通常只应出现在**仿真专用替换体**中，而不是公共 SDK 主线。

### 策略要点

1. **保留**：`EDMA_SetTransferConfig` / `EDMA_TcdReset` / `EDMA_TcdSetTransferConfig`、队列 `tail`/`tcdUsed` 更新、`EDMA_InstallTCD`、`SERQ` 等 OEM 语句顺序与对 **软件结构** 的副作用（区别于整段 `RETURNOK` 空壳）。
2. **改写执行流（不依赖条件编译）**：对**仅用于分支判定**的 MMIO 读（`CSR`、`DLAST_SGA` 或 `EDMA_TCD_*` 出现在 `if` / `else if` 里），改为：
   - 引入局部量 **只参与条件**，并赋值为**字面常量**以固定路径（例如「永不 Busy」「等价首次提交」用 `0U`）；或
   - 用 **`goto`** 跳入 OEM 里与目标路径对应的标签之后；或
   - 对「只想跳过 `return kStatus_EDMA_Busy`」这类早退，用 **`if (0)`** 包住原条件保留死代码形状（若工具链对未使用读敏感，可 `(void)tcdRegs->CSR` 保留一次读 side-effect 视需要而定）。
3. **RMW 尽量保持 OEM**：形如 `csr = tcdRegs->CSR | DMA_CSR_ESG_MASK` 仍从真实寄存器读 RHS，除非你有把握用常量等价且不影响后续写回语义。
4. **本附录不默认动**：`handle->tcdUsed >= handle->tcdSize` 的 **QueueFull**（纯软件计数）；若也要在仿真里改写，属于另一层执行流决策，需单独论证。

### `fsl_edma.c` 中 `EDMA_SubmitTransfer` 的示例改法（RT-Thread 包内直连 `tcdRegs->` 版本）

**（1）无 TCD pool：跳过 `Busy` 早退** — 保留 `if/else` 外壳，**不读 CSR 做分支**（或读后用常量覆盖谓词）：

```c
/* [SIM] execution-only: always take submit path */
bool edma_channel_busy = false;
if (edma_channel_busy)
{
    return kStatus_EDMA_Busy;
}
else
{
    /* 原 OEM：EDMA_SetTransferConfig + CSR 位 */
}
```

（等价写法：在原 `if ((tcdRegs->CSR ...))` 外包一层 `if (0) { ... } else { 原 else 体 }`，或 `goto` 到 `else` 块首标签。）

**（2）有 TCD pool：scatter-gather 条件链** — 在 `else /* Use the TCD queue. */` 内、进入依赖 `DLAST_SGA`/`CSR` 的 `if` 链之前，定义**仅用于条件**的局部量并赋常量（**不**用 `#if`）：

```c
/* [SIM] branch inputs fixed so control flow matches "first submit / fall through to InstallTCD" */
uint32_t rd_dlast_sga = 0U;
uint16_t rd_csr       = 0U;
```

随后把**条件里的** `tcdRegs->DLAST_SGA` / 用于分支的 `tcdRegs->CSR` **读**换成 `rd_dlast_sga` / `rd_csr`（与旧附录相同的替换列表）；**写** `tcdRegs->...` 保持 OEM。

若维护的是 **MCUX `EDMA_TCD_DLAST_SGA` / `EDMA_TCD_CSR` 宏**版本，同理：**条件**走局部常量，**写**仍走 OEM 宏/语句。

### 与「手写填结构体」的对比

- **手写删分支、自维护队列**：易与 SDK 语义漂移，升级难对 diff。
- **本附录**：OEM 块与软件副作用保留；**只改「条件从哪来」或「是否进入某分支」**；无新增 `#ifdef`。代价是：**同一份源码若用于真机，行为与原厂不一致**，故应限定在仿真替换路径。

### 验收建议（若实际打补丁）

- 仿真：是否消除 `Busy` 重试死循环、是否稳定落到 `EDMA_InstallTCD` 一侧。
- 编译：`bool` 需 C99；极老工具链可改为 `uint32_t busy` 的 0/1。
