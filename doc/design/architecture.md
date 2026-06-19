# LCMHalMCP 架构设计

本文描述仓库当前实现的整体架构。旧版 `README_STRUCTURE.md` 更接近早期重构规划，本目录文档以当前代码为准。

## 1. 系统目标

LCMHalMCP 的目标是让嵌入式 HAL/driver demo 在没有真实硬件的环境下完成：

1. 静态识别硬件相关函数；
2. 生成可模拟的替换实现；
3. 用编译与 rubric 约束防止错误替换落盘；
4. 生成模拟器配置并运行固件；
5. 根据运行时反馈继续修复。

## 2. 分层结构

```text
入口层
  main.py / server.py
    |
工作流层
  run/build/emulate/recover/clean/analyze/dump/classify-stats
    |
智能体层
  Analyzer / Builder / BuilderFixer / Fixer / EmulatorRunner / DriverLocator
    |
工具层
  Collector / Builder / Replacer / Emulator
    |
数据与模型层
  CodeQL DB / src.zip / DataManager / ai_log / Pydantic models
    |
目标固件与模拟器
  testcase source / build.sh / fuzzemu / Unicorn / debug_output
```

## 3. 数据流

```text
lcmhal_config.yml
  -> config.globs.globs_init()
  -> tools.builder.proj_builder.build_proj_dbgen()
  -> tools.collector.collector.register_db()
  -> tools.collector.* 查询 CodeQL DB 和 src.zip
  -> agents.analyzer_agent.analyze_functions()
  -> core.data_manager 保存 classify/replacement/history
  -> tools.builder.core.verify_replacement()/update_function_replacement()
  -> tools.replacer.code_replacer.function_replace()
  -> tools.builder.core.build_project()
  -> tools.emulator.conf_generator.generate_emulator_configs()
  -> tools.emulator.core.emulate_proj()
  -> agents.fixer_agent / agents.builder_agent 动态修复
```

## 4. 关键设计约束

- CodeQL DB 是源码真相来源之一。`src.zip` 用于读取原始函数和恢复文件，避免替换后的源码污染后续分析。
- `DataManager` 是跨 agent 的运行时状态中心，保存 MMIO 分类结果、替换更新和替换历史。
- 替换代码采用 fail-closed 策略：没有通过 `VerifyReplacement` 或 `FixFunctionBuildErrors` 成功证据的 replacement 会在 Analyzer 最终响应中被清空。
- `HAL_BE_*` 弱符号是源码替换与 fuzzemu handler 的桥。源码中保留弱实现，模拟时由 `semu_config.yml` 的 handlers 接管。
- RTOS/NVIC/SysTick/VTOR 等 CORE 类函数默认不应替换，除非替换能保留关键寄存器语义。

## 5. 主要外部依赖

- CodeQL CLI：构建和查询 C/C++ CodeQL database。
- LangChain/LangGraph：智能体状态图、工具调用和结构化输出。
- FastMCP / langchain-mcp-adapters：stdio MCP 服务与工具适配。
- ARM GCC / objcopy：固件构建与 ELF/BIN 转换。
- pyelftools：解析 ELF 符号表，生成 `syms.yml`。
- fuzzemu/Unicorn/AFL++：固件模拟执行与 fuzz 支持。

