# STM32外设构建脚本

## 概述

本项目包含两个STM32外设驱动的构建脚本，用于编译和测试STM32平台下的外设驱动示例。这些脚本基于Zephyr RTOS构建系统，可以方便地编译和测试不同的STM32开发板和外设驱动。

## 创建的构建脚本

### 1. 以太网驱动构建脚本 (`eth_driver/build.sh`)

**目标**: 编译STM32F7 Discovery开发板的Ethernet驱动示例

**主要特性**:
- 使用STM32F7 Discovery开发板 (`stm32f7_disco`)
- 编译Zephyr的Ethernet驱动示例 (`zephyr/samples/drivers/ethernet`)
- 自动检测Zephyr环境
- 支持环境变量覆盖 (BOARD, APP, ZEPHYR_BASE, ZEPHYR_SDK)
- 自动创建构建目录和输出目录
- 生成的可执行文件保存到 `emulate/output.elf`

**使用方法**:
```bash
cd testcases/eth_driver
# 使用默认配置
./build.sh

# 使用自定义开发板
BOARD=stm32f769i_disco ./build.sh

# 使用自定义Zephyr路径
ZEPHYR_BASE=/path/to/zephyr ./build.sh
```

### 2. Flash驱动构建脚本 (`flash_driver/build.sh`)

**目标**: 编译STM32F4 Discovery开发板的Flash驱动示例

**主要特性**:
- 使用STM32F4 Discovery开发板 (`stm32f4_disco`)
- 编译Zephyr的Flash驱动示例 (`zephyr/samples/drivers/flash_shell`)
- 自动检测Zephyr环境
- 支持环境变量覆盖 (BOARD, APP, ZEPHYR_BASE, ZEPHYR_SDK)
- 自动创建构建目录和输出目录
- 生成的可执行文件保存到 `emulate/output.elf`

**使用方法**:
```bash
cd testcases/flash_driver
# 使用默认配置
./build.sh

# 使用自定义开发板
BOARD=stm32f429i_disco ./build.sh

# 使用自定义Zephyr路径
ZEPHYR_BASE=/path/to/zephyr ./build.sh
```

## 环境要求

### 必需组件
1. **Zephyr RTOS**: 需要安装Zephyr SDK和构建系统
2. **west工具**: Zephyr的构建工具
3. **ARM GCC工具链**: 用于编译STM32目标

### 环境变量
脚本使用以下环境变量:
- `ZEPHYR_BASE`: Zephyr源代码路径 (默认: `/root/zephyr`)
- `ZEPHYR_SDK`: Zephyr SDK路径 (默认: `/root/zephyr-sdk-0.16.8`)
- `BOARD`: 目标开发板 (可覆盖默认值)
- `APP`: 要编译的应用程序 (可覆盖默认值)

## 脚本结构

两个构建脚本具有相同的结构:

1. **环境检查**: 验证Zephyr环境是否存在
2. **参数设置**: 设置开发板、应用和构建目录
3. **环境激活**: 激活Zephyr构建环境
4. **构建执行**: 使用west工具执行构建
5. **结果处理**: 复制生成的可执行文件到输出目录

## 测试工具

项目包含一个测试脚本 `test_stm32_build_scripts.sh`，用于验证构建脚本的基本功能:

```bash
cd testcases
./test_stm32_build_scripts.sh
```

测试工具会检查:
- 脚本文件是否存在
- 脚本语法是否正确
- 关键配置是否正确
- 文件权限是否设置

## 故障排除

### 常见问题

1. **Zephyr环境未找到**
   ```
   错误: Zephyr环境目录不存在: /root/zephyr
   ```
   **解决方案**: 设置正确的ZEPHYR_BASE环境变量
   ```bash
   export ZEPHYR_BASE=/path/to/your/zephyr
   ```

2. **west命令未找到**
   ```
   ./build.sh: line XX: west: command not found
   ```
   **解决方案**: 确保Zephyr环境已正确激活
   ```bash
   source $ZEPHYR_BASE/zephyr-env.sh
   ```

3. **开发板不支持**
   ```
   ERROR: Unknown board stm32f7_disco
   ```
   **解决方案**: 检查开发板名称或使用支持的开发板
   ```bash
   BOARD=stm32f769i_disco ./build.sh
   ```

### 调试模式

要查看详细的构建信息，可以在运行脚本前设置调试环境变量:
```bash
export ZEPHYR_VERBOSE=1
./build.sh
```

## 扩展指南

### 添加新的构建脚本

要添加新的STM32外设构建脚本，可以复制现有脚本并修改以下部分:

1. **开发板配置**: 修改`BOARD`默认值
2. **应用配置**: 修改`APP`默认值
3. **脚本描述**: 更新echo输出和注释

### 支持的STM32开发板

以下是一些常用的STM32开发板，可以与这些脚本一起使用:

- `stm32f4_disco` - STM32F4 Discovery
- `stm32f7_disco` - STM32F7 Discovery  
- `stm32f769i_disco` - STM32F769I Discovery
- `stm32f429i_disco` - STM32F429I Discovery
- `nucleo_f411re` - STM32F411RE Nucleo
- `nucleo_f746zg` - STM32F746ZG Nucleo

### 支持的Zephyr示例

以下是一些常用的Zephyr驱动示例:

- `zephyr/samples/drivers/uart/echo_bot` - UART回显示例
- `zephyr/samples/drivers/i2c/i2c_scan` - I2C扫描示例
- `zephyr/samples/drivers/spi/spi_loopback` - SPI回环测试
- `zephyr/samples/drivers/adc/adc_simple` - ADC简单示例
- `zephyr/samples/drivers/pwm/pwm_led` - PWM控制LED

## 许可证

这些构建脚本是LCMHalMCPServer项目的一部分，遵循项目的许可证条款。

## 更新日志

### 2026-01-06
- 创建了两个STM32外设构建脚本
  - 以太网驱动构建脚本 (`eth_driver/build.sh`)
  - Flash驱动构建脚本 (`flash_driver/build.sh`)
- 创建了测试工具 (`test_stm32_build_scripts.sh`)
- 创建了本文档

## 联系信息

如有问题或建议，请参考LCMHalMCPServer项目的主README文件。
