# RT-Thread 变量导出示例

## 示例介绍

本示例演示了 RT-Thread 的变量导出（var_export）功能，允许将变量导出到特定的内存区域，并在运行时动态查询和访问这些变量。

## 使用的驱动

- **var_export 模块**：RT-Thread 内置的变量导出模块，用于管理导出的变量
- **内存管理**：用于在特定内存区域分配和管理导出的变量

## 使用的板子

- **HiFive1**：基于 RISC-V 架构的开发板，由 SiFive 公司设计
- **平台**：RISC-V 64 位处理器

## 示例功能

本示例展示了 var_export 模块的以下功能：

1. **变量导出**：
   - 使用 `VAR_EXPORT(module_name, identifier, value)` 宏将变量导出到特定模块
   - 支持将多个变量导出到不同的模块
   - 导出的变量存储在特定的内存区域

2. **变量查询**：
   - 通过模块名初始化查询模块
   - 使用迭代器遍历同一模块下的所有导出变量
   - 根据标识符查询特定变量的值
   - 检查变量是否存在

3. **命令行接口**：
   - 通过 Finsh/Msh 命令行调用 `found_by_module` 函数
   - 在命令行中动态查询导出的变量

## 构建和运行

### 构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/var_export
chmod +x build.sh
./build.sh
```

### 清除构建

```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/var_export
chmod +x clear.sh
./clear.sh
```

### 运行

将生成的 `rtthread.elf` 文件烧录到 HiFive1 开发板上，通过串口终端可以使用 Msh 命令行运行示例：

```
msh > found_by_module
```

## 注意事项

1. 本示例需要在 HiFive1 开发板上运行
2. 确保开发板已正确连接并配置
3. 需要启用 RT-Thread 的 var_export 功能（`RT_USING_VAR_EXPORT`）
4. 需要启用 Finsh/Msh 命令行功能（`RT_USING_FINSH`）
5. 通过串口终端查看运行输出