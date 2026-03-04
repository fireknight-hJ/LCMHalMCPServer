# CMake configuration for Zephyr BLE driver test
cmake_minimum_required(VERSION 3.20)
project(zephyr_ble_test C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Add executable
add_executable(zephyr_ble_test
    main.c
    syscalls.c
    startup_nrf52840.s
)

# Target-specific settings for nRF52840
set_target_properties(zephyr_ble_test PROPERTIES
    OUTPUT_NAME "zephyr_ble_test"
    SUFFIX ".elf"
)

# Include directories
target_include_directories(zephyr_ble_test PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
)

# Linker script
set_target_properties(zephyr_ble_test PROPERTIES
    LINK_FLAGS "-T${CMAKE_CURRENT_SOURCE_DIR}/linker.ld -nostartfiles -nostdlib"
)

# Compiler flags for ARM Cortex-M4
target_compile_options(zephyr_ble_test PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -mfloat-abi=hard
    -mfpu=fpv4-sp-d16
    -ffunction-sections
    -fdata-sections
    -Wall
    -Wextra
    -Werror
    -Wno-unused-parameter
    -Wno-unused-variable
    -Wno-unused-function
    -Os
)

# Linker flags
target_link_options(zephyr_ble_test PRIVATE
    -mcpu=cortex-m4
    -mthumb
    -mfloat-abi=hard
    -mfpu=fpv4-sp-d16
    -Wl,--gc-sections
    -Wl,--print-memory-usage
    -Wl,-Map=${CMAKE_CURRENT_BINARY_DIR}/zephyr_ble_test.map
)

# Install target
install(TARGETS zephyr_ble_test
    DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
)