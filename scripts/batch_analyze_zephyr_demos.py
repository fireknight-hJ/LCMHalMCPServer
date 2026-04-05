#!/usr/bin/env python3
"""
按 demo 逐个批量跑 FunctionClassifier（data_manager.load_mmio_functions）。

- 扫描 `testcases/server/zephyr/**/lcmhal_config.yml`，每个目录视为一个 Zephyr demo。
- 已有 `lcmhal_ai_log/function_classify_<func>_*.json` 的函数会走缓存，不重复调 LLM。
- 并发由环境变量 `LCMHAL_ANALYZE_MAX_CONCURRENT` 控制（与 main/build 一致；未设置时 analyzer 默认 8）。

用法（在仓库根目录）:

  python scripts/batch_analyze_zephyr_demos.py

  # 只跑其中一个 demo 目录
  python scripts/batch_analyze_zephyr_demos.py --only testcases/server/zephyr/stm32/eth_dhcpv4_nucleo_f767zi

  # 仅列出将运行的目录，不执行
  python scripts/batch_analyze_zephyr_demos.py --dry-run

  # 限制单 demo 内 Classify 并发（示例）
  LCMHAL_ANALYZE_MAX_CONCURRENT=6 python scripts/batch_analyze_zephyr_demos.py

日志：每个 demo 打印 MMIO 函数数与完成后 mmio_info_list 条数；失败不中断，最后汇总。
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
import traceback
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _discover_demo_dirs(zephyr_root: Path) -> list[Path]:
    if not zephyr_root.is_dir():
        return []
    found: list[Path] = []
    for p in zephyr_root.rglob("lcmhal_config.yml"):
        found.append(p.parent)
    return sorted(set(found), key=lambda x: str(x))


async def _analyze_one_demo(demo_dir: Path) -> dict:
    """对单个 testcase 目录执行 load_mmio_functions，返回结果摘要。"""
    import config.globs as globs
    from config.globs import load_config_from_yaml, globs_init
    from core.data_manager import data_manager
    from tools.collector.collector import get_mmio_func_list, register_db

    rel = demo_dir
    try:
        rel = demo_dir.relative_to(_repo_root())
    except ValueError:
        pass

    out: dict = {"path": str(rel), "ok": False, "mmio_target": 0, "mmio_loaded": 0, "error": None}

    config = load_config_from_yaml(str(demo_dir))
    globs_init(config)
    register_db(globs.db_path)
    n = len(get_mmio_func_list(globs.db_path))
    out["mmio_target"] = n
    print(f"\n=== [{rel}]  MMIO 函数数(目标): {n} ===", flush=True)

    await data_manager.load_mmio_functions()
    loaded = len(data_manager.mmio_info_list)
    out["mmio_loaded"] = loaded
    out["ok"] = True
    print(f"=== [{rel}]  完成 mmio_info_list: {loaded} ===", flush=True)
    if n > 0 and loaded < n:
        print(
            f"提示: 目标 {n} 个 MMIO 函数，仅载入 {loaded} 条（可能部分超时；重跑同一脚本会保留缓存并补跑缺失）",
            flush=True,
        )
    return out


async def _main_async(args: argparse.Namespace) -> int:
    root = _repo_root()
    os.chdir(root)
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    zephyr_root = Path(args.zephyr_root).resolve()
    if args.only:
        demo_dirs = [Path(args.only).resolve()]
        if not (demo_dirs[0] / "lcmhal_config.yml").is_file():
            print(f"错误: 未找到 lcmhal_config.yml: {demo_dirs[0]}", file=sys.stderr)
            return 1
    else:
        demo_dirs = _discover_demo_dirs(zephyr_root)

    if not demo_dirs:
        print(f"未找到任何 demo（在 {zephyr_root} 下搜索 lcmhal_config.yml）", file=sys.stderr)
        return 1

    print(
        f"仓库根: {root}\n"
        f"Zephyr 根: {zephyr_root}\n"
        f"将处理 {len(demo_dirs)} 个 demo\n"
        f"LCMHAL_ANALYZE_MAX_CONCURRENT={os.environ.get('LCMHAL_ANALYZE_MAX_CONCURRENT', '(默认见 analyzer)')}",
        flush=True,
    )

    if args.dry_run:
        for d in demo_dirs:
            try:
                r = d.relative_to(root)
            except ValueError:
                r = d
            print(f"  [dry-run] {r}")
        return 0

    results: list[dict] = []
    for d in demo_dirs:
        try:
            results.append(await _analyze_one_demo(d))
        except Exception as e:
            try:
                rel = d.relative_to(root)
            except ValueError:
                rel = d
            print(f"!!! [{rel}] 异常: {e}", flush=True)
            traceback.print_exc()
            results.append(
                {
                    "path": str(rel),
                    "ok": False,
                    "mmio_target": 0,
                    "mmio_loaded": 0,
                    "error": str(e),
                }
            )

    ok_n = sum(1 for r in results if r.get("ok"))
    print(
        f"\n--- 汇总 ---\n成功(有结果或目标为0): {ok_n}/{len(results)}",
        flush=True,
    )
    for r in results:
        err = r.get("error")
        flag = "OK" if r.get("ok") and not err else "FAIL"
        print(
            f"  [{flag}] {r['path']}  target={r.get('mmio_target')} loaded={r.get('mmio_loaded')}"
            + (f" err={err}" if err else ""),
            flush=True,
        )

    return 0 if ok_n == len(results) else 1


def main() -> None:
    parser = argparse.ArgumentParser(description="批量对 Zephyr 下各 demo 运行 load_mmio_functions（FunctionClassifier）")
    parser.add_argument(
        "--zephyr-root",
        default="testcases/server/zephyr",
        help="Zephyr testcase 根目录（相对仓库根或绝对路径）",
    )
    parser.add_argument(
        "--only",
        default=None,
        help="只处理该 demo 目录（须含 lcmhal_config.yml），例如 testcases/server/zephyr/stm32/eth_dhcpv4_nucleo_f767zi",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只列出将运行的 demo 路径，不执行分析",
    )
    args = parser.parse_args()
    zr = Path(args.zephyr_root)
    if not zr.is_absolute():
        args.zephyr_root = str(_repo_root() / zr)
    if args.only and not Path(args.only).is_absolute():
        args.only = str(_repo_root() / args.only)

    raise SystemExit(asyncio.run(_main_async(args)))


if __name__ == "__main__":
    main()
