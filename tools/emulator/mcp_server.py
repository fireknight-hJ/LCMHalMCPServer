from fastmcp import FastMCP
import json
import config.globs as globs
import asyncio
from models.build_results.build_output import BuildOutput
from models.analyze_results.function_analyze import ReplacementUpdate
import os

# 导入核心功能模块
from tools.emulator.core import emulate_proj as core_emulate_proj
from tools.emulator.core import mmio_function_emulate_info as core_mmio_function_emulate_info
from tools.emulator.core import function_calls_emulate_info as core_function_calls_emulate_info

# 用于模拟执行代码并返回输出的mcp服务器

mcp = FastMCP("LCMHalMCP", version="1.0.0")

@mcp.tool()
async def emulate_proj() -> dict:
    """run emulator with generated configs, return the emulation result"""
    return core_emulate_proj()

@mcp.tool()
async def mmio_function_emulate_info() -> str:
    """return the emulator results of all mmio functions being used"""
    return core_mmio_function_emulate_info()

@mcp.tool()
async def function_calls_emulate_info() -> str:
    """return the emulator results of all function call stack being used"""
    return core_function_calls_emulate_info()

# @mcp.tool()
# async def get_decompiled_code_by_pc_address(address: int) -> str:
#     """return the decompiled code by the given pc address"""
#     with open(os.path.join(globs.script_path, "emulate/debug_output/decompiled_code.txt"), "r") as f:
#         data = f.read()
#     return data

if __name__ == "__main__":
    # 导入argparse模块（如果尚未导入）
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='LCMHal MCP Server')
    # 添加--script-dir选项参数，设置help信息
    parser.add_argument('--script-dir', dest='script_path', help='Path to the compilation script directory', required=True)
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 从命令行参数设置script_path
    globs.script_path = args.script_path
    # 从配置文件加载配置
    config = globs.load_config_from_yaml(globs.script_path)
    
    # 设置全局变量
    globs.globs_init(config)

    # 启动mcp服务器
    mcp.run(transport="stdio")