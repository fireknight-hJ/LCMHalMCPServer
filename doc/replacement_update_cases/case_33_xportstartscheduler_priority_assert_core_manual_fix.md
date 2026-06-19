# Case 33 - xPortStartScheduler Priority Assert (CORE Manual Fix)

## 背景

- Demo: `stm32/LwIP_StreamingServer`（同类策略后续复用于其他 FreeRTOS demo）
- Function: `xPortStartScheduler`
- 归类: `feedback_loop_failure_core_manual_fix`
- 分类状态: `function_type=CORE (protected)`, `auto_replacement=disabled_by_policy`
- 关注问题: `priority/assert + scheduler startup abort`

## 触发原因（Feedback Loop Failure Reason）

该问题发生在调度器启动早期。`vTaskStartScheduler` 调用 `xPortStartScheduler` 后，会先执行一组 Cortex-M/FreeRTOS 专属一致性检查（`configASSERT`）：

- 向量表安装检查（SVC/PendSV handler 是否正确）
- `configMAX_SYSCALL_INTERRUPT_PRIORITY` 与硬件优先级位宽匹配检查
- `ucMaxSysCallPriority != 0` 检查
- PRIGROUP 约束检查（在 `vPortValidateInterruptPriority` 路径中体现）

在仿真环境中，如果前置 NVIC/VTOR/优先级分组配置不满足预期，会在这些前置 assert 处提前中断，表现为调度器未正常进入首任务路径，进而陷入死循环。

## 为什么这次没有自动修复

这是一个刻意保留的系统边界：

- `xPortStartScheduler` 属于 FreeRTOS **CORE 调度核心函数**；
- 按当前策略，CORE 函数默认禁止自动替换，避免把 OS 上下文切换链路改坏；
- 因此，这类失败不会由自动 ReplacementUpdate 直接“改函数体”来自愈，而是会停在异常退出。

这就是本例作为“反馈闭环失败样例”的关键点：  
**不是模型没发现问题，而是策略上不允许自动改 CORE。**

## 人工修复策略（工程妥协）

本例采用人工介入，而非放开 CORE 自动替换。原则如下：

1. **不改 CORE 函数本体**：`vTaskStartScheduler` / `xPortStartScheduler` / `prvPortStartFirstTask` 等保持原始实现。
2. **人工修外围条件**：优先修复/核对 NVIC、PRIGROUP、VTOR、SysTick、`FreeRTOSConfig` 优先级参数一致性。
3. **人工清理误替换**：若历史流程误生成过 OS CORE 相关 `replacement_update_*`，先清理后重跑，恢复内核原链路。
4. **保留策略约束**：此类工程妥协不下放给大模型自动决策，由人工确认风险后处理。

该策略随后在其他 FreeRTOS demo 中沿用：  
遇到 CORE 启动链路 assert，不做自动替换，统一走“人工定位 + 外围修复 + CORE 保真”流程。

## 证据路径

- FreeRTOS 源码（检查点所在）:  
  `/home/haojie/mcuxsdk-workspace/mcuxsdk/rtos/freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.c`
- 相关调用链证据:  
  `testcases/server/stm32/LwIP_StreamingServer/emulate/debug_output/function.txt`  
  `testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS/emulate/debug_output/function.txt`
- 过程复盘（CORE 不可随意替换）:  
  `case_study/rtos_os_core_scheduler_stub_fix/README.md`  
  `case_study/rtos_nvic_init_stub_fix/README.md`

## 前因后果解读

- 前因: 调度器启动前置优先级/assert 检查失败，系统在 CORE 启动链路异常陷入死循环。
- 动作: 不走自动替换，改为人工修复外围配置并保持 CORE 函数不变。
- 后果: 成功避免“为了跑通而破坏内核语义”的过度自动化，形成可复用的 FreeRTOS 工程处理准则。

## 代码页（完整附录）

> 以下为本案例对应版本的完整函数源码，用于复盘“卡在优先级 assert”的具体代码语义。  
> 来源：`mcuxsdk-workspace/mcuxsdk/rtos/freertos/freertos-kernel/`。

### A. `vTaskStartScheduler`（完整）

