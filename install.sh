#!/bin/bash

detect_os() {
    if [[ "$(uname)" == "Darwin" ]]; then
        echo "macos"
    elif [[ "$(uname)" == "Linux" ]]; then
        echo "linux"
    else
        echo "unsupported"
        exit 1
    fi
}

install_codeql_mac() {
    brew install codeql
}

install_codeql_linux() {
    sudo apt update
    sudo apt install -y codeql
}

install_arm_none_eabi_gcc_mac() {
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
}

install_arm_none_eabi_gcc_linux() {
    if ! command -v arm-none-eabi-gcc &> /dev/null
    then
        echo "arm-none-eabi-gcc not found, install it"
        wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu/14.3.rel1/binrel/arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
        tar -xJvf arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
        export PATH=$PATH:$PWD/arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi/bin
        rm arm-gnu-toolchain-14.3.rel1-x86_64-arm-none-eabi.tar.xz
        echo "arm-none-eabi-gcc installed"
        echo "arm-none-eabi-gcc version:"
        arm-none-eabi-gcc --version
        echo "arm-none-eabi-gcc installed successfully"
    else
        echo "arm-none-eabi-gcc already installed"
    fi
}

install_fuzzemu_mac() {
    if [ ! -d "fuzzemu" ]; then
        echo "fuzzemu directory does not exist, cloning fuzzemu repository"
        git clone https://github.com/IoTS-P/fuzzemu.git
    else
        echo "fuzzemu directory already exists, skipping clone"
    fi
    cd fuzzemu
    git checkout feat/support_lcmhal
    bash install_mac.sh || exit 1
    echo "fuzzemu installed successfully"
}

install_fuzzemu_linux() {
    if [ ! -d "fuzzemu" ]; then
        echo "fuzzemu directory does not exist, cloning fuzzemu repository"
        git clone https://github.com/IoTS-P/fuzzemu.git
    else
        echo "fuzzemu directory already exists, skipping clone"
    fi
    cd fuzzemu
    git checkout feat/support_lcmhal
    cd ..
    bash setup_linux.sh || exit 1
    echo "fuzzemu installed successfully"
}

OS=$(detect_os)
echo "[+] Detected OS: $OS"

cd "$(dirname "$0")"

echo "[+] Installing CodeQL..."
case $OS in
    macos)
        install_codeql_mac
        ;;
    linux)
        install_codeql_linux
        ;;
esac

cd queries
codeql pack install
cd ..

echo "[+] Installing Python dependencies..."
pip install -r requirements.txt

echo "[+] Installing arm-none-eabi-gcc..."
case $OS in
    macos)
        install_arm_none_eabi_gcc_mac
        ;;
    linux)
        install_arm_none_eabi_gcc_linux
        ;;
esac

echo "[+] Installing fuzzemu..."
case $OS in
    macos)
        install_fuzzemu_mac
        ;;
    linux)
        install_fuzzemu_linux
        ;;
esac

echo "Installation completed successfully."
