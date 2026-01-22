# RT-Thread RT-Link 示例

## 示例介绍

本示例演示了 RT-Thread 的 RT-Link 通信协议功能，包括短帧和长帧通信、传输速率测试等功能。

## 使用的驱动

- **RT-Link 协议**：RT-Thread 轻量级通信协议，支持可靠传输和多服务通信
- **服务管理**：支持多种服务类型的注册和管理
- **数据缓冲**：动态数据缓冲管理，支持不同大小的数据传输
- **回调机制**：发送和接收回调函数，实现异步通信

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例包含以下 RT-Link 通信功能：

1. **rtlink_example.c**：
   - 演示 RT-Link 协议的基本通信功能
   - 支持短帧和长帧传输测试
   - 实现数据发送和接收的回调函数
   - 提供传输速率测试功能
   - 支持多种服务类型（socket、wifi等）

2. **rtlink_dev_example.c**：
   - RT-Link 设备层示例
   - 演示设备与 RT-Link 协议的集成

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/rt-link
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/rt-link
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以看到 RT-Link 通信的运行状态。

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 需要启用 RT-Thread 的 RT-Link 功能（`RT_USING_RT_LINK`）
4. 通过串口终端查看运行输出和传输速率测试结果