# 自动化编译执行与动态修复系统核心代码与流程

## 一、核心代码片段

### 1. Builder Agent核心代码

```python
# Agent状态定义
class AgentState(MessagesState):
    final_response: BuildOutput
    function_name: str

# 图构建核心逻辑
async def build_graph():
    global _graph
    if _graph is not None:
        return _graph
    
    tools = await client.get_tools()
    await init_builder()
    tools = tools + [
        build_project,
        get_replace_func_details_by_file,
        update_function_replacement,
        get_function_analysis_and_replacement
    ]
    
    model_with_tools = model.bind_tools(tools)
    model_with_structured_output = model.with_structured_output(BuildOutput)
    tool_node = ToolNode(tools)
    
    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tools_with_logging)
    
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", should_continue)
    builder.add_edge("tools", "agent")
    builder.add_edge("respond", END)
    
    _graph = builder.compile()
    return _graph

# 条件路由判断
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    else:
        return "respond"
```

### 2. Emulator Runner Agent核心代码

```python
# Agent状态定义
class AgentState(MessagesState):
    final_response: EmulateResult
    function_name: str

# 图构建核心逻辑
async def build_graph():
    global _graph
    if _graph is not None:
        return _graph
    
    tools = await client.get_tools()
    tools.append(builder_agent)
    tools.append(fixer_agent)
    
    model_with_tools = model.bind_tools(tools)
    model_with_structured_output = model.with_structured_output(EmulateResult)
    tool_node = ToolNode(tools)
    
    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tools_with_logging)
    
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", should_continue)
    builder.add_edge("tools", "agent")
    builder.add_edge("respond", END)
    
    _graph = builder.compile()
    return _graph

# 状态持久化
def should_continue(state: AgentState):
    global _overwrite
    dump_message_raw_log("emulator_state", json.dumps(dump_message_state(state)), overwrite=_overwrite)
    if _overwrite == False:
        _overwrite = True
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    else:
        return "respond"
```

### 3. Fixer Agent核心代码

```python
# Agent状态定义
class AgentState(MessagesState):
    final_response: ReplacementUpdate
    function_name: str

# 图构建核心逻辑
async def build_graph():
    global _graph
    if _graph is not None:
        return _graph
    
    await init_builder()
    tools = await client.get_tools()
    tools = tools + [
        mmio_function_emulate_info,
        function_calls_emulate_info,
        get_replace_function_details_by_file,
        update_function_replacement,
        get_function_analysis_and_replacement
    ]
    
    model_with_tools = model.bind_tools(tools)
    model_with_structured_output = model.with_structured_output(ReplacementUpdate)
    tool_node = ToolNode(tools)
    
    builder = StateGraph(AgentState)
    builder.add_node("agent", call_model)
    builder.add_node("respond", respond)
    builder.add_node("tools", tools_with_logging)
    
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", should_continue)
    builder.add_edge("tools", "agent")
    builder.add_edge("respond", END)
    
    _graph = builder.compile()
    return _graph

# 结果汇总节点（带重试机制）
def respond(state: AgentState):
    max_retries = 5
    retry_count = 0
    response = None
    
    while retry_count < max_retries and response is None:
        try:
            response = model_with_structured_output.invoke(
                state["messages"] + [HumanMessage(content=SUMMARY_PROMPT)]
            )
            result = {"final_response": response}
        except Exception as e:
            retry_count += 1
            print(f"[ERROR] Failed to generate structured response (attempt {retry_count}/{max_retries}): {e}")
    
    if response is None:
        result = {"final_response": ReplacementUpdate(
            function_name=function_name,
            replacement_code="",
            reason="Failed to generate replacement code after multiple attempts"
        )}
    
    return result
```

### 4. 工具函数核心代码

```python
# 模拟器工具
@tool("EmulateProject", description="Run emulator and return emulate result")
def emulate_proj() -> dict:
    return core_emulate_proj()

@tool("GetMMIOFunctionEmulateInfo", description="Get MMIO function emulate info")
def mmio_function_emulate_info() -> str:
    return core_mmio_function_emulate_info()

@tool("GetFunctionCallsEmulateInfo", description="Get function calls stack info")
def function_calls_emulate_info() -> str:
    return core_function_calls_emulate_info()

# 编译工具
@tool("BuildProject", description="Build project and return build result")
def build_project() -> dict:
    return core_build_project()

@tool("UpdateFunctionReplacement", description="Update function replacement code")
def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    return core_update_functional_replacement(func_name, replace_code, reason)

@tool("GetFunctionAnalysisAndReplacement", description="Get function analysis and replacement")
def get_function_analysis_and_replacement(func_name: str) -> dict:
    return core_get_function_analysis_and_replacement(func_name)
```

## 二、工作流程框图

