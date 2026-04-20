# MMIO 结构体实例定位模式总结（基于 LCMHalMCP 仓库证据）

日期：2026-03-18  
适用范围：本仓库中的简化 MMIO 用例（如 `testcases/zephyr_uart_official/`、`testcases/uart_driver/`）以及部分 demo 的替换/分析日志（如 `testcases/server/stm32/UART_Hyperterminal_IT/replacement_log.md`、`testcases/server/rtthread/stm32f401-st-nucleo/fatfs/replacement_log.md`）。  

## 背景

定位 **MMIO（Memory-Mapped I/O）结构体实例**是识别硬件相关代码的关键步骤：只有先找出“寄存器块结构体指针”在代码中是如何被构造/传递/保存的，才能进一步稳定地识别寄存器字段访问（如 `->DR`、`->CR1`）以及由此派生的“硬件依赖函数”。

结合本项目中出现的代码形态与日志证据，可以将“MMIO 结构体实例定位”归纳为三类典型模式（与论文写作表述一致，但此处每个模式都给出仓库内可追溯证据）。

## 系统实现：这三种模式如何落到 CodeQL 识别

本节补齐“设计文档层面”的实现细节：在 LCMHalMCP 中，这三类模式不是停留在文字总结，而是直接体现在 **CodeQL 查询（`.ql`）→ Python 收集器（`tools/collector/`）→ 上层 Agent 使用** 的流水线里。

### 1) CodeQL 查询入口与产物

仓库中与 MMIO 相关的 collector 查询主要在 `queries/collectors/mmio/`，典型查询会 `import libraries.MMIOAnalyzer` 并输出“表达式字符串 + 所属函数 + 文件 + 行号 + 类型检查结果”等字段。例如：

```1:10:/home/haojie/workspace/lcmhalmcp/queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql
import cpp
import libraries.MMIOAnalyzer

from
    Function func,
    InterestingMMIOExpr expr
where
    isInterestingMMIOFunction(func) and
    expr.getEnclosingFunction() = func 
// select func, expr, 
select expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.checkExprType(), expr.checkEnclosingType()
```

以及（更偏“追踪后表达式”的版本）：

```1:10:/home/haojie/workspace/lcmhalmcp/queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql
import cpp
import libraries.MMIOAnalyzer

from
    Function func,
    MMIOTracedExpr expr
where
    expr.getEnclosingFunction() = func and
    isInterestingMMIOFunction(func)
select expr.toString(), expr.getEnclosingFunction().getName(), expr.getFile().getAbsolutePath().toString(), expr.getLocation().getStartLine(), expr.checkExprType(), expr.checkEnclosingType()
```

说明：
- `libraries.MMIOAnalyzer` 在当前仓库中以“依赖库”的方式被引用（查询中可见 `import`），其内部谓词实现不在本仓库文件树内；但**本系统对该库的使用方式、输出字段形态、以及后续处理逻辑**在本仓库是可追溯的（见下一节）。

### 2) Python 收集器如何消费 CodeQL 结果

在配置层，MMIO 相关查询文件路径由 `config/collector_infos.py` 统一管理：

```15:31:/home/haojie/workspace/lcmhalmcp/config/collector_infos.py
# mmio & driver infos collector
mmio_structure_query_file = ""
mmio_function_query_file = "queries/collectors/mmio/info_mmio_function_collector.ql"
driver_function_query_file = "queries/collectors/mmio/info_driver_function_collector.ql"
buffer_function_query_file = "queries/collectors/mmio/info_buffer_function_collector.ql"
...
# mmio info collector
mmioinfo_interestingmmioexpr_query_file = "queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql"
mmioinfo_mmioexpr_query_file = "queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql"
mmioinfo_interestingmmiofunccontains_query_file = "queries/collectors/mmio/mmioinfo_interestingmmiofunccontains_collector.ql"
```

收集阶段由 `tools/collector/mmio.py` 负责：它运行查询、把结果解析成 `MmioExprInfo` 等结构化对象，并按函数名聚合到 `mmioinfo_*_dict` 里：

