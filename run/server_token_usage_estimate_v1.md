# Server Demo Token Usage Estimate

- Baseline sessions: 11
- Avg tokens/invoke: 12741.58 (prompt 12516.61, completion 224.97)
- Avg elapsed/invoke: 10695.21 ms
- Fallback invokes/function: 11.225

| Demo | 估算函数总数 | 现有函数数 | 现有invoke | token记录invoke | 放大倍数 | 估算invoke | 估算Prompt | 估算Completion | 估算TotalToken | 估算耗时(min) | 估算方式 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| nxp/NXP_LwIP_FreeRTOS | 107 | 12 | 464 | 464 | 8.917 | 4137.33 | 50573800 | 1040521 | 51614321 | 758.06 | demo_specific |
| stm32/LwIP_HTTP_Server_Socket_RTOS | 304 | 0 | 0 | 0 | 1.0 | 3412.53 | 42713346 | 767707 | 43481053 | 608.3 | global_baseline |
| rtthread/stm32f401-st-nucleo/fatfst-nucleo/fatfs | 281 | 0 | 0 | 0 | 1.0 | 3154.35 | 39481744 | 709624 | 40191368 | 562.27 | global_baseline |
| stm32/LwIP_HTTP_Server_SocketRTOS | 281 | 0 | 0 | 0 | 1.0 | 3154.35 | 39481744 | 709624 | 40191368 | 562.27 | global_baseline |
| stm32/LwIP_StreamingServer | 281 | 0 | 0 | 0 | 1.0 | 3154.35 | 39481744 | 709624 | 40191368 | 562.27 | global_baseline |
| zephyr/nxp/eth_dhcpv4_mimxrt1060 | 276 | 0 | 0 | 0 | 1.0 | 3098.22 | 38779222 | 696997 | 39476219 | 552.27 | global_baseline |
| zephyr/stm32/eth_dhcpv4_nucleo_f767zi | 260 | 0 | 0 | 0 | 1.0 | 2918.61 | 36531151 | 656591 | 37187742 | 520.25 | global_baseline |
| zephyr/atmel/eth_dhcpv4_sam_e70 | 188 | 0 | 0 | 0 | 1.0 | 2110.38 | 26414832 | 474766 | 26889598 | 376.18 | global_baseline |
| zephyr/nxp/i2c_fxos8700_lpc55 | 150 | 0 | 0 | 0 | 1.0 | 1683.82 | 21075664 | 378803 | 21454467 | 300.15 | global_baseline |
| stm32/UART_Hyperterminal_IT | 120 | 0 | 0 | 0 | 1.0 | 1347.05 | 16860531 | 303042 | 17163573 | 240.12 | global_baseline |
| zephyr/nxp/fs_littlefs_mimxrt1060 | 113 | 0 | 0 | 0 | 1.0 | 1268.47 | 15877000 | 285365 | 16162365 | 226.11 | global_baseline |
| rtthread/imxrt1052-nxp-evk/i2c | 110 | 0 | 0 | 0 | 1.0 | 1234.8 | 15455487 | 277789 | 15733276 | 220.11 | global_baseline |
| stm32/BLE_HeartRateFreeRTOS | 109 | 0 | 0 | 0 | 1.0 | 1223.57 | 15314982 | 275263 | 15590245 | 218.11 | global_baseline |
| stm32/LwIP_HTTP_Server_Raw | 106 | 0 | 0 | 0 | 1.0 | 1189.9 | 14893469 | 267687 | 15161156 | 212.1 | global_baseline |
| nxp/NXP_LwIP_BareMetal | 105 | 0 | 0 | 0 | 1.0 | 1178.67 | 14752965 | 265162 | 15018127 | 210.1 | global_baseline |
| zephyr/nxp/uart_echo_mimxrt1060 | 103 | 0 | 0 | 0 | 1.0 | 1156.22 | 14471956 | 260111 | 14732067 | 206.1 | global_baseline |
| nxp/NXP_UART_BareMetal | 90 | 0 | 0 | 0 | 1.0 | 1010.29 | 12645398 | 227282 | 12872680 | 180.09 | global_baseline |
| zephyr/atmel/i2c_shell_atsame54 | 79 | 0 | 0 | 0 | 1.0 | 886.81 | 11099850 | 199503 | 11299353 | 158.08 | global_baseline |
| zephyr/atmel/fs_littlefs_atsame54 | 76 | 0 | 0 | 0 | 1.0 | 853.13 | 10678336 | 191927 | 10870263 | 152.07 | global_baseline |
| rtthread/imxrt1052-nxp-evk/uart | 73 | 0 | 0 | 0 | 1.0 | 819.46 | 10256823 | 184351 | 10441174 | 146.07 | global_baseline |
| rtthread/imxrt1060-nxp-evk/eth | 73 | 0 | 0 | 0 | 1.0 | 819.46 | 10256823 | 184351 | 10441174 | 146.07 | global_baseline |
| nxp/NXP_FATFS_BareMetal | 67 | 0 | 0 | 0 | 1.0 | 752.1 | 9413797 | 169198 | 9582995 | 134.07 | global_baseline |
| nxp/NXP_UART_FreeRTOS | 91 | 4 | 31 | 31 | 22.75 | 705.25 | 9171208 | 212781 | 9383989 | 192.22 | demo_specific |
| rtthread/imxrt1060-nxp-evk/base | 65 | 0 | 0 | 0 | 1.0 | 729.65 | 9132788 | 164148 | 9296936 | 130.06 | global_baseline |
| zephyr/atmel/uart_echo_atsame54 | 63 | 0 | 0 | 0 | 1.0 | 707.2 | 8851779 | 159097 | 9010876 | 126.06 | global_baseline |
| nxp/NXP_I2C_BareMetal | 104 | 8 | 58 | 58 | 13.0 | 754.0 | 8265465 | 222235 | 8487700 | 145.77 | demo_specific |
| rtthread/stm32f401-st-nucleo/fatfs | 56 | 0 | 0 | 0 | 1.0 | 628.62 | 7868248 | 141420 | 8009668 | 112.05 | global_baseline |
| rtthread/stm32f401-st-nucleo/base | 55 | 0 | 0 | 0 | 1.0 | 617.4 | 7727743 | 138894 | 7866637 | 110.05 | global_baseline |
| rtthread/stm32f401-st-nucleo/eth | 55 | 0 | 0 | 0 | 1.0 | 617.4 | 7727743 | 138894 | 7866637 | 110.05 | global_baseline |
| rtthread/stm32f401-st-nucleo/i2c | 55 | 0 | 0 | 0 | 1.0 | 617.4 | 7727743 | 138894 | 7866637 | 110.05 | global_baseline |
| rtthread/stm32f401-st-nucleo/uart | 55 | 0 | 0 | 0 | 1.0 | 617.4 | 7727743 | 138894 | 7866637 | 110.05 | global_baseline |
| rtthread/imxrt1052-nxp-evk/base | 53 | 0 | 0 | 0 | 1.0 | 594.95 | 7446735 | 133844 | 7580579 | 106.05 | global_baseline |
| rtthread/imxrt1052-nxp-evk/fatfs | 53 | 0 | 0 | 0 | 1.0 | 594.95 | 7446735 | 133844 | 7580579 | 106.05 | global_baseline |
| zephyr/stm32/fs_littlefs_disco_l475 | 50 | 0 | 0 | 0 | 1.0 | 561.27 | 7025221 | 126268 | 7151489 | 100.05 | global_baseline |
| zephyr/stm32/i2c_hts221_disco_l475 | 37 | 0 | 0 | 0 | 1.0 | 415.34 | 5198664 | 93438 | 5292102 | 74.04 | global_baseline |
| zephyr/stm32/uart_echo_disco_l475 | 35 | 0 | 0 | 0 | 1.0 | 392.89 | 4917655 | 88387 | 5006042 | 70.03 | global_baseline |
| nxp/NXP_FATFS_FreeRTOS | 65 | 7 | 48 | 48 | 9.286 | 445.71 | 4763079 | 98772 | 4861851 | 68.85 | demo_specific |
| nxp/NXP_I2C_FreeRTOS | 0 | 0 | 0 | 0 | 1.0 | 0.0 | 0 | 0 | 0 | 0.0 | global_baseline |
| stm32/FatFs_USBDisk_RTOS | 0 | 0 | 0 | 0 | 1.0 | 0.0 | 0 | 0 | 0 | 0.0 | global_baseline |
| **TOTAL** | **4244** | **31** | **601** | **601** | - | **49563.3** | **617509213** | **11365098** | **628874311** | **8922.68** | - |
