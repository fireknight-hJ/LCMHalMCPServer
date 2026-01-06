# Emulator工具的LangChain工具函数模块
# 提供直接调用的工具函数，使用@tool装饰器定义
from langchain.tools import tool
from tools.emulator.core import (
    emulate_proj as core_emulate_proj,
    mmio_function_emulate_info as core_mmio_function_emulate_info,
    function_calls_emulate_info as core_function_calls_emulate_info
)


@tool(
    "EmulateProject",
    description="Run emulator and return emulate result, including stdout, stderr and exitcode"
)
def emulate_proj() -> dict:
    """运行模拟器"""
    return core_emulate_proj()


@tool(
    "GetMMIOFunctionEmulateInfo",
    description="Get MMIO function emulate info from lcmhal.txt"
)
def mmio_function_emulate_info() -> str:
    """获取所有MMIO函数的模拟器结果信息"""
    return core_mmio_function_emulate_info()


@tool(
    "GetFunctionCallsEmulateInfo",
    description="Get function calls stack emulate info from function.txt"
)
def function_calls_emulate_info() -> str:
    """获取所有函数调用栈的模拟器结果信息"""
    return core_function_calls_emulate_info()
