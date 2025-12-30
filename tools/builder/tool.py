# Builder工具的LangChain工具函数模块
# 提供直接调用的工具函数，使用@tool装饰器定义
from langchain.tools import tool
from tools.builder.core import (
    build_project as core_build_project,
    get_replace_func_details_by_file as core_get_replace_func_details_by_file,
    update_function_replacement as core_update_function_replacement,
    init_builder as core_init_builder
)


@tool(
    "BuildProject",
    description="Build project and return build result, including exitcode and stderr output"
)
async def build_project():
    """构建项目"""
    return core_build_project()


@tool(
    "GetReplaceFuncDetailsByFile",
    description="Get replacement functions info of the corresponding file"
)
async def get_replace_func_details_by_file(file_path: str):
    """根据文件路径获取替换函数详情"""
    return core_get_replace_func_details_by_file(file_path)


@tool(
    "UpdateFunctionReplacement",
    description="Update function replacement code"
)
async def update_function_replacement(func_name: str, replace_code: str, reason: str):
    """更新函数替换代码"""
    return core_update_function_replacement(func_name, replace_code, reason)


@tool(
    "InitBuilder",
    description="Initialize builder tool"
)
async def init_builder():
    """初始化builder工具"""
    core_init_builder()
    return {"status": "success", "message": "Builder tool initialized successfully"}