```c
void vTaskStartScheduler( void )
{
    BaseType_t xReturn;

    traceENTER_vTaskStartScheduler();

    #if ( configUSE_CORE_AFFINITY == 1 ) && ( configNUMBER_OF_CORES > 1 )
    {
        /* Sanity check that the UBaseType_t must have greater than or equal to
         * the number of bits as confNUMBER_OF_CORES. */
        configASSERT( ( sizeof( UBaseType_t ) * taskBITS_PER_BYTE ) >= configNUMBER_OF_CORES );
    }
    #endif /* #if ( configUSE_CORE_AFFINITY == 1 ) && ( configNUMBER_OF_CORES > 1 ) */

    xReturn = prvCreateIdleTasks();

    #if ( configUSE_TIMERS == 1 )
    {
        if( xReturn == pdPASS )
        {
            xReturn = xTimerCreateTimerTask();
        }
        else
        {
            mtCOVERAGE_TEST_MARKER();
        }
    }
    #endif /* configUSE_TIMERS */

    if( xReturn == pdPASS )
    {
        /* freertos_tasks_c_additions_init() should only be called if the user
         * definable macro FREERTOS_TASKS_C_ADDITIONS_INIT() is defined, as that is
         * the only macro called by the function. */
        #ifdef FREERTOS_TASKS_C_ADDITIONS_INIT
        {
            freertos_tasks_c_additions_init();
        }
        #endif

        /* Interrupts are turned off here, to ensure a tick does not occur
         * before or during the call to xPortStartScheduler().  The stacks of
         * the created tasks contain a status word with interrupts switched on
         * so interrupts will automatically get re-enabled when the first task
         * starts to run. */
        portDISABLE_INTERRUPTS();

        #if ( configUSE_C_RUNTIME_TLS_SUPPORT == 1 )
        {
            /* Switch C-Runtime's TLS Block to point to the TLS
             * block specific to the task that will run first. */
            configSET_TLS_BLOCK( pxCurrentTCB->xTLSBlock );
        }
        #endif

        xNextTaskUnblockTime = portMAX_DELAY;
        xSchedulerRunning = pdTRUE;
        xTickCount = ( TickType_t ) configINITIAL_TICK_COUNT;

        /* If configGENERATE_RUN_TIME_STATS is defined then the following
         * macro must be defined to configure the timer/counter used to generate
         * the run time counter time base.   NOTE:  If configGENERATE_RUN_TIME_STATS
         * is set to 0 and the following line fails to build then ensure you do not
         * have portCONFIGURE_TIMER_FOR_RUN_TIME_STATS() defined in your
         * FreeRTOSConfig.h file. */
        portCONFIGURE_TIMER_FOR_RUN_TIME_STATS();

        traceTASK_SWITCHED_IN();

        traceSTARTING_SCHEDULER( xIdleTaskHandles );

        /* Setting up the timer tick is hardware specific and thus in the
         * portable interface. */

        /* The return value for xPortStartScheduler is not required
         * hence using a void datatype. */
        ( void ) xPortStartScheduler();

        /* In most cases, xPortStartScheduler() will not return. If it
         * returns pdTRUE then there was not enough heap memory available
         * to create either the Idle or the Timer task. If it returned
         * pdFALSE, then the application called xTaskEndScheduler().
         * Most ports don't implement xTaskEndScheduler() as there is
         * nothing to return to. */
    }
    else
    {
        /* This line will only be reached if the kernel could not be started,
         * because there was not enough FreeRTOS heap to create the idle task
         * or the timer task. */
        configASSERT( xReturn != errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY );
    }

    /* Prevent compiler warnings if INCLUDE_xTaskGetIdleTaskHandle is set to 0,
     * meaning xIdleTaskHandles are not used anywhere else. */
    ( void ) xIdleTaskHandles;

    /* OpenOCD makes use of uxTopUsedPriority for thread debugging. Prevent uxTopUsedPriority
     * from getting optimized out as it is no longer used by the kernel. */
    ( void ) uxTopUsedPriority;

    traceRETURN_vTaskStartScheduler();
}
```

### B. `xPortStartScheduler`（完整）

