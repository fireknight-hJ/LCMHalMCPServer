## LCMHAL 函数替换日志

- **Testcase 路径**: `testcases/server/zephyr/nxp/eth_dhcpv4_mimxrt1060`

## 1. 替换函数总览

| 函数名 | 文件路径 | 行号 | 替换次数 |
|--------|----------|------|----------|
| `ENET_GetRxFrame` | `/home/haojie/zephyrproject/modules/hal/nxp/mcux/mcux-sdk/drivers/enet/fsl_enet.c` | 2169 | 1 |
| `ENET_SetMacAddr` | `/home/haojie/zephyrproject/modules/hal/nxp/mcux/mcux-sdk/drivers/enet/fsl_enet.c` | 1124 | 1 |
| `clock_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c` | 125 | 2 |
| `eth_callback` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 930 | 2 |
| `eth_mcux_common_isr` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 1310 | 1 |
| `eth_mcux_phy_enter_reset` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 355 | 1 |
| `eth_mcux_phy_event` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 448 | 1 |
| `eth_mcux_phy_setup` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 632 | 1 |
| `eth_mcux_phy_start` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 370 | 1 |
| `eth_mcux_set_config` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 1240 | 1 |
| `eth_tx` | `/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c` | 704 | 1 |
| `imx_pinctrl_init` | `/home/haojie/zephyrproject/zephyr/drivers/pinctrl/pinctrl_imx.c` | 66 | 1 |
| `imxrt_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c` | 317 | 1 |
| `z_arm_platform_init` | `/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c` | 344 | 1 |

## 2. 各函数替换详情

### ENET_GetRxFrame

```text
=== ENET_GetRxFrame 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/modules/hal/nxp/mcux/mcux-sdk/drivers/enet/fsl_enet.c
- 行号：2169
- 函数内容：status_t ENET_GetRxFrame(ENET_Type *base, enet_handle_t *handle, enet_rx_frame_struct_t *rxFrame, uint8_t ringId)
{
    assert(handle != NULL);
    assert(ringId < (uint8_t)FSL_FEATURE_ENET_QUEUE);
    assert(handle->rxBdRing[ringId].rxBdBase != NULL);
    assert(rxFrame != NULL);
    assert(rxFrame->rxBuffArray != NULL);

    status_t result                              = kStatus_ENET_RxFrameEmpty;
    enet_rx_bd_ring_t *rxBdRing                  = &handle->rxBdRing[ringId];
    volatile enet_rx_bd_struct_t *curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    bool isLastBuff                              = false;
    uintptr_t newBuff                            = 0;
    uint16_t buffLen                             = 0;
    enet_buffer_struct_t *rxBuffer;
    uintptr_t address;
    uintptr_t buffer;
    uint16_t index;

    /* Check the current buffer descriptor's empty flag. If empty means there is no frame received. */
    index = rxBdRing->rxGenIdx;
    while (0U == (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK))
    {
        /* Find the last buffer descriptor. */
        if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
        {
            /* The last buffer descriptor stores the error status of this received frame. */
            result = ENET_GetRxFrameErr((enet_rx_bd_struct_t *)(uintptr_t)curBuffDescrip, &rxFrame->rxFrameError);
            break;
        }

        /* Get feedback that no-empty BD takes frame length of 0. Probably an IP issue and drop this BD. */
        if (curBuffDescrip->length == 0U)
        {
            /* Set LAST bit manually to let following drop error frame operation drop this abnormal BD. */
            curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_LAST_MASK;
            result = kStatus_ENET_RxFrameError;
            break;
        }

        /* Can't find the last BD flag, no valid frame. */
        index          = ENET_IncreaseIndex(index, rxBdRing->rxRingLen);
        curBuffDescrip = rxBdRing->rxBdBase + index;
        if (index == rxBdRing->rxGenIdx)
        {
            /* kStatus_ENET_RxFrameEmpty. */
            break;
        }
    }

    /* Drop the error frame. */
    if (result == kStatus_ENET_RxFrameError)
    {
        curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
        do
        {
            /* The last buffer descriptor of a frame. */
            if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
            {
                isLastBuff = true;
            }

            /* Clears status including the owner flag. */
            curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
            /* Sets the receive buffer descriptor with the empty flag. */
            curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;

            /* Increase current buffer descriptor to the next one. */
            rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
            curBuffDescrip     = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
        } while (!isLastBuff);

        ENET_ActiveReadRing(base, ringId);

        return result;
    }
    else if (result != kStatus_Success)
    {
        return result;
    }
    else
    {
        /* Intentional empty */
    }

    /* Get the valid frame */
    curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    index          = 0;
    do
    {
        newBuff = (uintptr_t)(uint8_t *)handle->rxBuffAlloc(base, handle->userData, ringId);
        if (newBuff != 0U)
        {
            assert((uint64_t)newBuff + handle->rxBuffSizeAlign[ringId] - 1U <= UINT32_MAX);
            rxBuffer = &rxFrame->rxBuffArray[index];

#if defined(FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET) && FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET
            address = MEMORY_ConvertMemoryMapAddress(curBuffDescrip->buffer, kMEMORY_DMA2Local);
#else
            address = curBuffDescrip->buffer;
#endif /* FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET */
#if defined(FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL) && FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL
            if (handle->rxMaintainEnable[ringId])
            {
                DCACHE_InvalidateByRange(address, handle->rxBuffSizeAlign[ringId]);
            }
#endif /* FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL */

            rxBuffer->buffer = (void *)(uint8_t *)address;

            /* The last buffer descriptor of a frame. */
            if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
            {
                /* This is a valid frame. */
                isLastBuff       = true;
                rxFrame->totLen  = curBuffDescrip->length;
                rxBuffer->length = curBuffDescrip->length - buffLen;

                rxFrame->rxAttribute.promiscuous = false;
                if (0U != (base->RCR & ENET_RCR_PROM_MASK))
                {
                    if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_MISS_MASK))
                    {
                        rxFrame->rxAttribute.promiscuous = true;
                    }
                }
#ifdef ENET_ENHANCEDBUFFERDESCRIPTOR_MODE
                rxFrame->rxAttribute.timestamp = curBuffDescrip->timestamp;
#endif /* ENET_ENHANCEDBUFFERDESCRIPTOR_MODE */
            }
            else
            {
                rxBuffer->length = curBuffDescrip->length;
                buffLen += rxBuffer->length;
            }

            /* Give new buffer from application to BD */

#if defined(FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET) && FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET
            buffer = MEMORY_ConvertMemoryMapAddress(newBuff, kMEMORY_Local2DMA);
#else
            buffer  = newBuff;
#endif /* FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET */
#if defined(FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL) && FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL
            if (handle->rxMaintainEnable[ringId])
            {
                DCACHE_InvalidateByRange(buffer, handle->rxBuffSizeAlign[ringId]);
            }
#endif /* FSL_SDK_ENABLE_DRIVER_CACHE_CONTROL */

            curBuffDescrip->buffer = (uint32_t)buffer;

            /* Clears status including the owner flag. */
            curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
            /* Sets the receive buffer descriptor with the empty flag. */
            curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;

            /* Increase Rx array index and the buffer descriptor address. */
            index++;
            rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
            curBuffDescrip     = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
        }
        else
        {
            /* Drop frame if there's no new buffer memory */

            /* Free the incomplete frame buffers. */
            while (index-- != 0U)
            {
                handle->rxBuffFree(base, &rxFrame->rxBuffArray[index].buffer, handle->userData, ringId);
            }

            /* Update left buffers as ready for next coming frame */
            do
            {
                /* The last buffer descriptor of a frame. */
                if (0U != (curBuffDescrip->control & ENET_BUFFDESCRIPTOR_RX_LAST_MASK))
                {
                    isLastBuff = true;
                }

                /* Clears status including the owner flag. */
                curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
                /* Sets the receive buffer descriptor with the empty flag. */
                curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;

                /* Increase current buffer descriptor to the next one. */
                rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
                curBuffDescrip     = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
            } while (!isLastBuff);

            result = kStatus_ENET_RxFrameDrop;
            break;
        }
    } while (!isLastBuff);

    ENET_ActiveReadRing(base, ringId);

    return result;
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Receives one Ethernet frame from a specified buffer descriptor ring with zero copy, using user-defined allocation and free callbacks for buffer management.
- 是否需要替换：是
- 分类/替换原因：This function is classified as RECV because: 1) It performs critical data I/O (Ethernet frame reception), 2) It manages DMA buffer descriptors and ring structures, 3) It contains hardware-dependent operations including scanning buffer descriptor control flags (EMPTY, LAST masks), accessing ENET peripheral registers (base->RCR), and calling hardware activation functions (ENET_ActiveReadRing), 4) It fits the RECV category with complex DMA+RingBuffer control flow requiring 'single packet mode' simulation. The function scans buffer descriptor rings looking for received frames, processes buffer allocation/deallocation, and updates hardware state. GetMMIOFunctionInfo revealed multiple MMIO-related accesses including buffer descriptor field accesses and peripheral register checks.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
status_t ENET_GetRxFrame(ENET_Type *base, enet_handle_t *handle, enet_rx_frame_struct_t *rxFrame, uint8_t ringId)
{
    assert(handle != NULL);
    assert(ringId < (uint8_t)FSL_FEATURE_ENET_QUEUE);
    assert(handle->rxBdRing[ringId].rxBdBase != NULL);
    assert(rxFrame != NULL);
    assert(rxFrame->rxBuffArray != NULL);

    status_t result                              = kStatus_ENET_RxFrameEmpty;
    enet_rx_bd_ring_t *rxBdRing                  = &handle->rxBdRing[ringId];
    volatile enet_rx_bd_struct_t *curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    bool isLastBuff                              = false;
    uintptr_t newBuff                            = 0;
    uint16_t buffLen                             = 0;
    enet_buffer_struct_t *rxBuffer;
    uintptr_t address;
    uintptr_t buffer;
    uint16_t index;

    /* Skip hardware-dependent scanning loop - assume we have a valid frame */
    /* Original while loop scanning for non-empty BD removed for simulation */
    
    /* For simulation: Assume we have a valid frame to process */
    /* Skip to the valid frame processing section */
    
    /* Get the valid frame - single packet mode for simulation */
    curBuffDescrip = rxBdRing->rxBdBase + rxBdRing->rxGenIdx;
    index          = 0;
    
    /* Single iteration for simulation - process one frame only */
    newBuff = (uintptr_t)(uint8_t *)handle->rxBuffAlloc(base, handle->userData, ringId);
    if (newBuff != 0U)
    {
        assert((uint64_t)newBuff + handle->rxBuffSizeAlign[ringId] - 1U <= UINT32_MAX);
        rxBuffer = &rxFrame->rxBuffArray[index];

        /* Get address from current BD */
#if defined(FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET) && FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET
        address = MEMORY_ConvertMemoryMapAddress(curBuffDescrip->buffer, kMEMORY_DMA2Local);
#else
        address = curBuffDescrip->buffer;
#endif /* FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET */

        /* For simulation: If buffer is 0, allocate and set it */
        if (address == 0U)
        {
            address = newBuff;
        }

        rxBuffer->buffer = (void *)(uint8_t *)address;

        /* For simulation: Set as last buffer and get frame data */
        isLastBuff       = true;
        /* Simulate receiving frame data */
        rxFrame->totLen = HAL_BE_ENET_ReadFrame(rxBuffer->buffer, handle->rxBuffSizeAlign[ringId]);
        rxBuffer->length = rxFrame->totLen;

        rxFrame->rxAttribute.promiscuous = false;
        /* Skip hardware register check for simulation */
#ifdef ENET_ENHANCEDBUFFERDESCRIPTOR_MODE
        rxFrame->rxAttribute.timestamp = 0; /* No timestamp in simulation */
#endif /* ENET_ENHANCEDBUFFERDESCRIPTOR_MODE */

        /* Give new buffer from application to BD */
#if defined(FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET) && FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET
        buffer = MEMORY_ConvertMemoryMapAddress(newBuff, kMEMORY_Local2DMA);
#else
        buffer  = newBuff;
#endif /* FSL_FEATURE_MEMORY_HAS_ADDRESS_OFFSET */

        curBuffDescrip->buffer = (uint32_t)buffer;

        /* Clears status including the owner flag. */
        curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
        /* Sets the receive buffer descriptor with the empty flag. */
        curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;
        /* Set LAST flag for simulation */
        curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_LAST_MASK;
        /* Set length for simulation */
        curBuffDescrip->length = rxFrame->totLen;

        /* Increase Rx array index and the buffer descriptor address. */
        index++;
        rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
        
        result = kStatus_Success;
    }
    else
    {
        /* Drop frame if there's no new buffer memory */
        result = kStatus_ENET_RxFrameDrop;
        
        /* For simulation: Still need to advance the ring */
        curBuffDescrip->control &= ENET_BUFFDESCRIPTOR_RX_WRAP_MASK;
        curBuffDescrip->control |= ENET_BUFFDESCRIPTOR_RX_EMPTY_MASK;
        rxBdRing->rxGenIdx = ENET_IncreaseIndex(rxBdRing->rxGenIdx, rxBdRing->rxRingLen);
    }

    /* Skip hardware activation for simulation */
    /* ENET_ActiveReadRing(base, ringId); */

    return result;
}
```

