from fastmcp import FastMCP
import config.globs as globs
import asyncio
from tools.builder.proj_builder import build_proj, clear_proj
from tools.collector.collector import get_function_info
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace
from core.data_manager import data_manager

mcp = FastMCP("LCMHalMCP", version="1.0.0")

def replace_funcs():
    mmio_info_list = data_manager.get_mmio_info_list()
    replacement_updates = data_manager.get_replacement_updates()
    
    for func_name, classify_res in mmio_info_list.items():
        if func_name in replacement_updates:
            replace_res = function_replace(get_function_info(globs.db_path, func_name), replacement_updates[func_name].replacement_code)
        elif classify_res.has_replacement:
            replace_res = function_replace(get_function_info(globs.db_path, func_name), classify_res.function_replacement)

def recover_funcs():
    mmio_info_list = data_manager.get_mmio_info_list()
    
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            recover_res = function_recover(get_function_info(globs.db_path, func_name))

@mcp.tool()
async def build_project() -> dict:
    """build project, return build result, including exitcode and stderr output"""
    # 替换文件
    replace_funcs()
    # 编译项目
    clear_proj(globs.script_path)
    build_info = build_proj(globs.script_path)
    # 项目复原
    recover_funcs()
    # 结果输出
    return {
        "std_err": build_info.std_err,
        "exit_code": build_info.exit_code
    }

@mcp.tool()
async def get_replace_func_details_by_file(file_path: str) -> dict:
    """get replacement functions info of the corresponding file, please make sure the function to be analyzed
    file_path: the full path of the file in the codebase
    replace_func_infos: list of Functions replacement info 
    replacement_updates: list of Functions that have been updated before due to build failure"""
    return data_manager.get_replace_func_details_by_file(file_path)

@mcp.tool()
async def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """get all replacement functions info"""
    if not data_manager.update_function_replacement(func_name, replace_code, reason):
        return {"error": f"Function {func_name} not found in MMIO function list."}
    
    return {
        "function_name": func_name,
        "status": "success"
    }

def init_mcp():
    """初始化MCP服务"""
    # 加载MMIO函数信息
    data_manager.load_mmio_functions()


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