```150:268:/home/haojie/workspace/lcmhalmcp/tools/collector/mmio.py
    def collect_infos(self, db_path: str, force_refresh: bool = False) -> None:
        """
        收集所有信息，支持缓存机制
        """
        self.db_path = db_path
        ...
        collectors = [
            ("MMIO函数信息", self._collect_mmio_functions),
            ("驱动函数信息", self._collect_driver_functions),
            ("缓冲函数信息", self._collect_buffer_functions),
            ("MMIO表达式信息", self._collect_mmioinfo_interestingmmioexpr),
            ("MMIO表达式信息", self._collect_mmioinfo_mmioexpr),
            ("MMIO函数包含信息", self._collect_mmioinfo_interestingmmiofunc_contains),
        ]
        ...
    def _collect_mmioinfo_interestingmmioexpr(self) -> None:
        """收集MMIO表达式信息"""
        result = self._run_query_and_return_json(mmioinfo_interestingmmioexpr_query_file)
        if result:
            expr_dict = MmioExprInfo.resolve_from_query_result(self.db_path, result)
            self.mmioinfo_interestingmmioexpr_dict.update(expr_dict)
...
    def _collect_mmioinfo_mmioexpr(self) -> None:
        """收集MMIO表达式信息"""
        result = self._run_query_and_return_json(mmioinfo_mmioexpr_query_file)
        if result:
            expr_dict = MmioExprInfo.resolve_from_query_result(self.db_path, result)
            self.mmioinfo_mmioexpr_dict.update(expr_dict)
```

并且在 `tools/collector/collector.py` 中，这些 MMIO 信息会作为全局 `CodebaseInfos` 的一部分被加载，供上层模块统一查询：

```9:18:/home/haojie/workspace/lcmhalmcp/tools/collector/collector.py
class CodebaseInfos:
    def __init__(self, db_path: str = ""):
        self.db_path = db_path
        if not db_path:
            return
        self.common_infos = create_commoncodebase_info(db_path, force_refresh=False)
        self.driver_infos = create_drivercodebase_info(db_path, force_refresh=False)
        self.mmio_infos = create_mmiocodebase_info(db_path, force_refresh=False)
```

### 3) 与“三种定位模式”的对应关系（实现视角）

从实现角度看，这三种模式的作用是：把“寄存器字段访问”追溯到一个可被 CodeQL 稳定描述的**基对象表达式**（base object expression）。在本仓库里，我们至少能看到两种可直接落地的实现片段：

- **常量基址的追踪（模式一/模式三的关键证据链）**：`queries/tool_dataflow_trace.ql` 展示了用 CodeQL DataFlow/TaintTracking 将“常量大值表达式（外设基址）”追踪到后续的变量访问/解引用位置的做法：

```16:34:/home/haojie/workspace/lcmhalmcp/queries/tool_dataflow_trace.ql
predicate isMMIOConstantExpr(ConstantExpr src_mmio) {
    exists( DataFlow::Node source, DataFlow::Node sink, Expr varAccess, PointerDereferenceExpr deref | 
        source.asExpr() = src_mmio and
        isConstantBigValueExpr(src_mmio) and
        sink.asExpr() = varAccess and 
        deref.getOperand() = varAccess and
        TaintFlow::flow(source, sink) and
        not sink.asExpr().getFile() instanceof DriverFile
    )
}

predicate isMMIOTracedExpr(Expr e) {
    exists( DataFlow::Node source, DataFlow::Node sink, ConstantExpr src_mmio | 
        source.asExpr() = src_mmio and
        isMMIOConstantExpr(src_mmio) and
        sink.asExpr() = e and 
        TaintFlow::flow(source, sink) and
        not sink.asExpr().getFile() instanceof DriverFile
    )
    
}
```

- **指针参数 + 常量实参（模式三的另一条实现线索）**：测试查询 `queries/tests/test_mmio_operation_patch.ql` 里给出了“函数第 0 个参数是指针类型，实参是常量大值表达式”的识别思路（用于定位“把常量基址传给接受结构体指针的驱动函数”的调用点）：

```15:25:/home/haojie/workspace/lcmhalmcp/queries/tests/test_mmio_operation_patch.ql
predicate isMMIOStructure_MK(Struct s){
    exists( FunctionCall call, Expr e, TypedefType typeDef | 
        call.getTarget().getParameter(0).getType() instanceof PointerType and
        (
            (call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = typeDef and
            typeDef.getBaseType() = s) or
            call.getTarget().getParameter(0).getType().(PointerType).getBaseType() = s
        ) and
        call.getArgument(0) = e and
        isConstantBigValueExpr(e)
    )
}
```

