# Zephyr 测试用例（testcases/server/zephyr）

本目录按 **厂商**（`stm32` / `nxp` / `atmel`）分子目录，每个子目录对应一个 **west 构建的 Zephyr sample**，结构与 README 约定一致：

| 文件 | 说明 |
|------|------|
| `build.sh` | 在 Zephyr workspace 中执行 `west build`，将 `zephyr.elf` 复制为本目录 `emulate/output.elf` |
| `clear.sh` | 删除本次 west 构建目录及 `emulate/output.elf` |
| `lcmhal_config.yml` | `script_path` / `db_path` / `src_path` / `proj_path`，供 `main.py` 等流程加载 |

## 共享 Kconfig 片段

目录 **`overlays/`** 存放可被多个用例复用的 `*.conf`（例如 `EXTRA_CONF_FILE`），当前含 `atsame54_i2c_shell.conf`。

## 环境要求

- **Zephyr workspace**（含 `west`、Zephyr SDK）：默认 `ZEPHYR_PROJECT=/home/haojie/zephyrproject`  
  可通过环境变量覆盖：  
  `export ZEPHYR_PROJECT=/path/to/your/zephyrproject`
- `src_path` 指向该 workspace 下的 **`zephyr`** 源码树；`proj_path` 为 workspace **根目录**（与 `west.yml` 同级）。

## 矩阵一览（3 厂商 × 4 组件）

| 组件 | STM32 | NXP | Atmel |
|------|--------|-----|--------|
| ETH | `stm32/eth_dhcpv4_nucleo_f767zi` | `nxp/eth_dhcpv4_mimxrt1060` | `atmel/eth_dhcpv4_sam_e70` |
| UART | `stm32/uart_echo_disco_l475` | `nxp/uart_echo_mimxrt1060` | `atmel/uart_echo_atsame54` |
| I2C | `stm32/i2c_hts221_disco_l475` | `nxp/i2c_fxos8700_lpc55` | `atmel/i2c_shell_atsame54`（`overlays/atsame54_i2c_shell.conf` 供 `EXTRA_CONF_FILE`） |
| 文件系统 | `stm32/fs_littlefs_disco_l475` | `nxp/fs_littlefs_mimxrt1060` | `atmel/fs_littlefs_atsame54` |

## emulate 目录

构建成功后生成 `emulate/output.elf`。模拟器侧 `base_config.yml` / `semu_config.yml` 等可按需通过工具链生成或从其它 testcase 拷贝模板后调整。

## 数据库路径

`lcmhal_config.yml` 中 `db_path` 默认指向 `dbs_server` 下独立 `DATABASE_Zephyr_*`，请在本机创建对应 CodeQL 数据库或按实际路径修改。
