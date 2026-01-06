# Emulator工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
import os
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


def mmio_function_emulate_info() -> str:
    """获取所有MMIO函数的模拟器结果信息
    
    Returns:
        str: 模拟器输出的MMIO函数信息
    """
    with open(os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt"), "r") as f:
        data = "".join(f.readlines())
    return data


def function_calls_emulate_info() -> str:
    """获取所有函数调用栈的模拟器结果信息
    
    Returns:
        str: 模拟器输出的函数调用栈信息
    """
    with open(os.path.join(globs.script_path, "emulate/debug_output/function.txt"), "r") as f:
        data = "".join(f.readlines())
    return data