对模式二（`Instance`）而言，当前仓库里“最终 collector 查询如何精确匹配 `Instance` 字段写入点”对应的 `.ql` 规则不在 `queries/collectors/mmio/` 中直接出现（更可能封装在 `libraries.MMIOAnalyzer` 的谓词里）。但从系统整体链路上，模式二仍以“表达式级别的 toString + 行号定位”的方式被收集并交给上层 Agent（例如 `expr.toString()` 里会包含 `huart->Instance` 这种基对象表达式形态）。

## 三种典型定位模式

### 模式一：直接地址强转（Direct cast from fixed base address）

**定义**：将固定外设基地址（宏或字面量）强制转换为外设寄存器结构体指针，常见于寄存器定义/简化驱动头部。

**识别特征**：
- 出现类似 `((XXX_TypeDef *)XXX_BASE)` 的宏或赋值；
- 后续对该指针做字段访问：`XXX->REG = ...`、`XXX->REG & ...`。

**仓库证据（示例）**：

```25:27:/home/haojie/workspace/lcmhalmcp/testcases/zephyr_uart_official/src/main.c
#define USART1 ((USART_TypeDef *)USART1_BASE)
#define USART2 ((USART_TypeDef *)USART2_BASE)
#define USART3 ((USART_TypeDef *)USART3_BASE)
```

并且同文件中直接对 `USART1->CR1/BRR/...` 进行访问，属于“强转得到实例 → 直接字段访问”的闭环（例如 `mmio_uart_init_direct`）。

另一个同类证据：

```18:21:/home/haojie/workspace/lcmhalmcp/testcases/uart_driver/src/test_mmio_driver.c
#define USART1_BASE 0x40011000UL
#define USART1 ((USART_TypeDef *)USART1_BASE)
```

### 模式二：间接初始化（Handle/descriptor assigns base to Instance）

**定义**：通过句柄（handle）/配置表（descriptor/config table）等间接结构，把外设基地址赋值给某个“寄存器块指针成员”，后续通过该成员完成寄存器访问。STM32 HAL 生态中常见成员名为 `Instance`。

**识别特征**：
- 存在结构体指针类型成员（常见命名 `Instance`）；
- 该成员被赋值为外设基地址宏、外设实例数组项或配置表中的 `Instance` 字段；
- 寄存器访问呈现为多级解引用：`hxxx->Instance->REG` 或 `obj.handle.Instance->REG`。

**仓库证据（示例 1：HAL 句柄 Instance 赋值）**：

在 `UART_Hyperterminal_IT` 的替换日志中，`BSP_COM_Init` 包含对 `huart->Instance` 的赋值（该日志记录了函数内容与替换建议/更新，属于本项目工作流的真实产物/归档证据）：

```110:113:/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/UART_Hyperterminal_IT/replacement_log.md
  /* USART configuration */
  huart->Instance = COM_USART[COM];
  HAL_UART_Init(huart);
```

**仓库证据（示例 2：配置表/描述符驱动的 Instance 传递）**：

在 RT-Thread STM32F401 FATFS 的替换日志中，`rt_hw_spi_bus_init` 体现了“配置表字段 `spi_config[i].Instance` → 句柄字段 `handle.Instance`”的赋值链：

```3669:3674:/home/haojie/workspace/lcmhalmcp/testcases/server/rtthread/stm32f401-st-nucleo/fatfs/replacement_log.md
    for (rt_size_t i = 0; i < sizeof(spi_config) / sizeof(spi_config[0]); i++)
    {
        spi_bus_obj[i].config = &spi_config[i];
        spi_bus_obj[i].spi_bus.parent.user_data = &spi_config[i];
        spi_bus_obj[i].handle.Instance = spi_config[i].Instance;
```

这类形态的关键在于：**MMIO 实例不再由“字面地址强转”直接出现，而是沿着初始化代码的数据流，被写入句柄的 `Instance` 成员**。因此定位模式二通常需要结合“结构体成员识别 + 赋值点追踪（dataflow）”来完成。

