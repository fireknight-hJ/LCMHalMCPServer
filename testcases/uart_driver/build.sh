#!/bin/bash

# 构建 MMIO 测试驱动脚本
# 这个脚本构建包含直接MMIO操作的测试驱动，使用Zephyr兼容的API

# 获取当前脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)

echo "========================================"
echo "MMIO 测试驱动构建脚本 (Zephyr兼容)"
echo "========================================"
echo "构建目录: $SCRIPTDIR"
echo "构建时间: $(date)"
echo "========================================"

# 检查构建脚本是否存在
if [ ! -f "$SCRIPTDIR/build_mmio.sh" ]; then
    echo "错误: 未找到构建脚本 $SCRIPTDIR/build_mmio.sh"
    exit 1
fi

# 执行构建脚本
echo "执行构建脚本: $SCRIPTDIR/build_mmio.sh"
bash "$SCRIPTDIR/build_mmio.sh"

# 检查构建结果
BUILD_RESULT=$?
if [ $BUILD_RESULT -eq 0 ]; then
    echo "========================================"
    echo "MMIO 测试驱动构建成功!"
    echo "========================================"
    
    # 检查生成的ELF文件
    ELF_FILE="$SCRIPTDIR/emulate/output.elf"
    if [ -f "$ELF_FILE" ]; then
        echo "输出文件: $ELF_FILE"
        echo "文件大小: $(du -h "$ELF_FILE" | cut -f1)"
        echo "文件类型: $(file "$ELF_FILE")"
        
        # 显示函数符号
        echo ""
        echo "生成的函数符号 (MMIO相关):"
        if command -v nm >/dev/null 2>&1; then
            nm "$ELF_FILE" 2>/dev/null | grep -E "(mmio_|zephyr_|main)" | head -20 || echo "无法解析符号表"
        else
            echo "nm命令不可用，跳过符号显示"
        fi
    else
        echo "警告: 未找到生成的ELF文件: $ELF_FILE"
    fi
    
    exit 0
else
    echo "========================================"
    echo "MMIO 测试驱动构建失败!"
    echo "========================================"
    exit $BUILD_RESULT
fi
