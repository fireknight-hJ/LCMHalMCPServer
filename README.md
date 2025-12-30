# LCMHalMCPServer


使用方式：创建testcases目录，目录下创建：
- build.sh: 构建脚本（脚本职责如下）：
  - 1. 构建项目并生成elf文件
  - 2. 将生成的elf文件移动到脚本所在目录(并重命名为output.elf)
- clear.sh: 删除构建缓存脚本（包括编译生成的elf，obj文件等中间产物）

之后运行main.py (入参为testcases目录)
工具会自动尝试按照 codeql初步分析 + llm代码分析 + 代码替换&编译生成新的elf + 动态运行反馈 流程进行测试


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