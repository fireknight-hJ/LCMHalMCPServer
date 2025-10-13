# LCMHalMCPServer

start server: 

``` shell
python server.py
```

testing:

utils test:
``` shell
python -m utils.db_query
```

mcp servers test (with cline):
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