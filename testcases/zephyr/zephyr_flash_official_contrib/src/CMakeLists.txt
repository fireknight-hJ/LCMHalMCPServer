# 简化的CMake配置，专门用于flash测试
cmake_minimum_required(VERSION 3.20)
project(zephyr_flash_test C ASM)

# 设置交叉编译工具链
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# 交叉编译器
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)

# 编译器标志
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mcpu=cortex-m3 -mthumb -mfloat-abi=soft")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffreestanding -nostdlib -nodefaultlibs --specs=nosys.specs")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wno-unused-parameter")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -g -ffunction-sections -fdata-sections")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fno-common -fno-builtin -std=gnu11")

# 汇编器标志
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -mcpu=cortex-m3 -mthumb")
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -x assembler-with-cpp")

# 包含目录
include_directories(
    .
    /home/ckq/LCMHalMCPServer/zephyr_official/include
    /home/ckq/LCMHalMCPServer/zephyr_official/include/zephyr
    /home/ckq/LCMHalMCPServer/zephyr_official/include/drivers
)

# 定义宏
add_definitions(
    -D__ZEPHYR__
    -DKERNEL
    -DCONFIG_ASSERT=y
    -DCONFIG_PRINTK=y
    -DCONFIG_FLASH=y
    -DCONFIG_FLASH_PAGE_LAYOUT=y
    -DCONFIG_FLASH_HAS_PAGE_LAYOUT=y
    -DCONFIG_FLASH_HAS_WRITE_PROTECTION=y
    -DCONFIG_SOC_SERIES_STM32F1X=y
    -DCONFIG_SOC_STM32F103C8=y
    -DCONFIG_FLASH_STM32=y
    -DCONFIG_FLASH_STM32_BASE=0x40022000
    -DCONFIG_FLASH_STM32_PAGE_SIZE=1024
    -DCONFIG_FLASH_STM32_SIZE=65536
)

# 源文件
set(SOURCES startup_stm32f103c8tx.s main.c syscalls.c)

# 可执行文件
add_executable(zephyr_flash_test ${SOURCES})

# 链接器脚本
target_link_options(zephyr_flash_test PRIVATE -T${CMAKE_CURRENT_SOURCE_DIR}/linker.ld)
target_link_options(zephyr_flash_test PRIVATE -nostdlib -nostartfiles -Wl,--gc-sections)
target_link_libraries(zephyr_flash_test PRIVATE -lgcc)