=== 信息结束 ===
```

### ENET_SetMacAddr

```text
=== ENET_SetMacAddr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/modules/hal/nxp/mcux/mcux-sdk/drivers/enet/fsl_enet.c
- 行号：1124
- 函数内容：void ENET_SetMacAddr(ENET_Type *base, uint8_t *macAddr)
{
    uint32_t address;

    /* Set physical address lower register. */
    address = (uint32_t)(((uint32_t)macAddr[0] << 24U) | ((uint32_t)macAddr[1] << 16U) | ((uint32_t)macAddr[2] << 8U) |
                         (uint32_t)macAddr[3]);
    base->PALR = address;
    /* Set physical address high register. */
    address    = (uint32_t)(((uint32_t)macAddr[4] << 8U) | ((uint32_t)macAddr[5]));
    base->PAUR = address << ENET_PAUR_PADDR2_SHIFT;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Sets the MAC address for the ENET (Ethernet) module by writing to hardware registers
- 是否需要替换：是
- 分类/替换原因：GetFunctionInfo revealed the function writes to ENET peripheral registers (PALR and PAUR) to configure the MAC address. GetMMIOFunctionInfo confirmed hardware register accesses. The function performs peripheral initialization (setting MAC address) without data transmission/reception, interrupt handling, or polling loops. According to classification priority order (CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER), this fits INIT category as it initializes peripheral configuration. The replacement removes MMIO operations while preserving function structure and parameter handling.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/*!
* brief Sets the ENET module Mac address.
*
* param base  ENET peripheral base address.
* param macAddr The six-byte Mac address pointer.
*        The pointer is allocated by application and input into the API.
*/
void ENET_SetMacAddr(ENET_Type *base, uint8_t *macAddr)
{
    uint32_t address;

    /* Set physical address lower register. */
    address = (uint32_t)(((uint32_t)macAddr[0] << 24U) | ((uint32_t)macAddr[1] << 16U) | ((uint32_t)macAddr[2] << 8U) |
                         (uint32_t)macAddr[3]);
    /* [INIT REMOVED] base->PALR = address; */
    /* Set physical address high register. */
    address    = (uint32_t)(((uint32_t)macAddr[4] << 8U) | ((uint32_t)macAddr[5]));
    /* [INIT REMOVED] base->PAUR = address << ENET_PAUR_PADDR2_SHIFT; */
}
```

=== 信息结束 ===
```

### clock_init

```text
=== clock_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c
- 行号：125
- 函数内容：static ALWAYS_INLINE void clock_init(void)
{
	/* Boot ROM did initialize the XTAL, here we only sets external XTAL
	 * OSC freq
	 */
	CLOCK_SetXtalFreq(DT_PROP(DT_CLOCKS_CTLR_BY_NAME(CCM_NODE, xtal),
				  clock_frequency));
	CLOCK_SetRtcXtalFreq(DT_PROP(DT_CLOCKS_CTLR_BY_NAME(CCM_NODE, rtc_xtal),
				     clock_frequency));

	/* Set PERIPH_CLK2 MUX to OSC */
	CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0x1);

	/* Set PERIPH_CLK MUX to PERIPH_CLK2 */
	CLOCK_SetMux(kCLOCK_PeriphMux, 0x1);

	/* Setting the VDD_SOC value.
	 */
	DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(CONFIG_DCDC_VALUE);
	/* Waiting for DCDC_STS_DC_OK bit is asserted */
	while (DCDC_REG0_STS_DC_OK_MASK !=
			(DCDC_REG0_STS_DC_OK_MASK & DCDC->REG0)) {
		;
	}

#ifdef CONFIG_INIT_ARM_PLL
	CLOCK_InitArmPll(&armPllConfig); /* Configure ARM PLL to 1200M */
#endif
#ifdef CONFIG_INIT_ENET_PLL
	CLOCK_InitEnetPll(&ethPllConfig);
#endif
#ifdef CONFIG_INIT_VIDEO_PLL
	CLOCK_InitVideoPll(&videoPllConfig);
#endif

#if DT_NODE_EXISTS(DT_CHILD(CCM_NODE, arm_podf))
	/* Set ARM PODF */
	BUILD_ASSERT_PODF_IN_RANGE(arm_podf, 1, 8);
	CLOCK_SetDiv(kCLOCK_ArmDiv, DT_PROP(DT_CHILD(CCM_NODE, arm_podf), clock_div) - 1);
#endif
	/* Set AHB PODF */
	BUILD_ASSERT_PODF_IN_RANGE(ahb_podf, 1, 8);
	CLOCK_SetDiv(kCLOCK_AhbDiv, DT_PROP(DT_CHILD(CCM_NODE, ahb_podf), clock_div) - 1);
	/* Set IPG PODF */
	BUILD_ASSERT_PODF_IN_RANGE(ipg_podf, 1, 4);
	CLOCK_SetDiv(kCLOCK_IpgDiv, DT_PROP(DT_CHILD(CCM_NODE, ipg_podf), clock_div) - 1);

	/* Set PRE_PERIPH_CLK to PLL1, 1200M */
	CLOCK_SetMux(kCLOCK_PrePeriphMux, 0x3);

	/* Set PERIPH_CLK MUX to PRE_PERIPH_CLK */
	CLOCK_SetMux(kCLOCK_PeriphMux, 0x0);

#ifdef CONFIG_UART_MCUX_LPUART
	/* Configure UART divider to default */
	CLOCK_SetMux(kCLOCK_UartMux, 0); /* Set UART source to PLL3 80M */
	CLOCK_SetDiv(kCLOCK_UartDiv, 0); /* Set UART divider to 1 */
#endif

#ifdef CONFIG_I2C_MCUX_LPI2C
	CLOCK_SetMux(kCLOCK_Lpi2cMux, 0); /* Set I2C source as USB1 PLL 480M */
	CLOCK_SetDiv(kCLOCK_Lpi2cDiv, 5); /* Set I2C divider to 6 */
#endif

#ifdef CONFIG_SPI_MCUX_LPSPI
	CLOCK_SetMux(kCLOCK_LpspiMux, 1); /* Set SPI source to USB1 PFD0 720M */
	CLOCK_SetDiv(kCLOCK_LpspiDiv, 7); /* Set SPI divider to 8 */
#endif

#ifdef CONFIG_DISPLAY_MCUX_ELCDIF
	/* MUX selects video PLL, which is initialized to 93MHz */
	CLOCK_SetMux(kCLOCK_LcdifPreMux, 2);
	/* Divide output by 2 */
	CLOCK_SetDiv(kCLOCK_LcdifDiv, 1);
	/* Set final div based on LCDIF clock-frequency */
	CLOCK_SetDiv(kCLOCK_LcdifPreDiv,
		((CLOCK_GetPllFreq(kCLOCK_PllVideo) / 2) /
		DT_PROP(DT_CHILD(DT_NODELABEL(lcdif), display_timings),
			clock_frequency)) - 1);
#endif


#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet), okay) && CONFIG_NET_L2_ETHERNET
#if CONFIG_ETH_MCUX_RMII_EXT_CLK
	/* Enable clock input for ENET1 */
	IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1TxClkOutputDir, false);
#else
	/* Enable clock output for ENET1 */
	IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1TxClkOutputDir, true);
#endif
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet2), okay) && CONFIG_NET_L2_ETHERNET
	/* Set ENET2 ref clock to be generated by External OSC,*/
	/* direction as output and frequency to 50MHz */
	IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET2TxClkOutputDir |
				kIOMUXC_GPR_ENET2RefClkMode, true);
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb1), okay) && CONFIG_USB_DC_NXP_EHCI
	CLOCK_EnableUsbhs0PhyPllClock(kCLOCK_Usb480M,
		DT_PROP_BY_PHANDLE(DT_NODELABEL(usb1), clocks, clock_frequency));
	CLOCK_EnableUsbhs0Clock(kCLOCK_Usb480M,
		DT_PROP_BY_PHANDLE(DT_NODELABEL(usb1), clocks, clock_frequency));
	USB_EhciPhyInit(kUSB_ControllerEhci0, CPU_XTAL_CLK_HZ, &usbPhyConfig);
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb2), okay) && CONFIG_USB_DC_NXP_EHCI
	CLOCK_EnableUsbhs1PhyPllClock(kCLOCK_Usb480M,
		DT_PROP_BY_PHANDLE(DT_NODELABEL(usb2), clocks, clock_frequency));
	CLOCK_EnableUsbhs1Clock(kCLOCK_Usb480M,
		DT_PROP_BY_PHANDLE(DT_NODELABEL(usb2), clocks, clock_frequency));
	USB_EhciPhyInit(kUSB_ControllerEhci1, CPU_XTAL_CLK_HZ, &usbPhyConfig);
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc1), okay) && CONFIG_IMX_USDHC
	/* Configure USDHC clock source and divider */
	CLOCK_InitSysPfd(kCLOCK_Pfd0, 24U);
	CLOCK_SetDiv(kCLOCK_Usdhc1Div, 1U);
	CLOCK_SetMux(kCLOCK_Usdhc1Mux, 1U);
	CLOCK_EnableClock(kCLOCK_Usdhc1);
#endif
#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc2), okay) && CONFIG_IMX_USDHC
	/* Configure USDHC clock source and divider */
	CLOCK_InitSysPfd(kCLOCK_Pfd0, 24U);
	CLOCK_SetDiv(kCLOCK_Usdhc2Div, 1U);
	CLOCK_SetMux(kCLOCK_Usdhc2Mux, 1U);
	CLOCK_EnableClock(kCLOCK_Usdhc2);
#endif

#ifdef CONFIG_VIDEO_MCUX_CSI
	CLOCK_EnableClock(kCLOCK_Csi); /* Disable CSI clock gate */
	CLOCK_SetDiv(kCLOCK_CsiDiv, 0); /* Set CSI divider to 1 */
	CLOCK_SetMux(kCLOCK_CsiMux, 0); /* Set CSI source to OSC 24M */
#endif
#ifdef CONFIG_CAN_MCUX_FLEXCAN
	CLOCK_SetDiv(kCLOCK_CanDiv, 1); /* Set CAN_CLK_PODF. */
	CLOCK_SetMux(kCLOCK_CanMux, 2); /* Set Can clock source. */
#endif

#ifdef CONFIG_LOG_BACKEND_SWO
	/* Enable ARM trace clock to enable SWO output */
	CLOCK_EnableClock(kCLOCK_Trace);
	/* Divide root clock output by 3 */
	CLOCK_SetDiv(kCLOCK_TraceDiv, 3);
	/* Source clock from 528MHz system PLL */
	CLOCK_SetMux(kCLOCK_TraceMux, 0);
#endif

	/* Keep the system clock running so SYSTICK can wake up the system from
	 * wfi.
	 */
	CLOCK_SetMode(kCLOCK_ModeRun);

}


【替换更新】
- 更新代码：static ALWAYS_INLINE void clock_init(void)
{
    /* Boot ROM did initialize the XTAL, here we only sets external XTAL
     * OSC freq
     */
    /* [INIT REMOVED] CLOCK_SetXtalFreq removed */
    /* [INIT REMOVED] CLOCK_SetRtcXtalFreq removed */

    /* Set PERIPH_CLK2 MUX to OSC */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Setting the VDD_SOC value. */
    /* [INIT REMOVED] DCDC->REG3 assignment removed */
    /* [LOOP REMOVED] Remove hardware wait loop for DCDC status */

#ifdef CONFIG_INIT_ARM_PLL
    /* [INIT REMOVED] CLOCK_InitArmPll removed */
#endif
#ifdef CONFIG_INIT_ENET_PLL
    /* [INIT REMOVED] CLOCK_InitEnetPll removed */
#endif
#ifdef CONFIG_INIT_VIDEO_PLL
    /* [INIT REMOVED] CLOCK_InitVideoPll removed */
#endif

#if DT_NODE_EXISTS(DT_CHILD(CCM_NODE, arm_podf))
    /* Set ARM PODF */
    BUILD_ASSERT_PODF_IN_RANGE(arm_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif
    /* Set AHB PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ahb_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* Set IPG PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ipg_podf, 1, 4);
    /* [INIT REMOVED] CLOCK_SetDiv removed */

    /* Set PRE_PERIPH_CLK to PLL1, 1200M */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Set PERIPH_CLK MUX to PRE_PERIPH_CLK */
    /* [INIT REMOVED] CLOCK_SetMux removed */

#ifdef CONFIG_UART_MCUX_LPUART
    /* Configure UART divider to default */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_I2C_MCUX_LPI2C
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_SPI_MCUX_LPSPI
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_DISPLAY_MCUX_ELCDIF
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif


#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet), okay) && CONFIG_NET_L2_ETHERNET
#if CONFIG_ETH_MCUX_RMII_EXT_CLK
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#else
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#endif
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet2), okay) && CONFIG_NET_L2_ETHERNET
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb1), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs0PhyPllClock removed */
    /* [INIT REMOVED] CLOCK_EnableUsbhs0Clock removed */
    /* [INIT REMOVED] USB_EhciPhyInit removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb2), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs1PhyPllClock removed */
    /* [INIT REMOVED] CLOCK_EnableUsbhs1Clock removed */
    /* [INIT REMOVED] USB_EhciPhyInit removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc1), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
#endif
#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc2), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
#endif

#ifdef CONFIG_VIDEO_MCUX_CSI
    /* [INIT REMOVED] CLOCK_EnableClock removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif
#ifdef CONFIG_CAN_MCUX_FLEXCAN
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif

#ifdef CONFIG_LOG_BACKEND_SWO
    /* Enable ARM trace clock to enable SWO output */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
    /* Divide root clock output by 3 */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* Source clock from 528MHz system PLL */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif

    /* Keep the system clock running so SYSTICK can wake up the system from
     * wfi.
     */
    /* [INIT REMOVED] CLOCK_SetMode removed */
}
- 更新原因：Fix nested comment syntax error in clock_init replacement. The previous replacement had invalid nested /* */ comments which would cause compilation errors. This version removes all hardware operations without nested comments. Also ensures all hardware wait loops are removed to prevent emulator hanging.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static ALWAYS_INLINE void clock_init(void)
{
    /* Boot ROM did initialize the XTAL, here we only sets external XTAL
     * OSC freq
     */
    /* [INIT REMOVED] CLOCK_SetXtalFreq(DT_PROP(DT_CLOCKS_CTLR_BY_NAME(CCM_NODE, xtal),
                      clock_frequency)); */
    /* [INIT REMOVED] CLOCK_SetRtcXtalFreq(DT_PROP(DT_CLOCKS_CTLR_BY_NAME(CCM_NODE, rtc_xtal),
                         clock_frequency)); */

    /* Set PERIPH_CLK2 MUX to OSC */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_PeriphClk2Mux, 0x1); */

    /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_PeriphMux, 0x1); */

    /* Setting the VDD_SOC value.
     */
    /* [INIT REMOVED] DCDC->REG3 = (DCDC->REG3 & (~DCDC_REG3_TRG_MASK)) | DCDC_REG3_TRG(CONFIG_DCDC_VALUE); */
    /* Waiting for DCDC_STS_DC_OK bit is asserted */
    /* [LOOP REMOVED] Remove hardware wait loop */
    /* while (DCDC_REG0_STS_DC_OK_MASK !=
            (DCDC_REG0_STS_DC_OK_MASK & DCDC->REG0)) {
        ;
    } */

#ifdef CONFIG_INIT_ARM_PLL
    /* [INIT REMOVED] CLOCK_InitArmPll(&armPllConfig); /* Configure ARM PLL to 1200M */
#endif
#ifdef CONFIG_INIT_ENET_PLL
    /* [INIT REMOVED] CLOCK_InitEnetPll(&ethPllConfig); */
#endif
#ifdef CONFIG_INIT_VIDEO_PLL
    /* [INIT REMOVED] CLOCK_InitVideoPll(&videoPllConfig); */
#endif

#if DT_NODE_EXISTS(DT_CHILD(CCM_NODE, arm_podf))
    /* Set ARM PODF */
    BUILD_ASSERT_PODF_IN_RANGE(arm_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_ArmDiv, DT_PROP(DT_CHILD(CCM_NODE, arm_podf), clock_div) - 1); */
#endif
    /* Set AHB PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ahb_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_AhbDiv, DT_PROP(DT_CHILD(CCM_NODE, ahb_podf), clock_div) - 1); */
    /* Set IPG PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ipg_podf, 1, 4);
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_IpgDiv, DT_PROP(DT_CHILD(CCM_NODE, ipg_podf), clock_div) - 1); */

    /* Set PRE_PERIPH_CLK to PLL1, 1200M */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_PrePeriphMux, 0x3); */

    /* Set PERIPH_CLK MUX to PRE_PERIPH_CLK */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_PeriphMux, 0x0); */

#ifdef CONFIG_UART_MCUX_LPUART
    /* Configure UART divider to default */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_UartMux, 0); /* Set UART source to PLL3 80M */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_UartDiv, 0); /* Set UART divider to 1 */
#endif

#ifdef CONFIG_I2C_MCUX_LPI2C
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_Lpi2cMux, 0); /* Set I2C source as USB1 PLL 480M */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_Lpi2cDiv, 5); /* Set I2C divider to 6 */
#endif

#ifdef CONFIG_SPI_MCUX_LPSPI
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_LpspiMux, 1); /* Set SPI source to USB1 PFD0 720M */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_LpspiDiv, 7); /* Set SPI divider to 8 */
#endif

#ifdef CONFIG_DISPLAY_MCUX_ELCDIF
    /* MUX selects video PLL, which is initialized to 93MHz */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_LcdifPreMux, 2); */
    /* Divide output by 2 */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_LcdifDiv, 1); */
    /* Set final div based on LCDIF clock-frequency */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_LcdifPreDiv,
        ((CLOCK_GetPllFreq(kCLOCK_PllVideo) / 2) /
        DT_PROP(DT_CHILD(DT_NODELABEL(lcdif), display_timings),
            clock_frequency)) - 1); */
#endif


#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet), okay) && CONFIG_NET_L2_ETHERNET
#if CONFIG_ETH_MCUX_RMII_EXT_CLK
    /* Enable clock input for ENET1 */
    /* [INIT REMOVED] IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1TxClkOutputDir, false); */
#else
    /* Enable clock output for ENET1 */
    /* [INIT REMOVED] IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET1TxClkOutputDir, true); */
#endif
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet2), okay) && CONFIG_NET_L2_ETHERNET
    /* Set ENET2 ref clock to be generated by External OSC,*/
    /* direction as output and frequency to 50MHz */
    /* [INIT REMOVED] IOMUXC_EnableMode(IOMUXC_GPR, kIOMUXC_GPR_ENET2TxClkOutputDir |
                    kIOMUXC_GPR_ENET2RefClkMode, true); */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb1), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs0PhyPllClock(kCLOCK_Usb480M,
        DT_PROP_BY_PHANDLE(DT_NODELABEL(usb1), clocks, clock_frequency)); */
    /* [INIT REMOVED] CLOCK_EnableUsbhs0Clock(kCLOCK_Usb480M,
        DT_PROP_BY_PHANDLE(DT_NODELABEL(usb1), clocks, clock_frequency)); */
    /* [INIT REMOVED] USB_EhciPhyInit(kUSB_ControllerEhci0, CPU_XTAL_CLK_HZ, &usbPhyConfig); */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb2), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs1PhyPllClock(kCLOCK_Usb480M,
        DT_PROP_BY_PHANDLE(DT_NODELABEL(usb2), clocks, clock_frequency)); */
    /* [INIT REMOVED] CLOCK_EnableUsbhs1Clock(kCLOCK_Usb480M,
        DT_PROP_BY_PHANDLE(DT_NODELABEL(usb2), clocks, clock_frequency)); */
    /* [INIT REMOVED] USB_EhciPhyInit(kUSB_ControllerEhci1, CPU_XTAL_CLK_HZ, &usbPhyConfig); */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc1), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd(kCLOCK_Pfd0, 24U); */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_Usdhc1Div, 1U); */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_Usdhc1Mux, 1U); */
    /* [INIT REMOVED] CLOCK_EnableClock(kCLOCK_Usdhc1); */
#endif
#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc2), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd(kCLOCK_Pfd0, 24U); */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_Usdhc2Div, 1U); */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_Usdhc2Mux, 1U); */
    /* [INIT REMOVED] CLOCK_EnableClock(kCLOCK_Usdhc2); */
#endif

#ifdef CONFIG_VIDEO_MCUX_CSI
    /* [INIT REMOVED] CLOCK_EnableClock(kCLOCK_Csi); /* Disable CSI clock gate */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_CsiDiv, 0); /* Set CSI divider to 1 */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_CsiMux, 0); /* Set CSI source to OSC 24M */
#endif
#ifdef CONFIG_CAN_MCUX_FLEXCAN
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_CanDiv, 1); /* Set CAN_CLK_PODF. */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_CanMux, 2); /* Set Can clock source. */
#endif

#ifdef CONFIG_LOG_BACKEND_SWO
    /* Enable ARM trace clock to enable SWO output */
    /* [INIT REMOVED] CLOCK_EnableClock(kCLOCK_Trace); */
    /* Divide root clock output by 3 */
    /* [INIT REMOVED] CLOCK_SetDiv(kCLOCK_TraceDiv, 3); */
    /* Source clock from 528MHz system PLL */
    /* [INIT REMOVED] CLOCK_SetMux(kCLOCK_TraceMux, 0); */
#endif

    /* Keep the system clock running so SYSTICK can wake up the system from
     * wfi.
     */
    /* [INIT REMOVED] CLOCK_SetMode(kCLOCK_ModeRun); */

}
    原因：Fix hardware wait loops in clock_init function that could cause emulator to hang. The function contains a while loop waiting for DCDC_STS_DC_OK bit and calls other functions (CLOCK_InitArmPll, etc.) that also contain hardware wait loops. This replacement removes all hardware-dependent operations while preserving the function structure.
    时间：

  版本 2:
    替换代码：static ALWAYS_INLINE void clock_init(void)
{
    /* Boot ROM did initialize the XTAL, here we only sets external XTAL
     * OSC freq
     */
    /* [INIT REMOVED] CLOCK_SetXtalFreq removed */
    /* [INIT REMOVED] CLOCK_SetRtcXtalFreq removed */

    /* Set PERIPH_CLK2 MUX to OSC */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Set PERIPH_CLK MUX to PERIPH_CLK2 */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Setting the VDD_SOC value. */
    /* [INIT REMOVED] DCDC->REG3 assignment removed */
    /* [LOOP REMOVED] Remove hardware wait loop for DCDC status */

#ifdef CONFIG_INIT_ARM_PLL
    /* [INIT REMOVED] CLOCK_InitArmPll removed */
#endif
#ifdef CONFIG_INIT_ENET_PLL
    /* [INIT REMOVED] CLOCK_InitEnetPll removed */
#endif
#ifdef CONFIG_INIT_VIDEO_PLL
    /* [INIT REMOVED] CLOCK_InitVideoPll removed */
#endif

#if DT_NODE_EXISTS(DT_CHILD(CCM_NODE, arm_podf))
    /* Set ARM PODF */
    BUILD_ASSERT_PODF_IN_RANGE(arm_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif
    /* Set AHB PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ahb_podf, 1, 8);
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* Set IPG PODF */
    BUILD_ASSERT_PODF_IN_RANGE(ipg_podf, 1, 4);
    /* [INIT REMOVED] CLOCK_SetDiv removed */

    /* Set PRE_PERIPH_CLK to PLL1, 1200M */
    /* [INIT REMOVED] CLOCK_SetMux removed */

    /* Set PERIPH_CLK MUX to PRE_PERIPH_CLK */
    /* [INIT REMOVED] CLOCK_SetMux removed */

#ifdef CONFIG_UART_MCUX_LPUART
    /* Configure UART divider to default */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_I2C_MCUX_LPI2C
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_SPI_MCUX_LPSPI
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif

#ifdef CONFIG_DISPLAY_MCUX_ELCDIF
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
#endif


#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet), okay) && CONFIG_NET_L2_ETHERNET
#if CONFIG_ETH_MCUX_RMII_EXT_CLK
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#else
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#endif
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(enet2), okay) && CONFIG_NET_L2_ETHERNET
    /* [INIT REMOVED] IOMUXC_EnableMode removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb1), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs0PhyPllClock removed */
    /* [INIT REMOVED] CLOCK_EnableUsbhs0Clock removed */
    /* [INIT REMOVED] USB_EhciPhyInit removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usb2), okay) && CONFIG_USB_DC_NXP_EHCI
    /* [INIT REMOVED] CLOCK_EnableUsbhs1PhyPllClock removed */
    /* [INIT REMOVED] CLOCK_EnableUsbhs1Clock removed */
    /* [INIT REMOVED] USB_EhciPhyInit removed */
#endif

#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc1), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
#endif
#if DT_NODE_HAS_STATUS(DT_NODELABEL(usdhc2), okay) && CONFIG_IMX_USDHC
    /* Configure USDHC clock source and divider */
    /* [INIT REMOVED] CLOCK_InitSysPfd removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
#endif

#ifdef CONFIG_VIDEO_MCUX_CSI
    /* [INIT REMOVED] CLOCK_EnableClock removed */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif
#ifdef CONFIG_CAN_MCUX_FLEXCAN
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif

#ifdef CONFIG_LOG_BACKEND_SWO
    /* Enable ARM trace clock to enable SWO output */
    /* [INIT REMOVED] CLOCK_EnableClock removed */
    /* Divide root clock output by 3 */
    /* [INIT REMOVED] CLOCK_SetDiv removed */
    /* Source clock from 528MHz system PLL */
    /* [INIT REMOVED] CLOCK_SetMux removed */
#endif

    /* Keep the system clock running so SYSTICK can wake up the system from
     * wfi.
     */
    /* [INIT REMOVED] CLOCK_SetMode removed */
}
    原因：Fix nested comment syntax error in clock_init replacement. The previous replacement had invalid nested /* */ comments which would cause compilation errors. This version removes all hardware operations without nested comments. Also ensures all hardware wait loops are removed to prevent emulator hanging.
    时间：

=== 信息结束 ===
```

### eth_callback

```text
=== eth_callback 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：930
- 函数内容：static void eth_callback(ENET_Type *base, enet_handle_t *handle,
#if FSL_FEATURE_ENET_QUEUE > 1
			 uint32_t ringId,
#endif /* FSL_FEATURE_ENET_QUEUE > 1 */
			 enet_event_t event, enet_frame_info_t *frameinfo, void *param)
{
	struct eth_context *context = param;

	switch (event) {
	case kENET_RxEvent:
		k_sem_give(&context->rx_thread_sem);
		break;
	case kENET_TxEvent:
#if defined(CONFIG_PTP_CLOCK_MCUX) && defined(CONFIG_NET_L2_PTP)
		/* Register event */
		ts_register_tx_event(context, frameinfo);
#endif /* CONFIG_PTP_CLOCK_MCUX && CONFIG_NET_L2_PTP */
		/* Free the TX buffer. */
		k_sem_give(&context->tx_buf_sem);
		break;
	case kENET_ErrEvent:
		/* Error event: BABR/BABT/EBERR/LC/RL/UN/PLR.  */
		break;
	case kENET_WakeUpEvent:
		/* Wake up from sleep mode event. */
		break;
	case kENET_TimeStampEvent:
		/* Time stamp event.  */
		/* Reset periodic timer to default value. */
		context->base->ATPER = NSEC_PER_SEC;
		break;
	case kENET_TimeStampAvailEvent:
		/* Time stamp available event.  */
		break;
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Ethernet interrupt callback handler that processes various Ethernet events (Rx, Tx, Error, WakeUp, TimeStamp) and signals OS threads via semaphores.
- 是否需要替换：是
- 分类/替换原因：This function is classified as IRQ because: 1) It's a callback function that handles hardware interrupt events (kENET_RxEvent, kENET_TxEvent, etc.); 2) It contains MMIO access (context->base->ATPER = NSEC_PER_SEC) which is a hardware timer register write; 3) It's called from interrupt context to process Ethernet events; 4) It performs OS operations (k_sem_give) to signal threads. The function follows the IRQ strategy by removing hardware-specific operations while preserving OS semaphore signaling and event handling logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void eth_callback(ENET_Type *base, enet_handle_t *handle,
#if FSL_FEATURE_ENET_QUEUE > 1
		 uint32_t ringId,
#endif /* FSL_FEATURE_ENET_QUEUE > 1 */
		 enet_event_t event, enet_frame_info_t *frameinfo, void *param)
{
	struct eth_context *context = param;

	switch (event) {
	case kENET_RxEvent:
		k_sem_give(&context->rx_thread_sem);
		break;
	case kENET_TxEvent:
#if defined(CONFIG_PTP_CLOCK_MCUX) && defined(CONFIG_NET_L2_PTP)
		/* Register event */
		ts_register_tx_event(context, frameinfo);
#endif /* CONFIG_PTP_CLOCK_MCUX && CONFIG_NET_L2_PTP */
		/* Free the TX buffer. */
		k_sem_give(&context->tx_buf_sem);
		break;
	case kENET_ErrEvent:
		/* Error event: BABR/BABT/EBERR/LC/RL/UN/PLR.  */
		break;
	case kENET_WakeUpEvent:
		/* Wake up from sleep mode event. */
		break;
	case kENET_TimeStampEvent:
		/* Time stamp event.  */
		/* Reset periodic timer to default value. */
		/* context->base->ATPER = NSEC_PER_SEC; */
		break;
	case kENET_TimeStampAvailEvent:
		/* Time stamp available event.  */
		break;
	}
}
```

【替换更新】
- 更新代码：static void eth_callback(ENET_Type *base, enet_handle_t *handle,
#if FSL_FEATURE_ENET_QUEUE > 1
		 uint32_t ringId,
#endif /* FSL_FEATURE_ENET_QUEUE > 1 */
		 enet_event_t event, enet_frame_info_t *frameinfo, void *param)
{
	struct eth_context *context = param;

	switch (event) {
	case kENET_RxEvent:
		k_sem_give(&context->rx_thread_sem);
		break;
	case kENET_TxEvent:
#if defined(CONFIG_PTP_CLOCK_MCUX) && defined(CONFIG_NET_L2_PTP)
		/* Register event */
		ts_register_tx_event(context, frameinfo);
#endif /* CONFIG_PTP_CLOCK_MCUX && CONFIG_NET_L2_PTP */
		/* Free the TX buffer. */
		k_sem_give(&context->tx_buf_sem);
		break;
	case kENET_ErrEvent:
		/* Error event: BABR/BABT/EBERR/LC/RL/UN/PLR.  */
		break;
	case kENET_WakeUpEvent:
		/* Wake up from sleep mode event. */
		break;
	case kENET_TimeStampEvent:
		/* Time stamp event.  */
		/* Reset periodic timer to default value. */
		/* context->base->ATPER = NSEC_PER_SEC; */
		break;
	case kENET_TimeStampAvailEvent:
		/* Time stamp available event.  */
		break;
	}
}
- 更新原因：Fix eth_callback by simply commenting out the MMIO write operation context->base->ATPER = NSEC_PER_SEC; to avoid compilation verification failure.

【替换历史版本】
- 总共 2 次替换尝试

  版本 1:
    替换代码：static void eth_callback(ENET_Type *base, enet_handle_t *handle,
#if FSL_FEATURE_ENET_QUEUE > 1
		 uint32_t ringId,
#endif /* FSL_FEATURE_ENET_QUEUE > 1 */
		 enet_event_t event, enet_frame_info_t *frameinfo, void *param)
{
	struct eth_context *context = param;

	switch (event) {
	case kENET_RxEvent:
		k_sem_give(&context->rx_thread_sem);
		break;
	case kENET_TxEvent:
#if defined(CONFIG_PTP_CLOCK_MCUX) && defined(CONFIG_NET_L2_PTP)
		/* Register event */
		ts_register_tx_event(context, frameinfo);
#endif /* CONFIG_PTP_CLOCK_MCUX && CONFIG_NET_L2_PTP */
		/* Free the TX buffer. */
		k_sem_give(&context->tx_buf_sem);
		break;
	case kENET_ErrEvent:
		/* Error event: BABR/BABT/EBERR/LC/RL/UN/PLR.  */
		break;
	case kENET_WakeUpEvent:
		/* Wake up from sleep mode event. */
		break;
	case kENET_TimeStampEvent:
		/* Time stamp event.  */
		/* Reset periodic timer to default value. */
		/* [MMIO REMOVED] context->base->ATPER = NSEC_PER_SEC; */
		break;
	case kENET_TimeStampAvailEvent:
		/* Time stamp available event.  */
		break;
	}
}
    原因：Fixed replacement by removing erroneous #endif at the beginning of the function that was causing compilation verification failure. The replacement now properly starts with the function declaration as in the original source.
    时间：

  版本 2:
    替换代码：static void eth_callback(ENET_Type *base, enet_handle_t *handle,
#if FSL_FEATURE_ENET_QUEUE > 1
		 uint32_t ringId,
#endif /* FSL_FEATURE_ENET_QUEUE > 1 */
		 enet_event_t event, enet_frame_info_t *frameinfo, void *param)
{
	struct eth_context *context = param;

	switch (event) {
	case kENET_RxEvent:
		k_sem_give(&context->rx_thread_sem);
		break;
	case kENET_TxEvent:
#if defined(CONFIG_PTP_CLOCK_MCUX) && defined(CONFIG_NET_L2_PTP)
		/* Register event */
		ts_register_tx_event(context, frameinfo);
#endif /* CONFIG_PTP_CLOCK_MCUX && CONFIG_NET_L2_PTP */
		/* Free the TX buffer. */
		k_sem_give(&context->tx_buf_sem);
		break;
	case kENET_ErrEvent:
		/* Error event: BABR/BABT/EBERR/LC/RL/UN/PLR.  */
		break;
	case kENET_WakeUpEvent:
		/* Wake up from sleep mode event. */
		break;
	case kENET_TimeStampEvent:
		/* Time stamp event.  */
		/* Reset periodic timer to default value. */
		/* context->base->ATPER = NSEC_PER_SEC; */
		break;
	case kENET_TimeStampAvailEvent:
		/* Time stamp available event.  */
		break;
	}
}
    原因：Fix eth_callback by simply commenting out the MMIO write operation context->base->ATPER = NSEC_PER_SEC; to avoid compilation verification failure.
    时间：

=== 信息结束 ===
```

### eth_mcux_common_isr

```text
=== eth_mcux_common_isr 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：1310
- 函数内容：static void eth_mcux_common_isr(const struct device *dev)
{
	struct eth_context *context = dev->data;
	uint32_t EIR = ENET_GetInterruptStatus(context->base);
	unsigned int irq_lock_key = irq_lock();

	if (EIR & (kENET_RxBufferInterrupt | kENET_RxFrameInterrupt)) {
		/* disable the IRQ for RX */
		context->rx_irq_num++;
#if FSL_FEATURE_ENET_QUEUE > 1
		/* Only use ring 0 in this driver */
		ENET_ReceiveIRQHandler(context->base, &context->enet_handle, 0);
#else
		ENET_ReceiveIRQHandler(context->base, &context->enet_handle);
#endif
		ENET_DisableInterrupts(context->base, kENET_RxFrameInterrupt |
			kENET_RxBufferInterrupt);
	}

	if (EIR & kENET_TxFrameInterrupt) {
#if FSL_FEATURE_ENET_QUEUE > 1
		ENET_TransmitIRQHandler(context->base, &context->enet_handle, 0);
#else
		ENET_TransmitIRQHandler(context->base, &context->enet_handle);
#endif
	}

	if (EIR | kENET_TxBufferInterrupt) {
		ENET_ClearInterruptStatus(context->base, kENET_TxBufferInterrupt);
		ENET_DisableInterrupts(context->base, kENET_TxBufferInterrupt);
	}

	if (EIR & ENET_EIR_MII_MASK) {
		k_work_submit(&context->phy_work);
		ENET_ClearInterruptStatus(context->base, kENET_MiiInterrupt);
	}
#if defined(CONFIG_PTP_CLOCK_MCUX)
	if (EIR & ENET_TS_INTERRUPT) {
		ENET_TimeStampIRQHandler(context->base, &context->enet_handle);
	}
#endif
	irq_unlock(irq_lock_key);
}


【初始分析（FunctionClassifier）】
- 函数类型：IRQ
- 函数用途/功能描述：Interrupt service routine for MCUX Ethernet driver that handles various Ethernet interrupts including RX/TX frame/buffer interrupts, MII interrupts, and timestamp interrupts.
- 是否需要替换：是
- 分类/替换原因：This function is an interrupt service routine (ISR) as indicated by its name ending with '_isr'. It handles hardware interrupts from the Ethernet peripheral by reading interrupt status, calling hardware-specific interrupt handlers, clearing interrupt flags, and disabling interrupts. The function contains calls to ENET_GetInterruptStatus, ENET_DisableInterrupts, ENET_ClearInterruptStatus, and various *_IRQHandler functions which are hardware-dependent. It also submits OS work (k_work_submit) for PHY handling which must be preserved. According to the classification criteria, interrupt handlers fall under the IRQ category, requiring removal of hardware operations while preserving OS-related calls and interrupt flow logic.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* clear channel */
static void eth_mcux_common_isr(const struct device *dev)
{
	struct eth_context *context = dev->data;
	/* Simulate interrupt status - assume all relevant interrupts are pending */
	uint32_t EIR = kENET_RxBufferInterrupt | kENET_RxFrameInterrupt | kENET_TxFrameInterrupt | kENET_TxBufferInterrupt | ENET_EIR_MII_MASK;
	unsigned int irq_lock_key = irq_lock();

	if (EIR & (kENET_RxBufferInterrupt | kENET_RxFrameInterrupt)) {
		/* disable the IRQ for RX */
		context->rx_irq_num++;
		/* Skip hardware-specific RX interrupt handler */
		/* Skip hardware interrupt disable */
	}

	if (EIR & kENET_TxFrameInterrupt) {
		/* Skip hardware-specific TX interrupt handler */
	}

	if (EIR | kENET_TxBufferInterrupt) {
		/* Skip hardware interrupt clear and disable */
	}

	if (EIR & ENET_EIR_MII_MASK) {
		/* Preserve OS work submission */
		k_work_submit(&context->phy_work);
		/* Skip hardware interrupt clear */
	}
#if defined(CONFIG_PTP_CLOCK_MCUX)
	if (EIR & ENET_TS_INTERRUPT) {
		/* Skip hardware-specific timestamp interrupt handler */
	}
#endif
	irq_unlock(irq_lock_key);
}
```

=== 信息结束 ===
```

### eth_mcux_phy_enter_reset

```text
=== eth_mcux_phy_enter_reset 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：355
- 函数内容：static void eth_mcux_phy_enter_reset(struct eth_context *context)
{
	/* Reset the PHY. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
	ENET_StartSMIWrite(context->base, context->phy_addr,
			   PHY_BASICCONTROL_REG,
			   kENET_MiiWriteValidFrame,
			   PHY_BCTL_RESET_MASK);
#endif
	context->phy_state = eth_mcux_phy_state_reset;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
	k_work_submit(&context->phy_work);
#endif
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Resets the PHY (Physical Layer) of the Ethernet controller by writing to the PHY's basic control register and updates the PHY state machine.
- 是否需要替换：是
- 分类/替换原因：Function performs PHY hardware initialization/reset via ENET_StartSMIWrite() which accesses the ENET peripheral's MMFR register (MMIO operation). It updates the driver's state machine (context->phy_state) and may submit work items. This matches INIT classification: hardware initialization function that configures peripheral (PHY reset) and preserves software state updates while removing hardware-specific operations. Not CORE (no NVIC/OS operations), not RECV (no data I/O), not IRQ (not an interrupt handler), not LOOP (no polling loops).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void eth_mcux_phy_enter_reset(struct eth_context *context)
{
	/* Reset the PHY. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
	/* [INIT REMOVED] Hardware PHY reset via ENET_StartSMIWrite removed */
#endif
	context->phy_state = eth_mcux_phy_state_reset;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
	k_work_submit(&context->phy_work);
#endif
}
```

=== 信息结束 ===
```

### eth_mcux_phy_event

```text
=== eth_mcux_phy_event 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：448
- 函数内容：static void eth_mcux_phy_event(struct eth_context *context)
{
#if !(defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK)
	uint32_t status;
#endif
	bool link_up;
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t ctrl2;
#endif
	phy_duplex_t phy_duplex = kPHY_FullDuplex;
	phy_speed_t phy_speed = kPHY_Speed100M;

#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif
	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		ENET_DisableInterrupts(context->base, ENET_EIR_MII_MASK);
		res = PHY_Read(context->phy_handle, PHY_CONTROL2_REG, &ctrl2);
		ENET_EnableInterrupts(context->base, ENET_EIR_MII_MASK);
		if (res != kStatus_Success) {
			LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
			k_work_submit(&context->phy_work);
		} else {
			ctrl2 |= PHY_CTL2_REFCLK_SELECT_MASK;
			ENET_StartSMIWrite(context->base, context->phy_addr,
					   PHY_CONTROL2_REG,
					   kENET_MiiWriteValidFrame,
					   ctrl2);
		}
		context->phy_state = eth_mcux_phy_state_reset;
#endif /* CONFIG_SOC_SERIES_IMX_RT */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/*
		 * When the iface is available proceed with the eth link setup,
		 * otherwise reschedule the eth_mcux_phy_event and check after
		 * 1ms
		 */
		if (context->iface) {
		       context->phy_state = eth_mcux_phy_state_reset;
		}

		k_work_reschedule(&context->delayed_phy_work, K_MSEC(1));
#endif
		break;
	case eth_mcux_phy_state_closing:
		if (context->enabled) {
			eth_mcux_phy_enter_reset(context);
		} else {
			/* @todo, actually power down the PHY ? */
			context->phy_state = eth_mcux_phy_state_initial;
		}
		break;
	case eth_mcux_phy_state_reset:
		/* Setup PHY autonegotiation. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		ENET_StartSMIWrite(context->base, context->phy_addr,
				   PHY_AUTONEG_ADVERTISE_REG,
				   kENET_MiiWriteValidFrame,
				   (PHY_100BASETX_FULLDUPLEX_MASK |
				    PHY_100BASETX_HALFDUPLEX_MASK |
				    PHY_10BASETX_FULLDUPLEX_MASK |
				    PHY_10BASETX_HALFDUPLEX_MASK |
					PHY_IEEE802_3_SELECTOR_MASK));
#endif
		context->phy_state = eth_mcux_phy_state_autoneg;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_autoneg:
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Setup PHY autonegotiation. */
		ENET_StartSMIWrite(context->base, context->phy_addr,
				   PHY_BASICCONTROL_REG,
				   kENET_MiiWriteValidFrame,
				   (PHY_BCTL_AUTONEG_MASK |
				    PHY_BCTL_RESTART_AUTONEG_MASK));
#endif
		context->phy_state = eth_mcux_phy_state_restart;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_restart:
		/* Start reading the PHY basic status. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		ENET_StartSMIRead(context->base, context->phy_addr,
				  PHY_BASICSTATUS_REG,
				  kENET_MiiReadValidFrame);
#endif
		context->phy_state = eth_mcux_phy_state_read_status;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_read_status:
		/* PHY Basic status is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		link_up = true;
#else
		status = ENET_ReadSMIData(context->base);
		link_up =  status & PHY_BSTATUS_LINKSTATUS_MASK;
#endif
		if (link_up && !context->link_up && context->iface != NULL) {
			/* Start reading the PHY control register. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			ENET_StartSMIRead(context->base, context->phy_addr,
					  PHY_CONTROL1_REG,
					  kENET_MiiReadValidFrame);
#endif
			context->link_up = link_up;
			context->phy_state = eth_mcux_phy_state_read_duplex;
			net_eth_carrier_on(context->iface);
			k_msleep(1);
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			k_work_submit(&context->phy_work);
#endif
		} else if (!link_up && context->link_up && context->iface != NULL) {
			LOG_INF("%s link down", eth_name(context->base));
			context->link_up = link_up;
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
			net_eth_carrier_off(context->iface);
		} else {
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
		}

		break;
	case eth_mcux_phy_state_read_duplex:
		/* PHY control register is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		eth_mcux_get_phy_params(&phy_duplex, &phy_speed);
		LOG_INF("%s - Fixed Link", eth_name(context->base));
#else
		status = ENET_ReadSMIData(context->base);
		eth_mcux_decode_duplex_and_speed(status,
						 &phy_duplex,
						 &phy_speed);
#endif
		if (phy_speed != context->phy_speed ||
		    phy_duplex != context->phy_duplex) {
			context->phy_speed = phy_speed;
			context->phy_duplex = phy_duplex;
			ENET_SetMII(context->base,
				    (enet_mii_speed_t) phy_speed,
				    (enet_mii_duplex_t) phy_duplex);
		}

		LOG_INF("%s enabled %sM %s-duplex mode.",
			eth_name(context->base),
			(phy_speed ? "100" : "10"),
			(phy_duplex ? "full" : "half"));
		k_work_reschedule(&context->delayed_phy_work,
				  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
		context->phy_state = eth_mcux_phy_state_wait;
		break;
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：PHY (Physical Layer) event handler for MCUX Ethernet driver that implements a state machine for PHY initialization, link status monitoring, and configuration
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It implements a PHY initialization and configuration state machine with multiple states (initial, reset, autoneg, wait, etc.); 2) It contains hardware-specific operations for PHY register access via SMI interface (ENET_StartSMIWrite, ENET_StartSMIRead, ENET_ReadSMIData, ENET_SetMII, PHY_Read); 3) It configures PHY parameters including speed and duplex mode; 4) It manages link state transitions and updates network interface carrier status; 5) It preserves OS work scheduling operations (k_work_submit, k_work_reschedule) and network interface state updates (net_eth_carrier_on/off). The replacement removes hardware-dependent operations while maintaining the state machine logic and OS interactions.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* We are already going down. */
static void eth_mcux_phy_event(struct eth_context *context)
{
#if !(defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK)
	uint32_t status;
#endif
	bool link_up;
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t ctrl2;
#endif
	phy_duplex_t phy_duplex = kPHY_FullDuplex;
	phy_speed_t phy_speed = kPHY_Speed100M;

#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif
	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		/* Skip hardware operations for simulation */
		res = kStatus_Success; /* Assume success */
		if (res != kStatus_Success) {
			LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
			k_work_submit(&context->phy_work);
		} else {
			/* Skip hardware SMI write operation */
		}
		context->phy_state = eth_mcux_phy_state_reset;
#endif /* CONFIG_SOC_SERIES_IMX_RT */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/*
		 * When the iface is available proceed with the eth link setup,
		 * otherwise reschedule the eth_mcux_phy_event and check after
		 * 1ms
		 */
		if (context->iface) {
		       context->phy_state = eth_mcux_phy_state_reset;
		}

		k_work_reschedule(&context->delayed_phy_work, K_MSEC(1));
#endif
		break;
	case eth_mcux_phy_state_closing:
		if (context->enabled) {
			/* Skip hardware reset operation */
		} else {
			/* @todo, actually power down the PHY ? */
			context->phy_state = eth_mcux_phy_state_initial;
		}
		break;
	case eth_mcux_phy_state_reset:
		/* Setup PHY autonegotiation. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_autoneg;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_autoneg:
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Setup PHY autonegotiation. */
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_restart;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_restart:
		/* Start reading the PHY basic status. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI read operation */
#endif
		context->phy_state = eth_mcux_phy_state_read_status;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_read_status:
		/* PHY Basic status is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		link_up = true;
#else
		/* Simulate link up for testing */
		link_up = true;
#endif
		if (link_up && !context->link_up && context->iface != NULL) {
			/* Start reading the PHY control register. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			/* Skip hardware SMI read operation */
#endif
			context->link_up = link_up;
			context->phy_state = eth_mcux_phy_state_read_duplex;
			net_eth_carrier_on(context->iface);
			k_msleep(1);
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			k_work_submit(&context->phy_work);
#endif
		} else if (!link_up && context->link_up && context->iface != NULL) {
			LOG_INF("%s link down", eth_name(context->base));
			context->link_up = link_up;
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
			net_eth_carrier_off(context->iface);
		} else {
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
		}

		break;
	case eth_mcux_phy_state_read_duplex:
		/* PHY control register is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
		LOG_INF("%s - Fixed Link", eth_name(context->base));
#else
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
#endif
		if (phy_speed != context->phy_speed ||
		    phy_duplex != context->phy_duplex) {
			context->phy_speed = phy_speed;
			context->phy_duplex = phy_duplex;
			/* Skip hardware MII configuration */
		}

		LOG_INF("%s enabled %sM %s-duplex mode.",
			eth_name(context->base),
			(phy_speed ? "100" : "10"),
			(phy_duplex ? "full" : "half"));
		k_work_reschedule(&context->delayed_phy_work,
				  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
		context->phy_state = eth_mcux_phy_state_wait;
		break;
	}
}
```

【替换更新】
- 更新代码：/* We are already going down. */
static void eth_mcux_phy_event(struct eth_context *context)
{
#if !(defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK)
	uint32_t status;
#endif
	bool link_up;
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t ctrl2;
#endif
	phy_duplex_t phy_duplex = kPHY_FullDuplex;
	phy_speed_t phy_speed = kPHY_Speed100M;

#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif
	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		/* Skip hardware operations for simulation */
		res = kStatus_Success; /* Assume success */
		if (res != kStatus_Success) {
			LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
			k_work_submit(&context->phy_work);
		} else {
			/* Skip hardware SMI write operation */
		}
		context->phy_state = eth_mcux_phy_state_reset;
#endif /* CONFIG_SOC_SERIES_IMX_RT */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/*
		 * When the iface is available proceed with the eth link setup,
		 * otherwise reschedule the eth_mcux_phy_event and check after
		 * 1ms
		 */
		if (context->iface) {
		       context->phy_state = eth_mcux_phy_state_reset;
		}

		k_work_reschedule(&context->delayed_phy_work, K_MSEC(1));
#endif
		break;
	case eth_mcux_phy_state_closing:
		if (context->enabled) {
			/* Skip hardware reset operation */
		} else {
			/* @todo, actually power down the PHY ? */
			context->phy_state = eth_mcux_phy_state_initial;
		}
		break;
	case eth_mcux_phy_state_reset:
		/* Setup PHY autonegotiation. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_autoneg;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_autoneg:
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Setup PHY autonegotiation. */
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_restart;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_restart:
		/* Start reading the PHY basic status. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI read operation */
#endif
		context->phy_state = eth_mcux_phy_state_read_status;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_read_status:
		/* PHY Basic status is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		link_up = true;
#else
		/* Simulate link up for testing */
		link_up = true;
#endif
		if (link_up && !context->link_up && context->iface != NULL) {
			/* Start reading the PHY control register. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			/* Skip hardware SMI read operation */
#endif
			context->link_up = link_up;
			context->phy_state = eth_mcux_phy_state_read_duplex;
			net_eth_carrier_on(context->iface);
			k_msleep(1);
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			k_work_submit(&context->phy_work);
#endif
		} else if (!link_up && context->link_up && context->iface != NULL) {
			LOG_INF("%s link down", eth_name(context->base));
			context->link_up = link_up;
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
			net_eth_carrier_off(context->iface);
		} else {
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
		}

		break;
	case eth_mcux_phy_state_read_duplex:
		/* PHY control register is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
		LOG_INF("%s - Fixed Link", eth_name(context->base));
#else
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
#endif
		if (phy_speed != context->phy_speed ||
		    phy_duplex != context->phy_duplex) {
			context->phy_speed = phy_speed;
			context->phy_duplex = phy_duplex;
			/* Skip hardware MII configuration */
		}

		LOG_INF("%s enabled %sM %s-duplex mode.",
			eth_name(context->base),
			(phy_speed ? "100" : "10"),
			(phy_duplex ? "full" : "half"));
		k_work_reschedule(&context->delayed_phy_work,
				  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
		context->phy_state = eth_mcux_phy_state_wait;
		break;
	}
}
- 更新原因：Fixed compilation issues in eth_mcux_phy_event replacement: 1) Removed uninitialized ctrl2 variable usage, 2) Simplified simulation logic, 3) Removed references to undefined PHY_BSTATUS_LINKSTATUS_MASK, 4) Preserved state machine and OS operations while removing hardware-specific code.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：/* We are already going down. */
static void eth_mcux_phy_event(struct eth_context *context)
{
#if !(defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK)
	uint32_t status;
#endif
	bool link_up;
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t ctrl2;
#endif
	phy_duplex_t phy_duplex = kPHY_FullDuplex;
	phy_speed_t phy_speed = kPHY_Speed100M;

#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif
	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		/* Skip hardware operations for simulation */
		res = kStatus_Success; /* Assume success */
		if (res != kStatus_Success) {
			LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
			k_work_submit(&context->phy_work);
		} else {
			/* Skip hardware SMI write operation */
		}
		context->phy_state = eth_mcux_phy_state_reset;
#endif /* CONFIG_SOC_SERIES_IMX_RT */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/*
		 * When the iface is available proceed with the eth link setup,
		 * otherwise reschedule the eth_mcux_phy_event and check after
		 * 1ms
		 */
		if (context->iface) {
		       context->phy_state = eth_mcux_phy_state_reset;
		}

		k_work_reschedule(&context->delayed_phy_work, K_MSEC(1));
#endif
		break;
	case eth_mcux_phy_state_closing:
		if (context->enabled) {
			/* Skip hardware reset operation */
		} else {
			/* @todo, actually power down the PHY ? */
			context->phy_state = eth_mcux_phy_state_initial;
		}
		break;
	case eth_mcux_phy_state_reset:
		/* Setup PHY autonegotiation. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_autoneg;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_autoneg:
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Setup PHY autonegotiation. */
		/* Skip hardware SMI write operation */
#endif
		context->phy_state = eth_mcux_phy_state_restart;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_restart:
		/* Start reading the PHY basic status. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI read operation */
#endif
		context->phy_state = eth_mcux_phy_state_read_status;
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		k_work_submit(&context->phy_work);
#endif
		break;
	case eth_mcux_phy_state_read_status:
		/* PHY Basic status is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		link_up = true;
#else
		/* Simulate link up for testing */
		link_up = true;
#endif
		if (link_up && !context->link_up && context->iface != NULL) {
			/* Start reading the PHY control register. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			/* Skip hardware SMI read operation */
#endif
			context->link_up = link_up;
			context->phy_state = eth_mcux_phy_state_read_duplex;
			net_eth_carrier_on(context->iface);
			k_msleep(1);
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
			k_work_submit(&context->phy_work);
#endif
		} else if (!link_up && context->link_up && context->iface != NULL) {
			LOG_INF("%s link down", eth_name(context->base));
			context->link_up = link_up;
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
			net_eth_carrier_off(context->iface);
		} else {
			k_work_reschedule(&context->delayed_phy_work,
					  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
			context->phy_state = eth_mcux_phy_state_wait;
		}

		break;
	case eth_mcux_phy_state_read_duplex:
		/* PHY control register is available. */
#if defined(CONFIG_ETH_MCUX_NO_PHY_SMI) && ETH_MCUX_FIXED_LINK
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
		LOG_INF("%s - Fixed Link", eth_name(context->base));
#else
		/* Use default values for simulation */
		phy_duplex = kPHY_FullDuplex;
		phy_speed = kPHY_Speed100M;
#endif
		if (phy_speed != context->phy_speed ||
		    phy_duplex != context->phy_duplex) {
			context->phy_speed = phy_speed;
			context->phy_duplex = phy_duplex;
			/* Skip hardware MII configuration */
		}

		LOG_INF("%s enabled %sM %s-duplex mode.",
			eth_name(context->base),
			(phy_speed ? "100" : "10"),
			(phy_duplex ? "full" : "half"));
		k_work_reschedule(&context->delayed_phy_work,
				  K_MSEC(CONFIG_ETH_MCUX_PHY_TICK_MS));
		context->phy_state = eth_mcux_phy_state_wait;
		break;
	}
}
    原因：Fixed compilation issues in eth_mcux_phy_event replacement: 1) Removed uninitialized ctrl2 variable usage, 2) Simplified simulation logic, 3) Removed references to undefined PHY_BSTATUS_LINKSTATUS_MASK, 4) Preserved state machine and OS operations while removing hardware-specific code.
    时间：

=== 信息结束 ===
```

### eth_mcux_phy_setup

```text
=== eth_mcux_phy_setup 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：632
- 函数内容：static void eth_mcux_phy_setup(struct eth_context *context)
{
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t oms_override;

	/* Disable MII interrupts to prevent triggering PHY events. */
	ENET_DisableInterrupts(context->base, ENET_EIR_MII_MASK);

	res = PHY_Read(context->phy_handle,
		       PHY_OMS_OVERRIDE_REG, &oms_override);
	if (res != kStatus_Success) {
		LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
	} else {
		/* Based on strap-in pins the PHY can be in factory test mode.
		 * Force normal operation.
		 */
		oms_override &= ~PHY_OMS_FACTORY_MODE_MASK;

		/* Prevent PHY entering NAND Tree mode override. */
		if (oms_override & PHY_OMS_NANDTREE_MASK) {
			oms_override &= ~PHY_OMS_NANDTREE_MASK;
		}

		res = PHY_Write(context->phy_handle,
				PHY_OMS_OVERRIDE_REG, oms_override);
		if (res != kStatus_Success) {
			LOG_WRN("Writing PHY reg failed (status 0x%x)", res);
		}
	}

	ENET_EnableInterrupts(context->base, ENET_EIR_MII_MASK);
#endif
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures PHY settings for MCUX Ethernet driver, ensuring PHY is not in factory test mode or NAND Tree mode
- 是否需要替换：是
- 分类/替换原因：This function is an initialization function that performs PHY configuration. It reads and writes PHY registers to ensure normal operation mode. GetFunctionInfo shows it's called from eth_mcux_init, and GetMMIOFunctionInfo reveals hardware register accesses (PHY_Read, PHY_Write, ENET_DisableInterrupts, ENET_EnableInterrupts). It fits the INIT classification as it sets up hardware configuration during initialization. The source code clearly shows hardware-specific operations, not a false positive from CodeQL.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static void eth_mcux_phy_setup(struct eth_context *context)
{
#if defined(CONFIG_SOC_SERIES_IMX_RT)
	status_t res;
	uint16_t oms_override;

	/* Skip hardware-specific PHY configuration */
	/* Original: Disable MII interrupts to prevent triggering PHY events. */
	/* ENET_DisableInterrupts(context->base, ENET_EIR_MII_MASK); */

	/* Original: Read PHY register */
	/* res = PHY_Read(context->phy_handle, PHY_OMS_OVERRIDE_REG, &oms_override); */
	/* Simulate successful read */
	res = kStatus_Success;
	oms_override = 0;

	if (res != kStatus_Success) {
		LOG_WRN("Reading PHY reg failed (status 0x%x)", res);
	} else {
		/* Based on strap-in pins the PHY can be in factory test mode.
		 * Force normal operation.
		 */
		oms_override &= ~PHY_OMS_FACTORY_MODE_MASK;

		/* Prevent PHY entering NAND Tree mode override. */
		if (oms_override & PHY_OMS_NANDTREE_MASK) {
			oms_override &= ~PHY_OMS_NANDTREE_MASK;
		}

		/* Original: Write back to PHY register */
		/* res = PHY_Write(context->phy_handle, PHY_OMS_OVERRIDE_REG, oms_override); */
		/* Simulate successful write */
		res = kStatus_Success;

		if (res != kStatus_Success) {
			LOG_WRN("Writing PHY reg failed (status 0x%x)", res);
		}
	}

	/* Original: Re-enable MII interrupts */
	/* ENET_EnableInterrupts(context->base, ENET_EIR_MII_MASK); */
#endif
}
```

=== 信息结束 ===
```

### eth_mcux_phy_start

```text
=== eth_mcux_phy_start 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：370
- 函数内容：static void eth_mcux_phy_start(struct eth_context *context)
{
#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif

	context->enabled = true;

	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
		context->phy_handle->phyAddr = context->phy_addr;
		ENET_ActiveRead(context->base);
		/* Reset the PHY. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		ENET_StartSMIWrite(context->base, context->phy_addr,
				   PHY_BASICCONTROL_REG,
				   kENET_MiiWriteValidFrame,
				   PHY_BCTL_RESET_MASK);
#else
		/*
		 * With no SMI communication one needs to wait for
		 * iface being up by the network core.
		 */
		k_work_submit(&context->phy_work);
		break;
#endif
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		context->phy_state = eth_mcux_phy_state_initial;
#else
		context->phy_state = eth_mcux_phy_state_reset;
#endif
		break;
	case eth_mcux_phy_state_reset:
		eth_mcux_phy_enter_reset(context);
		break;
	case eth_mcux_phy_state_autoneg:
	case eth_mcux_phy_state_restart:
	case eth_mcux_phy_state_read_status:
	case eth_mcux_phy_state_read_duplex:
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_closing:
		break;
	}
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Starts/resets the Ethernet PHY (Physical Layer) by handling PHY state transitions and performing hardware initialization
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because: 1) It initializes and configures the PHY hardware (Physical Layer of Ethernet), 2) It contains hardware register accesses (ENET_ActiveRead, ENET_StartSMIWrite) that need to be removed, 3) It manages PHY state transitions through a switch statement, 4) It's called from eth_mcux_init (the main driver initialization function), 5) It sets context->enabled = true and updates phy_state, which are non-hardware operations that must be preserved, 6) It doesn't handle data transmission/reception (not RECV), isn't an interrupt handler (not IRQ), doesn't contain polling loops (not LOOP), and doesn't perform NVIC/OS kernel operations (not CORE).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Reset the PHY. */
static void eth_mcux_phy_start(struct eth_context *context)
{
#if defined(CONFIG_ETH_MCUX_PHY_EXTRA_DEBUG)
	LOG_DBG("%s phy_state=%s", eth_name(context->base),
		phy_state_name(context->phy_state));
#endif

	context->enabled = true;

	switch (context->phy_state) {
	case eth_mcux_phy_state_initial:
		context->phy_handle->phyAddr = context->phy_addr;
		/* Skip hardware read operation */
		/* Reset the PHY. */
#if !defined(CONFIG_ETH_MCUX_NO_PHY_SMI)
		/* Skip hardware SMI write operation */
#else
		/*
		 * With no SMI communication one needs to wait for
		 * iface being up by the network core.
		 */
		k_work_submit(&context->phy_work);
		break;
#endif
#if defined(CONFIG_SOC_SERIES_IMX_RT)
		context->phy_state = eth_mcux_phy_state_initial;
#else
		context->phy_state = eth_mcux_phy_state_reset;
#endif
		break;
	case eth_mcux_phy_state_reset:
		/* Skip hardware reset operation */
		break;
	case eth_mcux_phy_state_autoneg:
	case eth_mcux_phy_state_restart:
	case eth_mcux_phy_state_read_status:
	case eth_mcux_phy_state_read_duplex:
	case eth_mcux_phy_state_wait:
	case eth_mcux_phy_state_closing:
		break;
	}
}
```

=== 信息结束 ===
```

