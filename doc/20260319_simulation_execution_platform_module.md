# 动态执行环境 / 仿真执行平台模块

**日期**: 2026-03-19  
**适用范围**: LCMHalMCP 论文写作，聚焦「仿真执行平台」本身，不涉及工作流编排  
**证据范围**: `tools/emulator/`、`doc/fuzzemu_execution_flow.md`、`doc/fuzzemu_vfp_skip_design.md`、`testcases/**/emulate/`

---

## 1. 概述

仿真执行平台是 LCMHalMCP 中负责在无真实硬件环境下运行替换后固件的模块。该模块基于 fuzzemu 框架，通过配置生成、符号提取、handler 绑定与执行控制，实现固件的可控模拟执行，并为上层工作流提供执行结果与诊断信息。

---

## 2. 循环检测与异常检测

### 2.1 异常循环的判定与终止

仿真器（fuzzemu）在 emulate 模式下会进行基本块级别的循环检测。当检测到「非白名单内的函数陷入循环」时，fuzzemu 会主动终止执行，并在 `emulate/debug_output/lcmhal.txt` 中写入固定格式的终止信息：

```
[-] Stop due to exceptional loop.
current function: <函数名>
current caller function: <调用者函数名>
---------- LCMHAL EXECUTION END ----------
end pc: 0x<地址>
```

**父侧判定逻辑**：`tools/emulator/core.py` 中的 `emulate_proj()` 在仿真结束后，读取 `lcmhal.txt` 全文，若包含字符串 `exceptional loop`，则置 `has_loop = True`。成功判定为：`success = (ret.returncode == 0 and not has_loop)`。即：**exit_code 为 0 且 lcmhal.txt 中未出现 exceptional loop 时，才视为仿真成功**。

**白名单机制**：`tools/emulator/conf_generator.py` 的 `baseconfig_dict['output.elf']['loop_whitelist']` 定义了应跳过循环检测的函数，包括 `memset`、`memcpy`、`memmove`、`FillZerobss`、`LoopFillZerobss`、`CopyDataInit`、`LoopCopyDataInit`、`Zero_Init`、`Reset_Handler`、`SystemInit`。这些函数在启动或初始化阶段包含合法循环，若不做白名单处理会导致误判为 exceptional loop。

**其他循环检测参数**：fuzzemu 的设计文档给出了循环检测的额外可调参数，并通过其配置/规则机制生效，例如：

- `skip_first_n_unique_blocks`：在固件初始化早期跳过前 N 个“唯一基本块”的循环检测，避免初始化阶段的结构性重复被误判为死循环
- `max_loop_times`：最大循环次数（fuzzemu 配置参数），用于限制循环检测的执行上限；当循环检测进入停止路径时，会通过 `lcmhal.txt` 输出 `exceptional loop` 终止信息

### 2.2 UNMAPPED / fault PC 的异常诊断

当仿真因内存访问异常（如 `UC_ERR_READ_UNMAPPED`）退出时，fuzzemu 会在 stdout 中输出 `UNMAPPED` 或 `fault PC: 0x...` 等信息。这些属于**异常诊断信息**，由父侧从 `emulate/debug_output/stdout.txt`（即仿真进程的 stdout 持久化）中抽取。

**解析与映射**：`tools/emulator/core.py` 中的 `get_fault_function_from_emulate_output()` 负责：

1. 读取 `stdout.txt`（或传入的 `emulate_stdout` 字符串）；
2. 若内容中不含 `UNMAPPED` 且不含 `fault PC:`，则返回空字符串；
3. 使用正则 `r"fault\s+PC:\s*0x([0-9a-fA-F]+)"` 提取 fault PC 的十六进制地址；
4. 从 `emulate/syms.yml` 解析符号表，格式为 `addr: symbol_name`（十进制或十六进制地址）；
5. 取 `addr <= fault_pc` 的最大 `addr` 对应的符号名，作为 fault 所在函数名返回。

`syms.yml` 由 `conf_generator.extract_syms()` 从 `output.elf` 中提取，使用 pyelftools 遍历符号表，将 `{st_value: name}` 写入 YAML。因此 fault PC 到函数名的映射依赖符号表覆盖该 PC 的最近前驱符号。

---

## 3. 仿真接口支持

### 3.1 HAL_BE_* 与 fuzzemu.handlers.common 的映射

固件中的 MMIO 操作被改写为对 `HAL_BE_*` 弱符号的调用。仿真时，fuzzemu 不执行 C 中的弱实现，而是根据 `semu_config.yml` 的 `handlers` 字段，将控制权切换到对应的 Python handler。

**基础映射**（`tools/emulator/conf_generator.py` 中的 `_base_handlers`）：

| HAL_BE_* 符号 | fuzzemu handler |
|---------------|-----------------|
| `HAL_BE_ENET_ReadFrame` | `fuzzemu.handlers.common.hal_read_frame` |
| `HAL_BE_In` | `fuzzemu.handlers.common.hal_in` |
| `HAL_BE_Out` | `fuzzemu.handlers.common.hal_out` |
| `HAL_BE_return_0` | `fuzzemu.handlers.common.return_zero` |
| `HAL_BE_return_1` | `fuzzemu.handlers.common.return_true` |
| `HAL_BE_Block_Read` | `fuzzemu.handlers.common.hal_block_in` |
| `HAL_BE_Block_Write` | `fuzzemu.handlers.common.hal_block_out` |

