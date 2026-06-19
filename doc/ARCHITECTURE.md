# LCMHalMCP 架构文档

## 1. 项目概述

**LCMHalMCP**（LLM-CodeQL-MCP-based HAL Analysis and Replacement Tool）是一个基于 LLM + CodeQL 的嵌入式 HAL（Hardware Abstraction Layer）代码自动化分析与替换工具。

### 1.1 项目规模

- **总代码量：** ~39,000 行 Python 代码
- **核心模块：** 8 个（agents, tools, core, config, models, prompts, utils, fuzzemu）
- **支持平台：** STM32F4, NXP i.MX RT, Ambiq Apollo, Nordic nRF
- **支持外设：** UART, I2C, SPI, ETH, Flash, BLE
- **支持 RTOS：** FreeRTOS, RT-Thread, Zephyr, 裸机

### 1.2 核心功能

1. **静态分析** - 使用 CodeQL 分析嵌入式固件代码，提取函数信息、调用关系、MMIO 操作
2. **智能识别** - 使用 LLM 识别 MMIO（内存映射 I/O）相关函数，分类函数类型
3. **代码生成** - 自动生成替换代码（stub/mock），支持语义等价性验证
4. **编译验证** - 自动编译并验证替换结果，支持增量修复
5. **动态仿真** - 使用 QEMU/Semihosting 进行仿真测试，收集运行时反馈
6. **MCP 接口** - 提供 MCP（Model Context Protocol）服务器接口，支持与 Cline 等工具集成

---

## 2. 系统架构

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              LCMHalMCP 系统                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐                                                            │
│  │   main.py   │  入口点，工作流编排                                         │
│  └──────┬──────┘                                                            │
│         │                                                                   │
│         ▼                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         工作流执行层                                 │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │   │
│  │  │  Config  │─▶│  Build   │─▶│ Analyze  │─▶│ Replace  │            │   │
│  │  │  (YAML)  │  │ (CodeQL) │  │  (LLM)   │  │  (Code)  │            │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │   │
│  │                                     │              │                 │   │
│  │                                     ▼              ▼                 │   │
│  │                              ┌──────────┐   ┌──────────┐            │   │
│  │                              │ Collector│   │ Emulator │            │   │
│  │                              │(DB Query)│   │  (QEMU)  │            │   │
│  │                              └──────────┘   └──────────┘            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                           AI 代理层                                  │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │   │
│  │  │  Analyzer   │ │   Builder   │ │   Fixer     │ │  Emulator   │   │   │
│  │  │   Agent     │ │   Agent     │ │   Agent     │ │   Runner    │   │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                           数据层                                     │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │   │
│  │  │  CodeQL DB  │ │  AI Logs    │ │   Cache     │ │  Config     │   │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 分层架构

