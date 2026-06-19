# LCMHalMCP

LCMHalMCP 是一个面向嵌入式 HAL/驱动代码的自动化分析、替换、编译验证与动态仿真反馈框架。项目把 CodeQL 静态分析、MCP 工具接口、LangGraph/LLM 多智能体、源码替换、交叉编译和 fuzzemu/Unicorn 仿真串成闭环，用来把依赖真实硬件寄存器和外设行为的固件 demo 转换成可以在服务器上构建、模拟、诊断和迭代修复的测试对象。

当前主线流程可以概括为：

```text
testcase/lcmhal_config.yml
  -> build.sh / CodeQL database
  -> Collector 静态收集函数、调用、结构体、驱动、MMIO 信息
  -> Analyzer Agent 对候选函数分类并生成替换
  -> VerifyReplacement / BuilderFixer 做 rubric 与编译验证
  -> Replacer 应用替换并重新构建 ELF/BIN
  -> Emulator 生成 fuzzemu 配置并运行模拟器
  -> Fixer / Builder 根据动态反馈继续修复
```

## 适用范围

- 芯片/平台：STM32、NXP i.MX RT、Zephyr 支持的 STM32/NXP/Atmel 板卡，项目中也预留 nRF、Ambiq 等扩展目标。
- OS/运行时：裸机、FreeRTOS、RT-Thread、Zephyr。
- 外设/组件：UART、I2C、ETH/LwIP、Flash/FATFS、BLE，以及由 CodeQL 查询识别出的 MMIO/driver/buffer 函数。
- 典型目标：将直接访问 MMIO、外设状态、DMA、PHY、NVIC/SysTick 或阻塞轮询的函数替换为可模拟的 HAL_BE_* 行为，并通过构建和仿真反馈确认替换是否可用。

## 目录导航

```text
lcmhalmcp/
├── main.py                  # CLI 主入口，编排 run/build/emulate/recover/clean/analyze/dump/classify-stats
├── server.py                # 顶层 FastMCP/CodeQL 查询服务入口
├── codeql_mcp.py            # CodeQL query-server2 客户端封装
├── agents/                  # LangGraph/LLM 智能体：Analyzer、Builder、BuilderFixer、Fixer、EmulatorRunner
├── tools/                   # 可复用工具模块：collector、builder、replacer、emulator
├── core/                    # 跨模块状态管理，主要是 DataManager
├── config/                  # testcase/global 配置、LLM 配置、CodeQL collector 路径配置
├── models/                  # Pydantic/dataclass 数据模型
├── prompts/                 # 各智能体提示词与代码生成规则
├── queries/                 # CodeQL 查询与 qll 库，按 common/driver/mmio/tests 组织
├── utils/                   # DB zip 读取、日志、缓存、rubric、源码路径映射、统计等工具函数
├── fuzzemu/                 # 基于 Unicorn/fuzzemu 的固件模拟执行子项目
├── testcases/               # server/macbook/zephyr 等测试用例矩阵
├── scripts/                 # 批处理、实验统计、消融与不确定性实验脚本
├── doc/                     # 设计、实验、case study 与论文材料
└── case_study/              # 具体替换/修复案例
```

更详细的模块设计见：

- `doc/design/architecture.md`
- `doc/design/modules.md`
- `doc/design/workflows.md`
- `doc/design/testcases.md`
- `doc/design/reusable-capabilities.md`

## Testcase 约定

每个可运行 testcase 目录需要包含：

- `build.sh`：构建脚本。职责是构建目标项目并生成 ELF，然后把生成的 ELF 移动/复制到 testcase 的 `emulate/output.elf`。
- `clear.sh`：清理脚本。删除构建缓存、ELF、obj 等中间产物，避免上一次构建影响下一次。
- `lcmhal_config.yml`：LCMHalMCP 配置文件，至少包含：
  - `script_path`：testcase 脚本目录
  - `db_path`：CodeQL 数据库目录
  - `src_path`：真实源码目录
  - `proj_path`：工程根目录

Zephyr 用例见 `testcases/server/zephyr/README.md`。Zephyr testcase 也遵循上述三文件约定，但构建在 Zephyr workspace 根目录通过 `west build` 完成：`src_path` 指向 workspace 内 `zephyr` 源码目录，`proj_path` 指向 workspace 根目录。默认 Zephyr workspace 为 `/home/haojie/zephyrproject`，可用环境变量覆盖：

```shell
export ZEPHYR_PROJECT=/path/to/your/zephyrproject
```

## 基本命令

完整流程：

```shell
python main.py run testcases/server/stm32/LwIP_StreamingServer
```

只执行静态分析、替换、构建和模拟配置生成，不进入 Emulator Runner 动态闭环：

```shell
python main.py build testcases/server/stm32/LwIP_StreamingServer
```

只运行已生成的模拟器配置：

```shell
python main.py emulate testcases/server/stm32/LwIP_StreamingServer
```

恢复 testcase 源码文件：