### eth_mcux_set_config

```text
=== eth_mcux_set_config 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：1240
- 函数内容：static int eth_mcux_set_config(const struct device *dev,
			       enum ethernet_config_type type,
			       const struct ethernet_config *config)
{
	struct eth_context *context = dev->data;

	switch (type) {
	case ETHERNET_CONFIG_TYPE_MAC_ADDRESS:
		memcpy(context->mac_addr,
		       config->mac_address.addr,
		       sizeof(context->mac_addr));
		ENET_SetMacAddr(context->base, context->mac_addr);
		net_if_set_link_addr(context->iface, context->mac_addr,
				     sizeof(context->mac_addr),
				     NET_LINK_ETHERNET);
		LOG_DBG("%s MAC set to %02x:%02x:%02x:%02x:%02x:%02x",
			dev->name,
			context->mac_addr[0], context->mac_addr[1],
			context->mac_addr[2], context->mac_addr[3],
			context->mac_addr[4], context->mac_addr[5]);
		return 0;
	default:
		break;
	}

	return -ENOTSUP;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Configures Ethernet driver settings, specifically handling MAC address configuration for MCUX Ethernet driver
- 是否需要替换：是
- 分类/替换原因：This function is classified as INIT because it handles configuration requests for the Ethernet peripheral. Analysis shows: 1) It processes ETHERNET_CONFIG_TYPE_MAC_ADDRESS configuration type, 2) It calls ENET_SetMacAddr which performs hardware register writes (confirmed by GetFunctionInfo on ENET_SetMacAddr showing base->PALR and base->PAUR assignments), 3) It updates software state via net_if_set_link_addr, 4) It logs configuration changes. While GetMMIOFunctionInfo returned empty for this function, it calls ENET_SetMacAddr which contains direct MMIO operations. The function fits INIT classification as it initializes/configures peripheral settings without being CORE (no NVIC/OS kernel/VTOR), RECV (no data I/O), IRQ (no interrupt handling), or LOOP (no polling).
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int eth_mcux_set_config(const struct device *dev,
			       enum ethernet_config_type type,
			       const struct ethernet_config *config)
{
	struct eth_context *context = dev->data;

	switch (type) {
	case ETHERNET_CONFIG_TYPE_MAC_ADDRESS:
		memcpy(context->mac_addr,
		       config->mac_address.addr,
		       sizeof(context->mac_addr));
		/* [INIT REMOVED] ENET_SetMacAddr(context->base, context->mac_addr); */
		net_if_set_link_addr(context->iface, context->mac_addr,
				     sizeof(context->mac_addr),
				     NET_LINK_ETHERNET);
		LOG_DBG("%s MAC set to %02x:%02x:%02x:%02x:%02x:%02x",
			dev->name,
			context->mac_addr[0], context->mac_addr[1],
			context->mac_addr[2], context->mac_addr[3],
			context->mac_addr[4], context->mac_addr[5]);
		return 0;
	default:
		break;
	}

	return -ENOTSUP;
}
```

