#!/bin/bash

# STM32 BLE驱动清理脚本
# 用于删除BLE驱动构建过程中生成的中间文件

# 获取当前脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)

echo "========================================"
echo "STM32 BLE驱动清理脚本"
echo "========================================"
echo "清理目录: $SCRIPTDIR"
echo "========================================"

# 清理构建目录
if [ -d "$SCRIPTDIR/build" ]; then
    echo "删除构建目录: $SCRIPTDIR/build"
    rm -rf "$SCRIPTDIR/build"
    echo "✅ 构建目录已删除"
else
    echo "⚠️  构建目录不存在: $SCRIPTDIR/build"
fi

# 清理emulate目录
if [ -d "$SCRIPTDIR/emulate" ]; then
    echo "删除emulate目录: $SCRIPTDIR/emulate"
    rm -rf "$SCRIPTDIR/emulate"
    echo "✅ emulate目录已删除"
else
    echo "⚠️  emulate目录不存在: $SCRIPTDIR/emulate"
fi

# 清理其他可能存在的中间文件
echo "清理其他中间文件..."
find "$SCRIPTDIR" -name "*.o" -type f -delete 2>/dev/null && echo "✅ 删除目标文件(*.o)"
find "$SCRIPTDIR" -name "*.d" -type f -delete 2>/dev/null && echo "✅ 删除依赖文件(*.d)"
find "$SCRIPTDIR" -name "*.elf" -type f -delete 2>/dev/null && echo "✅ 删除ELF文件(*.elf)"
find "$SCRIPTDIR" -name "*.bin" -type f -delete 2>/dev/null && echo "✅ 删除二进制文件(*.bin)"
find "$SCRIPTDIR" -name "*.hex" -type f -delete 2>/dev/null && echo "✅ 删除HEX文件(*.hex)"
find "$SCRIPTDIR" -name "*.map" -type f -delete 2>/dev/null && echo "✅ 删除映射文件(*.map)"
find "$SCRIPTDIR" -name "*.lst" -type f -delete 2>/dev/null && echo "✅ 删除列表文件(*.lst)"

echo ""
echo "========================================"
echo "清理完成!"
echo "========================================"
echo "所有构建中间文件已删除"
echo "可以重新运行 build.sh 进行构建"
echo "========================================"
