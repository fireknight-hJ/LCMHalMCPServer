# Zephyr官方UART测试驱动构建配置
# 基于ARM Cortex-M架构，使用Zephyr兼容的API

cmake_minimum_required(VERSION 3.13)
project(zephyr_uart_official C)

# 设置交叉编译工具链
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# 指定交叉编译器
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)
set(CMAKE_OBJCOPY arm-none-eabi-objcopy)
set(CMAKE_OBJDUMP arm-none-eabi-objdump)
set(CMAKE_SIZE arm-none-eabi-size)

# 设置C标准
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# ARM特定编译选项
set(CPU_COMPILE_OPTIONS 
    -mcpu=cortex-m3 
    -mthumb 
    -mfloat-abi=soft
    -ffreestanding
    -nostdlib
)

set(CPU_LINK_OPTIONS
    -mcpu=cortex-m3
    -mthumb
    -mfloat-abi=soft
    -nostdlib
    -Wl,--gc-sections
    -Wl,-Map=zephyr_uart_official.map
)

# 包含路径 - 模拟Zephyr头文件结构
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    # 添加Zephyr头文件路径（简化版本）
    /home/chenkaiqiu/LCMHalMCPServer/zephyr_official/include
    /home/chenkaiqiu/LCMHalMCPServer/zephyr_official/include/zephyr
    /home/chenkaiqiu/LCMHalMCPServer/zephyr_official/include/drivers
)

# 定义宏来模拟Zephyr配置
add_definitions(
    -D__ZEPHYR__
    -DKERNEL
    -DCONFIG_ASSERT=y
    -DCONFIG_PRINTK=y
    -DCONFIG_UART_INTERRUPT_DRIVEN=y
    -DCONFIG_UART_LINE_CTRL=n
    -DCONFIG_UART_CONSOLE=y
    # 设备树模拟
    -DDT_CHOSEN_zephyr_shell_uart=1
)

# 添加可执行文件
add_executable(zephyr_uart_official
    main.c
)

# 设置目标属性
target_compile_options(zephyr_uart_official PRIVATE
    ${CPU_COMPILE_OPTIONS}
    -Wall
    -Wextra
    -Werror
    -O0
    -g
    -ffunction-sections
    -fdata-sections
    -fno-common
    -fno-builtin
    -std=gnu11
)

# 设置链接选项
target_link_options(zephyr_uart_official PRIVATE
    ${CPU_LINK_OPTIONS}
    -static
    -T${CMAKE_CURRENT_SOURCE_DIR}/linker.ld
)

# 链接后处理：生成二进制文件
add_custom_command(TARGET zephyr_uart_official POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O binary $<TARGET_FILE:zephyr_uart_official> $<TARGET_FILE_DIR:zephyr_uart_official>/zephyr_uart_official.bin
    COMMAND ${CMAKE_SIZE} $<TARGET_FILE:zephyr_uart_official>
    COMMENT "生成二进制文件"
)
