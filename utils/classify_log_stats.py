"""
从 lcmhal_ai_log 中扫描 function_classify 日志，按 FunctionClassifier 的 function_type 聚合统计。

- 不调用 LLM，不依赖 data_manager.load_mmio_functions
- 每个函数只取最新一条 function_classify_<func>_<ts>.json
"""

from __future__ import annotations

import glob
import json
import os
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

# 与 models.analyze_results.function_analyze.FunctionClassifyResponse 一致（旧日志中的 NEEDCHECK 会归并为 NODRIVER）
VALID_TYPES = frozenset(
    {"CORE", "RECV", "IRQ", "RETURNOK", "SKIP", "NODRIVER", "INIT", "LOOP"}
)


def _func_name_from_classify_basename(basename: str) -> Optional[str]:
    if not basename.startswith("function_classify_") or not basename.endswith(".json"):
        return None
    stem = basename[:-5]
    parts = stem.split("_")
    if len(parts) < 4:
        return None
    ts = parts[-1]
    if not ts.isdigit():
        return None
    return "_".join(parts[2:-1])


def latest_classify_log_paths(log_dir: str) -> Dict[str, str]:
    """每个函数名 -> 最新一条 function_classify 日志路径（按时间戳字符串，再按文件 mtime）。"""
    pattern = os.path.join(log_dir, "function_classify_*_*.json")
    by_func: Dict[str, Tuple[Tuple[str, float], str]] = {}
    for path in glob.glob(pattern):
        name = os.path.basename(path)
        func = _func_name_from_classify_basename(name)
        if not func:
            continue
        ts = name[:-5].split("_")[-1]
        mtime = os.path.getmtime(path)
        key = (ts, mtime)
        prev = by_func.get(func)
        if prev is None or prev[0] < key:
            by_func[func] = (key, path)
    return {fn: p for fn, (_, p) in by_func.items()}


