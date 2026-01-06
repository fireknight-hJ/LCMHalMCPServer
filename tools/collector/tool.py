# Collector工具的LangChain工具函数模块
# 提供直接调用的工具函数，使用@tool装饰器定义
from typing import Dict, List, Optional, Any
from langchain.tools import tool
from tools.collector.core import (
    get_global_codebase_infos,
    register_db,
    get_files_in_db_zip,
    get_tree_in_db_zip,
    get_mmio_func_list,
    get_mmio_files,
    get_mmio_func_info,
    get_function_info,
    get_struct_or_enum_info,
    get_func_call_stack,
    get_driver_info,
    validate_database
)


@tool(
    "RegisterDatabase",
    description="Register database path for collector tool"
)
async def register_db_tool(db_path: str) -> bool:
    """注册数据库路径"""
    return register_db(db_path)


@tool(
    "ValidateDatabase",
    description="Validate database path and integrity"
)
async def validate_database_tool(db_path: str) -> Dict[str, Any]:
    """验证数据库路径和完整性"""
    return validate_database(db_path)


@tool(
    "GetFilesInDatabaseZip",
    description="Get files list in database zip file"
)
async def get_files_in_db_zip_tool(db_path: str) -> List[str]:
    """获取数据库zip文件中的文件列表"""
    return get_files_in_db_zip(db_path)


@tool(
    "GetDirectoryTreeInDatabaseZip",
    description="Get directory tree in database zip file"
)
async def get_tree_in_db_zip_tool(db_path: str) -> str:
    """获取数据库zip文件中的目录树"""
    return get_tree_in_db_zip(db_path)


@tool(
    "GetMMIOFunctionList",
    description="Get MMIO function list from database"
)
async def get_mmio_func_list_tool(db_path: str) -> List[str]:
    """获取MMIO函数列表"""
    return get_mmio_func_list(db_path)


@tool(
    "GetMMIORelatedFiles",
    description="Get MMIO related files list from database"
)
async def get_mmio_files_tool(db_path: str) -> List[str]:
    """获取MMIO相关文件列表"""
    return get_mmio_files(db_path)


@tool(
    "GetMMIOFunctionInfo",
    description="Get MMIO function detailed information from database"
)
async def get_mmio_func_info_tool(db_path: str, func_name: str) -> Dict[str, Any]:
    """获取MMIO函数详细信息"""
    return get_mmio_func_info(db_path, func_name)


@tool(
    "GetFunctionInfo",
    description="Get general function information from database"
)
async def get_function_info_tool(db_path: str, func_name: str) -> Optional[Any]:
    """获取通用函数信息"""
    return get_function_info(db_path, func_name)


@tool(
    "GetStructOrEnumInfo",
    description="Get struct or enum information from database"
)
async def get_struct_or_enum_info_tool(db_path: str, struct_name: str) -> Dict[str, Any]:
    """获取结构体或枚举信息"""
    return get_struct_or_enum_info(db_path, struct_name)


@tool(
    "GetFunctionCallStack",
    description="Get function call stack from database"
)
async def get_func_call_stack_tool(db_path: str, func_name: str, layer_cnt: int = 1) -> Dict[str, Any]:
    """获取函数调用栈"""
    return get_func_call_stack(db_path, func_name, layer_cnt)


@tool(
    "GetDriverInfo",
    description="Get driver information from database"
)
async def get_driver_info_tool(db_path: str, driver_name: str) -> Optional[Any]:
    """获取驱动信息"""
    return get_driver_info(db_path, driver_name)
