#!/bin/bash

# FreeRTOS LwIP Streaming Server 项目构建脚本
# 用于编译STM32F769I_EVAL平台的LwIP流媒体服务器项目

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer/SW4STM32/STM32F769I_EVAL/build
# 获取当前shell脚本所在目录
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)

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
make all

# 检查编译结果
if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    # 创建 emulate 目录
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    # 移动可执行文件到 emulate 目录
    mv -f "LwIP_StreamingServer.elf" "$SCRIPTDIR/emulate/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/emulate/output.elf"
        exit 1
    }
    
    # 从 ELF 文件生成二进制镜像文件 output.bin
    echo "从 ELF 文件生成 output.bin..."
    arm-none-eabi-objcopy -O binary "$SCRIPTDIR/emulate/output.elf" "$SCRIPTDIR/emulate/output.bin" || {
        echo "错误: 无法从 ELF 文件生成 output.bin"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi

# 1. 构建项目并生成elf文件
# 2. 将生成的elf文件移动到脚本所在目录