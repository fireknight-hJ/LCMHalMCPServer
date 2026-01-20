# Zephyr环境驱动测试指南

## 项目概述

LCMHalMCPServer是一个基于CodeQL和LLM的嵌入式系统驱动分析工具，专门用于在Zephyr环境中进行驱动测试和分析。该项目结合了静态代码分析和智能分析技术，能够全面测试各类驱动的正确性、安全性和兼容性。

## 核心特性

- **静态代码分析**：使用CodeQL进行深入的代码模式分析
- **智能分析**：集成LLM进行代码理解和修复建议
- **驱动定位**：自动识别驱动相关代码和调用关系
- **安全评估**：分析MMIO操作和潜在安全风险
- **自动化测试**：完整的端到端测试流程

## 系统架构

```
LCMHalMCPServer/
├── core/                    # 核心模块
├── tools/                   # 工具模块
│   ├── collector/          # 数据收集器
│   ├── analyzer/           # 分析器
│   ├── builder/            # 构建工具
│   └── fixer/              # 代码修复工具
├── queries/                # CodeQL查询文件
├── models/                 # 数据模型
├── testcases/              # 测试用例
└── utils/                  # 工具函数
```

## 环境准备

### 1. 依赖安装

```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装CodeQL CLI
# 从GitHub releases下载并配置PATH
```

### 2. 测试用例配置

在`testcases/zephyr_server/`目录下：

- `build.sh` - Zephyr项目构建脚本
- `clear.sh` - 清理构建缓存脚本

**build.sh示例配置：**
```bash
#!/usr/bin/env bash
set -euo pipefail

# 板型默认 qemu_riscv64，可通过 BOARD 环境变量覆盖
BOARD=${BOARD:-qemu_riscv64}
APP_DIR=${APP_DIR:-samples/hello_world}

echo "=== Zephyr build start ==="
echo "BOARD : $BOARD"
echo "APP   : $APP_DIR"

# 执行纯净构建
west build -p always -b "$BOARD" "$APP_DIR"

echo "=== Build finished successfully ==="
```

## 测试流程

### 阶段1：项目构建和数据库创建

#### 1.1 构建Zephyr项目

```bash
# 进入测试用例目录
cd testcases/zephyr_server/

# 默认构建
./build.sh

# 自定义构建
BOARD=qemu_cortex_m3 APP_DIR=samples/philosophers ./build.sh
```

#### 1.2 创建CodeQL数据库

```bash
# 创建CodeQL数据库
codeql database create zephyr-driver-db \
    --language=cpp \
    --source-root=/path/to/zephyr-project \
    --command="west build -b qemu_riscv64 samples/drivers/uart"
```

### 阶段2：启动分析服务

#### 2.1 启动主MCP服务器

```bash
# 启动主服务器
python server.py
```

#### 2.2 启动收集器MCP服务器

```bash
# 使用stdio传输
python -m tools.collector.mcp_server \
    --db-path /path/to/zephyr-driver-db \
    --transport stdio
```

### 阶段3：执行驱动分析

#### 3.1 驱动函数调用分析

```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def analyze_driver_calls():
    client = MultiServerMCPClient({
        "lcmhal_collector": {
            "command": "python",
            "args": [
                "-m", "tools.collector.mcp_server",
                "--db-path", "/path/to/zephyr-driver-db",
                "--transport", "stdio"
            ],
            "transport": "stdio"
        }
    })
    
    tools = await client.get_tools()
    
    # 注册数据库
    await tools["register_and_analyze_database"].invoke({})
    
    # 分析驱动函数
    driver_functions = ["uart_init", "i2c_transfer", "spi_send"]
    for func in driver_functions:
        # 获取函数信息
        func_info = await tools["collect_function_info"].invoke({"func_name": func})
        
        # 获取调用关系
        call_stack = await tools["collect_func_call_stack"].invoke({"func_name": func})
        
        # 获取驱动信息
        driver_info = await tools["collect_driver_info"].invoke({"driver_name": func})

asyncio.run(analyze_driver_calls())
```

