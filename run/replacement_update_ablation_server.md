# ReplacementUpdate Ablation

- Root: `/home/haojie/workspace/lcmhalmcp/testcases/server`
- Demo count: **39**
- Baseline positive types: `INIT,IRQ,LOOP,RECV`
- Baseline include has_replacement=true: `True`

## Overall

- baseline_predicted_count_sum: **2203**
- with_ru_predicted_count_sum: **2236**
- ru_increment_count_sum: **33**
- ru_increment_ratio_over_total: **0.0078**
- ru_increment_ratio_over_baseline: **0.0150**
- replacement_update_log_function_count_sum: **516**

## Per Demo

| DemoPath | Total | Baseline | WithRU | RU_Increment | RU_Inc/Total | RU_Inc/Baseline | RU_LogFn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nxp/NXP_FATFS_BareMetal` | 67 | 43 | 44 | 1 | 0.0149 | 0.0233 | 26 |
| `nxp/NXP_FATFS_FreeRTOS` | 65 | 42 | 42 | 0 | 0.0000 | 0.0000 | 34 |
| `nxp/NXP_I2C_BareMetal` | 104 | 75 | 78 | 3 | 0.0288 | 0.0400 | 45 |
| `nxp/NXP_I2C_FreeRTOS` | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0 |
| `nxp/NXP_LwIP_BareMetal` | 105 | 66 | 68 | 2 | 0.0190 | 0.0303 | 20 |
| `nxp/NXP_LwIP_FreeRTOS` | 107 | 71 | 71 | 0 | 0.0000 | 0.0000 | 9 |
| `nxp/NXP_UART_BareMetal` | 90 | 52 | 56 | 4 | 0.0444 | 0.0769 | 33 |
| `nxp/NXP_UART_FreeRTOS` | 91 | 63 | 63 | 0 | 0.0000 | 0.0000 | 25 |
| `rtthread/imxrt1052-nxp-evk/base` | 53 | 37 | 37 | 0 | 0.0000 | 0.0000 | 18 |
| `rtthread/imxrt1052-nxp-evk/fatfs` | 53 | 36 | 37 | 1 | 0.0189 | 0.0278 | 24 |
| `rtthread/imxrt1052-nxp-evk/i2c` | 110 | 67 | 67 | 0 | 0.0000 | 0.0000 | 33 |
| `rtthread/imxrt1052-nxp-evk/uart` | 73 | 46 | 46 | 0 | 0.0000 | 0.0000 | 20 |
| `rtthread/imxrt1060-nxp-evk/base` | 65 | 15 | 15 | 0 | 0.0000 | 0.0000 | 4 |
| `rtthread/imxrt1060-nxp-evk/eth` | 73 | 26 | 26 | 0 | 0.0000 | 0.0000 | 5 |
| `rtthread/stm32f401-st-nucleo/base` | 55 | 34 | 38 | 4 | 0.0727 | 0.1176 | 26 |
| `rtthread/stm32f401-st-nucleo/eth` | 55 | 36 | 37 | 1 | 0.0182 | 0.0278 | 19 |
| `rtthread/stm32f401-st-nucleo/fatfs` | 56 | 44 | 44 | 0 | 0.0000 | 0.0000 | 14 |
| `rtthread/stm32f401-st-nucleo/fatfst-nucleo/fatfs` | 281 | 183 | 185 | 2 | 0.0071 | 0.0109 | 18 |
| `rtthread/stm32f401-st-nucleo/i2c` | 55 | 38 | 38 | 0 | 0.0000 | 0.0000 | 5 |
| `rtthread/stm32f401-st-nucleo/uart` | 55 | 40 | 40 | 0 | 0.0000 | 0.0000 | 11 |
| `stm32/BLE_HeartRateFreeRTOS` | 109 | 65 | 65 | 0 | 0.0000 | 0.0000 | 0 |
| `stm32/FatFs_USBDisk_RTOS` | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0 |
| `stm32/LwIP_HTTP_Server_Raw` | 106 | 82 | 85 | 3 | 0.0283 | 0.0366 | 3 |
| `stm32/LwIP_HTTP_Server_SocketRTOS` | 281 | 183 | 185 | 2 | 0.0071 | 0.0109 | 18 |
| `stm32/LwIP_HTTP_Server_Socket_RTOS` | 304 | 225 | 225 | 0 | 0.0000 | 0.0000 | 17 |
| `stm32/LwIP_StreamingServer` | 281 | 183 | 185 | 2 | 0.0071 | 0.0109 | 18 |
| `stm32/UART_Hyperterminal_IT` | 120 | 88 | 90 | 2 | 0.0167 | 0.0227 | 8 |
| `zephyr/atmel/eth_dhcpv4_sam_e70` | 188 | 12 | 13 | 1 | 0.0053 | 0.0833 | 7 |
| `zephyr/atmel/fs_littlefs_atsame54` | 76 | 19 | 21 | 2 | 0.0263 | 0.1053 | 25 |
| `zephyr/atmel/i2c_shell_atsame54` | 79 | 16 | 16 | 0 | 0.0000 | 0.0000 | 11 |
| `zephyr/atmel/uart_echo_atsame54` | 63 | 13 | 16 | 3 | 0.0476 | 0.2308 | 13 |
| `zephyr/nxp/eth_dhcpv4_mimxrt1060` | 276 | 71 | 71 | 0 | 0.0000 | 0.0000 | 5 |
| `zephyr/nxp/fs_littlefs_mimxrt1060` | 113 | 32 | 32 | 0 | 0.0000 | 0.0000 | 2 |
| `zephyr/nxp/i2c_fxos8700_lpc55` | 150 | 61 | 61 | 0 | 0.0000 | 0.0000 | 0 |
| `zephyr/nxp/uart_echo_mimxrt1060` | 103 | 30 | 30 | 0 | 0.0000 | 0.0000 | 0 |
| `zephyr/stm32/eth_dhcpv4_nucleo_f767zi` | 260 | 37 | 37 | 0 | 0.0000 | 0.0000 | 0 |
| `zephyr/stm32/fs_littlefs_disco_l475` | 50 | 32 | 32 | 0 | 0.0000 | 0.0000 | 0 |
| `zephyr/stm32/i2c_hts221_disco_l475` | 37 | 21 | 21 | 0 | 0.0000 | 0.0000 | 0 |
| `zephyr/stm32/uart_echo_disco_l475` | 35 | 19 | 19 | 0 | 0.0000 | 0.0000 | 0 |

## Metric Meaning

- `RU_Increment`: functions brought in only because `has_replacement_update=true`.
- `RU_Inc/Total`: incremental coverage contribution of ReplacementUpdate over all functions.
- `RU_Inc/Baseline`: relative gain against baseline predicted set.
- `RU_LogFn`: number of functions that have replacement_update logs in this demo.