#!/usr/bin/env python3
"""
测试builder工具的功能
"""
import sys
import os

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.builder.tool import (
    build_project,
    get_replace_func_details_by_file,
    update_function_replacement,
    get_function_analysis_and_replacement,
    init_builder
)
from tools.builder.core import get_function_analysis_and_replacement as core_get_function_analysis_and_replacement


def test_builder_tools_import():
    """测试builder工具的导入是否正常"""
    print("测试builder工具的导入...")
    
    # 检查所有工具是否成功导入
    tools = [
        build_project,
        get_replace_func_details_by_file,
        update_function_replacement,
        get_function_analysis_and_replacement,
        init_builder
    ]
    
    for tool_obj in tools:
        print(f"成功导入工具: {tool_obj.name}")
    
    print("\n所有工具导入成功!")
    
    # 测试核心功能是否可以直接调用
    print("\n测试核心功能...")
    try:
        # 可以替换为实际存在的函数名进行测试
        result = core_get_function_analysis_and_replacement("example_func")
        print(f"核心功能测试结果: {result}")
    except Exception as e:
        print(f"核心功能测试失败: {e}")


if __name__ == "__main__":
    test_builder_tools_import()