```shell
python main.py recover testcases/server/stm32/LwIP_StreamingServer
```

清理某个函数的分析/替换日志：

```shell
python main.py clean testcases/server/stm32/LwIP_StreamingServer \
  --func-name HAL_UART_Init --type all --recover
```

单函数分析：

```shell
python main.py analyze testcases/server/stm32/LwIP_StreamingServer \
  --func-name HAL_UART_Init
```

导出替换日志：

```shell
python main.py dump-replacements testcases/server/stm32/LwIP_StreamingServer
```

统计 FunctionClassifier 分类结果：

```shell
python main.py classify-stats testcases/server/stm32
python main.py classify-stats testcases/server/stm32 --json --no-lists
```

## 批处理脚本

### 1. 平台批处理脚本

四个平台脚本分别是：

- `scripts/batch_main_analyze_zephyr_parallel.sh`
- `scripts/batch_main_analyze_rtthread_parallel.sh`
- `scripts/batch_main_analyze_stm32_parallel.sh`
- `scripts/batch_main_analyze_nxp_parallel.sh`

默认并发为 `3`，可通过第一个参数覆盖。每个 demo 会执行：

1. `python main.py <MAIN_CMD> <demo>`
2. `python main.py dump-replacements <demo>`
3. `python main.py classify-stats <demo> --json --no-lists > <demo>/classify_stats.json`

示例：

```shell
# 默认 MAIN_CMD=run
scripts/batch_main_analyze_zephyr_parallel.sh 3

# 只跑前半段，不进入 emulate
MAIN_CMD=build scripts/batch_main_analyze_rtthread_parallel.sh 3

# 跳过主流程，仅补跑 dump + classify-stats
MAIN_CMD= scripts/batch_main_analyze_stm32_parallel.sh 3

# 只跑单个 demo
scripts/batch_main_analyze_nxp_parallel.sh 3 testcases/server/nxp/NXP_UART_BareMetal
```

### 2. 自适应总控脚本

统一调度四个平台，默认顺序为 `zephyr -> rtthread -> stm32 -> nxp`：

- 脚本：`scripts/batch_main_analyze_adaptive.py`
- 默认 `MAIN_CMD=build`
- 平台内并发基线默认 `3`
- 根据上一个时间窗口内的 retry 密度自动降低并发

常用命令：

```shell
python scripts/batch_main_analyze_adaptive.py
python scripts/batch_main_analyze_adaptive.py --dry-run
python scripts/batch_main_analyze_adaptive.py --platforms zephyr rtthread
python scripts/batch_main_analyze_adaptive.py --main-cmd run
python scripts/batch_main_analyze_adaptive.py \
  --window-minutes 10 \
  --high-threshold 40 \
  --critical-threshold 100 \
  --base-jobs 3 --min-jobs 1
```

### 3. 检查模式

`adaptive` 脚本内置检查模式，会输出：

1. CodeQL/collector 缓存是否齐全，例如 `src.zip`、`lcmhal_tmp/common_info.json`、`driver_info.json`、`mmio_info.json`
2. `lcmhal_ai_log` 覆盖情况，例如 `function_classify_*`、`replacement_update_*`
3. 当前后台相关 demo 进程，例如 `main.py build/run/analyze/dump/classify`

```shell
python scripts/batch_main_analyze_adaptive.py --check-only
python scripts/batch_main_analyze_adaptive.py --check
```

## MCP 服务与调试

启动顶层 MCP server：

```shell
python server.py
```

工具测试：

```shell
python -m utils.db_query
```

使用 Cline/Cursor 等 MCP 客户端测试静态分析 collector：

```json
{
  "mcpServers": {
    "lcmhal-infoCollector": {
      "timeout": 300,
      "command": "python",
      "args": [
        "-m",
        "tools.collector.mcp_server",
        "--db-path",
        "$CODEQL_DBPATH",
        "--transport",
        "stdio"
      ],
      "cwd": "/home/haojie/workspace/lcmhalmcp",
      "type": "stdio"
    }
  }
}
```

直接测试 MCP server：

```shell
python -m tools.collector.mcp_server
python -m tests.collector_mcp_test
```

VS Code debug 配置示例：

```json
{
  "name": "debug collector mcp server",
  "type": "debugpy",
  "request": "launch",
  "module": "tools.collector.mcp_server",
  "cwd": "${workspaceFolder}/lcmhalmcp",
  "console": "integratedTerminal",
  "args": [],
  "justMyCode": false
}
```

## 实验与可调参数

`lcmhal_config.yml` 与环境变量可以控制实验模式：

- `experiment_mode=full`：默认模式，启用 VerifyReplacement、BuilderFixer 和未验证替换清空策略。
- `experiment_mode=no_feedback`：消融模式，不挂载验证/修复工具，直接采纳结构化输出中的替换。
- `tool_profile=full`：Collector 提供完整工具集。
- `tool_profile=minimal`：仅保留 `GetFunctionInfo`，用于源代码上下文消融。
- `analyzer_recursion_limit`：FunctionClassifier LangGraph 最大步数。
- `llm_usage_log_enable` / `LCMHAL_LLM_USAGE_LOG=1`：在 session JSON 中记录 LLM token 与耗时。

