# STM32驱动编译指令集合

本文档汇总了STM32平台下UART、Flash、ETH、BLE驱动的编译指令和配置说明。

## 目录结构

```
testcases/
├── uart_driver/          # UART驱动测试
│   ├── build.sh         # UART驱动构建脚本
│   └── clear.sh         # UART驱动清理脚本
├── flash_driver/        # Flash驱动测试
│   ├── build.sh         # Flash驱动构建脚本
│   └── clear.sh         # Flash驱动清理脚本
├── eth_driver/          # Ethernet驱动测试
│   ├── build.sh         # Ethernet驱动构建脚本
│   └── clear.sh         # Ethernet驱动清理脚本
├── ble_driver/          # BLE驱动测试
│   ├── build.sh         # BLE驱动构建脚本
│   └── clear.sh         # BLE驱动清理脚本
├── test_all_drivers.sh  # 一键测试所有驱动脚本
└── compile_commands.md  # 本文档
```

## 环境配置

### 1. Zephyr环境
```bash
# Zephyr源码目录
export ZEPHYR_BASE=/root/zephyr

# Zephyr SDK目录
export ZEPHYR_SDK_INSTALL_DIR=/root/zephyr-sdk-0.16.8

# 激活Zephyr环境
source $ZEPHYR_BASE/zephyr-env.sh
```

### 2. 工具链配置
```bash
# 使用Zephyr SDK工具链
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export CMAKE_PREFIX_PATH=$ZEPHYR_SDK_INSTALL_DIR/cmake
```

## 各驱动编译指令

### 1. UART驱动

**开发板**: STM32F4 Discovery (stm32f4_disco)
**示例应用**: samples/drivers/uart

```bash
# 进入UART驱动测试目录
cd testcases/uart_driver

# 构建UART驱动测试
./build.sh

# 使用其他STM32开发板
BOARD=stm32f3_disco ./build.sh
BOARD=nucleo_f411re ./build.sh
```

**构建参数**:
- `BOARD`: 目标开发板 (默认: stm32f4_disco)
- `APP_DIR`: 应用目录 (默认: samples/drivers/uart)
- `BUILD_DIR`: 构建输出目录 (默认: /tmp/zephyr_uart_build)

### 2. Flash驱动

**开发板**: STM32F4 Discovery (stm32f4_disco)
**示例应用**: samples/drivers/flash_shell

```bash
# 进入Flash驱动测试目录
cd testcases/flash_driver

# 构建Flash驱动测试
./build.sh

# 使用其他STM32开发板
BOARD=stm32f7_disco ./build.sh
```

**构建参数**:
- `BOARD`: 目标开发板 (默认: stm32f4_disco)
- `APP_DIR`: 应用目录 (默认: samples/drivers/flash_shell)
- `BUILD_DIR`: 构建输出目录 (默认: /tmp/zephyr_flash_build)

### 3. Ethernet驱动

**开发板**: STM32F7 Discovery (stm32f7_disco)
**示例应用**: samples/drivers/ethernet

```bash
# 进入Ethernet驱动测试目录
cd testcases/eth_driver

# 构建Ethernet驱动测试
./build.sh

# 使用其他STM32开发板（需支持Ethernet）
BOARD=stm32f429i_disc1 ./build.sh
```

**构建参数**:
- `BOARD`: 目标开发板 (默认: stm32f7_disco)
- `APP_DIR`: 应用目录 (默认: samples/drivers/ethernet)
- `BUILD_DIR`: 构建输出目录 (默认: /tmp/zephyr_eth_build)

### 4. BLE驱动

**开发板**: STM32WB55RG Nucleo (stm32wb55rg_nucleo)
**示例应用**: samples/bluetooth/peripheral

```bash
# 进入BLE驱动测试目录
cd testcases/ble_driver

# 构建BLE驱动测试
./build.sh

# 使用其他STM32 BLE开发板
BOARD=stm32wb5mmg_nucleo ./build.sh
```

**构建参数**:
- `BOARD`: 目标开发板 (默认: stm32wb55rg_nucleo)
- `APP_DIR`: 应用目录 (默认: samples/bluetooth/peripheral)
- `BUILD_DIR`: 构建输出目录 (默认: /tmp/zephyr_ble_build)

## 一键测试所有驱动

```bash
# 进入testcases目录
cd testcases

# 执行一键测试
./test_all_drivers.sh
```

**测试流程**:
1. 检查Zephyr环境
2. 依次构建UART、Flash、Ethernet、BLE驱动
3. 输出构建结果统计
4. 生成构建日志