| 层级 | 组件 | 职责 |
|------|------|------|
| **入口层** | main.py, server.py | 命令行入口、MCP 服务器 |
| **工作流层** | run_workflow, recover_workflow | 编排整个分析流程 |
| **代理层** | agents/* | AI 驱动的分析、构建、修复 |
| **工具层** | tools/* | CodeQL 查询、代码替换、仿真 |
| **核心层** | core/* | 数据管理、收集器核心 |
| **配置层** | config/* | 全局配置、LLM 配置 |
| **模型层** | models/* | 数据结构定义 |
| **提示层** | prompts/* | LLM 提示词模板 |
| **工具函数层** | utils/* | 数据库操作、日志管理 |

---

## 3. 目录结构详解

```
lcmhalmcp/
├── main.py                    # 主入口 - 工作流编排
│   ├── run_workflow()         # 主工作流：构建 → 分析 → 替换 → 编译 → 仿真
│   ├── recover_workflow()     # 恢复工作流：从数据库恢复原始代码
│   └── clean_function_logs()  # 清理 AI 分析日志
│
├── server.py                  # MCP 服务器入口
│
├── agents/                    # AI 代理模块 (LangGraph + LangChain)
│   ├── analyzer_agent.py      # 函数分析代理
│   │   ├── build_graph()      # 构建 LangGraph 状态图
│   │   ├── analyze_functions()# 批量分析 MMIO 函数
│   │   └── 工具: GetFunctionInfo, GetMMIOFunctionInfo, GetStructOrEnumInfo...
│   │
│   ├── builder_agent.py       # 构建代理 - 自动修复编译错误
│   │   ├── run_build_project()# 运行构建并自动修复
│   │   └── 递归修复直到编译成功
│   │
│   ├── builder_fixer_agent.py # 构建修复代理 - 作为工具被调用
│   │   └── builder_fixer_agent() # 单函数编译验证和修复
│   │
│   ├── fixer_agent.py         # 函数修复代理 - 生成替换代码
│   │   ├── build_graph()      # 修复流程状态图
│   │   └── 工具: build_project, emulate_proj, mmio_function_emulate_info...
│   │
│   ├── emulator_runner_agent.py # 仿真运行代理
│   │   └── run_emulator()     # 启动 QEMU 仿真
│   │
│   └── driver_locator_agent.py  # 驱动定位代理
│
├── tools/                     # 工具模块
│   ├── analyzer/              # 静态分析工具
│   │
│   ├── builder/               # 项目构建工具
│   │   ├── proj_builder.py    # 项目构建器
│   │   │   ├── build_proj_dbgen() # 构建 CodeQL 数据库
│   │   │   ├── build_proj()       # 编译项目
│   │   │   └── clear_proj()       # 清理构建产物
│   │   │
│   │   ├── core.py            # 构建核心逻辑 ★★★
│   │   │   ├── replace_funcs()         # 替换函数
│   │   │   ├── recover_funcs()         # 恢复函数
│   │   │   ├── build_project()         # 构建项目
│   │   │   ├── verify_replacement()    # 验证替换代码
│   │   │   ├── update_function_replacement() # 更新替换
│   │   │   ├── elf_to_bin()            # ELF 转 BIN
│   │   │   └── _compile_verify_single_replacement() # 单函数编译验证
│   │   │
│   │   ├── tool.py            # 构建工具封装
│   │   └── mcp_server.py      # MCP 服务器接口
│   │
│   ├── collector/             # CodeQL 数据收集器
│   │   ├── collector.py       # 主收集器 ★★★
│   │   │   ├── CodebaseInfos  # 代码库信息总数据结构
│   │   │   ├── register_db()  # 注册数据库
│   │   │   ├── get_mmio_func_list()    # 获取 MMIO 函数列表
│   │   │   ├── get_function_info()     # 获取函数信息
│   │   │   ├── get_mmio_func_info()    # 获取 MMIO 函数详情
│   │   │   ├── get_struct_or_enum_info() # 获取结构体/枚举
│   │   │   ├── get_func_call_stack()   # 获取调用栈
│   │   │   └── get_driver_info()       # 获取驱动信息
│   │   │
│   │   ├── core.py            # 核心查询函数导出
│   │   ├── mmio.py            # MMIO 相关查询 ★★★
│   │   │   ├── MmioCodebaseInfo        # MMIO 代码库信息
│   │   │   ├── mmio_functions          # MMIO 函数字典
│   │   │   ├── driver_functions        # 驱动函数字典
│   │   │   ├── buffer_functions        # 缓冲函数字典
│   │   │   ├── mmioinfo_interestingmmioexpr_dict  # MMIO 表达式
│   │   │   └── mmioinfo_interestingmmiofunc_contains_dict # 包含关系
│   │   │
│   │   ├── driver.py          # 驱动信息查询
│   │   ├── common.py          # 通用代码信息
│   │   ├── base.py            # 基类
│   │   ├── tool.py            # 工具封装
│   │   └── mcp_server.py      # MCP 服务器接口
│   │
│   ├── replacer/              # 代码替换工具
│   │   ├── code_replacer.py   # 代码替换器
│   │   │   ├── get_func_content()  # 获取函数内容
│   │   │   └── function_replace()  # 替换函数
│   │   │
│   │   ├── code_recover.py    # 代码恢复器
│   │   │   └── recover_code_file() # 从数据库恢复代码
│   │   │
│   │   └── diff_gen.py        # 差异生成
│   │
│   └── emulator/              # 仿真工具
│       ├── conf_generator.py  # 配置生成器 ★★★
│       │   ├── generate_emulator_configs() # 生成所有配置
│       │   ├── generate_base_config()      # 生成基础配置
│       │   ├── generate_semu_config()      # 生成 semu 配置
│       │   ├── extract_syms()              # 提取符号表
│       │   ├── fix_flash_size()            # 修正内存配置
│       │   └── mmio_funcs_emulate_config() # MMIO 函数仿真配置
│       │
│       ├── emulate_runner.py  # 仿真运行器
│       ├── core.py            # 仿真核心
│       ├── tool.py            # 工具封装
│       └── mcp_server.py      # MCP 服务器接口
│
├── core/                      # 核心模块
│   ├── data_manager.py        # 数据管理器 ★★★
│   │   ├── DataManager        # 全局数据管理类
│   │   │   ├── mmio_info_list           # MMIO 函数信息列表
│   │   │   ├── mmio_infos_by_file       # 按文件分类的 MMIO 信息
│   │   │   ├── replacement_updates      # 替换更新信息
│   │   │   ├── replacement_updates_by_file # 按文件分类的替换更新
│   │   │   └── replacement_history      # 替换历史版本
│   │   │
│   │   └── 方法:
│   │       ├── load_mmio_functions()              # 加载 MMIO 函数
│   │       ├── update_function_replacement()      # 更新函数替换
│   │       ├── get_function_analysis_and_replacement() # 获取分析结果
│   │       ├── get_replace_func_details_by_file() # 按文件获取详情
│   │       └── dump_full_info()                   # 导出全量信息
│   │
│   └── collector.py           # 收集器核心
│
├── config/                    # 配置模块
│   ├── globs.py               # 全局配置管理 ★★★
│   │   ├── script_path        # 测试用例路径
│   │   ├── db_path            # CodeQL 数据库路径
│   │   ├── src_path           # 源代码路径
│   │   ├── proj_path          # 项目路径
│   │   ├── ai_log_enable      # AI 日志开关
│   │   └── enable_compile_verify # 编译验证开关
│   │
│   ├── llm_config.py          # LLM 配置
│   ├── collector_infos.py     # 收集器信息配置
│   └── model_singleton.py     # 模型单例（统一 LLM 实例）
│
├── models/                    # 数据模型
│   ├── query_results/         # 查询结果模型
│   │   ├── common.py          # 通用模型
│   │   │   ├── FunctionInfo   # 函数信息
│   │   │   ├── FunctionCallInfo # 调用信息
│   │   │   └── StructInfo     # 结构体信息
│   │   │
│   │   └── mmio.py            # MMIO 模型
│   │       ├── MmioExprInfo   # MMIO 表达式信息
│   │       └── MmioFunctionContainsInfo # 包含关系信息
│   │
│   ├── analyze_results/       # 分析结果模型
│   │   └── function_analyze.py # 函数分析模型 ★★★
│   │       ├── FunctionClassifyResponse # 函数分类响应
│   │       │   ├── function_name        # 函数名
│   │       │   ├── function_type        # 类型: MMIO/DRIVER/LOGIC/CORE
│   │       │   ├── usage_type           # 用途
│   │       │   ├── has_replacement      # 是否需要替换
│   │       │   ├── reason               # 原因
│   │       │   ├── original_code        # 原始代码
│   │       │   ├── recommended_code     # 推荐替换代码
│   │       │   └── confidence           # 置信度
│   │       │
│   │       └── ReplacementUpdate # 替换更新
│   │           ├── function_name        # 函数名
│   │           ├── replacement_code     # 替换代码
│   │           └── reason               # 原因
│   │
│   ├── build_results/         # 构建结果模型
│   │   └── BuildInfo          # 构建信息
│   │
│   └── emulate_results/       # 仿真结果模型
│       └── EmulateInfo        # 仿真信息
│
├── prompts/                   # LLM 提示词
│   ├── function_classifier.py # 函数分类提示词
│   │   └── system_prompting_en # 系统提示词
│   │
│   ├── function_fixer.py      # 函数修复提示词
│   │   ├── system_prompt_en   # 系统提示词
│   │   └── 代码生成规则
│   │
│   ├── code_generation_rules.md # 代码生成规则
│   │   ├── 类型约束（不要在 NXP 代码中使用 HAL_StatusTypeDef）
│   │   ├── 函数签名必须一致
│   │   └── 不要引入不存在的类型
│   │
│   ├── summary_prompt.py      # 总结提示词
│   │   ├── function_classify_final_prompt_en
│   │   └── fixer_summary_prompt_en
│   │
│   └── project_builder.py     # 项目构建提示词
│
├── queries/                   # CodeQL 查询（Datalog）
│   ├── collectors/            # 收集器查询
│   │   └── common/            # 通用查询
│   │       └── info_function_collector.ql # 函数信息收集
│   │
│   └── libraries/             # 查询库
│
├── utils/                     # 工具函数
│   ├── db_query.py            # 数据库查询
│   │   └── run_query_and_return_json() # 执行 CodeQL 查询
│   │
│   ├── db_file.py             # 数据库文件操作
│   │   ├── list_files_in_db_zip() # 列出数据库中的文件
│   │   ├── read_struct_with_start_line_from_db() # 读取代码结构
│   │   └── get_tree_in_db_zip() # 获取目录树
│   │
│   ├── db_cache.py            # 数据库缓存
│   │   ├── dump_message_json_log() # 保存消息日志
│   │   ├── check_analyzed_json_log() # 检查日志是否存在
│   │   └── get_analyzed_json_log() # 获取日志内容
│   │
│   ├── src_ops.py             # 源码操作
│   │   ├── src_replace()      # 源码替换
│   │   └── file_convert_proj2src() # 路径转换
│   │
│   ├── ai_log_manager.py      # AI 日志管理器
│   │   └── ai_log_manager     # 单例，管理日志目录
│   │
│   ├── replacement_rubric.py  # 替换规则检查
│   │   └── check_replacement_rubric() # 检查替换代码质量
│   │
│   ├── log.py                 # 日志工具
│   ├── db_lock.py             # 数据库锁
│   ├── failcheck.py           # 失败检查
│   └── ghidra_helper.py       # Ghidra 辅助工具
│
├── fuzzemu/                   # 模糊测试/仿真框架
│   └── fuzzemu/               # 核心框架
│       ├── handlers/          # HAL 处理器
│       │   ├── stm32f4_hal/   # STM32F4 HAL 处理
│       │   │   ├── stm32f4_i2c.py # I2C 处理
│       │   │   ├── stm32f4_uart.py # UART 处理
│       │   │   └── st_consts.py   # 常量定义
│       │   │
│       │   └── models/        # 设备模型
│       │       └── i2c.py     # I2C 模型
│       │
│       ├── models/            # 仿真模型
│       │   ├── semu/          # semu 模型
│       │   ├── lemu/          # lemu 模型
│       │   └── uemu/          # uemu 模型
│       │
│       ├── configuration/     # 配置模块
│       └── helper/            # 辅助工具
│
├── testcases/                 # 测试用例
│   ├── server/                # 服务器测试用例
│   │   ├── nxp/               # NXP 芯片测试
│   │   │   ├── NXP_I2C_FreeRTOS/
│   │   │   │   ├── lcmhal_config.yml # 配置文件
│   │   │   │   ├── build.sh          # 构建脚本
│   │   │   │   ├── clear.sh          # 清理脚本
│   │   │   │   └── emulate/          # 仿真配置
│   │   │   │
│   │   │   ├── NXP_UART_FreeRTOS/
│   │   │   ├── NXP_LwIP_FreeRTOS/
│   │   │   ├── NXP_FATFS_FreeRTOS/
│   │   │   └── ...
│   │   │
│   │   ├── stm32/             # STM32 芯片测试
│   │   └── rtthread/          # RT-Thread 测试
│   │
│   └── macbook/               # 本地测试用例
│
├── case_study/                # 案例研究
│   ├── fatfs_classifier_replacements_202603.md
│   ├── hal_eth_init_dma_fix/
│   ├── hal_eth_init_subfunction_fix/
│   └── rtthread_vtor_0x0_unmapped_fix/
│
└── doc/                       # 文档
    └── ARCHITECTURE.md        # 本文档
```

---

## 4. 核心数据流

### 4.1 完整工作流程

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           完整工作流程 (run_workflow)                         │
└──────────────────────────────────────────────────────────────────────────────┘

[1] 配置加载 (load_config_from_yaml)
    │   - 读取 lcmhal_config.yml
    │   - 设置 script_path, db_path, src_path, proj_path
    │
    ▼
[2] 全局初始化 (globs_init)
    │   - 初始化全局变量
    │   - 设置日志开关
    │
    ▼
[3] CodeQL 数据库构建 (build_proj_dbgen)
    │   ├── 3.1 调用 build.sh 编译项目
    │   │   - CMake 配置
    │   │   - Ninja 构建
    │   │   - 生成 ELF 文件
    │   │
    │   └── 3.2 生成 CodeQL 数据库
    │       - codeql database create
    │       - 解析 C/C++ 代码
    │       - 构建查询索引
    │
    ▼
[4] 数据库注册 (register_db)
    │   ├── 4.1 创建 CodebaseInfos 实例
    │   │   - common_infos: 通用代码信息
    │   │   - driver_infos: 驱动代码信息
    │   │   - mmio_infos: MMIO 代码信息
    │   │
    │   └── 4.2 缓存到内存
    │       - codebase_infos_dict[db_path] = CodebaseInfos
    │
    ▼
[5] Builder 初始化 (init_builder)
    │   └── 5.1 加载 MMIO 函数信息 (data_manager.load_mmio_functions)
    │       ├── 获取函数列表 (get_mmio_func_list)
    │       ├── 调用 Analyzer Agent 分析 (analyze_functions)
    │       │   ├── 对每个函数调用 LangGraph
    │       │   ├── 使用工具获取函数信息
    │       │   ├── LLM 分类函数类型
    │       │   └── 生成 FunctionClassifyResponse
    │       │
    │       └── 缓存分析结果
    │           - mmio_info_list[func_name] = classify_res
    │
    ▼
[6] 项目构建 (build_project) ─────────────────────────────────────────────────┐
    │   ├── 6.1 恢复原始文件 (recover_funcs)                                    │
    │   │   - 从数据库恢复所有被替换的文件                                        │
    │   │                                                                        │
    │   ├── 6.2 替换函数 (replace_funcs)                                         │
    │   │   - 遍历 mmio_info_list                                               │
    │   │   - 跳过 CORE 类型函数                                                │
    │   │   - 应用 replacement_code                                             │
    │   │   - 使用 src_replace() 替换源文件                                      │
    │   │                                                                        │
    │   ├── 6.3 清理构建 (clear_proj)                                            │
    │   │   - 调用 clear.sh                                                     │
    │   │   - 删除中间产物                                                       │
    │   │                                                                        │
    │   ├── 6.4 编译项目 (build_proj)                                            │
    │   │   - 调用 build.sh                                                     │
    │   │   - 生成 output.elf                                                   │
    │   │   - 捕获 stdout/stderr                                                │
    │   │                                                                        │
    │   ├── 6.5 恢复文件 (recover_funcs)                                         │
    │   │   - 恢复所有被替换的文件                                               │
    │   │                                                                        │
    │   └── 6.6 后处理                                                           │
    │       ├── ELF 转 BIN (elf_to_bin)                                         │
    │       └── 提取符号表 (extract_syms)                                        │
    │                                                                            │
    │   ┌──────────────────────────────────────────────────────────────────┐   │
    │   │ 如果编译失败 (exit_code != 0)                                     │   │
    │   │   └─▶ Builder Agent (run_build_project)                          │   │
    │   │       ├── 分析编译错误                                            │   │
    │   │       ├── 识别需要修复的函数                                       │   │
    │   │       ├── 调用 Fixer Agent 生成新代码                             │   │
    │   │       │   ├── 获取函数信息                                        │   │
    │   │       │   ├── 分析错误原因                                        │   │
    │   │       │   ├── 生成修复代码                                        │   │
    │   │       │   └── 调用 update_function_replacement                    │   │
    │   │       ├── 重新编译 (build_project)                                │   │
    │   │       └─▶ 循环直到成功或达到最大次数                               │   │
    │   └──────────────────────────────────────────────────────────────────┘   │
    │                                                                            │
    ▼                                                                            │
[7] 仿真配置生成 (generate_emulator_configs)                                   │
    │   ├── 7.1 生成基础配置 (generate_base_config)                             │
    │   │   - base_config.yml                                                  │
    │   │   - MMIO 函数列表                                                    │
    │   │   - Handler 映射                                                     │
    │   │                                                                        │
    │   ├── 7.2 生成规则文件 (generate_rule_config)                             │
    │   │   - semu_rule.txt                                                    │
    │   │                                                                        │
    │   ├── 7.3 生成输入文件 (generate_base_input)                              │
    │   │   - base_input/input.bin                                             │
    │   │                                                                        │
    │   └── 7.4 生成 semu 配置 (generate_semu_config)                           │
    │       - fuzzemu-helper config                                             │
    │       - fix_flash_size()                                                  │
    │                                                                            │
    ▼                                                                            │
[8] 仿真运行 (run_emulator)                                                     │
    │   ├── 8.1 启动 QEMU 仿真                                                  │
    │   │   - 加载 output.bin                                                  │
    │   │   - 应用 semu_config.yml                                             │
    │   │                                                                        │
    │   ├── 8.2 执行程序                                                        │
    │   │   - 运行 MMIO 函数                                                   │
    │   │   - 记录函数调用                                                      │
    │   │   - 收集执行日志                                                      │
    │   │                                                                        │
    │   └── 8.3 分析结果                                                        │
    │       - 检查执行状态                                                      │
    │       - 识别异常                                                          │
    │       - 生成报告                                                          │
    │                                                                            │
    ▼                                                                            │
[9] 结果输出                                                                    │
    ├── 生成分析报告                                                            │
    │   - full_info_TIMESTAMP.json                                              │
    │   - function_classify_FUNC_TIMESTAMP.json                                 │
    │   - replacement_update_FUNC_TIMESTAMP.json                                │
    │                                                                            │
    └── 保存替换代码                                                            │
        - 输出到源文件                                                          │
```

### 4.2 函数分类流程

```
┌─────────────────────────────────────────────────────────────────┐
│                  Analyzer Agent 函数分类流程                     │
└─────────────────────────────────────────────────────────────────┘

输入: 函数名列表
输出: FunctionClassifyResponse

┌──────────────┐
│ 开始         │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 1. 获取函数基本信息                       │
│    - get_function_info(func_name)        │
│    - 返回: FunctionInfo                   │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 2. 获取 MMIO 相关信息                     │
│    - get_mmio_func_info(func_name)       │
│    - 返回: MMIO 表达式、寄存器访问        │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 3. 获取调用栈                             │
│    - get_func_call_stack(func_name)      │
│    - 返回: 调用者和被调用者               │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 4. 获取相关结构体/枚举                    │
│    - get_struct_or_enum_info()           │
│    - 返回: 类型定义                       │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 5. LLM 分析                              │
│    - 调用 LangChain 模型                  │
│    - 使用 function_classifier 提示词      │
│    - 输出: FunctionClassifyResponse       │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 6. 验证替换代码 (可选)                    │
│    - verify_replacement()                │
│    - Rubric 检查                          │
│    - 编译验证 (可选)                      │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────┐
│ 返回结果     │
│ - function_type: MMIO | DRIVER | LOGIC | CORE
│ - has_replacement: true | false
│ - recommended_code: ...
└──────────────┘
```

### 4.3 函数修复流程

```
┌─────────────────────────────────────────────────────────────────┐
│                   Fixer Agent 函数修复流程                       │
└─────────────────────────────────────────────────────────────────┘

触发条件: 编译失败或仿真错误

┌──────────────┐
│ 开始         │
│ 输入: 函数名, 错误信息
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 1. 获取函数分析信息                       │
│    - get_function_analysis_and_replacement()
│    - 返回: mmio_info + replacement_history
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 2. 获取文件上下文                         │
│    - get_replace_func_details_by_file() │
│    - 返回: 同文件其他函数信息             │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 3. 获取仿真信息 (如果有)                  │
│    - mmio_function_emulate_info()        │
│    - 返回: 函数调用日志                   │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 4. LLM 生成修复代码                       │
│    - 分析错误原因                         │
│    - 参考 replacement_history            │
│    - 使用 function_fixer 提示词           │
│    - 输出: ReplacementUpdate              │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────┐
│ 5. 更新替换代码                           │
│    - update_function_replacement()       │
│    - 保存到 replacement_updates          │
│    - 记录到 replacement_history           │
└──────┬───────────────────────────────────┘
       │
       ▼
┌──────────────┐
│ 返回结果     │
│ - replacement_code: ...
│ - reason: ...
└──────────────┘
```

---

## 5. 核心数据结构

### 5.1 FunctionInfo（函数信息）

```python
@dataclass
class FunctionInfo:
    name: str                           # 函数名
    file_path: str                      # 文件路径
    location_line: int                  # 起始行号
    function_content: str               # 函数完整代码
    function_content_in_lines: Dict     # 按行存储的代码
```

### 5.2 FunctionClassifyResponse（函数分类响应）

```python
@dataclass
class FunctionClassifyResponse:
    function_name: str                  # 函数名
    function_type: str                  # 类型: MMIO | DRIVER | LOGIC | CORE
    usage_type: str                     # 用途描述
    has_replacement: bool               # 是否需要替换
    reason: str                         # 分类原因
    original_code: str                  # 原始代码
    recommended_code: str               # 推荐替换代码
    confidence: float                   # 置信度 (0-1)
```

**函数类型说明：**

| 类型 | 说明 | 是否替换 |
|------|------|----------|
| `MMIO` | 内存映射 I/O 函数 | ✅ 替换为 stub |
| `DRIVER` | 驱动层函数 | ✅ 可能替换 |
| `LOGIC` | 纯逻辑函数 | ❌ 不替换 |
| `CORE` | RTOS 核心/调度器 | ❌ 禁止替换 |

### 5.3 ReplacementUpdate（替换更新）

```python
@dataclass
class ReplacementUpdate:
    function_name: str                  # 函数名
    replacement_code: str               # 替换代码
    reason: str                         # 替换原因
```

### 5.4 DataManager（数据管理器）

```python
class DataManager:
    # MMIO 函数信息
    mmio_info_list: Dict[str, FunctionClassifyResponse]
    mmio_infos_by_file: Dict[str, List[FunctionClassifyResponse]]
    
    # 替换更新
    replacement_updates: Dict[str, ReplacementUpdate]
    replacement_updates_by_file: Dict[str, List[ReplacementUpdate]]
    
    # 替换历史（重要：支持迭代修复）
    replacement_history: Dict[str, List[Dict]]
```

---

## 6. 模块依赖关系

```
                    ┌─────────┐
                    │ main.py │
                    └────┬────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ config  │    │ agents  │    │  tools  │
    │         │    │         │    │         │
    │ globs   │    │analyzer │    │builder  │
    │ llm_    │    │builder  │    │collector│
    │ config  │    │fixer    │    │replacer │
    │ model_  │    │emulator │    │emulator │
    │ singleton│   │         │    │         │
    └────┬────┘    └────┬────┘    └────┬────┘
         │              │              │
         │    ┌─────────┼─────────┐    │
         │    │         │         │    │
         │    ▼         ▼         ▼    │
         │ ┌───────┐ ┌───────┐ ┌─────┐│
         │ │ core  │ │prompts│ │models│
         │ │       │ │       │ │      ││
         │ │data_  │ │func_  │ │query_ ││
         │ │manager│ │class- │ │results││
         │ │       │ │ifier  │ │analyze││
         │ │       │ │func_  │ │       ││
         │ │       │ │fixer  │ │       ││
         │ └───────┘ └───────┘ └─────┘│
         │                            │
         └────────────┬───────────────┘
                      │
                      ▼
                 ┌─────────┐
                 │  utils  │
                 │         │
                 │db_query │
                 │db_file  │
                 │db_cache │
                 │src_ops  │
                 │log      │
                 └────┬────┘
                      │
                      ▼
                 ┌─────────┐
                 │ fuzzemu │
                 │         │
                 │handlers │
                 │models   │
                 └─────────┘
```

---

## 7. 关键设计决策

### 7.1 为什么使用 CodeQL？

**决策：** 使用 CodeQL 作为静态分析引擎

**原因：**
- CodeQL 提供强大的代码查询能力（Datalog 语言）
- 支持多种语言（C/C++、Python、Java 等）
- 可自定义查询规则，灵活提取代码信息
- 数据库可复用，支持增量分析
- 开源且社区活跃

**权衡：**
- 需要预先构建数据库（首次构建耗时 5-30 分钟）
- 学习 Datalog 语法有一定门槛
- 对大型项目（100万+ 行）内存占用较高（4-8GB）

### 7.2 为什么使用 LangGraph + LangChain？

**决策：** 使用 LangGraph 构建 Agent 工作流

**原因：**
- 支持复杂的状态管理（MessagesState）
- 内置工具调用机制（ToolNode）
- 易于调试和追踪（支持 checkpointing）
- 支持多 Agent 协作
- 社区活跃，文档完善

**权衡：**
- 依赖较多（langchain, langgraph, langchain-mcp-adapters）
- 版本更新频繁，需要跟进
- 抽象层较多，调试需要深入

### 7.3 为什么分离 Collector 和 Analyzer？

**决策：** 将代码收集（Collector）和 AI 分析（Analyzer）分离

**原因：**
- **可复用性**：Collector 可独立使用（MCP 服务器），供其他工具调用
- **性能**：减少重复查询，CodeQL 查询结果可缓存
- **可测试性**：Collector 和 Analyzer 可分别测试
- **增量分析**：支持只分析变更的函数

**权衡：**
- 需要维护两套接口（直接调用 + MCP）
- 数据结构需要在多处定义

### 7.4 为什么使用 DataManager 单例？

**决策：** 使用全局 DataManager 单例管理所有分析数据

**原因：**
- **数据一致性**：所有 Agent 访问同一份数据
- **缓存复用**：避免重复加载 MMIO 函数信息
- **历史追踪**：支持 replacement_history，便于迭代修复
- **简化接口**：Agent 不需要传递 db_path 等参数

**权衡：**
- 全局状态可能导致测试困难
- 需要注意并发访问（使用 threading.Lock）

### 7.5 为什么使用 MCP 接口？

**决策：** 提供 MCP（Model Context Protocol）服务器接口

**原因：**
- **标准化**：MCP 是 AI 工具互操作的开放协议
- **集成友好**：支持与 Cline、Cursor 等工具集成
- **解耦**：工具可独立部署，通过网络调用
- **扩展性**：易于添加新工具

---

## 8. 扩展点

### 8.1 添加新的 HAL 支持

在 `fuzzemu/fuzzemu/handlers/` 下添加新的处理器：

```python
# fuzzemu/fuzzemu/handlers/nxp_hal/nxp_i2c.py
from fuzzemu.handlers.base import BaseHandler

class NXP_I2C_Handler(BaseHandler):
    """NXP I2C HAL 处理器"""
    
    def get_supported_functions(self):
        return [
            "I2C_MasterInit",
            "I2C_MasterTransferNonBlocking",
            "I2C_MasterGetTransferStatus",
        ]
    
    def handle(self, call):
        func_name = call.function_name
        args = call.arguments
        
        if func_name == "I2C_MasterInit":
            # 模拟 I2C 初始化
            return {"status": "kStatus_Success"}
        
        elif func_name == "I2C_MasterTransferNonBlocking":
            # 模拟 I2C 传输
            return {"status": "kStatus_Success"}
```

### 8.2 添加新的测试用例

在 `testcases/` 下创建新目录：

```
testcases/server/nxp/NXP_SPI_FreeRTOS/
├── lcmhal_config.yml    # 配置文件
│   script_path: "/path/to/testcase"
│   db_path: "/path/to/database"
│   src_path: "/path/to/source"
│   proj_path: "/path/to/project"
│
├── build.sh             # 构建脚本
│   #!/bin/bash
│   # 1. 配置 CMake
│   # 2. 编译项目
│   # 3. 生成 output.elf
│
├── clear.sh             # 清理脚本
│   #!/bin/bash
│   # 删除 build/ 目录
│
└── emulate/             # 仿真配置（自动生成）
    ├── base_config.yml
    ├── semu_config.yml
    ├── semu_rule.txt
    ├── output.elf
    └── output.bin
```

### 8.3 添加新的 Agent

在 `agents/` 下创建新代理：

```python
# agents/my_agent.py
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.tools import tool
from config.model_singleton import get_model

# 定义状态
class MyAgentState(MessagesState):
    function_name: str
    result: str

# 定义工具
@tool
def my_tool(input: str) -> str:
    """工具描述"""
    return f"处理结果: {input}"

# 构建图
async def build_graph():
    model = get_model()
    tools = [my_tool]
    model_with_tools = model.bind_tools(tools)
    
    graph = StateGraph(MyAgentState)
    
    # 添加节点
    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(tools))
    
    # 添加边
    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", should_continue)
    graph.add_edge("tools", "agent")
    graph.add_edge("agent", END)
    
    return graph.compile()

# 入口函数
async def run_my_agent(function_name: str):
    graph = await build_graph()
    result = await graph.ainvoke({
        "function_name": function_name,
        "messages": []
    })
    return result
```

### 8.4 添加新的 CodeQL 查询

在 `queries/collectors/` 下添加新查询：

```ql
// queries/collectors/common/spi_function_collector.ql

import cpp

// 查找所有 SPI 相关函数
select 
    f.getName() as func_name,
    f.getFile().getAbsolutePath() as file_path,
    f.getLocation().getStartLine() as line_number
from 
    Function f
where
    f.getName().toLowerCase().matches("%spi%") or
    f.getName().toLowerCase().matches("%miso%") or
    f.getName().toLowerCase().matches("%mosi%")
```

---

## 9. 支持的平台和外设

### 9.1 芯片平台

| 平台 | 架构 | 状态 | 说明 |
|------|------|------|------|
| STM32F4 | ARM Cortex-M4 | ✅ 完整支持 | HAL 库完善，测试覆盖 |
| STM32F7 | ARM Cortex-M7 | ✅ 完整支持 | 与 F4 类似 |
| STM32H7 | ARM Cortex-M7 | 🚧 部分支持 | 高性能系列 |
| NXP i.MX RT | ARM Cortex-M7 | 🚧 部分支持 | MCUXpresso SDK |
| Ambiq Apollo | ARM Cortex-M4 | 📋 计划中 | 低功耗系列 |
| Nordic nRF52 | ARM Cortex-M4 | 📋 计划中 | BLE 专用 |
| ESP32 | Xtensa/RISC-V | 📋 计划中 | WiFi/BLE |

### 9.2 外设类型

| 外设 | 状态 | 说明 |
|------|------|------|
| UART/LPUART | ✅ | 完整支持，包括 DMA 模式 |
| I2C | 🚧 | 基本支持，DMA 模式开发中 |
| SPI | 📋 | 计划中 |
| ETH (LwIP) | ✅ | 支持 TCP/IP 协议栈 |
| Flash (FATFS) | ✅ | 支持文件系统 |
| BLE | 📋 | 计划中 |
| CAN | 📋 | 计划中 |
| USB | 📋 | 计划中 |

### 9.3 RTOS 支持

| RTOS | 状态 | 说明 |
|------|------|------|
| FreeRTOS | ✅ | 完整支持，测试覆盖 |
| RT-Thread | 🚧 | 部分支持，适配中 |
| Zephyr | 📋 | 计划中 |
| 裸机 (BareMetal) | ✅ | 完整支持 |
| uC/OS | 📋 | 计划中 |

---

## 10. MCP 接口

LCMHalMCP 提供 MCP（Model Context Protocol）服务器接口，支持与其他 AI 工具集成。

### 10.1 配置示例

```json
{
  "mcpServers": {
    "lcmhal-collector": {
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
    },
    "lcmhal-builder": {
      "timeout": 600,
      "command": "python",
      "args": [
        "-m",
        "tools.builder.mcp_server",
        "--script-dir",
        "$TESTCASE_DIR"
      ],
      "type": "stdio"
    },
    "lcmhal-emulator": {
      "timeout": 300,
      "command": "python",
      "args": [
        "-m",
        "tools.emulator.mcp_server",
        "--script-dir",
        "$TESTCASE_DIR"
      ],
      "type": "stdio"
    }
  }
}
```

### 10.2 可用工具

#### Collector MCP 工具

| 工具名 | 说明 | 参数 |
|--------|------|------|
| `get_function_info` | 获取函数信息 | `func_name: str` |
| `get_mmio_func_info` | 获取 MMIO 函数详情 | `func_name: str` |
| `get_mmio_func_list` | 获取 MMIO 函数列表 | 无 |
| `get_struct_or_enum_info` | 获取结构体/枚举 | `struct_name: str` |
| `get_func_call_stack` | 获取调用栈 | `func_name: str, layer_cnt: int` |
| `get_driver_info` | 获取驱动信息 | `driver_name: str` |

#### Builder MCP 工具

| 工具名 | 说明 | 参数 |
|--------|------|------|
| `build_project` | 构建项目 | 无 |
| `update_function_replacement` | 更新函数替换 | `func_name, replace_code, reason` |
| `get_replace_func_details_by_file` | 获取文件替换详情 | `file_path: str` |
| `get_function_analysis_and_replacement` | 获取函数分析和替换 | `func_name: str` |

#### Emulator MCP 工具

| 工具名 | 说明 | 参数 |
|--------|------|------|
| `emulate_proj` | 运行仿真 | 无 |
| `mmio_function_emulate_info` | 获取 MMIO 函数仿真信息 | `func_name: str` |
| `function_calls_emulate_info` | 获取函数调用仿真信息 | `func_name: str` |

---

## 11. 快速开始

### 11.1 环境准备

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 安装 CodeQL CLI
# 参考: https://github.com/github/codeql-cli-binaries

# 3. 安装 ARM 工具链
sudo apt install gcc-arm-none-eabi

# 4. 安装 QEMU（可选，用于仿真）
sudo apt install qemu-system-arm
```

### 11.2 运行测试

```bash
# 1. 进入项目目录
cd ~/workspace/lcmhalmcp

# 2. 运行测试用例
python main.py run testcases/server/nxp/NXP_UART_FreeRTOS

# 3. 查看结果
# 日志位于: /path/to/db/lcmhal_ai_log/
# - full_info_TIMESTAMP.json        # 全量信息
# - function_classify_FUNC_*.json   # 函数分类结果
# - replacement_update_FUNC_*.json  # 替换更新记录
```

### 11.3 恢复代码

```bash
# 恢复所有被替换的文件
python main.py recover testcases/server/nxp/NXP_UART_FreeRTOS

# 清理特定函数的分析日志
python main.py clean testcases/server/nxp/NXP_UART_FreeRTOS \
    --func-name HAL_UART_Transmit \
    --type all \
    --recover
```

### 11.4 启动 MCP 服务器

```bash
# 启动 Collector MCP 服务器
python -m tools.collector.mcp_server \
    --db-path /path/to/database \
    --transport stdio

# 启动 Builder MCP 服务器
python -m tools.builder.mcp_server \
    --script-dir /path/to/testcase

# 启动 Emulator MCP 服务器
python -m tools.emulator.mcp_server \
    --script-dir /path/to/testcase
```

---

## 12. 常见问题

### 12.1 CodeQL 数据库构建失败

**问题：** `codeql database create` 失败

**解决方案：**
1. 确保安装了 CodeQL CLI
2. 确保构建命令正确（build.sh 可独立运行）
3. 检查内存是否充足（建议 8GB+）

### 12.2 编译失败后无法自动修复

**问题：** Builder Agent 无法修复编译错误

**解决方案：**
1. 检查 `lcmhal_ai_log/` 中的日志
2. 手动查看编译错误信息
3. 可能需要调整 `prompts/function_fixer.py` 中的提示词

### 12.3 仿真运行崩溃

**问题：** QEMU 仿真崩溃

**解决方案：**
1. 检查 `emulate/semu_config.yml` 配置
2. 检查 MMIO 函数是否正确替换
3. 查看 `fuzzemu` 处理器是否支持该函数

---

## 13. 文档版本

- **版本:** 2.0
- **更新日期:** 2026-03-05
- **作者:** 龙虾哥 🦞
- **代码量:** ~39,000 行
- **文档长度:** ~1,500 行