def _read_final_response(path: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """返回 (final_response dict, 错误信息)。"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return None, str(e)
    fr = data.get("final_response")
    if fr is None:
        return None, "missing final_response"
    if not isinstance(fr, dict):
        return None, "final_response is not a dict"
    return fr, None


def aggregate_classify_stats(log_dir: str) -> Dict[str, Any]:
    """
    扫描 log_dir 下 function_classify 日志，返回结构化统计。

    返回字段（新增字段均为增量，不破坏旧字段）:
      - by_type: { type: [sorted function names] }                         (旧)
      - counts: { type: n } 及 UNKNOWN / PARSE_ERROR                        (旧)
      - by_type_has_replacement: {type: {"true": [...], "false": [...]}}   (新)
      - counts_has_replacement: {type: {"true": n, "false": n}}            (新)
      - per_function: {func: {function_type, has_replacement, log_path}}   (新)
      - parse_errors: [{ function, path, error }]
      - log_dir, total_functions
    """
    if not os.path.isdir(log_dir):
        return {
            "log_dir": log_dir,
            "by_type": {},
            "counts": {},
            "by_type_has_replacement": {},
            "counts_has_replacement": {},
            "per_function": {},
            "parse_errors": [],
            "total_functions": 0,
            "error": "log directory does not exist",
        }

    latest = latest_classify_log_paths(log_dir)
    by_type: Dict[str, List[str]] = defaultdict(list)
    by_type_has_rep: Dict[str, Dict[str, List[str]]] = defaultdict(
        lambda: {"true": [], "false": []}
    )
    per_function: Dict[str, Dict[str, Any]] = {}
    parse_errors: List[Dict[str, str]] = []

    for func, path in latest.items():
        fr, err = _read_final_response(path)
        if err:
            parse_errors.append({"function": func, "path": path, "error": err})
            continue

        name_in_json = fr.get("function_name") or func
        ftype = fr.get("function_type")
        if ftype == "NEEDCHECK":
            ftype = "NODRIVER"  # legacy classify logs
        if not ftype or ftype not in VALID_TYPES:
            ftype = "UNKNOWN"
        has_rep = bool(fr.get("has_replacement", False))

        by_type[ftype].append(name_in_json)
        by_type_has_rep[ftype]["true" if has_rep else "false"].append(name_in_json)
        per_function[name_in_json] = {
            "function_type": ftype,
            "has_replacement": has_rep,
            "log_path": os.path.abspath(path),
        }

    for t in list(by_type.keys()):
        by_type[t] = sorted(set(by_type[t]), key=str)
        by_type_has_rep[t]["true"] = sorted(set(by_type_has_rep[t]["true"]), key=str)
        by_type_has_rep[t]["false"] = sorted(set(by_type_has_rep[t]["false"]), key=str)

    counts = {t: len(names) for t, names in by_type.items()}
    counts["PARSE_ERROR"] = len(parse_errors)

    counts_has_rep: Dict[str, Dict[str, int]] = {}
    for t, split in by_type_has_rep.items():
        counts_has_rep[t] = {"true": len(split.get("true", [])), "false": len(split.get("false", []))}

    return {
        "log_dir": os.path.abspath(log_dir),
        "by_type": dict(sorted(by_type.items(), key=lambda x: (-len(x[1]), x[0]))),
        "counts": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
        "by_type_has_replacement": dict(sorted(by_type_has_rep.items(), key=lambda x: (-len(x[1].get("true", [])) - len(x[1].get("false", [])), x[0]))),
        "counts_has_replacement": dict(sorted(counts_has_rep.items(), key=lambda x: (-sum(x[1].values()), x[0]))),
        "per_function": per_function,
        "parse_errors": parse_errors,
        "total_functions": len(latest),
    }


def format_classify_stats_text(stats: Dict[str, Any], include_lists: bool = True) -> str:
    """人类可读的统计文本。"""
    lines: List[str] = []
    if stats.get("error"):
        lines.append(f"错误: {stats['error']}")
        return "\n".join(lines)

    lines.append(f"日志目录: {stats['log_dir']}")
    lines.append(f"已统计函数数（每函数取最新 classify 日志）: {stats['total_functions']}")
    lines.append("")

    lines.append("按分类计数（含 has_replacement 拆分）:")
    counts = stats.get("counts") or {}
    counts_has_rep = stats.get("counts_has_replacement") or {}
    for t, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        if t == "PARSE_ERROR":
            lines.append(f"  {t}: {n}")
            continue
        rep = counts_has_rep.get(t) or {}
        lines.append(f"  {t}: {n} (has_replacement=true: {rep.get('true', 0)}, false: {rep.get('false', 0)})")

    if include_lists:
        lines.append("")
        lines.append("各分类函数列表（按 has_replacement 拆分）:")
        by_type_has_rep = stats.get("by_type_has_replacement") or {}
        for t in sorted(by_type_has_rep.keys()):
            split = by_type_has_rep[t]
            t_true = split.get("true", [])
            t_false = split.get("false", [])
            lines.append(f"  [{t}] (total: {len(t_true) + len(t_false)})")
            lines.append(f"    has_replacement=true ({len(t_true)})")
            for fn in t_true:
                lines.append(f"      - {fn}")
            lines.append(f"    has_replacement=false ({len(t_false)})")
            for fn in t_false:
                lines.append(f"      - {fn}")

    errs = stats.get("parse_errors") or []
    if errs:
        lines.append("")
        lines.append(f"解析失败 ({len(errs)}):")
        for e in errs[:50]:
            lines.append(f"  - {e.get('function')}: {e.get('error')}")
        if len(errs) > 50:
            lines.append(f"  ... 另有 {len(errs) - 50} 条")
    return "\n".join(lines)


def summarize_batch_counts(batch_stats: List[Dict[str, Any]]) -> Dict[str, Any]:
    """将多个 testcase 的 stats 汇总为跨工程的分类计数与总函数数。"""
    merged: Dict[str, int] = defaultdict(int)
    merged_rep: Dict[str, Dict[str, int]] = defaultdict(lambda: {"true": 0, "false": 0})
    total_functions = 0

    for s in batch_stats:
        total_functions += int(s.get("total_functions") or 0)
        for k, v in (s.get("counts") or {}).items():
            try:
                merged[k] += int(v)
            except (TypeError, ValueError):
                continue
        for t, split in (s.get("counts_has_replacement") or {}).items():
            try:
                merged_rep[t]["true"] += int(split.get("true") or 0)
                merged_rep[t]["false"] += int(split.get("false") or 0)
            except (TypeError, ValueError):
                continue

    return {
        "summary_counts": dict(sorted(merged.items(), key=lambda x: (-x[1], x[0]))),
        "summary_counts_has_replacement": dict(
            sorted(merged_rep.items(), key=lambda x: (-(x[1].get("true", 0) + x[1].get("false", 0)), x[0]))
        ),
        "summary_total_functions": total_functions,
    }


_TYPE_PRIORITY = {
    "CORE": 0,
    "RECV": 1,
    "IRQ": 2,
    "INIT": 3,
    "LOOP": 4,
    "RETURNOK": 5,
    "SKIP": 6,
    "NODRIVER": 7,
    "UNKNOWN": 8,
    "PARSE_ERROR": 9,
}


def summarize_batch_unique_by_function_name(batch_stats: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    批量汇总（去重版）：跨 demo 按 function_name 去重，避免同名函数在不同 demo 中重复计数。

    - 去重键：per_function 的 key（即 function_name）
    - 若同名函数在不同 demo 中出现不同 function_type：取更“高优先级”的类型（_TYPE_PRIORITY 越小优先级越高）
    - has_replacement：若任一 demo 为 true，则视为 true
    """
    merged_type_by_fn: Dict[str, str] = {}
    merged_has_rep_by_fn: Dict[str, bool] = {}

    for s in batch_stats:
        pf = (s.get("per_function") or {})
        if not isinstance(pf, dict):
            continue
        for fn, info in pf.items():
            if not fn or not isinstance(fn, str):
                continue
            if not isinstance(info, dict):
                continue
            t = info.get("function_type") or "UNKNOWN"
            if t not in _TYPE_PRIORITY:
                t = "UNKNOWN"
            has_rep = bool(info.get("has_replacement", False))

            prev_t = merged_type_by_fn.get(fn)
            if prev_t is None or _TYPE_PRIORITY.get(t, 99) < _TYPE_PRIORITY.get(prev_t, 99):
                merged_type_by_fn[fn] = t
            merged_has_rep_by_fn[fn] = merged_has_rep_by_fn.get(fn, False) or has_rep

    counts: Dict[str, int] = defaultdict(int)
    counts_has_rep: Dict[str, Dict[str, int]] = defaultdict(lambda: {"true": 0, "false": 0})
    for fn, t in merged_type_by_fn.items():
        counts[t] += 1
        if merged_has_rep_by_fn.get(fn, False):
            counts_has_rep[t]["true"] += 1
        else:
            counts_has_rep[t]["false"] += 1

    return {
        "summary_unique_counts": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
        "summary_unique_counts_has_replacement": dict(
            sorted(counts_has_rep.items(), key=lambda x: (-(x[1].get("true", 0) + x[1].get("false", 0)), x[0]))
        ),
        "summary_unique_total_functions": len(merged_type_by_fn),
    }


_TYPE_PRIORITY = {
    "CORE": 0,
    "RECV": 1,
    "IRQ": 2,
    "INIT": 3,
    "LOOP": 4,
    "RETURNOK": 5,
    "SKIP": 6,
    "NODRIVER": 7,
    "UNKNOWN": 8,
    "PARSE_ERROR": 9,
}


def summarize_batch_unique_by_function_name(batch_stats: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    批量汇总（去重版）：跨 demo 按 function_name 去重，避免同名函数在不同 demo 中重复计数。

    - 去重键：per_function 的 key（即 function_name）
    - 若同名函数在不同 demo 中出现不同 function_type：取更“高优先级”的类型（_TYPE_PRIORITY 越小优先级越高）
    - has_replacement：若任一 demo 为 true，则视为 true
    """
    merged_type_by_fn: Dict[str, str] = {}
    merged_has_rep_by_fn: Dict[str, bool] = {}

    for s in batch_stats:
        pf = (s.get("per_function") or {})
        if not isinstance(pf, dict):
            continue
        for fn, info in pf.items():
            if not fn or not isinstance(fn, str):
                continue
            if not isinstance(info, dict):
                continue
            t = info.get("function_type") or "UNKNOWN"
            if t not in _TYPE_PRIORITY:
                t = "UNKNOWN"
            has_rep = bool(info.get("has_replacement", False))

            prev_t = merged_type_by_fn.get(fn)
            if prev_t is None or _TYPE_PRIORITY.get(t, 99) < _TYPE_PRIORITY.get(prev_t, 99):
                merged_type_by_fn[fn] = t
            merged_has_rep_by_fn[fn] = merged_has_rep_by_fn.get(fn, False) or has_rep

    # 聚合计数
    counts: Dict[str, int] = defaultdict(int)
    counts_has_rep: Dict[str, Dict[str, int]] = defaultdict(lambda: {"true": 0, "false": 0})
    for fn, t in merged_type_by_fn.items():
        counts[t] += 1
        if merged_has_rep_by_fn.get(fn, False):
            counts_has_rep[t]["true"] += 1
        else:
            counts_has_rep[t]["false"] += 1

    return {
        "summary_unique_counts": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
        "summary_unique_counts_has_replacement": dict(
            sorted(counts_has_rep.items(), key=lambda x: (-(x[1].get("true", 0) + x[1].get("false", 0)), x[0]))
        ),
        "summary_unique_total_functions": len(merged_type_by_fn),
    }