#### 3.2 MMIO操作安全分析

```python
async def analyze_mmio_operations():
    # ... 客户端初始化
    
    # 获取MMIO函数列表
    mmio_funcs = await tools["collect_mmio_func_list"].invoke({})
    
    # 分析每个MMIO函数
    for func_name in mmio_funcs:
        mmio_info = await tools["collect_mmio_func_info"].invoke({
            "func_name": func_name
        })
        
        # 安全检查
        if is_potential_risk(mmio_info):
            print(f"安全风险: {func_name}")
            
    # 获取MMIO相关文件
    mmio_files = await tools["collect_mmio_files"].invoke({})
```

#### 3.3 驱动类型使用分析

```python
async def analyze_driver_types():
    # ... 客户端初始化
    
    # 分析驱动结构体
    driver_structs = ["uart_config", "i2c_device", "spi_handle"]
    for struct in driver_structs:
        struct_info = await tools["collect_struct_or_enum_info"].invoke({
            "struct_name": struct
        })
        
    # 分析枚举类型
    enum_info = await tools["collect_struct_or_enum_info"].invoke({
        "struct_name": "uart_baudrate"
    })
```

### 阶段4：代码修复和重新编译

#### 4.1 代码修复建议

基于分析结果，系统会提供：
- 不安全MMIO操作的修复建议
- 驱动调用关系的优化建议
- 类型使用的一致性检查

#### 4.2 重新编译测试

```bash
# 应用修复后重新编译
./build.sh

# 清理构建缓存（如果需要）
./clear.sh
```

## 支持的驱动测试类型

### 1. 驱动函数调用分析
- 分析非驱动文件对驱动函数的调用
- 识别潜在的调用关系问题
- 验证驱动接口的正确使用

### 2. 驱动类型使用分析
- 检查驱动类型在非驱动文件中的使用
- 验证类型转换的安全性
- 识别类型不匹配问题

### 3. MMIO操作分析
- 分析内存映射IO操作
- 识别不安全的MMIO访问模式
- 检查地址对齐和访问权限

### 4. 驱动注册分析
- 分析驱动注册和初始化过程
- 验证驱动注册的正确性
- 检查驱动依赖关系

### 5. 安全风险评估
- 识别潜在的安全漏洞
- 分析权限提升风险
- 检查输入验证完整性

## 测试工具详解

### 数据收集工具

#### 驱动收集器
- `driver_info_driverfromfunction_collector` - 收集驱动函数信息
- `driver_info_driverfromdeclstmt_collector` - 收集声明语句中的驱动信息
- `driver_info_driverfromexpr_collector` - 收集表达式中的驱动信息

#### MMIO收集器
- `mmioinfo_mmioexpr_collector` - 收集MMIO表达式信息
- `mmioinfo_interestingmmioexpr_collector` - 收集感兴趣的MMIO表达式

#### 函数收集器
- `info_function_collector` - 收集函数定义信息
- `info_function_call_collector` - 收集函数调用信息

### 分析工具

#### 统一分析器
整合所有收集的信息进行综合分析，提供：
- 驱动调用关系图
- 安全风险评估报告
- 代码修复建议

#### 驱动定位器
基于CodeQL查询识别：
- 驱动文件（DriverFile）
- 驱动函数（DriverFunction） 
- 驱动类型（DriverType）
- 驱动调用关系

## 测试结果输出

### JSON格式结果
```json
{
  "driver_analysis": {
    "function_calls": [...],
    "mmio_operations": [...],
    "security_risks": [...],
    "repair_suggestions": [...]
  }
}
```

### 可视化报告
- 函数调用关系图
- 安全风险热力图
- 代码修复建议列表

### 详细分析信息
- 精确的文件位置和行号
- 调用栈深度分析
- 类型使用统计

## 自动化测试脚本

### 完整的端到端测试