**与本项目静态分析模块的关系（论文内证据）**：

仓库中的论文/设计文档在静态分析实体定义里明确把 `huart->Instance` 作为“MMIO 字段访问基对象表达式”的典型例子：

```138:164:/home/haojie/workspace/lcmhalmcp/doc/THESIS_CH3_系统设计与实现.md
- **MMIO 字段访问实体**：记录某一次寄存器字段访问的基对象表达式（如 `huart->Instance`）、字段名（如 `DR`）、访问方向（读/写/读改写）、所属函数、语句位置等。
...
   huart->Instance->DR = (uint8_t)ch;
```

这段表述与上述 replacement log 中的“Instance 赋值链”是互补的：前者强调“访问侧（use-site）长什么样”，后者提供“初始化侧（def-site）如何把基址写入 Instance”的证据。

### 模式三：常量指针参数（Const/typed pointer parameter）

**定义**：函数通过参数接收 MMIO 结构体指针（寄存器块基址），常见于底层驱动/通用外设操作函数。调用者可以来自模式一（直接传 `USART1`）或模式二（传 `huart->Instance`）。

**识别特征**：
- 函数形参类型为某个寄存器结构体指针，如 `USART_TypeDef *uart`；
- 函数体内部通过该参数访问寄存器字段：`uart->CR1 = ...`。

**仓库证据（示例）**：

```55:60:/home/haojie/workspace/lcmhalmcp/testcases/uart_driver/src/test_mmio_driver.c
// 使用指针的MMIO操作
void mmio_uart_init_pointer(USART_TypeDef *uart) {
    // 通过指针访问MMIO寄存器
    uart->CR1 = 0x2000;
    uart->BRR = 0x0341;
}
```

该模式的价值在于：**一旦能识别参数类型为 MMIO 结构体指针，就能把“硬件依赖”与该函数强绑定**，且可进一步沿着调用链向上传播（谁把 `USART1` / `huart->Instance` 传进来的）。

## 表 3.1：三种模式对比（面向静态识别）

| 模式 | 典型形态（示意） | 本仓库证据入口 | 主要识别点 | 难点 |
|------|------------------|----------------|------------|------|
| 模式一：直接强转 | `#define USART1 ((USART_TypeDef*)USART1_BASE)` | `testcases/zephyr_uart_official/src/main.c` | 常量基址 + 强转 + `->REG` | 宏/内联展开、不同厂商命名 |
| 模式二：间接初始化 | `huart->Instance = ...;` / `handle.Instance = config.Instance;` | `testcases/server/stm32/UART_Hyperterminal_IT/replacement_log.md`、`testcases/server/rtthread/stm32f401-st-nucleo/fatfs/replacement_log.md` | 结构体成员 `Instance` 的“写入点”与后续 `Instance->REG` 的“使用点” | 需要数据流追踪；`Instance` 字段可能多级嵌套 |
| 模式三：指针参数 | `fn(USART_TypeDef *uart) { uart->CR1=...; }` | `testcases/uart_driver/src/test_mmio_driver.c` | 形参类型是 MMIO 结构体指针 | 类型别名/宏类型、跨文件声明 |

## 小结

- 模式一/三通常能通过“语法形态 + 类型信息”较直接地定位到 MMIO 实例；
- 模式二的关键在于“把基址写入 `Instance` 的赋值语句”往往分散在初始化流程或配置表遍历中，需要结合 **结构体成员识别**与**数据流追踪**，才能把 `huart->Instance->REG` 这种使用点可靠地关联回“外设基址来源”。

## 附录：证据索引

- `testcases/zephyr_uart_official/src/main.c`：模式一（强转宏）+ 直接字段访问
- `testcases/uart_driver/src/test_mmio_driver.c`：模式三（指针参数）+ 指针字段访问
- `testcases/server/stm32/UART_Hyperterminal_IT/replacement_log.md`：模式二（`huart->Instance = ...` 赋值）
- `testcases/server/rtthread/stm32f401-st-nucleo/fatfs/replacement_log.md`：模式二（配置表/描述符到 `handle.Instance`）
- `doc/THESIS_CH3_系统设计与实现.md`：模式二（`huart->Instance->DR` 作为 MMIO 字段访问基对象示例）


