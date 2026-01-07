# Emulator工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
import os
import re
from tools.emulator.emulate_runner import run_emulator
from tools.emulator.conf_generator import extract_syms


def emulate_proj() -> dict:
    """运行模拟器，返回模拟结果
    
    Returns:
        dict: 模拟结果，包含std_out、std_err和exit_code
    """
    # 每次emulate前重新生成syms.yml配置文件，因为重新build后符号表会变化
    extract_syms()
    ret = run_emulator()
    return {
        "std_out": ret.stdout,
        "std_err": ret.stderr,
        "exit_code": ret.returncode
    }


def ensure_emulator_output_exists():
    """确保模拟器输出文件存在，如果不存在则运行模拟器生成
    """
    # 检查两个关键文件是否存在
    lcmhal_file = os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt")
    function_file = os.path.join(globs.script_path, "emulate/debug_output/function.txt")
    
    if not os.path.exists(lcmhal_file) or not os.path.exists(function_file):
        # 如果任一文件不存在，运行模拟器生成
        print("模拟器输出文件不存在，正在运行模拟器生成...")
        emulate_proj()
        print("模拟器运行完成，输出文件已生成")


def mmio_function_emulate_info() -> str:
    """获取所有MMIO函数的模拟器结果信息
    
    Returns:
        str: 模拟器输出的MMIO函数信息
    """
    # 确保模拟器输出文件存在
    ensure_emulator_output_exists()
    
    with open(os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt"), "r") as f:
        data = "".join(f.readlines())
    return data


def function_calls_emulate_info() -> str:
    """获取所有函数调用栈的模拟器结果信息，并压缩连续重复的行
    
    Returns:
        str: 模拟器输出的函数调用栈信息（已压缩连续重复行）
    """
    # 确保模拟器输出文件存在
    ensure_emulator_output_exists()
    
    # 定义正则表达式模式：捕获序号和核心内容
    # 模式匹配：空格 + 序号 + 空格 + 核心内容
    pattern = re.compile(r'\s+(\d+)\s+(.+)')
    
    compressed_lines = []
    prev_core = None
    start_seq = None
    end_seq = None
    
    with open(os.path.join(globs.script_path, "emulate/debug_output/function.txt"), "r") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                seq = int(match.group(1))
                core = match.group(2)
                
                if core == prev_core:
                    # 连续重复行，更新结束序号
                    end_seq = seq
                else:
                    # 新的核心内容，处理上一组
                    if prev_core:
                        if start_seq == end_seq:
                            # 只有一行，直接添加
                            compressed_lines.append(f"\t\t{start_seq} {prev_core}")
                        else:
                            # 多行连续重复，显示范围
                            compressed_lines.append(f"\t\t{start_seq}-{end_seq} {prev_core} (重复{((end_seq - start_seq) // 4) + 1}次)")
                    
                    # 重置当前组
                    prev_core = core
                    start_seq = seq
                    end_seq = seq
    
    # 处理最后一组
    if prev_core:
        if start_seq == end_seq:
            compressed_lines.append(f"\t\t{start_seq} {prev_core}")
        else:
            compressed_lines.append(f"\t\t{start_seq}-{end_seq} {prev_core} (重复{((end_seq - start_seq) // 4) + 1}次)")
    
    return "\n".join(compressed_lines)
