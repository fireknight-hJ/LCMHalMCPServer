#!/usr/bin/env python3
"""
测试MCP服务器启动和基本功能
"""

import os
import sys
import time
import subprocess
import threading
from pathlib import Path

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 配置
PROJECT_ROOT = Path(__file__).parent
LOG_DIR = PROJECT_ROOT / "zephyr-driver-db" / "log"
LOG_FILE = LOG_DIR / "mcp_server_test.log"

# 确保日志目录存在
LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_message(message, level="INFO"):
    """记录日志消息"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    # 写入文件
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    # 输出到控制台
    print(f"{level}: {message}")
    
    return log_entry

def test_mcp_server_import():
    """测试MCP服务器导入"""
    log_message("测试MCP服务器导入")
    
    servers_to_test = [
        ("tools.collector.mcp_server", "收集器MCP服务器"),
        ("tools.analyzer.mcp_server", "分析器MCP服务器"),
        ("tools.builder.mcp_server", "构建器MCP服务器"),
        ("tools.emulator.mcp_server", "仿真器MCP服务器"),
        ("server", "主服务器")
    ]
    
    results = []
    
    for module_name, description in servers_to_test:
        try:
            log_message(f"导入 {description} ({module_name})")
            
            # 动态导入
            if module_name == "server":
                module = __import__("server")
            else:
                module_parts = module_name.split('.')
                module = __import__(module_parts[0])
                for part in module_parts[1:]:
                    module = getattr(module, part)
            
            # 检查是否有mcp对象
            if hasattr(module, 'mcp'):
                mcp = module.mcp
                results.append({
                    "server": description,
                    "import_success": True,
                    "has_mcp": True,
                    "mcp_type": type(mcp).__name__
                })
                log_message(f"{description} 导入成功，包含MCP对象")
            else:
                results.append({
                    "server": description,
                    "import_success": True,
                    "has_mcp": False
                })
                log_message(f"{description} 导入成功，但不包含MCP对象")
                
        except Exception as e:
            results.append({
                "server": description,
                "import_success": False,
                "error": str(e)
            })
            log_message(f"{description} 导入失败: {str(e)}", "ERROR")
    
    return results

def test_mcp_tools():
    """测试MCP工具"""
    log_message("测试MCP工具")
    
    try:
        # 导入收集器MCP服务器并检查工具
        from tools.collector.mcp_server import mcp
        
        # 获取工具列表
        tools = mcp._tools if hasattr(mcp, '_tools') else {}
        
        tool_list = []
        for tool_name, tool_info in tools.items():
            tool_list.append({
                "name": tool_name,
                "description": tool_info.get('description', '无描述'),
                "async": tool_info.get('is_async', False)
            })
        
        log_message(f"找到 {len(tool_list)} 个工具")
        
        return {
            "success": True,
            "tools_found": len(tool_list),
            "tools": tool_list
        }
        
    except Exception as e:
        log_message(f"测试MCP工具失败: {str(e)}", "ERROR")
        return {
            "success": False,
            "error": str(e)
        }

def start_mcp_server_in_background():
    """在后台启动MCP服务器"""
    log_message("尝试在后台启动MCP服务器")
    
    # 启动收集器MCP服务器
    server_script = PROJECT_ROOT / "tools" / "collector" / "mcp_server.py"
    
    if not server_script.exists():
        log_message(f"服务器脚本不存在: {server_script}", "ERROR")
        return None
    
    try:
        # 启动服务器进程
        cmd = [sys.executable, str(server_script)]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # 等待一段时间让服务器启动
        time.sleep(3)
        
        # 检查进程是否还在运行
        if process.poll() is None:
            log_message(f"MCP服务器已启动，PID: {process.pid}")
            return process
        else:
            # 读取错误输出
            stdout, stderr = process.communicate()
            log_message(f"服务器启动失败，返回码: {process.returncode}", "ERROR")
            log_message(f"标准输出: {stdout[:500]}", "DEBUG")
            log_message(f"错误输出: {stderr[:500]}", "DEBUG")
            return None
            
    except Exception as e:
        log_message(f"启动MCP服务器时发生异常: {str(e)}", "ERROR")
        return None

def test_server_connection(port=8112):
    """测试服务器连接"""
