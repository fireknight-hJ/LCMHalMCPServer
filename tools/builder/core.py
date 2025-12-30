# Builder工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
from tools.builder.proj_builder import build_proj, clear_proj
from tools.collector.collector import get_function_info
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace
from core.data_manager import data_manager


def replace_funcs():
    """替换需要替换的函数"""
    mmio_info_list = data_manager.get_mmio_info_list()
    replacement_updates = data_manager.get_replacement_updates()
    
    for func_name, classify_res in mmio_info_list.items():
        if func_name in replacement_updates:
            replace_res = function_replace(get_function_info(globs.db_path, func_name), replacement_updates[func_name].replacement_code)
        elif classify_res.has_replacement:
            replace_res = function_replace(get_function_info(globs.db_path, func_name), classify_res.function_replacement)


def recover_funcs():
    """恢复被替换的函数"""
    mmio_info_list = data_manager.get_mmio_info_list()
    
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            recover_res = function_recover(get_function_info(globs.db_path, func_name))


def build_project() -> dict:
    """构建项目
    
    Returns:
        dict: 构建结果，包含std_err和exit_code
    """
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


def get_replace_func_details_by_file(file_path: str) -> dict:
    """根据文件路径获取替换函数详情
    
    Args:
        file_path: 文件的完整路径
        
    Returns:
        dict: 替换函数的详细信息
    """
    return data_manager.get_replace_func_details_by_file(file_path)


def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """更新函数替换代码
    
    Args:
        func_name: 函数名称
        replace_code: 替换代码
        reason: 替换原因
        
    Returns:
        dict: 更新结果
    """
    if not data_manager.update_function_replacement(func_name, replace_code, reason):
        return {"error": f"Function {func_name} not found in MMIO function list."}
    
    return {
        "function_name": func_name,
        "status": "success"
    }


def init_builder():
    """初始化builder工具
    
    加载MMIO函数信息
    """
    # 加载MMIO函数信息
    data_manager.load_mmio_functions()