<!--
## 静态分析模块：骗动函数识别与调用图构建

### 1) 定义与核心准则

本模块的核心任务是：从固件源代码中识别“骗动函数”，并为后续智能替换阶段提供候选目标列表。为了与仓库实现对齐，本文将“骗动函数”在实现层面对应为“驱动函数（driver function）”集合。

核心准则（定位规则）：
1. 凡是包含 `MMIO（文中原始表述为 MMIC）` 访问的函数，均定义为驱动函数；理由是此类函数与硬件寄存器交互具有直接性，且其输出位置（字段访问表达式与所在函数）可被 CodeQL 稳定捕获，满足后续替换需要的确定性证据链。
2. 在实现中，该“包含 MMIO 访问”的判定由 `libraries.MMIOAnalyzer` 中的谓词/类型（例如 `InterestingMMIOExpr` 与 `isInterestingMMIOFunction(func)`）驱动；而驱动函数集合则由 `DriverFunction` 对应的 CodeQL 查询直接输出。

实现对齐证据：
- `tools/collector/mmio.py` 中维护了驱动函数缓存容器 `driver_functions`（键为函数名，值为 `FunctionInfo`）。证据：`tools/collector/mmio.py`（`driver_functions: Dict[str, FunctionInfo]`、以及 `_load_from_dict`/`to_dict` 对该字段的恢复/序列化）。
- `queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 里使用了 `isInterestingMMIOFunction(func)` 进行函数过滤（即“包含 MMIO 访问”的判定入口）。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 中 `where isInterestingMMIOFunction(func) and expr.getEnclosingFunction() = func`。

### 2) 概念流程到仓库实现的映射

下述流程按用户给定的 4 步展开，并逐一映射到仓库中的 “MMIO collector / Driver collector / CodeQL queries / models”。

1. 三种定位模式识别所有 MMIO 结构体实例  
   这一阶段在本仓库中以 CodeQL “表达式级别识别”实现：通过 `InterestingMMIOExpr` 与 `MMIOTracedExpr` 的查询结果，把“寄存器块结构体实例”及其在源码中的基对象形态（例如 `->` 解引用所形成的表达式）映射为可记录的表达式对象。  
   对应证据（表达式识别入口）：
   - `queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 输出 `expr.toString()`、所属函数、文件与行号，并同时附带 `expr.checkExprType()` / `expr.checkEnclosingType()`。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 的 `select` 列表。
   - `queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql` 输出 `MMIOTracedExpr expr` 的同类字段。证据：`queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql` 中 `select expr.toString(), ... expr.checkExprType(), expr.checkEnclosingType()`。

2. 对每个 MMIO 结构体实例追踪字段访问表达式，记录字段名/访问类型/语句位置/函数归属  
   仓库通过“表达式字符串 + 位置 + 表达式类型”来表达字段访问信息：
   - 字段名/访问位置：`MmioExprInfo.name` 对应查询结果的 `expr.toString()`（即表达式字符串形态，通常包含类似 `hxxx->Instance->REG` 这样的基对象与字段访问片段）。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 中 `select expr.toString(), ...`；以及 `models/query_results/mmio.py` 中 `MmioExprInfo.resolve_from_query_result` 将 `item[0]` 赋值给 `name`。
   - 访问类型（读/写）：当前模型中并未显式存储独立的 `read/write` 布尔字段；访问方向由 `expr_type` 表征。`MmioExprInfo.expr_type` 对应 CodeQL 的 `expr.checkExprType()`。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 的 `select ... expr.checkExprType()`；以及 `models/query_results/mmio.py` 中 `MmioExprInfo` 字段 `expr_type` 与 `resolve_from_query_result` 的映射关系。
   - 语句位置与函数归属：`MmioExprInfo.file_path` + `MmioExprInfo.start_line` 表示语句位置；`MmioExprInfo.function` 表示所属函数名。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 的 `getFile().getAbsolutePath().toString()` 与 `getLocation().getStartLine()`；以及 `models/query_results/mmio.py` 中对应字段与解析逻辑。

