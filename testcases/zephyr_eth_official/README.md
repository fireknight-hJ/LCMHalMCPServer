# Zephyr Official ETH Driver Test

This is a Zephyr community official ETH driver test case based on Zephyr RTOS samples.

## License

This test case is licensed under the Apache License 2.0, consistent with Zephyr RTOS licensing.

```
Copyright (c) 2024 Zephyr Community

SPDX-License-Identifier: Apache-2.0
```

## Purpose

This test case demonstrates:
1. ETH device initialization using Zephyr driver APIs
2. MMIO register access for ETH peripheral (STM32)
3. Basic send/receive operations
4. Interrupt handling for ETH DMA

## Based on Zephyr Official Samples

This test case is based on the following Zephyr official samples:
- `zephyr_official/samples/boards/espressif/ethernet/src/main.c`
- `zephyr_official/samples/net/ethernet/gptp/src/main.c`

## Building

```bash
# Set Zephyr environment
export ZEPHYR_BASE=/path/to/zephyr
export ZEPHYR_SDK_INSTALL_DIR=/path/to/zephyr-sdk

# Build the test
./build.sh
```

## Analysis

This test case can be analyzed using the LCMHalMCPServer analysis pipeline:
```bash
python main.py testcases/zephyr_eth_official
```

The analysis includes:
1. CodeQL static analysis
2. LLM-based code analysis
3. Code replacement and compilation
4. Dynamic execution feedback

## Code Structure

- `src/main.c` - Main test application
- `src/CMakeLists.txt` - CMake configuration
- `build.sh` - Build script
- `lcmhal_config.yml` - Analysis configuration
- `emulate/` - Emulation configuration and outputs
- `codeql_db/` - CodeQL database and analysis results

## Contributing

This test case follows Zephyr community contribution guidelines and can be used as a reference for ETH driver testing in Zephyr RTOS.
