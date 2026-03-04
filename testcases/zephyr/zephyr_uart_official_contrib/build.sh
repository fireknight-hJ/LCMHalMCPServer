#!/bin/bash

# Zephyr官方UART驱动测试构建脚本
# 用于开源贡献的测试用例
# 目标：支持flash的ARM板子（STM32F103C8T6 Blue Pill）

# 获取当前脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)
SRCDIR="$SCRIPTDIR/src"
BUILDDIR="$SCRIPTDIR/build"

echo "========================================"
echo "Zephyr官方UART驱动测试构建脚本"
echo "用于开源贡献"
echo "========================================"
echo "源代码目录: $SRCDIR"
echo "构建目录: $BUILDDIR"
echo "目标板子: STM32F103C8T6 (Blue Pill)"
echo "目标架构: ARM Cortex-M3"
echo "编译器: arm-none-eabi-gcc"
echo "Zephyr路径: /home/ckq/LCMHalMCPServer/zephyr_official"
echo "========================================"

# 检查ARM工具链
if ! command -v arm-none-eabi-gcc >/dev/null 2>&1; then
    echo "错误: 未找到ARM工具链 (arm-none-eabi-gcc)"
    echo "请安装: sudo apt-get install gcc-arm-none-eabi"
    exit 1
fi

# 检查Zephyr头文件
if [ ! -d "/home/ckq/LCMHalMCPServer/zephyr_official/include" ]; then
    echo "错误: 未找到Zephyr头文件"
    echo "请确保Zephyr仓库已克隆到正确位置"
    exit 1
fi

# 检查源代码
if [ ! -f "$SRCDIR/main.c" ]; then
    echo "错误: 未找到测试驱动源代码: $SRCDIR/main.c"
    exit 1
fi

# 检查链接器脚本
if [ ! -f "$SRCDIR/linker.ld" ]; then
    echo "错误: 未找到链接器脚本: $SRCDIR/linker.ld"
    exit 1
fi

# 清理之前的构建
if [ -d "$BUILDDIR" ]; then
    echo "清理之前的构建..."
    rm -rf "$BUILDDIR"
fi

# 创建构建目录
mkdir -p "$BUILDDIR"
cd "$BUILDDIR" || exit 1

# 配置CMake (ARM交叉编译)
echo "配置CMake (ARM交叉编译)..."
if [ -f "$SRCDIR/toolchain.cmake" ]; then
    echo "使用toolchain.cmake文件..."
    cmake "$SRCDIR" \
        -DCMAKE_BUILD_TYPE=Debug \
        -DCMAKE_TOOLCHAIN_FILE="$SRCDIR/toolchain.cmake"
else
    echo "使用默认CMake配置..."
    cmake "$SRCDIR" -DCMAKE_BUILD_TYPE=Debug
fi

if [ $? -ne 0 ]; then
    echo "错误: CMake配置失败"
    exit 1
fi

# 构建
echo "开始构建..."
make -j$(nproc)

if [ $? -ne 0 ]; then
    echo "错误: 构建失败"
    exit 1
fi

# 检查构建结果
ELF_FILE="$BUILDDIR/zephyr_uart_contrib.elf"
if [ -f "$ELF_FILE" ]; then
    echo "========================================"
    echo "Zephyr官方UART驱动测试构建成功!"
    echo "========================================"
    echo "输出文件: $ELF_FILE"
    echo "文件大小: $(du -h "$ELF_FILE" | cut -f1)"
    echo "文件类型: $(file "$ELF_FILE")"
    
    # 复制到emulate目录
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    
    cp -f "$ELF_FILE" "$SCRIPTDIR/emulate/output.elf"
    echo "已复制到: $SCRIPTDIR/emulate/output.elf"
    
    # 创建根目录的符号链接，以便tools/builder/core.py能找到
    ln -sf "$SCRIPTDIR/emulate/output.elf" "$SCRIPTDIR/output.elf"
    echo "已创建符号链接: $SCRIPTDIR/output.elf -> $SCRIPTDIR/emulate/output.elf"
    
    # 显示符号信息
    echo ""
    echo "生成的函数符号 (UART相关):"
    if command -v arm-none-eabi-nm >/dev/null 2>&1; then
        arm-none-eabi-nm "$ELF_FILE" | grep -E "(uart_|main|test_|HAL_BE)" | head -20
    else
        nm "$ELF_FILE" | grep -E "(uart_|main|test_|HAL_BE)" | head -20
    fi
    
    # 显示段信息
    echo ""
    echo "段信息:"
    if command -v arm-none-eabi-size >/dev/null 2>&1; then
        arm-none-eabi-size "$ELF_FILE"
    else
        size "$ELF_FILE" 2>/dev/null || echo "无法获取段信息"
    fi
    
    # 创建配置文件
    echo ""
    echo "创建配置文件..."
    cat > "$SCRIPTDIR/lcmhal_config.yml" << EOF
# Zephyr官方UART驱动测试配置 - 用于开源贡献
script_path: "$SCRIPTDIR"
db_path: "$SCRIPTDIR/codeql_db"
src_path: "$SRCDIR"
proj_path: "$SCRIPTDIR"

# 构建配置
build_command: "bash $SCRIPTDIR/build.sh"
build_dir: "$BUILDDIR"

# 模拟器配置
emulate_dir: "$SCRIPTDIR/emulate"
entry_point: "0x8000201"

# 目标板子信息
target_board: "STM32F103C8T6 (Blue Pill)"
target_cpu: "ARM Cortex-M3"
flash_size: "64KB"
ram_size: "20KB"

# 测试配置
test_cases:
  - name: "uart_echo_test"
    description: "UART回显测试"
  - name: "uart_performance_test"
    description: "UART性能测试"
  - name: "uart_error_handling_test"
    description: "UART错误处理测试"
EOF
    
    echo "配置文件已创建: $SCRIPTDIR/lcmhal_config.yml"
    
    # 创建简单的输入文件
    echo "创建测试输入文件..."
    echo "TEST" > "$SCRIPTDIR/emulate/input.txt"
    echo -n "TEST" > "$SCRIPTDIR/emulate/base_input/input.bin" 2>/dev/null || mkdir -p "$SCRIPTDIR/emulate/base_input" && echo -n "TEST" > "$SCRIPTDIR/emulate/base_input/input.bin"
    
    echo "========================================"
    echo "测试用例准备完成!"
    echo "可以运行: python3 /home/ckq/LCMHalMCPServer/main.py $SCRIPTDIR"
    echo "========================================"
    
    exit 0
else
    echo "错误: 未找到生成的ELF文件: $ELF_FILE"
    echo "检查构建目录: $BUILDDIR"
    ls -la "$BUILDDIR" || true
    exit 1
fi