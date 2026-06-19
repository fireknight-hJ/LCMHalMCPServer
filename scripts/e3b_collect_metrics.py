#!/usr/bin/env python3
"""
从 E3b 批跑目录的 run_log.tsv 读取 session_id 与 db_path，
加载 {db_path}/lcmhal_ai_log/session_<session_id>_*.json，抽取 llm_usage_summary。
只读 JSON，不调用 main / emulate。
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import sys
from typing import Any, Dict, List, Optional


def _load_session_json(db_path: str, session_id: str) -> Optional[Dict[str, Any]]:
    if not session_id or not db_path:
        return None
    log_dir = os.path.join(db_path, "lcmhal_ai_log")
    pattern = os.path.join(log_dir, f"session_{session_id}_*.json")
    paths = sorted(glob.glob(pattern))
    if not paths:
        return None
    # 同一 session_id 应对应单文件；若多个取字典序最后（通常时间戳最新）
    path = paths[-1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def _flatten_usage(summary: Dict[str, Any]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not summary:
        return out
    for k in (
        "invoke_count",
        "total_elapsed_ms",
        "avg_elapsed_ms",
        "total_prompt_tokens",
        "total_completion_tokens",
        "total_tokens",
    ):
        v = summary.get(k)
        if v is not None:
            out[k] = str(v)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Collect llm_usage_summary from E3b batch run_log.tsv")
    ap.add_argument(
        "--batch-dir",
        required=True,
        help="Directory containing run_log.tsv (e.g. runs/e3b_uncertainty/20260506_120000)",
    )
    ap.add_argument(
        "-o",
        "--output",
        help="Write TSV summary to this path (default: <batch-dir>/llm_summary.tsv)",
    )
    args = ap.parse_args()
    batch_dir = os.path.abspath(args.batch_dir)
    tsv_path = os.path.join(batch_dir, "run_log.tsv")
    if not os.path.isfile(tsv_path):
        print(f"error: missing {tsv_path}", file=sys.stderr)
        return 1

    out_path = args.output or os.path.join(batch_dir, "llm_summary.tsv")

    rows: List[Dict[str, str]] = []
    fieldnames: List[str] = [
        "firmware_id",
        "testcase_rel_path",
        "db_path",
        "run_idx",
        "exit_code",
        "wall_sec",
        "session_id",
        "session_json_found",
        "invoke_count",
        "total_elapsed_ms",
        "total_prompt_tokens",
        "total_completion_tokens",
        "total_tokens",
        "log_file",
    ]

    with open(tsv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            sid = (row.get("session_id") or "").strip()
            db_path = (row.get("db_path") or "").strip()
            data = _load_session_json(db_path, sid) if sid else None
            summary = (data or {}).get("llm_usage_summary") if isinstance(data, dict) else None
            summary = summary if isinstance(summary, dict) else {}
            flat = _flatten_usage(summary)

            rows.append(
                {
                    "firmware_id": row.get("firmware_id", ""),
                    "testcase_rel_path": row.get("testcase_rel_path", ""),
                    "db_path": db_path,
                    "run_idx": row.get("run_idx", ""),
                    "exit_code": row.get("exit_code", ""),
                    "wall_sec": row.get("wall_sec", ""),
                    "session_id": sid,
                    "session_json_found": "yes" if data else "no",
                    "invoke_count": flat.get("invoke_count", ""),
                    "total_elapsed_ms": flat.get("total_elapsed_ms", ""),
                    "total_prompt_tokens": flat.get("total_prompt_tokens", ""),
                    "total_completion_tokens": flat.get("total_completion_tokens", ""),
                    "total_tokens": flat.get("total_tokens", ""),
                    "log_file": row.get("log_file", ""),
                }
            )

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # Human-readable stdout
    print(f"Wrote {out_path}")
    for r in rows:
        line = (
            f"{r['firmware_id']}\t{r['run_idx']}\tsession={r['session_id'][:8] if r['session_id'] else ''}…\t"
            f"json={r['session_json_found']}\ttokens={r['total_tokens'] or '-'}"
        )
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
