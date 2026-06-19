# Case 08 - prvTaskExitError

## 背景

- Demo: `nxp/NXP_FATFS_FreeRTOS`
- Function: `prvTaskExitError`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang`

## 触发原因（ReplacementUpdate reason）

prvTaskExitError contains an assertion that would always fail (configASSERT( uxCriticalNesting == ~0UL )) followed by an infinite loop. In emulation, we don't want assertion failures or infinite loops. The replacement just returns to allow graceful error handling. This function is called from xPortStartScheduler if the scheduler fails to start, but in emulation we want to avoid hard failures.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/rtos/freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.c`
- 行号: `234`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_prvTaskExitError_20260406204823.json`

### 原函数源码片段（定位到行号附近）

```c

    return pxTopOfStack;
}
/*-----------------------------------------------------------*/

static void prvTaskExitError( void )
{
    volatile uint32_t ulDummy = 0;

    /* A function that implements a task must not exit or attempt to return to
     * its caller as there is nothing to return to.  If a task wants to exit it
     * should instead call vTaskDelete( NULL ).
     *
     * Artificially force an assert() to be triggered if configASSERT() is
     * defined, then stop here so application writers can catch the error. */
    configASSERT( uxCriticalNesting == ~0UL );
    portDISABLE_INTERRUPTS();
```

### ReplacementUpdate 代码片段（最新版本）

```c
static void prvTaskExitError( void )
{
    /* In emulation, we don't want to trigger assertion failures or enter infinite loops.
     * The original function has configASSERT( uxCriticalNesting == ~0UL ) which would fail,
     * followed by an infinite loop. Instead, we just return to allow graceful error handling. */
    return;
}
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `loop/hang` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
