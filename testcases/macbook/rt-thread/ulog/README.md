# RT-Thread ULOG 日志系统示例

## 示例介绍

本示例演示了 RT-Thread 的 ULOG 日志系统功能，包括不同级别的日志输出、日志过滤和 syslog 兼容模式。

## 使用的驱动

- **ULOG 日志系统**：RT-Thread 内置的轻量级日志系统
- **控制台驱动**：用于将日志输出到串口终端
- **Syslog 兼容层**：支持标准 Syslog API 的兼容模式

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例展示了 ULOG 日志系统的以下功能：

1. **多级别日志输出**：
   - DEBUG 级别（LOG_D/ulog_d）
   - INFO 级别（LOG_I/ulog_i）
   - WARNING 级别（LOG_W/ulog_w）
   - ERROR 级别（LOG_E/ulog_e）

2. **两种使用模式**：
   - ULOG 原生模式：使用 RT-Thread 特有的日志 API
   - Syslog 兼容模式：使用标准 Syslog API

3. **日志过滤功能**：
   - 全局日志级别过滤
   - 基于标签（tag）的日志级别过滤
   - 支持静默模式和全级别输出模式切换

4. **动态配置**：
   - 运行时修改日志过滤级别
   - 实时调整日志输出行为

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/ulog
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/ulog
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以看到日志输出。

在 MSH 命令行中运行：
```
ulog_example
```

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 需要启用 RT-Thread 的 ULOG 功能（`ULOG_USING_SYSLOG` 或 `ULOG_USING_FILTER`）
4. 通过串口终端查看日志输出
5. 日志输出频率会根据随机延迟有所变化