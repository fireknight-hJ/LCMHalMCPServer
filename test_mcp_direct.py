#!/usr/bin/env python3
"""
直接测试MCP工具调用
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

async def test_mcp():
    try:
        print("\n创建MCP客户端...")
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
                    "transport": "stdio"
                },
            }
        )
        
        print("获取工具...")
        tools = await client.get_tools()
        print(f"获取到 {len(tools)} 个工具")
        
        for i, tool in enumerate(tools):
            print(f"工具 {i+1}: {tool.name}")
        
        return True
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_mcp())
    if success:
        print("\n✓ MCP工具调用成功")
    else:
        print("\n✗ MCP工具调用失败")
