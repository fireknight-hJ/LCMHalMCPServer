# ARM Cortex-M3 toolchain configuration for STM32F103C8T6
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# Specify the cross compiler
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_CXX_COMPILER arm-none-eabi-g++)

# Set compiler flags
set(CMAKE_C_FLAGS "-mcpu=cortex-m3 -mthumb -ffunction-sections -fdata-sections -Wall -Wextra -Werror -Os -g" CACHE STRING "C Compiler Flags")
set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS}" CACHE STRING "C++ Compiler Flags")

# Set linker flags
set(CMAKE_EXE_LINKER_FLAGS "-mcpu=cortex-m3 -mthumb -Wl,--gc-sections -nostartfiles" CACHE STRING "Linker Flags")

# Search for programs in the build host directories
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)