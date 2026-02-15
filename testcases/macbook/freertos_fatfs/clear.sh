#!/bin/bash

# FreeRTOS FatFs 示例项目清理脚本
# 用于删除构建缓存和生成的文件

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/FatFs_USBDisk_RTOS
# 获取当前shell脚本所在目录
SCRIPTDIR=/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_fatfs

# 清理构建缓存
if [ -d "$PWDDIR" ]; then
    echo "清理构建缓存..."
    cd "$PWDDIR" || {
        echo "错误: 无法切换到目录 $PWDDIR"
        exit 1
    }
    # 假设项目使用make构建系统
    make clean 2>/dev/null || echo "无构建缓存需要清理"
fi

# 清理生成的文件
if [ -f "$SCRIPTDIR/output.elf" ]; then
    echo "清理生成的可执行文件..."
    rm -f "$SCRIPTDIR/output.elf"
fi

echo "清理完成!"
