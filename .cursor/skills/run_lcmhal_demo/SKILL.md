---
name: run_lcmhal_demo
description: 运行 LCMHAL demo 并评估执行结果（通用：任意 testcase 目录）
---

# 运行 LCMHAL Demo

## 重要：统一入口

**跑 demo 必须通过项目的 main 入口**，即执行 `python main.py run <TESTCASE_DIR>`。  
**不要**自己写 Python 脚本（例如在脚本里 `import`、调用 `emulate_proj`、`register_db`、`generate_emulator_configs` 等）去跑 demo，以免跳过 build/分析等步骤或与正式流程不一致。

## 适用条件

任一**包含 `lcmhal_config.yml` 的 testcase 目录**均可作为运行目标，例如：

- `testcases/server/stm32/LwIP_StreamingServer`
- `testcases/server/nxp/NXP_UART_FreeRTOS`
- `testcases/server/nxp/NXP_LwIP_FreeRTOS`
- `testcases/server/rtthread/imxrt1052-nxp-evk/uart`
- 其他 `testcases/server/<vendor>/<demo>/` 下具备 `lcmhal_config.yml` 的目录

## 执行命令（唯一推荐方式）

在项目根目录下执行 main 入口：

```bash
cd /home/haojie/workspace/lcmhalmcp
python main.py run <TESTCASE_DIR>
```

将 `<TESTCASE_DIR>` 替换为上述 testcase 的**绝对路径或相对路径**，例如：

```bash
python main.py run testcases/server/stm32/LwIP_StreamingServer
python main.py run testcases/server/nxp/NXP_UART_FreeRTOS
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

输出文件位于该 testcase 的 `emulate/debug_output/` 下：

- `<TESTCASE_DIR>/emulate/debug_output/lcmhal.txt`
- `<TESTCASE_DIR>/emulate/debug_output/function.txt`
- `<TESTCASE_DIR>/emulate/debug_output/debug.txt`
