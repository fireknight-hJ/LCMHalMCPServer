# E3b LLM 输出不确定性实验 — 执行手册

本文档是 [E3b-LLM不确定性实验方案.md](./E3b-LLM不确定性实验方案.md) 在 **LCMHalMCP 仓库内** 的可操作版本：约定 testcase 路径、`python main.py run` 批跑方式、环境变量、日志与指标落点、失败保留与论文表格衔接。

**约定**：所有完整替换+仿真流程必须通过项目入口 `python main.py run <TESTCASE_DIR>` 执行，不绕过 `main.py` 直接调用内部工具（与 `.cursor/skills/run_lcmhal_demo/SKILL.md` 一致）。

---

## 1. 目的与控制变量

与方案第一章、第二章一致：仅在每次运行使用 **新的进程（因而新的 LLM session / session_id）**；固件源码版本、CodeQL 规则、替换策略、`lcmhal_config.yml` 除路径外的逻辑配置、仿真环境与论文 5.4 中定义的「关键节点」集合保持不变。

---

## 2. 环境清单

| 项目 | 说明 |
|------|------|
| 工作副本 | 仓库根目录：`lcmhalmcp`，建议在固定 commit 上贴标签（如 `e3b-baseline`）便于论文追溯 |
| LLM | 与主实验一致（方案中为 DeepSeek V3.2）；具体密钥与模型名见 `config/llm_config.py`（该文件通常不入库，本地配置） |
| CodeQL / 构建链 | 与主实验一致 |
| Python | 与仓库 `README` / CI 要求一致 |
| 词元日志 | 单次进程内开启：`export LCMHAL_LLM_USAGE_LOG=1`（见 `config/globs.py` 中 `LCMHAL_LLM_USAGE_LOG`）；或在对应 testcase 的 `lcmhal_config.yml` 中设置 `llm_usage_log_enable: true` |
| API 限流 | 实验前确认不会因限流中断长会话（方案第七节） |

---

## 3. Testcase 与本仓库路径、`db_path`

以下为当前仓库内 `lcmhal_config.yml` 中的路径（若本机路径不同，请先修正 YAML 再跑）。

| 编号 | `python main.py run` 参数（相对仓库根目录） | `db_path`（CodeQL DB / ai_log 根） |
|------|---------------------------------------------|-----------------------------------|
| U1 | `testcases/server/nxp/NXP_LwIP_BareMetal` | `/home/haojie/workspace/dbs_server/DATABASE_NXP_LwIP_BareMetal` |
| U2 | `testcases/server/nxp/NXP_I2C_BareMetal` | `/home/haojie/workspace/dbs_server/DATABASE_NXP_I2C_BareMetal` |
| U3 | `testcases/server/rtthread/stm32f401-st-nucleo/eth` | `/home/haojie/workspace/dbs_server/DATABASE_RTThread_stm32f401_eth` |
| U4 | `testcases/server/stm32/UART_Hyperterminal_IT` | `/home/haojie/workspace/dbs_server/DATABASE_UART_Hyperterminal_IT` |
| U5 | `testcases/server/rtthread/imxrt1052-nxp-evk/base`（GPIO 类代表，与论文对齐选用 base demo） | `/home/haojie/workspace/dbs_server/DATABASE_RTThread_imxrt1052_base` |

**运行前检查**：

- 各 `db_path` 目录存在且与主实验为同一数据库版本。
- 各 `src_path` / `proj_path` 存在；**U4** 依赖 `posixGen_Demos` 等本机路径，缺失会导致构建/分析失败。

---

## 4. 独立 Session 与词元汇总

- 每执行一次 `python main.py run` 即新进程，会在该 testcase 的 `db_path` 下 `lcmhal_ai_log/` 生成新的 `session_<uuid>_<timestamp>.json`。
- 进程结束且 `ai_log` 正常 finalize 时，标准错误会打印类似 `[LLM Usage] invokes=... prompt_tokens=...` 行（需开启 `LCMHAL_LLM_USAGE_LOG` 或 YAML 中 `llm_usage_log_enable`）。

---

## 5. 单次标准命令

在仓库根目录：

```bash
cd /home/haojie/workspace/lcmhalmcp
export LCMHAL_LLM_USAGE_LOG=1
python main.py run testcases/server/nxp/NXP_LwIP_BareMetal
```

将最后一行路径替换为第二节表中对应 testcase 即可。

---

## 6. 批跑脚本（15 次）

使用仓库提供的批处理脚本（仅编排与记账，内部仍调用 `main.py run`）：

