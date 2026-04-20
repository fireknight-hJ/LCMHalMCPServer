#!/bin/bash

PWDDIR=/home/haojie/mcuxsdk-workspace
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
# mcuxsdk-workspace 下的 build.sh 目前仅兼容 lwip 包装；此处直接调用 build_firmware.sh
export BOARD="${BOARD:-evkbimxrt1050}"
export APP_PATH="mcuxsdk/examples/freertos_driver_examples/freertos_i2c"
export BUILD_DIR="$PWDDIR/build-i2c-freertos"
./build_firmware.sh

if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    mv -f "build-i2c-freertos/freertos_i2c.elf" "$SCRIPTDIR/emulate/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/emulate/output.elf"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi
