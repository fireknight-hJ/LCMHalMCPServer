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
python -m tests.collector_mcp_test

# test builder_mcp_server

# test driver_dir_server

```