#!/usr/bin/env python3
"""
测试ToolNode，重现'Missing required config key 'N/A' for 'tools''错误
"""
import sys
import asyncio
sys.path.append('.')

# 设置globs配置
import config.globs as globs
from config.globs import globs_init, load_config_from_yaml

# 初始化globs
script_path = '/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver'
config = load_config_from_yaml(script_path)
globs_init(config)

print(f"globs配置:")
print(f"  db_path: {globs.db_path}")
print(f"  script_path: {globs.script_path}")

# 导入必要的模块
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import ToolNode

async def test_toolnode():
    """测试ToolNode"""
    try:
        print("\n1. 创建MCP客户端...")
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
        
        print("2. 获取工具...")
        tools = await client.get_tools()
        print(f"获取到 {len(tools)} 个工具")
        
        print("3. 创建ToolNode...")
        tool_node = ToolNode(tools)
        
        print("4. 创建测试状态...")
        test_state = {
            "messages": [
                {"role": "user", "content": "Test"}
            ]
        }
        
        print("5. 调用ToolNode（这可能会触发错误）...")
        result = await tool_node.ainvoke(test_state)
        
        print(f"6. 结果: {result}")
        return True
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_toolnode())
    if success:
        print("\n✓ 测试成功，错误未重现")
    else:
        print("\n✗ 测试失败，错误重现")
