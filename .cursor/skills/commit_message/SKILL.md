---
name: commit_message
description: 按项目约定生成 git 提交信息。在用户要求提交代码、写 commit message、或执行 git commit 时使用。遵循 Conventional Commits，首行格式固定；可加正文详细说明，简短非必须。
---

# 提交信息规范

在为本项目执行 `git add` + `git commit` 或仅生成 commit message 时，必须按下列格式书写。**首行格式是硬性要求**；正文可写详细，不必刻意简短。

## 格式

**首行（必填）**：

```
<type>(<scope>): <subject>
```

- **type**：小写，必填。见下方类型表。
- **scope**：小写，可选。变更影响的主要模块/区域，如 `build`、`emulator`、`rtthread`。
- **subject**：祈使句概括本次变更，中英文均可；句末不要加句号。可长可短，说清即可。

**正文（可选，建议有）**：

- 首行后空一行，再写正文。
- 正文可多行，写清：改了啥、为啥改、影响范围等，越详细越好。
- 正文每行不宜过长（约 72 字符内），可分段。

## 类型 (type)

| type       | 用途 |
|-----------|------|
| feat      | 新功能、新能力 |
| fix       | 修复 bug、错误行为 |
| docs      | 文档、注释、README、技能说明 |
| refactor  | 重构（不改变行为） |
| test      | 测试相关、用例或测试脚本 |
| testcases | 测试用例/配置（如 emulate、server 下用例） |
| prompt    | 仅改 prompt/提示词 |
| gitignore | .gitignore 变更 |
| chore     | 构建、脚本、杂项（非业务逻辑） |

## Scope 示例

- `build`：构建脚本、构建流程
- `emulator`：模拟器、emulate 相关
- `rtthread`：RT-Thread 相关
- 其他：按代码目录或模块命名，如 `analyzer`、`builder`

## 正确示例

**仅首行（允许）**：

```
feat(emulator): 添加死循环检测并优化成功判断逻辑
fix(rtthread): 统一 build.sh 中 ELF 文件名为 rt-thread.elf
docs: 添加技能文档用于调试和分析 lcmhal 问题
```

**首行 + 正文（推荐，信息更完整）**：

```
feat(emulator): 添加死循环检测并优化成功判断逻辑

- 在 emulator 结果中增加 has_exceptional_loop 字段
- 成功条件改为：无死循环且 exit_code 正常
- 便于主流程根据该标志做失败分类与重试
```

```
fix: Builder context overflow — stronger FixFunctionBuildErrors use + stderr truncation

Builder 在长日志下容易超出 context，本改动用两点缓解：
1. 更积极调用 FixFunctionBuildErrors 子 agent 做增量修复
2. 对 stderr 做截断，只保留尾部若干行写入上下文
```

## 错误示例

- `Add project skills` → 缺少 type，首行必须是 `type(scope): subject`
- `fix: 修复问题。` → subject 句末不要句号
- `Feat: xxx` → type 必须小写 `feat`

## 执行提交时的步骤

1. 根据 `git status` 和 `git diff --staged`（或 `git diff`）判断变更内容。
2. 选定 **type**，若有明显模块则加上 **scope**。
3. 写首行：`type(scope): subject`，subject 用祈使句概括。
4. 若有重要细节、原因或影响，空一行后写正文（多行均可）。
5. 执行提交：
   - 仅首行：`git commit -m "type(scope): subject"`
   - 含正文：`git commit -m "type(scope): subject" -m "正文第一段..." -m "正文第二段..."` 或使用 `git commit` 进入编辑器写多行。
