# STM32 Demo Token Usage Estimate

- Baseline sessions: 11
- Avg tokens/invoke: 12741.58 (prompt 12516.61, completion 224.97)
- Avg elapsed/invoke: 10695.21 ms
- Fallback invokes/function: 11.225

| Demo | 估算函数总数 | 现有函数数 | 现有invoke | 放大倍数 | 估算invoke | 估算Prompt | 估算Completion | 估算TotalToken | 估算耗时(min) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS | 304 | 0 | 0 | 1.0 | 3412.5 | 42713346 | 767707 | 43481053 | 608.3 |
| testcases/server/stm32/LwIP_HTTP_Server_SocketRTOS | 281 | 0 | 0 | 1.0 | 3154.3 | 39481744 | 709624 | 40191368 | 562.27 |
| testcases/server/stm32/LwIP_StreamingServer | 281 | 0 | 0 | 1.0 | 3154.3 | 39481744 | 709624 | 40191368 | 562.27 |
| testcases/server/stm32/UART_Hyperterminal_IT | 120 | 0 | 0 | 1.0 | 1347.1 | 16860531 | 303042 | 17163573 | 240.12 |
| testcases/server/stm32/BLE_HeartRateFreeRTOS | 109 | 0 | 0 | 1.0 | 1223.6 | 15314982 | 275263 | 15590245 | 218.11 |
| testcases/server/stm32/LwIP_HTTP_Server_Raw | 106 | 0 | 0 | 1.0 | 1189.9 | 14893469 | 267687 | 15161156 | 212.1 |
| testcases/server/stm32/FatFs_USBDisk_RTOS | 0 | 0 | 0 | 1.0 | 0 | 0 | 0 | 0 | 0.0 |
| **TOTAL** | **1201** | **0** | **0** | - | **13481.7** | **168745816** | **3032947** | **171778763** | **2403.17** |