```c
BaseType_t xPortStartScheduler( void )
{
    /* This port can be used on all revisions of the Cortex-M7 core other than
     * the r0p1 parts.  r0p1 parts should use the port from the
     * /source/portable/GCC/ARM_CM7/r0p1 directory. */
    configASSERT( portCPUID != portCORTEX_M7_r0p1_ID );
    configASSERT( portCPUID != portCORTEX_M7_r0p0_ID );

    /* An application can install FreeRTOS interrupt handlers in one of the
     * following ways:
     * 1. Direct Routing - Install the functions vPortSVCHandler and
     *    xPortPendSVHandler for SVCall and PendSV interrupts respectively.
     * 2. Indirect Routing - Install separate handlers for SVCall and PendSV
     *    interrupts and route program control from those handlers to
     *    vPortSVCHandler and xPortPendSVHandler functions.
     *
     * Applications that use Indirect Routing must set
     * configCHECK_HANDLER_INSTALLATION to 0 in their FreeRTOSConfig.h. Direct
     * routing, which is validated here when configCHECK_HANDLER_INSTALLATION
     * is 1, should be preferred when possible. */
    #if ( configCHECK_HANDLER_INSTALLATION == 1 )
    {
        const portISR_t * const pxVectorTable = portSCB_VTOR_REG;

        /* Validate that the application has correctly installed the FreeRTOS
         * handlers for SVCall and PendSV interrupts. We do not check the
         * installation of the SysTick handler because the application may
         * choose to drive the RTOS tick using a timer other than the SysTick
         * timer by overriding the weak function vPortSetupTimerInterrupt().
         *
         * Assertion failures here indicate incorrect installation of the
         * FreeRTOS handlers. For help installing the FreeRTOS handlers, see
         * https://www.freertos.org/Why-FreeRTOS/FAQs.
         *
         * Systems with a configurable address for the interrupt vector table
         * can also encounter assertion failures or even system faults here if
         * VTOR is not set correctly to point to the application's vector table. */
        configASSERT( pxVectorTable[ portVECTOR_INDEX_SVC ] == vPortSVCHandler );
        configASSERT( pxVectorTable[ portVECTOR_INDEX_PENDSV ] == xPortPendSVHandler );
    }
    #endif /* configCHECK_HANDLER_INSTALLATION */

    #if ( configASSERT_DEFINED == 1 )
    {
        volatile uint8_t ucOriginalPriority;
        volatile uint32_t ulImplementedPrioBits = 0;
        volatile uint8_t * const pucFirstUserPriorityRegister = ( volatile uint8_t * const ) ( portNVIC_IP_REGISTERS_OFFSET_16 + portFIRST_USER_INTERRUPT_NUMBER );
        volatile uint8_t ucMaxPriorityValue;

        /* Determine the maximum priority from which ISR safe FreeRTOS API
         * functions can be called.  ISR safe functions are those that end in
         * "FromISR".  FreeRTOS maintains separate thread and ISR API functions to
         * ensure interrupt entry is as fast and simple as possible.
         *
         * Save the interrupt priority value that is about to be clobbered. */
        ucOriginalPriority = *pucFirstUserPriorityRegister;

        /* Determine the number of priority bits available.  First write to all
         * possible bits. */
        *pucFirstUserPriorityRegister = portMAX_8_BIT_VALUE;

        /* Read the value back to see how many bits stuck. */
        ucMaxPriorityValue = *pucFirstUserPriorityRegister;

        /* Use the same mask on the maximum system call priority. */
        ucMaxSysCallPriority = configMAX_SYSCALL_INTERRUPT_PRIORITY & ucMaxPriorityValue;

        /* Check that the maximum system call priority is nonzero after
         * accounting for the number of priority bits supported by the
         * hardware. A priority of 0 is invalid because setting the BASEPRI
         * register to 0 unmasks all interrupts, and interrupts with priority 0
         * cannot be masked using BASEPRI.
         * See https://www.FreeRTOS.org/RTOS-Cortex-M3-M4.html */
        configASSERT( ucMaxSysCallPriority );

        /* Check that the bits not implemented in hardware are zero in
         * configMAX_SYSCALL_INTERRUPT_PRIORITY. */
        configASSERT( ( configMAX_SYSCALL_INTERRUPT_PRIORITY & ( ~ucMaxPriorityValue ) ) == 0U );

        /* Calculate the maximum acceptable priority group value for the number
         * of bits read back. */

        while( ( ucMaxPriorityValue & portTOP_BIT_OF_BYTE ) == portTOP_BIT_OF_BYTE )
        {
            ulImplementedPrioBits++;
            ucMaxPriorityValue <<= ( uint8_t ) 0x01;
        }

        if( ulImplementedPrioBits == 8 )
        {
            /* When the hardware implements 8 priority bits, there is no way for
             * the software to configure PRIGROUP to not have sub-priorities. As
             * a result, the least significant bit is always used for sub-priority
             * and there are 128 preemption priorities and 2 sub-priorities.
             *
             * This may cause some confusion in some cases - for example, if
             * configMAX_SYSCALL_INTERRUPT_PRIORITY is set to 5, both 5 and 4
             * priority interrupts will be masked in Critical Sections as those
             * are at the same preemption priority. This may appear confusing as
             * 4 is higher (numerically lower) priority than
             * configMAX_SYSCALL_INTERRUPT_PRIORITY and therefore, should not
             * have been masked. Instead, if we set configMAX_SYSCALL_INTERRUPT_PRIORITY
             * to 4, this confusion does not happen and the behaviour remains the same.
             *
             * The following assert ensures that the sub-priority bit in the
             * configMAX_SYSCALL_INTERRUPT_PRIORITY is clear to avoid the above mentioned
             * confusion. */
            configASSERT( ( configMAX_SYSCALL_INTERRUPT_PRIORITY & 0x1U ) == 0U );
            ulMaxPRIGROUPValue = 0;
        }
        else
        {
            ulMaxPRIGROUPValue = portMAX_PRIGROUP_BITS - ulImplementedPrioBits;
        }

        /* Shift the priority group value back to its position within the AIRCR
         * register. */
        ulMaxPRIGROUPValue <<= portPRIGROUP_SHIFT;
        ulMaxPRIGROUPValue &= portPRIORITY_GROUP_MASK;

        /* Restore the clobbered interrupt priority register to its original
         * value. */
        *pucFirstUserPriorityRegister = ucOriginalPriority;
    }
    #endif /* configASSERT_DEFINED */

    /* Make PendSV and SysTick the lowest priority interrupts, and make SVCall
     * the highest priority. */
    portNVIC_SHPR3_REG |= portNVIC_PENDSV_PRI;
    portNVIC_SHPR3_REG |= portNVIC_SYSTICK_PRI;
    portNVIC_SHPR2_REG = 0;

    /* Start the timer that generates the tick ISR.  Interrupts are disabled
     * here already. */
    vPortSetupTimerInterrupt();

    /* Initialise the critical nesting count ready for the first task. */
    uxCriticalNesting = 0;

    /* Ensure the VFP is enabled - it should be anyway. */
    vPortEnableVFP();

    /* Lazy save always. */
    *( portFPCCR ) |= portASPEN_AND_LSPEN_BITS;

    /* Start the first task. */
    prvPortStartFirstTask();

    /* Should never get here as the tasks will now be executing!  Call the task
     * exit error function to prevent compiler warnings about a static function
     * not being called in the case that the application writer overrides this
     * functionality by defining configTASK_RETURN_ADDRESS.  Call
     * vTaskSwitchContext() so link time optimisation does not remove the
     * symbol. */
    vTaskSwitchContext();
    prvTaskExitError();

    /* Should not get here! */
    return 0;
}
```

