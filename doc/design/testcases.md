# Testcase 与实验矩阵设计

## 1. 单个 testcase 结构

一个标准 testcase 至少包含：

```text
<testcase>/
├── build.sh
├── clear.sh
├── lcmhal_config.yml
└── emulate/
    ├── output.elf
    ├── output.bin
    ├── syms.yml
    ├── base_config.yml
    ├── semu_config.yml
    ├── base_input/input.bin
    └── debug_output/
        ├── stdout.txt
        ├── stderr.txt
        ├── function.txt
        ├── lcmhal.txt
        └── debug.txt
```

`emulate/` 下的文件由构建和 `tools/emulator/conf_generator.py` 生成或刷新。

## 2. `lcmhal_config.yml`

关键字段：

- `script_path`：testcase 目录。
- `db_path`：CodeQL database 目录。
- `src_path`：真实源码根目录，用于源码替换。
- `proj_path`：项目工程根目录，用于路径映射与构建。

可选实验字段：

- `experiment_mode`：`full` 或 `no_feedback`。
- `tool_profile`：`full` 或 `minimal`。
- `analyzer_recursion_limit`：Analyzer LangGraph 最大步数。
- `llm_usage_log_enable`：是否记录 LLM token 和耗时。

## 3. Server testcase 矩阵

`testcases/server/` 是主要实验矩阵：

- `stm32/`
  - `LwIP_StreamingServer`
  - `LwIP_HTTP_Server_Raw`
  - `LwIP_HTTP_Server_Socket_RTOS`
  - `UART_Hyperterminal_IT`
  - `FatFs_USBDisk_RTOS`
  - `BLE_HeartRateFreeRTOS`
- `nxp/`
  - `NXP_UART_BareMetal` / `NXP_UART_FreeRTOS`
  - `NXP_I2C_BareMetal` / `NXP_I2C_FreeRTOS`
  - `NXP_LwIP_BareMetal` / `NXP_LwIP_FreeRTOS`
  - `NXP_FATFS_BareMetal` / `NXP_FATFS_FreeRTOS`
- `rtthread/`
  - `imxrt1052-nxp-evk`
  - `stm32f401-st-nucleo`
- `zephyr/`
  - `stm32/`
  - `nxp/`
  - `atmel/`

## 4. Zephyr testcase

Zephyr 目录按厂商和 sample 组织，每个 sample 仍提供 `build.sh`、`clear.sh`、`lcmhal_config.yml`。构建方式是进入 Zephyr workspace，通过 `west build` 构建，并复制 `zephyr.elf` 到 testcase 的 `emulate/output.elf`。

默认环境：

```shell
export ZEPHYR_PROJECT=/home/haojie/zephyrproject
```

矩阵：

| 组件 | STM32 | NXP | Atmel |
|------|-------|-----|-------|
| ETH | `stm32/eth_dhcpv4_nucleo_f767zi` | `nxp/eth_dhcpv4_mimxrt1060` | `atmel/eth_dhcpv4_sam_e70` |
| UART | `stm32/uart_echo_disco_l475` | `nxp/uart_echo_mimxrt1060` | `atmel/uart_echo_atsame54` |
| I2C | `stm32/i2c_hts221_disco_l475` | `nxp/i2c_fxos8700_lpc55` | `atmel/i2c_shell_atsame54` |
| 文件系统 | `stm32/fs_littlefs_disco_l475` | `nxp/fs_littlefs_mimxrt1060` | `atmel/fs_littlefs_atsame54` |

共享 Kconfig 片段位于 `testcases/server/zephyr/overlays/`。

## 5. Macbook testcase

`testcases/macbook/` 保存本地开发/迁移用 testcase，包括 FreeRTOS、NXP、RT-Thread 等样例。其结构与 server testcase 一致，但路径通常指向本机工程和本机 DB。

## 6. 批量实验产物

批量运行常见产物：

- `<testcase>/replacement_log.md`
- `<testcase>/classify_stats.json`
- `<testcase>/classify_stats_output.json`
- `<root>/classify_stats_summary.md`
- `<db_path>/lcmhal_ai_log/session_*.json`
- `<db_path>/lcmhal_ai_log/function_classify_*.json`
- `<db_path>/lcmhal_ai_log/replacement_update_*.json`

## 7. 设计注意点

- `build.sh` 必须保证成功后 `emulate/output.elf` 存在。
- `clear.sh` 应清掉会影响下一次编译的缓存和中间文件。
- CodeQL DB 应与当前源码版本对应；若源码被替换后重新建库，recover 的基线也会改变。
- RTOS 初始化路径中的 CORE 函数要谨慎处理，尤其是 SysTick、NVIC、VTOR、PendSV 和 scheduler 相关函数。
- `emulate/output.bin` 会由 `output.elf` 自动刷新，避免 ELF/BIN 不一致。

