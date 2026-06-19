#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass
class Row:
    rel_path: str
    total: int
    baseline_count: int
    with_ru_count: int
    ru_increment_count: int
    ru_increment_ratio_total: float
    ru_increment_ratio_baseline: float
    ru_log_function_count: int


def _safe_div(a: int, b: int) -> float:
    return float(a) / float(b) if b else 0.0


def _find_outputs(root: str) -> List[str]:
    outs: List[str] = []
    for dirpath, _, files in os.walk(os.path.abspath(root)):
        if "classify_stats_output.json" in files:
            outs.append(os.path.join(dirpath, "classify_stats_output.json"))
    return sorted(outs)


def _load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"invalid json root: {path}")
    return data


def _sets_from_stats(stats: dict, pos_types: Set[str], include_has_rep: bool) -> Dict[str, Set[str]]:
    per_func = stats.get("per_function") or {}
    if not isinstance(per_func, dict):
        return {"baseline": set(), "with_ru": set(), "ru_only": set()}
    baseline: Set[str] = set()
    with_ru: Set[str] = set()
    for fn, info in per_func.items():
        if not isinstance(fn, str) or not fn or not isinstance(info, dict):
            continue
        t = str(info.get("function_type") or "")
        has_rep = bool(info.get("has_replacement", False))
        has_ru = bool(info.get("has_replacement_update", False))
        in_baseline = (t in pos_types) or (include_has_rep and has_rep)
        in_with_ru = in_baseline or has_ru
        if in_baseline:
            baseline.add(fn)
        if in_with_ru:
            with_ru.add(fn)
    return {"baseline": baseline, "with_ru": with_ru, "ru_only": (with_ru - baseline)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Ablation: quantify ReplacementUpdate contribution.")
    ap.add_argument("--root", required=True, help="Root scanning classify_stats_output.json")
    ap.add_argument("--positive-types", default="INIT,IRQ,RECV,LOOP")
    ap.add_argument("--exclude-has-replacement", action="store_true")
    ap.add_argument("--output-prefix", required=True)
    args = ap.parse_args()

    pos_types = {x.strip().upper() for x in args.positive_types.split(",") if x.strip()}
    include_has_rep = not args.exclude_has_replacement
    files = _find_outputs(args.root)
    root_abs = os.path.abspath(args.root)

    rows: List[Row] = []
    ru_only_union: Set[str] = set()
    for p in files:
        s = _load(p)
        rel = os.path.relpath(os.path.dirname(p), root_abs).replace("\\", "/")
        total = int(s.get("total_functions") or 0)
        sets = _sets_from_stats(s, pos_types, include_has_rep)
        inc = len(sets["ru_only"])
        ru_only_union.update(sets["ru_only"])
        rows.append(
            Row(
                rel_path=rel,
                total=total,
                baseline_count=len(sets["baseline"]),
                with_ru_count=len(sets["with_ru"]),
                ru_increment_count=inc,
                ru_increment_ratio_total=_safe_div(inc, total),
                ru_increment_ratio_baseline=_safe_div(inc, len(sets["baseline"])),
                ru_log_function_count=int(s.get("replacement_update_count") or 0),
            )
        )
    rows.sort(key=lambda x: x.rel_path)

    total_total = sum(r.total for r in rows)
    total_baseline = sum(r.baseline_count for r in rows)
    total_with_ru = sum(r.with_ru_count for r in rows)
    total_inc = sum(r.ru_increment_count for r in rows)
    total_ru_logs = sum(r.ru_log_function_count for r in rows)
    result = {
        "root": root_abs,
        "demo_count": len(rows),
        "positive_types": sorted(pos_types),
        "include_has_replacement_in_baseline": include_has_rep,
        "overall": {
            "total_functions": total_total,
            "baseline_predicted_count_sum": total_baseline,
            "with_ru_predicted_count_sum": total_with_ru,
            "ru_increment_count_sum": total_inc,
            "ru_increment_ratio_over_total": _safe_div(total_inc, total_total),
            "ru_increment_ratio_over_baseline": _safe_div(total_inc, total_baseline),
            "replacement_update_log_function_count_sum": total_ru_logs,
            "ru_only_function_union_count": len(ru_only_union),
        },
        "demos": [r.__dict__ for r in rows],
    }

    out_json = args.output_prefix + ".json"
    out_md = args.output_prefix + ".md"
    os.makedirs(os.path.dirname(os.path.abspath(out_json)), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    ov = result["overall"]
    lines = [
        "# ReplacementUpdate Ablation",
        "",
        f"- Root: `{root_abs}`",
        f"- Demo count: **{len(rows)}**",
        f"- Baseline positive types: `{','.join(sorted(pos_types))}`",
        f"- Baseline include has_replacement=true: `{include_has_rep}`",
        "",
        "## Overall",
        "",
        f"- baseline_predicted_count_sum: **{ov['baseline_predicted_count_sum']}**",
        f"- with_ru_predicted_count_sum: **{ov['with_ru_predicted_count_sum']}**",
        f"- ru_increment_count_sum: **{ov['ru_increment_count_sum']}**",
        f"- ru_increment_ratio_over_total: **{ov['ru_increment_ratio_over_total']:.4f}**",
        f"- ru_increment_ratio_over_baseline: **{ov['ru_increment_ratio_over_baseline']:.4f}**",
        f"- replacement_update_log_function_count_sum: **{ov['replacement_update_log_function_count_sum']}**",
        "",
        "## Per Demo",
        "",
        "| DemoPath | Total | Baseline | WithRU | RU_Increment | RU_Inc/Total | RU_Inc/Baseline | RU_LogFn |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        lines.append(
            f"| `{r.rel_path}` | {r.total} | {r.baseline_count} | {r.with_ru_count} | {r.ru_increment_count} | {r.ru_increment_ratio_total:.4f} | {r.ru_increment_ratio_baseline:.4f} | {r.ru_log_function_count} |"
        )
    lines += [
        "",
        "## Metric Meaning",
        "",
        "- `RU_Increment`: functions brought in only because `has_replacement_update=true`.",
        "- `RU_Inc/Total`: incremental coverage contribution of ReplacementUpdate over all functions.",
        "- `RU_Inc/Baseline`: relative gain against baseline predicted set.",
        "- `RU_LogFn`: number of functions that have replacement_update logs in this demo.",
    ]
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[ru-ablation] json: {out_json}")
    print(f"[ru-ablation] markdown: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
