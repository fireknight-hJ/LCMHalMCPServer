#!/usr/bin/env python3
"""
测试按函数名获取分析和替换信息的功能
"""
import sys
import os
import asyncio

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.data_manager import data_manager
from tools.builder.core import get_function_analysis_and_replacement
from tools.builder.core import init_builder


def test_function_info():
    """测试获取函数信息的功能"""
    # 测试不存在的函数
    print("测试不存在的函数:")
    result = get_function_analysis_and_replacement("non_existent_function")
    print(f"结果: {result}\n")
    
    # 测试MMIO信息（如果有）
    print("测试获取MMIO信息:")
    # 假设存在一个名为"example_func"的函数
    # 实际测试时需要替换为真实存在的函数名
    result = get_function_analysis_and_replacement("example_func")
    print(f"结果: {result}\n")


async def main():
    """主函数"""
    print("初始化数据管理器...")
    await init_builder()
    
    print("数据加载完成，开始测试...")
    test_function_info()


if __name__ == "__main__":
    asyncio.run(main())