```bash
#!/bin/bash
# automated_zephyr_driver_test.sh

set -euo pipefail

# 配置参数
ZEPHYR_PROJECT="/path/to/zephyr-project"
BOARD="qemu_riscv64"
APP="samples/drivers/uart"
DB_PATH="/tmp/zephyr-driver-db"
TEST_SCRIPT="comprehensive_driver_test.py"

echo "=== Zephyr驱动自动化测试开始 ==="

# 1. 环境检查
echo "检查环境依赖..."
which codeql >/dev/null || { echo "CodeQL未安装"; exit 1; }
which west >/dev/null || { echo "Zephyr west未安装"; exit 1; }

# 2. 构建项目
echo "构建Zephyr项目..."
cd "$ZEPHYR_PROJECT"
west build -b "$BOARD" "$APP"

# 3. 创建CodeQL数据库
echo "创建CodeQL数据库..."
codeql database create "$DB_PATH" \
    --language=cpp \
    --source-root="$ZEPHYR_PROJECT" \
    --command="west build -b $BOARD $APP"

# 4. 执行驱动分析
echo "执行驱动分析..."
python "$TEST_SCRIPT" --db-path "$DB_PATH"

# 5. 生成测试报告
echo "生成测试报告..."
python generate_report.py --db-path "$DB_PATH"

echo "=== 自动化测试完成 ==="
```

### 持续集成集成

```yaml
# .github/workflows/driver-test.yml
name: Zephyr Driver Testing

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  driver-test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Build Zephyr project
      run: |
        cd testcases/zephyr_server
        ./build.sh
    
    - name: Run driver tests
      run: |
        python -m pytest tests/ -v
```

## 故障排除

### 常见问题

1. **数据库创建失败**
   - 检查Zephyr项目路径是否正确
   - 验证构建命令是否成功执行
   - 确认CodeQL版本兼容性

2. **分析服务启动失败**
   - 检查数据库路径权限
   - 验证Python依赖是否完整安装
   - 查看日志文件获取详细错误信息

3. **测试结果异常**
   - 确认测试用例配置正确
   - 检查驱动函数名称拼写
   - 验证代码修改是否影响分析结果

### 调试技巧

- 启用详细日志：设置`ai_log_enable = True`
- 使用调试模式启动服务
- 检查中间文件生成情况
- 验证查询结果格式

## 最佳实践

### 测试策略
1. **分层测试**：从单元测试到集成测试逐步进行
2. **回归测试**：确保代码修改不影响现有功能
3. **边界测试**：测试极端情况和边界条件
4. **性能测试**：监控驱动性能指标

### 代码质量
1. **代码审查**：结合静态分析结果进行代码审查
2. **安全编码**：遵循安全编码规范
3. **文档维护**：保持测试文档和代码同步更新
4. **版本控制**：使用版本控制管理测试用例和配置

## 扩展开发

### 添加新的驱动测试

1. **创建新的CodeQL查询**
   ```ql
   // queries/collectors/driver/new_driver_test.ql
   import cpp
   
   class NewDriverTest extends ... {
     // 实现新的驱动测试逻辑
   }
   ```

2. **添加收集器工具**
   ```python
   # tools/collector/new_driver.py
   from tools.collector.base import BaseCollector
   
   class NewDriverCollector(BaseCollector):
       def collect(self, db_path: str):
           # 实现新的驱动信息收集逻辑
           pass
   ```

3. **集成到分析流程**
   ```python
   # 在统一分析器中集成新的测试
   analyzer.add_collector(NewDriverCollector())
   ```

## 总结

本指南详细介绍了在Zephyr环境中使用LCMHalMCPServer进行驱动测试的完整流程。通过结合CodeQL静态分析和LLM智能分析，可以全面测试驱动的正确性、安全性和兼容性，为嵌入式系统开发提供可靠的测试保障。

通过遵循本指南的步骤和最佳实践，开发团队可以建立高效的驱动测试流程，提高代码质量，减少潜在的安全风险。
