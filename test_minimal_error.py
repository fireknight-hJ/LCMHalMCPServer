#!/usr/bin/env python3
"""
最小化测试，重现'Missing required config key 'N/A' for 'tools''错误
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
from langchain_deepseek import ChatDeepSeek
from config.llm_config import llm_deepseek_config

async def test_error():
    """测试错误重现"""
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
        
        print("3. 初始化模型...")
        model = ChatDeepSeek(
            model=llm_deepseek_config["model_name"], 
            api_key=llm_deepseek_config["api_key"], 
            api_base=llm_deepseek_config["base_url"]
        )
        
        print("4. 绑定工具到模型...")
        model_with_tools = model.bind_tools(tools)
        
        print("5. 调用模型...")
        # 模拟analyzer_agent的调用
        from langchain_core.messages import HumanMessage
        
        messages = [
            {"role": "system", "content": "You are an analyzer agent."},
            {"role": "user", "content": "Classify the function: complex_mmio_operation"}
        ]
        
        # 转换为HumanMessage格式
        langchain_messages = [HumanMessage(content="Classify the function: complex_mmio_operation")]
        
        print("6. 调用模型（这可能会触发错误）...")
        response = await model_with_tools.ainvoke(langchain_messages)
        
        print(f"7. 响应: {response}")
        return True
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_error())
    if success:
        print("\n✓ 测试成功，错误未重现")
    else:
        print("\n✗ 测试失败，错误重现")
