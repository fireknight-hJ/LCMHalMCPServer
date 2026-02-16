#!/bin/bash

PWDDIR=/home/haojie/mcuxsdk-workspace

if [ ! -d "$PWDDIR" ]; then
    echo "错误: 构建目录不存在: $PWDDIR"
    exit 1
fi

cd "$PWDDIR" || {
    echo "错误: 无法切换到目录 $PWDDIR"
    exit 1
}

echo "开始清除项目..."
rm -rf build-eth

if [ $? -eq 0 ]; then
    echo "清除成功完成!"    
else
    echo "清除失败!"
    exit 1
fi
