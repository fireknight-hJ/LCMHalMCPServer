#!/usr/bin/env python3
"""
E3b 批次实测汇总 TSV：从 isolated_db 复算

- **识别函数个数**、**RU落盘次数**（前期：分类采纳 + `replacement_update` 落盘）
- **迭代优化数量**、**迭代优化目标**（后期：`function_fix_*.json` 个数及文件名中的符号序列）

不写入「末轮成功替换 / 仿真成功 / exit」——改看 `run_log.tsv` 或日志即可。

用法:
  python3 tools/e3b_batch_replacement_stats.py \\
    --isolated-db-root runs/e3b_uncertainty/20260508_045825/isolated_db \\
    --summary-tsv doc/experiments/E3b-批次20260508_045825_实测汇总.tsv
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

OUT_HEADERS = [
    "固件ID",
    "testcase相对路径",
    "run",
    "分析函数个数",
    "识别函数个数",
    "RU落盘次数",
    "迭代优化数量",
    "迭代优化目标",
    "invokes",
    "total_tokens",
    "wall秒",
    "log文件",
]

LEGACY_IN = {
    "firmware_id": "固件ID",
    "testcase_rel_path": "testcase相对路径",
    "run_idx": "run",
    "analyze_functions_n": "分析函数个数",
    "invokes": "invokes",
    "total_tokens": "total_tokens",
    "wall_sec": "wall秒",
    "log_file": "log文件",
}


def parse_func_name_classify(name: str) -> str | None:
    m = re.match(r"function_classify_(.+)_\d{14}\.json$", name)
    return m.group(1) if m else None


def parse_func_name_ru(name: str) -> str | None:
    m = re.match(r"replacement_update_(.+)_\d{14}\.json$", name)
    return m.group(1) if m else None


def parse_func_name_fix(name: str) -> str | None:
    m = re.match(r"function_fix_(.+)_\d{14}\.json$", name)
    return m.group(1) if m else None


def stats_for_run(log_dir: Path) -> dict[str, int | str]:
    replace_true: set[str] = set()
    for p in log_dir.glob("function_classify_*.json"):
        fn = parse_func_name_classify(p.name)
        if not fn:
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except (json.JSONDecodeError, OSError):
            continue
        fr = data.get("final_response") or {}
        if fr.get("has_replacement") is True:
            replace_true.add(fn)

    ru_total = len(list(log_dir.glob("replacement_update_*.json")))

    fix_paths = sorted(log_dir.glob("function_fix_*.json"), key=lambda p: p.name)
    targets: list[str] = []
    for p in fix_paths:
        fn = parse_func_name_fix(p.name)
        if fn:
            targets.append(fn)

    return {
        "识别函数个数": len(replace_true),
        "RU落盘次数": ru_total,
        "迭代优化数量": len(fix_paths),
        "迭代优化目标": ";".join(targets),
    }


def run_key_from_log_cell(log_cell: str) -> str | None:
    m = re.search(r"(U\d+_run\d+)\.log$", log_cell)
    return m.group(1) if m else None


def normalize_input_row(raw: dict[str, str], header_line: list[str]) -> dict[str, str]:
    out: dict[str, str] = {h: "" for h in OUT_HEADERS}
    if "firmware_id" in raw or ("固件ID" not in raw and "firmware_id" in header_line):
        for eng, zh in LEGACY_IN.items():
            if eng in raw and raw[eng] is not None:
                out[zh] = str(raw[eng]).strip()
        legacy_map = {
            "classify_has_replace_true_fn_n": "识别函数个数",
            "replacement_update_files_n": "RU落盘次数",
        }
        for eng, zh in legacy_map.items():
            if eng in raw and raw[eng]:
                out[zh] = str(raw[eng]).strip()
    else:
        for h in OUT_HEADERS:
            if h in raw and raw[h] is not None:
                out[h] = str(raw[h]).strip()

    # 从上一版中文表迁移「动态修复*」→「迭代优化*」
    if not out.get("迭代优化数量") and raw.get("动态修复会话次数"):
        out["迭代优化数量"] = str(raw["动态修复会话次数"]).strip()
    if not out.get("迭代优化目标") and raw.get("动态修复目标") is not None:
        out["迭代优化目标"] = str(raw["动态修复目标"]).strip()

    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--isolated-db-root", type=Path, required=True)
    ap.add_argument("--summary-tsv", type=Path, required=True)
    args = ap.parse_args()
    root: Path = args.isolated_db_root
    tsv_path: Path = args.summary_tsv
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 1

    cache: dict[str, dict[str, int | str]] = {}
    for run_dir in sorted(root.iterdir()):
        if not run_dir.is_dir():
            continue
        logd = run_dir / "lcmhal_ai_log"
        if logd.is_dir():
            cache[run_dir.name] = stats_for_run(logd)

    if not tsv_path.is_file():
        print(f"missing TSV: {tsv_path}", file=sys.stderr)
        return 1

    with tsv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        in_fields = reader.fieldnames or []
        rows_in = list(reader)

    out_rows: list[dict[str, str]] = []
    for raw in rows_in:
        row = normalize_input_row(raw, list(in_fields))
        key = run_key_from_log_cell(row.get("log文件", ""))
        st = cache.get(key or "", {})
        for k, v in st.items():
            row[str(k)] = str(v)
        out_rows.append(row)

    with tsv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=OUT_HEADERS,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        w.writeheader()
        for row in out_rows:
            w.writerow({h: row.get(h, "") for h in OUT_HEADERS})

    print(f"updated {tsv_path} ({len(out_rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
