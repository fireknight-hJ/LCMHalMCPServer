# Copyright (c) 2024 Zephyr Community
#
# SPDX-License-Identifier: Apache-2.0
#
# Zephyr ETH Driver Test - Full Zephyr build system
# Based on Zephyr official samples structure

cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(zephyr_eth_test)

# Application configuration
set(APP_NAME zephyr_eth_test)

# Source files
target_sources(app PRIVATE
    main.c
)

# Include directories
target_include_directories(app PRIVATE
    ${ZEPHYR_BASE}/include
    ${ZEPHYR_BASE}/drivers
    ${ZEPHYR_BASE}/drivers/ethernet
    ${ZEPHYR_BASE}/net
)
