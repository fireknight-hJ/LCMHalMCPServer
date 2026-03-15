import subprocess
import os
import config.globs as globs
import sys

def _ensure_bin_from_elf():
    """模拟执行前用 output.elf 重新生成 output.bin，保证与 ELF 一致。"""
    emulate_dir = os.path.join(globs.script_path, "emulate")
    elf_path = os.path.join(emulate_dir, "output.elf")
    bin_path = os.path.join(emulate_dir, "output.bin")
    if not os.path.isfile(elf_path):
        return
    for cmd in ["arm-none-eabi-objcopy", "objcopy"]:
        try:
            r = subprocess.run(
                [cmd, "-O", "binary", elf_path, bin_path],
                cwd=emulate_dir,
                capture_output=True,
                text=True,
            )
            if r.returncode == 0:
                print("[INFO] Regenerated output.bin from output.elf (overwrites existing bin)")
                return
        except FileNotFoundError:
            continue
    print("[WARN] Could not run objcopy to regenerate output.bin; using existing bin if present.")

# 与 conf_generator 一致：配置里可写 return_zero 表示“返回 0”
_HANDLER_ALIASES = {
    "return_zero": "fuzzemu.handlers.common.return_zero",
    "return_0": "fuzzemu.handlers.common.return_zero",
}


def _expand_handler_aliases():
    """运行前将 semu_config.yml 里 handlers 的简短别名展开，便于配置里直接写 return_zero。"""
    config_path = os.path.join(globs.script_path, "emulate", "semu_config.yml")
    if not os.path.isfile(config_path):
        return
    with open(config_path, "r") as f:
        content = f.read()
    for alias, full in _HANDLER_ALIASES.items():
        content = content.replace(f": {alias}\n", f": {full}\n")
        content = content.replace(f": {alias} ", f": {full} ")
    with open(config_path, "w") as f:
        f.write(content)


def run_emulator() -> subprocess.CompletedProcess:
    """
    运行emulator, 返回执行状态（是否执行成功）
    """
    _ensure_bin_from_elf()
    _expand_handler_aliases()
    # 使用globs.script_path作为input_file的基础路径
    input_file = f"{globs.script_path}/emulate/base_input/input.bin"  # input_file现在指向script_path下的文件
    config_file = f"{globs.script_path}/emulate/semu_config.yml"
    
    # 使用python -m运行fuzzemu.harness模块
    ret = subprocess.run(
        [
            "python",
            "-m",
            "fuzzemu.harness",
            input_file,
            config_file,
            "-d",
            "5",
            "--skip-mmio-hook"
        ],
        cwd=globs.script_path+"/emulate",
        check=False,
        stdout=subprocess.PIPE,  # 捕获标准输出
        stderr=subprocess.PIPE   # 捕获标准错误
    )
    
    return ret

if __name__ == "__main__":
    # 编译脚本路径
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    # codeql的DB路径
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    # 项目路径, DB中记录的项目路径
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
    ret = run_emulator()
    print(f"Emulator exited with return code: {ret.returncode}")
    # print(f"Emulator stdout: {ret.stdout.decode('utf-8')}")
    # print(f"Emulator stderr: {ret.stderr.decode('utf-8')}")