### C. `vPortValidateInterruptPriority`（完整）

```c
void vPortValidateInterruptPriority( void )
{
    uint32_t ulCurrentInterrupt;
    uint8_t ucCurrentPriority;

    /* Obtain the number of the currently executing interrupt. */
    __asm volatile ( "mrs %0, ipsr" : "=r" ( ulCurrentInterrupt )::"memory" );

    /* Is the interrupt number a user defined interrupt? */
    if( ulCurrentInterrupt >= portFIRST_USER_INTERRUPT_NUMBER )
    {
        /* Look up the interrupt's priority. */
        ucCurrentPriority = pcInterruptPriorityRegisters[ ulCurrentInterrupt ];

        /* The following assertion will fail if a service routine (ISR) for
         * an interrupt that has been assigned a priority above
         * configMAX_SYSCALL_INTERRUPT_PRIORITY calls an ISR safe FreeRTOS API
         * function.  ISR safe FreeRTOS API functions must *only* be called
         * from interrupts that have been assigned a priority at or below
         * configMAX_SYSCALL_INTERRUPT_PRIORITY.
         *
         * Numerically low interrupt priority numbers represent logically high
         * interrupt priorities, therefore the priority of the interrupt must
         * be set to a value equal to or numerically *higher* than
         * configMAX_SYSCALL_INTERRUPT_PRIORITY.
         *
         * Interrupts that  use the FreeRTOS API must not be left at their
         * default priority of  zero as that is the highest possible priority,
         * which is guaranteed to be above configMAX_SYSCALL_INTERRUPT_PRIORITY,
         * and  therefore also guaranteed to be invalid.
         *
         * FreeRTOS maintains separate thread and ISR API functions to ensure
         * interrupt entry is as fast and simple as possible.
         *
         * The following links provide detailed information:
         * https://www.FreeRTOS.org/RTOS-Cortex-M3-M4.html
         * https://www.freertos.org/Why-FreeRTOS/FAQs */
        configASSERT( ucCurrentPriority >= ucMaxSysCallPriority );
    }

    /* Priority grouping:  The interrupt controller (NVIC) allows the bits
     * that define each interrupt's priority to be split between bits that
     * define the interrupt's pre-emption priority bits and bits that define
     * the interrupt's sub-priority.  For simplicity all bits must be defined
     * to be pre-emption priority bits.  The following assertion will fail if
     * this is not the case (if some bits represent a sub-priority).
     *
     * If the application only uses CMSIS libraries for interrupt
     * configuration then the correct setting can be achieved on all Cortex-M
     * devices by calling NVIC_SetPriorityGrouping( 0 ); before starting the
     * scheduler.  Note however that some vendor specific peripheral libraries
     * assume a non-zero priority group setting, in which cases using a value
     * of zero will result in unpredictable behaviour. */
    configASSERT( ( portAIRCR_REG & portPRIORITY_GROUP_MASK ) <= ulMaxPRIGROUPValue );
}
```
