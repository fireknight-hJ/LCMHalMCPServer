#!/bin/bash

PWDDIR=/home/haojie/posixGen_Demos/LwIP_StreamingServer/SW4STM32/STM32F769I_EVAL/Debug
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)

if [ ! -d "$PWDDIR" ]; then
    echo "错误: 构建目录不存在: $PWDDIR"
    exit 1
fi

cd "$PWDDIR" || {
    echo "错误: 无法切换到目录 $PWDDIR"
    exit 1
}

echo "开始编译项目..."
make all

if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    mv -f "LwIP_StreamingServer.elf" "$SCRIPTDIR/emulate/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/emulate/output.elf"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi
