---
name: fuzzemu_local_development
description: 在仓库内修改 fuzzemu 并本地安装的通用流程，适用于所有对 fuzzemu 源码/配置的更新场景
---

# 在仓库内更新 fuzzemu（通用流程）

## 原则

**不要直接改 Python 环境里已安装的 fuzzemu 源码**（如 `site-packages/fuzzemu/`）。所有对 fuzzemu 的修改都应在**本仓库的 `fuzzemu/` 子目录**中完成，然后通过 `pip install .` 安装，使改动生效。

适用于：新增/修改配置项、改 hook 逻辑、改 handler、改循环检测、改内存或规则等**任意**对 fuzzemu 内容的更新。

## 目录与入口

- **本地源码位置**：`<repo>/fuzzemu/`
  - 包主体：`fuzzemu/fuzzemu/`（`models/`、`configuration/`、`emulate/`、`handlers/`、`log/` 等）
  - 入口：`fuzzemu/harness.py`（主程序）、`fuzzemu/helper/main.py`（fuzzemu-helper）
  - 安装定义：`fuzzemu/setup.py`
- **设计文档**：`fuzzemu/fuzzemu_lcmhal_design_doc.md`（与 lcmhal 相关的设计说明）

## 配置如何生效

1. **lcmhal 侧**：`tools/emulator/conf_generator.py` 生成 `base_config.yml`（含各 elf 的配置字典，如 `output.elf`）。
2. **fuzzemu-helper**：`fuzzemu-helper config base_config.yml -s` 会调用 `dump_config.config()`，根据 base_config 生成对应目录下的 `semu_config.yml`（或 `{model}_config.yml`），并合并 include（如 `syms.yml`）。
3. **运行时**：fuzzemu 通过 `configuration/config.py` 的 `get_config(config_path)` 加载该 yml，与 `default_config` 合并后得到 `globs.config`；新增配置项需在 `default_config` 里设默认值，否则可能读不到。

因此：**新增配置项时**，在 `fuzzemu/configuration/config.py` 的 `default_config` 里增加默认值；在 lcmhal 侧则在 `conf_generator.py` 的 `baseconfig_dict` 或 `customize_emulator_config()` 里提供具体值。

## 修改后安装

在仓库根目录下执行：

```bash
cd /path/to/lcmhalmcp/fuzzemu
pip install .
```

如需边改边测，可用可编辑安装：

```bash
cd /path/to/lcmhalmcp/fuzzemu
pip install -e .
```

安装后，当前环境中的 `fuzzemu`、`fuzzemu-helper` 会使用仓库内 `fuzzemu/` 的代码和配置。

## 示例：循环检测白名单（loop_whitelist）

- **需求**：某些函数（如 C 运行时初始化）不参与死循环检测，需白名单机制。
- **配置**：在 `config.py` 的 `default_config` 中已有 `loop_whitelist=[]`；在 `base_config.yml` 的 `output.elf` 下配置 `loop_whitelist: [memset, FillZerobss, ...]`，或由 `conf_generator.py` 的 `baseconfig_dict['output.elf']['loop_whitelist']` 统一维护。
- **实现**：在 `fuzzemu/models/loop_queue.py` 的 `_loopcheck_hook` 里，在调用 `loop_detect` 前用 `get_pc_function(uc)` 取当前函数名，若在 `globs.config.loop_whitelist` 中则直接 `return`，不执行本次检测。
- **相关**：误报分析与常见初始化函数见 skill `analyze_loop_false_positive`。

其他类型的更新（新 handler、新规则、新 hook 等）同样：在 `fuzzemu/` 子目录改代码或配置默认值，必要时在 `conf_generator.py` 或 base_config 里补配置，最后在 `fuzzemu/` 下执行 `pip install .` 使改动生效。
