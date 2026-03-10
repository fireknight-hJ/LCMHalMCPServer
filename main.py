import asyncio
import json
import os
import sys
import yaml
import argparse
import config.globs as globs
from config.globs import load_config_from_yaml
from tools.builder.proj_builder import build_proj_dbgen, clear_proj
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from tools.replacer.code_replacer import function_replace
from tools.replacer.code_recover import function_recover
from tools.emulator.conf_generator import generate_emulator_configs
from tools.emulator.core import get_fault_function_from_emulate_output
from utils.src_ops import src_replace


def clean_function_logs(func_name: str, log_type: str = "all"):
    """删除指定函数的分析日志，避免旧结果被加载并应用。

    - replacement: 删除 replacement_update_*.json（Fixer 的替换会参与 replace_funcs）
    - classify: 删除 function_classify_*.json（Classifier 结果会作为 mmio_info_list 被加载）
    - analysis: 删除 function_analysis_*.json
    - all: 上述三者都删。对 SystemInit 等 RTOS 关键初始化函数，建议用 all，再配合 --recover 恢复源码。

    Args:
        func_name: 函数名
        log_type: 日志类型 - "replacement", "classify", "analysis", "all"
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
    
    if log_type in ["classify", "all"]:
        for f in os.listdir(log_dir):
            if f.startswith(f"function_classify_{func_name}_") and f.endswith(".json"):
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


def clean_all_ai_log():
    """清空当前 db_path 下 lcmhal_ai_log 目录内全部文件（工具自带实现）。"""
    log_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
    if not os.path.exists(log_dir):
        print(f"日志目录不存在: {log_dir}")
        return
    deleted = 0
    for f in os.listdir(log_dir):
        path = os.path.join(log_dir, f)
        if os.path.isfile(path):
            os.remove(path)
            deleted += 1
            print(f"删除: {f}")
    print(f"\n共删除 {deleted} 个文件，ai_log 已清空")


async def run_workflow():
    config = load_config_from_yaml(globs.script_path)
    
    globs.globs_init(config)
    print(f"[run_workflow] script_path={globs.script_path}, db_path={globs.db_path}", file=sys.stderr)
    
    build_proj_dbgen(globs.script_path, globs.db_path)
    register_db(globs.db_path)
    from tools.builder.core import init_builder
    await init_builder()
    from tools.builder.core import build_project
    build_output = build_project()
    print(f"Build project output: {build_output}")
    # 若首次构建失败，交给 Builder Agent 递归修（含 update_function_replacement 修正签名等）
    if build_output.get("exit_code", 0) != 0:
        from agents.builder_agent import run_build_project
        print("[run_workflow] Build failed, invoking Builder Agent to fix recursively...")
        builder_result = await run_build_project()
        print(f"Builder Agent result: {builder_result}")
    generate_emulator_configs()
    from agents.emulator_runner_agent import run_emulator
    from agents.analyzer_agent import analyze_functions
    from core.data_manager import data_manager
    from tools.builder.core import replace_funcs, build_project as core_build_project

    emulate_output = await run_emulator()
    print(f"Emulate output: {emulate_output}")

    # 若模拟失败且存在 UNMAPPED/fault PC，则根据 function.txt/stdout 解析出 fault 函数，
    # 若该函数未在 mmio_info_list 中（未被分析/替换过），则对其做一次 analyze 并应用替换，再重新构建与模拟
    max_emulate_fault_rounds = 3
    for _ in range(max_emulate_fault_rounds):
        success = getattr(emulate_output, "success", None)
        if success is None and isinstance(emulate_output, dict):
            success = emulate_output.get("success", False)
        if success:
            break
        fault_func = get_fault_function_from_emulate_output()
        if not fault_func:
            print("[run_workflow] Emulate failed but no fault PC/fault function parsed, skip fault recovery.")
            break
        mmio_list = data_manager.get_mmio_info_list()
        if fault_func in mmio_list:
            print(f"[run_workflow] Fault function {fault_func} already in mmio_info_list, skip fault recovery.")
            break
        print(f"[run_workflow] Emulate fault at {fault_func}, analyzing and applying replacement then re-build/re-emulate...")
        try:
            result_map = await analyze_functions([fault_func])
            if result_map and fault_func in result_map and getattr(result_map[fault_func], "has_replacement", False):
                data_manager.mmio_info_list[fault_func] = result_map[fault_func]
                replace_funcs()
                build_output = core_build_project()
                if build_output.get("exit_code", 0) != 0:
                    print(f"[run_workflow] Re-build after fault fix failed, skip re-emulate.")
                    break
                generate_emulator_configs()
                emulate_output = await run_emulator()
                print(f"Emulate output (after fault fix): {emulate_output}")
            else:
                print(f"[run_workflow] No replacement for {fault_func}, skip fault recovery.")
                break
        except Exception as e:
            print(f"[run_workflow] Fault recovery failed: {e}")
            break


async def emulate_workflow():
    """仅运行模拟器（不做 CodeQL/替换/编译），直接调用 Emulator 相关工具跑 demo。

    前提：testcase 的 emulate/output.elf 和 emulate/output.bin 已存在且与当前源码匹配。
    """
    config = load_config_from_yaml(globs.script_path)
    globs.globs_init(config)
    print(f"[emulate] script_path={globs.script_path}, db_path={globs.db_path}", file=sys.stderr)

    from tools.emulator.core import emulate_proj
    ret = emulate_proj()
    print(f"Emulate output: {ret}")


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
    parser.add_argument(
        "command",
        choices=["run", "emulate", "recover", "clean", "analyze"],
        help="Command to execute: run, emulate, recover, clean, or analyze a single function",
    )
    parser.add_argument("script_path", nargs="?", default="", help="Path to the testcase directory or config file")
    parser.add_argument("--config", "-c", default=None, help="Path to config YAML file (overrides script_path)")
    parser.add_argument("--func-name", "-f", default=None, help="Function name (for 'clean' and 'analyze' commands)")
    parser.add_argument("--type", "-t", choices=["replacement", "analysis", "classify", "all"], default="all", help="Log type to clean (used with 'clean' command)")
    parser.add_argument("--recover", "-r", action="store_true", help="After cleaning, recover this function's source file from DB (used with 'clean -f FUNC')")
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="For 'analyze' command: do not delete existing logs; reuse previous analysis if present",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="For 'clean' command: clean entire lcmhal_ai_log directory for this testcase (ignore --func-name)",
    )
    
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
        
        if getattr(args, "all", False):
            clean_all_ai_log()
        elif not args.func_name:
            print("Error: --func-name is required for clean command (or use --all to clean entire ai_log)")
            return
        else:
            clean_function_logs(args.func_name, args.type)
        if args.recover and args.func_name:
            func_info = get_function_info(globs.db_path, args.func_name)
            if func_info:
                if function_recover(func_info):
                    print(f"Recovered source file for {args.func_name} from DB: {func_info.file_path}")
                else:
                    print(f"Recover failed for {args.func_name}. If DB was built after replacement, restore the file from git, e.g. git checkout -- <file>")
            else:
                print(f"Function {args.func_name} not found in DB, skip recover.")
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
    elif args.command == "emulate":
        # run/emulate 都必须指定 testcase 目录，否则可能使用错误目录/DB
        if args.script_path:
            potential_path = args.script_path
        elif args.config:
            potential_path = args.config
        else:
            print("Error: emulate 命令必须指定 testcase 目录（包含 lcmhal_config.yml）。")
            print("  示例: python main.py emulate testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS")
            return

        if os.path.isfile(potential_path):
            globs.script_path = os.path.dirname(potential_path)
        else:
            globs.script_path = potential_path

        await emulate_workflow()
    elif args.command == "analyze":
        # 单函数重新分析：可选先清理该函数的日志，然后调用 Analyzer 对单个函数做 classify
        if not args.func_name:
            print("Error: analyze 命令需要指定 --func-name")
            return

        # 和 run 一样，需要明确 testcase 目录，以加载正确的 DB
        if args.script_path:
            potential_path = args.script_path
        elif args.config:
            potential_path = args.config
        else:
            print("Error: analyze 命令必须指定 testcase 目录（包含 lcmhal_config.yml）。")
            print("  示例: python main.py analyze testcases/server/nxp/NXP_UART_FreeRTOS -f LPUART_ReadNonBlocking")
            return

        # 如果传入的是配置文件路径，提取其所在目录
        if os.path.isfile(potential_path):
            globs.script_path = os.path.dirname(potential_path)
        else:
            globs.script_path = potential_path

        config = load_config_from_yaml(globs.script_path)
        globs.globs_init(config)
        register_db(globs.db_path)

        # 默认先清掉该函数相关的 AI 日志，确保是真正的“重新分析”；加 --no-clean 可保留旧日志
        if not args.no_clean:
            clean_function_logs(args.func_name, "all")

        # 仅对单个函数调用 Analyzer
        print(f"[analyze] script_path={globs.script_path}, db_path={globs.db_path}", file=sys.stderr)
        print(f"[analyze] analyzing function: {args.func_name}")
        from agents.analyzer_agent import analyze_functions
        result_map = await analyze_functions([args.func_name])
        res = result_map.get(args.func_name)
        if res is None:
            print(f"[analyze] No analysis result for function {args.func_name}")
        else:
            # 以 JSON 形式打印，便于后续对比/记录
            print(json.dumps(res.model_dump(), indent=2, ensure_ascii=False))
    else:
        # run 必须指定 testcase 目录，否则会用到错误 DB（如误用 StreamingServer 导致 F7/F4 混用）
        if args.script_path:
            potential_path = args.script_path
        elif args.config:
            potential_path = args.config
        else:
            print("Error: run 命令必须指定 testcase 目录（包含 lcmhal_config.yml），否则会使用错误 DB。")
            print("  示例: python main.py run testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS")
            return
        
        # 如果传入的是配置文件路径，提取其所在目录
        if os.path.isfile(potential_path):
            globs.script_path = os.path.dirname(potential_path)
        else:
            globs.script_path = potential_path
        
        await run_workflow()


if __name__ == "__main__":
    asyncio.run(main())
