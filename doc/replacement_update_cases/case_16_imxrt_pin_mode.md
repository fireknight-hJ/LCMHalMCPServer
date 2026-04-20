# Case 16 - imxrt_pin_mode

## 背景

- Demo: `rtthread/imxrt1052-nxp-evk/uart`
- Function: `imxrt_pin_mode`
- 归类: `C_already_replaced_refined`
- 分类状态: `function_type=INIT`, `has_replacement=True`, `in_baseline=True`
- 关注问题: `compile,restore`

## 触发原因（ReplacementUpdate reason）

Fixed LOG_D macro call by putting the entire string literal on a single line to avoid compilation errors from unterminated string. The original had the string split across two lines causing syntax errors. Also added (void) casts for unused variables to avoid warnings.

## 源码与替换代码对应

- 原源码位置: `/home/haojie/rt-thread/bsp/nxp/imx/imxrt/libraries/drivers/drv_gpio.c`
- 行号: `522`
- RU 日志文件: `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_uart/lcmhal_ai_log/replacement_update_imxrt_pin_mode_20260407041741.json`

### 原函数源码片段（定位到行号附近）

```c
imxrt_isr(192, 0, GPIO13);
    imxrt_isr(192, 16, GPIO13);
    rt_interrupt_leave();
}
#endif
static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
```

### ReplacementUpdate 代码片段（最新版本）

```c
static void imxrt_pin_mode(rt_device_t dev, rt_base_t pin, rt_uint8_t mode)
{
    gpio_pin_config_t gpio;
    rt_int8_t port, pin_num;

#ifndef SOC_IMXRT1170_SERIES
    rt_uint32_t config_value = 0;
#endif

    port = pin >> 5;
    pin_num = pin & 31;

    if (PIN_INVALID_CHECK(port, pin_num))
    {
        LOG_D("invalid pin,rtt pin: %d,port: %d,pin: %d", pin, port + 1, pin_num);
        return;
    }

    gpio.outputLogic = 0;
    gpio.interruptMode = kGPIO_NoIntmode;

    switch (mode)
    {
    case PIN_MODE_OUTPUT:
    {
        gpio.direction = kGPIO_DigitalOutput;
#ifndef SOC_IMXRT1170_SERIES
        config_value = 0x0030U;    /* Drive Strength R0/6 */
// ... truncated ...
```

## 前因后果解读

- 前因: 该函数在仿真中触发了 `compile,restore` 相关问题。
- 动作: RU 对函数做了面向仿真的替换/修正，减少硬件依赖并保持接口语义。
- 后果: 该案例对应了 RU 的质量增量贡献，可用于论文中的定性论证。
