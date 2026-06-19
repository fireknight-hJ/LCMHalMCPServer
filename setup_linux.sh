#!/bin/bash

cd "$(dirname "$0")"
FUZZEMU_DIR="$(pwd)/fuzzemu"
echo "[+] fuzzemu dir: $FUZZEMU_DIR"

if [[ "$(uname)" != "Linux" ]]; then
    echo "[-] This script is intended for Linux only!"
    exit 1
fi

echo "[+] Running on Linux"

echo "[*] Checking dependencies (you may need to install manually with sudo)..."
echo "    Required: python3, python3-pip, cmake, git, flex, bison, pkg-config,"
echo "              libglib2.0-dev, libpixman-1-dev, ninja-build, clang, llvm,"
echo "              automake, tmux, redis-server, wget, autoconf, htop, vim,"
echo "              unzip, gnuplot, binutils-arm-none-eabi"

echo "[*] Installing Python dependencies..."
pip3 install cython setuptools --upgrade

echo "[*] Checking arm-none-eabi-gcc..."
if ! command -v arm-none-eabi-gcc &> /dev/null
then
    echo "arm-none-eabi-gcc not found, install it"
    wget -q https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu/14.3.rel1/binrel/arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
    tar -xJf arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
    export PATH=$PATH:$PWD/arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi/bin
    rm arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
    echo "arm-none-eabi-gcc installed"
    echo "arm-none-eabi-gcc version:"
    arm-none-eabi-gcc --version
    echo "arm-none-eabi-gcc installed successfully"
else
    echo "arm-none-eabi-gcc already installed"
fi

echo "[*] Installing AFL++..."
cd "$FUZZEMU_DIR"
bash ./install_afl.sh

echo "[*] Installing fuzzemu..."
pip3 install . || exit 1

TOOL_NAME=$(cat "$FUZZEMU_DIR/tool_name")
$TOOL_NAME -h || (echo "[-] Fail to install $TOOL_NAME!" && exit 1)
echo "Success to install $TOOL_NAME!"
