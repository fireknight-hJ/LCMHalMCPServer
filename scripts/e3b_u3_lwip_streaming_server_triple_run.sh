#!/usr/bin/env bash
# E3b U3：STM32Cube「LwIP Streaming Server」三连跑（独立 LLM session + 可归档 isolated_db）
#
# 仓库 testcase：testcases/server/stm32/LwIP_StreamingServer
#
# 用法（仓库根目录）：
#   bash scripts/e3b_u3_lwip_streaming_server_triple_run.sh
#
# 依赖：
#   - lcmhal_config.yml 中的 db_path / proj_path 与本脚本变量一致（若路径不同请改下方变量）
#   - proj_path 为 git 仓库，以便 run 间 git reset --hard 恢复 OEM 源码
#   - python main.py run 可用（含 config.globs）
#
set -euo pipefail

if [[ "${E3B_U3_CONFIRM:-}" != "yes" ]]; then
  echo "为避免误清空 CodeQL DB 下的 lcmhal_ai_log，本脚本需显式确认。" >&2
  echo "若已备份或接受清空日志，请执行：" >&2
  echo "  export E3B_U3_CONFIRM=yes" >&2
  echo "  bash scripts/e3b_u3_lwip_streaming_server_triple_run.sh" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TC="${TC:-testcases/server/stm32/LwIP_StreamingServer}"
DB="${DB:-/home/haojie/workspace/dbs_server/DATABASE_LwIP_StreamingServer}"
PROJ="${PROJ:-/home/haojie/posixGen_Demos/LwIP_StreamingServer}"
PYTHON="${PYTHON:-python3}"

STAMP="$(date +%Y%m%d_%H%M%S)"
BATCH="${BATCH:-$ROOT/runs/e3b_uncertainty/${STAMP}_U3_LwIP_StreamingServer}"
BASELINE="$BATCH/db_baseline_oem"

mkdir -p "$BATCH/logs" "$BATCH/isolated_db" "$BATCH/artifacts"

echo "[e3b-u3-stream] BATCH=$BATCH"

if [[ ! -d "$ROOT/$TC" ]]; then
  echo "错误: testcase 不存在: $ROOT/$TC" >&2
  exit 1
fi
if [[ ! -d "$DB" ]]; then
  echo "错误: CodeQL DB 目录不存在: $DB" >&2
  exit 1
fi
if [[ ! -d "$PROJ" ]]; then
  echo "错误: 工程源码目录不存在: $PROJ" >&2
  exit 1
fi

cd "$ROOT"

mirror_replace() {
  local src="$1" dst="$2"
  [[ -d "$src" ]] || {
    echo "[e3b-u3-stream] mirror_replace: 源目录不存在: $src" >&2
    return 1
  }
  rm -rf "$dst"
  mkdir -p "$dst"
  cp -a "${src}/." "${dst}/"
}

echo "[e3b-u3-stream] 清空首轮 ai_log 并制作 OEM 快照（CodeQL DB + src.zip 等）…"
"$PYTHON" main.py clean "$TC" --all 2>/dev/null || true
mkdir -p "$(dirname "$BASELINE")"
mirror_replace "$DB" "$BASELINE"

restore_oem() {
  echo "[e3b-u3-stream] 从快照恢复 DB → $DB"
  mirror_replace "$BASELINE" "$DB"
  echo "[e3b-u3-stream] git reset 工程: $PROJ"
  git -C "$PROJ" reset --hard HEAD
  git -C "$PROJ" clean -fd
  "$PYTHON" main.py clean "$TC" --all 2>/dev/null || true
}

for i in 1 2 3; do
  echo "==================== U3 run $i / 3 ===================="
  restore_oem
  set +e
  "$PYTHON" main.py run "$TC" --llm-usage-log 2>&1 | tee "$BATCH/logs/U3_run${i}.log"
  ec=$?
  set -e
  echo "" | tee -a "$BATCH/logs/U3_run${i}.log"
  echo "[e3b-u3-stream] main_exit_code=$ec" | tee -a "$BATCH/logs/U3_run${i}.log"

  mkdir -p "$BATCH/isolated_db"
  mirror_replace "$DB" "$BATCH/isolated_db/U3_run${i}"

  ad="$BATCH/artifacts/U3_run${i}"
  mkdir -p "$ad"
  {
    echo "firmware_id=U3 run=$i"
    echo "testcase_rel_path=$TC"
    echo "db_path_canonical=$DB"
    echo "db_path_used=$BATCH/isolated_db/U3_run${i}"
    echo "main_exit_code=$ec"
  } >"$ad/e3b_run_manifest.txt"
done

echo "[e3b-u3-stream] 完成。归档："
echo "  logs:       $BATCH/logs/U3_run{1,2,3}.log"
echo "  isolated_db $BATCH/isolated_db/U3_run{1,2,3}"
echo ""
echo "生成 U3 三行汇总 TSV（示例）："
echo "  $PYTHON tools/e3b_batch_replacement_stats.py \\"
echo "    --isolated-db-root $BATCH/isolated_db \\"
echo "    --summary-tsv doc/experiments/E3b-U3_LwIP_StreamingServer_${STAMP}_实测汇总.tsv"
echo ""
echo "可选：手工追加 run_log.tsv（列格式见 runs/e3b_uncertainty/20260508_045825/run_log.tsv）。"
