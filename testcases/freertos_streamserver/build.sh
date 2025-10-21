#!/bin/bash

# FreeRTOS LwIP Streaming Server 项目构建脚本
# 用于编译STM32F769I_EVAL平台的LwIP流媒体服务器项目

# 设置项目构建目录路径
PWDDIR=/home/haojie/posixGen_Demos/LwIP_StreamingServer/SW4STM32/STM32F769I_EVAL/build

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
else
    echo "编译失败!"
    exit 1
fi