**参数与返回值约定**：`hal_in` / `hal_out` 从 `input.bin` 读写数据；`hal_read_frame` 用于以太网帧读取；`hal_block_in` / `hal_block_out` 用于块设备；`return_zero` / `return_true` 直接返回 r0=0 或 r0=1，用于无数据交换的成功/失败语义。

**扩展 handler 列表**：除 `_base_handlers` 外，`conf_generator.py` 还定义了：

- `HANDLERS_DO_RETURN_LIST`：遇到即 `do_return`（跳过原逻辑），如 `puts`、`fflush`、`DP83848_Init`、`rt_thread_mdelay`、`DelayLoop`、`LPUART_WriteBlocking`、`ENET_SetSMI` 等；
- `HANDLERS_RETURN_ZERO_LIST`：跳过并 r0=0，如 `HAL_RCC_ClockConfig`、`HAL_ETH_ReadPHYRegister`、`ethernetif_phy_init`、`PHY_Init`；
- `HANDLERS_RETURN_2_LIST`：跳过并 r0=2（如 100M 全双工 link up），如 `DP83848_GetLinkState`、`PHY_GetLinkStatus`、`PHY_GetLinkSpeedDuplex`；
- `HANDLERS_RETURN_PHY_ID_LIST`：跳过并 r0=0x2000（DP83848 PHY ID），如 `ENET_MDIORead`。

### 3.2 semu_config.yml 的生成与修正

**生成流程**（`conf_generator.generate_semu_config()`）：

1. 校验 `base_config.yml` 存在且格式正确（顶层 key 为 `output.elf`，且含 `rules`）；
2. 若无效则调用 `generate_base_config()` 重新生成；
3. 确保 `semu_rule.txt`、`base_input/input.bin` 存在；
4. 执行 `fuzzemu-helper config base_config.yml -s`，在 `emulate/` 下生成 `semu_config.yml`；
5. 调用 `fix_flash_size()` 根据 `output.bin` 实际大小修正 `memory_map.flash`（4KB 对齐，移除与 flash 重叠的 region）；
6. 调用 `fix_initial_sp_from_syms()`：若 `syms.yml` 中存在 `_estack`，用其值覆盖 `semu_config.yml` 的 `initial_sp`。

**典型 semu_config.yml 结构**（以 `testcases/server/nxp/NXP_LwIP_BareMetal/emulate/semu_config.yml` 为例）：

- `emulate_mode: emulate`
- `enable_native: false`
- `entry_point`、`initial_sp`、`isr_vector`
- `loop_whitelist`：与 base_config 一致
- `handlers`：符号名到 handler 路径的映射
- `memory_map`：`flash`（base_addr、file、permissions、size）、`ram`、`mmio`、`nvic`、`irq_ret`、`peripheral` 等
- `mmio_funcs`：需追踪的驱动函数列表
- `rules`、`model`、`include`（如 `./syms.yml`）

### 3.3 内存映射与执行初始化（memory_map / entry_point / initial_sp）

fuzzemu 的模拟执行需要同时满足两类关键信息：**地址空间映射**与**初始执行上下文**。

1) 内存映射（`memory_map`）

`semu_config.yml` 会提供多个内存区域（示例：`flash`、`ram`、`mmio`、`nvic`、`peripheral`、`peripheral_ram`、`irq_ret`），用于让 Unicorn 在对应地址上能够正确读写/取指。父侧在 `tools/emulator/conf_generator.py` 的 `fix_flash_size()` 中会根据 `emulate/output.bin` 的实际大小修正 `memory_map.flash` 的 `base_addr/size`（对齐到 4KB），并移除与 flash 重叠的 region，避免 Unicorn 出现映射冲突或取指越界问题。

2) 初始栈与入口点（`initial_sp` / `entry_point` / `isr_vector`）

`semu_config.yml` 明确包含 `entry_point`、`initial_sp`、`isr_vector` 等字段，用于让模拟器从正确位置开始执行并设置初始栈指针。为了提高与固件链接脚本的一致性，父侧在 `conf_generator.fix_initial_sp_from_syms()` 中：若 `emulate/syms.yml` 中存在 `_estack`，则会用该值覆盖 `semu_config.yml` 的 `initial_sp`。

### 3.4 仿真进程的启动与超时

**启动方式**（`tools/emulator/emulate_runner.run_emulator()`）：

```
python -m fuzzemu.harness <input_file> <config_file> -d 5 --skip-mmio-hook
```

- `input_file`：`{script_path}/emulate/base_input/input.bin`
- `config_file`：`{script_path}/emulate/semu_config.yml`
- `cwd`：`{script_path}/emulate`
- `-d 5`：debug 等级
- `--skip-mmio-hook`：跳过 MMIO hook，由 handlers 接管

