# Case 09 - vPortEndScheduler

## 背景

- Demo: `nxp/NXP_FATFS_FreeRTOS`
- Function: `vPortEndScheduler`
- 归类: `A_RU_only_not_replaced`
- 分类状态: `function_type=NA`, `has_replacement=False`, `in_baseline=False`
- 关注问题: `loop/hang`

## 触发原因（ReplacementUpdate reason）

vPortEndScheduler contains configASSERT(uxCriticalNesting == 1000UL) which always fails, causing an exceptional loop in emulation. This prevents the application from terminating normally when vTaskEndScheduler() is called. The function is essentially a stub for ports with 'nothing to return to'. In emulation context, we need to allow graceful termination without triggering assertion failures that cause exceptional loops.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/mcuxsdk-workspace/mcuxsdk/rtos/freertos/freertos-kernel/portable/GCC/ARM_CM4F/port.c`
- 行号: `467`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_FreeRTOS/lcmhal_ai_log/replacement_update_vPortEndScheduler_20260406202300.json`

### 原函数源码片段（定位到行号附近）

```c
    /* Should not get here! */
    return 0;
}
/*-----------------------------------------------------------*/

void vPortEndScheduler( void )
{
    /* Not implemented in ports where there is nothing to return to.
     * Artificially force an assert. */
    configASSERT( uxCriticalNesting == 1000UL );
}
/*-----------------------------------------------------------*/

void vPortEnterCritical( void )
{
    portDISABLE_INTERRUPTS();
    uxCriticalNesting++;
```

### ReplacementUpdate 代码片段（最新版本）

```c
void vPortEndScheduler( void )
{
    /* In emulation, we need to allow the scheduler to end gracefully.
     * The original implementation has an assertion that always fails.
     * Simply return to allow normal termination. */
    return;
}
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `loop/hang` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的覆盖增量贡献，可用于论文中的定性论证。