### 1. 整体工作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   Emulator Runner Agent (主控)                    │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   开始执行     │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  运行模拟器    │
                    │ EmulateProject  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  验证执行结果  │
                    └─────────────────┘
                              │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │  执行成功   │       │  执行失败   │
            └─────────────┘       └─────────────┘
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │   结束流程   │       │ 调用Fixer  │
            └─────────────┘       └─────────────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │ 分析错误日志   │
                                  │ 检索函数调用  │
                                  │ 检索MMIO调用  │
                                  └─────────────────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │ 生成修复代码   │
                                  │ UpdateFunction  │
                                  │ Replacement    │
                                  └─────────────────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │ 调用Builder  │
                                  └─────────────────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │  编译项目     │
                                  │ BuildProject   │
                                  └─────────────────┘
                                            │
                                            ▼
                                  ┌─────────────────┐
                                  │  验证编译结果  │
                                  └─────────────────┘
                                            │
                                  ┌───────────┴───────────┐
                                  │                       │
                                  ▼                       ▼
                          ┌─────────────┐       ┌─────────────┐
                          │  编译成功   │       │  编译失败   │
                          └─────────────┘       └─────────────┘
                                  │                       │
                                  ▼                       ▼
                          ┌─────────────┐       ┌─────────────┐
                          │  重新运行    │       │  重新修复    │
                          │  模拟器     │       │  编译错误    │
                          └─────────────┘       └─────────────┘
                                  │                       │
                                  └───────────┬───────────┘
                                              │
                                              ▼
                                    （回到运行模拟器步骤）
```

### 2. Builder Agent工作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Builder Agent 工作流程                         │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  接收编译请求  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  执行编译命令  │
                    │ BuildProject   │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  捕获编译输出  │
                    │  (stdout/stderr)│
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  解析编译结果  │
                    └─────────────────┘
                              │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │ exit_code=0 │       │ exit_code≠0 │
            │  编译成功   │       │  编译失败   │
            └─────────────┘       └─────────────┘
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │ 返回成功状态 │       │ 返回错误信息 │
            │ BuildOutput  │       │ 包含错误详情  │
            └─────────────┘       └─────────────┘
```

### 3. Fixer Agent工作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Fixer Agent 工作流程                          │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  接收修复请求  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  检索模拟器日志│
                    │ (Step 1)     │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │function_calls_ │
                    │emulate_info()  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │mmio_function_  │
                    │emulate_info()   │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  分析错误日志  │
                    │ (Step 2)     │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  识别问题函数  │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  检查现有分析  │
                    │ (Step 3)     │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │GetFunctionAnalysis│
                    │AndReplacement() │
                    └─────────────────┘
                              │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │ 已有替换   │       │ 无现有工作   │
            └─────────────┘       └─────────────┘
                    │                       │
                    ▼                       ▼
            ┌─────────────┐       ┌─────────────┐
            │ 审查替换   │       │ 进行新分析   │
            └─────────────┘       └─────────────┘
                    │                       │
                    └───────────┬───────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  生成修复代码  │
                    │ (Step 4)     │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │UpdateFunction  │
                    │Replacement()   │
                    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  返回修复结果  │
                    │ReplacementUpdate│
                    └─────────────────┘
```

### 4. 智能体协作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  智能体协作时序图                            │
└─────────────────────────────────────────────────────────────────────────┘

Emulator Runner          Fixer Agent           Builder Agent
      │                      │                      │
      │                      │                      │
      ├─ EmulateProject ───>│                      │
      │◄─ EmulateResult ────┤                      │
      │                      │                      │
      │◄─ (执行失败) ─────┤                      │
      │                      │                      │
      ├─ (调用Fixer) ─────>│                      │
      │                      │                      │
      │                      ├─ function_calls_      │
      │                      │   emulate_info() ───>│
      │                      │◄─ (函数调用日志) ──┤
      │                      │                      │
      │                      ├─ mmio_function_     │
      │                      │   emulate_info() ───>│
      │                      │◄─ (MMIO调用日志) ──┤
      │                      │                      │
      │                      ├─ GetFunctionAnalysis  │
      │                      │   AndReplacement() ─>│
      │                      │◄─ (函数分析结果) ─┤
      │                      │                      │
      │                      ├─ UpdateFunction     │
      │                      │   Replacement() ───>│
      │◄─ ReplacementUpdate ──┤                      │
      │                      │                      │
      ├─ (调用Builder) ────┼──────────────────────>│
      │                      │                      │
      │                      │                      ├─ BuildProject()
      │                      │                      │
      │                      │◄─ BuildOutput ─────┤
      │◄─ BuildOutput ──────┤                      │
      │                      │                      │
      │◄─ (编译成功) ─────┤                      │
      │                      │                      │
      ├─ EmulateProject ───>│                      │
      │◄─ EmulateResult ────┤                      │
      │                      │                      │
      │◄─ (执行成功) ─────┤                      │
      │                      │                      │
      ▼                      ▼                      ▼
   (流程结束)             (任务完成)             (任务完成)
```

## 三、数据流图

### 1. 错误诊断数据流

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    错误诊断数据流                              │
└─────────────────────────────────────────────────────────────────────────┘