3. 汇总所有包含 MMIO 字段访问的函数，形成驱动函数列表  
   在实现中，“包含 MMIO 访问的函数集合”通过驱动函数 CodeQL 查询输出，并由 `tools/collector/mmio.py` 解析为 `MmioCodebaseInfo.driver_functions`：
   - CodeQL 侧：`queries/collectors/mmio/info_driver_function_collector.ql` 以 `DriverFunction f` 为输入集合输出函数名、文件与起始行等信息（`select f.getName(), f.getFile().getAbsolutePath(), f.getLocation().getStartLine(), ...`）。证据：`queries/collectors/mmio/info_driver_function_collector.ql` 的 `from DriverFunction f ... select f.getName()...`。
   - Python collector：`tools/collector/mmio.py` 的 `_collect_driver_functions()` 运行 `driver_function_query_file` 并把结果填入 `self.driver_functions[func_name] = FunctionInfo(...)`。证据：`tools/collector/mmio.py` 中 `_collect_driver_functions` 内部对 `self.driver_functions` 的赋值。
   - 驱动函数输出字段：`MmioCodebaseInfo` 使用 `driver_functions` 作为驱动函数缓存容器。证据：`tools/collector/mmio.py` 中 dataclass 字段与缓存加载/保存逻辑。

4. 分析驱动函数之间的调用关系，构建函数调用图  
   调用图的边集合由 Driver collector 采集并缓存为 `driverto_functioncall_dict`：
   - CodeQL 侧：`queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql` 以 `DriverToCall call` 为关系输入，输出：调用边字符串（`call.toString2()`）、目标函数（`call.getTargetFunction().toString()`）、封装函数（`call.getEnclosingFunction().getName()`）、调用位置（文件/起始行）以及调用类型 `call.isDirectCall()`。证据：该 `.ql` 文件的 `select` 列表。
   - Python collector：`tools/collector/driver.py` 在 `_collect_driverto_functioncall()` 中运行 `driverto_functioncall_query_file`，并把查询结果解析为 `DriverFunctionCallInfo` 列表，聚合到 `self.driverto_functioncall_dict`。证据：`tools/collector/driver.py` 中 `driverto_functioncall_dict` 字段定义与 `_collect_driverto_functioncall` 的更新逻辑。
   - 数据模型：`models/query_results/driver.py` 中 `DriverFunctionCallInfo` 明确了调用图边的字段：`name`（边标识/文本）、`callee_name`、`file_path`、`start_line`、`start_line_content`、以及 `call_type`。证据：`models/query_results/driver.py` 的 `DriverFunctionCallInfo` 定义与 `resolve_from_query_result` 映射逻辑。

### 3) 实现细节：模块级组件与数据流

本项目中与“静态分析模块”直接相关的组件可概括为两条并行的数据流：

1. MMIO 数据流（生成候选驱动函数与 MMIO 字段访问表达式集合）
   - 查询路径配置：`config/collector_infos.py` 通过变量将 `.ql` 文件路径映射到 collector 运行时。证据：`config/collector_infos.py` 中 `driver_function_query_file`、`mmioinfo_interestingmmioexpr_query_file` 与 `mmioinfo_mmioexpr_query_file` 等字段。
   - 采集与缓存：`tools/collector/mmio.py` 的 `collect_infos()` 按顺序调用多个 `_collect_*` 方法，并把结果写入 `MmioCodebaseInfo` 的不同字典/列表。关键容器包括：
     - `driver_functions`：驱动函数候选列表
     - `mmioinfo_interestingmmioexpr_dict` / `mmioinfo_mmioexpr_dict`：MMIO 字段访问表达式集合（按函数归组）
   证据：`tools/collector/mmio.py` 中 `collect_infos()` 的 collector 执行列表，以及 `_collect_driver_functions` / `_collect_mmioinfo_interestingmmioexpr` / `_collect_mmioinfo_mmioexpr` 的实现。

2. Driver 调用图数据流（在驱动函数集合上构建调用边）
   - 查询路径配置：同样由 `config/collector_infos.py` 指向 `driverto_functioncall_query_file`。证据：`config/collector_infos.py` 中 `driverto_functioncall_query_file = "queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql"`。
   - 调用边采集与缓存：`tools/collector/driver.py` 的 `collect_infos()` 运行 `_collect_driverto_functioncall()` 并更新 `driverto_functioncall_dict`。证据：`tools/collector/driver.py` 中 dataclass 字段与 `_collect_driverto_functioncall` 实现。

