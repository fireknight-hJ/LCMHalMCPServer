#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple


RETRY_TOKEN = "Retrying request to /chat/completions"
TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3}")


@dataclass
class PlatformConfig:
    name: str
    script: str
    log_dir: str


PLATFORMS: Dict[str, PlatformConfig] = {
    "rtthread": PlatformConfig(
        name="rtthread",
        script="scripts/batch_main_analyze_rtthread_parallel.sh",
        log_dir="run/batch_main_analyze_rtthread_logs",
    ),
    "stm32": PlatformConfig(
        name="stm32",
        script="scripts/batch_main_analyze_stm32_parallel.sh",
        log_dir="run/batch_main_analyze_stm32_logs",
    ),
    "nxp": PlatformConfig(
        name="nxp",
        script="scripts/batch_main_analyze_nxp_parallel.sh",
        log_dir="run/batch_main_analyze_nxp_logs",
    ),
    "zephyr": PlatformConfig(
        name="zephyr",
        script="scripts/batch_main_analyze_zephyr_parallel.sh",
        log_dir="run/batch_main_analyze_zephyr_logs",
    ),
}

PLATFORM_TESTCASE_ROOT: Dict[str, str] = {
    "rtthread": "testcases/server/rtthread",
    "stm32": "testcases/server/stm32",
    "nxp": "testcases/server/nxp",
    "zephyr": "testcases/server/zephyr",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Adaptive orchestrator for batch_main_analyze_* scripts. "
            "It auto-degrades concurrency based on retry density in the previous time window."
        )
    )
    parser.add_argument(
        "--platforms",
        nargs="+",
        default=["zephyr", "rtthread", "stm32", "nxp"],
        help="Platforms to run in order (default: zephyr rtthread stm32 nxp)",
    )
    parser.add_argument(
        "--base-jobs",
        type=int,
        default=3,
        help="Base concurrency for each platform before adaptive degrade (default: 3)",
    )
    parser.add_argument(
        "--min-jobs",
        type=int,
        default=1,
        help="Minimum allowed concurrency after degrade (default: 1)",
    )
    parser.add_argument(
        "--window-minutes",
        type=int,
        default=10,
        help="Window size (minutes) used for retry counting (default: 10)",
    )
    parser.add_argument(
        "--high-threshold",
        type=int,
        default=40,
        help="If previous-window retries >= this value, jobs - 1 (default: 40)",
    )
    parser.add_argument(
        "--critical-threshold",
        type=int,
        default=100,
        help="If previous-window retries >= this value, jobs - 2 (default: 100)",
    )
    parser.add_argument(
        "--main-cmd",
        default=os.environ.get("MAIN_CMD", "build"),
        help="MAIN_CMD passed to child scripts (default: env MAIN_CMD or 'build')",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print computed jobs and commands without executing scripts",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run preflight checks: cache coverage, ai_log coverage, and running demo processes",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run checks only and exit without running any platform script",
    )
    return parser.parse_args()


