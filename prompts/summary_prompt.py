summary_prompt_en = """Your current task is to summarize the preceding conversation and generate a final answer.
**IMPORTANT INSTRUCTIONS**: You must only summarize, you cannot call any tools, you cannot ask questions, and you cannot request more information.

Please summarize the following content:
1. What is the problem?
2. What was the analysis process?
3. What fixes were implemented?
4. What is the final conclusion?

Now begin summarizing:"""

# Fixer专用的结构化输出提示
fixer_summary_prompt_en = """Your current task is to generate a final answer in JSON format.

**ABSOLUTELY CRITICAL INSTRUCTIONS:**
1. You CANNOT call any tools
2. You CANNOT ask questions
3. You CANNOT request more information
4. You CANNOT output any text other than the JSON object
5. You CANNOT wrap the JSON in any code blocks or formatting

**JSON FORMAT REQUIREMENTS:**
You must output exactly this format:
{
  "function_name": "name_of_function",
  "replacement_code": "fixed_function_code",
  "reason": "explanation_of_the_fix"
}

**WARNING:** Any deviation from these instructions will cause a critical error.

Now output the JSON object:"""

summary_prompt_zh = """你现在的任务是总结前面的对话内容，生成最终答案。
**重要指令**：你只能进行总结，不能调用任何工具，不能提问，不能请求更多信息。

请总结以下内容：
1. 问题是什么？
2. 分析过程是怎样的？
3. 实施了哪些修复？
4. 最终结论是什么？

现在开始总结："""

# 用于指导模型生成FunctionClassifyResponse结构化输出的prompt
function_classify_final_prompt_en = """Based on the entire conversation history, please generate the final function classification result in the required JSON format. You must strictly follow the format requirements and ensure all required fields are present.

Required fields:
- function_name: The name of the function being analyzed
- function_type: One of the following options: RECV, IRQ, RETURNOK, SKIP, NEEDCHECK, NODRIVER, INIT
- functionality: A description of the main functionality of the function
- classification_reason: Explanation of why the function was classified as this type
- has_replacement: Whether the function has a replacement implementation
- function_replacement: The replacement code if has_replacement is true, otherwise an empty string

**IMPORTANT**: You must output only the JSON object, no other text!"""

function_classify_final_prompt_zh = """根据整个对话历史，请按照要求的JSON格式生成最终的函数分类结果。你必须严格遵循格式要求，确保所有必填字段都存在。

必填字段：
- function_name: 被分析的函数名称
- function_type: 以下选项之一：RECV, IRQ, RETURNOK, SKIP, NEEDCHECK, NODRIVER, INIT
- functionality: 函数主要功能的描述
- classification_reason: 解释为什么将该函数分类为这种类型
- has_replacement: 函数是否有替换实现
- function_replacement: 如果has_replacement为true，则为替换代码，否则为空字符串

**重要**：你必须只输出JSON对象，不要其他任何文本！"""

# FailCheck专用的分析提示
failcheck_analyze_prompt_en = """Your task is to analyze a failed agent conversation that exceeded maximum iterations and provide a detailed summary.

**CONTEXT:**
The conversation between an AI agent and its tools has been terminated due to exceeding the maximum iteration limit (typically 50 rounds). Your job is to analyze the entire conversation history and provide a structured analysis.

**ANALYSIS REQUIREMENTS:**
1. **Segment Summary**: Divide the conversation into logical segments and describe what happened in each segment (e.g., "From message 1-10: Initial problem analysis", "From message 11-25: Attempting to fix function X").
2. **Key Actions**: Identify the main tools used, commands executed, and decisions made in each segment.
3. **Failure Analysis**: Explain why the conversation exceeded the maximum iteration limit. Common reasons include:
   - The agent was stuck in a loop of repeated actions
   - The agent failed to make progress towards the goal
   - The agent couldn't resolve a specific issue
   - The agent kept requesting the same information or tools
4. **Root Cause**: Try to identify the underlying root cause of the failure.
5. **Recommendations**: Provide suggestions for how to improve the process to avoid similar failures in the future.

**FORMAT REQUIREMENTS:**
- Start with a clear title: "FAILCHECK ANALYSIS REPORT"
- Use clear section headings for each part of your analysis
- Be detailed but concise
- Focus on facts from the conversation history
- Avoid speculation unless you explicitly indicate it's a hypothesis

**CONVERSATION HISTORY:**
{conversation_history}

Now begin your analysis:"""

failcheck_analyze_prompt_zh = """你的任务是分析一个因超过最大迭代次数而失败的代理对话，并提供详细的总结。

**背景：**
AI代理与其工具之间的对话因超过最大迭代限制（通常为50轮）而终止。你的工作是分析整个对话历史并提供结构化分析。

**分析要求：**
1. **分段总结**：将对话分成逻辑段，并描述每个段中发生的事情（例如："从消息1-10：初始问题分析"，"从消息11-25：尝试修复函数X"）。
2. **关键动作**：识别每个段中使用的主要工具、执行的命令和做出的决策。
3. **失败分析**：解释为什么对话超过了最大迭代限制。常见原因包括：
   - 代理陷入了重复动作的循环
   - 代理未能朝着目标取得进展
   - 代理无法解决特定问题
   - 代理不断请求相同的信息或工具
4. **根本原因**：尝试找出失败的根本原因。
5. **建议**：提供关于如何改进流程以避免将来类似失败的建议。

**格式要求：**
- 以清晰的标题开始："FAILCHECK分析报告"
- 为分析的每个部分使用清晰的节标题
- 详细但简洁
- 关注对话历史中的事实
- 避免猜测，除非你明确表示这是一个假设

**对话历史：**
{conversation_history}

现在开始你的分析："""
