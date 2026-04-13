"""
递归查找包含 lcmhal_config.yml 的 testcase 目录，并读取其中的 db_path（不触发 globs_init）。
"""

from __future__ import annotations

import os
from typing import List, Optional, Tuple

import yaml

CONFIG_FILENAME = "lcmhal_config.yml"

# 加速遍历：跳过常见无关目录
SKIP_SUBDIR_NAMES = frozenset(
    {
        ".git",
        "__pycache__",
        "node_modules",
        ".venv",
        "venv",
        ".mypy_cache",
        ".pytest_cache",
        ".tox",
        "build",
        "dist",
    }
)


def find_testcase_dirs_under_root(root: str) -> List[str]:
    """
    递归遍历 root，返回所有「直接包含 lcmhal_config.yml」的目录绝对路径，按路径排序去重。

    规则：
    - 若某目录已命中 lcmhal_config.yml，则该目录视为一个 testcase 根目录；
    - 命中后不再继续向其子目录递归（避免重复/嵌套 testcase 造成重复统计）。
    """
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        return []
    found: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        dirnames[:] = [
            d for d in dirnames if d not in SKIP_SUBDIR_NAMES and not d.startswith(".")
        ]
        if CONFIG_FILENAME in filenames:
            found.append(os.path.abspath(dirpath))
            # 命中后不再递归该目录的子目录
            dirnames[:] = []
    return sorted(set(found))


def resolve_classify_stats_targets(user_path: str) -> Tuple[List[str], str]:
    """
    根据用户传入的路径，得到要统计的 testcase 目录列表与扫描模式。

    - 若路径为文件，则取其所在目录。
    - 若该目录下存在 lcmhal_config.yml：单 testcase，返回 [该目录]。
    - 否则：视为根目录，递归查找所有含 lcmhal_config.yml 的子目录（批量）。

    Returns:
        (testcase_dirs, mode_label)  mode_label 为 "single" / "batch" / "invalid"
    """
    if os.path.isfile(user_path):
        start = os.path.abspath(os.path.dirname(user_path))
    else:
        start = os.path.abspath(user_path)

    if not os.path.isdir(start):
        return [], "invalid"

    cfg = os.path.join(start, CONFIG_FILENAME)
    if os.path.isfile(cfg):
        return [start], "single"

    discovered = find_testcase_dirs_under_root(start)
    return discovered, "batch"


def read_db_path_from_testcase_dir(testcase_dir: str) -> Tuple[Optional[str], Optional[str]]:
    """
    从 testcase 目录的 lcmhal_config.yml 读取 db_path。

    Returns:
        (db_path, error_message) 成功时 error_message 为 None。
    """
    cfg_path = os.path.join(testcase_dir, CONFIG_FILENAME)
    if not os.path.isfile(cfg_path):
        return None, f"missing {CONFIG_FILENAME}"
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except Exception as e:
        return None, str(e)
    db = data.get("db_path")
    if not db or not isinstance(db, str):
        return None, "db_path missing or invalid in lcmhal_config.yml"
    return os.path.expanduser(db.strip()), None

