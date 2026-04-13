#!/usr/bin/env python3
"""
MMIO ablation metrics helper.

Purpose:
- Aggregate metrics from classify_stats_output.json files.
- Compare two experiment outputs (A/B) by testcase path.
- Optionally evaluate against manual gold labels.

Usage examples:
  # Single run summary
  python scripts/mmio_ablation_metrics.py \
    --root testcases/server \
    --output-prefix testcases/server/mmio_metrics

  # A/B comparison (for ablation)
  python scripts/mmio_ablation_metrics.py \
    --root-a results/with_static \
    --root-b results/without_static \
    --output-prefix run/mmio_ablation

  # With manual gold labels
  python scripts/mmio_ablation_metrics.py \
    --root testcases/server \
    --gold-map run/mmio_gold_labels.json \
    --output-prefix run/mmio_metrics_with_gold
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple


DEFAULT_POSITIVE_TYPES = {"INIT", "IRQ", "RECV", "LOOP"}
IGNORED_TYPES = {"PARSE_ERROR", "UNKNOWN"}


@dataclass
class DemoMetrics:
    rel_path: str
    total_functions: int
    predicted_count: int
    predicted_ratio: float
    has_replacement_true_count: int
    has_replacement_true_ratio: float
    replacement_update_count: int
    replacement_update_ratio: float
    parse_error_count: int
    # Optional gold metrics
    gold_size: Optional[int] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1: Optional[float] = None


def _load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"JSON root is not dict: {path}")
    return data


def _safe_ratio(num: int, den: int) -> float:
    if den <= 0:
        return 0.0
    return float(num) / float(den)


def _f1(p: float, r: float) -> float:
    if p + r == 0.0:
        return 0.0
    return 2.0 * p * r / (p + r)


def _find_classify_outputs(root: str) -> List[str]:
    hits: List[str] = []
    root = os.path.abspath(root)
    for dirpath, _, filenames in os.walk(root):
        if "classify_stats_output.json" in filenames:
            hits.append(os.path.join(dirpath, "classify_stats_output.json"))
    return sorted(hits)


def _predict_set_from_stats(
    stats: dict,
    positive_types: Set[str],
    include_has_replacement_true: bool,
    include_replacement_update: bool,
) -> Set[str]:
    per_function = stats.get("per_function") or {}
    if not isinstance(per_function, dict):
        return set()
    pred: Set[str] = set()
    for fn, info in per_function.items():
        if not isinstance(fn, str) or not fn:
            continue
        if not isinstance(info, dict):
            continue
        ftype = str(info.get("function_type") or "")
        has_rep = bool(info.get("has_replacement", False))
        has_rep_update = bool(info.get("has_replacement_update", False))

        if ftype in positive_types:
            pred.add(fn)
            continue
        if include_has_replacement_true and has_rep:
            pred.add(fn)
            continue
        if include_replacement_update and has_rep_update:
            pred.add(fn)
            continue
    return pred


def _calc_demo_metrics(
    stats: dict,
    rel_path: str,
    positive_types: Set[str],
    include_has_replacement_true: bool,
    include_replacement_update: bool,
    gold_map: Optional[Dict[str, List[str]]] = None,
) -> DemoMetrics:
    total_functions = int(stats.get("total_functions") or 0)
    parse_error_count = int((stats.get("counts") or {}).get("PARSE_ERROR", 0) or 0)
    replacement_update_count = int(stats.get("replacement_update_count") or 0)

    pred_set = _predict_set_from_stats(
        stats,
        positive_types=positive_types,
        include_has_replacement_true=include_has_replacement_true,
        include_replacement_update=include_replacement_update,
    )
    predicted_count = len(pred_set)

    per_function = stats.get("per_function") or {}
    has_replacement_true_count = 0
    if isinstance(per_function, dict):
        for _, info in per_function.items():
            if isinstance(info, dict) and bool(info.get("has_replacement", False)):
                has_replacement_true_count += 1

    m = DemoMetrics(
        rel_path=rel_path,
        total_functions=total_functions,
        predicted_count=predicted_count,
        predicted_ratio=_safe_ratio(predicted_count, total_functions),
        has_replacement_true_count=has_replacement_true_count,
        has_replacement_true_ratio=_safe_ratio(has_replacement_true_count, total_functions),
        replacement_update_count=replacement_update_count,
        replacement_update_ratio=_safe_ratio(replacement_update_count, total_functions),
        parse_error_count=parse_error_count,
    )

    if gold_map is not None:
        gold = set(gold_map.get(rel_path) or [])
        if gold:
            tp = len(pred_set & gold)
            p = _safe_ratio(tp, len(pred_set))
            r = _safe_ratio(tp, len(gold))
            m.gold_size = len(gold)
            m.precision = p
            m.recall = r
            m.f1 = _f1(p, r)
        else:
            m.gold_size = 0
            m.precision = 0.0
            m.recall = 0.0
            m.f1 = 0.0
    return m


def _aggregate(demo_metrics: List[DemoMetrics], has_gold: bool) -> dict:
    n = len(demo_metrics)
    sum_total = sum(m.total_functions for m in demo_metrics)
    sum_pred = sum(m.predicted_count for m in demo_metrics)
    sum_has_rep = sum(m.has_replacement_true_count for m in demo_metrics)
    sum_rep_upd = sum(m.replacement_update_count for m in demo_metrics)
    sum_parse = sum(m.parse_error_count for m in demo_metrics)

    out = {
        "demo_count": n,
        "total_functions": sum_total,
        "predicted_count": sum_pred,
        "predicted_ratio_micro": _safe_ratio(sum_pred, sum_total),
        "has_replacement_true_count": sum_has_rep,
        "has_replacement_true_ratio_micro": _safe_ratio(sum_has_rep, sum_total),
        "replacement_update_count": sum_rep_upd,
        "replacement_update_ratio_micro": _safe_ratio(sum_rep_upd, sum_total),
        "parse_error_count": sum_parse,
        "predicted_ratio_macro": _safe_ratio(
            int(round(sum(m.predicted_ratio for m in demo_metrics) * 1_000_000)),
            int(1_000_000 * max(n, 1)),
        ),
    }

    if has_gold and n > 0:
        p_vals = [m.precision for m in demo_metrics if m.precision is not None]
        r_vals = [m.recall for m in demo_metrics if m.recall is not None]
        f_vals = [m.f1 for m in demo_metrics if m.f1 is not None]
        out["gold_macro_precision"] = (sum(p_vals) / len(p_vals)) if p_vals else 0.0
        out["gold_macro_recall"] = (sum(r_vals) / len(r_vals)) if r_vals else 0.0
        out["gold_macro_f1"] = (sum(f_vals) / len(f_vals)) if f_vals else 0.0
    return out


def _parse_types(raw: str) -> Set[str]:
    items = [x.strip().upper() for x in raw.split(",")]
    return {x for x in items if x and x not in IGNORED_TYPES}


def _load_gold_map(path: Optional[str]) -> Optional[Dict[str, List[str]]]:
    if not path:
        return None
    data = _load_json(path)
    out: Dict[str, List[str]] = {}
    for k, v in data.items():
        if not isinstance(k, str):
            continue
        if isinstance(v, list):
            out[k] = [x for x in v if isinstance(x, str) and x]
    return out


def _collect_from_root(
    root: str,
    positive_types: Set[str],
    include_has_replacement_true: bool,
    include_replacement_update: bool,
    gold_map: Optional[Dict[str, List[str]]],
) -> Tuple[List[DemoMetrics], Dict[str, dict]]:
    files = _find_classify_outputs(root)
    root_abs = os.path.abspath(root)
    demos: List[DemoMetrics] = []
    by_rel: Dict[str, dict] = {}
    for path in files:
        stats = _load_json(path)
        rel_dir = os.path.relpath(os.path.dirname(path), root_abs).replace("\\", "/")
        m = _calc_demo_metrics(
            stats=stats,
            rel_path=rel_dir,
            positive_types=positive_types,
            include_has_replacement_true=include_has_replacement_true,
            include_replacement_update=include_replacement_update,
            gold_map=gold_map,
        )
        demos.append(m)
        by_rel[rel_dir] = stats
    demos.sort(key=lambda x: x.rel_path)
    return demos, by_rel


def _metrics_to_dict(m: DemoMetrics) -> dict:
    return {
        "rel_path": m.rel_path,
        "total_functions": m.total_functions,
        "predicted_count": m.predicted_count,
        "predicted_ratio": m.predicted_ratio,
        "has_replacement_true_count": m.has_replacement_true_count,
        "has_replacement_true_ratio": m.has_replacement_true_ratio,
        "replacement_update_count": m.replacement_update_count,
        "replacement_update_ratio": m.replacement_update_ratio,
        "parse_error_count": m.parse_error_count,
        "gold_size": m.gold_size,
        "precision": m.precision,
        "recall": m.recall,
        "f1": m.f1,
    }


def _render_markdown_single(
    root: str,
    demos: List[DemoMetrics],
    agg: dict,
    positive_types: Set[str],
    include_has_replacement_true: bool,
    include_replacement_update: bool,
    has_gold: bool,
) -> str:
    lines: List[str] = []
    lines.append("# MMIO Metrics Summary")
    lines.append("")
    lines.append(f"- Root: `{os.path.abspath(root)}`")
    lines.append(f"- Demo count: **{agg['demo_count']}**")
    lines.append(f"- Positive types: `{','.join(sorted(positive_types))}`")
    lines.append(f"- include_has_replacement_true: `{include_has_replacement_true}`")
    lines.append(f"- include_replacement_update: `{include_replacement_update}`")
    lines.append("")
    lines.append("## Overall")
    lines.append("")
    lines.append(f"- total_functions: **{agg['total_functions']}**")
    lines.append(f"- predicted_count: **{agg['predicted_count']}**")
    lines.append(f"- predicted_ratio_micro: **{agg['predicted_ratio_micro']:.4f}**")
    lines.append(f"- has_replacement_true_count: **{agg['has_replacement_true_count']}**")
    lines.append(f"- replacement_update_count: **{agg['replacement_update_count']}**")
    lines.append(f"- parse_error_count: **{agg['parse_error_count']}**")
    if has_gold:
        lines.append(f"- gold_macro_precision: **{agg.get('gold_macro_precision', 0.0):.4f}**")
        lines.append(f"- gold_macro_recall: **{agg.get('gold_macro_recall', 0.0):.4f}**")
        lines.append(f"- gold_macro_f1: **{agg.get('gold_macro_f1', 0.0):.4f}**")
    lines.append("")
    lines.append("## Per Demo")
    lines.append("")
    header = [
        "DemoPath",
        "Total",
        "Pred",
        "PredRatio",
        "HasRepT",
        "RepUpd",
        "ParseErr",
    ]
    if has_gold:
        header.extend(["GoldN", "P", "R", "F1"])
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    for m in demos:
        row = [
            f"`{m.rel_path}`",
            str(m.total_functions),
            str(m.predicted_count),
            f"{m.predicted_ratio:.4f}",
            str(m.has_replacement_true_count),
            str(m.replacement_update_count),
            str(m.parse_error_count),
        ]
        if has_gold:
            row.extend(
                [
                    str(m.gold_size if m.gold_size is not None else 0),
                    f"{(m.precision or 0.0):.4f}",
                    f"{(m.recall or 0.0):.4f}",
                    f"{(m.f1 or 0.0):.4f}",
                ]
            )
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")
    return "\n".join(lines)


def _render_markdown_compare(
    root_a: str,
    root_b: str,
    demos_a: List[DemoMetrics],
    demos_b: List[DemoMetrics],
    agg_a: dict,
    agg_b: dict,
) -> str:
    by_a = {m.rel_path: m for m in demos_a}
    by_b = {m.rel_path: m for m in demos_b}
    common = sorted(set(by_a.keys()) & set(by_b.keys()))

    lines: List[str] = []
    lines.append("# MMIO Ablation Comparison")
    lines.append("")
    lines.append(f"- Root A: `{os.path.abspath(root_a)}`")
    lines.append(f"- Root B: `{os.path.abspath(root_b)}`")
    lines.append(f"- Common demos: **{len(common)}**")
    lines.append("")
    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | A | B | Delta(B-A) |")
    lines.append("| --- | --- | --- | --- |")
    keys = [
        "total_functions",
        "predicted_count",
        "predicted_ratio_micro",
        "has_replacement_true_count",
        "replacement_update_count",
        "parse_error_count",
    ]
    for k in keys:
        av = agg_a.get(k, 0)
        bv = agg_b.get(k, 0)
        if isinstance(av, float) or isinstance(bv, float):
            lines.append(f"| {k} | {float(av):.4f} | {float(bv):.4f} | {float(bv) - float(av):.4f} |")
        else:
            lines.append(f"| {k} | {int(av)} | {int(bv)} | {int(bv) - int(av)} |")
    lines.append("")
    lines.append("## Per Demo")
    lines.append("")
    lines.append("| DemoPath | PredRatio_A | PredRatio_B | Delta | RepUpd_A | RepUpd_B | Delta |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for rel in common:
        a = by_a[rel]
        b = by_b[rel]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{rel}`",
                    f"{a.predicted_ratio:.4f}",
                    f"{b.predicted_ratio:.4f}",
                    f"{(b.predicted_ratio - a.predicted_ratio):.4f}",
                    str(a.replacement_update_count),
                    str(b.replacement_update_count),
                    str(b.replacement_update_count - a.replacement_update_count),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Compute MMIO metrics and ablation comparison.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--root", help="Single experiment root (scan classify_stats_output.json recursively)")
    mode.add_argument("--root-a", help="Experiment A root")
    ap.add_argument("--root-b", help="Experiment B root (required with --root-a)")

    ap.add_argument(
        "--positive-types",
        default=",".join(sorted(DEFAULT_POSITIVE_TYPES)),
        help="Comma-separated function types treated as MMIO-positive (default: INIT,IRQ,LOOP,RECV)",
    )
    ap.add_argument(
        "--include-has-replacement-true",
        action="store_true",
        help="Also treat has_replacement=true as MMIO-positive",
    )
    ap.add_argument(
        "--include-replacement-update",
        action="store_true",
        help="Also treat has_replacement_update=true as MMIO-positive",
    )
    ap.add_argument(
        "--gold-map",
        help=(
            "Optional JSON path for manual labels: "
            "{ \"<rel_demo_path>\": [\"funcA\", \"funcB\", ...], ... }"
        ),
    )
    ap.add_argument(
        "--output-prefix",
        required=True,
        help="Output prefix path, produce <prefix>.json and <prefix>.md",
    )
    args = ap.parse_args()

    if args.root_a and not args.root_b:
        raise SystemExit("--root-b is required when --root-a is set")
    if args.root_b and not args.root_a:
        raise SystemExit("--root-a is required when --root-b is set")

    positive_types = _parse_types(args.positive_types)
    if not positive_types:
        raise SystemExit("positive_types cannot be empty")
    gold_map = _load_gold_map(args.gold_map)

    out_json = args.output_prefix + ".json"
    out_md = args.output_prefix + ".md"
    os.makedirs(os.path.dirname(os.path.abspath(out_json)), exist_ok=True)

    if args.root:
        demos, _ = _collect_from_root(
            root=args.root,
            positive_types=positive_types,
            include_has_replacement_true=args.include_has_replacement_true,
            include_replacement_update=args.include_replacement_update,
            gold_map=gold_map,
        )
        agg = _aggregate(demos, has_gold=gold_map is not None)
        out = {
            "mode": "single",
            "root": os.path.abspath(args.root),
            "positive_types": sorted(positive_types),
            "include_has_replacement_true": args.include_has_replacement_true,
            "include_replacement_update": args.include_replacement_update,
            "overall": agg,
            "demos": [_metrics_to_dict(m) for m in demos],
        }
        md = _render_markdown_single(
            root=args.root,
            demos=demos,
            agg=agg,
            positive_types=positive_types,
            include_has_replacement_true=args.include_has_replacement_true,
            include_replacement_update=args.include_replacement_update,
            has_gold=gold_map is not None,
        )
    else:
        demos_a, _ = _collect_from_root(
            root=args.root_a,
            positive_types=positive_types,
            include_has_replacement_true=args.include_has_replacement_true,
            include_replacement_update=args.include_replacement_update,
            gold_map=gold_map,
        )
        demos_b, _ = _collect_from_root(
            root=args.root_b,
            positive_types=positive_types,
            include_has_replacement_true=args.include_has_replacement_true,
            include_replacement_update=args.include_replacement_update,
            gold_map=gold_map,
        )
        agg_a = _aggregate(demos_a, has_gold=gold_map is not None)
        agg_b = _aggregate(demos_b, has_gold=gold_map is not None)
        out = {
            "mode": "compare",
            "root_a": os.path.abspath(args.root_a),
            "root_b": os.path.abspath(args.root_b),
            "positive_types": sorted(positive_types),
            "include_has_replacement_true": args.include_has_replacement_true,
            "include_replacement_update": args.include_replacement_update,
            "overall_a": agg_a,
            "overall_b": agg_b,
            "demos_a": [_metrics_to_dict(m) for m in demos_a],
            "demos_b": [_metrics_to_dict(m) for m in demos_b],
        }
        md = _render_markdown_compare(
            root_a=args.root_a,
            root_b=args.root_b,
            demos_a=demos_a,
            demos_b=demos_b,
            agg_a=agg_a,
            agg_b=agg_b,
        )

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"[mmio-metrics] json: {out_json}")
    print(f"[mmio-metrics] markdown: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