def parse_ts(line: str) -> Optional[datetime]:
    m = TS_RE.match(line)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def count_retries_in_window(log_dir: Path, start: datetime, end: datetime) -> int:
    if not log_dir.exists():
        return 0
    count = 0
    for file in log_dir.glob("*.log"):
        try:
            with file.open("r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if RETRY_TOKEN not in line:
                        continue
                    ts = parse_ts(line)
                    if ts is None:
                        continue
                    if start <= ts < end:
                        count += 1
        except OSError:
            continue
    return count


def load_state(path: Path) -> Dict[str, int]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {k: int(v) for k, v in data.items() if isinstance(v, int)}
    except Exception:
        pass
    return {}


def save_state(path: Path, state: Dict[str, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def calc_degraded_jobs(
    current_jobs: int,
    retries_prev_window: int,
    min_jobs: int,
    high_threshold: int,
    critical_threshold: int,
) -> int:
    jobs = current_jobs
    if retries_prev_window >= critical_threshold:
        jobs -= 2
    elif retries_prev_window >= high_threshold:
        jobs -= 1
    return max(min_jobs, jobs)


def run_platform(
    root: Path,
    platform: PlatformConfig,
    jobs: int,
    main_cmd: str,
    dry_run: bool,
) -> int:
    script_path = root / platform.script
    if not script_path.exists():
        print(f"[{platform.name}] script not found: {script_path}")
        return 127

    cmd = [str(script_path), str(jobs)]
    env = os.environ.copy()
    env["MAIN_CMD"] = main_cmd
    print(f"[{platform.name}] run: MAIN_CMD={main_cmd!r} {' '.join(cmd)}")
    if dry_run:
        return 0
    completed = subprocess.run(cmd, cwd=str(root), env=env)
    return completed.returncode


def discover_demo_dirs(root: Path, selected_platforms: List[str]) -> List[Path]:
    demo_dirs: List[Path] = []
    for p in selected_platforms:
        rel = PLATFORM_TESTCASE_ROOT.get(p)
        if not rel:
            continue
        base = root / rel
        if not base.exists():
            continue
        for cfg in base.rglob("lcmhal_config.yml"):
            demo_dirs.append(cfg.parent)
    return sorted(demo_dirs)


def parse_db_path_from_config(config_file: Path) -> str:
    # 优先走简易解析，避免强依赖额外包
    try:
        for raw in config_file.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line.startswith("db_path:"):
                continue
            val = line.split(":", 1)[1].strip()
            if val.startswith('"') and val.endswith('"'):
                return val[1:-1]
            if val.startswith("'") and val.endswith("'"):
                return val[1:-1]
            return val
    except Exception:
        return ""
    return ""


def check_demo_cache_status(demo_dir: Path, db_path_raw: str) -> Dict[str, object]:
    db_path = Path(db_path_raw)
    ltmp = db_path / "lcmhal_tmp"
    ai_log = db_path / "lcmhal_ai_log"

    common_json = ltmp / "common_info.json"
    driver_json = ltmp / "driver_info.json"
    mmio_json = ltmp / "mmio_info.json"
    src_zip = db_path / "src.zip"

    classify_cnt = 0
    replacement_cnt = 0
    if ai_log.exists():
        try:
            classify_cnt = len(list(ai_log.glob("function_classify_*_*.json")))
            replacement_cnt = len(list(ai_log.glob("replacement_update_*_*.json")))
        except OSError:
            pass

    return {
        "demo": str(demo_dir.relative_to(demo_dir.parents[2])),
        "demo_abs": str(demo_dir),
        "db_path": str(db_path),
        "db_exists": db_path.exists(),
        "src_zip": src_zip.exists(),
        "tmp_dir": ltmp.exists(),
        "common_info": common_json.exists(),
        "driver_info": driver_json.exists(),
        "mmio_info": mmio_json.exists(),
        "ai_log_dir": ai_log.exists(),
        "classify_count": classify_cnt,
        "replacement_count": replacement_cnt,
    }


def get_related_processes() -> List[Dict[str, str]]:
    try:
        # etime 可快速判断“挂了多久”
        out = subprocess.check_output(
            ["ps", "-eo", "pid,ppid,etime,cmd"], text=True, stderr=subprocess.STDOUT
        )
    except Exception:
        return []

    patterns = [
        "batch_main_analyze_adaptive.py",
        "batch_main_analyze_zephyr_parallel.sh",
        "batch_main_analyze_rtthread_parallel.sh",
        "batch_main_analyze_stm32_parallel.sh",
        "batch_main_analyze_nxp_parallel.sh",
        "python main.py run",
        "python main.py build",
        "python main.py analyze",
        "python main.py dump-replacements",
        "python main.py classify-stats",
    ]
    demo_re = re.compile(r"(testcases/server/[A-Za-z0-9_./-]+)")
    rows: List[Dict[str, str]] = []
    for line in out.splitlines()[1:]:
        s = line.strip()
        if not s:
            continue
        if not any(p in s for p in patterns):
            continue
        parts = s.split(None, 3)
        if len(parts) < 4:
            continue
        pid, ppid, etime, cmd = parts
        demo = ""
        m = demo_re.search(cmd)
        if m:
            demo = m.group(1)
        rows.append({"pid": pid, "ppid": ppid, "etime": etime, "demo": demo, "cmd": cmd})
    return rows


def print_checks(root: Path, selected_platform_names: List[str]) -> None:
    print("\n=== preflight checks ===")
    demo_dirs = discover_demo_dirs(root, selected_platform_names)
    if not demo_dirs:
        print("No testcase dirs found for selected platforms.")
        return

    statuses = []
    for demo in demo_dirs:
        cfg = demo / "lcmhal_config.yml"
        db_path = parse_db_path_from_config(cfg)
        if not db_path:
            statuses.append(
                {
                    "demo": str(demo.relative_to(root)),
                    "db_path": "",
                    "db_exists": False,
                    "src_zip": False,
                    "tmp_dir": False,
                    "common_info": False,
                    "driver_info": False,
                    "mmio_info": False,
                    "ai_log_dir": False,
                    "classify_count": 0,
                    "replacement_count": 0,
                    "config_error": True,
                }
            )
            continue
        st = check_demo_cache_status(demo, db_path)
        st["demo"] = str(demo.relative_to(root))
        st["config_error"] = False
        statuses.append(st)

    # 1) CodeQL/collector cache summary
    ready_all = [
        s
        for s in statuses
        if s.get("db_exists")
        and s.get("src_zip")
        and s.get("common_info")
        and s.get("driver_info")
        and s.get("mmio_info")
    ]
    print("\n[1] CodeQL & collector cache")
    print(f"- demos_total={len(statuses)}")
    print(f"- full_cache_ready={len(ready_all)}")
    missing = [s for s in statuses if s not in ready_all]
    if missing:
        print("- missing_examples:")
        for s in missing[:12]:
            miss_keys = []
            for k in ["db_exists", "src_zip", "common_info", "driver_info", "mmio_info"]:
                if not s.get(k):
                    miss_keys.append(k)
            print(f"  - {s['demo']}: missing={','.join(miss_keys)}")

    # 2) ai_log summary
    print("\n[2] AI log coverage (FunctionClassifier / ReplacementUpdate)")
    with_ai = [s for s in statuses if s.get("ai_log_dir")]
    classify_nonzero = [s for s in statuses if int(s.get("classify_count", 0)) > 0]
    replacement_nonzero = [s for s in statuses if int(s.get("replacement_count", 0)) > 0]
    print(f"- ai_log_dir_exists={len(with_ai)}")
    print(f"- classify_logs_nonzero={len(classify_nonzero)}")
    print(f"- replacement_logs_nonzero={len(replacement_nonzero)}")
    # 列出缺失者
    miss_ai = [s for s in statuses if int(s.get("classify_count", 0)) == 0 or int(s.get("replacement_count", 0)) == 0]
    if miss_ai:
        print("- low_coverage_examples:")
        for s in miss_ai[:12]:
            print(
                f"  - {s['demo']}: classify={s.get('classify_count',0)}, replacement={s.get('replacement_count',0)}"
            )

    # 3) running processes
    rows = get_related_processes()
    print("\n[3] Running related processes")
    print(f"- process_count={len(rows)}")
    if not rows:
        print("  - none")
    else:
        # 按 demo 聚合
        by_demo: Dict[str, int] = defaultdict(int)
        for r in rows:
            key = r["demo"] if r["demo"] else "(non-demo)"
            by_demo[key] += 1
        print("- process_by_demo:")
        for demo, cnt in sorted(by_demo.items(), key=lambda x: (-x[1], x[0]))[:20]:
            print(f"  - {demo}: {cnt}")
        print("- top_processes:")
        for r in rows[:20]:
            print(f"  - pid={r['pid']} etime={r['etime']} demo={r['demo'] or '-'} cmd={r['cmd']}")


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    state_path = root / "run" / "batch_main_analyze_adaptive_state.json"
    state = load_state(state_path)

    selected: List[PlatformConfig] = []
    for name in args.platforms:
        if name not in PLATFORMS:
            print(f"[warn] unknown platform skipped: {name}")
            continue
        selected.append(PLATFORMS[name])

    if not selected:
        print("No valid platform selected.")
        return 1

    selected_names = [p.name for p in selected]
    if args.check or args.check_only:
        print_checks(root, selected_names)
        if args.check_only:
            return 0

    all_results: List[Tuple[str, int]] = []
    now = datetime.now()
    w = timedelta(minutes=max(1, args.window_minutes))
    prev_start = now - 2 * w
    prev_end = now - w

    for p in selected:
        initial_jobs = state.get(p.name, args.base_jobs)
        initial_jobs = max(args.min_jobs, initial_jobs)
        retries_prev = count_retries_in_window(root / p.log_dir, prev_start, prev_end)
        jobs = calc_degraded_jobs(
            current_jobs=initial_jobs,
            retries_prev_window=retries_prev,
            min_jobs=args.min_jobs,
            high_threshold=args.high_threshold,
            critical_threshold=args.critical_threshold,
        )
        print(
            f"[{p.name}] prev_window_retries={retries_prev}, "
            f"jobs: {initial_jobs} -> {jobs}"
        )

        rc = run_platform(root=root, platform=p, jobs=jobs, main_cmd=args.main_cmd, dry_run=args.dry_run)
        all_results.append((p.name, rc))

        # update persisted jobs for next run
        state[p.name] = jobs
        save_state(state_path, state)

    print("\n=== adaptive summary ===")
    failed = 0
    for name, rc in all_results:
        print(f"- {name}: exit_code={rc}")
        if rc != 0:
            failed += 1
    print(f"state_file: {state_path}")
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
