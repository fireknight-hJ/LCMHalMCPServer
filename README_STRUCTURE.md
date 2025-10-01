# lcmhalmcp 项目目录结构规划

## 当前问题分析
- 所有工具函数都集中在 `server.py` 中，导致文件臃肿
- 缺乏模块化，难以维护和扩展
- CodeQL 查询脚本组织不够清晰
- 缺少统一的分析模块架构

## 推荐的目录结构

```
lcmhalmcp/
├── README.md
├── requirements.txt
├── server.py                    # 主服务器入口
├── core/                        # 核心模块
│   ├── __init__.py
│   ├── codeql_client.py         # CodeQL 客户端封装 (从 codeql_mcp.py 重构)
│   ├── mcp_server.py            # MCP 服务器核心逻辑
│   └── config.py                # 配置管理
├── tools/                       # 工具模块
│   ├── __init__.py
│   ├── base_tool.py             # 工具基类
│   ├── query_tools/             # 查询相关工具
│   │   ├── __init__.py
│   │   ├── basic_queries.py     # 基础查询工具
│   │   └── quick_eval.py        # 快速评估工具
│   ├── collector_tools/         # 数据收集器工具
│   │   ├── __init__.py
│   │   ├── driver_collectors.py # 驱动相关收集器
│   │   ├── mmio_collectors.py   # MMIO 相关收集器
│   │   ├── function_collectors.py # 函数相关收集器
│   │   └── struct_collectors.py # 结构体相关收集器
│   └── analysis_tools/          # 分析工具
│       ├── __init__.py
│       ├── unified_analyzer.py  # 统一分析器
│       └── cache_manager.py     # 缓存管理
├── queries/                     # CodeQL 查询文件
│   ├── codeql-pack.yml
│   ├── codeql-pack.lock.yml
│   ├── libraries/               # 查询库文件
│   │   ├── DriverLocator.qll
│   │   ├── RegistrationLocator.qll
│   │   └── MMIOAnalyzer.qll
│   ├── collectors/              # 收集器查询
│   │   ├── driver/
│   │   │   ├── driver_info_driverfromfunction_collector.ql
│   │   │   ├── driver_info_driverfromdeclstmt_collector.ql
│   │   │   └── ...
│   │   ├── mmio/
│   │   │   ├── mmio_operation_finder.ql
│   │   │   ├── mmio_structure_finder.ql
│   │   │   └── ...
│   │   ├── function/
│   │   │   ├── info_function_collector.ql
│   │   │   ├── info_function_call_collector.ql
│   │   │   └── ...
│   │   └── struct/
│   │       ├── info_struct_collector.ql
│   │       └── ...
│   ├── analyzers/               # 分析器查询
│   │   ├── unified_analysis.ql
│   │   └── ...
│   └── tests/                   # 测试查询
│       ├── test_driver_mmio_expr.ql
│       ├── test.ql
│       └── ...
├── utils/                       # 工具函数
│   ├── __init__.py
│   ├── db_cache.py              # 数据库缓存
│   ├── db_file.py               # 数据库文件操作
│   ├── query_utils.py           # 查询工具函数
│   └── file_utils.py            # 文件工具函数
├── models/                      # 数据模型
│   ├── __init__.py
│   ├── query_result.py          # 查询结果模型
│   ├── analysis_result.py       # 分析结果模型
│   └── driver_info.py           # 驱动信息模型
└── tests/                       # 测试文件
    ├── __init__.py
    ├── test_server.py
    ├── test_tools.py
    └── test_utils.py
```

## 主要改进点

### 1. 模块化工具系统
- **基础工具类**: 提供统一的工具注册和管理
- **分类工具模块**: 按功能分类，便于维护和扩展
- **自动工具发现**: 支持动态加载新工具

### 2. 统一分析模块
- **UnifiedAnalyzer**: 预收集多种信息的统一分析器
- **缓存机制**: 避免重复查询，提高性能
- **结果聚合**: 整合多个收集器的结果

### 3. 查询文件组织
- **按功能分类**: 驱动、MMIO、函数、结构体等
- **库文件分离**: 可重用的查询库
- **测试查询**: 专门的测试目录

### 4. 数据模型
- **结构化结果**: 统一的查询结果格式
- **类型安全**: 使用数据类定义模型
- **序列化支持**: 便于结果存储和传输

## 迁移计划

### 第一阶段：基础重构
1. 创建新的目录结构
2. 重构 `codeql_mcp.py` 为 `core/codeql_client.py`
3. 创建工具基类和分类

### 第二阶段：工具迁移
1. 将现有工具迁移到对应的工具模块
2. 实现统一分析器
3. 重构查询文件组织

### 第三阶段：优化和测试
1. 添加自动工具发现机制
2. 完善缓存管理
3. 添加测试用例

## 扩展性设计

### 添加新收集器工具
```python
# 在 tools/collector_tools/ 中添加新文件
from tools.base_tool import BaseCollectorTool

class NewDriverCollector(BaseCollectorTool):
    def __init__(self):
        super().__init__(
            name="new_driver_collector",
            description="Collect new driver information",
            query_file="queries/collectors/driver/new_driver_collector.ql"
        )
    
    async def execute(self, db_path: str, **kwargs):
        # 实现具体的收集逻辑
        pass
```

### 统一分析器使用
```python
from tools.analysis_tools.unified_analyzer import UnifiedAnalyzer

analyzer = UnifiedAnalyzer()
results = await analyzer.analyze_database(db_path, collect_types=[
    'driver_info', 'mmio_operations', 'function_calls'
])
```

这个结构设计将显著提高项目的可维护性和扩展性，支持你未来添加更多功能和统一分析模块的需求。
