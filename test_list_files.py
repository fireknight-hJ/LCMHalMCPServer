#!/usr/bin/env python3
# 查看src.zip中的文件结构

import sys
import os

# 将项目根目录添加到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.db_file import list_files_in_db_zip

def list_files():
    """查看src.zip中的文件结构"""
    print("正在查看src.zip中的文件结构...")
    
    # 测试参数
    db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    
    files = list_files_in_db_zip(db_path)
    print(f"\n文件列表 ({len(files)} 个文件):")
    
    # 过滤出main.c文件
    main_c_files = [f for f in files if 'main.c' in f]
    print(f"\n包含 'main.c' 的文件 ({len(main_c_files)} 个):")
    for f in main_c_files:
        print(f"  {f}")
    
    # 过滤出Src目录下的文件
    src_files = [f for f in files if 'Src/' in f]
    print(f"\nSrc目录下的文件 ({len(src_files)} 个):")
    for f in src_files[:10]:  # 只显示前10个
        print(f"  {f}")
    if len(src_files) > 10:
        print(f"  ... 还有 {len(src_files) - 10} 个文件")

if __name__ == "__main__":
    list_files()