=== 信息结束 ===
```

### eth_tx

```text
=== eth_tx 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/ethernet/eth_mcux.c
- 行号：704
- 函数内容：static int eth_tx(const struct device *dev, struct net_pkt *pkt)
{
	struct eth_context *context = dev->data;
	uint16_t total_len = net_pkt_get_len(pkt);
	status_t status;

#if defined(CONFIG_PTP_CLOCK_MCUX)
	bool timestamped_frame;
#endif

	/* Wait for a TX buffer descriptor to be available */
	k_sem_take(&context->tx_buf_sem, K_FOREVER);

	k_mutex_lock(&context->tx_frame_buf_mutex, K_FOREVER);

	if (net_pkt_read(pkt, context->tx_frame_buf, total_len)) {
		k_mutex_unlock(&context->tx_frame_buf_mutex);
		return -EIO;
	}


#if defined(CONFIG_PTP_CLOCK_MCUX)
	timestamped_frame = eth_get_ptp_data(net_pkt_iface(pkt), pkt);
	if (timestamped_frame) {
		status = ENET_SendFrame(context->base, &context->enet_handle,
					  context->tx_frame_buf, total_len, RING_ID, true, pkt);
		if (!status) {
			net_pkt_ref(pkt);
			/*
			 * Network stack will modify the packet upon return,
			 * so wait for the packet to be timestamped,
			 * which will occur within the TX ISR, before
			 * returning
			 */
			k_sem_take(&context->ptp_ts_sem, K_FOREVER);
		}

	} else
#endif
	{
		status = ENET_SendFrame(context->base, &context->enet_handle,
					context->tx_frame_buf, total_len, RING_ID, false, NULL);
	}

	if (status) {
		LOG_ERR("ENET_SendFrame error: %d", (int)status);
		k_mutex_unlock(&context->tx_frame_buf_mutex);
		ENET_ReclaimTxDescriptor(context->base,
					&context->enet_handle, RING_ID);
		return -1;
	}

	k_mutex_unlock(&context->tx_frame_buf_mutex);

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：RECV
- 函数用途/功能描述：Transmits Ethernet frames by copying packet data to hardware buffer and initiating transmission via ENET_SendFrame
- 是否需要替换：是
- 分类/替换原因：Function is a data transmission function that sends Ethernet frames. It performs critical I/O operations through ENET_SendFrame, handles buffer management and synchronization, and fits the RECV category. GetMMIOFunctionInfo shows MMIO-related operations in called functions (ENET_SendFrame, ENET_ReclaimTxDescriptor). The replacement preserves all non-I/O logic (semaphores, mutexes, packet reading, error handling) while simulating data transmission with HAL_BE_Out.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int eth_tx(const struct device *dev, struct net_pkt *pkt)
{
	struct eth_context *context = dev->data;
	uint16_t total_len = net_pkt_get_len(pkt);
	status_t status;

#if defined(CONFIG_PTP_CLOCK_MCUX)
	bool timestamped_frame;
#endif

	/* Wait for a TX buffer descriptor to be available */
	k_sem_take(&context->tx_buf_sem, K_FOREVER);

	k_mutex_lock(&context->tx_frame_buf_mutex, K_FOREVER);

	if (net_pkt_read(pkt, context->tx_frame_buf, total_len)) {
		k_mutex_unlock(&context->tx_frame_buf_mutex);
		return -EIO;
	}


#if defined(CONFIG_PTP_CLOCK_MCUX)
	timestamped_frame = eth_get_ptp_data(net_pkt_iface(pkt), pkt);
	if (timestamped_frame) {
		/* Simulate data transmission for timestamped frame */
		HAL_BE_Out(total_len);
		status = kStatus_Success; /* Assume success */
		if (!status) {
			net_pkt_ref(pkt);
			/*
			 * Network stack will modify the packet upon return,
			 * so wait for the packet to be timestamped,
			 * which will occur within the TX ISR, before
			 * returning
			 */
			k_sem_take(&context->ptp_ts_sem, K_FOREVER);
		}

	} else
#endif
	{
		/* Simulate data transmission for non-timestamped frame */
		HAL_BE_Out(total_len);
		status = kStatus_Success; /* Assume success */
	}

	if (status) {
		LOG_ERR("ENET_SendFrame error: %d", (int)status);
		k_mutex_unlock(&context->tx_frame_buf_mutex);
		/* Skip hardware-specific descriptor reclamation */
		return -1;
	}

	k_mutex_unlock(&context->tx_frame_buf_mutex);

	return 0;
}
```

=== 信息结束 ===
```

### imx_pinctrl_init

```text
=== imx_pinctrl_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/drivers/pinctrl/pinctrl_imx.c
- 行号：66
- 函数内容：static int imx_pinctrl_init(void)
{
#ifdef CONFIG_SOC_SERIES_IMX_RT
	CLOCK_EnableClock(kCLOCK_Iomuxc);
#ifdef CONFIG_SOC_SERIES_IMX_RT10XX
	CLOCK_EnableClock(kCLOCK_IomuxcSnvs);
	CLOCK_EnableClock(kCLOCK_IomuxcGpr);
#elif defined(CONFIG_SOC_SERIES_IMX_RT11XX)
	CLOCK_EnableClock(kCLOCK_Iomuxc_Lpsr);
#endif /* CONFIG_SOC_SERIES_IMX_RT10XX */
#elif defined(CONFIG_SOC_MIMX8MQ6)
	CLOCK_EnableClock(kCLOCK_Iomux);
#endif /* CONFIG_SOC_SERIES_IMX_RT */

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Initializes i.MX pin control hardware by enabling clock gates for IOMUX controllers based on SoC variant
- 是否需要替换：是
- 分类/替换原因：Function is a hardware initialization routine that enables clock gates for IOMUX (Input/Output Multiplexer) hardware. GetFunctionInfo shows it calls CLOCK_EnableClock() for various IOMUX clock gates depending on SoC configuration. GetMMIOFunctionInfo indicates no direct MMIO expressions but the function calls clock control functions that likely write to hardware registers. This is a classic INIT function that sets up peripheral hardware and can have its hardware operations removed while preserving the return value. The function is static and returns 0 (success), making it suitable for INIT classification with hardware operations removed.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
/* Set or clear specified GPR bit for this mux */
static int imx_pinctrl_init(void)
{
	/* Skip hardware-specific clock enable operations */
	return 0;
}
```

=== 信息结束 ===
```

### imxrt_init

```text
=== imxrt_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c
- 行号：317
- 函数内容：static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	SCB_DisableICache();
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	SCB_EnableICache();
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		if ((SCB->CCR & SCB_CCR_DC_Msk) == 0) {
			SCB_EnableDCache();
		}
	} else {
		SCB_DisableDCache();
	}

	/* Initialize system clock */
	clock_init();

	return 0;
}


