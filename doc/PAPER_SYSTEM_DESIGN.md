# LCMHalMCP: An LLM-Enhanced CodeQL-Based Framework for Automated HAL Code Analysis and Replacement

## System Design

### 4.1 Overview

LCMHalMCP (LLM-CodeQL-MCP-based HAL Analysis and Replacement Tool) is a framework designed to automate the analysis and transformation of Hardware Abstraction Layer (HAL) code in embedded systems. The system integrates static analysis capabilities from CodeQL with large language model (LLM) reasoning to identify, classify, and replace hardware-dependent functions with platform-independent stubs suitable for simulation and testing.

The framework comprises approximately 39,000 lines of Python code organized into eight core modules: agents, tools, core, config, models, prompts, utils, and fuzzemu. It supports multiple embedded platforms including STM32F4/F7, NXP i.MX RT, and provides compatibility with FreeRTOS, RT-Thread, and bare-metal configurations.

### 4.2 System Architecture

The architecture of LCMHalMCP follows a layered design pattern that separates concerns across functional boundaries. As illustrated in Figure 1, the system consists of four primary layers: the Entry Layer, Workflow Layer, Agent Layer, and Data Layer.

**Entry Layer.** The entry layer provides two interfaces for system access: `main.py` serves as the command-line interface for workflow orchestration, while `server.py` implements a Model Context Protocol (MCP) server for integration with external tools such as Cline and Cursor.

**Workflow Layer.** The workflow layer orchestrates the complete analysis pipeline through three primary workflows: (1) the run workflow executes the full analysis cycle from database construction to simulation; (2) the recover workflow restores original source code from the database; and (3) the clean workflow removes cached analysis results for specific functions.

**Agent Layer.** The agent layer implements AI-driven analysis and repair capabilities using LangGraph and LangChain. Four specialized agents cooperate to achieve the system's objectives: the Analyzer Agent classifies functions based on their hardware dependencies; the Builder Agent manages compilation and automatic error correction; the Fixer Agent generates replacement code for identified functions; and the Emulator Runner Agent executes simulation tests.

**Data Layer.** The data layer manages persistent storage through four components: the CodeQL database stores extracted code information; the AI logs preserve analysis results; the cache maintains frequently accessed data; and the configuration store holds system parameters.

### 4.3 Core Components

#### 4.3.1 CodeQL Collector

The CodeQL Collector module serves as the primary interface for querying code information from the constructed database. It provides three categories of information extraction:

**Common Code Information.** The module extracts general function metadata including function names, file paths, line numbers, and complete function bodies. This information forms the basis for subsequent LLM analysis.

**MMIO Function Information.** The module identifies Memory-Mapped I/O (MMIO) functions by analyzing register access patterns and peripheral interactions. It maintains dictionaries for MMIO functions, driver functions, and buffer functions, along with expression-level details about MMIO operations.

**Driver Information.** The module extracts driver-level code patterns and their relationships to hardware peripherals, enabling context-aware function classification.

The Collector implements a caching mechanism that stores extracted information in JSON format, reducing database query overhead for subsequent analyses. The cache invalidation strategy supports both time-based and force-refresh modes.

#### 4.3.2 Analyzer Agent

The Analyzer Agent employs a LangGraph state machine to classify functions according to their hardware dependencies. The agent executes the following pipeline:

1. **Information Gathering.** For each candidate function, the agent retrieves function information, MMIO details, call stack relationships, and relevant type definitions using tool calls to the Collector module.

2. **LLM Classification.** The gathered information is presented to a large language model with a specialized prompt that guides classification into one of four categories:
   - **MMIO**: Functions that directly access memory-mapped hardware registers
   - **DRIVER**: Driver-level functions that abstract hardware operations
   - **LOGIC**: Pure logic functions with no hardware dependencies
   - **CORE**: RTOS kernel and scheduler functions that must not be modified

3. **Code Generation.** For functions classified as requiring replacement (MMIO and some DRIVER functions), the agent generates stub code that preserves the original function signature while removing hardware dependencies.

4. **Validation.** Generated code undergoes rubric-based validation checking for type consistency, signature matching, and adherence to platform-specific conventions.

The agent outputs a `FunctionClassifyResponse` structure containing the classification result, recommended replacement code, and confidence metrics.

#### 4.3.3 Builder Module

The Builder Module manages the compilation and iterative repair process. Its core operations include:

**Code Replacement.** The module applies generated stub code to source files while maintaining the original code in the database for potential rollback. A thread-safe locking mechanism prevents concurrent modifications during the replace-build-recover cycle.

**Project Compilation.** The module invokes platform-specific build scripts (build.sh) to compile the modified project. Compilation results are captured and analyzed for errors.

**Automatic Repair.** Upon compilation failure, the Builder Agent analyzes error messages and invokes the Fixer Agent to generate corrected code. This process iterates until compilation succeeds or a maximum retry count is reached.

**Output Processing.** Successful compilation produces ELF and binary outputs. The module performs ELF-to-binary conversion using arm-none-eabi-objcopy and extracts symbol tables for simulation configuration.

#### 4.3.4 Emulator Module

The Emulator Module configures and executes simulation tests using the fuzzemu framework:

**Configuration Generation.** The module generates four configuration files: (1) base_config.yml defines simulation parameters including memory maps and handler bindings; (2) semu_config.yml provides detailed memory configuration; (3) semu_rule.txt specifies execution rules; and (4) input.bin provides test input data.

**Memory Configuration.** The module automatically calculates and aligns flash memory regions based on the compiled binary size, ensuring 4KB alignment for simulation compatibility.

**Handler Binding.** MMIO functions identified by the Analyzer are bound to appropriate handlers in the fuzzemu framework, enabling simulation of hardware operations.

