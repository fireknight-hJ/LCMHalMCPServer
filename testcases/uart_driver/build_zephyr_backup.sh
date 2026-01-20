#!/bin/bash

# STM32 UART驱动构建脚本
# 用于编译STM32F4 Discovery开发板的UART驱动示例

# 设置Zephyr环境
ZEPHYR_BASE=${ZEPHYR_BASE:-/home/chenkaiqiu/zephyr}
ZEPHYR_SDK=${ZEPHYR_SDK:-/home/chenkaiqiu/zephyr-sdk-0.16.8}

# 获取当前脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)

# 检查Zephyr环境
if [ ! -d "$ZEPHYR_BASE" ]; then
    echo "错误: Zephyr环境目录不存在: $ZEPHYR_BASE"
    echo "请设置ZEPHYR_BASE环境变量或安装Zephyr SDK"
    exit 1
fi

# 设置开发板和应用
BOARD=${BOARD:-stm32f4_disco}
APP=${APP:-samples/drivers/uart/echo_bot}

# 输出构建信息
echo "========================================"
echo "STM32 UART驱动构建脚本"
echo "========================================"
echo "开发板: $BOARD"
echo "应用: $APP"
echo "Zephyr目录: $ZEPHYR_BASE"
echo "构建目录: $SCRIPTDIR/build"
echo "========================================"

# 切换到Zephyr目录
echo "切换到Zephyr目录: $ZEPHYR_BASE"
cd "$ZEPHYR_BASE" || {
    echo "错误: 无法切换到Zephyr目录 $ZEPHYR_BASE"
    exit 1
}

# 设置环境变量
export ZEPHYR_BASE
export ZEPHYR_SDK

# 激活Zephyr环境
if [ -f "$ZEPHYR_BASE/zephyr-env.sh" ]; then
    echo "激活Zephyr环境..."
    source "$ZEPHYR_BASE/zephyr-env.sh"
else
    echo "警告: 未找到zephyr-env.sh，尝试使用默认环境"
fi

# 清理之前的构建
if [ -d "$SCRIPTDIR/build" ]; then
    echo "清理之前的构建..."
    rm -rf "$SCRIPTDIR/build"
fi

# 创建构建目录
mkdir -p "$SCRIPTDIR/build"

# 开始构建
echo "开始构建UART驱动..."
echo "使用命令: west build -b $BOARD $APP --build-dir $SCRIPTDIR/build"

# 执行构建
west build -b "$BOARD" "$APP" --build-dir "$SCRIPTDIR/build"

# 检查构建结果
if [ $? -eq 0 ]; then
    echo "========================================"
    echo "UART驱动构建成功!"
    echo "========================================"
    
    # 创建emulate目录
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    
    # 复制生成的可执行文件
    ELF_FILE="$SCRIPTDIR/build/zephyr/zephyr.elf"
    if [ -f "$ELF_FILE" ]; then
        echo "复制可执行文件到: $SCRIPTDIR/emulate/output.elf"
        cp -f "$ELF_FILE" "$SCRIPTDIR/emulate/output.elf"
        echo "文件大小: $(du -h "$SCRIPTDIR/emulate/output.elf" | cut -f1)"
    else
        echo "警告: 未找到生成的ELF文件"
    fi
    
    # 显示构建信息
    echo ""
    echo "构建完成!"
    echo "输出文件: $SCRIPTDIR/emulate/output.elf"
    echo "构建目录: $SCRIPTDIR/build"
    
    exit 0
else
    echo "========================================"
    echo "UART驱动构建失败!"
    echo "========================================"
    exit 1
fi
