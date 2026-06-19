---
name: debug_lcmhal_failure
description: 排查 LCMHAL demo 运行失败问题
---

# 排查 LCMHAL Demo 运行失败

## 排查步骤

### 1. 检查 main.py 标准输出

main.py 执行过程中会输出关键信息：
- Build 输出：编译是否成功、替换了哪些函数
- Emulate 输出：模拟器执行结果
- 检查是否有 `exceptional loop`、`error`、`fail` 等关键词

### 2. 检查固件执行日志

日志目录：`emulate/debug_output/`

**lcmhal.txt** - MMIO 函数调用记录
- 查看是否有 `[-] Stop due to exceptional loop`
- 查看 `current function` 和 `current caller function` 确定卡在哪里

**function.txt** - 函数调用栈
- 查看完整的函数调用链

**debug.txt** - 调试信息
- 查看具体执行到了哪个地址

### 3. 特殊情况：日志为空

如果 `lcmhal.txt` 为空或几乎为空，说明固件从开始就没跑通。需要检查：

1. **编译是否成功**：检查 main.py 输出中 build 结果
2. **入口点配置**：
   - 检查 `emulate/semu_config.yml` 中的 `entry_point` 是否正确
   - 检查 `initial_sp` 是否正确
   - 对比 ELF 文件：`arm-none-eabi-nm -n output.elf | grep Reset_Handler`
3. **内存配置**：flash 起始地址应为 0x8000000

### 4. 正常情况：有日志但失败

根据日志分析失败原因：

**死循环 (exceptional loop)**：
- 查看 `current function` 和 `current caller function`
- 确定是哪个函数导致的循环

**其他错误**：
- 内存访问错误
- 崩溃

### 5. 读取固件源码分析

1. **获取问题地址**：从 lcmhal.txt 或 debug.txt 获取 PC 地址

2. **反汇编**：
   ```bash
   arm-none-eabi-objdump -d output.elf | grep -A 10 "地址"
   ```

3. **查看源文件**：在源码目录中找到对应的 C 文件

### 6. 检查函数替换情况

**重要**：必须从 AI log 读取函数替换情况，源码会自动复原！

Builder 工具在编译前会进行函数替换，编译完成后会自动复原源码。因此：
- 查看源码不会找到任何替换内容
- 必须从 AI log 中查看替换记录

**通过 dump-replacements 生成 replacement_log.md（推荐）**：
- 在 testcase 目录下执行：`python main.py dump-replacements --config <testcase目录或config.yml>`
- 或使用 lcmhal 封装：`./lcmhal dump-replacements <testcase路径>`
- 默认会在该 testcase 目录下生成 **replacement_log.md**，包含：
  - **1. 替换函数总览**：函数名、文件路径、行号、替换次数
  - **2. 各函数替换详情**：每个函数的分析摘要与替换内容（来自 data_manager / AI log）
- 可选指定输出文件：`--log-file 其他名.md` 或 `--log-file /绝对路径.md`
- 排查执行问题时，先看 `replacement_log.md` 即可快速了解当前有哪些函数被替换、替换成了什么，再结合 lcmhal.txt/function.txt 定位问题。

AI log 目录：`DATABASE_PATH/lcmhal_ai_log/`

查找替换记录（若未生成 replacement_log.md）：
- 搜索包含 `ReplacementUpdate` 的日志
- 搜索 `replacement_code` 字段
- 或查看 main.py 输出中的 `[REPLACE]` 信息

### 7. 根据 AI log 分析问题

根据 AI log 中记录的：
- 替换了哪些函数
- 替换的代码内容 (`replacement_code`)
- 替换原因 (`reason`)

分析问题根因，例如：
- 某个函数的替换逻辑是否有问题
- 是否遗漏了某些需要替换的函数
- 替换代码是否正确

## 常见问题

| 问题 | 原因 |
|------|------|
| 日志为空 | 入口点配置错误或编译失败 |
| exceptional loop | 某个驱动函数存在循环等待硬件 |
| 编译失败 | 源码替换导致语法错误 |
