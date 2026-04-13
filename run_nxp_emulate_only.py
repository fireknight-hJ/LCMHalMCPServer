#!/usr/bin/env python3
"""仅生成模拟器配置并运行 NXP LwIP 网络 demo（跳过 build/analysis）。"""
import os
import sys
import subprocess
from pathlib import Path

# 确保能 import 项目模块
sys.path.insert(0, str(Path(__file__).resolve().parent))

import config.globs as globs
from config.globs import load_config_from_yaml
from tools.collector.collector import register_db
from tools.emulator.conf_generator import generate_emulator_configs, extract_syms
from tools.emulator.core import emulate_proj

SCRIPT_DIR = Path(__file__).resolve().parent
NXP_LWIP = SCRIPT_DIR / "testcases/server/nxp/NXP_LwIP_FreeRTOS"


def ensure_output_bin():
    """若没有 output.bin 则从 output.elf 用 objcopy 生成。"""
    elf_path = NXP_LWIP / "emulate" / "output.elf"
    bin_path = NXP_LWIP / "emulate" / "output.bin"
    if bin_path.exists():
        return
    if not elf_path.exists():
        print(f"[ERROR] 未找到 {elf_path}")
        sys.exit(1)
    # 尝试 arm-none-eabi-objcopy（NXP MCU 一般为 ARM）
    for cmd in ["arm-none-eabi-objcopy", "objcopy"]:
        ret = subprocess.run(
            [cmd, "-O", "binary", str(elf_path), str(bin_path)],
            capture_output=True,
            text=True,
        )
        if ret.returncode == 0:
            print(f"[INFO] 已生成 output.bin")
            return
    print("[ERROR] 未找到 objcopy，请安装 arm-none-eabi-gcc 或设置 PATH")
    sys.exit(1)


def main():
    config = load_config_from_yaml(str(NXP_LWIP))
    globs.globs_init(config)
    print(f"script_path: {globs.script_path}")
    print(f"db_path: {globs.db_path}")

    register_db(globs.db_path)
    ensure_output_bin()
    extract_syms()
    generate_emulator_configs()
    result = emulate_proj()
    print("Emulate result:", result)
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    sys.exit(main())