### 4) 输出产物（目标列表与调用图）

从当前实现层面，本模块输出两类核心产物（均可在 collector 的缓存 JSON 中追溯）：

1. 目标列表：`MmioCodebaseInfo.driver_functions`
   - 含义：被判定为包含 MMIO 访问的“驱动函数”集合；
   - 结构：字典，key 为函数名，value 为 `FunctionInfo`（函数所在文件与起始行以及函数内容片段）。证据：`tools/collector/mmio.py` 中 `driver_functions` 字段、以及 `_collect_driver_functions` 的填充逻辑。

2. 调用图边集合：`DriverCodebaseInfo.driverto_functioncall_dict`
   - 含义：以驱动函数为“调用方”，记录它调用到的其他函数（callee）的边集合；
   - 结构：字典，key 为调用方函数名，value 为 `DriverFunctionCallInfo` 列表；每条边包含 `callee_name`、调用位置（`file_path`/`start_line`）以及 `call_type`（由 CodeQL `call.isDirectCall()` 表征）。证据：`tools/collector/driver.py` 与 `models/query_results/driver.py` 中对应字段。

### 5) 关于“读/写访问类型”的表示方法（避免字段臆造）

由于仓库侧的 `MmioExprInfo` 未见显式的 `read`/`write` 独立字段，本节明确说明：
- 访问类型（读/写方向）由 `expr_type` 表征；`expr_type` 的来源是 CodeQL 表达式 `expr.checkExprType()` 的返回值。
- 若需要把表达式进一步关联到“函数包含的 MMIO 类型/包含点”以便做更细粒度分类，可结合 `MmioFunctionContainsInfo.flag` 这类包含辅助字段；但 `flag` 的用途是承载 CodeQL 输出的包含/分类标志，而不是直接替代“读/写方向”的判断。
- 因此任何面向“读/写”的下游判断，需要基于 `expr_type` 的实际取值语义进行解释（而不是依赖一个并不存在的 `read/write` 字段）。  
证据：`models/query_results/mmio.py` 中 `MmioExprInfo.expr_type` 与 `MmioFunctionContainsInfo.flag`；以及两类 mmio 表达式 collector `.ql` 中的 `expr.checkExprType()`。

### 6) 附录：证据索引（静态分析模块追加）

- `tools/collector/mmio.py`：驱动函数缓存结构与填充（`driver_functions`、`_collect_driver_functions`、`collect_infos`）。证据链接：`tools/collector/mmio.py`（dataclass 字段 `driver_functions`，以及 `_collect_driver_functions` 内 `self.driver_functions[func_name] = FunctionInfo(...)`）。
- `queries/collectors/mmio/info_driver_function_collector.ql`：驱动函数集合选择入口（`from DriverFunction f` 与 `select f.getName(), ...`）。证据链接：`queries/collectors/mmio/info_driver_function_collector.ql`。
- `queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql`：字段访问表达式收集入口（`expr.toString()`、`getEnclosingFunction()`、`expr.checkExprType()`）。证据链接：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql`。
- `queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql`：字段访问追踪表达式收集入口（`MMIOTracedExpr`、`expr.checkExprType()`）。证据链接：`queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql`。
- `models/query_results/mmio.py`：`MmioExprInfo`/`MmioFunctionContainsInfo` 数据结构（`name`/`expr_type`/`flag`）。证据链接：`models/query_results/mmio.py`。
- `tools/collector/driver.py`：调用关系采集与缓存（`driverto_functioncall_dict`、`_collect_driverto_functioncall`）。证据链接：`tools/collector/driver.py`。
- `queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql`：调用边字段选择（`DriverToCall`、`callee/target/enclosing`、`call.isDirectCall()`）。证据链接：`queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql`。
- `models/query_results/driver.py`：`DriverFunctionCallInfo` 字段定义（`callee_name`、`call_type`、位置字段）。证据链接：`models/query_results/driver.py`。
- `config/collector_infos.py`：查询文件路径配置（`driver_function_query_file`、`driverto_functioncall_query_file`、mmioinfo 查询变量）。证据链接：`config/collector_infos.py`。

-->
