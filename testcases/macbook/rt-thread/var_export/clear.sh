#!/bin/bash

# RT-Thread var_export 示例项目清除脚本
# 用于清除 hifive1 平台的 var_export 示例项目构建缓存

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/rt-thread/bsp/hifive1
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

# 清除项目
echo "开始清除项目..."
scons -c

# 检查清除结果
if [ $? -eq 0 ]; then
    echo "清除成功完成!"
else
    echo "清除失败!"
    exit 1
fi