模拟器执行日志
      │
      ├─ 函数调用栈 (function.txt)
      │   ├─ 函数名称
      │   ├─ 调用顺序
      │   ├─ 调用深度
      │   └─ 错误上下文
      │
      ├─ MMIO函数调用 (lcmhal.txt)
      │   ├─ 访问的寄存器
      │   ├─ 操作类型 (读/写)
      │   ├─ 操作值
      │   └─ 执行结果
      │
      └─ 错误信息
          ├─ 错误类型
          ├─ 错误位置
          └─ 错误描述
              │
              ▼
    Fixer Agent分析
              │
              ├─ 解析函数调用栈
              │   ├─ 识别问题函数
              │   ├─ 追踪调用链
              │   └─ 定位错误位置
              │
              ├─ 解析MMIO调用
              │   ├─ 识别MMIO操作
              │   ├─ 分析操作模式
              │   └─ 关联问题函数
              │
              └─ 综合分析
                  ├─ 确定根本原因
                  ├─ 识别错误模式
                  └─ 形成修复策略
                      │
                      ▼
              生成修复代码
                      │
                      ├─ 函数名称
                      ├─ 替换代码
                      └─ 修复原因
                          │
                          ▼
                    Builder Agent编译
                          │
                          ├─ 应用修复代码
                          ├─ 执行编译
                          └─ 验证编译结果
                              │
                              ▼
                        模拟器验证
                              │
                              ├─ 加载新固件
                              ├─ 执行测试
                              └─ 验证修复效果
```

### 2. 状态转换图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    状态转换图                                  │
└─────────────────────────────────────────────────────────────────────────┘

      ┌─────────────┐
      │   IDLE     │  初始状态
      └─────────────┘
            │
            ▼
      ┌─────────────┐
      │  EMULATING  │  运行模拟器
      └─────────────┘
            │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
┌─────────────┐   ┌─────────────┐
│  SUCCESS    │   │  FAILED     │
│  执行成功    │   │  执行失败    │
└─────────────┘   └─────────────┘
      │                 │
      ▼                 ▼
   ┌─────────────┐   ┌─────────────┐
   │   DONE     │   │  DIAGNOSING  │
   │  流程结束    │   │  诊断错误    │
   └─────────────┘   └─────────────┘
                           │
                           ▼
                     ┌─────────────┐
                     │  FIXING     │
                     │  修复代码    │
                     └─────────────┘
                           │
                           ▼
                     ┌─────────────┐
                     │  BUILDING   │
                     │  编译项目    │
                     └─────────────┘
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
          ┌─────────────┐   ┌─────────────┐
          │  BUILD_OK   │   │  BUILD_FAIL  │
          │  编译成功    │   │  编译失败    │
          └─────────────┘   └─────────────┘
                  │                 │
                  ▼                 ▼
          ┌─────────────┐   ┌─────────────┐
          │  EMULATING  │   │  REPAIRING  │
          │  重新运行    │   │  重新修复    │
          └─────────────┘   └─────────────┘
                  │                 │
                  └────────┬────────┘
                           │
                           ▼
                     (回到EMULATING状态)
```

## 四、关键交互流程

### 1. 验证标准检查

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  验证标准检查流程                              │
└─────────────────────────────────────────────────────────────────────────┘

模拟器执行完成
      │
      ▼
┌─────────────────────────┐
│ 检查1: 死循环检测  │
│ - 监控执行时间      │
│ - 检测循环状态      │
│ - 超时判定          │
└─────────────────────────┘
      │
      ├─ 未超时 ──> PASS
      │
      └─ 超时 ──> FAIL
            │
            ▼
┌─────────────────────────┐
│ 检查2: 异常检测    │
│ - 检测内存访问错误    │
│ - 检测总线错误        │
│ - 检测段错误          │
└─────────────────────────┘
      │
      ├─ 无异常 ──> PASS
      │
      └─ 有异常 ──> FAIL
            │
            ▼
┌─────────────────────────┐
│ 检查3: main函数检测 │
│ - 检测程序入口      │
│ - 验证执行路径      │
│ - 确认正常启动      │
└─────────────────────────┘
      │
      ├─ 到达main ──> PASS
      │
      └─ 未到达 ──> FAIL
            │
            ▼
      所有检查通过 ──> SUCCESS
```

### 2. 工具调用优先级

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  工具调用优先级                                │
└─────────────────────────────────────────────────────────────────────────┘

Fixer Agent工具调用顺序:

1. function_calls_emulate_info()  [必须首先调用]
   - 获取完整执行流程
   - 获取错误上下文
   - 优先级: 最高

2. mmio_function_emulate_info()  [必须第二个调用]
   - 获取MMIO函数信息
   - 识别硬件操作
   - 优先级: 高

3. GetFunctionAnalysisAndReplacement()  [对每个可疑函数调用]
   - 检查现有分析
   - 避免重复工作
   - 优先级: 中

4. UpdateFunctionReplacement()  [最后调用]
   - 应用修复代码
   - 更新数据库
   - 优先级: 低

调用规则:
- 必须按顺序调用1和2
- 3可以对多个函数调用
- 4在每个修复周期只调用一次
- 总调用数限制: 5-6次/会话
```
