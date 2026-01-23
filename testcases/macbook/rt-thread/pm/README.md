# RT-Thread 电源管理示例

## 示例介绍

本示例演示了 RT-Thread 的电源管理功能，包括系统睡眠模式和唤醒机制的实现。

## 使用的驱动

- **电源管理驱动**：RT-Thread 内置的电源管理框架
- **定时器驱动**：支持在睡眠模式下的定时器唤醒功能
- **GPIO 驱动**：支持外部引脚中断唤醒功能
- **软定时器**：用于在睡眠模式下的定时任务

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例包含以下电源管理功能：

1. **timer_app.c**：
   - 演示使用软定时器在深度睡眠模式下唤醒系统
   - 定期打印当前系统 tick 值
   - 使用 `rt_pm_request(PM_SLEEP_MODE_DEEP)` 请求进入深度睡眠模式

2. **wakeup_app.c**：
   - 演示使用外部引脚中断唤醒系统
   - 当外部引脚触发下降沿中断时，唤醒系统并控制 LED 闪烁
   - 使用 `rt_pm_request()` 和 `rt_pm_release()` 管理电源模式

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/pm
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/pm
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以看到电源管理功能的运行状态。

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 需要启用 RT-Thread 的电源管理功能（`RT_USING_PM`）
4. 需要启用软定时器功能（`RT_USING_TIMER_SOFT`）
5. 通过串口终端查看运行输出