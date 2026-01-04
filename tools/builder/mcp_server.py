from fastmcp import FastMCP
import config.globs as globs
import asyncio
from tools.builder.core import build_project as core_build_project
from tools.builder.core import get_replace_func_details_by_file as core_get_replace_func_details_by_file
from tools.builder.core import update_function_replacement as core_update_function_replacement
from tools.builder.core import init_builder

mcp = FastMCP("LCMHalMCP", version="1.0.0")

@mcp.tool()
async def build_project() -> dict:
    """build project, return build result, including exitcode and stderr output"""
    return core_build_project()

@mcp.tool()
async def get_replace_func_details_by_file(file_path: str) -> dict:
    """get replacement functions info of the corresponding file, please make sure the function to be analyzed
    file_path: the full path of the file in the codebase
    replace_func_infos: list of Functions replacement info 
    replacement_updates: list of Functions that have been updated before due to build failure"""
    return core_get_replace_func_details_by_file(file_path)

@mcp.tool()
async def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """get all replacement functions info"""
    return core_update_function_replacement(func_name, replace_code, reason)


def init_mcp():
    """初始化MCP服务"""
    # 加载MMIO函数信息
    asyncio.run(init_builder())


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
    # 初始化服务
    init_mcp()

    # 启动mcp服务器
    mcp.run(transport="stdio")