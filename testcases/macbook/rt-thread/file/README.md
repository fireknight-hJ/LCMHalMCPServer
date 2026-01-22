# RT-Thread 文件系统示例

## 示例介绍

本示例演示了 RT-Thread 的文件系统功能，包括文件的读写、创建、删除、目录操作等基本文件系统操作。

## 使用的驱动

- **DFS (Device File System)**：RT-Thread 设备文件系统驱动，提供了统一的文件操作接口
- **虚拟文件系统**：支持多种文件系统格式（如 FAT、EXT2、RAMFS 等）

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例包含以下文件操作功能：

1. **readwrite.c**：文件读写测试
2. **listdir.c**：目录列表操作
3. **readspeed.c**：文件读取速度测试
4. **writespeed.c**：文件写入速度测试
5. **seekdir.c**：目录查找操作

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/file
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/file
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以看到运行结果。

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 可以通过串口终端查看运行输出