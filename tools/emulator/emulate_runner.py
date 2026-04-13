import subprocess
import os
import config.globs as globs
import sys
import shutil
import shlex
import re

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


def _set_emulate_mode(mode: str):
    """切换 semu_config.yml 的 emulate_mode（emulate/fuzz）。"""
    config_path = os.path.join(globs.script_path, "emulate", "semu_config.yml")
    if not os.path.isfile(config_path):
        return
    with open(config_path, "r") as f:
        content = f.read()
    new_content = re.sub(r"emulate_mode:\s*\w+", f"emulate_mode: {mode}", content, count=1)
    if new_content != content:
        with open(config_path, "w") as f:
            f.write(new_content)


def run_emulator() -> subprocess.CompletedProcess:
    """
    运行emulator, 返回执行状态（是否执行成功）
    """
    _ensure_bin_from_elf()
    _expand_handler_aliases()
    _set_emulate_mode("emulate")
    # 使用globs.script_path作为input_file的基础路径
    input_file = f"{globs.script_path}/emulate/base_input/input.bin"  # input_file现在指向script_path下的文件
    config_file = f"{globs.script_path}/emulate/semu_config.yml"
    
    # 使用python -m运行fuzzemu.harness模块，增加 3 分钟超时保护
    cmd = [
        "python",
        "-m",
        "fuzzemu.harness",
        input_file,
        config_file,
        "-d",
        "5",
        "--skip-mmio-hook",
    ]
    try:
        ret = subprocess.run(
            cmd,
            cwd=globs.script_path + "/emulate",
            check=False,
            stdout=subprocess.PIPE,  # 捕获标准输出
            stderr=subprocess.PIPE,  # 捕获标准错误
            timeout=180,             # 3 分钟超时
        )
    except subprocess.TimeoutExpired as e:
        # 超时视为“正常结束”，返回码置为 0，并在 stdout 中提示 3min timeout
        base_stdout = e.stdout or b""
        timeout_msg = "3min timeout: emulate exceeded 180 seconds\n"
        if isinstance(base_stdout, bytes):
            stdout = base_stdout + timeout_msg.encode("utf-8")
        else:
            stdout = (base_stdout or "") + timeout_msg
        stderr = e.stderr or b""
        ret = subprocess.CompletedProcess(
            cmd,
            0,
            stdout=stdout,
            stderr=stderr,
        )
    return ret


def run_fuzz() -> subprocess.CompletedProcess:
    """
    启动 AFL++ fuzz 测试（后台运行），输出固定到 emulate/fuzz_output。
    """
    _ensure_bin_from_elf()
    _expand_handler_aliases()
    _set_emulate_mode("fuzz")

    emulate_dir = os.path.join(globs.script_path, "emulate")
    input_dir = os.path.join(emulate_dir, "base_input")
    config_file = os.path.join(emulate_dir, "semu_config.yml")
    output_dir = os.path.join(emulate_dir, "fuzz_output")
    log_file = os.path.join(output_dir, "afl_stdout.log")

    if not os.path.isdir(input_dir):
        return subprocess.CompletedProcess(
            args=[],
            returncode=1,
            stdout=b"",
            stderr=f"fuzz input dir not found: {input_dir}".encode("utf-8"),
        )

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # 与 fuzzemu-helper run 行为一致：AFL unicorn 模式，默认 24h 超时
    duration_hours = int(os.environ.get("LCMHAL_FUZZ_DURATION_HOURS", "24"))
    timeout_ms = int(os.environ.get("LCMHAL_FUZZ_TIMEOUT_MS", "10000"))
    fuzz_tool = os.environ.get("LCMHAL_FUZZ_TOOL", "fuzzemu")

    afl_cmd = (
        f"nohup timeout {duration_hours}h "
        f"afl-fuzz -U -m none -i {shlex.quote(input_dir)} -o {shlex.quote(output_dir)} "
        f"-t {timeout_ms} -- {shlex.quote(fuzz_tool)} @@ {shlex.quote(config_file)} "
        f"> {shlex.quote(log_file)} 2>&1 & echo $!"
    )
    ret = subprocess.run(
        ["bash", "-lc", afl_cmd],
        cwd=emulate_dir,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return ret


def list_afl_tasks() -> list[dict]:
    """列出当前系统中所有 afl-fuzz 任务。"""
    cmd = "ps -eo pid=,ppid=,etimes=,cmd="
    ret = subprocess.run(
        ["bash", "-lc", cmd],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if ret.returncode != 0:
        return []

    tasks = []
    for raw in ret.stdout.splitlines():
        line = raw.strip()
        if not line:
            continue
        # 固定 4 段：pid ppid etimes cmd...
        parts = line.split(None, 3)
        if len(parts) < 4:
            continue
        pid_s, ppid_s, etimes_s, cmdline = parts
        if "afl-fuzz" not in cmdline:
            continue

        output_dir = ""
        m = re.search(r"\s-o\s+(\S+)", cmdline)
        if m:
            output_dir = m.group(1)

        try:
            pid = int(pid_s)
            ppid = int(ppid_s)
            etimes = int(etimes_s)
        except ValueError:
            continue

        tasks.append(
            {
                "pid": pid,
                "ppid": ppid,
                "elapsed_seconds": etimes,
                "output_dir": output_dir,
                "cmd": cmdline,
            }
        )
    tasks.sort(key=lambda x: x["pid"])
    return tasks

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