```bash
# 默认：5 个固件 × 3 次，输出到 runs/e3b_uncertainty/<时间戳>/
./scripts/e3b_uncertainty_batch.sh

# 若已设置 LCMHAL_REPO_ROOT，可显式指定仓库根目录
LCMHAL_REPO_ROOT=/path/to/lcmhalmcp ./scripts/e3b_uncertainty_batch.sh
```

脚本行为摘要：

- 设置 `LCMHAL_LLM_USAGE_LOG=1`。
- 固定顺序：U1 Run1–3 → U2 Run1–3 → … → U5 Run1–3（顺序不作实验因子；若需随机顺序，可自行改脚本并记录 seed）。
- 每次运行将完整标准输出+标准错误写入 `logs/U{x}_run{y}.log`。
- 生成 `run_log.tsv`：含 `session_id`、退出码、墙钟时间、以及从日志中匹配到的 `[LLM Usage]` 行（若存在）。
- 若存在 `emulate/debug_output/`，在每次 run 后将其复制到 `artifacts/U{x}_run{y}/debug_output/`，避免后续 run 覆盖导致无法对比（与计划文档第 9 节一致）。

**注意**：`testcases/.../emulate/` 在 `.gitignore` 中，但批跑时仍会在工作区内生成；artifacts 用于批次留存。

---

## 7. 批跑后汇总（session 词元）

对某批次目录执行：

```bash
python scripts/e3b_collect_metrics.py --batch-dir runs/e3b_uncertainty/<批次目录名>
```

会从 `run_log.tsv` 读取 `session_id` 与 `db_path`，加载 `{db_path}/lcmhal_ai_log/session_<session_id>_*.json`，提取 `llm_usage_summary`（若该次 run 已 finalize 并写入），在标准输出打印 TSV，并可选写入 `llm_summary.tsv`。

若某次未记录 `llm_usage_summary`（例如未开启词元记录或 run 异常退出），脚本在输出中对应列为空，需结合该次 `logs/*.log` 人工补录。

---

## 8. 指标来源与论文表格填法

| 方案指标 | 本仓库中的建议来源 |
|----------|-------------------|
| 驱动函数识别数、分类与替换相关统计 | 每次完整 run 后，在 testcase 或 DB 侧通过 `classify_stats` 相关流程与 `classify_stats_output.json`、以及 `lcmhal_ai_log` 中 `function_classify_*` 等（见 `main.py` 子命令与 `utils/classify_log_stats.py`）。**识别数**若来自 CodeQL 阶段，应以与 5.4 节定义一致为准。 |
| 替换代码生成数、迭代/修复轮次 | 以该次 run 的 session 日志与主流程打印为准；若论文中「迭代数」与 `main.py` 中 `max_emulate_fault_rounds` 等内部计数不完全一致，在论文中明确定义后再从日志中对应字段或人工统计。 |
| 关键节点命中率、通过/失败 | **论文 5.4 自定义**；需从各固件配置中定位「关键节点」定义，并对照当次 `artifacts/.../debug_output/lcmhal.txt` 等仿真输出核对。若尚无自动解析脚本，本实验保留**人工判定列**于结果表。 |
| 仿真是否成功（工程意义） | 参考 `.cursor/skills/run_lcmhal_demo/SKILL.md`：死循环、异常、预期 MMIO/函数轨迹等。与「关键节点 100%」可并列记录。 |
| LLM 词元、墙钟时间 | `LCMHAL_LLM_USAGE_LOG` + session 元数据 + 批跑 TSV；`e3b_collect_metrics.py` 辅助词元列。 |

**失败样本**：按方案第七节，不丢弃；在 `run_log.tsv` 与论文表中标注失败原因（分类错误 / 替换质量 / 闭环未收敛 / 仿真异常等）。

---

## 9. 15 次运行顺序与结果表模板

建议在论文主表（方案 4.1 节）中增加列：**批次目录名**、**session 日志文件名**、**备注**。

批跑完成后，`run_log.tsv` 与 `llm_summary.tsv`（若生成）可作为填表草稿；最终「识别数 / 替换数 / 迭代数 / 关键节点命中率」仍以你与 5.4 节一致的统计口径为准。

---

## 10. 与论文 LaTeX 衔接

成稿时将分析段落写入 `body/chap05_experiment.tex` 中规划的小节（如「LLM 输出稳定性分析」）；本文档与 `runs/e3b_uncertainty/` 下批次目录一并作为可复现材料保存。

---

## 11. 可选深化（方案 3.2 节）

对 U1、U2 可增加：

- **分类一致性**：对比三次 run 的 `function_classify_*` 日志中同一函数的 `function_type`。
- **替换代码差异**：在 `{db_path}/lcmhal_ai_log/` 下针对同一函数名的 `replacement_update_*` 日志做 diff。

步骤与工具命令可按需在后续实验中补充到本文档附录。
