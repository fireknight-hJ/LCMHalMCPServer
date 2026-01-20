# ARM 交叉编译配置用于构建测试MMIO驱动
cmake_minimum_required(VERSION 3.13)
project(test_arm_zephyr C)

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

# ARM 特定编译选项
set(CPU_COMPILE_OPTIONS 
    -mcpu=cortex-m3 
    -mthumb 
    -mfloat-abi=soft
)

set(CPU_LINK_OPTIONS
    -mcpu=cortex-m3
    -mthumb
    -mfloat-abi=soft
)

# 包含路径
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# 添加可执行文件 - ARM Zephyr兼容MMIO测试
add_executable(test_arm_zephyr
    test_arm_zephyr.c
)

# 设置目标属性
target_compile_options(test_arm_zephyr PRIVATE
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
)

# 设置链接选项
target_link_options(test_arm_zephyr PRIVATE
    ${CPU_LINK_OPTIONS}
    -nostdlib
    -static
    -Wl,--gc-sections
    -Wl,-Map=test_arm_zephyr.map
    -T${CMAKE_CURRENT_SOURCE_DIR}/linker.ld
)

# 链接后处理：生成二进制和hex文件
add_custom_command(TARGET test_arm_zephyr POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O binary $<TARGET_FILE:test_arm_zephyr> $<TARGET_FILE_DIR:test_arm_zephyr>/test_arm_zephyr.bin
    COMMAND ${CMAKE_OBJCOPY} -O ihex $<TARGET_FILE:test_arm_zephyr> $<TARGET_FILE_DIR:test_arm_zephyr>/test_arm_zephyr.hex
    COMMAND ${CMAKE_SIZE} $<TARGET_FILE:test_arm_zephyr>
    COMMENT "生成二进制和hex文件"
)

# 安装目标
install(TARGETS test_arm_zephyr
    DESTINATION bin
)