### 4.4 Data Management

The system employs a centralized `DataManager` singleton that maintains consistency across all components:

```python
class DataManager:
    mmio_info_list: Dict[str, FunctionClassifyResponse]
    mmio_infos_by_file: Dict[str, List[FunctionClassifyResponse]]
    replacement_updates: Dict[str, ReplacementUpdate]
    replacement_updates_by_file: Dict[str, List[ReplacementUpdate]]
    replacement_history: Dict[str, List[Dict]]
```

The `replacement_history` structure is particularly significant for iterative repair, as it maintains the complete evolution of replacement attempts for each function. This historical context enables the Fixer Agent to avoid repeating unsuccessful approaches.

### 4.5 MCP Interface

LCMHalMCP implements the Model Context Protocol (MCP) to enable integration with external AI tools. Three MCP servers are provided:

**Collector MCP Server.** Exposes functions for database queries including `get_function_info`, `get_mmio_func_info`, `get_struct_or_enum_info`, `get_func_call_stack`, and `get_driver_info`.

**Builder MCP Server.** Provides project management functions including `build_project`, `update_function_replacement`, `get_replace_func_details_by_file`, and `get_function_analysis_and_replacement`.

**Emulator MCP Server.** Offers simulation functions including `emulate_proj`, `mmio_function_emulate_info`, and `function_calls_emulate_info`.

The MCP interface uses JSON-RPC over stdio transport, enabling seamless integration with tools that support the MCP standard.

### 4.6 Extensibility

The framework provides several extension points for adapting to new platforms and requirements:

**HAL Handlers.** New hardware abstraction layers can be supported by implementing handlers in the fuzzemu framework. Each handler defines supported functions and their simulation behavior.

**Test Cases.** New test scenarios are added by creating directories with configuration files (lcmhal_config.yml), build scripts, and cleanup scripts. The framework automatically discovers and processes these test cases.

**Analysis Agents.** Custom agents can be created using the LangGraph framework, binding appropriate tools and defining state transition logic.

**CodeQL Queries.** Custom queries can be added to the queries/collectors/ directory to extract additional code information, enabling platform-specific analysis patterns.

### 4.7 Design Rationale

The architectural decisions in LCMHalMCP reflect trade-offs between flexibility, performance, and maintainability:

**CodeQL Selection.** CodeQL was chosen for its powerful Datalog-based query language and support for multiple programming languages. While database construction requires initial time investment, the resulting database supports incremental analysis and complex relationship queries.

**LangGraph Integration.** LangGraph provides robust state management and tool integration for agent workflows. Its checkpointing capability enables debugging of complex multi-step reasoning processes.

**Layered Separation.** The separation between Collector and Analyzer modules enables independent testing and allows the Collector to serve as a standalone MCP server for other tools.

**Centralized Data Management.** The DataManager singleton ensures data consistency across agents while simplifying interface design by eliminating the need to pass database paths and configuration parameters between components.

---

## 5. Implementation Details

### 5.1 Technology Stack

LCMHalMCP is implemented in Python 3.10+ with the following key dependencies:

| Component | Technology | Purpose |
|-----------|------------|---------|
| Static Analysis | CodeQL CLI | Database construction and querying |
| LLM Framework | LangChain + LangGraph | Agent orchestration |
| LLM Providers | OpenAI / Anthropic / Local | Language model inference |
| MCP Protocol | langchain-mcp-adapters | Tool integration |
| Simulation | fuzzemu + QEMU | Embedded system emulation |
| Build Tools | CMake + Ninja + ARM GCC | Project compilation |

### 5.2 Directory Structure

The project is organized as follows:

```
lcmhalmcp/
├── main.py              # Entry point
├── agents/              # AI agents (analyzer, builder, fixer, emulator)
├── tools/               # Core tools (collector, builder, replacer, emulator)
├── core/                # Data management
├── config/              # Configuration management
├── models/              # Data structures
├── prompts/             # LLM prompt templates
├── queries/             # CodeQL queries
├── utils/               # Utility functions
├── fuzzemu/             # Simulation framework
└── testcases/           # Test scenarios
```

### 5.3 Supported Platforms

| Platform | Architecture | Status |
|----------|--------------|--------|
| STM32F4/F7 | ARM Cortex-M4/M7 | Fully Supported |
| NXP i.MX RT | ARM Cortex-M7 | Partially Supported |
| Ambiq Apollo | ARM Cortex-M4 | Planned |
| Nordic nRF52 | ARM Cortex-M4 | Planned |

### 5.4 Supported Peripherals

| Peripheral | Status | Notes |
|------------|--------|-------|
| UART/LPUART | Supported | Including DMA mode |
| I2C | Partial | Basic support |
| SPI | Planned | — |
| Ethernet (LwIP) | Supported | TCP/IP stack |
| Flash (FATFS) | Supported | File system |

---

## References

[1] GitHub, "CodeQL," https://codeql.github.com/

[2] LangChain, "LangGraph," https://langchain-ai.github.io/langgraph/

[3] Anthropic, "Model Context Protocol," https://modelcontextprotocol.io/

[4] STMicroelectronics, "STM32 HAL Driver," https://www.st.com/en/embedded-software/stm32cube-embedded-software.html

[5] NXP, "MCUXpresso SDK," https://www.nxp.com/design-software/development-software/mcuxpresso-software-and-tools

[6] FreeRTOS, "FreeRTOS Real-Time Operating System," https://www.freertos.org/

[7] QEMU, "QEMU Emulator," https://www.qemu.org/

---

*Document Version: 2.0*  
*Last Updated: March 5, 2026*
