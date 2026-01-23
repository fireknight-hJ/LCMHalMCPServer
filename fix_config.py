#!/usr/bin/env python3
"""
修正配置脚本：解决'Missing required config key 'N/A' for 'tools''错误
"""
import os
import sys
import shutil
from pathlib import Path

def create_backup(file_path, backup_dir):
    """创建文件备份"""
    if not os.path.exists(file_path):
        print(f"警告: 文件不存在: {file_path}")
        return False
    
    file_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, file_name)
    
    try:
        shutil.copy2(file_path, backup_path)
        print(f"已创建备份: {file_path} -> {backup_path}")
        return True
    except Exception as e:
        print(f"备份失败 {file_path}: {e}")
        return False

def fix_globs_module():
    """修正globs模块配置"""
    globs_path = "config/globs.py"
    backup_dir = "backup_20260122_150735"
    
    # 创建备份
    if not create_backup(globs_path, backup_dir):
        return False
    
    # 读取文件内容
    with open(globs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否需要修正
    if 'db_path = "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/codeql_db"' in content:
        print("globs模块配置看起来正确")
        return True
    
    # 修正配置
    new_content = content.replace(
        'db_path = "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/codeql_db" # mac',
        'db_path = "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/codeql_db"'
    )
    
    # 确保默认配置正确
    if 'default_config = {' in new_content:
        # 更新默认配置
        default_config_start = new_content.find('default_config = {')
        if default_config_start != -1:
            # 查找默认配置结束
            brace_count = 0
            i = default_config_start
            while i < len(new_content):
                if new_content[i] == '{':
                    brace_count += 1
                elif new_content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        break
                i += 1
            
            default_config_end = i + 1
            default_config = new_content[default_config_start:default_config_end]
            
            # 检查默认配置是否正确
            if '"db_path": "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/codeql_db"' not in default_config:
                # 修正默认配置
                new_default_config = '''default_config = {
    "script_path": "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver",
    "db_path": "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/codeql_db",
    "src_path": "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver/src",
    "proj_path": "/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver"
}'''
                new_content = new_content[:default_config_start] + new_default_config + new_content[default_config_end:]
    
    # 写入修正后的内容
    with open(globs_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("已修正globs模块配置")
    return True

def fix_mcp_server_config():
    """修正MCP服务器配置"""
    mcp_server_path = "tools/collector/mcp_server.py"
    backup_dir = "backup_20260122_150735"
    
    # 创建备份
    if not create_backup(mcp_server_path, backup_dir):
        return False
    
    # 读取文件内容
    with open(mcp_server_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否需要修正
    if 'globs.db_path = args.db_path' in content:
        print("MCP服务器配置看起来正确")
        return True
    
    # 确保globs在解析参数后立即设置
    if 'def parse_args():' in content and 'if __name__ == "__main__":' in content:
        # 查找main部分
        main_start = content.find('if __name__ == "__main__":')
        if main_start != -1:
            # 在main部分添加globs初始化
            main_content = content[main_start:]
            
            # 检查是否已经有globs初始化
            if 'globs.db_path = args.db_path' not in main_content:
                # 在解析参数后添加globs初始化
                args_parse = 'args = parse_args()'
                args_pos = main_content.find(args_parse)
                if args_pos != -1:
                    insert_pos = args_pos + len(args_parse)
                    new_main_content = main_content[:insert_pos] + '\n    globs.db_path = args.db_path' + main_content[insert_pos:]
                    
                    # 更新整个内容
                    new_content = content[:main_start] + new_main_content
                    
                    # 写入修正后的内容
                    with open(mcp_server_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print("已修正MCP服务器配置")
                    return True
    
    return False

def test_fix():
    """测试修正是否有效"""
    print("\n测试修正...")
    
    # 导入globs模块测试
    try:
        import config.globs as globs
        from config.globs import globs_init, load_config_from_yaml
        
        # 初始化globs
        script_path = '/home/chenkaiqiu/LCMHalMCPServer/testcases/uart_driver'
        config_data = load_config_from_yaml(script_path)
        globs_init(config_data)
        
        print(f"globs配置测试:")
        print(f"  db_path: {globs.db_path}")
        print(f"  script_path: {globs.script_path}")
        
        if globs.db_path and globs.db_path != 'N/A':
            print("✓ globs配置正确")
            return True
        else:
            print("✗ globs配置不正确")
            return False
            
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False

def main():
    """主函数"""
    print("开始修正配置...")
    
    # 创建备份目录
    backup_dir = "backup_20260122_150735"
    os.makedirs(backup_dir, exist_ok=True)
    
    # 修正globs模块
    print("\n1. 修正globs模块...")
    if not fix_globs_module():
        print("警告: globs模块修正可能失败")
    
    # 修正MCP服务器配置
    print("\n2. 修正MCP服务器配置...")
    if not fix_mcp_server_config():
        print("警告: MCP服务器配置修正可能失败")
    
    # 测试修正
    print("\n3. 测试修正...")
    if test_fix():
        print("\n✓ 修正成功!")
        
        # 运行测试脚本
        print("\n4. 运行测试脚本...")
        test_script = "test_fix.py"
        if os.path.exists(test_script):
            print(f"运行测试脚本: {test_script}")
            os.system(f"cd /home/chenkaiqiu/LCMHalMCPServer && source .venv/bin/activate && python {test_script}")
        else:
            print(f"测试脚本不存在: {test_script}")
    else:
        print("\n✗ 修正失败!")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