**超时处理**：`subprocess.run` 设置 `timeout=180`（3 分钟）。若超时，`TimeoutExpired` 被捕获，返回码置为 0，并在 stdout 末尾追加 `3min timeout: emulate exceeded 180 seconds`，以便父侧统一处理。

---

## 4. 驱动函数追踪

### 4.1 mmio_funcs 与 lcmhal.txt

`semu_config.yml` 中的 `mmio_funcs` 列表决定了**哪些函数在进入时会被记录到 lcmhal.txt**。该列表由 `conf_generator.mmio_funcs_emulate_config()` 从 CodeQL 数据库的 `get_mmio_func_list(globs.db_path)` 获取，写入 `baseconfig_dict['output.elf']['mmio_funcs']`，最终经 fuzzemu-helper 合并进 `semu_config.yml`。

**lcmhal.txt 日志格式**：

- **MMIO 函数进入记录**（每行一条）：
  ```
  <时间戳> - <当前PC> irq <irq号>-> <目标PC> <函数名> (from <调用者PC> <调用者函数名>)
  ```
  示例：`0x8015be4 irq 0x0-> 0x80157a8 HAL_MspInit (from 0x8015bb0 HAL_Init)`

- **异常循环终止记录**：
  ```
  [-] Stop due to exceptional loop.
  current function: <卡住时的函数>
  current caller function: <调用者>
  ---------- LCMHAL EXECUTION END ----------
  end pc: 0x<地址>
  ```

字段含义：`irq 0x0` 表示非中断上下文；`from 0x... CALLER` 表示调用链中的上一级。

### 4.2 function.txt 与调用栈压缩

fuzzemu 还会将函数调用序列写入 `emulate/debug_output/function.txt`。每行格式为：

```
<序号> <PC> irq <irq号>-> <目标PC> <函数名> (from <调用者PC> <调用者函数名>)
```

**压缩输出**：`tools/emulator/core.py` 的 `function_calls_emulate_info()` 会对 `function.txt` 做压缩处理：

1. **连续重复行**：多行相同核心内容合并为 `start_seq-end_seq <内容> (重复N次)`；
2. **多行循环**：检测长度为 2 至 `max_loop_lines`（默认 5）的循环模式，合并为 `[LOOP] start_seq-end_seq (重复N次)` 加循环内各行；
3. **行数限制**：若超过 `max_output_lines`（默认 1000），只保留末尾行，并在开头插入 `[TRUNCATED]` 提示。

压缩后的输出供 Fixer Agent 等上层组件分析调用栈与循环模式，用于定位 exceptional loop 或 fault 的上下文。

---

## 5. 补充：VFP 指令跳过

部分固件（如带 LwIP、libjpeg 的 STM32/FreeRTOS demo）会生成 VFP 指令。Unicorn 对部分 VFP 编码未实现，执行时会抛出 `UC_ERR_INSN_INVALID`。根据 `doc/fuzzemu_vfp_skip_design.md`，fuzzemu 在 emulate 模式下，当 `errno == UC_ERR_INSN_INVALID` 时，会尝试判定当前 PC 处是否为可跳过的 VFP 指令；若是，则将 PC 推进到下一条指令并继续执行，从而避免因单条不支持的 VFP 指令导致整次模拟崩溃。该逻辑仅对 `UC_ERR_INSN_INVALID` 生效，对 `UC_ERR_READ_UNMAPPED` 等不做跳过。

在进入“VFP 跳过”分支之前，fuzzemu 会在 Unicorn 初始化阶段尝试显式启用 VFP（通过写 `FPEXC.EN` 与 `CPACR: cp10/cp11 full access`），以降低无关的非法指令比例；但由于 Unicorn 对部分 Thumb-2 VFP 编码仍存在缺口，所以仍需要跳过策略作为兜底。

---

## 6. 小结

仿真执行平台模块通过以下机制支撑 LCMHalMCP 的动态验证：

1. **循环检测**：fuzzemu 在基本块级别检测循环，`loop_whitelist` 过滤启动/初始化阶段的合法循环；父侧通过 `lcmhal.txt` 中的 `exceptional loop` 判定仿真是否因异常循环终止。
2. **异常诊断**：`UNMAPPED` / `fault PC` 从 stdout 抽取，经 `get_fault_function_from_emulate_output()` 解析 fault PC 并映射到 `syms.yml` 中的函数名。
3. **仿真接口**：`HAL_BE_*` 通过 `handlers` 映射到 `fuzzemu.handlers.common.*`；`semu_config.yml` 由 `base_config.yml` 经 `fuzzemu-helper config -s` 生成，再经 `fix_flash_size`、`fix_initial_sp_from_syms` 修正；仿真通过 `python -m fuzzemu.harness` 启动，带 3 分钟超时保护。
4. **驱动函数追踪**：`mmio_funcs` 决定被记录到 `lcmhal.txt` 的函数；`function.txt` 经 `function_calls_emulate_info()` 压缩后供上层分析调用栈与循环模式。
