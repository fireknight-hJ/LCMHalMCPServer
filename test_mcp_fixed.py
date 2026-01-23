#!/usr/bin/env python3
"""
测试修正的MCP客户端配置
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

print(f"globs配置:")
print(f"  db_path: {globs.db_path}")
print(f"  script_path: {globs.script_path}")

# 直接导入MCP客户端
from langchain_mcp_adapters.client import MultiServerMCPClient

async def test_mcp_fixed():
    try:
        print("\n创建修正的MCP客户端...")
        client = MultiServerMCPClient(
            {
                "lcmhal_collector": {
                    "command": "python",
                    "args": [
                        "-m",
                        "tools.collector.mcp_server",
                        "--db-path",
                        globs.db_path,
                        "--transport",
                        "stdio"
                    ],
                    "transport": "stdio",
                    # 添加所有可能的键
                    "name": "lcmhal_collector",
                    "description": "LCMHal MCP Collector Server",
                    "version": "1.0.0",
                },
            }
        )
        
        print("获取工具...")
        tools = await client.get_tools()
        print(f"获取到 {len(tools)} 个工具")
        
        # 测试调用一个工具
        if tools:
            print(f"\n测试调用工具: {tools[0].name}")
            # 注意：这里只是测试工具获取，不实际调用
            
        return True
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_analyzer():
    """测试analyzer_agent"""
    try:
        print("\n测试analyzer_agent...")
        from agents.analyzer_agent import analyze_functions
        
        functions = ['complex_mmio_operation']
        print(f"分析函数: {functions}")
        result = await analyze_functions(functions)
        print(f"分析结果: {result}")
        return True
    except Exception as e:
        print(f"analyzer_agent错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("测试1: 直接MCP客户端")
    print("=" * 60)
    success1 = asyncio.run(test_mcp_fixed())
    
    print("\n" + "=" * 60)
    print("测试2: analyzer_agent")
    print("=" * 60)
    success2 = asyncio.run(test_analyzer())
    
    if success1 and success2:
        print("\n✓ 所有测试成功")
    else:
        print("\n✗ 某些测试失败")
