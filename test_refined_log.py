#!/usr/bin/env python3
"""
测试精炼日志功能的脚本
"""
import os
import json
import tempfile
from utils.ai_log_manager import ai_log_manager


def test_refined_log():
    """测试精炼日志功能"""
    # 初始化日志管理器
    ai_log_manager.set_enabled(True)
    
    # 创建临时目录
    tmp_dir = tempfile.mkdtemp()
    print(f"临时目录: {tmp_dir}")
    
    # 初始化会话
    session_id = ai_log_manager.initialize_session(tmp_dir)
    print(f"会话ID: {session_id}")
    
    # 测试消息序列
    test_state = {
        'messages': [
            {
                'role': 'system',
                'type': 'system',
                'content': 'Test system prompt'
            },
            {
                'role': 'user',
                'type': 'human',
                'content': 'Hello, test message 1'
            },
            {
                'role': 'assistant',
                'type': 'ai',
                'content': 'Response to message 1'
            },
            {
                'role': 'user',
                'type': 'human',
                'content': 'Hello, test message 2'
            },
            {
                'role': 'assistant',
                'type': 'ai',
                'content': 'Response to message 2',
                'tool_calls': [
                    {
                        'name': 'TestTool',
                        'args': {'param': 'test'},
                        'id': 'call_1'
                    }
                ]
            },
            {
                'role': 'tool',
                'type': 'tool',
                'name': 'TestTool',
                'content': '{"result": "success"}',
                'tool_call_id': 'call_1'
            }
        ]
    }
    
    # 记录精炼日志
    ai_log_manager.log_agent_refined_memory('test_agent', test_state, 'test_function')
    
    # 查找并显示日志文件
    log_subdir = os.path.join(tmp_dir, 'lcmhal_ai_log')
    if os.path.exists(log_subdir):
        print(f"\n日志子目录: {log_subdir}")
        print(f"文件列表: {os.listdir(log_subdir)}")
        
        # 查找精炼日志文件
        for filename in os.listdir(log_subdir):
            if filename.startswith('refined_'):
                log_path = os.path.join(log_subdir, filename)
                print(f"\n--- {filename} 内容 ---")
                with open(log_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    print(json.dumps(content, ensure_ascii=False, indent=2))
                    
                    # 验证交互顺序
                    print(f"\n--- 交互顺序验证 ---")
                    interactions = content.get('interactions', [])
                    for i, interaction in enumerate(interactions):
                        print(f"第 {i+1} 个交互: {interaction['type']} - {interaction['agent_name']} - {interaction.get('role', '')} - {interaction.get('tool_name', '')}")
    
    print(f"\n测试完成！")


if __name__ == "__main__":
    test_refined_log()
