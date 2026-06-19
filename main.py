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


async def run_build_workflow():
    """仅执行构建：init_builder（加载 MMIO 并分析）→ replace_funcs → 编译 → 生成 emulate 配置。不接入 Builder 智能体。"""
    config = load_config_from_yaml(globs.script_path)
    globs.globs_init(config)
    print(f"[build] script_path={globs.script_path}, db_path={globs.db_path}", file=sys.stderr)

    build_proj_dbgen(globs.script_path, globs.db_path)
    register_db(globs.db_path)
    from tools.builder.core import init_builder, build_project
    await init_builder()
    build_output = build_project()
    print(f"Build project output: {build_output}")
    if build_output.get("exit_code", 0) == 0:
        generate_emulator_configs()
    return build_output


async def run_workflow():
    config = load_config_from_yaml(globs.script_path)
    if not isinstance(config, dict):
        config = {}
    # main.py「run」分支可能在 globs_init 后设置了 llm_usage_log_enable；YAML 重载时保留该开关
    if getattr(globs, "llm_usage_log_enable", False):
        config["llm_usage_log_enable"] = True
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
        choices=[
            "run",
            "build",
            "emulate",
            "recover",
            "clean",
            "analyze",
            "dump-replacements",
            "classify-stats",
        ],
        help="Command to execute: run, build, emulate, recover, clean, analyze, dump-replacements, or classify-stats",
    )
    parser.add_argument(
        "script_path",
        nargs="?",
        default="",
        help="Path to testcase dir, lcmhal_config.yml, or (for classify-stats) a root dir to scan recursively",
    )
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
    parser.add_argument(
        "--log-file",
        default=None,
        help="For 'dump-replacements' command: output log filename (default: replacement_log.md in testcase config directory)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="For 'classify-stats': print machine-readable JSON only (no human-readable tables)",
    )
    parser.add_argument(
        "--no-lists",
        action="store_true",
        help="For 'classify-stats': only print counts per type (and per-type has_replacement split), omit per-function lists",
    )
    parser.add_argument(
        "--no-batch-summary",
        action="store_true",
        help="For 'classify-stats' batch mode: omit merged totals across all testcases",
    )
    # 毕设/消融：仅 analyze 在加载 lcmhal_config 后会合并进 config（见 analyze 分支）
    parser.add_argument(
        "--experiment-mode",
        choices=["full", "no_feedback"],
        default=None,
        help="Override experiment_mode: no_feedback disables VerifyReplacement/Fixer (analyze only)",
    )
    parser.add_argument(
        "--tool-profile",
        choices=["full", "minimal"],
        default=None,
        help="Override tool_profile: minimal keeps only GetFunctionInfo (analyze only)",
    )
    parser.add_argument(
        "--analyzer-recursion-limit",
        type=int,
        default=None,
        metavar="N",
        help="Override LangGraph recursion_limit for classifier (analyze only)",
    )
    parser.add_argument(
        "--llm-usage-log",
        action="store_true",
        help="Enable LLM usage+timing records in session JSON under lcmhal_ai_log (analyze only)",
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

    if args.command == "dump-replacements":
        # 解析配置路径（与 clean 命令类似）
        if args.config:
            config_path = args.config
        elif args.script_path:
            config_path = args.script_path
        else:
            print("Error: config file path required for dump-replacements command")
            return

        # load_config_from_yaml 期望目录路径
        if os.path.isfile(config_path):
            dir_path = os.path.dirname(config_path)
        else:
            dir_path = config_path

        config = load_config_from_yaml(dir_path)
        globs.script_path = dir_path
        globs.globs_init(config)

        # 加载 MMIO/替换信息（含历史），以便复用 data_manager 的格式化接口
        from core.data_manager import data_manager
        from tools.collector.collector import (
            get_mmio_func_list,
            get_mmio_func_list_interesting_mmioexpr,
        )

        await data_manager.load_mmio_functions()
        all_mmio_func_names = get_mmio_func_list(globs.db_path)
        interesting_mmioexpr_names = get_mmio_func_list_interesting_mmioexpr(globs.db_path)

        # 构造输出文件路径：默认在配置目录下的 replacement_log.md
        if args.log_file:
            log_filename = args.log_file
        else:
            log_filename = "replacement_log.md"
        if not os.path.isabs(log_filename):
            log_path = os.path.join(dir_path, log_filename)
        else:
            log_path = log_filename

        lines = []
        # 顶部信息（Markdown 标题）
        lines.append("## LCMHAL 函数替换日志")
        lines.append("")
        lines.append(f"- **Testcase 路径**: `{dir_path}`")
        lines.append("")

        # 收集所有“实际发生过替换”的函数名：
        # 1) 有 ReplacementUpdate 历史的
        # 2) 有当前 ReplacementUpdate 的
        # 3) FunctionClassifier 判定 has_replacement=True 的（即使从未有过 ReplacementUpdate）
        replacement_history = getattr(data_manager, "replacement_history", {}) or {}
        replacement_updates = getattr(data_manager, "replacement_updates", {}) or {}
        mmio_info_list = data_manager.get_mmio_info_list() or {}

        func_names = set(replacement_history.keys()) | set(replacement_updates.keys())
        for fn, info in mmio_info_list.items():
            try:
                if getattr(info, "has_replacement", False):
                    func_names.add(fn)
            except Exception:
                continue
        func_names = sorted(func_names)

        if not func_names:
            lines.append(
                "当前 testcase **没有**可写入下方「替换章节」的条目：无 `replacement_update_*.json`，"
                "且 FunctionClassifier 对 MMIO 函数的 **`has_replacement` 均为 false** 时，也不会出现在替换总览里。"
            )
            lines.append("")
        else:
            # 第一章：总览表
            lines.append("## 1. 替换函数总览")
            lines.append("")
            lines.append("| 函数名 | 文件路径 | 行号 | 替换次数 |")
            lines.append("|--------|----------|------|----------|")
            for func_name in func_names:
                info = data_manager.get_function_analysis_and_replacement(func_name)
                func_info = info.get("function_info", {}) or {}
                file_path = func_info.get("file_path", "未知")
                location_line = func_info.get("location_line", "未知")
                history_list = replacement_history.get(func_name, [])
                # 估算“替换次数”：有历史则用历史长度，否则如果存在当前 ReplacementUpdate 或 has_replacement，则视为 1
                if history_list:
                    replace_count = len(history_list)
                else:
                    if func_name in replacement_updates:
                        replace_count = 1
                    else:
                        mi = mmio_info_list.get(func_name)
                        replace_count = 1 if (mi and getattr(mi, "has_replacement", False)) else 0
                lines.append(f"| `{func_name}` | `{file_path}` | {location_line} | {replace_count} |")

            # 第二章：按函数详细展示（Markdown 小节 + 文本块）
            lines.append("")
            lines.append("## 2. 各函数替换详情")
            lines.append("")
            for func_name in func_names:
                lines.append(f"### {func_name}")
                lines.append("")
                formatted = data_manager.get_function_analysis_and_replacement_formatted_by_function(func_name)
                lines.append("```text")
                lines.append(formatted)
                lines.append("```")
                lines.append("")

        # FunctionClassifier：与 get_mmio_func_list() 一致（CodeQL MMIOFunction 全集）
        n_all = len(all_mmio_func_names)
        n_classified = len(mmio_info_list)
        n_interesting = len(interesting_mmioexpr_names)
        if mmio_info_list:
            lines.append(
                f"## FunctionClassifier 汇总（已跑 classify：**{n_classified}** 个；CodeQL `MMIOFunction`：**{n_all}** 个）"
            )
            lines.append("")
            lines.append(
                "说明：`load_mmio_functions()` 对 **`get_mmio_func_list()`** 中的全部函数调用 `function_classify`（与 "
                "`info_mmio_function_collector.ql` / **`MMIOFunction`** 一致，凡含 MMIO 操作均纳入）。"
                f"较窄的 **interesting MMIO expr** 子集（`get_mmio_func_list_interesting_mmioexpr()`）本 DB 共 **{n_interesting}** 个，仅作对比，见文末附录。"
                "下表为已缓存的 classify；**「替换」章节**仍仅含 `replacement_update_*` 或 `has_replacement=true`。"
            )
            lines.append("")
            lines.append("| 函数名 | function_type | has_replacement | 简述 |")
            lines.append("|--------|---------------|-----------------|------|")

            def _md_cell(s: str, max_len: int = 120) -> str:
                if not s:
                    return ""
                one = " ".join(s.split())
                if len(one) > max_len:
                    one = one[: max_len - 3] + "..."
                return one.replace("|", "\\|")

            for fn in sorted(mmio_info_list.keys()):
                info = mmio_info_list.get(fn)
                if info is None:
                    continue
                try:
                    ftype = getattr(info, "function_type", "") or ""
                    has_rep = getattr(info, "has_replacement", False)
                    blurb = getattr(info, "functionality", "") or getattr(info, "classification_reason", "") or ""
                    lines.append(
                        f"| `{fn}` | {ftype} | {has_rep} | {_md_cell(blurb)} |"
                    )
                except Exception:
                    lines.append(f"| `{fn}` | (error) | | |")

            lines.append("")

        if interesting_mmioexpr_names and n_interesting < n_all:
            lines.append(
                f"## 附录：interesting MMIO expr 子集（共 {n_interesting} 个，较 `get_mmio_func_list()` 更窄）"
            )
            lines.append("")
            lines.append(
                "来自 `mmioinfo_mmioexpr_collector.ql`（`isInterestingMMIOFunction` + `MMIOTracedExpr`）。"
                "Classifier 已改为覆盖 **全部** `MMIOFunction`，本附录仅便于对照旧口径。"
            )
            lines.append("")
            for name in sorted(interesting_mmioexpr_names):
                lines.append(f"- `{name}`")
            lines.append("")

        try:
            with open(log_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            print(f"Replacement log written to: {log_path}")
        except Exception as e:
            print(f"Error writing replacement log to {log_path}: {e}")
        return

    if args.command == "classify-stats":
        if args.config:
            user_path = args.config
        elif args.script_path:
            user_path = args.script_path
        else:
            print("Error: testcase 目录、根目录或 lcmhal_config.yml 路径必填（classify-stats 需定位 db_path）")
            print("  单例: python main.py classify-stats testcases/server/nxp/NXP_UART_BareMetal")
            print("  批量: python main.py classify-stats testcases/server/nxp   # 递归子目录中含 lcmhal_config.yml 的均统计")
            return

        from utils.classify_log_stats import (
            aggregate_classify_stats,
            format_classify_stats_text,
            summarize_batch_counts,
            summarize_batch_unique_by_function_name,
            summarize_batch_unique_replacement_updates,
        )
        from utils.lcmhal_testcase_scan import read_db_path_from_testcase_dir, resolve_classify_stats_targets

        def _write_auto_stats_file(testcase_dir: str, stats_obj: dict):
            """自动将完整 classify 统计写入 testcase 目录，便于后续复用。"""
            out_path = os.path.join(testcase_dir, "classify_stats_output.json")
            try:
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(stats_obj, f, ensure_ascii=False, indent=2)
                print(f"[classify-stats] auto output written: {out_path}")
            except Exception as e:
                print(f"[classify-stats] auto output write failed: {out_path}, err={e}")

        def _demo_alias_from_relpath(rel_path: str) -> str:
            """给 demo 生成稳定短名：最后两级目录 + 简短哈希后缀，避免重名。"""
            import hashlib
            parts = [p for p in rel_path.replace("\\", "/").split("/") if p]
            tail = parts[-2:] if len(parts) >= 2 else parts
            base = "-".join(tail) if tail else "demo"
            digest = hashlib.md5(rel_path.encode("utf-8")).hexdigest()[:6]
            return f"{base}-{digest}"

        def _write_batch_markdown_summary(scan_root_dir: str, results: list):
            """批量模式：在根目录输出 markdown 汇总表（每 demo 各类型计数 + 总计行）。"""
            # 只统计配置正常、且有 stats 的条目
            valid = [r for r in results if not r.get("config_error") and isinstance(r.get("stats"), dict)]
            if not valid:
                return

            # 收集所有类型列（按字母序，PARSE_ERROR 放最后）
            all_types = set()
            for r in valid:
                counts = (r["stats"].get("counts") or {})
                all_types.update(counts.keys())
            all_types = sorted([t for t in all_types if t != "PARSE_ERROR"])
            if "PARSE_ERROR" in {k for r in valid for k in (r["stats"].get("counts") or {}).keys()}:
                all_types.append("PARSE_ERROR")

            md_path = os.path.join(scan_root_dir, "classify_stats_summary.md")
            lines = []
            lines.append("# Classify Stats Batch Summary")
            lines.append("")
            lines.append(f"- Scan root: `{scan_root_dir}`")
            lines.append(f"- Testcase count: **{len(valid)}**")
            lines.append("")

            header = ["DemoPath", "DemoName"] + all_types + ["RepUpd", "TOTAL"]
            sep = ["---"] * len(header)
            lines.append("| " + " | ".join(header) + " |")
            lines.append("| " + " | ".join(sep) + " |")

            totals_by_type = {t: 0 for t in all_types}
            grand_total = 0
            grand_rep_upd = 0
            root_abs = os.path.abspath(scan_root_dir)

            for r in sorted(valid, key=lambda x: x.get("testcase_dir", "")):
                td = os.path.abspath(r["testcase_dir"])
                rel = os.path.relpath(td, root_abs)
                alias = _demo_alias_from_relpath(rel)
                counts = r["stats"].get("counts") or {}
                row_total = 0
                row_cells = [f"`{rel}`", f"`{alias}`"]
                for t in all_types:
                    v = int(counts.get(t, 0) or 0)
                    row_cells.append(str(v))
                    row_total += v
                    totals_by_type[t] += v
                rep_n = int(r["stats"].get("replacement_update_count") or 0)
                row_cells.append(str(rep_n))
                grand_rep_upd += rep_n
                row_cells.append(str(row_total))
                grand_total += row_total
                lines.append("| " + " | ".join(row_cells) + " |")

            total_row = (
                ["**TOTAL**", "-"]
                + [str(totals_by_type[t]) for t in all_types]
                + [str(grand_rep_upd), str(grand_total)]
            )
            lines.append("| " + " | ".join(total_row) + " |")
            lines.append("")

            try:
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(lines))
                print(f"[classify-stats] batch markdown summary written: {md_path}")
            except Exception as e:
                print(f"[classify-stats] batch markdown summary write failed: {md_path}, err={e}")

        testcase_dirs, mode = resolve_classify_stats_targets(user_path)
        if mode == "invalid":
            print(f"Error: 路径不存在或不是目录/文件: {user_path}")
            return
        if not testcase_dirs:
            scanned = os.path.abspath(user_path) if not os.path.isfile(user_path) else os.path.dirname(os.path.abspath(user_path))
            print(f"Error: 未找到任何 lcmhal_config.yml（已扫描: {scanned}）")
            return

        scan_root = os.path.abspath(user_path if os.path.isdir(user_path) else os.path.dirname(os.path.abspath(user_path)))

        batch_results: list = []
        for td in testcase_dirs:
            db_path, err = read_db_path_from_testcase_dir(td)
            entry = {"testcase_dir": os.path.abspath(td), "db_path": db_path, "config_error": err}
            if err:
                entry["stats"] = {
                    "log_dir": "",
                    "by_type": {},
                    "counts": {},
                    "by_type_has_replacement": {},
                    "counts_has_replacement": {},
                    "per_function": {},
                    "parse_errors": [],
                    "total_functions": 0,
                    "replacement_update_count": 0,
                    "replacement_update_functions": [],
                    "replacement_update_by_function": {},
                    "replacement_update_only_functions": [],
                    "replacement_update_parse_errors": [],
                    "error": err,
                }
            else:
                log_dir = os.path.join(db_path, "lcmhal_ai_log")
                st = aggregate_classify_stats(log_dir)
                st["testcase_dir"] = os.path.abspath(td)
                entry["stats"] = st
            batch_results.append(entry)

        # 单 testcase
        if len(testcase_dirs) == 1:
            stats = batch_results[0]["stats"]
            # 无论终端显示模式如何，自动落一份“完整统计”到 testcase 目录：
            # 包含计数、每函数列表、has_replacement 拆分等。
            _write_auto_stats_file(batch_results[0]["testcase_dir"], stats)
            if args.no_lists:
                slim = {
                    "testcase_dir": stats.get("testcase_dir"),
                    "log_dir": stats.get("log_dir"),
                    "total_functions": stats.get("total_functions"),
                    "replacement_update_count": stats.get("replacement_update_count"),
                    "replacement_update_functions": stats.get("replacement_update_functions"),
                    "counts": stats.get("counts"),
                    "counts_has_replacement": stats.get("counts_has_replacement"),
                    "error": stats.get("error"),
                }
                if args.json:
                    print(json.dumps(slim, ensure_ascii=False, indent=2))
                else:
                    print(format_classify_stats_text(stats, include_lists=False))
            elif args.json:
                print(json.dumps(stats, ensure_ascii=False, indent=2))
            else:
                print(format_classify_stats_text(stats, include_lists=True))
            return

        # 批量
        summary_src = [br["stats"] for br in batch_results if not br.get("config_error")]
        summary = summarize_batch_counts(summary_src) if summary_src else {
            "summary_counts": {},
            "summary_counts_has_replacement": {},
            "summary_total_functions": 0,
            "summary_total_replacement_update_functions": 0,
        }
        summary_unique = summarize_batch_unique_by_function_name(summary_src) if summary_src else {
            "summary_unique_counts": {},
            "summary_unique_counts_has_replacement": {},
            "summary_unique_total_functions": 0,
        }
        summary_unique_rep = summarize_batch_unique_replacement_updates(summary_src) if summary_src else {
            "summary_unique_replacement_update_count": 0,
            "summary_unique_replacement_update_functions": [],
        }

        if args.json:
            out = {
                "scan_root": scan_root,
                "mode": "batch",
                "testcase_count": len(batch_results),
                **summary,
                **summary_unique,
                **summary_unique_rep,
                "testcases": batch_results,
            }
            if args.no_batch_summary:
                out.pop("summary_counts", None)
                out.pop("summary_counts_has_replacement", None)
                out.pop("summary_total_functions", None)
                out.pop("summary_total_replacement_update_functions", None)
                out.pop("summary_unique_counts", None)
                out.pop("summary_unique_counts_has_replacement", None)
                out.pop("summary_unique_total_functions", None)
                out.pop("summary_unique_replacement_update_count", None)
                out.pop("summary_unique_replacement_update_functions", None)
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return

        print(f"批量 classify-stats: 扫描根目录 {scan_root}")
        print(f"共 {len(batch_results)} 个 testcase（含 lcmhal_config.yml）\n")
        if not args.no_batch_summary and summary.get("summary_counts"):
            print("=== 汇总（全部 testcase 计数相加，未去重）===")
            print(f"  总函数条目数: {summary.get('summary_total_functions', 0)}")
            print(
                f"  ReplacementUpdate 函数数（各 demo 相加，未去重）: "
                f"{summary.get('summary_total_replacement_update_functions', 0)}"
            )
            for t, n in (summary.get("summary_counts") or {}).items():
                rep = (summary.get("summary_counts_has_replacement") or {}).get(t) or {}
                if t == "PARSE_ERROR":
                    print(f"  {t}: {n}")
                else:
                    print(f"  {t}: {n} (has_replacement=true: {rep.get('true', 0)}, false: {rep.get('false', 0)})")
            print("")

            if summary_unique.get("summary_unique_counts"):
                print("=== 汇总（按函数名去重）===")
                print(f"  去重后函数数: {summary_unique.get('summary_unique_total_functions', 0)}")
                for t, n in (summary_unique.get("summary_unique_counts") or {}).items():
                    rep = (summary_unique.get("summary_unique_counts_has_replacement") or {}).get(t) or {}
                    print(f"  {t}: {n} (has_replacement=true: {rep.get('true', 0)}, false: {rep.get('false', 0)})")
                print("")

            if summary_unique_rep.get("summary_unique_replacement_update_count", 0) or summary_unique_rep.get(
                "summary_unique_replacement_update_functions"
            ):
                print("=== ReplacementUpdate（跨 demo 按函数名去重）===")
                print(
                    f"  去重后函数数: {summary_unique_rep.get('summary_unique_replacement_update_count', 0)}"
                )
                names = summary_unique_rep.get("summary_unique_replacement_update_functions") or []
                if names:
                    print("  函数列表:")
                    for fn in names:
                        print(f"    - {fn}")
                print("")

        for br in batch_results:
            td = br["testcase_dir"]
            # 批量模式下也给每个 testcase 自动落一份完整统计
            _write_auto_stats_file(td, br["stats"])
            print("=" * 60)
            print(f"Testcase: {td}")
            if br.get("config_error"):
                print(f"  [跳过] 配置错误: {br['config_error']}")
                continue
            st = br["stats"]
            if args.no_lists:
                print(f"  日志目录: {st.get('log_dir')}")
                if st.get("error"):
                    print(f"  错误: {st['error']}")
                else:
                    print(f"  已统计函数数: {st.get('total_functions', 0)}")
                    print(
                        f"  ReplacementUpdate 函数数: {int(st.get('replacement_update_count') or 0)}"
                    )
                    for t, n in sorted((st.get('counts') or {}).items(), key=lambda x: (-x[1], x[0])):
                        if t == "PARSE_ERROR":
                            print(f"    {t}: {n}")
                            continue
                        rep = (st.get("counts_has_replacement") or {}).get(t) or {}
                        print(f"    {t}: {n} (true: {rep.get('true', 0)}, false: {rep.get('false', 0)})")
            else:
                block = format_classify_stats_text(st, include_lists=True)
                for line in block.splitlines():
                    print(f"  {line}" if line else "")
            print("")

        # 批量模式结束后，在扫描根目录输出一份总览 Markdown
        _write_batch_markdown_summary(scan_root, batch_results)
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
        if not isinstance(config, dict):
            config = {}
        if args.experiment_mode is not None:
            config["experiment_mode"] = args.experiment_mode
        if args.tool_profile is not None:
            config["tool_profile"] = args.tool_profile
        if args.analyzer_recursion_limit is not None:
            config["analyzer_recursion_limit"] = args.analyzer_recursion_limit
        if args.llm_usage_log:
            config["llm_usage_log_enable"] = True
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
    elif args.command == "build":
        # build：仅构建（init_builder + replace + 编译 + 生成 emulate 配置）
        if args.script_path:
            potential_path = args.script_path
        elif args.config:
            potential_path = args.config
        else:
            print("Error: build 命令必须指定 testcase 目录（包含 lcmhal_config.yml）。")
            print("  示例: python main.py build testcases/server/stm32/UART_Hyperterminal_IT")
            return
        if os.path.isfile(potential_path):
            globs.script_path = os.path.dirname(potential_path)
        else:
            globs.script_path = potential_path
        await run_build_workflow()

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

        config = load_config_from_yaml(globs.script_path)
        if not isinstance(config, dict):
            config = {}
        if args.llm_usage_log:
            config["llm_usage_log_enable"] = True
        globs.globs_init(config)

        await run_workflow()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        try:
            from config import globs as _globs

            _globs.finalize_session()
        except Exception as _e:
            print(f"[WARN] finalize_session failed: {_e}")
