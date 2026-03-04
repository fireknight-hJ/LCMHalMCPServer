# Zephyr官方UART驱动测试 - CMake配置
# 用于开源贡献的测试用例

cmake_minimum_required(VERSION 3.13)
project(zephyr_uart_contrib C)

# 设置C标准
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# 交叉编译配置 - ARM Cortex-M3 (STM32F103)
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# ARM工具链
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)

# 编译器标志
set(CMAKE_C_FLAGS "-mcpu=cortex-m3 -mthumb -ffunction-sections -fdata-sections -Wall -Wextra -Werror -Os -g")
set(CMAKE_C_FLAGS_DEBUG "-O0 -g3")
set(CMAKE_C_FLAGS_RELEASE "-Os -flto")

# 链接器标志
set(CMAKE_EXE_LINKER_FLAGS "-mcpu=cortex-m3 -mthumb -Wl,--gc-sections -nostartfiles -T${CMAKE_SOURCE_DIR}/linker.ld")

# 包含目录
include_directories(
    ${CMAKE_SOURCE_DIR}
    /home/ckq/LCMHalMCPServer/zephyr_official/include
)

# 源文件
set(SOURCES
    main.c
)

# 可执行文件
add_executable(zephyr_uart_contrib ${SOURCES})

# 目标属性
set_target_properties(zephyr_uart_contrib PROPERTIES
    OUTPUT_NAME "zephyr_uart_contrib"
    SUFFIX ".elf"
)

# 安装目标（可选）
install(TARGETS zephyr_uart_contrib
    DESTINATION ${CMAKE_BINARY_DIR}
)