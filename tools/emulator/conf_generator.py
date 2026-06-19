from config import globs
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from pathlib import Path
import re
import subprocess
import sys  # 添加sys模块导入
import shutil
import yaml  # 导入PyYAML库

import yaml
from elftools.elf.constants import SH_FLAGS
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

# 生成配置时加入 handlers 的符号，模拟器遇到这些符号直接 do_return（人工 mock，不执行原逻辑）
HANDLERS_DO_RETURN_LIST = [
    'puts',
    'fflush',
    'DP83848_Init',
    'stm32_putc',
    'rt_thread_mdelay',        # RT-Thread 线程延时，避免在模拟器里真正 sleep
    'DelayLoop',              # 纯忙等延时
    'SDK_DelayAtLeastUs',     # NXP SDK 延时
    'LPUART_WriteBlocking',   # 阻塞写 UART，模拟器无硬件
    'ENET_SetSMI',            # SMI/MDIO 配置在模拟器无意义，整体跳过；避免进入内部 assert
]

# 不直接跳过 __assert_func / sys_assert，应通过满足导致 assert 的条件解决（见 doc 与下方 PHY 读）

# 遇到这些符号时跳过原逻辑，并将返回值设为 1（r0=1）
HANDLERS_RETURN_1_LIST = []

# 遇到这些符号时跳过原逻辑，并将返回值设为 2（r0=2），例如 100M 全双工 link up
HANDLERS_RETURN_2_LIST = [
    'DP83848_GetLinkState',
    'PHY_GetLinkStatus',      # 模拟器无 PHY，直接返回“link up”
    'PHY_GetLinkSpeedDuplex', # 同上，返回 2 表示 100M 全双工
]

# 遇到这些符号时跳过原逻辑，并将返回值设为 0（r0=0，如 HAL_OK / kStatus_Success）
# HAL_ETH_ReadPHYRegister 返回 0 表示“读成功”；ethernetif_phy_init/PHY_Init 跳过时返回 0 表示成功，避免 assert 及未初始化 ops 导致 blx 0
HANDLERS_RETURN_ZERO_LIST = [
    'HAL_RCC_ClockConfig',
    'HAL_ETH_ReadPHYRegister',
    'ethernetif_phy_init',
    'PHY_Init',
]

# 遇到这些符号时 r0 返回 0x2000（DP83848 PHY ID），满足 ethernetif_phy_init 等对 PHY 检测的 assert
HANDLERS_RETURN_PHY_ID_LIST = [
    'ENET_MDIORead',
]

