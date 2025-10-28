#!/bin/bash

# 安装codeql
brew install codeql
# 移动到Query目录安装codeql pack
cd queries
codeql pack install

# 安装python依赖
pip install -r requirements.txt

# TODO: 可能需要arm-none-eabi-gcc安装
if ! command -v arm-none-eabi-gcc &> /dev/null
then
    echo "arm-none-eabi-gcc not found, install it"
    wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu/14.3.rel1/binrel/arm-gnu-toolchain-14.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
    tar -xJvf arm-gnu-toolchain-14.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
    export PATH=$PATH:$PWD/arm-gnu-toolchain-14.3.rel1-darwin-arm64-arm-none-eabi/bin
    rm arm-gnu-toolchain-14.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
    echo "arm-none-eabi-gcc installed"
    echo "arm-none-eabi-gcc version:"
    arm-none-eabi-gcc --version
    echo "arm-none-eabi-gcc installed successfully"
else
    echo "arm-none-eabi-gcc already installed"
fi


# 测试安装是否成功（TODO）
# 1. 静态分析模块
# 2. LLM调用模块
# 3. 编译测试模块
# 4. 动态执行模块