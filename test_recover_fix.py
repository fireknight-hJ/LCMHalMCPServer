#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试recover_funcs()修复是否正确
"""

import os
import sys
import tempfile
import shutil

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.builder.core import recover_funcs
from core.data_manager import data_manager
import config.globs as globs

# 模拟测试环境
def test_recover_funcs():
    # 设置模拟配置
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    
    # 模拟一些替换更新
    test_funcs = ["HAL_UART_IRQHandler", "HAL_UART_Transmit_IT"]
    
    # 手动添加一些替换更新到data_manager
    from models.analyze_results.function_analyze import ReplacementUpdate
    for func_name in test_funcs:
        replacement_update = ReplacementUpdate(
            function_name=func_name,
            replacement_code="/* Test replacement */",
            reason="Test"
        )
        data_manager.replacement_updates[func_name] = replacement_update
    
    print("=== Testing recover_funcs() fix ===")
    print(f"mmio_info_list contains {len(data_manager.get_mmio_info_list())} functions")
    print(f"replacement_updates contains {len(data_manager.get_replacement_updates())} functions")
    
    # 测试修复后的recover_funcs
    import asyncio
    asyncio.run(data_manager.load_mmio_functions())
    
    print("\n=== Calling recover_funcs() ===")
    recover_funcs()
    print("recover_funcs() completed successfully")
    
    # 清理测试数据
    data_manager.replacement_updates.clear()

if __name__ == "__main__":
    test_recover_funcs()