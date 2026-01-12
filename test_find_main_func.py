#!/usr/bin/env python3
# 查找main函数的起始行号

import sys
import os

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.db_file import read_file_from_db_zip

def find_main_func():
    """查找main函数的起始行号"""
    print("正在查找main函数的起始行号...")
    
    # 测试参数
    db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    file_path = "home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/main.c"
    
    # 读取文件内容
    content, success = read_file_from_db_zip(db_path, file_path)
    if not success:
        print(f"❌ 读取文件失败: {content}")
        return
    
    lines = content.splitlines()
    print(f"\n文件总行数: {len(lines)}")
    
    # 查找main函数的起始行
    main_start_line = -1
    for i, line in enumerate(lines):
        if 'int main(' in line or 'void main(' in line:
            main_start_line = i + 1  # 行号从1开始
            print(f"\n找到main函数:")
            print(f"  行号: {main_start_line}")
            print(f"  内容: {line.strip()}")
            
            # 打印前后几行的内容
            start = max(0, i - 5)
            end = min(len(lines), i + 20)
            print(f"\n  上下文 ({start+1}-{end}行):")
            for j in range(start, end):
                prefix = "--> " if j == i else "    "
                print(f"  {prefix}{j+1:4d}: {lines[j]}")
            break
    
    if main_start_line == -1:
        print("❌ 未找到main函数")

if __name__ == "__main__":
    find_main_func()
