from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage
from config.llm_config import llm_deepseek_config
from prompts.summary_prompt import failcheck_analyze_prompt_en, failcheck_analyze_prompt_zh
import sys
import config.globs as globs
from utils.ai_log_manager import ai_log_manager
import os
import time

# Initialize the model for failcheck analysis
failcheck_model = ChatDeepSeek(
    model=llm_deepseek_config["model_name"], 
    api_key=llm_deepseek_config["api_key"], 
    api_base=llm_deepseek_config["base_url"]
)

def format_conversation_history(messages):
    """格式化对话历史，为每个消息添加编号"""
    formatted = []
    for i, msg in enumerate(messages, 1):
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        formatted.append(f"Message {i} [{role}]: {content[:100]}{'...' if len(content) > 100 else ''}")
    return "\n".join(formatted)

def analyze_failed_conversation(messages, agent_name="Unknown Agent", max_iterations=50):
    """分析失败的对话历史并生成报告"""
    print(f"\n{'='*50}")
    print(f"FAILCHECK ACTIVATED")
    print(f"Agent: {agent_name}")
    print(f"Iterations exceeded: {max_iterations}")
    print(f"Total messages: {len(messages)}")
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

