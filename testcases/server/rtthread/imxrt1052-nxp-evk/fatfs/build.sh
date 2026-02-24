#!/bin/bash

PWDDIR=/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk
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
./build.sh fatfs

if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    # RT-Thread 默认生成的 ELF 名称为 rt-thread.elf，这里将其统一重命名为 output.elf 供 emulator 使用
    mv -f "rt-thread.elf" "$SCRIPTDIR/emulate/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/emulate/output.elf"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi
