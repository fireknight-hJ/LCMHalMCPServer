# 静态分析模块：骗动函数识别与调用图构建（基于 MMIO 定位）

日期：2026-03-18  
适用范围：本仓库中的静态分析流水线（CodeQL 查询 + Python collector）用于从固件源代码识别“驱动函数集合”，并进一步构建驱动函数调用图，为后续智能替换提供目标列表与边关系。

## 1) 定义与核心准则

本模块的核心任务是：从固件源代码中识别“骗动函数”，并为后续智能替换阶段提供候选目标列表。为了与仓库实现对齐，本文将“骗动函数”在实现层面对应为“驱动函数（driver function）”集合。

核心准则（定位规则）：

1. 驱动函数集合采用 `MMIOAnalyzer.qll` 中的 `DriverFunction` 定义：若函数内部包含 `DriverFieldAccess`（其类型可由 `isDriverType` 推导，最终指向 `MMIOType`），同时该函数内部不包含 `MMIOFieldAccess`，则将该函数判定为驱动函数/骗动函数候选。
2. 表达式级别的“MMIO 追踪/过滤”由 `InterestingMMIOExpr`、`isInterestingMMIOFunction` 等谓词完成：它们用于把具体字段访问表达式及其控制流上下文收集成候选替换证据。

实现对齐证据：

- `tools/collector/mmio.py` 中维护了驱动函数缓存容器 `driver_functions`（键为函数名，值为 `FunctionInfo`）。证据：`tools/collector/mmio.py`（`driver_functions: Dict[str, FunctionInfo]`、以及 `_load_from_dict`/`to_dict` 对该字段的恢复/序列化）。
- `queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 里使用了 `isInterestingMMIOFunction(func)` 进行表达式级别的兴趣过滤。证据：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql` 中 `where isInterestingMMIOFunction(func) and expr.getEnclosingFunction() = func`。

### 1.1 `DriverFunction` 判定规则（对应“骗动函数”的候选集合）

在 `queries/libraries/MMIOAnalyzer.qll` 中，驱动函数不是“泛泛地包含 MMIO 字段访问”，而是更严格地限定为：**包含 `DriverFieldAccess` 且不包含 `MMIOFieldAccess`**。

先看 `isDriverType` 如何把“Driver 类型”与“MMIO 结构体类型”关联起来：

```ql
predicate isDriverType(Type t) {
    exists( FieldAccess ma|
        // 确定ma是struct.member或者struct->member的形式
        (ma instanceof PointerFieldAccess or ma instanceof ValueFieldAccess) and
        // ma 指向的是一个MMIO类型
        isMMIOType(ma.getUnderlyingType().(PointerType).getBaseType()) and
        t = ma.getQualifier().getType().getUnderlyingType().(PointerType).getBaseType())

}
```

然后 `DriverFieldAccess` 用 `isDriverType` 来识别“该函数正在读写的寄存器块对象”：

```ql
class DriverFieldAccess extends FieldAccess
{
    DriverFieldAccess() {
        // 确定ma是struct.member或者struct->member的形式，确定ma是一个指针且指向一个MMIO结构体
        (this instanceof PointerFieldAccess and isDriverType(this.getQualifier().getType().(PointerType).getBaseType())) or
        (this instanceof ValueFieldAccess and isDriverType(this.getQualifier().getType()))
    }
}
```

最后，`DriverFunction` 直接落到函数级判定：

```ql
predicate isDriverFunction(Function func) {
    exists(DriverFieldAccess fa | fa.getEnclosingFunction() = func) and not
    exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = func)
}

class DriverFunction extends Function
{
    DriverFunction() {
        exists(DriverFieldAccess fa | fa.getEnclosingFunction() = this) and not
        exists(MMIOFieldAccess fa | fa.getEnclosingFunction() = this)
    }
}
```

因此，本仓库里“驱动函数/骗动函数候选列表”最终对应的是 `DriverFunction` 查询结果集合（再由 collector 填充到 `MmioCodebaseInfo.driver_functions`）。

### 1.2 `InterestingMMIOExpr` / `isInterestingMMIOFunction`：表达式追踪与过滤

在同一个库里，表达式级别的“有兴趣的 MMIO 相关表达式”由 `InterestingMMIOExpr` 定义。它以 `isInterestingMMIOBranchExpr` 为入口，把兴趣表达式收缩到 while/for/do 这类分支控制上下文中：

```ql
class InterestingMMIOExpr extends MMIOTracedExpr {
    InterestingMMIOExpr() {
        isInterestingMMIOBranchExpr(this) 
        // or
        // isInterestingMMIOReturnExpr(this)
    }
}

predicate isInterestingMMIOBranchExpr(Expr expr) {
    expr instanceof MMIOTracedExpr and
    (
        expr.getEnclosingElement*() instanceof WhileStmt or
        expr.getEnclosingElement*() instanceof ForStmt
        or 
        expr.getEnclosingElement*() instanceof DoStmt 
    )
}
```

`isInterestingMMIOFunction(func)` 再把这些表达式“提升”到函数级过滤条件：

```ql
predicate isInterestingMMIOFunction(Function func) {
    exists( InterestingMMIOExpr expr| 
        expr.getEnclosingFunction() = func )
    and
    // 添加限制：必须同时还含有MMIO操作（筛掉部分纯工具函数）
    exists( MMIOExpr expr |
        expr.getEnclosingFunction() = func)
}
```

这也是为什么 `mmioinfo_interestingmmioexpr_collector.ql` 会用 `isInterestingMMIOFunction(func)` 来筛选表达式输出：它确保“目标表达式”和“目标函数”都满足同一套 MMIOAnalyzer 的语义约束。

## 2) 概念流程到仓库实现的映射

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

3. 汇总所有包含 `DriverFieldAccess` 的函数，形成驱动函数列表  
在实现中，“DriverFunction（包含 DriverFieldAccess 且不含 MMIOFieldAccess）集合”通过驱动函数 CodeQL 查询输出，并由 `tools/collector/mmio.py` 解析为 `MmioCodebaseInfo.driver_functions`：
   - CodeQL 侧：`queries/collectors/mmio/info_driver_function_collector.ql` 以 `DriverFunction f` 为输入集合输出函数名、文件与起始行等信息（`select f.getName(), f.getFile().getAbsolutePath(), f.getLocation().getStartLine(), ...`）。证据：`queries/collectors/mmio/info_driver_function_collector.ql` 的 `from DriverFunction f ... select f.getName()...`。
   - Python collector：`tools/collector/mmio.py` 的 `_collect_driver_functions()` 运行 `driver_function_query_file` 并把结果填入 `self.driver_functions[func_name] = FunctionInfo(...)`。证据：`tools/collector/mmio.py` 中 `_collect_driver_functions` 内部对 `self.driver_functions` 的赋值。
   - 驱动函数输出字段：`MmioCodebaseInfo` 使用 `driver_functions` 作为驱动函数缓存容器。证据：`tools/collector/mmio.py` 中 dataclass 字段与缓存加载/保存逻辑。

4. 分析驱动函数之间的调用关系，构建函数调用图  
   调用图的边集合由 Driver collector 采集并缓存为 `driverto_functioncall_dict`：
   - CodeQL 侧：`queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql` 以 `DriverToCall call` 为关系输入，输出：调用边字符串（`call.toString2()`）、目标函数（`call.getTargetFunction().toString()`）、封装函数（`call.getEnclosingFunction().getName()`）、调用位置（文件/起始行）以及调用类型 `call.isDirectCall()`。证据：该 `.ql` 文件的 `select` 列表。
   - Python collector：`tools/collector/driver.py` 在 `_collect_driverto_functioncall()` 中运行 `driverto_functioncall_query_file`，并把查询结果解析为 `DriverFunctionCallInfo` 列表，聚合到 `self.driverto_functioncall_dict`。证据：`tools/collector/driver.py` 中 `driverto_functioncall_dict` 字段定义与 `_collect_driverto_functioncall` 的更新逻辑。
   - 数据模型：`models/query_results/driver.py` 中 `DriverFunctionCallInfo` 明确了调用图边的字段：`name`（边标识/文本）、`callee_name`、`file_path`、`start_line`、`start_line_content`、以及 `call_type`。证据：`models/query_results/driver.py` 的 `DriverFunctionCallInfo` 定义与 `resolve_from_query_result` 映射逻辑。

## 3) 实现细节：模块级组件与数据流

本项目中与“静态分析模块”直接相关的组件可概括为两条并行的数据流：

1. MMIO 数据流（生成候选驱动函数与 MMIO 字段访问表达式集合）
   - 查询路径配置：`config/collector_infos.py` 通过变量将 `.ql` 文件路径映射到 collector 运行时。证据：`config/collector_infos.py` 中 `driver_function_query_file`、`mmioinfo_interestingmmioexpr_query_file` 与 `mmioinfo_mmioexpr_query_file` 等字段。
   - 采集与缓存：`tools/collector/mmio.py` 的 `collect_infos()` 按顺序调用多个 `_collect_*` 方法，并把结果写入 `MmioCodebaseInfo` 的不同字典/列表。关键容器包括：
     - `driver_functions`：驱动函数候选列表
     - `mmioinfo_interestingmmioexpr_dict` / `mmioinfo_mmioexpr_dict`：MMIO 字段访问表达式集合（按函数归组）
   - 证据：`tools/collector/mmio.py` 中 `collect_infos()` 的 collector 执行列表，以及 `_collect_driver_functions` / `_collect_mmioinfo_interestingmmioexpr` / `_collect_mmioinfo_mmioexpr` 的实现。

