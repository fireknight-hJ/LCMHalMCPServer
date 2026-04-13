#!/usr/bin/env python3
"""
从 lcmhal_ai_log 下 function_classify_*.json 统计「首次 VerifyReplacement 即 pass」比例（TODO-5）。

仅统计至少出现过一次 VerifyReplacement 的日志；no_feedback 实验无该工具，会归入 skipped。
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from typing import Any, Dict, List, Optional, Tuple


def _parse_verify_pass(content: Any) -> Optional[bool]:
    if content is None:
        return None
    try:
        if isinstance(content, str):
            data = json.loads(content)
        elif isinstance(content, dict):
            data = content
        else:
            return None
        if "pass" in data:
            return bool(data.get("pass"))
    except (json.JSONDecodeError, TypeError, ValueError):
        return None
    return None


def _analyze_messages(messages: List[Any]) -> Tuple[Optional[bool], int]:
    """
    返回 (first_verify_pass, verify_call_count)。
    first_verify_pass: 第一次 VerifyReplacement 的 pass 值；若无 Verify 则为 None。
    """
    id_to_tool: Dict[str, Tuple[str, Dict[str, Any]]] = {}
    verify_outcomes: List[bool] = []

    for msg in messages:
        if not isinstance(msg, dict):
            continue
        tcalls = msg.get("tool_calls")
        if tcalls:
            for tc in tcalls:
                if not isinstance(tc, dict):
                    continue
                tid = tc.get("id")
                name = tc.get("name")
                args = tc.get("args") if isinstance(tc.get("args"), dict) else {}
                if tid and name:
                    id_to_tool[str(tid)] = (name, args)

    for msg in messages:
        if not isinstance(msg, dict):
            continue
        if msg.get("type") != "tool":
            continue
        tid = msg.get("tool_call_id")
        if not tid:
            continue
        name, _ = id_to_tool.get(str(tid), (None, {}))
        if name != "VerifyReplacement":
            continue
        passed = _parse_verify_pass(msg.get("content"))
        if passed is not None:
            verify_outcomes.append(passed)

    if not verify_outcomes:
        return None, 0
    return verify_outcomes[0], len(verify_outcomes)


def scan_log_dir(log_dir: str) -> Dict[str, Any]:
    pattern = os.path.join(log_dir, "function_classify_*.json")
    paths = sorted(glob.glob(pattern))
    n_files = 0
    n_with_verify = 0
    n_first_pass = 0
    n_first_fail = 0
    per_file: List[Dict[str, Any]] = []

    for path in paths:
        n_files += 1
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            per_file.append({"path": path, "error": str(e)})
            continue
        messages = data.get("messages")
        if not isinstance(messages, list):
            per_file.append({"path": path, "error": "missing messages"})
            continue
        first_pass, n_verify = _analyze_messages(messages)
        row: Dict[str, Any] = {
            "path": path,
            "verify_calls": n_verify,
            "first_verify_pass": first_pass,
        }
        if n_verify == 0:
            row["bucket"] = "no_verify_in_log"
        else:
            n_with_verify += 1
            if first_pass is True:
                n_first_pass += 1
                row["bucket"] = "first_pass"
            elif first_pass is False:
                n_first_fail += 1
                row["bucket"] = "first_fail"
            else:
                row["bucket"] = "unknown"
        per_file.append(row)

    rate = (float(n_first_pass) / float(n_with_verify)) if n_with_verify else None
    return {
        "log_dir": os.path.abspath(log_dir),
        "function_classify_files": n_files,
        "logs_with_at_least_one_verify": n_with_verify,
        "first_verify_pass_count": n_first_pass,
        "first_verify_fail_count": n_first_fail,
        "first_verify_pass_rate_among_with_verify": rate,
        "per_file": per_file,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="First VerifyReplacement pass stats from classify logs.")
    ap.add_argument("--log-dir", required=True, help="Path to .../lcmhal_ai_log")
    ap.add_argument("--output", default="", help="Write JSON summary to this path (optional)")
    args = ap.parse_args()

    out = scan_log_dir(args.log_dir)
    text = json.dumps(out, ensure_ascii=False, indent=2)
    print(text)
    if args.output:
        out_abs = os.path.abspath(args.output)
        out_dir = os.path.dirname(out_abs)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[first-verify-stats] wrote {args.output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