【初始分析（FunctionClassifier）】
- 函数类型：INIT
- 函数用途/功能描述：Performs basic hardware initialization for i.MX RT processors including cache configuration and system clock initialization
- 是否需要替换：是
- 分类/替换原因：The function is an initialization function that configures hardware components: 1) It calls cache control functions (SCB_EnableICache/DisableICache, SCB_EnableDCache/DisableDCache) which access SCB registers, 2) It calls clock_init() which contains MMIO operations (DCDC registers, clock control registers), 3) It performs system initialization but does NOT configure NVIC, OS kernel, or VTOR (not CORE), 4) It does not handle data transmission/reception (not RECV), 5) It does not handle interrupts (not IRQ), 6) While clock_init() contains hardware-dependent loops, the main function itself doesn't have loops (not LOOP). Based on priority order (CORE > RECV > IRQ > INIT > LOOP > RETURNOK > SKIP > NODRIVER), this is classified as INIT.
- 原始代码：见上方【函数基本信息】中的函数内容
- 推荐/初始替换代码（FunctionClassifier）：
```
static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	/* [INIT REMOVED] SCB_DisableICache(); */
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	/* [INIT REMOVED] SCB_EnableICache(); */
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		/* [INIT REMOVED] Skip hardware check and enable */
		/* Original: if ((SCB->CCR & SCB_CCR_DC_Msk) == 0) { SCB_EnableDCache(); } */
	} else {
		/* [INIT REMOVED] SCB_DisableDCache(); */
	}

	/* Initialize system clock */
	/* [INIT REMOVED] clock_init(); */

	return 0;
}
```

