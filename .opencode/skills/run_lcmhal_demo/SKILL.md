---
name: run_lcmhal_demo
description: 运行 LCMHAL demo 并评估执行结果
---

# 运行 LCMHAL Demo

## Demo 配置文件目录

Demo 的配置文件位于 `testcases/server/stm32/LwIP_StreamingServer/lcmhal_config.yml`

对应目录：`/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer`

## 执行命令

```bash
cd /home/haojie/workspace/lcmhalmcp
python main.py run /home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer
```

## 评估结果

### 1. 检查 EmulateProject 返回值

Emulator 工具返回包含以下关键字段：
- `success`: bool - 是否成功
- `exit_code`: int - 退出码
- `has_exceptional_loop`: bool - 是否有死循环

### 2. 失败条件

满足以下任一条件视为失败：

1. **死循环**: `has_exceptional_loop: true` 或 lcmhal.txt 包含 `[-] Stop due to exceptional loop`
2. **Agent 执行超轮次**: Agent 执行超过 50 个轮次
3. **未捕获 MMIO 函数**: lcmhal.txt 为空或无预期函数
4. **非正常退出**: `success: false` 或 exit_code 不为 0

### 3. 成功条件

1. `success: true`
2. lcmhal.txt 包含预期的 MMIO 函数调用
3. 无死循环日志

## 输出文件位置

- `/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer/emulate/debug_output/lcmhal.txt`
- `/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer/emulate/debug_output/function.txt`
- `/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer/emulate/debug_output/debug.txt`
