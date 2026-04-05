#!/bin/bash
set -e
ZEPHYR_PROJECT="${ZEPHYR_PROJECT:-/home/haojie/zephyrproject}"
SCRIPTDIR=$(cd "$(dirname "$0")" || exit; pwd)
BOARD="atsame54_xpro"
SAMPLE="zephyr/samples/subsys/fs/littlefs"
WEST_BUILD_DIR="compile_results/lcmhal_atmel_fs_littlefs_atsame54"

cd "$ZEPHYR_PROJECT" || exit 1
command -v west >/dev/null 2>&1 || { echo "west not found"; exit 1; }

west build -b "$BOARD" -p always "$SAMPLE" -d "$WEST_BUILD_DIR"

mkdir -p "$SCRIPTDIR/emulate"
cp -f "$ZEPHYR_PROJECT/$WEST_BUILD_DIR/zephyr/zephyr.elf" "$SCRIPTDIR/emulate/output.elf"
echo "OK: $SCRIPTDIR/emulate/output.elf"
