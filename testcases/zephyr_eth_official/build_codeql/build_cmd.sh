#!/bin/bash
set -e

# Set up Zephyr environment
export ZEPHYR_BASE="${ZEPHYR_BASE:-/home/chenkaiqiu/LCMHalMCPServer/zephyr_official}"
export ZEPHYR_MODULES="${ZEPHYR_MODULES:-/home/chenkaiqiu/LCMHalMCPServer/zephyr_official/modules}"
export ZEPHYR_SDK_INSTALL_DIR="${ZEPHYR_SDK_INSTALL_DIR:-/home/chenkaiqiu/zephyr-sdk-0.16.8}"

# Source Zephyr environment
if [ -f "${ZEPHYR_BASE}/zephyr-env.sh" ]; then
    source "${ZEPHYR_BASE}/zephyr-env.sh"
fi

# Configure the project
cmake -GNinja -DBOARD=native_sim/native/64 "${PROJECT_DIR}/src" 2>&1 | tee cmake.log

# Build the project (just enough for CodeQL to analyze)
ninja 2>&1 | tee build.log
