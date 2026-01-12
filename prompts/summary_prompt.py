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
