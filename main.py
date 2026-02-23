import asyncio
import os
import yaml
import argparse
import config.globs as globs
from config.globs import load_config_from_yaml
from tools.builder.proj_builder import build_proj_dbgen, clear_proj
from agents.analyzer_agent import analyze_functions
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from tools.replacer.code_replacer import function_replace
from tools.replacer.code_recover import function_recover
from tools.emulator.conf_generator import generate_emulator_configs
from utils.src_ops import src_replace


def clean_function_logs(func_name: str, log_type: str = "all"):
    """删除指定函数的分析日志
    
    Args:
        func_name: 函数名
        log_type: 日志类型 - "replacement", "analysis", "all"
    """
    log_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
    if not os.path.exists(log_dir):
        print(f"日志目录不存在: {log_dir}")
        return
    
    deleted_files = []
    
    if log_type in ["replacement", "all"]:
        for f in os.listdir(log_dir):
            if f.startswith(f"replacement_update_{func_name}_") and f.endswith(".json"):
                file_path = os.path.join(log_dir, f)
                os.remove(file_path)
                deleted_files.append(file_path)
                print(f"删除: {f}")
    
    if log_type in ["analysis", "all"]:
        for f in os.listdir(log_dir):
            if f.startswith(f"function_analysis_{func_name}_") and f.endswith(".json"):
                file_path = os.path.join(log_dir, f)
                os.remove(file_path)
                deleted_files.append(file_path)
                print(f"删除: {f}")
    
    if not deleted_files:
        print(f"未找到 {func_name} 的日志文件")
    else:
        print(f"\n共删除 {len(deleted_files)} 个文件")


async def run_workflow():
    config = load_config_from_yaml(globs.script_path)
    
    globs.globs_init(config)
    
    build_proj_dbgen(globs.script_path, globs.db_path)
    register_db(globs.db_path)
    from tools.builder.core import init_builder
    await init_builder()
    from tools.builder.core import build_project
    build_output = build_project()
    print(f"Build project output: {build_output}")
    generate_emulator_configs()
    from agents.emulator_runner_agent import run_emulator
    emulate_output = await run_emulator()
    print(f"Emulate output: {emulate_output}")


async def recover_workflow():
    from tools.replacer.code_recover import recover_code_file
    import utils.db_file as db_file
    
    if not globs.script_path:
        print("Error: script_path not provided")
        return
    
    config = load_config_from_yaml(globs.script_path)
    globs.globs_init(config)
    
    print(f"Recovering source files from DB: {globs.db_path}")
    print(f"Source path: {globs.src_path}")
    
    db_files = db_file.list_files_in_db_zip(globs.db_path)
    print(f"Found {len(db_files)} files in DB")
    
    success_count = 0
    fail_count = 0
    for code_path in db_files:
        if recover_code_file(code_path):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"Recovery completed: {success_count} success, {fail_count} failed")


async def main():
    parser = argparse.ArgumentParser(description="LCMHAL MCP Tool")
    parser.add_argument("command", choices=["run", "recover", "clean"], help="Command to execute: run, recover, or clean")
    parser.add_argument("script_path", nargs="?", default="", help="Path to the script/config file")
    parser.add_argument("--config", "-c", default=None, help="Path to config YAML file (overrides script_path)")
    parser.add_argument("--func-name", "-f", default=None, help="Function name to clean logs for (used with 'clean' command)")
    parser.add_argument("--type", "-t", choices=["replacement", "analysis", "all"], default="all", help="Log type to clean (used with 'clean' command)")
    
    args = parser.parse_args()
    
    if args.command == "clean":
        if args.config:
            config_path = args.config
        elif args.script_path:
            config_path = args.script_path
        else:
            print("Error: config file path required for clean command")
            return
        
        # load_config_from_yaml 期望目录路径
        if os.path.isfile(config_path):
            dir_path = os.path.dirname(config_path)
        else:
            dir_path = config_path
        
        config = load_config_from_yaml(dir_path)
        globs.script_path = dir_path
        globs.globs_init(config)
        
        if not args.func_name:
            print("Error: --func-name is required for clean command")
            return
        
        clean_function_logs(args.func_name, args.type)
        return
    
    if args.command == "recover":
        if args.config:
            globs.script_path = args.config
        elif args.script_path:
            globs.script_path = args.script_path
        else:
            print("Error: config file path required for recover command")
            return
        await recover_workflow()
    else:
        # 处理 script_path：如果是配置文件路径，提取目录
        if args.script_path:
            potential_path = args.script_path
        elif args.config:
            potential_path = args.config
        else:
            potential_path = globs.default_config["script_path"]
        
        # 如果传入的是配置文件路径，提取其所在目录
        if os.path.isfile(potential_path):
            globs.script_path = os.path.dirname(potential_path)
        else:
            globs.script_path = potential_path
        
        await run_workflow()


if __name__ == "__main__":
    asyncio.run(main())
