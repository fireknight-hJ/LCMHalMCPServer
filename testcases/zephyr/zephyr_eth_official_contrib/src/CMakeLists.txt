# 简化的CMake配置，专门用于ETH测试
cmake_minimum_required(VERSION 3.20)
project(zephyr_eth_test C ASM)

# 设置交叉编译工具链
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# 交叉编译器
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)

# 编译器标志
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-sp-d16")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffreestanding -nostdlib -nodefaultlibs --specs=nosys.specs")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wno-unused-parameter")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -g -ffunction-sections -fdata-sections")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fno-common -fno-builtin -std=gnu11")

# 汇编器标志
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -mcpu=cortex-m7 -mthumb -mfloat-abi=hard -mfpu=fpv5-sp-d16")
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -x assembler-with-cpp")

# 包含目录
include_directories(
    .
    /home/ckq/LCMHalMCPServer/zephyr_official/include
    /home/ckq/LCMHalMCPServer/zephyr_official/include/zephyr
    /home/ckq/LCMHalMCPServer/zephyr_official/include/drivers
    /home/ckq/LCMHalMCPServer/zephyr_official/include/net
)

# 定义宏
add_definitions(
    -D__ZEPHYR__
    -DKERNEL
    -DCONFIG_ASSERT=y
    -DCONFIG_PRINTK=y
    -DCONFIG_NETWORKING=y
    -DCONFIG_NET_L2_ETHERNET=y
    -DCONFIG_ETH_STM32_HAL=y
    -DCONFIG_ETH_DW_MAC_STM32=y
    -DCONFIG_ETH_STM32=y
    -DCONFIG_SOC_SERIES_STM32F7X=y
    -DCONFIG_SOC_STM32F746XX=y
    -DCONFIG_ETH_STM32_HAL_PHY_LAN8742A=y
    -DCONFIG_ETH_STM32_HAL_MII=y
    -DCONFIG_PHY=y
    -DCONFIG_PHY_STM32=y
)

# 源文件
set(SOURCES startup_stm32f746xx.s main.c syscalls.c)

# 可执行文件
add_executable(zephyr_eth_test ${SOURCES})

# 链接器脚本
target_link_options(zephyr_eth_test PRIVATE -T${CMAKE_CURRENT_SOURCE_DIR}/linker.ld)
target_link_options(zephyr_eth_test PRIVATE -nostdlib -nostartfiles -Wl,--gc-sections)
target_link_libraries(zephyr_eth_test PRIVATE -lgcc)