命令行覆盖示例：

```shell
python main.py analyze testcases/server/nxp/NXP_UART_BareMetal \
  --func-name LPUART_WriteBlocking \
  --experiment-mode full \
  --tool-profile full \
  --analyzer-recursion-limit 50 \
  --llm-usage-log
```

## 给同学复用的能力模块

项目中可拆卸、可复用的能力不是一个单独脚本，而是几组边界比较清楚的模块：

| 能力 | 代表模块 | 可以复用来做什么 |
|------|----------|------------------|
| 静态分析能力 | `queries/`, `tools/collector/`, `models/query_results/` | 对 CodeQL DB 提取函数源码、调用关系、结构体/枚举、驱动注册/调用、MMIO 表达式、MMIO 函数集合、相关文件和调用栈 |
| MCP 工具服务能力 | `tools/*/mcp_server.py`, `server.py` | 把 collector、builder、emulator 暴露成 stdio MCP 工具，给 Cline/Cursor/其他 agent 调用 |
| 函数分类与替换生成能力 | `agents/analyzer_agent.py`, `prompts/function_classifier.py`, `utils/replacement_rubric.py` | 判断函数属于 CORE/RECV/IRQ/RETURNOK/SKIP/NODRIVER/INIT/LOOP，生成替换代码并在结束前做验证 |
| 编译验证与修复能力 | `tools/builder/`, `agents/builder_agent.py`, `agents/builder_fixer_agent.py` | 临时应用单函数替换、编译验证、失败后定位错误并修正 replacement，成功后再落盘 |
| 源码替换/恢复能力 | `tools/replacer/`, `utils/src_ops.py`, `utils/db_file.py` | 从 CodeQL DB 的 `src.zip` 读取原始函数，映射到真实源码路径，注入 `HAL_BE_*` 弱符号并替换/恢复函数 |
| 模拟器配置生成能力 | `tools/emulator/conf_generator.py` | 从 ELF 生成 `syms.yml`、`base_config.yml`、`semu_config.yml`，绑定 handlers、修正 flash size 和 initial_sp |
| 模拟器运行与反馈能力 | `tools/emulator/core.py`, `tools/emulator/emulate_runner.py`, `fuzzemu/` | 运行固件模拟，反馈 stdout/stderr、`lcmhal.txt` 中的 MMIO 调用、`function.txt` 调用栈、exceptional loop、UNMAPPED/fault PC |
| 动态闭环修复能力 | `agents/emulator_runner_agent.py`, `agents/fixer_agent.py` | 根据仿真失败日志调用 Fixer/Builder 迭代修复，直到模拟成功或达到终止条件 |
| 批处理与实验统计能力 | `scripts/`, `utils/classify_log_stats.py`, `utils/lcmhal_testcase_scan.py` | 扫描 testcase、批量跑平台矩阵、汇总分类/替换统计、生成实验表格 |

更完整的可复用能力说明见 `doc/design/reusable-capabilities.md`。

## 目标测试矩阵

项目当前围绕以下组合展开：

- 外设：UART、I2C、SPI、Flash、ETH、BLE
- 芯片/SDK：STM32、NXP、Nordic nRF、Ambiq
- OS/运行时：FreeRTOS、裸机、RT-Thread、Zephyr、mbedOS

典型 testcase 包括：

- STM32：`LwIP_StreamingServer`、`LwIP_HTTP_Server_Raw`、`LwIP_HTTP_Server_Socket_RTOS`、`UART_Hyperterminal_IT`、`FatFs_USBDisk_RTOS`、`BLE_HeartRateFreeRTOS`
- NXP：`NXP_UART_*`、`NXP_I2C_*`、`NXP_LwIP_*`、`NXP_FATFS_*`
- RT-Thread：`imxrt1052-nxp-evk`、`stm32f401-st-nucleo` 等
- Zephyr：`testcases/server/zephyr/{stm32,nxp,atmel}` 下的 ETH/UART/I2C/filesystem samples

## 参考文档

- `doc/ARCHITECTURE.md`：历史架构文档
- `doc/PAPER_SYSTEM_DESIGN.md`：论文系统设计草稿
- `doc/20260319_functionclassifier-verifyreplacement-buildfixer-workflow.md`：FunctionClassifier/Verify/BuilderFixer 协同
- `doc/20260319_dynamic_test_feedback_closed_loop_agent_workflow.md`：动态反馈闭环
- `doc/20260319_simulation_execution_platform_module.md`：仿真执行平台
- `doc/fuzzemu_execution_flow.md`：从固件 main 到 fuzzemu handler 的链路
- `doc/replacement_update_cases/README.md`：替换案例库
