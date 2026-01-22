#!/bin/bash

# RT-Thread file 示例项目构建脚本
# 用于编译 hifive1 平台的 file 示例项目

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/rt-thread/bsp/hifive1
# 获取当前shell脚本所在目录
SCRIPTDIR=/Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/file

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
scons -j8

# 检查编译结果
if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    # 移动生成的可执行文件到 DBDIR
    if [ ! -d "$SCRIPTDIR/emulate" ]; then
        mkdir -p "$SCRIPTDIR/emulate"
    fi
    # 强制移动可执行文件到脚本目录，覆盖同名文件
    # 生成的elf文件名通用名称 "output.elf"
    mv -f "rtthread.elf" "$SCRIPTDIR/emulate/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/emulate/output.elf"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi

# 1. 构建项目并生成elf文件
# 2. 将生成的elf文件移动到脚本所在目录