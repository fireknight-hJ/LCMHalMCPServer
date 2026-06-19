#!/usr/bin/env bash
# E3b：5 个 testcase × 3 次 run，仅调用 python main.py run；输出 runs/e3b_uncertainty/<stamp>/。
set -euo pipefail

REPO_ROOT="${LCMHAL_REPO_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
cd "$REPO_ROOT"

RUNS_ROOT="${REPO_ROOT}/runs/e3b_uncertainty"
STAMP="$(date +%Y%m%d_%H%M%S)"
BATCH_DIR="${RUNS_ROOT}/${STAMP}"
mkdir -p "${BATCH_DIR}/logs" "${BATCH_DIR}/artifacts"

# id:testcase_rel_path_from_repo_root:db_path（须与本机 lcmhal_config.yml 一致）
RUNS_LIST=(
  "U1:testcases/server/nxp/NXP_LwIP_BareMetal:/home/haojie/workspace/dbs_server/DATABASE_NXP_LwIP_BareMetal"
  "U2:testcases/server/nxp/NXP_I2C_BareMetal:/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal"
  "U3:testcases/server/rtthread/stm32f401-st-nucleo/eth:/home/haojie/workspace/dbs_server/DATABASE_RTThread_stm32f401_eth"
  "U4:testcases/server/stm32/UART_Hyperterminal_IT:/home/haojie/workspace/dbs_server/DATABASE_UART_Hyperterminal_IT"
  "U5:testcases/server/rtthread/imxrt1052-nxp-evk/base:/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_base"
)

export LCMHAL_LLM_USAGE_LOG=1

echo -e "firmware_id\ttestcase_rel_path\tdb_path\trun_idx\texit_code\twall_sec\tsession_id\tllm_usage_line\tlog_file\tartifact_dir" \
  >"${BATCH_DIR}/run_log.tsv"

_extract_session_id() {
  local log="$1"
  if [[ ! -f "$log" ]]; then
    echo ""
    return
  fi
  # stderr 常见格式: Session ID: <uuid>
  sed -n 's/.*Session ID:[[:space:]]*\([0-9a-fA-F-]\{36\}\).*/\1/p' "$log" | tail -n 1 || true
}

for entry in "${RUNS_LIST[@]}"; do
  FID="${entry%%:*}"
  rest="${entry#*:}"
  TCPATH="${rest%%:*}"
  DBPATH="${rest##*:}"

  for r in 1 2 3; do
    LOG="${BATCH_DIR}/logs/${FID}_run${r}.log"
    ART="${BATCH_DIR}/artifacts/${FID}_run${r}"
    mkdir -p "$ART"

    START="$(date +%s)"
    set +e
    python main.py run "$TCPATH" >"$LOG" 2>&1
    EC=$?
    set -e
    END="$(date +%s)"
    WALL=$((END - START))

    SID="$(_extract_session_id "$LOG")"
    LLM_LINE=""
    if grep -Fq '[LLM Usage]' "$LOG" 2>/dev/null; then
      LLM_LINE="$(grep -F '[LLM Usage]' "$LOG" | tail -n 1 || true)"
    fi
    LLM_SAFE="$(printf '%s' "$LLM_LINE" | tr '\t' ' ')"

    SRC_DBG="${REPO_ROOT}/${TCPATH}/emulate/debug_output"
    if [[ -d "$SRC_DBG" ]]; then
      cp -a "$SRC_DBG" "${ART}/debug_output"
    fi

    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$FID" "$TCPATH" "$DBPATH" "$r" "$EC" "$WALL" "${SID}" "${LLM_SAFE}" \
      "$LOG" "$ART" >>"${BATCH_DIR}/run_log.tsv"
  done
done

echo "E3b batch finished: ${BATCH_DIR}"
echo "Next: python scripts/e3b_collect_metrics.py --batch-dir ${BATCH_DIR}"