【替换更新】
- 更新代码：static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	/* [INIT REMOVED] SCB_DisableICache(); */
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	/* [INIT REMOVED] SCB_EnableICache(); */
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		/* [INIT REMOVED] Skip hardware check and enable */
		/* Original: if ((SCB->CCR & SCB_CCR_DC_Msk) == 0) { SCB_EnableDCache(); } */
	} else {
		/* [INIT REMOVED] SCB_DisableDCache(); */
	}

	/* Initialize system clock */
	/* [INIT REMOVED] clock_init(); */

	return 0;
}
- 更新原因：Fix compilation verification failure by ensuring proper function signature and removing potential syntax issues

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：static int imxrt_init(void)
{
#ifndef CONFIG_IMXRT1XXX_CODE_CACHE
	/* SystemInit enables code cache, disable it here */
	/* [INIT REMOVED] SCB_DisableICache(); */
#else
	/* z_arm_init_arch_hw_at_boot() disables code cache if CONFIG_ARCH_CACHE is enabled,
	 * enable it here.
	 */
	/* [INIT REMOVED] SCB_EnableICache(); */
#endif

	if (IS_ENABLED(CONFIG_IMXRT1XXX_DATA_CACHE)) {
		/* [INIT REMOVED] Skip hardware check and enable */
		/* Original: if ((SCB->CCR & SCB_CCR_DC_Msk) == 0) { SCB_EnableDCache(); } */
	} else {
		/* [INIT REMOVED] SCB_DisableDCache(); */
	}

	/* Initialize system clock */
	/* [INIT REMOVED] clock_init(); */

	return 0;
}
    原因：Fix compilation verification failure by ensuring proper function signature and removing potential syntax issues
    时间：

=== 信息结束 ===
```

### z_arm_platform_init

```text
=== z_arm_platform_init 函数分析与替换信息 ===

【函数基本信息】
- 文件路径：/home/haojie/zephyrproject/zephyr/soc/arm/nxp_imx/rt/soc_rt10xx.c
- 行号：344
- 函数内容：void z_arm_platform_init(void)
{
	/* Call CMSIS SystemInit */
	SystemInit();
}


【替换更新】
- 更新代码：void z_arm_platform_init(void)
{
	/* Call CMSIS SystemInit */
	SystemInit();
}
- 更新原因：z_arm_platform_init is a CORE function that calls SystemInit() which configures VTOR. According to strict rules, VTOR writes MUST be preserved for the scheduler to work correctly. This replacement keeps the original function intact to ensure SystemInit() is called, which will configure VTOR and other critical system components.

【替换历史版本】
- 总共 1 次替换尝试

  版本 1:
    替换代码：void z_arm_platform_init(void)
{
	/* Call CMSIS SystemInit */
	SystemInit();
}
    原因：z_arm_platform_init is a CORE function that calls SystemInit() which configures VTOR. According to strict rules, VTOR writes MUST be preserved for the scheduler to work correctly. This replacement keeps the original function intact to ensure SystemInit() is called, which will configure VTOR and other critical system components.
    时间：

=== 信息结束 ===
```

## FunctionClassifier 汇总（已跑 classify：**276** 个；CodeQL `MMIOFunction`：**276** 个）

说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 `info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **30** 个，仅作对比，见文末附录。下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。

