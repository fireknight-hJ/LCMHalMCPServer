#!/bin/bash

# FreeRTOS FatFs 示例项目构建脚本
# 用于编译 FatFs_USBDisk_RTOS 项目

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/FatFs_USBDisk_RTOS/STM32CubeIDE/Release
# 获取当前shell脚本所在目录
SCRIPTDIR=/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_fatfs

# 检查目录是否存在
if [ ! -d "$PWDDIR" ]; then
    echo "错误: 构建目录不存在: $PWDDIR"
    exit 1
fi

# 切换工作目录到项目所在目录
echo "切换到构建目录: $PWDDIR"
cd "$PWDDIR" || {
    echo "错误: 无法切换到目录 $PWDDIR"
    exit 1
}

# 编译项目
echo "开始编译项目..."
# 假设项目使用make构建系统
make

# 检查编译结果
if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    # 移动生成的可执行文件到脚本目录
    if [ ! -d "$SCRIPTDIR" ]; then
        mkdir -p "$SCRIPTDIR"
    fi
    # 检查是否存在可执行文件
    if [ -f "FatFs_USBDisk_RTOS.elf" ]; then
        # 移动可执行文件到脚本目录
        mv -f "FatFs_USBDisk_RTOS.elf" "$SCRIPTDIR/output.elf" || {
            echo "错误: 无法移动可执行文件到 $SCRIPTDIR/output.elf"
            exit 1
        }
    elif [ -f "output.elf" ]; then
        # 如果已经是output.elf，直接复制
        cp -f "output.elf" "$SCRIPTDIR/output.elf" || {
            echo "错误: 无法复制可执行文件到 $SCRIPTDIR/output.elf"
            exit 1
        }
    else
        echo "错误: 未找到可执行文件"
        exit 1
    fi
else
    echo "编译失败!"
    exit 1
fi
