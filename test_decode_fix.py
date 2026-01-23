#!/usr/bin/env python3
# 测试UTF-8解码修复

import sys
import os

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.db_file import read_file_from_db_zip, read_struct_with_start_line_from_db

def test_decode_fix():
    """测试UTF-8解码修复是否有效"""
    print("正在测试UTF-8解码修复...")
    
    # 测试参数
    db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    file_path = "home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/main.c"
    start_line = 70
    func_name = "main"
    
    # 测试1: 直接读取文件
    print(f"\n1. 测试读取文件: {file_path}")
    content, success = read_file_from_db_zip(db_path, file_path)
    if success:
        print("✅ 成功读取文件")
        print(f"   文件长度: {len(content)} 字节")
        print(f"   行数: {len(content.splitlines())}")
    else:
        print(f"❌ 读取文件失败: {content}")
        return False
    
    # 测试2: 读取结构体/函数定义
    print(f"\n2. 测试读取函数: {func_name} (起始行: {start_line})")
    struct_content, struct_content_in_lines = read_struct_with_start_line_from_db(db_path, file_path, start_line, func_name)
    if struct_content:
        print("✅ 成功读取函数定义")
        print(f"   函数内容长度: {len(struct_content)} 字节")
        print(f"   行数: {len(struct_content.splitlines())}")
        # 打印函数内容的前几行
        print("\n   函数内容前5行:")
        for i, line in enumerate(struct_content.splitlines()[:5]):
            print(f"   {i+1}: {line}")
    else:
        print("❌ 读取函数定义失败")
        return False
    
    print("\n✅ 所有测试通过！UTF-8解码修复有效。")
    return True

if __name__ == "__main__":
    test_decode_fix()
