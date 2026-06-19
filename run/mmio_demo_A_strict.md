# MMIO Metrics Summary

- Root: `/home/haojie/workspace/lcmhalmcp/testcases/server`
- Demo count: **39**
- Positive types: `INIT,IRQ,LOOP,RECV`
- include_has_replacement_true: `False`
- include_replacement_update: `False`

## Overall

- total_functions: **4244**
- predicted_count: **2181**
- predicted_ratio_micro: **0.5139**
- has_replacement_true_count: **1696**
- replacement_update_count: **516**
- parse_error_count: **0**

## Per Demo

| DemoPath | Total | Pred | PredRatio | HasRepT | RepUpd | ParseErr |
| --- | --- | --- | --- | --- | --- | --- |
| `nxp/NXP_FATFS_BareMetal` | 67 | 42 | 0.6269 | 37 | 26 | 0 |
| `nxp/NXP_FATFS_FreeRTOS` | 65 | 41 | 0.6308 | 36 | 34 | 0 |
| `nxp/NXP_I2C_BareMetal` | 104 | 74 | 0.7115 | 50 | 45 | 0 |
| `nxp/NXP_I2C_FreeRTOS` | 0 | 0 | 0.0000 | 0 | 0 | 0 |
| `nxp/NXP_LwIP_BareMetal` | 105 | 64 | 0.6095 | 61 | 20 | 0 |
| `nxp/NXP_LwIP_FreeRTOS` | 107 | 71 | 0.6636 | 70 | 9 | 0 |
| `nxp/NXP_UART_BareMetal` | 90 | 49 | 0.5444 | 49 | 33 | 0 |
| `nxp/NXP_UART_FreeRTOS` | 91 | 62 | 0.6813 | 39 | 25 | 0 |
| `rtthread/imxrt1052-nxp-evk/base` | 53 | 37 | 0.6981 | 34 | 18 | 0 |
| `rtthread/imxrt1052-nxp-evk/fatfs` | 53 | 34 | 0.6415 | 31 | 24 | 0 |
| `rtthread/imxrt1052-nxp-evk/i2c` | 110 | 67 | 0.6091 | 50 | 33 | 0 |
| `rtthread/imxrt1052-nxp-evk/uart` | 73 | 44 | 0.6027 | 41 | 20 | 0 |
| `rtthread/imxrt1060-nxp-evk/base` | 65 | 15 | 0.2308 | 5 | 4 | 0 |
| `rtthread/imxrt1060-nxp-evk/eth` | 73 | 26 | 0.3562 | 6 | 5 | 0 |
| `rtthread/stm32f401-st-nucleo/base` | 55 | 34 | 0.6182 | 32 | 26 | 0 |
| `rtthread/stm32f401-st-nucleo/eth` | 55 | 36 | 0.6545 | 35 | 19 | 0 |
| `rtthread/stm32f401-st-nucleo/fatfs` | 56 | 43 | 0.7679 | 40 | 14 | 0 |
| `rtthread/stm32f401-st-nucleo/fatfst-nucleo/fatfs` | 281 | 182 | 0.6477 | 161 | 18 | 0 |
| `rtthread/stm32f401-st-nucleo/i2c` | 55 | 38 | 0.6909 | 33 | 5 | 0 |
| `rtthread/stm32f401-st-nucleo/uart` | 55 | 40 | 0.7273 | 39 | 11 | 0 |
| `stm32/BLE_HeartRateFreeRTOS` | 109 | 65 | 0.5963 | 58 | 0 | 0 |
| `stm32/FatFs_USBDisk_RTOS` | 0 | 0 | 0.0000 | 0 | 0 | 0 |
| `stm32/LwIP_HTTP_Server_Raw` | 106 | 82 | 0.7736 | 75 | 3 | 0 |
| `stm32/LwIP_HTTP_Server_SocketRTOS` | 281 | 182 | 0.6477 | 161 | 18 | 0 |
| `stm32/LwIP_HTTP_Server_Socket_RTOS` | 304 | 221 | 0.7270 | 213 | 17 | 0 |
| `stm32/LwIP_StreamingServer` | 281 | 182 | 0.6477 | 161 | 18 | 0 |
| `stm32/UART_Hyperterminal_IT` | 120 | 87 | 0.7250 | 87 | 8 | 0 |
| `zephyr/atmel/eth_dhcpv4_sam_e70` | 188 | 12 | 0.0638 | 12 | 7 | 0 |
| `zephyr/atmel/fs_littlefs_atsame54` | 76 | 19 | 0.2500 | 19 | 25 | 0 |
| `zephyr/atmel/i2c_shell_atsame54` | 79 | 16 | 0.2025 | 14 | 11 | 0 |
| `zephyr/atmel/uart_echo_atsame54` | 63 | 13 | 0.2063 | 13 | 13 | 0 |
| `zephyr/nxp/eth_dhcpv4_mimxrt1060` | 276 | 71 | 0.2572 | 12 | 5 | 0 |
| `zephyr/nxp/fs_littlefs_mimxrt1060` | 113 | 32 | 0.2832 | 2 | 2 | 0 |
| `zephyr/nxp/i2c_fxos8700_lpc55` | 150 | 61 | 0.4067 | 3 | 0 | 0 |
| `zephyr/nxp/uart_echo_mimxrt1060` | 103 | 30 | 0.2913 | 2 | 0 | 0 |
| `zephyr/stm32/eth_dhcpv4_nucleo_f767zi` | 260 | 37 | 0.1423 | 15 | 0 | 0 |
| `zephyr/stm32/fs_littlefs_disco_l475` | 50 | 32 | 0.6400 | 0 | 0 | 0 |
| `zephyr/stm32/i2c_hts221_disco_l475` | 37 | 21 | 0.5676 | 0 | 0 | 0 |
| `zephyr/stm32/uart_echo_disco_l475` | 35 | 19 | 0.5429 | 0 | 0 | 0 |
