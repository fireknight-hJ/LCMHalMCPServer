#!/bin/bash
ZEPHYR_PROJECT="${ZEPHYR_PROJECT:-/home/haojie/zephyrproject}"
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)
WEST_BUILD_DIR="compile_results/lcmhal_stm32_eth_dhcpv4_nucleo_f767zi"
rm -rf "$ZEPHYR_PROJECT/$WEST_BUILD_DIR"
rm -f "$SCRIPTDIR/emulate/output.elf"
echo "cleared: $WEST_BUILD_DIR, output.elf"
