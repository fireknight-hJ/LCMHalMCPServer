cd /home/haojie/workspace/lcmhalmcp
python main.py analyze testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS -f HAL_BE_ENET_ReadFrame
python main.py run testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS
python main.py emulate testcases/server/stm32/LwIP_HTTP_Server_Socket_RTOS