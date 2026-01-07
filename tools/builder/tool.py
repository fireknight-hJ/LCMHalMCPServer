# Builder工具的LangChain工具函数模块
# 提供直接调用的工具函数，使用@tool装饰器定义
import asyncio
from langchain.tools import tool
from tools.builder.core import (
    build_project as core_build_project,
    get_replace_func_details_by_file as core_get_replace_func_details_by_file,
    update_function_replacement as core_update_function_replacement,
    get_function_analysis_and_replacement as core_get_function_analysis_and_replacement,
    get_function_analysis_and_replacement_formatted as core_get_function_analysis_and_replacement_formatted,
    init_builder as core_init_builder
)


@tool(
    "BuildProject",
    description="Build project and return build result, including exitcode and stderr output"
)
def build_project() -> dict:
    """构建项目"""
    return core_build_project()


@tool(
    "GetReplaceFuncDetailsByFile",
    description="Get replacement functions info of the corresponding file"
)
def get_replace_func_details_by_file(file_path: str) -> dict:
    """根据文件路径获取替换函数详情"""
    return core_get_replace_func_details_by_file(file_path)


@tool(
    "UpdateFunctionReplacement",
    description="Update function replacement code"
)
def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """更新函数替换代码"""
    return core_update_function_replacement(func_name, replace_code, reason)


@tool(
    "InitBuilder",
    description="Initialize builder tool"
)
def init_builder() -> dict:
    """初始化builder工具"""
    asyncio.run(core_init_builder())
    return {"status": "success", "message": "Builder tool initialized successfully"}


@tool(
    "GetFunctionAnalysisAndReplacement",
    description="Get function analysis (MMIO info) and replacement details by function name"
)
def get_function_analysis_and_replacement(func_name: str) -> dict:
    """根据函数名获取函数分析和替换信息"""
    return core_get_function_analysis_and_replacement(func_name)


@tool(
    "GetFunctionAnalysisAndReplacementFormatted",
    description="Get formatted function analysis (MMIO info) and replacement details by function name, easier for LLM to understand"
)
def get_function_analysis_and_replacement_formatted(func_name: str) -> str:
    """根据函数名获取格式化的函数分析和替换信息，便于大模型理解"""
    return core_get_function_analysis_and_replacement_formatted(func_name)
