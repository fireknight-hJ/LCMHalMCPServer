#!/usr/bin/env python3
"""Write BOARD_BootClockRUN OEM + replacement snippets for doc/experiments/snippets/."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "runs/e3b_uncertainty/20260508_045825/isolated_db"
OUT = ROOT / "doc/experiments/snippets"
OUT.mkdir(parents=True, exist_ok=True)


def get_oem() -> str:
    p = DB / "U5_run2/lcmhal_ai_log/function_classify_BOARD_BootClockRUN_20260508051417.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    for m in d["messages"]:
        c = m.get("content") or ""
        if m.get("type") == "tool" and m.get("name") == "GetFunctionInfo" and "function_content='" in c:
            s = c.split("function_content='", 1)[1].split("', function_content_in_lines", 1)[0]
            return s.encode("utf-8").decode("unicode_escape")
    raise RuntimeError("OEM not found")


def main() -> None:
    oem = get_oem()
    (OUT / "U5_BOARD_oem_BOARD_BootClockRUN_head50.c").write_text(
        "\n".join(oem.split("\n")[:50]) + "\n", encoding="utf-8"
    )

    r3 = json.loads(
        (DB / "U5_run3/lcmhal_ai_log/function_classify_BOARD_BootClockRUN_20260508053546.json").read_text(
            encoding="utf-8"
        )
    )["final_response"]["function_replacement"]
    (OUT / "U5_run3_BOARD_BootClockRUN_replace_full.c").write_text(r3 + "\n", encoding="utf-8")

    r2 = json.loads(
        (DB / "U5_run2/lcmhal_ai_log/function_fix_BOARD_BootClockRUN_20260508052822.json").read_text(
            encoding="utf-8"
        )
    )["final_response"]["replacement_code"]
    (OUT / "U5_run2_BOARD_BootClockRUN_function_fix_replace_full.c").write_text(r2 + "\n", encoding="utf-8")

    r1 = json.loads(
        (DB / "U5_run1/lcmhal_ai_log/replacement_update_BOARD_BootClockRUN_20260508050956.json").read_text(
            encoding="utf-8"
        )
    )["replacement_code"]
    (OUT / "U5_run1_BOARD_BootClockRUN_replacement_update_v1_full.c").write_text(r1 + "\n", encoding="utf-8")

    r1b = json.loads(
        (DB / "U5_run1/lcmhal_ai_log/replacement_update_BOARD_BootClockRUN_20260508051151.json").read_text(
            encoding="utf-8"
        )
    )["replacement_code"]
    (OUT / "U5_run1_BOARD_BootClockRUN_replacement_update_v2_full.c").write_text(r1b + "\n", encoding="utf-8")

    ru2 = json.loads(
        (DB / "U5_run2/lcmhal_ai_log/replacement_update_BOARD_BootClockRUN_20260508052702.json").read_text(
            encoding="utf-8"
        )
    )["replacement_code"]
    (OUT / "U5_run2_BOARD_BootClockRUN_replacement_update_full.c").write_text(ru2 + "\n", encoding="utf-8")

    print("wrote:", "\n  ".join(str(p.relative_to(ROOT)) for p in sorted(OUT.glob("U5*.c"))))


if __name__ == "__main__":
    main()