# 将字符串模板替换为Python字典结构
_base_handlers = {
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

baseconfig_dict = {
    'output.elf': {
        'rules': 'semu_rule.txt',
        'enable_native': False,
        'emulate_mode': 'emulate',
        # loop_whitelist: Functions that should skip loop detection (含启动/时钟初始化中的合法循环)
        'loop_whitelist': [
            'memset',
            'memcpy',
            'memmove',
            'FillZerobss',
            'LoopFillZerobss',
            'CopyDataInit',
            'LoopCopyDataInit',
            'Zero_Init',
            'Reset_Handler',   # 复位后首条 C 逻辑，内含 .data/.bss 等初始化循环
            'SystemInit',     # 系统/时钟初始化，常有 PLL 等等待循环
        ],
        'handlers': dict(
            _base_handlers,
            **{name: 'do_return' for name in HANDLERS_DO_RETURN_LIST},
            **{name: 'fuzzemu.handlers.common.return_1' for name in HANDLERS_RETURN_1_LIST},
            **{name: 'fuzzemu.handlers.common.return_2' for name in HANDLERS_RETURN_2_LIST},
            **{name: 'fuzzemu.handlers.common.return_zero' for name in HANDLERS_RETURN_ZERO_LIST},
            **{name: 'fuzzemu.handlers.common.return_phy_id' for name in HANDLERS_RETURN_PHY_ID_LIST},
        )
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

def _base_config_valid(base_path):
    """base_config.yml 必须是以 output.elf 为唯一顶层 key，且其下含 rules。
    fuzzemu-helper 按此格式把 base_config 合并进 semu_config；格式错误会导致生成的
    semu_config 缺少 rules/model/mmio_funcs，进而报 Config Error: 'rules' not exists。
    详见 doc/NXP_LwIP_BareMetal_emulate_fixes_summary.md 或 fuzzemu helper/dump_config.py。
    """
    if not base_path.exists():
        return False
    try:
        with open(base_path, "r") as f:
            data = yaml.safe_load(f)
    except Exception:
        return False
    if not isinstance(data, dict) or len(data) != 1 or "output.elf" not in data:
        return False
    elf_cfg = data["output.elf"]
    return isinstance(elf_cfg, dict) and "rules" in elf_cfg


def generate_semu_config():
    base_config_path = Path(f"{globs.script_path}/emulate/base_config.yml")
    if not base_config_path.exists() or not _base_config_valid(base_config_path):
        if base_config_path.exists():
            print("[INFO] base_config.yml 格式无效（需以 output.elf 为 key 且含 rules），已重新生成")
        generate_base_config()
    if not Path(f"{globs.script_path}/emulate/semu_rule.txt").exists():
        generate_rule_config()
    if not Path(f"{globs.script_path}/emulate/base_input/input.bin").exists():
        generate_base_input()
    
    # 检查 output.bin 是否存在，使用实际 bin 文件大小而不是 ELF 文件大小
    bin_path = Path(f"{globs.script_path}/emulate/output.bin")
    if bin_path.exists():
        bin_size = bin_path.stat().st_size
        # 向上对齐到 0x1000 (4KB)
        aligned_size = ((bin_size + 0xFFF) & ~0xFFF)
        print(f"[INFO] output.bin size: {bin_size}, aligned to: {aligned_size}")
    
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
    
    # 修正 flash 大小为实际 bin 文件大小
    fix_flash_size()
    # 若 syms 中有 _estack，用其修正 initial_sp（与固件链接脚本一致，避免栈顶错误导致 PC 跳到 0）
    fix_initial_sp_from_syms()
    # 展开 handler 简短别名：return_zero / return_0 -> 返回 0 的完整路径
    expand_handler_aliases()


# handler 简短别名 -> fuzzemu 完整路径（配置里可写 return_zero 表示“返回 0”）
HANDLER_ALIASES = {
    "return_zero": "fuzzemu.handlers.common.return_zero",
    "return_0": "fuzzemu.handlers.common.return_zero",
}


def expand_handler_aliases():
    """将 semu_config.yml 里 handlers 的简短别名展开为完整路径。"""
    config_path = Path(globs.script_path) / "emulate" / "semu_config.yml"
    if not config_path.exists():
        return
    content = config_path.read_text()
    changed = False
    for alias, full in HANDLER_ALIASES.items():
        # 只替换作为值的 ": alias"（行尾或后接空格/注释）
        old = f": {alias}\n"
        new = f": {full}\n"
        if old in content:
            content = content.replace(old, new)
            changed = True
        old2 = f": {alias} "
        new2 = f": {full} "
        if old2 in content:
            content = content.replace(old2, new2)
            changed = True
    if changed:
        config_path.write_text(content)


def fix_initial_sp_from_syms():
    """若 syms.yml 中存在 _estack，则用其值覆盖 semu_config 的 initial_sp。"""
    syms_path = Path(globs.script_path) / "emulate" / "syms.yml"
    config_path = Path(globs.script_path) / "emulate" / "semu_config.yml"
    if not syms_path.exists() or not config_path.exists():
        return
    estack_addr = None
    with open(syms_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.endswith("_estack"):
                try:
                    # 格式为 "  decimal_addr: _estack" 或 "decimal_addr: _estack"
                    estack_addr = int(line.split(":")[0].strip())
                    break
                except (ValueError, IndexError):
                    continue
    if estack_addr is None:
        return
    sp_hex = hex(estack_addr)
    content = config_path.read_text()
    if "initial_sp:" not in content:
        return
    new_content = re.sub(r"initial_sp:\s*0x[0-9a-fA-F]+", f"initial_sp: {sp_hex}", content, count=1)
    if new_content != content:
        config_path.write_text(new_content)
        print(f"[INFO] Set initial_sp from _estack: {sp_hex}")


def fix_flash_size():
    """修正 semu_config.yml 中的内存配置，确保对齐到 4KB
    
    策略：
    1. 删除 .isr_vector 条目（如果存在）
    2. 合并 flash 区域，覆盖 .isr_vector 的地址范围
    3. 确保 base_addr 和 size 都是 4KB 对齐
    """
    config_path = Path(f"{globs.script_path}/emulate/semu_config.yml")
    bin_path = Path(f"{globs.script_path}/emulate/output.bin")
    
    if not config_path.exists() or not bin_path.exists():
        return
    
    bin_size = bin_path.stat().st_size
    aligned_size = ((bin_size + 0xFFF) & ~0xFFF)  # 对齐到 4KB
    
    # 读取配置文件
    with open(config_path, 'r') as f:
        content = f.read()
    
    # 解析 YAML
    config = yaml.safe_load(content)
    
    memory_map = config.get('memory_map', {})
    
    # 获取 flash 配置
    flash = memory_map.get('flash', {})
    flash_addr = flash.get('base_addr', 0x8000000)
    if isinstance(flash_addr, str):
        flash_addr = int(flash_addr, 0)
    
    # NXP i.MX RT 等：entry 在 0x6xxxxxxx（FlexSPI/XIP），若 flash 被误放在 0x20000000 会导致 INVALID Fetch
    entry = config.get('entry_point')
    if entry is not None:
        entry = int(entry, 0) if isinstance(entry, str) else entry
        if (0x60000000 <= entry < 0x60400000) and (flash_addr == 0x20000000):
            flash_addr = 0x60000000
            print(f"[INFO] entry_point 0x{entry:x} in XIP range, set flash base to 0x60000000")
    
    # 对齐地址到 4KB
    aligned_addr = flash_addr & ~0xFFF
    
    # 与 flash 同址的 region（如 fuzzemu-helper 生成的 peripheral_ram）会导致 Unicorn UC_ERR_MAP，需要移除
    def _addr_val(v):
        a = v.get('base_addr') if isinstance(v, dict) else None
        if a is None:
            return None
        return int(a, 0) if isinstance(a, str) else a
    overlapping = {k for k, v in memory_map.items() if k != 'flash' and _addr_val(v) == flash_addr}
    
    # 更新配置
    config['memory_map'] = {
        'flash': {
            'base_addr': hex(aligned_addr),
            'file': 'output.bin',
            'permissions': 'r-x',
            'size': hex(aligned_size)
        }
    }
    
    # 添加其他必要的内存区域（排除与 flash 重叠的）
    for key in ['irq_ret', 'mmio', 'nvic', 'peripheral', 'ram']:
        if key in memory_map and key not in overlapping:
            config['memory_map'][key] = memory_map[key]
    
    # 写回配置文件，保持原有格式
    lines = content.split('\n')
    new_lines = []
    in_memory_map = False
    skip_next = False
    skip_region = None  # 要整块跳过的 region 名（与 flash 重叠）
    
    for i, line in enumerate(lines):
        # 跳过 .isr_vector 条目
        if '.isr_vector:' in line:
            skip_next = True
            continue
        if skip_next and line.strip() and line[0] != ' ' and line[0] != '\t':
            skip_next = False
        
        if skip_next and line.strip().startswith('base_addr:'):
            continue
        if skip_next and line.strip().startswith('permissions:'):
            continue
        if skip_next and line.strip().startswith('size:'):
            skip_next = False
            continue
        
        # 跳过与 flash 重叠的 region 整块（直到下一个 memory_map 下的 region 名，形如 "  name:"）
        # 若已离开 memory_map（顶格或空行），则停止跳过，避免把 mmio_funcs/model/rules 等截掉（如 NXP ram 与 flash 同址时）
        if skip_region is not None:
            if line.startswith('  ') and not line.startswith('    ') and line.strip().endswith(':'):
                skip_region = None  # 下一个 region，保留该行
            elif not line.startswith(' ') and not line.startswith('\t'):
                skip_region = None  # 顶格行 = 新顶层 key，已离开 memory_map，保留后续内容
            else:
                continue
            
        if 'memory_map:' in line:
            in_memory_map = True
            new_lines.append(line)
            continue
        
        # memory_map 下形如 "  region_name:"（两空格开头，非四空格）
        if in_memory_map and line.startswith('  ') and not line.startswith('    ') and line.strip().endswith(':'):
            region_name = line.strip().rstrip(':').strip()
            if region_name in overlapping:
                skip_region = region_name
                continue
        
        if in_memory_map and line.strip() == 'flash:':
            # 替换 flash 配置
            new_lines.append('  flash:')
            new_lines.append(f'    base_addr: {hex(aligned_addr)}')
            new_lines.append('    file: output.bin')
            new_lines.append('    permissions: r-x')
            new_lines.append(f'    size: {hex(aligned_size)}')
            skip_next = True
            continue
            
        if in_memory_map and line.strip() and not line[0].isspace() and ':' in line:
            in_memory_map = False
            
        if skip_next:
            continue
            
        new_lines.append(line)
    
    with open(config_path, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print(f"[INFO] Fixed memory map: base_addr={hex(aligned_addr)}, size={hex(aligned_size)}")

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
