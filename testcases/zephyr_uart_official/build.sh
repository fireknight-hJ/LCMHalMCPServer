#!/bin/bash

# Zephyr官方UART测试驱动构建脚本
# 基于Zephyr官方示例，包含MMIO操作

# 获取当前脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)
SRCDIR="$SCRIPTDIR/src"
BUILDDIR="$SCRIPTDIR/build"

echo "========================================"
echo "Zephyr官方UART测试驱动构建脚本"
echo "========================================"
echo "源代码目录: $SRCDIR"
echo "构建目录: $BUILDDIR"
echo "目标架构: ARM Cortex-M3"
echo "编译器: arm-none-eabi-gcc"
echo "Zephyr路径: /home/chenkaiqiu/LCMHalMCPServer/zephyr_official"
echo "========================================"

# 检查ARM工具链
if ! command -v arm-none-eabi-gcc >/dev/null 2>&1; then
    echo "错误: 未找到ARM工具链 (arm-none-eabi-gcc)"
    echo "请安装: sudo apt-get install gcc-arm-none-eabi"
    exit 1
fi

# 检查Zephyr头文件
if [ ! -d "/home/chenkaiqiu/LCMHalMCPServer/zephyr_official/include" ]; then
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
cmake "$SRCDIR" -DCMAKE_BUILD_TYPE=Debug

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
ELF_FILE="$BUILDDIR/zephyr_uart_official"
if [ -f "$ELF_FILE" ]; then
    echo "========================================"
    echo "Zephyr官方UART测试驱动构建成功!"
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
    
    # 显示符号信息
    echo ""
    echo "生成的函数符号 (MMIO相关):"
    if command -v arm-none-eabi-nm >/dev/null 2>&1; then
        arm-none-eabi-nm "$ELF_FILE" | grep -E "(mmio_|zephyr_|main|serial_cb|print_uart)" | head -20
    else
        nm "$ELF_FILE" | grep -E "(mmio_|zephyr_|main|serial_cb|print_uart)" | head -20
    fi
    
    # 创建配置文件
    echo ""
    echo "创建配置文件..."
    cat > "$SCRIPTDIR/lcmhal_config.yml" << EOF
# Zephyr官方UART测试配置
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
EOF
    
    echo "配置文件已创建: $SCRIPTDIR/lcmhal_config.yml"
    
    exit 0
else
    echo "错误: 未找到生成的ELF文件: $ELF_FILE"
    echo "检查构建目录: $BUILDDIR"
    ls -la "$BUILDDIR" || true
    exit 1
fi