| 函数名 | function_type | has_replacement | 简述 |
|--------|---------------|-----------------|------|
| `CLOCK_DeinitArmPll` | SKIP | False | De-initializes (powers down) the ARM PLL by writing to the PLL control register |
| `CLOCK_DeinitAudioPll` | INIT | False | De-initializes the Audio PLL by writing power-down mask to the PLL control register |
| `CLOCK_DeinitEnetPll` | INIT | False | Disables the ENET PLL by writing a power-down mask to the PLL control register |
| `CLOCK_DeinitExternalClk` | INIT | False | Deinitializes the external 24MHz clock by powering it down |
| `CLOCK_DeinitRcOsc24M` | RETURNOK | False | Power down the RCOSC 24M clock by disabling the RC oscillator enable bit in the XTALOSC24M control register. |
| `CLOCK_DeinitSysPfd` | SKIP | False | De-initializes/disables the System PLL PFD (Phase Frequency Detector) by setting clock gate bits in the CCM_ANALOG re... |
| `CLOCK_DeinitSysPll` | INIT | False | De-initializes (powers down) the System PLL by writing a power-down mask to the clock control register |
| `CLOCK_DeinitUsb1Pfd` | RETURNOK | False | De-initializes (disables) the USB1 PLL PFD clock by setting the clock gate bit in the hardware register. |
| `CLOCK_DeinitUsb1Pll` | INIT | False | Deinitializes the USB1 PLL by writing zero to the PLL_USB1 register |
| `CLOCK_DeinitUsb2Pll` | RETURNOK | False | Deinitializes the USB2 PLL by writing 0 to the CCM_ANALOG->PLL_USB2 register |
| `CLOCK_DeinitVideoPll` | RETURNOK | False | De-initializes the Video PLL by writing a power-down mask to the PLL_VIDEO register |
| `CLOCK_DisableUsbhs0PhyPllClock` | RETURNOK | False | Disables USB HS PHY PLL clock by clearing enable bits and gating clocks |
| `CLOCK_DisableUsbhs1PhyPllClock` | RETURNOK | False | Disables the USB HS PHY PLL clock by clearing enable bits and setting clock gate control bits in hardware registers. |
| `CLOCK_EnableUsbhs0Clock` | INIT | False | Enables USB High Speed clock by configuring clock gating, resetting USB controller, and setting up power management |
| `CLOCK_EnableUsbhs0PhyPllClock` | INIT | False | Enables the internal 480MHz USB HS PHY PLL clock for USB functionality |
| `CLOCK_EnableUsbhs1Clock` | INIT | False | Enables USB HS clock by configuring clock gating, resetting USB controller, and setting PMU registers |
| `CLOCK_EnableUsbhs1PhyPllClock` | INIT | False | Enables the USB HS PHY PLL clock by initializing the USB PLL and configuring USB PHY control registers |
| `CLOCK_GetAhbFreq` | RETURNOK | False | Calculates and returns the AHB (Advanced High-performance Bus) clock frequency in hertz by reading clock controller r... |
| `CLOCK_GetClockOutCLKO1Freq` | RETURNOK | False | Reads the clock output 1 configuration from CCM register and returns the calculated frequency based on selected clock... |
| `CLOCK_GetClockOutClkO2Freq` | RETURNOK | False | Reads the clock output 2 configuration from CCM register and returns the calculated frequency based on selected clock... |
| `CLOCK_GetFreq` | NODRIVER | False | Dispatcher function that returns clock frequency in hertz for a specific clock name by calling appropriate specialize... |
| `CLOCK_GetIpgFreq` | RETURNOK | False | Gets the IPG (IP Bus) clock frequency by reading the CCM CBCDR register to obtain the IPG clock divider and dividing ... |
| `CLOCK_GetPerClkFreq` | RETURNOK | False | Reads the PER (Peripheral) clock frequency from hardware clock configuration registers |
| `CLOCK_GetPeriphClkFreq` | RETURNOK | False | Reads clock control module registers to determine the peripheral clock frequency based on current clock source select... |
| `CLOCK_GetPllFreq` | RETURNOK | False | Reads PLL configuration registers to calculate and return the current output frequency of a specified PLL |
| `CLOCK_GetPllUsb1SWFreq` | INIT | False | Returns the frequency of USB1 PLL switch clock based on PLL3 clock source selection |
| `CLOCK_GetSemcFreq` | RETURNOK | False | Gets the SEMC (Smart External Memory Controller) clock frequency in hertz by reading CCM register configuration and c... |
| `CLOCK_GetSysPfdFreq` | RETURNOK | False | Gets the current System PLL PFD (Phase Fractional Divider) output frequency for a specific PFD (Pfd0-Pfd3) by reading... |
| `CLOCK_GetUsb1PfdFreq` | RETURNOK | False | Calculates and returns the USB1 PLL PFD (Phase Fractional Divider) output frequency based on hardware register values |
| `CLOCK_InitArmPll` | INIT | False | Initializes the ARM PLL with specific configuration settings including bypass mode, divider selection, and waits for ... |
| `CLOCK_InitAudioPll` | INIT | False | Initializes the Audio PLL with specific configuration settings including bypass, numerator/denominator, loop divider,... |
| `CLOCK_InitEnetPll` | INIT | False | Initializes the ENET PLL (Phase-Locked Loop) for Ethernet clock generation with specific divider and output settings |
| `CLOCK_InitExternalClk` | INIT | False | Initializes the external 24MHz clock by powering up the crystal oscillator and waiting for it to stabilize |
| `CLOCK_InitRcOsc24M` | INIT | False | Initializes the RC oscillator 24MHz clock by enabling it through hardware register access |
| `CLOCK_InitSysPfd` | INIT | False | Initializes the System PLL PFD (Phase Fractional Divider) by setting the fractional divider value and managing clock ... |
| `CLOCK_InitSysPll` | INIT | False | Initializes the System PLL (Phase-Locked Loop) with specific configuration settings including dividers, fractional mo... |
| `CLOCK_InitUsb1Pfd` | INIT | False | Initializes the USB1 PLL PFD (Phase Fractional Divider) clock by configuring fractional value and managing clock gati... |
| `CLOCK_InitUsb1Pll` | INIT | False | Initializes the USB1 PLL (Phase-Locked Loop) with specific configuration settings including bypass mode, clock source... |
| `CLOCK_InitUsb2Pll` | INIT | False | Initializes the USB2 PLL with specific configuration settings including bypass mode, divider selection, and waits for... |
| `CLOCK_InitVideoPll` | INIT | False | Initializes the video PLL with specific configuration settings including loop divider, post divider, numerator, denom... |
| `CLOCK_IsSysPfdEnabled` | RETURNOK | False | Checks if a System Phase Fractional Divider (PFD) is enabled by reading the clock control module hardware register. |
| `CLOCK_IsUsb1PfdEnabled` | RETURNOK | False | Checks if the USB1 Phase Fractional Divider (PFD) is enabled by reading the PFD_480 register and checking the appropr... |
| `CLOCK_SetClockOutput1` | INIT | False | Configures clock output 1 by setting the clock source and divider, with option to enable or disable the output |
| `CLOCK_SetClockOutput2` | INIT | False | Configures the clock source and divider for clock output 2 on the NXP MIMXRT1062 microcontroller |
| `CLOCK_SwitchOsc` | INIT | False | Switches the OSC (oscillator) source for the SoC based on the input parameter |
| `ENET_ActiveSendRing` | INIT | False | Activates frame sending for specified Ethernet transmission ring by writing to TDAR registers to start transmission. |
| `ENET_AddMulticastGroup` | INIT | False | Adds the ENET device to a multicast group by calculating CRC from multicast address and enabling hardware multicast f... |
| `ENET_CommonFrame0IRQHandler` | IRQ | False | Common interrupt handler for ENET peripheral that dispatches to specific ISRs (Tx, Rx, timestamp, error) based on int... |
| `ENET_Deinit` | INIT | False | Deinitializes the ENET (Ethernet) module by disabling interrupts, disabling the ENET peripheral, and gating its clocks |
| `ENET_Down` | INIT | False | Stops and disables the ENET module by disabling interrupts and the ENET controller, then frees receive buffers. |
| `ENET_ErrorIRQHandler` | IRQ | False | Interrupt handler for ENET (Ethernet) error and wakeup interrupts, handling special IRQs including error, MII, and wa... |
| `ENET_GetMacAddr` | RETURNOK | False | Reads the MAC address from ENET peripheral registers (PALR and PAUR) and stores it in a user-provided buffer |
| `ENET_GetRxFrame` | RECV | True | Receives one Ethernet frame from a specified buffer descriptor ring with zero copy, using user-defined allocation and... |
| `ENET_GetStatistics` | RETURNOK | False | Reads statistical data from ENET peripheral registers and populates a statistics structure with Rx/Tx frame counts, e... |
| `ENET_Init` | INIT | False | Initializes the ENET (Ethernet) peripheral module by enabling clocks, resetting hardware, and configuring the module ... |
| `ENET_LeaveMulticastGroup` | INIT | False | Removes ENET device from a multicast group by updating multicast hash table registers |
| `ENET_MDIOC45Read` | RECV | False | Performs MDIO read operation using IEEE802.3 Clause 45 format to read data from PHY registers through SMI interface |
| `ENET_MDIOC45Write` | INIT | False | MDIO write operation using IEEE802.3 Clause 45 format to write data to a PHY register through ENET peripheral |
| `ENET_MDIORead` | RECV | False | Reads data from a PHY register using MDIO (Management Data Input/Output) with IEEE802.3 Clause 22 format |
| `ENET_MDIOWaitTransferOver` | LOOP | False | Waits for MDIO (Management Data Input/Output) transfer completion by polling the MII interrupt status flag |
| `ENET_MDIOWrite` | INIT | False | Performs MDIO write operations with IEEE802.3 Clause 22 format to write data to PHY registers over the MII management... |
| `ENET_ReceiveIRQHandler` | IRQ | False | Ethernet receive interrupt handler that processes receive frame and buffer interrupts, clears interrupt flags, and in... |
| `ENET_SendFrame` | RECV | False | Transmits an ENET Ethernet frame for a specified ring, handling DMA buffer management and hardware activation for dat... |
| `ENET_SetMII` | INIT | False | Sets the ENET MII speed and duplex mode for the Ethernet MAC peripheral |
| `ENET_SetMacAddr` | INIT | True | Sets the MAC address for the ENET (Ethernet) module by writing to hardware registers |
| `ENET_SetMacController` | INIT | False | Configures Ethernet MAC controller hardware registers including receive/transmit control, buffer descriptors, interru... |
| `ENET_SetSMI` | INIT | False | Configures the ENET SMI (Serial Management Interface) - MII management interface by setting MDC clock frequency and h... |
| `ENET_StartTxFrame` | RECV | False | Sends one Ethernet frame in specified BD ring with zero copy, supporting scattered buffer transmit |
| `ENET_TransmitIRQHandler` | IRQ | False | Ethernet transmit interrupt handler that processes transmit completion events, clears interrupt flags, and either rec... |
| `ENET_UpdateReadBuffers` | NODRIVER | False | Static helper function that updates receive buffer descriptors and activates receive ring for Ethernet peripheral |
| `GPIO_PinInit` | INIT | False | Initializes a GPIO pin with specified direction, output logic, and interrupt mode configuration |
| `LPUART_Deinit` | LOOP | False | Deinitializes an LPUART instance by waiting for transmit completion, disabling TX/RX, and disabling the LPUART clock |
| `LPUART_Init` | INIT | False | Initializes an LPUART instance with user configuration structure and peripheral clock, configuring baud rate, parity,... |
| `LPUART_TransferReceiveNonBlocking` | RECV | False | Non-blocking UART receive function that receives data using interrupt methods, handling both ring buffer and direct i... |
| `LPUART_TransferSendNonBlocking` | INIT | False | Transmits a buffer of data using interrupt method by enabling transmitter interrupts and updating driver state for no... |
| `SystemCoreClockUpdate` | INIT | False | Reads clock control registers to calculate and update the system core clock frequency |
| `SystemInit` | CORE | False | System initialization function that configures VTOR (vector table), disables watchdogs and SysTick, enables FPU and c... |
| `TRNG_Deinit` | INIT | False | Shuts down the TRNG peripheral by moving it to program mode, stopping entropy generation, waiting for oscillator to s... |
| `TRNG_Init` | INIT | False | Initializes the True Random Number Generator (TRNG) peripheral hardware and starts entropy generation |
| `add_to_head` | NODRIVER | False | Adds a shell history item to the head of the history list by copying data and prepending to a doubly linked list |
| `add_to_waitq_locked` | CORE | False | Adds a thread to a wait queue with scheduler spinlock held, marking it as pending and removing it from the ready queue |
| `adjust_owner_prio` | NODRIVER | False | Adjusts the priority of a mutex owner thread by comparing current priority with new priority and updating if different |
| `arch_new_thread` | CORE | False | Architecture-specific thread initialization function for ARM Cortex-M that sets up the initial exception stack frame ... |
| `arp_entry_find` | NODRIVER | False | Searches through a linked list of ARP entries to find an entry matching a specific network interface and destination ... |
| `arp_hdr_check` | NODRIVER | False | Validates ARP header fields for correctness including hardware type, protocol type, address lengths, and loopback add... |
| `arp_update` | NODRIVER | False | Updates ARP cache with new IP-to-MAC address mappings and processes pending packets waiting for ARP resolution |
| `bg_thread_main` | CORE | False | Mainline for kernel's background thread that completes kernel initialization and invokes application's main() routine |
| `check_used_port` | NODRIVER | False | Checks if a network port is already in use by iterating through network contexts and comparing protocol, port, and ad... |
| `clone_pkt_attributes` | NODRIVER | False | Copies network packet attributes from source packet to clone packet, including family, context, IP headers, VLAN tags... |
| `cmd_net_ip_add` | NODRIVER | False | Shell command handler for adding IPv4 addresses to network interfaces - parses arguments and calls network stack conf... |
| `cmd_net_ip_del` | NODRIVER | False | Shell command handler for deleting IPv4 addresses from network interfaces, handling both unicast and multicast addresses |
| `conn_addr_cmp` | NODRIVER | False | Compares network addresses (IPv4/IPv6) between a packet and socket address to check for duplicate connection handlers |
| `conn_are_endpoints_valid` | NODRIVER | False | Validates network connection endpoints by checking if source address is device's own address, if source and destinati... |
| `conn_find_handler` | NODRIVER | False | Searches for an existing network connection handler in the connection list based on protocol, addresses, ports, and r... |
| `context_sendto` | NODRIVER | False | Network context send function that handles protocol-specific data transmission for IPv4, IPv6, AF_PACKET, and AF_CAN ... |
| `dhcpv4_add_req_ipaddr` | NODRIVER | False | Adds DHCPv4 'Requested IP Address' option to a network packet |
| `dhcpv4_add_server_id` | NODRIVER | False | Adds DHCPv4 server ID option to a network packet as part of DHCP protocol handling |
| `dhcpv4_create_message` | NODRIVER | False | Creates a DHCPv4 message packet with appropriate options based on message type |
| `encode_float` | NODRIVER | False | Converts IEEE 754-2008 double-precision floating-point values to text format for formatted output in Zephyr's cbprint... |
| `eth_callback` | IRQ | True | Ethernet interrupt callback handler that processes various Ethernet events (Rx, Tx, Error, WakeUp, TimeStamp) and sig... |
| `eth_mcux_common_isr` | IRQ | True | Interrupt service routine for MCUX Ethernet driver that handles various Ethernet interrupts including RX/TX frame/buf... |
| `eth_mcux_phy_enter_reset` | INIT | True | Resets the PHY (Physical Layer) of the Ethernet controller by writing to the PHY's basic control register and updates... |
| `eth_mcux_phy_event` | INIT | True | PHY (Physical Layer) event handler for MCUX Ethernet driver that implements a state machine for PHY initialization, l... |
| `eth_mcux_phy_setup` | INIT | True | Configures PHY settings for MCUX Ethernet driver, ensuring PHY is not in factory test mode or NAND Tree mode |
| `eth_mcux_phy_start` | INIT | True | Starts/resets the Ethernet PHY (Physical Layer) by handling PHY state transitions and performing hardware initialization |
| `eth_mcux_set_config` | INIT | True | Configures Ethernet driver settings, specifically handling MAC address configuration for MCUX Ethernet driver |
| `eth_rx_thread` | NODRIVER | False | Zephyr RTOS thread function that handles Ethernet RX operations by waiting for RX semaphore, processing received fram... |
| `eth_tx` | RECV | True | Transmits Ethernet frames by copying packet data to hardware buffer and initiating transmission via ENET_SendFrame |
| `ethernet_fill_header` | NODRIVER | False | Creates and fills Ethernet headers (regular or VLAN) for network packets by allocating buffer fragments and copying M... |
| `ethernet_fill_in_dst_on_ipv4_mcast` | NODRIVER | False | Checks if an IPv4 packet is multicast and converts the IPv4 multicast address to an Ethernet MAC address |
| `ethernet_ll_prepare_on_ipv4` | NODRIVER | False | Prepares IPv4 packets for Ethernet transmission by handling ARP resolution for unicast destinations |
| `ethernet_recv` | NODRIVER | False | Processes received Ethernet packets in the Zephyr network stack, handling Ethernet header parsing, VLAN tagging, fram... |
| `ethernet_remove_l2_header` | NODRIVER | False | Removes the L2 header buffer from a network packet by manipulating the packet buffer chain and releasing the buffer f... |
| `ethernet_send` | NODRIVER | False | Ethernet L2 packet transmission function that determines packet type, sets up Ethernet headers, handles VLAN tagging,... |
| `first` | NODRIVER | False | Returns the first timeout structure from the kernel's timeout linked list |
| `generate_eth0_mac` | NODRIVER | False | Generates a MAC address for the eth0 Ethernet interface |
| `get_addresses` | NODRIVER | False | Formats network context addresses (local and remote) into string buffers for display, handling IPv4, IPv6, and other ... |
| `halt_thread` | CORE | False | Dequeues a specified thread and moves it into a new state (dead or suspended), performing thread cleanup operations |
| `handle_ipv4_echo_reply` | NODRIVER | False | Processes IPv4 ICMP echo reply packets (ping responses), extracts timing information, calculates round-trip time, and... |
| `icmpv4_handle_echo_request` | NODRIVER | False | Handles ICMPv4 echo request packets (ping requests) by validating the request, allocating a reply packet, copying pay... |
| `icmpv4_handle_header_options` | NODRIVER | False | Handles ICMPv4 header options processing by parsing IPv4 header options from incoming packet and preparing reply pack... |
| `icmpv4_update_record_route` | NODRIVER | False | Processes ICMPv4 Record Route options by parsing option data, finding free entries, and adding local IP address to th... |
| `icmpv4_update_time_stamp` | NODRIVER | False | Updates ICMPv4 timestamp options in reply packets according to RFC 791, handling overflow checking and timestamp inse... |
| `if_ipv4_get_addr` | NODRIVER | False | Searches for an IPv4 address on a network interface that matches specified criteria (address state and link-local/glo... |
| `iface_router_lookup` | NODRIVER | False | Searches for a router entry in the global router table based on network interface, address family, and IP address |
| `igmp_v2_create_packet` | NODRIVER | False | Creates an IGMP version 2 packet by setting up IPv4 headers with router alert options and calling IGMP payload creati... |
| `imx_pinctrl_init` | INIT | True | Initializes i.MX pin control hardware by enabling clock gates for IOMUX controllers based on SoC variant |
| `imxrt_init` | INIT | True | Performs basic hardware initialization for i.MX RT processors including cache configuration and system clock initiali... |
| `init_ready_q` | CORE | False | Initializes the scheduler's ready queue data structure based on configured scheduler type (SCALABLE, MULTIQ, or DUMB). |
| `ipv4_addr_find` | NODRIVER | False | Searches for an IPv4 address in a network interface's address list by iterating through unicast addresses and compari... |
| `ipv4_is_broadcast_address` | NODRIVER | False | Determines if an IPv4 address is a broadcast address for a given network interface |
| `ipv4_maddr_find` | NODRIVER | False | Searches for an IPv4 multicast address in a network interface's multicast address table, filtering by usage status an... |
| `k_heap_init` | NODRIVER | False | Initializes a kernel synchronized heap structure with wait queue and system heap |
| `k_mbox_get` | NODRIVER | False | Zephyr RTOS mailbox receive function that retrieves messages from a mailbox by searching for compatible senders and w... |
| `k_mbox_init` | NODRIVER | False | Initializes a Zephyr RTOS mailbox data structure by setting up transmit/receive wait queues, initializing a spinlock,... |
| `k_mem_slab_init` | NODRIVER | False | Initializes a kernel memory slab structure with buffer, block size, and block count parameters |
| `k_msgq_cleanup` | NODRIVER | False | Cleans up a message queue by checking for waiting threads and freeing dynamically allocated buffer memory |
| `k_msgq_init` | NODRIVER | False | Initializes a Zephyr RTOS message queue data structure by setting buffer pointers, size parameters, and internal state |
| `k_poll_event_init` | NODRIVER | False | Initializes a Zephyr kernel poll event structure with provided parameters and validation |
| `k_stack_cleanup` | NODRIVER | False | Cleans up a Zephyr kernel stack object by checking wait queue and freeing allocated memory if needed |
| `k_stack_init` | NODRIVER | False | Initializes a kernel stack data structure by setting up wait queue, lock, and buffer pointers |
| `k_timer_init` | NODRIVER | False | Initializes a kernel timer structure by setting callback functions, status, wait queue, timeout structure, and perfor... |
| `k_work_cancel_delayable_sync` | NODRIVER | False | Cancels a delayable work item synchronously in Zephyr RTOS work queue subsystem |
| `k_work_cancel_sync` | NODRIVER | False | Synchronously cancels a work item in Zephyr RTOS, waiting for completion if the work is currently running |
| `k_work_flush` | NODRIVER | False | Flushes a work item if necessary, waiting for completion if the work is queued or running |
| `k_work_flush_delayable` | NODRIVER | False | Flushes a delayable work item in Zephyr RTOS, waiting for it to complete if necessary |
| `k_work_init_delayable` | NODRIVER | False | Initializes a delayable work item structure for Zephyr RTOS work queue system |
| `k_work_poll_init` | NODRIVER | False | Initializes a pollable work structure in Zephyr RTOS, setting up work item with handler and timeout initialization |
| `k_work_poll_submit_to_queue` | NODRIVER | False | Submits a pollable work item to a work queue in Zephyr RTOS, managing poll events, timeouts, and work submission |
| `k_work_queue_start` | NODRIVER | False | Starts a work queue thread in Zephyr RTOS by initializing data structures and creating/starting a kernel thread to pr... |
| `mbox_message_put` | NODRIVER | False | Helper routine for sending mailbox messages that handles both synchronous and asynchronous sends in Zephyr RTOS |
| `mcux_ccm_get_subsys_rate` | RETURNOK | False | Retrieves clock rates for various subsystems (I2C, SPI, UART, USDHC, DMA, PWM, CAN, GPT, QTMR, SAI) by reading hardwa... |
| `mgmt_thread` | NODRIVER | False | Network management thread that runs in an infinite loop, popping events from a queue and running callbacks for networ... |
| `move_thread_to_end_of_prio_q` | CORE | False | Moves a thread to the end of its priority queue in the Zephyr RTOS scheduler |
| `net_arp_input` | NODRIVER | False | Processes incoming ARP packets, validates ARP headers, handles ARP requests and replies, updates ARP cache, and sends... |
| `net_arp_prepare` | NODRIVER | False | Prepares ARP requests and manages ARP cache lookups for IPv4 packets in the Zephyr networking subsystem |
| `net_buf_alloc_len` | NODRIVER | False | Allocates a network buffer from a pool with optional data allocation, handling synchronization and timeout |
| `net_buf_alloc_with_data` | NODRIVER | False | Allocates a network buffer from a pool and initializes it with external data |
| `net_buf_append_bytes` | NODRIVER | False | Appends multiple bytes to a network buffer, creating new fragments when needed and handling buffer allocation |
| `net_buf_clone` | NODRIVER | False | Creates a clone/copy of an existing network buffer, either by reference counting or allocating new memory and copying... |
| `net_buf_linearize` | NODRIVER | False | Copies data from a fragmented network buffer chain into a contiguous linear destination buffer, handling offsets and ... |
| `net_buf_reset` | NODRIVER | False | Resets a network buffer by calling net_buf_simple_reset on its internal buffer structure after verifying buffer flags... |
| `net_buf_unref` | NODRIVER | False | Decrements reference count of network buffer and frees it when count reaches zero, handling buffer fragments. |
| `net_calc_chksum` | NODRIVER | False | Calculates network checksum for IP packets, supporting both IPv4 and IPv6 with various protocols (TCP, UDP, ICMP, ICM... |
| `net_calc_chksum_ipv4` | NODRIVER | False | Calculates IPv4 checksum for network packets by summing header and options data |
| `net_conn_input` | NODRIVER | False | Network connection input handler that matches incoming packets against registered connection handlers and invokes app... |
| `net_conn_register` | NODRIVER | False | Registers a network connection handler for protocol processing, managing connection structures and parameters without... |
| `net_context_bind` | NODRIVER | False | Binds a network context to a specific address and port, handling multiple address families (IPv6, IPv4, AF_PACKET, AF... |
| `net_context_connect` | NODRIVER | False | Establishes a network connection for a socket context, handling IPv4/IPv6 address setup, parameter validation, and co... |
| `net_context_create_ipv4_new` | NODRIVER | False | Creates IPv4 packets for network contexts by validating source addresses, setting TTL, DSCP/ECN, and priority fields,... |
| `net_dhcpv4_init` | NODRIVER | False | Initializes DHCPv4 client functionality by registering UDP callbacks for DHCP ports, setting up timeout work, and reg... |
| `net_dhcpv4_input` | NODRIVER | False | Processes incoming DHCPv4 packets, validates them, extracts DHCP message data, parses options, and handles DHCP replies |
| `net_eth_ipv4_mcast_to_mac_addr` | NODRIVER | False | Converts an IPv4 multicast address to an Ethernet multicast MAC address according to RFC 1112 specification |
| `net_eth_ipv6_mcast_to_mac_addr` | NODRIVER | False | Converts an IPv6 multicast address to an Ethernet MAC address according to RFC 2464 specification |
| `net_icmpv4_finalize` | NODRIVER | False | Finalizes ICMPv4 packets by calculating and setting checksums and handling IPv4 header options |
| `net_icmpv4_input` | NODRIVER | False | Processes incoming ICMPv4 packets by validating headers, checking checksums, filtering broadcast packets, and calling... |
| `net_icmpv4_send_error` | NODRIVER | False | Creates and sends ICMPv4 error messages based on an original packet, error type, and error code |
| `net_if_ipv4_addr_add` | NODRIVER | False | Adds an IPv4 address to a network interface by finding an available slot in the interface's address table and configu... |
| `net_if_ipv4_addr_lookup` | NODRIVER | False | Searches through all network interfaces to find a matching IPv4 address in their address tables |
| `net_if_ipv4_addr_mask_cmp` | NODRIVER | False | Compares an IPv4 address with network interface's IPv4 addresses using subnet masks to check if they belong to the sa... |
| `net_if_ipv4_addr_rm` | NODRIVER | False | Removes an IPv4 address from a network interface by searching through the interface's address list, marking it as unu... |
| `net_if_ipv4_get_best_match` | NODRIVER | False | Selects the best matching IPv4 source address for a given destination address by finding the longest prefix match amo... |
| `net_if_ipv4_maddr_add` | NODRIVER | False | Adds an IPv4 multicast address to a network interface by finding an available slot and configuring the multicast addr... |
| `net_if_ipv4_select_src_addr` | NODRIVER | False | Selects the best source IPv4 address for a given destination address based on network interface configuration and add... |
| `net_ipv4_create` | NODRIVER | False | Creates an IPv4 packet header by setting Type of Service (TOS) fields and delegating to net_ipv4_create_full for comp... |
| `net_ipv4_finalize` | NODRIVER | False | Finalizes IPv4 packet headers by setting header fields, calculating checksums, and calling appropriate transport laye... |
| `net_ipv4_igmp_input` | NODRIVER | False | Processes IGMP (Internet Group Management Protocol) packets, validates destination addresses, checks checksums, updat... |
| `net_ipv4_input` | NODRIVER | False | Processes incoming IPv4 packets, validates headers, checks conditions, and dispatches to appropriate transport layer ... |
| `net_ipv4_parse_hdr_options` | NODRIVER | False | Parses IPv4 header options from a network packet, validating option formats and calling callback for specific option ... |
| `net_mgmt_add_event_callback` | NODRIVER | False | Adds a network management event callback to the callback list for event notification |
| `net_mgmt_del_event_callback` | NODRIVER | False | Removes a network management event callback from the callback list and updates the global event mask |
| `net_pkt_append_buffer` | NODRIVER | False | Appends a buffer to a network packet, either setting it as the first buffer or inserting it as a fragment to existing... |
| `net_pkt_available_buffer` | NODRIVER | False | Calculates the available buffer space in a network packet by subtracting current length from maximum length |
| `net_pkt_available_payload_buffer` | NODRIVER | False | Calculates available payload buffer space in a network packet after accounting for protocol headers |
| `net_pkt_buffer_hexdump` | NODRIVER | False | Prints a hex dump of a network packet's buffer chain for debugging purposes |
| `net_pkt_buffer_info` | NODRIVER | False | Prints debugging information about a network packet's buffer chain, showing buffer pointers, reference counts, length... |
| `net_pkt_clone_internal` | NODRIVER | False | Clones a network packet by allocating memory and copying packet data and attributes |
| `net_pkt_compact` | NODRIVER | False | Compacts data in a network packet by merging fragments and removing empty fragments to optimize memory usage |
| `net_pkt_copy` | NODRIVER | False | Copies data from source network packet to destination network packet for specified length, handling buffer management... |
| `net_pkt_cursor_init` | NODRIVER | False | Initializes the cursor structure within a network packet by setting buffer pointer and position |
| `net_pkt_cursor_operate` | NODRIVER | False | Internal network packet cursor operation function that performs skip/read/write/memset operations on packet data buffers |
| `net_pkt_find_offset` | NODRIVER | False | Finds the offset of a pointer within a network packet's buffer chain by traversing the linked list of net_buf fragments. |
| `net_pkt_frag_add` | NODRIVER | False | Adds a network buffer fragment to a network packet, managing the fragment chain |
| `net_pkt_frag_del` | NODRIVER | False | Deletes a fragment from a network packet's fragment list, handling reference counting and memory management |
| `net_pkt_frag_insert` | NODRIVER | False | Inserts a network buffer fragment into a network packet's fragment list by updating pointer linkages |
| `net_pkt_get_contiguous_len` | NODRIVER | False | Calculates the length of contiguous data available in a network packet buffer by examining the packet cursor position... |
| `net_pkt_get_current_offset` | NODRIVER | False | Calculates the current byte offset within a network packet by traversing the buffer chain from start to cursor position. |
| `net_pkt_pull` | NODRIVER | False | Removes data from the beginning of a network packet buffer by adjusting buffer lengths and shifting data within buffe... |
| `net_pkt_remaining_data` | NODRIVER | False | Calculates the total remaining data in a network packet from the current cursor position through all buffer fragments |
| `net_pkt_remove_tail` | NODRIVER | False | Removes specified length of data from the tail of a network packet buffer by adjusting buffer fragment lengths and fr... |
| `net_pkt_shallow_clone` | NODRIVER | False | Creates a shallow clone of a network packet by allocating a new packet structure and copying buffer references, inter... |
| `net_pkt_trim_buffer` | NODRIVER | False | Removes empty buffers from a network packet's buffer chain by iterating through linked list of net_buf structures and... |
| `net_pkt_unref` | NODRIVER | False | Decrements reference count of a network packet and frees it when count reaches zero |
| `net_pkt_update_length` | NODRIVER | False | Updates the length of network packet buffers by distributing total length across buffer fragments in a linked list |
| `net_recv_data` | NODRIVER | False | Network packet reception handler that processes received packets at the IP/networking layer, validates parameters, ap... |
| `net_rx` | NODRIVER | False | Processes received network packets by updating statistics, checking for loopback, and forwarding to packet processing |
| `net_send_data` | NODRIVER | False | Handles network packet transmission by validating packets, updating statistics, checking IP addresses, and forwarding... |
| `net_udp_finalize` | NODRIVER | False | Finalizes a UDP packet by setting the UDP length field and calculating checksum if needed |
| `net_udp_get_hdr` | NODRIVER | False | Extracts UDP header from a network packet by skipping IP headers and retrieving UDP header data |
| `net_udp_input` | NODRIVER | False | Processes UDP packet input by validating UDP header length and checksum, returning UDP header pointer or NULL on failure |
| `net_udp_set_hdr` | NODRIVER | False | Sets a UDP header in a network packet by copying the provided UDP header structure to the appropriate position in the... |
| `next` | NODRIVER | False | Returns the next timeout entry in the kernel's timeout linked list |
| `ping_work` | NODRIVER | False | Network shell ping work handler that sends ICMP echo requests at regular intervals and manages ping sequence timing |
| `pkt_alloc_buffer` | NODRIVER | False | Allocates network packet buffers from a buffer pool, creating a linked list of buffer fragments to satisfy the reques... |
| `pkt_cursor_advance` | NODRIVER | False | Advances the cursor position within a network packet buffer, moving to the next buffer if the current one is fully pr... |
| `pkt_cursor_jump` | NODRIVER | False | Network packet cursor manipulation function that jumps to the next fragment in a packet buffer chain, looking for fra... |
| `pkt_cursor_update` | NODRIVER | False | Updates the cursor position within a network packet buffer, determining whether to jump to next buffer or increment p... |
| `pkt_get_max_len` | NODRIVER | False | Calculates the maximum length of a network packet by summing the maximum lengths of all buffer fragments in the packe... |
| `processing_data` | NODRIVER | False | Processes network packets by calling process_data() and handles return status for packet consumption, dropping, or co... |
| `ready_thread` | CORE | False | Adds a thread to the run queue if it's ready and not already queued, as part of the OS kernel scheduler |
| `remove_from_tail` | NODRIVER | False | Removes the oldest item from shell history list and frees its space from the ring buffer |
| `remove_timeout` | NODRIVER | False | Removes a timeout from the kernel's timeout tracking system and adjusts timing of subsequent timeouts |
| `send_igmp_report` | NODRIVER | False | Sends IGMP V2 membership reports for joined multicast groups on a network interface |
| `signal_poller` | NODRIVER | False | Handles signaling a poller thread when a poll event occurs, managing thread state transitions (unpending, setting ret... |
| `timeout_rem` | NODRIVER | False | Calculates remaining ticks for a timeout by traversing the timeout list and subtracting elapsed time |
| `triggered_work_cancel` | NODRIVER | False | Cancels a poll-based work item by removing timeouts, clearing event registrations, and resetting work queue ownership |
| `triggered_work_handler` | NODRIVER | False | Handles triggered work items in the Zephyr kernel's poll subsystem by clearing event registrations and executing the ... |
| `trng_ApplyUserConfig` | INIT | False | Applies user configuration settings to the TRNG (True Random Number Generator) module by setting retry counts, statis... |
| `trng_SetFrequencyCountMaxLimit` | INIT | False | Sets statistical Frequency Count Maximum and Minimum Limit Registers for TRNG peripheral |
| `trng_SetMonobitLimit` | RETURNOK | False | Sets the Statistical Check Monobit Limit Register (TRNG_SCML) for TRNG peripheral statistical checking |
| `trng_SetPokerMaxLimit` | RETURNOK | False | Sets the statistical Poker Maximum Limit Register and Poker Range Register for TRNG peripheral statistical checking |
| `trng_SetRunBit1Limit` | INIT | False | Sets the Statistical Check Run Length 1 Limit Register (TRNG_SCR1L) for TRNG peripheral configuration |
| `trng_SetRunBit2Limit` | INIT | False | Sets the Statistical Check Run Length 2 Limit Register for TRNG peripheral configuration |
| `trng_SetRunBit3Limit` | RETURNOK | False | Sets the Statistical Check Run Length 3 Limit Register for TRNG peripheral with parameter validation |
| `trng_SetRunBit4Limit` | INIT | False | Sets the Statistical Check Run Length 4 Limit Register for TRNG peripheral configuration |
| `trng_SetRunBit5Limit` | INIT | False | Sets the Statistical Check Run Length 5 Limit Register for TRNG peripheral |
| `trng_SetRunBit6Limit` | INIT | False | Sets the Statistical Check Run Length 6 Limit Register for TRNG peripheral |
| `update_cache` | NODRIVER | False | Updates the scheduler's ready queue cache based on preemption decisions, determining which thread should be cached as... |
| `z_abort_timeout` | NODRIVER | False | Removes a timeout from the kernel timeout queue if it's currently scheduled |
| `z_add_timeout` | CORE | False | Adds a timeout to the kernel's timeout list for scheduling timeout callbacks |
| `z_cbvprintf_impl` | NODRIVER | False | Callback-based printf implementation that formats output using a callback mechanism, processing format strings and va... |
| `z_handle_obj_poll_events` | NODRIVER | False | Handles poll events by retrieving events from a doubly-linked list and signaling them with a given state within the Z... |
| `z_impl_k_condvar_init` | NODRIVER | False | Initializes a Zephyr RTOS condition variable object by setting up its wait queue and kernel object tracking |
| `z_impl_k_mutex_init` | NODRIVER | False | Initializes a Zephyr kernel mutex structure by setting owner to NULL, lock count to 0, initializing wait queue, and c... |
| `z_impl_k_mutex_lock` | NODRIVER | False | Zephyr RTOS mutex lock implementation with priority inheritance and timeout support |
| `z_impl_k_poll` | CORE | False | Zephyr RTOS kernel polling function that manages poll events, registers events, and handles thread scheduling for pol... |
| `z_impl_k_poll_signal_init` | NODRIVER | False | Initializes a Zephyr RTOS poll signal object by setting up the poll events list, resetting the signaled flag, and ini... |
| `z_impl_k_poll_signal_raise` | NODRIVER | False | Raises a poll signal in the Zephyr kernel, setting the signal result and signaled flag, then potentially triggers thr... |
| `z_impl_k_queue_init` | NODRIVER | False | Initializes a kernel queue data structure by setting up its internal linked lists, spinlock, wait queue, and kernel o... |
| `z_impl_k_sem_init` | NODRIVER | False | Initializes a kernel semaphore object with specified initial count and limit, validates parameters, and sets up inter... |
| `z_impl_k_timer_status_sync` | NODRIVER | False | Zephyr kernel timer status synchronization function that waits for a timer to expire and returns its status |
| `z_impl_k_yield` | CORE | False | Zephyr RTOS kernel function that implements thread yielding - voluntarily gives up CPU to allow other threads to run ... |
| `z_impl_net_addr_ntop` | NODRIVER | False | Converts binary network addresses (IPv4/IPv6) to string representation (text format) |
| `z_impl_net_addr_pton` | NODRIVER | False | Converts presentation format IP address (string) to network format (binary) for both IPv4 and IPv6 addresses |
| `z_init_thread_base` | NODRIVER | False | Initializes the base thread structure for Zephyr RTOS kernel thread management, setting thread properties like priori... |
| `z_priq_dumb_best` | CORE | False | Scheduler function that finds the best thread from a priority queue (returns thread at head of queue) |
| `z_priq_dumb_remove` | CORE | False | Removes a thread from a priority queue in the Zephyr RTOS scheduler |
| `z_priq_mq_best` | CORE | False | Finds the highest priority thread in a multi-queue priority queue for the Zephyr RTOS scheduler |
| `z_sched_waitq_walk` | CORE | False | Walks through a wait queue and invokes a callback function on each waiting thread in the scheduler |
| `z_set_prio` | CORE | False | Sets thread priority in the Zephyr RTOS scheduler without rescheduling, returning whether rescheduling is needed later. |
| `z_setup_new_thread` | CORE | False | Sets up a new thread in Zephyr RTOS by initializing thread data structures, setting up thread stack, and performing a... |
| `z_shell_history_get` | NODRIVER | False | Retrieves command history items from shell history buffer based on navigation direction (up/down) |
| `z_shell_history_init` | NODRIVER | False | Initializes a shell history data structure by setting up a doubly linked list and resetting the current pointer |
| `z_shell_history_put` | NODRIVER | False | Adds a command line to the shell history buffer using ring buffer and linked list management |
| `z_timer_expiration_handler` | CORE | False | Kernel timer expiration handler that processes timer expirations, updates timer status, calls user expiry functions, ... |
| `z_unpend_all` | CORE | False | Kernel scheduler function that removes all threads from a wait queue, marks them as ready, and indicates if schedulin... |

## 附录：interesting MMIO expr 子集（共 30 个，较 `get_mmio_func_list()` 更窄）

来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。

- `CLOCK_InitArmPll`
- `CLOCK_InitAudioPll`
- `CLOCK_InitEnetPll`
- `CLOCK_InitExternalClk`
- `CLOCK_InitSysPll`
- `CLOCK_InitUsb1Pll`
- `CLOCK_InitUsb2Pll`
- `CLOCK_InitVideoPll`
- `CLOCK_SetDiv`
- `CLOCK_SetMux`
- `ENET_AddMulticastGroup`
- `ENET_GetInstance`
- `ENET_GetRxFrame`
- `ENET_LeaveMulticastGroup`
- `ENET_MDIOWaitTransferOver`
- `ENET_ReadFrame`
- `ENET_ReceiveIRQHandler`
- `ENET_RxBufferFreeAll`
- `ENET_SendFrame`
- `ENET_SetHandler`
- `ENET_SetMacController`
- `ENET_SetRxBufferDescriptors`
- `ENET_StartTxFrame`
- `ENET_TransmitIRQHandler`
- `clock_init`
- `eth_mcux_phy_event`
- `eth_mcux_phy_setup`
- `eth_rx`
- `eth_rx_thread`
- `eth_tx`
