#!/usr/bin/env python3
"""
扫描 ai_log 中的 function_classify 日志，检测是否因「审查机制」丢失替换函数。

审查机制：在 FunctionClassifier 的 respond 节点中，若既无 VerifyReplacement 通过、
又无 FixFunctionBuildErrors 成功，则会将模型输出的替换清空（has_replacement=False, function_replacement=""）。

用法:
  python scripts/check_classifier_dropped_replacements.py <lcmhal_ai_log 目录或 db_path>
  例如: python scripts/check_classifier_dropped_replacements.py /path/to/dbs_server/DATABASE_LwIP_HTTP_Server_Socket_RTOS
  若未传参则使用环境或当前目录下的 lcmhal_ai_log。
"""
import json
import os
import sys
import glob


def _messages_contain_replacement(messages: list) -> bool:
    """从 messages 中判断对话里是否曾出现过替换内容（模型产出过替换但可能被 respond 清空）。
    只检查 type 为 ai/AIMessage 的消息，避免误匹配 system prompt 中的字段名。
    """
    if not messages:
        return False
    for m in messages:
        if not isinstance(m, dict):
            continue
        msg_type = (m.get("type") or (m.get("id", [""])[-1] if isinstance(m.get("id"), list) else "") or "").lower()
        if "ai" not in msg_type:
            continue
        content = m.get("content") or m.get("data", {}).get("content") or ""
        if isinstance(content, str):
            # 模型输出中的 JSON 形式：必须出现 has_replacement 为 true 或 function_replacement 非空
            if '"has_replacement": true' in content or '"has_replacement":True' in content:
                return True
            if '"function_replacement": "' in content and '"function_replacement": ""' not in content:
                return True
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict) and "text" in part:
                    t = part.get("text", "")
                    if '"has_replacement": true' in t or '"function_replacement": "' in t:
                        return True
    return False


def scan_log_dir(log_dir: str) -> dict:
    """
    扫描 log_dir 下 function_classify_<func>_<ts>.json，返回统计与列表。
    """
    pattern = os.path.join(log_dir, "function_classify_*_*.json")
    files = glob.glob(pattern)
    # 按函数名去重，每个函数只保留最新一份
    by_func = {}
    for path in files:
        name = os.path.basename(path)
        # function_classify_HAL_XXX_20260310120000.json -> func = HAL_XXX, 最后一段是时间
        parts = name.replace(".json", "").split("_")
        if len(parts) < 3:
            continue
        # 最后一段是时间戳
        ts = parts[-1]
        func = "_".join(parts[2:-1])
        if func not in by_func or by_func[func][0] < ts:
            by_func[func] = (ts, path)

    no_replacement = []           # has_replacement 最终为 False
    dropped_by_audit = []          # 最终无替换，但 messages 里曾出现替换 → 可能因审查清空
    has_replacement_ok = []       # 最终有替换
    rubric_fail = []              # 有 replacement_check_reason（rubric 未通过但可能仍有替换）

    for func, (ts, path) in by_func.items():
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[WARN] 无法读取 {path}: {e}", file=sys.stderr)
            continue

        fr = data.get("final_response")
        if not fr:
            continue
        if isinstance(fr, dict):
            has_rep = fr.get("has_replacement", False)
            rep_code = (fr.get("function_replacement") or "").strip()
            reason = fr.get("replacement_check_reason")
        else:
            has_rep = getattr(fr, "has_replacement", False)
            rep_code = (getattr(fr, "function_replacement", None) or "").strip()
            reason = getattr(fr, "replacement_check_reason", None)

        if reason:
            rubric_fail.append((func, reason[:80]))

        if has_rep and rep_code:
            has_replacement_ok.append(func)
            continue

        no_replacement.append(func)
        messages = data.get("messages", [])
        if _messages_contain_replacement(messages):
            dropped_by_audit.append(func)

    return {
        "no_replacement": no_replacement,
        "dropped_by_audit": dropped_by_audit,
        "has_replacement_ok": has_replacement_ok,
        "rubric_fail": rubric_fail,
        "total_classified": len(by_func),
    }


def main():
    if len(sys.argv) >= 2:
        arg = sys.argv[1]
        if os.path.isdir(arg):
            log_dir = os.path.join(arg, "lcmhal_ai_log") if "lcmhal_ai_log" not in arg else arg
        else:
            log_dir = os.path.join(arg, "lcmhal_ai_log")
    else:
        log_dir = os.path.join(os.getcwd(), "lcmhal_ai_log")
        # 常见 db 路径
        for base in [os.environ.get("LCMHAL_DB_PATH"), "/home/haojie/workspace/dbs_server"]:
            if base:
                d = os.path.join(base, "DATABASE_LwIP_HTTP_Server_Socket_RTOS", "lcmhal_ai_log")
                if os.path.isdir(d):
                    log_dir = d
                    break

    if not os.path.isdir(log_dir):
        print(f"目录不存在: {log_dir}", file=sys.stderr)
        print("用法: python scripts/check_classifier_dropped_replacements.py <db_path 或 lcmhal_ai_log 路径>", file=sys.stderr)
        sys.exit(1)

    r = scan_log_dir(log_dir)
    print(f"扫描目录: {log_dir}")
    print(f"已分类函数数: {r['total_classified']}")
    print(f"最终有替换: {len(r['has_replacement_ok'])}")
    print(f"最终无替换: {len(r['no_replacement'])}")
    if r["dropped_by_audit"]:
        print(f"\n[可能因审查机制丢失替换] 共 {len(r['dropped_by_audit'])} 个（最终无替换但对话中曾出现替换内容）:")
        for fn in sorted(r["dropped_by_audit"]):
            print(f"  - {fn}")
    else:
        print("\n未发现明显因审查机制清空替换的条目（无替换的条目在对话中也未发现替换内容）。")
    if r["rubric_fail"]:
        print(f"\n[Rubric 未通过] 共 {len(r['rubric_fail'])} 个（仅记录原因，不一定被清空）:")
        for fn, reason in r["rubric_fail"][:20]:
            print(f"  - {fn}: {reason}...")
        if len(r["rubric_fail"]) > 20:
            print(f"  ... 共 {len(r['rubric_fail'])} 条")
    print()
    if r["no_replacement"] and not r["dropped_by_audit"]:
        print("提示: 若需确认「因审查丢失」，请重跑并在日志中查看 [FunctionClassifier] 未采纳未验证替换: <函数名> 的输出。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
