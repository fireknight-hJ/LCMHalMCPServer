#!/usr/bin/env python3
"""
测试修正方案：在调用MCP工具之前正确初始化globs模块
"""
import sys
import asyncio
sys.path.append('.')

import config.globs as globs
from config.globs import globs_init, load_config_from_yaml

# 初始化globs
script_path = '/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver'
config = load_config_from_yaml(script_path)
globs_init(config)

print(f"globs初始化完成:")
print(f"  db_path: {globs.db_path}")
print(f"  script_path: {globs.script_path}")

# 现在导入analyzer_agent
from agents.analyzer_agent import analyze_functions

async def test():
    functions = ['complex_mmio_operation']
    try:
        print(f"开始分析函数: {functions}")
        result = await analyze_functions(functions)
        print(f'分析结果: {result}')
        return True
    except Exception as e:
        print(f'异常: {e}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test())
    if success:
        print("测试成功！错误已修复。")
    else:
        print("测试失败。")