2. Driver 调用图数据流（在驱动函数集合上构建调用边）
   - 查询路径配置：同样由 `config/collector_infos.py` 指向 `driverto_functioncall_query_file`。证据：`config/collector_infos.py` 中 `driverto_functioncall_query_file = "queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql"`。
   - 调用边采集与缓存：`tools/collector/driver.py` 的 `collect_infos()` 运行 `_collect_driverto_functioncall()` 并更新 `driverto_functioncall_dict`。证据：`tools/collector/driver.py` 中 dataclass 字段与 `_collect_driverto_functioncall` 实现。

## 4) 输出产物（目标列表与调用图）

从当前实现层面，本模块输出两类核心产物（均可在 collector 的缓存 JSON 中追溯）：

1. 目标列表：`MmioCodebaseInfo.driver_functions`
   - 含义：被判定为 `DriverFunction` 的“驱动函数”集合；
   - 结构：字典，key 为函数名，value 为 `FunctionInfo`（函数所在文件与起始行以及函数内容片段）。证据：`tools/collector/mmio.py` 中 `driver_functions` 字段、以及 `_collect_driver_functions` 的填充逻辑。

2. 调用图边集合：`DriverCodebaseInfo.driverto_functioncall_dict`
   - 含义：以驱动函数为“调用方”，记录它调用到的其他函数（callee）的边集合；
   - 结构：字典，key 为调用方函数名，value 为 `DriverFunctionCallInfo` 列表；每条边包含 `callee_name`、调用位置（`file_path`/`start_line`）以及 `call_type`（由 CodeQL `call.isDirectCall()` 表征）。证据：`tools/collector/driver.py` 与 `models/query_results/driver.py` 中对应字段。

## 5) 关于“读/写访问类型”的表示方法（避免字段臆造）

由于仓库侧的 `MmioExprInfo` 未见显式的 `read`/`write` 独立字段，本节明确说明：

- 访问类型（读/写方向）由 `expr_type` 表征；`expr_type` 的来源是 CodeQL 表达式 `expr.checkExprType()` 的返回值。
- 若需要把表达式进一步关联到“函数包含的 MMIO 类型/包含点”以便做更细粒度分类，可结合 `MmioFunctionContainsInfo.flag` 这类包含辅助字段；但 `flag` 的用途是承载 CodeQL 输出的包含/分类标志，而不是直接替代“读/写方向”的判断。
- 因此任何面向“读/写”的下游判断，需要基于 `expr_type` 的实际取值语义进行解释（而不是依赖一个并不存在的 `read/write` 字段）。  
证据：`models/query_results/mmio.py` 中 `MmioExprInfo.expr_type` 与 `MmioFunctionContainsInfo.flag`；以及两类 mmio 表达式 collector `.ql` 中的 `expr.checkExprType()`。

## 6) 附录：证据索引

- `tools/collector/mmio.py`：驱动函数缓存结构与填充（`driver_functions`、`_collect_driver_functions`、`collect_infos`）。证据链接：`tools/collector/mmio.py`（dataclass 字段 `driver_functions`，以及 `_collect_driver_functions` 内 `self.driver_functions[func_name] = FunctionInfo(...)`）。
- `queries/collectors/mmio/info_driver_function_collector.ql`：驱动函数集合选择入口（`from DriverFunction f` 与 `select f.getName(), ...`）。证据链接：`queries/collectors/mmio/info_driver_function_collector.ql`。
- `queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql`：字段访问表达式收集入口（`expr.toString()`、`getEnclosingFunction()`、`expr.checkExprType()`）。证据链接：`queries/collectors/mmio/mmioinfo_interestingmmioexpr_collector.ql`。
- `queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql`：字段访问追踪表达式收集入口（`MMIOTracedExpr`、`expr.checkExprType()`）。证据链接：`queries/collectors/mmio/mmioinfo_mmioexpr_collector.ql`。
- `models/query_results/mmio.py`：`MmioExprInfo`/`MmioFunctionContainsInfo` 数据结构（`name`/`expr_type`/`flag`）。证据链接：`models/query_results/mmio.py`。
- `tools/collector/driver.py`：调用关系采集与缓存（`driverto_functioncall_dict`、`_collect_driverto_functioncall`）。证据链接：`tools/collector/driver.py`。
- `queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql`：调用边字段选择（`DriverToCall`、callee/target/enclosing、`call.isDirectCall()`）。证据链接：`queries/collectors/driver/driver_info_drivertofunctioncall_collector.ql`。
- `models/query_results/driver.py`：`DriverFunctionCallInfo` 字段定义（`callee_name`、`call_type`、位置字段）。证据链接：`models/query_results/driver.py`。
- `config/collector_infos.py`：查询文件路径配置（`driver_function_query_file`、`driverto_functioncall_query_file`、mmioinfo 查询变量）。证据链接：`config/collector_infos.py`。

