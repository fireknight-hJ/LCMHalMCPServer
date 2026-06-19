#!/usr/bin/env python3
"""
从 E3b 批次 isolated_db 解析表 5-x 所需字段（与 logs/run_log 交叉处见 --compare）。

识别数：lcmhal_ai_log/log_index.json 中 legacy_logs 以 function_classify_ 为前缀的键数
  （= 产生过独立 function_classify 日志条目的函数数；可能与主流程首次 classifying N 不一致）。

末轮替换数：主流程 [REPLACE] 仅出现在 stdout，默认从 run_log.tsv 的 log_file 解析末次 X/X。

仿真成功：lcmhal_ai_log/run_emulator__*.json 按文件名序最后一文件的 final_response.success；
  若无 run_emulator 落盘则记为否。

LLM invokes / total_tokens：session_<session_id>_*.json 的 llm_usage_summary。

main 退出码：优先 artifacts/<U*_run>/e3b_run_manifest.txt 的 main_exit_code；否则 run_log.tsv exit_code。

墙钟（s）：session 的 end_time - start_time（ISO）；若无 end_time 则用 run_log.tsv wall_sec。
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


def _load_session(db_path: str, session_id: str) -> Optional[Dict[str, Any]]:
    """加载 session JSON。若 run_log 中的 session_id 与落盘文件名不一致，回退为 lcmhal_ai_log 下
    带 llm_usage_summary 的最后一个 session_*.json（按路径序）。"""
    log_dir = os.path.join(db_path, "lcmhal_ai_log")
    pattern = os.path.join(log_dir, f"session_{session_id}_*.json")
    paths = sorted(glob.glob(pattern))
    if not paths:
        all_sess = sorted(glob.glob(os.path.join(log_dir, "session_*.json")))
        candidates: list[Dict[str, Any]] = []
        for p in all_sess:
            try:
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(data, dict) and data.get("llm_usage_summary"):
                candidates.append(data)
        return candidates[-1] if candidates else None
    try:
        with open(paths[-1], "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return None


def _session_wall_sec(session: Dict[str, Any]) -> Optional[int]:
    st = session.get("start_time")
    et = session.get("end_time")
    if not st or not et:
        return None
    try:
        a = datetime.fromisoformat(str(st))
        b = datetime.fromisoformat(str(et))
        return int((b - a).total_seconds())
    except ValueError:
        return None


def _log_index_classify_count(db_path: str) -> Optional[int]:
    p = os.path.join(db_path, "lcmhal_ai_log", "log_index.json")
    if not os.path.isfile(p):
        return None
    try:
        with open(p, "r", encoding="utf-8") as f:
            idx = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None
    keys = [k for k in (idx.get("legacy_logs") or {}) if str(k).startswith("function_classify_")]
    return len(keys)


def _last_replace_from_log(log_path: str) -> Tuple[Optional[str], Optional[Tuple[int, int]]]:
    if not log_path or not os.path.isfile(log_path):
        return None, None
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except OSError:
        return None, None
    repl = list(re.finditer(r"\[REPLACE\] Successfully replaced functions: (\d+)/(\d+)", text))
    if not repl:
        return None, None
    m = repl[-1]
    a, b = int(m.group(1)), int(m.group(2))
    if a == b:
        return str(a), (a, b)
    return f"{a}/{b}", (a, b)


def _first_classifying_n_from_log(log_path: str) -> Optional[int]:
    if not log_path or not os.path.isfile(log_path):
        return None
    try:
        with open(log_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                m = re.search(r"\[analyze_functions\] classifying (\d+) functions", line)
                if m:
                    return int(m.group(1))
    except OSError:
        return None
    return None


def _emulate_success_from_isolated_db(db_path: str) -> bool:
    log_dir = Path(db_path) / "lcmhal_ai_log"
    paths = sorted(log_dir.glob("run_emulator__*.json"))
    if not paths:
        return False
    try:
        data = json.loads(paths[-1].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    fr = data.get("final_response")
    if isinstance(fr, dict) and "success" in fr:
        return bool(fr.get("success"))
    # 回退：扫描最后一条 EmulateProject 工具返回 JSON
    last = None
    for m in data.get("messages") or []:
        if m.get("type") != "tool":
            continue
        if m.get("name") != "EmulateProject":
            continue
        c = m.get("content")
        if not isinstance(c, str):
            continue
        try:
            j = json.loads(c)
        except json.JSONDecodeError:
            continue
        if isinstance(j, dict) and "success" in j:
            last = bool(j.get("success"))
    return bool(last)


def _parse_llm_usage_line(line: str) -> Tuple[Optional[int], Optional[int]]:
    if not line:
        return None, None
    mi = re.search(r"invokes=(\d+)", line)
    mt = re.search(r"total_tokens=(\d+)", line)
    inv = int(mi.group(1)) if mi else None
    tt = int(mt.group(1)) if mt else None
    return inv, tt


def _manifest_exit(batch_dir: str, firmware_id: str, run_idx: str) -> Optional[int]:
    # e.g. U1 + run 1 -> U1_run1
    tag = f"{firmware_id}_run{run_idx}"
    man = Path(batch_dir) / "artifacts" / tag / "e3b_run_manifest.txt"
    if not man.is_file():
        return None
    try:
        txt = man.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = re.search(r"^main_exit_code=(\d+)\s*$", txt, re.M)
    if m:
        return int(m.group(1))
    return None


def _fmt_int_spaced(n: int) -> str:
    s = str(n)
    if len(s) <= 3:
        return s
    parts = []
    while s:
        parts.append(s[-3:])
        s = s[:-3]
    return " ".join(reversed(parts))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-dir", required=True)
    ap.add_argument("--compare", action="store_true", help="Print classify_N_log vs log_index delta")
    ap.add_argument("-o", "--output-tsv", help="Write machine-readable TSV")
    args = ap.parse_args()
    batch_dir = os.path.abspath(args.batch_dir)
    tsv_path = os.path.join(batch_dir, "run_log.tsv")
    if not os.path.isfile(tsv_path):
        print(f"error: missing {tsv_path}", file=sys.stderr)
        return 1

    rows_out: list[dict[str, Any]] = []
    with open(tsv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            fid = (row.get("firmware_id") or "").strip()
            run_idx = (row.get("run_idx") or "").strip()
            db_path = (row.get("db_path_used") or row.get("db_path") or "").strip()
            sid = (row.get("session_id") or "").strip()
            log_file = (row.get("log_file") or "").strip()
            exit_tsv = row.get("exit_code", "").strip()
            wall_tsv = row.get("wall_sec", "").strip()

            session = _load_session(db_path, sid) if sid else None
            summ = (session or {}).get("llm_usage_summary") if isinstance(session, dict) else None
            summ = summ if isinstance(summ, dict) else {}

            invokes = summ.get("invoke_count")
            total_tokens = summ.get("total_tokens")
            if invokes is None or total_tokens is None:
                li = (row.get("llm_usage_line") or "").strip()
                fi, ft = _parse_llm_usage_line(li)
                invokes = invokes if invokes is not None else fi
                total_tokens = total_tokens if total_tokens is not None else ft
            wall_sess = _session_wall_sec(session) if session else None
            wall = wall_sess if wall_sess is not None else (int(wall_tsv) if wall_tsv.isdigit() else None)

            cls_idx = _log_index_classify_count(db_path)
            last_rep_s, _ = _last_replace_from_log(log_file)
            emu_ok = _emulate_success_from_isolated_db(db_path)
            man_exit = _manifest_exit(batch_dir, fid, run_idx)
            try:
                exit_code = int(man_exit if man_exit is not None else exit_tsv)
            except ValueError:
                exit_code = None

            n_log = _first_classifying_n_from_log(log_file)

            rows_out.append(
                {
                    "firmware_id": fid,
                    "run_idx": run_idx,
                    "testcase_rel_path": (row.get("testcase_rel_path") or "").strip(),
                    "db_path": db_path,
                    "classify_keys_log_index": cls_idx,
                    "classify_n_first_log": n_log,
                    "last_replace": last_rep_s,
                    "emulate_ok_run_emulator_json": emu_ok,
                    "invoke_count": invokes,
                    "total_tokens": total_tokens,
                    "wall_sec": wall,
                    "main_exit_code": exit_code,
                }
            )

            if args.compare and cls_idx is not None and n_log is not None and cls_idx != n_log:
                print(f"NOTE {fid} run{run_idx}: log_index classify keys={cls_idx} vs log classifying N={n_log}", file=sys.stderr)

    if args.output_tsv:
        out_path = os.path.abspath(args.output_tsv)
        fieldnames = list(rows_out[0].keys()) if rows_out else []
        with open(out_path, "w", newline="", encoding="utf-8") as wf:
            w = csv.DictWriter(wf, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            for r in rows_out:
                w.writerow({k: "" if v is None else v for k, v in r.items()})
        print(f"Wrote {out_path}", file=sys.stderr)

    # Markdown table rows (short firmware names for 论文章节表)
    short = {
        "U1": "NXP_LwIP_BareMetal",
        "U2": "NXP_I2C_BareMetal",
        "U3": "stm32f401-st-nucleo/eth",
        "U4": "UART_Hyperterminal_IT",
        "U5": "imxrt1052-nxp-evk/base",
    }
    for r in rows_out:
        fid = r["firmware_id"]
        fw = short.get(fid, fid)
        tc = r.get("testcase_rel_path") or ""
        if fid == "U3" and "LwIP_StreamingServer" in tc:
            fw = "LwIP_StreamingServer"
        elif fid == "U3" and "LwIP_HTTP_Server_Socket_RTOS" in tc:
            fw = "LwIP_HTTP_Server_Socket_RTOS"
        cls = r["classify_keys_log_index"]
        rep = r["last_replace"] or ""
        emu = "是" if r["emulate_ok_run_emulator_json"] else "否"
        ex = r["main_exit_code"]
        inv = r["invoke_count"]
        tt = r["total_tokens"]
        w = r["wall_sec"]
        line = (
            f"| {fw} | {r['run_idx']} | {cls} | {rep} | {emu} | {ex} | "
            f"{_fmt_int_spaced(int(inv)) if inv is not None else ''} | "
            f"{_fmt_int_spaced(int(tt)) if tt is not None else ''} | "
            f"{_fmt_int_spaced(int(w)) if w is not None else ''} |"
        )
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
