from config import globs
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from pathlib import Path
import subprocess
import sys  # 添加sys模块导入
import shutil
import yaml  # 导入PyYAML库

import yaml
from elftools.elf.constants import SH_FLAGS
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

# 将字符串模板替换为Python字典结构
baseconfig_dict = {
    'output.elf': {
        'rules': 'semu_rule.txt',
        'enable_native': False,
        'emulate_mode': 'emulate',
        'handlers': {
            'Delay': 'do_return',
            'HAL_Delay': 'do_return',
            'wait': 'do_return',
            'wait_us': 'do_return',
            'HAL_BE_ENET_ReadFrame': 'fuzzemu.handlers.common.hal_read_frame',
            'HAL_BE_In': 'fuzzemu.handlers.common.hal_in',
            'HAL_BE_Out': 'fuzzemu.handlers.common.hal_out',
            'HAL_BE_return_0': 'fuzzemu.handlers.common.return_zero',
            'HAL_BE_return_1': 'fuzzemu.handlers.common.return_true',
            'HAL_BE_Block_Read': 'fuzzemu.handlers.common.hal_block_in',
            'HAL_BE_Block_Write': 'fuzzemu.handlers.common.hal_block_out'
        }
    }
}

rule_template = """==
==
=="""


def generate_rule_config():
    with open(f"{globs.script_path}/emulate/semu_rule.txt", "w") as f:
        f.write(rule_template)

# 修改generate_base_config函数，使用yaml.dump()生成YAML文件
def generate_base_config():
    global baseconfig_dict
    # 从数据库中获取MMIO函数列表
    mmio_funcs_emulate_config()
    # 应用定制化配置
    customize_emulator_config()
    # 生成YAML配置文件
    config_path = Path(f"{globs.script_path}/emulate/base_config.yml")
    # 确保目录存在
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        # 使用yaml.dump()将字典转换为YAML格式并写入文件
        yaml.dump(baseconfig_dict, f, default_flow_style=False, sort_keys=False)

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
    # 执行fuzzemu-helper命令，捕获输出以避免干扰MCP通信
    cmd = f"cd {globs.script_path}/emulate/ && fuzzemu-helper config base_config.yml -s"
    ret = subprocess.run(
        cmd, 
        shell=True, 
        check=True,
        capture_output=True,  # 捕获标准输出和错误
        text=True  # 以文本模式捕获
    )
    if ret.returncode != 0:
        print("[ERROR] 生成semu配置失败")
        print(f"Error output: {ret.stderr}")
        exit(1)
    else:
        # 只打印成功信息，不打印fuzzemu-helper的详细输出
        print(f"[INFO] 成功生成semu配置文件, 路径: {globs.script_path}/emulate/semu_config.yml")

def mmio_funcs_emulate_config():
    global baseconfig_dict
    # 实际调用函数获取MMIO函数列表，而不是引用函数对象
    try:
        mmio_funcs = get_mmio_func_list(globs.db_path)
        baseconfig_dict['output.elf']["mmio_funcs"] = mmio_funcs
    except Exception as e:
        print(f"[WARNING] Failed to get MMIO function list: {e}")
        baseconfig_dict['output.elf']["mmio_funcs"] = []


def customize_emulator_config():
    """定制化emulator配置的函数
    
    当前功能：强制将LoopCopyDataInit替换为do_return
    """
    global baseconfig_dict
    # deprecated: 在初始化阶段随意跳过tag会报错
    # 强制将LoopCopyDataInit添加到handlers中并映射为do_return
    # baseconfig_dict['output.elf']['handlers']['LoopCopyDataInit'] = 'do_return'
    # baseconfig_dict['output.elf']['handlers']['LoopFillZerobss'] = 'do_return'
    # baseconfig_dict['output.elf']['handlers']['CopyDataInit'] = 'do_return'
    # print("[INFO] Customized emulator config: Added LoopCopyDataInit -> do_return")
    # print("[INFO] Customized emulator config: Added LoopFillZerobss -> do_return")
    # print("[INFO] Customized emulator config: Added CopyDataInit -> do_return")

def extract_syms():
    yml_path = Path(globs.script_path) / "emulate" / "syms.yml"
    firmware_elfpath = Path(globs.script_path) / "emulate" / "output.elf"

    # Based on https://github.com/eliben/pyelftools/blob/master/scripts/readelf.py, display_symbol_tables
    res = {}
    with open(firmware_elfpath, "rb") as f:
        elffile = ELFFile(f)
        symbol_tables = [(idx, s) for idx, s in enumerate(elffile.iter_sections())
                            if isinstance(s, SymbolTableSection)]

        if not symbol_tables and elffile.num_sections() == 0:
            # print("[-] No symbol sections...")
            return res

        for _, section in symbol_tables:
            if section['sh_entsize'] == 0:
                # print("[-] section['sh_entsize'] == 0")
                # Symbol table has no entries
                continue

            for _, symbol in enumerate(section.iter_symbols()):
                if symbol.name and "$" not in symbol.name:
                    res[symbol['st_value']] = symbol.name
    config = {}
    config['symbols'] = res
    with open(yml_path, 'w') as f:
        yaml.dump(config, f)
        # print(f"    [+] Success Extra Syms File: {yml_path}")


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
    # 预分析数据库并注册
    register_db(globs.db_path)
    generate_emulator_configs()
