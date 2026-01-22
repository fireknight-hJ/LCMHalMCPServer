# RT-Thread YModem 协议示例

## 示例介绍

本示例演示了 RT-Thread 的 YModem 协议实现，用于通过串口进行可靠的文件传输。YModem 是一种常用的文件传输协议，支持错误检测和纠正功能。

## 使用的驱动

- **YModem 协议驱动**：RT-Thread 内置的 YModem 协议实现
- **UART 串口驱动**：用于通过串口进行数据传输
- **虚拟串口驱动**：用于在模拟器或开发板上提供虚拟串口功能
- **文件系统驱动**：用于将接收到的文件保存到文件系统（仅在 tofile.c 中使用）

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例包含以下 YModem 协议功能：

1. **echo.c**：
   - 演示 YModem 协议的基本功能
   - 将接收到的数据通过串口回显
   - 提供 `rym_cat_to_dev` 函数用于在两个设备之间传输数据
   - 提供 `rym_cat_vcom` 命令行接口函数

2. **null.c**：
   - 实现一个简单的 YModem 接收功能
   - 将接收到的数据直接丢弃（类似 /dev/null）

3. **tofile.c**：
   - 实现 YModem 协议的文件接收功能
   - 将接收到的文件保存到文件系统
   - 支持文件系统操作

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/ymodem
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/ymodem
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以使用 Msh 命令行运行示例：

```
msh > rym_cat_vcom
```

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 需要启用 RT-Thread 的 YModem 功能（`RT_USING_YMODEM`）
4. 需要启用 Finsh/Msh 命令行功能（`RT_USING_FINSH`）
5. 通过串口终端与开发板进行 YModem 文件传输
6. 确保串口波特率设置正确（默认通常为 115200bps）