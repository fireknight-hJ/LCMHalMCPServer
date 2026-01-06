#!/usr/bin/env python3
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.analyzer_agent import function_classify
import config.globs as globs
from utils.ai_log_manager import ai_log_manager
from utils.log_index import log_index_manager
import json

async def test_langgraph_logging():
    print("=" * 60)
    print("测试 LangGraph 节点日志记录")
    print("=" * 60)
    
    # 1. 初始化配置
    print("\n1. 初始化配置...")
    config = globs.load_config_from_yaml(globs.default_config["script_path"])
    globs.globs_init(config)
    
    session_id = globs.get_session_id()
    print(f"   Session ID: {session_id}")
    print(f"   日志目录: {globs.db_path}/lcmhal_ai_log")
    
    # 2. 测试 function_classify
    print("\n2. 测试 function_classify (这将触发 LangGraph 节点日志)...")
    try:
        result = await function_classify("HAL_ETH_ReadData", overwrite=True)
        print(f"   ✓ 分析完成")
        print(f"   结果: {result.model_dump_json()[:200]}...")
    except Exception as e:
        print(f"   ✗ 分析失败: {e}")
        import traceback
        traceback.print_exc()
    
    # 3. 检查 session 日志
    print("\n3. 检查 session 日志...")
    session_info = log_index_manager.get_session_info(session_id)
    if session_info and os.path.exists(session_info['session_file']):
        with open(session_info['session_file'], 'r', encoding='utf-8') as f:
            session_data = json.load(f)
            logs = session_data.get('logs', [])
            print(f"   总日志条目数: {len(logs)}")
            
            # 统计不同类型的日志
            log_types = {}
            langgraph_logs = []
            for log in logs:
                log_type = log.get('interaction_type', 'unknown')
                log_types[log_type] = log_types.get(log_type, 0) + 1
                
                if log_type == 'langgraph_node':
                    langgraph_logs.append(log)
            
            print(f"\n   日志类型统计:")
            for log_type, count in log_types.items():
                print(f"   - {log_type}: {count}")
            
            print(f"\n   LangGraph 节点日志详情:")
            for i, log in enumerate(langgraph_logs, 1):
                node_name = log.get('node_name', 'unknown')
                phase = log.get('metadata', {}).get('phase', 'unknown')
                messages_count = log.get('data', {}).get('messages_count', 0)
                function_name = log.get('function_name', 'unknown')
                print(f"   {i}. 节点: {node_name}, 阶段: {phase}, 消息数: {messages_count}, 函数: {function_name}")
                
                # 显示消息摘要
                messages_summary = log.get('data', {}).get('messages_summary', [])
                if messages_summary:
                    print(f"      消息摘要:")
                    for j, msg in enumerate(messages_summary[-3:], 1):  # 只显示最后3条消息
                        msg_type = msg.get('type', 'unknown')
                        content = msg.get('content', '')[:100]
                        print(f"      {j}. [{msg_type}] {content}...")
    else:
        print(f"   ✗ Session 日志文件不存在")
    
    # 4. 结束 session
    print("\n4. 结束 session...")
    globs.finalize_session()
    print("   ✓ Session 已结束")
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_langgraph_logging())
