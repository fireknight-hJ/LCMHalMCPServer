import subprocess
import config.globs as globs
import sys

def run_emulator() -> bool:
    """
    运行emulator, 返回执行状态（是否执行成功）
    """
    # 使用globs.script_path作为input_file的基础路径
    input_file = f"{globs.script_path}/base_input/input.bin"  # input_file现在指向script_path下的文件
    config_file = f"{globs.script_path}/semu_config.yml"
    
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
        cwd=globs.script_path,
        check=False,
        # stdout=subprocess.PIPE,  # 捕获标准输出
        # stderr=subprocess.PIPE   # 捕获标准错误
    )
    
    if ret.returncode != 0:
        # print("[ERROR] 运行emulator失败")
        return False
    else:
        # print("[INFO] 成功运行emulator")
        return True

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