## 环境变量参考

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `BOARD` | 驱动相关默认板型 | 目标STM32开发板型号 |
| `APP_DIR` | 驱动相关示例路径 | Zephyr示例应用路径 |
| `ZEPHYR_BASE` | `/root/zephyr` | Zephyr源码根目录 |
| `BUILD_DIR` | `/tmp/zephyr_*_build` | 构建输出目录 |
| `ZEPHYR_SDK_INSTALL_DIR` | `/root/zephyr-sdk-0.16.8` | Zephyr SDK安装目录 |
| `ZEPHYR_TOOLCHAIN_VARIANT` | `zephyr` | 工具链类型 |
| `CMAKE_PREFIX_PATH` | `$ZEPHYR_SDK_INSTALL_DIR/cmake` | CMake前缀路径 |

## 支持的STM32开发板

### UART驱动
- `stm32f4_disco` - STM32F4 Discovery (默认)
- `stm32f3_disco` - STM32F3 Discovery
- `nucleo_f411re` - STM32F411RE Nucleo
- `stm32f7_disco` - STM32F7 Discovery

### Flash驱动
- `stm32f4_disco` - STM32F4 Discovery (默认)
- `stm32f7_disco` - STM32F7 Discovery
- `nucleo_f429zi` - STM32F429ZI Nucleo

### Ethernet驱动
- `stm32f7_disco` - STM32F7 Discovery (默认，带Ethernet PHY)
- `stm32f429i_disc1` - STM32F429I Discovery
- `stm32h743zi_nucleo` - STM32H743ZI Nucleo

### BLE驱动
- `stm32wb55rg_nucleo` - STM32WB55RG Nucleo (默认，支持BLE)
- `stm32wb5mmg_nucleo` - STM32WB5MMG Nucleo
- `stm32wba52cg_nucleo` - STM32WBA52CG Nucleo

## 故障排除

### 常见构建错误

1. **开发板不支持**
   ```
   ERROR: board stm32xxx not found
   ```
   **解决方案**: 检查开发板名称是否正确，或使用`west boards`查看支持的开发板列表。

2. **工具链配置错误**
   ```
   ERROR: Could not find toolchain
   ```
   **解决方案**: 确保Zephyr SDK已正确安装，并设置`ZEPHYR_SDK_INSTALL_DIR`环境变量。

3. **权限不足**
   ```
   ERROR: Permission denied
   ```
   **解决方案**: 使用root权限执行，密码为`c508chenkaiqiu`:
   ```bash
   sudo -S <<< "c508chenkaiqiu" ./build.sh
   ```

4. **依赖缺失**
   ```
   ERROR: Missing required Python packages
   ```
   **解决方案**: 安装Zephyr Python依赖:
   ```bash
   pip install -r $ZEPHYR_BASE/scripts/requirements.txt
   ```

### 调试建议

1. **启用详细输出**:
   ```bash
   set -x  # 在build.sh开头添加
   ```

2. **检查构建日志**:
   ```bash
   cat $BUILD_DIR/build.log
   ```

3. **验证环境配置**:
   ```bash
   echo $ZEPHYR_BASE
   echo $ZEPHYR_SDK_INSTALL_DIR
   west --version
   ```

## 扩展使用

### 自定义应用测试

要测试自定义的驱动应用，修改`APP_DIR`环境变量:

```bash
# 测试自定义UART应用
APP_DIR=my_apps/uart_test ./build.sh

# 测试自定义Flash应用
APP_DIR=my_apps/flash_test ./build.sh
```

### 交叉编译配置

对于不同的工具链，设置`ZEPHYR_TOOLCHAIN_VARIANT`:

```bash
# 使用GNU ARM工具链
export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb

# 使用LLVM/Clang工具链
export ZEPHYR_TOOLCHAIN_VARIANT=llvm
```

### 构建选项配置

通过`west build`的`-D`选项传递CMake配置:

```bash
# 启用调试符号
west build -b stm32f4_disco samples/drivers/uart -DCMAKE_BUILD_TYPE=Debug

# 启用特定驱动功能
west build -b stm32f4_disco samples/drivers/uart -DCONFIG_UART_ASYNC_API=y
```

## 与LCMHalMCPServer集成

这些驱动测试可以与LCMHalMCPServer的驱动分析工具集成:

### 1. 创建CodeQL数据库
```bash
# 构建后创建驱动分析数据库
codeql database create zephyr-stm32-driver-db \
    --language=cpp \
    --source-root=/root/zephyr \
    --command="./test_all_drivers.sh"
```

### 2. 执行驱动安全分析
参考`ZEPHYR_DRIVER_TESTING_GUIDE.md`中的分析流程，对STM32驱动进行:
- 驱动函数调用链分析
- MMIO操作安全检查
- 中断处理安全评估
- 内存访问权限验证

---

*最后更新: 2025年12月5日*
*适用于: STM32系列开发板，Zephyr RTOS v3.5+*
