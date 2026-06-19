#!/bin/bash
set -e
ZEPHYR_PROJECT="${ZEPHYR_PROJECT:-/home/haojie/zephyrproject}"
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)
BOARD="lpcxpresso55s69_cpu0"
SAMPLE="zephyr/samples/sensor/fxos8700"
WEST_BUILD_DIR="compile_results/lcmhal_nxp_i2c_fxos8700_lpc55"

cd "$ZEPHYR_PROJECT" || exit 1
command -v west >/dev/null 2>&1 || { echo "west not found"; exit 1; }

west build -b "$BOARD" -p always "$SAMPLE" -d "$WEST_BUILD_DIR" -- -DCONF_FILE=prj_accel.conf

mkdir -p "$SCRIPTDIR/emulate"
cp -f "$ZEPHYR_PROJECT/$WEST_BUILD_DIR/zephyr/zephyr.elf" "$SCRIPTDIR/emulate/output.elf"
echo "OK: $SCRIPTDIR/emulate/output.elf"
