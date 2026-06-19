#!/usr/bin/env bash
set -euo pipefail

# 并行按 demo 运行：
#   1) python main.py run <demo>                (默认先执行主流程：建库/分析/替换/构建/仿真)
#   2) python main.py dump-replacements <demo>  (收集替换日志)
#   3) python main.py classify-stats <demo> --json --no-lists > <demo>/classify_stats.json
#
# 用法：
#   scripts/batch_main_analyze_zephyr_parallel.sh
#   scripts/batch_main_analyze_zephyr_parallel.sh 6
#   scripts/batch_main_analyze_zephyr_parallel.sh 4 testcases/server/zephyr/stm32/eth_dhcpv4_nucleo_f767zi
#   ZEPHYR_ROOT=testcases/server/zephyr scripts/batch_main_analyze_zephyr_parallel.sh 8
#   MAIN_CMD=build scripts/batch_main_analyze_zephyr_parallel.sh 4   # 先 build 再汇总
#   MAIN_CMD= scripts/batch_main_analyze_zephyr_parallel.sh 4        # 跳过主流程，仅汇总

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

MAX_JOBS="${1:-${LCMHAL_ANALYZE_MAX_CONCURRENT:-3}}"
ONLY_DEMO="${2:-}"
ZEPHYR_ROOT="${ZEPHYR_ROOT:-testcases/server/zephyr}"
LOG_DIR="${LOG_DIR:-run/batch_main_analyze_zephyr_logs}"
MAIN_CMD="${MAIN_CMD:-run}"

if ! [[ "$MAX_JOBS" =~ ^[0-9]+$ ]] || (( MAX_JOBS <= 0 )); then
  echo "MAX_JOBS 无效（$MAX_JOBS），回退为 3"
  MAX_JOBS=3
fi

mkdir -p "$LOG_DIR"

if [[ -n "$ONLY_DEMO" ]]; then
  if [[ -f "$ONLY_DEMO/lcmhal_config.yml" ]]; then
    DEMOS=("$ONLY_DEMO")
  else
    echo "ONLY_DEMO 无效：缺少 lcmhal_config.yml -> $ONLY_DEMO"
    exit 1
  fi
else
  mapfile -t DEMOS < <(find "$ZEPHYR_ROOT" -type f -name "lcmhal_config.yml" | sed 's#/lcmhal_config.yml$##' | sort)
fi

if [[ "${#DEMOS[@]}" -eq 0 ]]; then
  echo "未找到 demo：$ZEPHYR_ROOT 下没有 lcmhal_config.yml"
  exit 1
fi

echo "ROOT_DIR=$ROOT_DIR"
echo "ZEPHYR_ROOT=$ZEPHYR_ROOT"
echo "MAX_JOBS=$MAX_JOBS"
echo "DEMOS=${#DEMOS[@]}"
echo "LOG_DIR=$LOG_DIR"
echo "MAIN_CMD=${MAIN_CMD:-<empty>}"

run_one() {
  local demo="$1"
  local key
  key="$(echo "$demo" | tr '/' '_')"
  local log="$LOG_DIR/${key}.log"

  {
    echo "=== START $demo ==="
    if [[ -n "${MAIN_CMD:-}" ]]; then
      python main.py "$MAIN_CMD" "$demo"
    fi
    python main.py dump-replacements "$demo"
    python main.py classify-stats "$demo" --json --no-lists > "$demo/classify_stats.json"
    echo "=== DONE  $demo ==="
  } >"$log" 2>&1
}

pids=()
for demo in "${DEMOS[@]}"; do
  run_one "$demo" &
  pids+=("$!")
  while (( $(jobs -rp | wc -l) >= MAX_JOBS )); do
    sleep 0.2
  done
done

failed_jobs=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then
    failed_jobs=$((failed_jobs + 1))
  fi
done

echo ""
echo "全部完成。日志目录：$LOG_DIR"
echo "失败任务（如有）："
if ls "$LOG_DIR"/*.log >/dev/null 2>&1 && grep -nE "Traceback|Error:|!!!|failed|FAIL" "$LOG_DIR"/*.log >/dev/null 2>&1; then
  grep -nE "Traceback|Error:|!!!|failed|FAIL" "$LOG_DIR"/*.log || true
else
  echo "  无"
fi

if (( failed_jobs > 0 )); then
  echo "后台任务失败数：$failed_jobs"
  exit 1
fi
