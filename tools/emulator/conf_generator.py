from config import globs
from pathlib import Path
import subprocess
import sys  # 添加sys模块导入
import shutil


baseconfig_template = """output.elf:
  rules: "semu_rule.txt"
  enable_native: False
  emulate_mode: emulate
  handlers:
    Delay: do_return
    HAL_Delay: do_return
    wait: do_return
    wait_us: do_return
    HAL_BE_ENET_ReadFrame: handlers.common.hal_read_frame
    HAL_BE_In: handlers.common.hal_in
    HAL_BE_Out: handlers.common.hal_out
    HAL_BE_return_0: handlers.common.return_zero
    HAL_BE_return_1: handlers.common.return_true
    HAL_BE_Block_Read: handlers.common.hal_block_in
    HAL_BE_Block_Write: handlers.common.hal_block_out
"""

rule_template = """==
==
=="""



def generate_rule_config():
    with open(f"{globs.script_path}/emulate/semu_rule.txt", "w") as f:
        f.write(rule_template)

def generate_base_config():
    with open(f"{globs.script_path}/emulate/base_config.yml", "w") as f:
        f.write(baseconfig_template)

def generate_base_input():
    # 创建base_input文件夹
    base_input_path = Path(f"{globs.script_path}/emulate/base_input")
    base_input_path.mkdir(parents=True, exist_ok=True)
    
    # 从目录/resources/input.bin 移动
    pwd = Path(__file__).parent.parent.parent.resolve()
    input_template_path = pwd / "resources" / "input.bin"
    # 复制input.bin文件到base_input文件夹
    if input_template_path.exists():
        shutil.copy(input_template_path, base_input_path / "input.bin")
    else:
        print("[ERROR] 输入模板文件不存在，路径：", input_template_path)
        exit(1)

def generate_semu_config():
    if not Path(f"{globs.script_path}/emulate/base_config.yml").exists():
        generate_base_config()
    if not Path(f"{globs.script_path}/emulate/semu_rule.txt").exists():
        generate_rule_config()
    if not Path(f"{globs.script_path}/emulate/base_input/input.bin").exists():
        generate_base_input()
    # 修改subprocess.run，添加stdin和stdout参数，让命令能够与用户交互
    ret = subprocess.run(
        f"cd {globs.script_path}/emulate/ && fuzzemu-helper config base_config.yml -s", 
        shell=True, 
        check=True,
        stdin=sys.stdin,  # 继承父进程的标准输入
        stdout=sys.stdout,  # 继承父进程的标准输出
        stderr=sys.stderr  # 继承父进程的标准错误
    )
    if ret.returncode != 0:
        print("[ERROR] 生成semu配置失败")
        exit(1)
    else:
        print(f"[INFO] 成功生成semu配置文件, 路径: {globs.script_path}/semu_config.yml")



def generate_emulator_configs():
    if not Path(f"{globs.script_path}/emulate").exists():
        Path(f"{globs.script_path}/emulate").mkdir(parents=True, exist_ok=True)
    generate_base_config()
    generate_rule_config()
    generate_base_input()
    generate_semu_config()


if __name__ == "__main__":
    # 编译脚本路径
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    # codeql的DB路径
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    # 项目路径, DB中记录的项目路径
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
    generate_emulator_configs()
