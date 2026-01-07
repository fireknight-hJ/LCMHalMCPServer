#!/usr/bin/env python3
# 测试函数调用栈信息压缩功能

import sys
import os

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tools.emulator.core import function_calls_emulate_info

def main():
    """测试压缩功能"""
    print("正在获取并压缩函数调用栈信息...")
    compressed_content = function_calls_emulate_info()
    
    # 打印压缩后的内容
    print("\n压缩后的函数调用栈信息：")
    print(compressed_content)
    
    # 统计压缩效果
    original_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver/emulate/debug_output/function.txt"
    with open(original_path, 'r') as f:
        original_lines = f.readlines()
    
    compressed_lines = compressed_content.split('\n')
    
    print(f"\n压缩效果统计：")
    print(f"原始行数：{len(original_lines)}")
    print(f"压缩后行数：{len(compressed_lines)}")
    print(f"压缩率：{((1 - len(compressed_lines)/len(original_lines)) * 100):.2f}%")

if __name__ == "__main__":
    main()
