# MMIO Metrics Summary

- Root: `/home/haojie/workspace/lcmhalmcp/testcases/server`
- Demo count: **39**
- Positive types: `INIT,IRQ,LOOP,RECV,RETURNOK`
- include_has_replacement_true: `True`
- include_replacement_update: `True`

## Overall

- total_functions: **4244**
- predicted_count: **3126**
- predicted_ratio_micro: **0.7366**
- has_replacement_true_count: **1696**
- replacement_update_count: **516**
- parse_error_count: **0**

## Per Demo

| DemoPath | Total | Pred | PredRatio | HasRepT | RepUpd | ParseErr |
| --- | --- | --- | --- | --- | --- | --- |
| `nxp/NXP_FATFS_BareMetal` | 67 | 56 | 0.8358 | 37 | 26 | 0 |
| `nxp/NXP_FATFS_FreeRTOS` | 65 | 58 | 0.8923 | 36 | 34 | 0 |
| `nxp/NXP_I2C_BareMetal` | 104 | 92 | 0.8846 | 50 | 45 | 0 |
| `nxp/NXP_I2C_FreeRTOS` | 0 | 0 | 0.0000 | 0 | 0 | 0 |
| `nxp/NXP_LwIP_BareMetal` | 105 | 96 | 0.9143 | 61 | 20 | 0 |
| `nxp/NXP_LwIP_FreeRTOS` | 107 | 99 | 0.9252 | 70 | 9 | 0 |
| `nxp/NXP_UART_BareMetal` | 90 | 84 | 0.9333 | 49 | 33 | 0 |
| `nxp/NXP_UART_FreeRTOS` | 91 | 86 | 0.9451 | 39 | 25 | 0 |
| `rtthread/imxrt1052-nxp-evk/base` | 53 | 49 | 0.9245 | 34 | 18 | 0 |
| `rtthread/imxrt1052-nxp-evk/fatfs` | 53 | 49 | 0.9245 | 31 | 24 | 0 |
| `rtthread/imxrt1052-nxp-evk/i2c` | 110 | 96 | 0.8727 | 50 | 33 | 0 |
| `rtthread/imxrt1052-nxp-evk/uart` | 73 | 67 | 0.9178 | 41 | 20 | 0 |
| `rtthread/imxrt1060-nxp-evk/base` | 65 | 41 | 0.6308 | 5 | 4 | 0 |
| `rtthread/imxrt1060-nxp-evk/eth` | 73 | 48 | 0.6575 | 6 | 5 | 0 |
| `rtthread/stm32f401-st-nucleo/base` | 55 | 51 | 0.9273 | 32 | 26 | 0 |
| `rtthread/stm32f401-st-nucleo/eth` | 55 | 48 | 0.8727 | 35 | 19 | 0 |
| `rtthread/stm32f401-st-nucleo/fatfs` | 56 | 55 | 0.9821 | 40 | 14 | 0 |
| `rtthread/stm32f401-st-nucleo/fatfst-nucleo/fatfs` | 281 | 266 | 0.9466 | 161 | 18 | 0 |
| `rtthread/stm32f401-st-nucleo/i2c` | 55 | 51 | 0.9273 | 33 | 5 | 0 |
| `rtthread/stm32f401-st-nucleo/uart` | 55 | 50 | 0.9091 | 39 | 11 | 0 |
| `stm32/BLE_HeartRateFreeRTOS` | 109 | 101 | 0.9266 | 58 | 0 | 0 |
| `stm32/FatFs_USBDisk_RTOS` | 0 | 0 | 0.0000 | 0 | 0 | 0 |
| `stm32/LwIP_HTTP_Server_Raw` | 106 | 98 | 0.9245 | 75 | 3 | 0 |
| `stm32/LwIP_HTTP_Server_SocketRTOS` | 281 | 266 | 0.9466 | 161 | 18 | 0 |
| `stm32/LwIP_HTTP_Server_Socket_RTOS` | 304 | 288 | 0.9474 | 213 | 17 | 0 |
| `stm32/LwIP_StreamingServer` | 281 | 266 | 0.9466 | 161 | 18 | 0 |
| `stm32/UART_Hyperterminal_IT` | 120 | 112 | 0.9333 | 87 | 8 | 0 |
| `zephyr/atmel/eth_dhcpv4_sam_e70` | 188 | 13 | 0.0691 | 12 | 7 | 0 |
| `zephyr/atmel/fs_littlefs_atsame54` | 76 | 22 | 0.2895 | 19 | 25 | 0 |
| `zephyr/atmel/i2c_shell_atsame54` | 79 | 16 | 0.2025 | 14 | 11 | 0 |
| `zephyr/atmel/uart_echo_atsame54` | 63 | 16 | 0.2540 | 13 | 13 | 0 |
| `zephyr/nxp/eth_dhcpv4_mimxrt1060` | 276 | 95 | 0.3442 | 12 | 5 | 0 |
| `zephyr/nxp/fs_littlefs_mimxrt1060` | 113 | 51 | 0.4513 | 2 | 2 | 0 |
| `zephyr/nxp/i2c_fxos8700_lpc55` | 150 | 96 | 0.6400 | 3 | 0 | 0 |
| `zephyr/nxp/uart_echo_mimxrt1060` | 103 | 53 | 0.5146 | 2 | 0 | 0 |
| `zephyr/stm32/eth_dhcpv4_nucleo_f767zi` | 260 | 81 | 0.3115 | 15 | 0 | 0 |
| `zephyr/stm32/fs_littlefs_disco_l475` | 50 | 45 | 0.9000 | 0 | 0 | 0 |
| `zephyr/stm32/i2c_hts221_disco_l475` | 37 | 36 | 0.9730 | 0 | 0 | 0 |
| `zephyr/stm32/uart_echo_disco_l475` | 35 | 29 | 0.8286 | 0 | 0 | 0 |
