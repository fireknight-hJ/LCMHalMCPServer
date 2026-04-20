# LCMHalMCPServer


使用方式：创建testcases目录，目录下创建：
- build.sh: 构建脚本（脚本职责如下）：
  - 1. 构建项目并生成elf文件
  - 2. 将生成的elf文件移动到脚本所在目录(并重命名为output.elf)
- clear.sh: 删除构建缓存脚本（包括编译生成的elf，obj文件等中间产物，核心目的是不让中间产物影响下次编译构建）
- lcmhal_config.yml: 配置文件（包含以下配置项）：
  - script_path: 脚本路径
  - db_path: 数据库路径
  - src_path: 源代码路径
  - proj_path: 项目路径

**Zephyr**：见 `testcases/server/zephyr/README.md`。每个用例同样包含上述三文件；在 Zephyr workspace（`west`）根目录执行构建，`src_path` 为 `zephyr` 源码目录，`proj_path` 为 workspace 根；可通过环境变量 `ZEPHYR_PROJECT` 覆盖默认的 `/home/haojie/zephyrproject`。

之后运行main.py (入参为testcases目录)
工具会自动尝试按照 codeql初步分析 + llm代码分析 + 代码替换&编译生成新的elf + 动态运行反馈 流程进行测试

## 批处理脚本使用

### 1) 平台批处理脚本

四个平台脚本分别是：

- `scripts/batch_main_analyze_zephyr_parallel.sh`
- `scripts/batch_main_analyze_rtthread_parallel.sh`
- `scripts/batch_main_analyze_stm32_parallel.sh`
- `scripts/batch_main_analyze_nxp_parallel.sh`

默认并发为 `3`（可通过第一个参数覆盖），每个 demo 会执行：

1. `python main.py <MAIN_CMD> <demo>`
2. `python main.py dump-replacements <demo>`
3. `python main.py classify-stats <demo> --json --no-lists > <demo>/classify_stats.json`

示例：

```shell
# 默认（MAIN_CMD=run）
scripts/batch_main_analyze_zephyr_parallel.sh 3

# 只跑前半段（不进 emulate）
MAIN_CMD=build scripts/batch_main_analyze_rtthread_parallel.sh 3

# 跳过主流程，仅补跑汇总（dump + classify-stats）
MAIN_CMD= scripts/batch_main_analyze_stm32_parallel.sh 3

# 只跑单个 demo
scripts/batch_main_analyze_nxp_parallel.sh 3 testcases/server/nxp/NXP_UART_BareMetal
```

### 2) 自适应总控脚本

统一调度四个平台（默认顺序：`zephyr -> rtthread -> stm32 -> nxp`）：

- 脚本：`scripts/batch_main_analyze_adaptive.py`
- 默认 `MAIN_CMD=build`
- 平台内并发基线默认 `3`
- 根据“上一个时间窗口”的 retry 密度自动降并发

常用命令：

```shell
# 正常执行
python scripts/batch_main_analyze_adaptive.py

# 只预览将要执行的命令/并发
python scripts/batch_main_analyze_adaptive.py --dry-run

# 指定平台顺序或子集
python scripts/batch_main_analyze_adaptive.py --platforms zephyr rtthread

# 切回 run 模式
python scripts/batch_main_analyze_adaptive.py --main-cmd run

# 调整窗口和阈值
python scripts/batch_main_analyze_adaptive.py \
  --window-minutes 10 \
  --high-threshold 40 \
  --critical-threshold 100 \
  --base-jobs 3 --min-jobs 1
```

### 3) 检查功能（缓存/日志/后台进程）

`adaptive` 脚本内置检查模式，输出三类信息：

1. CodeQL/collector 缓存是否齐全（`src.zip`、`lcmhal_tmp/common_info.json`、`driver_info.json`、`mmio_info.json`）
2. `lcmhal_ai_log` 覆盖情况（`function_classify_*`、`replacement_update_*` 数量）
3. 当前后台相关 demo 进程（含 `main.py build/run/analyze/dump/classify`）

示例：

```shell
# 只检查，不执行批处理
python scripts/batch_main_analyze_adaptive.py --check-only

# 先检查，再执行
python scripts/batch_main_analyze_adaptive.py --check
```


start server: 

``` shell
python server.py
```

testing:

utils test:
``` shell
python -m utils.db_query
```

支持使用cline插件测试静态分析结果的mcp接口工具 mcp servers test (with cline):
``` json
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
        "--transfer",
        "stdio"
      ],
      "cwd": "/home/haojie/workspace/lcmhalmcp",
      "type": "stdio"
    }
  }
}
```

mcp servers test (with tests ):
``` shell
# test collector_mcp_server
python -m tools.collector.mcp_server # 打开mcp服务
python -m tests.collector_mcp_test # 测试mcp服务

# test builder_mcp_server

# test driver_dir_server

```

mcp servers debug (with vscode):
``` json
        {
            "name": "debug collector mcp server",
            "type": "debugpy",
            "request": "launch",
            "module": "tools.collector.mcp_server",
            "cwd": "${workspaceFolder}/lcmhalmcp",
            "console": "integratedTerminal",
            "args": [],
            "justMyCode": false
        },
```

预计测试的os+hal+外设：

1. (uart, i2c, spi), flash, eth, ble
2. stm32, nrf, nxp，ambiq

stm32 uart  --目录 --编译指令
      flash --目录 --编译指令
      eth --目录 --编译指令
      ble --目录 --编译指令

freertos，裸机，rtthread，zephyr，（mebedos）