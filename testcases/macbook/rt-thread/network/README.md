# RT-Thread 网络示例

## 示例介绍

本示例演示了 RT-Thread 的网络功能，包括 TCP 客户端/服务器、UDP 客户端/服务器等基本网络通信操作。

## 使用的驱动

- **网络栈驱动**：RT-Thread 内置的网络协议栈
- **SAL (Socket Abstraction Layer)**：RT-Thread 套接字抽象层，提供 BSD Socket 兼容接口
- **TCP/IP 协议**：实现了完整的 TCP/IP 协议栈
- **UDP 协议**：用户数据报协议实现

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例包含以下网络通信功能：

1. **tcpserver.c**：TCP 服务器实现
2. **tcpclient.c**：TCP 客户端实现
3. **udpserver.c**：UDP 服务器实现
4. **udpclient.c**：UDP 客户端实现
5. **chargen.c**：字符生成协议实现
6. **tcp_server.py**：Python TCP 服务器（用于测试）
7. **tcp_client.py**：Python TCP 客户端（用于测试）

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/network
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/network
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以看到网络服务的运行状态。

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接到网络
3. 可以通过 Python 测试脚本与开发板进行网络通信
4. 通过串口终端查看运行输出