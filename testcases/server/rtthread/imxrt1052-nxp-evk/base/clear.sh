#!/bin/bash

PWDDIR=/home/haojie/rt-thread/bsp/nxp/imx/imxrt/imxrt1052-nxp-evk

if [ ! -d "$PWDDIR" ]; then
    echo "错误: 构建目录不存在: $PWDDIR"
    exit 1
fi

cd "$PWDDIR" || {
    echo "错误: 无法切换到目录 $PWDDIR"
    exit 1
}

echo "开始清除项目..."
if ./build.sh clean 2>/dev/null; then
    echo "清除成功完成!"
else
    # 本 BSP 的 build.sh 不支持 clean，使用 scons -c 清理构建产物
    scons -c
    echo "清除成功完成 (scons -c)!"
fi
