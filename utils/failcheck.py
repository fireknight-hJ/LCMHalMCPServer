from langchain_core.messages import HumanMessage
from config.model_singleton import get_model
from prompts.summary_prompt import failcheck_analyze_prompt_en, failcheck_analyze_prompt_zh
import sys
import config.globs as globs
from utils.ai_log_manager import ai_log_manager
import os
import time
import json
import glob

# 使用统一的模型实例
failcheck_model = get_model()


def get_latest_session_log(db_path: str) -> str:
    """获取最新的session日志文件路径"""
    log_dir = os.path.join(db_path, "lcmhal_ai_log")
    if not os.path.exists(log_dir):
        return None
    
    pattern = os.path.join(log_dir, "session_*.json")
    files = glob.glob(pattern)
    
    if not files:
        return None
    
    latest_file = max(files, key=os.path.getmtime)
    return latest_file


def load_conversation_from_session_log(session_log_file: str) -> list:
    """从session日志文件加载完整的对话历史"""
    if not session_log_file or not os.path.exists(session_log_file):
        return []
    
    try:
        with open(session_log_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
        
        logs = session_data.get("logs", [])
        
        all_messages = []
        
        for log in logs:
            if log.get("interaction_type") != "langgraph_node":
                continue
            
            node_name = log.get("node_name", "")
            if node_name not in ["call_model", "respond", "tools"]:
                continue
            
            data = log.get("data", {})
            new_messages_summary = data.get("new_messages_summary", [])
            
            for msg in new_messages_summary:
                role = msg.get("role", "")
                content = msg.get("content", "")
                msg_type = msg.get("type", "")
                
                if not content and msg_type != "AIMessage":
                    continue
                
                if role in ["user", "human"]:
                    all_messages.append({"role": "user", "content": content})
                elif role == "assistant" or msg_type == "AIMessage":
                    tool_calls = msg.get("tool_calls", [])
                    if tool_calls:
                        for tc in tool_calls:
                            all_messages.append({
                                "role": "assistant", 
                                "content": f"[Tool Call: {tc.get('name')}] {tc.get('args', '')}"
                            })
                    if content:
                        all_messages.append({"role": "assistant", "content": content})
        
        return all_messages
        
    except Exception as e:
        print(f"[WARN] Failed to load session log: {e}")
        return []


def format_conversation_history(messages, max_messages=100, max_content_length=500):
    """格式化对话历史，为每个消息添加编号"""
    formatted = []
    seen_contents = set()
    
    for i, msg in enumerate(messages, 1):
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        
        content_key = f"{role}:{content[:50]}"
        if content_key in seen_contents:
            continue
        seen_contents.add(content_key)
        
        truncated = content[:max_content_length]
        if len(content) > max_content_length:
            truncated += "..."
        
        formatted.append(f"Message {i} [{role}]: {truncated}")
        
        if len(formatted) >= max_messages:
            formatted.append(f"... (and {len(messages) - max_messages} more messages)")
            break
    
    return "\n".join(formatted)

def analyze_failed_conversation(messages, agent_name="Unknown Agent", max_iterations=50, db_path: str = None):
    """分析失败的对话历史并生成报告"""
    print(f"\n{'='*50}")
    print(f"FAILCHECK ACTIVATED")
    print(f"Agent: {agent_name}")
    print(f"Iterations exceeded: {max_iterations}")
    print(f"Total messages (initial): {len(messages)}")
    
    # 尝试从session日志获取完整对话历史
    if db_path is None:
        db_path = getattr(globs, 'db_path', None)
    
    if db_path:
        session_log = get_latest_session_log(db_path)
        if session_log:
            print(f"Loading conversation from: {session_log}")
            full_messages = load_conversation_from_session_log(session_log)
            if full_messages and len(full_messages) > len(messages):
                messages = full_messages
                print(f"Loaded {len(messages)} messages from session log")
    
    print(f"Total messages (for analysis): {len(messages)}")
    print(f"{'='*50}\n")
    
    # 格式化对话历史
    formatted_history = format_conversation_history(messages)
    
    # 选择合适的提示语言
    prompt_template = failcheck_analyze_prompt_zh if globs.language_preference == "zh" else failcheck_analyze_prompt_en
    
    # 生成分析提示
    prompt = prompt_template.format(conversation_history=formatted_history)
    
    analysis_report = ""
    
    try:
        # 调用LLM进行分析
        response = failcheck_model.invoke([HumanMessage(content=prompt)])
        analysis_report = response.content
        
        print("\n" + "="*50)
        print("FAILCHECK ANALYSIS REPORT")
        print("="*50)
        print(analysis_report)
        print("\n" + "="*50)
        
    except Exception as e:
        print(f"\nError generating failcheck analysis: {e}")
        print("\nFallback analysis:")
        fallback_analysis = f"- Agent: {agent_name}\n- Failed due to exceeding max iterations ({max_iterations})\n- Total messages in conversation: {len(messages)}\n- Message preview:"
        message_preview = ""
        for i, msg in enumerate(messages[-5:], max(1, len(messages)-4)):
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            preview_line = f"  Message {i} [{role}]: {content[:100]}{'...' if len(content) > 100 else ''}"
            message_preview += f"\n{preview_line}"
            print(preview_line)
        
        analysis_report = fallback_analysis + message_preview
    
    print(f"\n{'='*50}")
    print(f"FAILCHECK COMPLETE - PROGRAM TERMINATED")
    print(f"{'='*50}\n")
    
    # 保存分析结果到日志
    if globs.ai_log_enable:
        # 使用ai_log_manager保存
        ai_log_manager.log_agent_error(
            agent_name=agent_name,
            error=analysis_report,
            function_name="failcheck_analysis",
            metadata={
                "max_iterations": max_iterations,
                "total_messages": len(messages),
                "analysis_type": "failcheck"
            }
        )
    
    # 保存分析结果到单独的文件
    try:
        # 创建failcheck日志目录
        failcheck_log_dir = os.path.join(globs.db_path, "lcmhal_failcheck_logs")
        os.makedirs(failcheck_log_dir, exist_ok=True)
        
        # 生成日志文件名
        timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        log_filename = f"failcheck_{agent_name}_{timestamp}.txt"
        log_filepath = os.path.join(failcheck_log_dir, log_filename)
        
        # 保存分析报告
        with open(log_filepath, 'w', encoding='utf-8') as f:
            f.write("FAILCHECK ANALYSIS REPORT\n")
            f.write("="*50 + "\n")
            f.write(f"Agent: {agent_name}\n")
            f.write(f"Iterations exceeded: {max_iterations}\n")
            f.write(f"Total messages: {len(messages)}\n")
            f.write(f"Analysis time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")
            f.write("="*50 + "\n\n")
            f.write(analysis_report)
        
        print(f"\n[INFO] Failcheck report saved to: {log_filepath}")
        
    except Exception as e:
        print(f"\n[ERROR] Failed to save failcheck report: {e}")
    
    # 彻底终止程序
    sys.exit(1)

