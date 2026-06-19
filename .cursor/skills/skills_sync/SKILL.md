---
name: skills_sync
description: Skills同步机制 - 在.opencode和Cursor全局skills之间保持同步
---

# Skills同步机制

## 同步原则

1. **双向同步** - .opencode/skills/ 和 ~/.cursor/skills-cursor/ 应该保持内容一致
2. **修改即同步** - 任何一边的修改都应该及时同步到另一边
3. **版本控制** - 使用git进行版本管理，确保修改历史可追踪
4. **标准化命名** - 统一使用kebab-case命名规范

## 目录结构

### 源目录（项目特定）
```
.opencode/skills/
├── debug_lcmhal_failure/
│   └── SKILL.md
├── run_lcmhal_demo/
│   └── SKILL.md
├── prompt_editing.md
└── [新的skill目录]/
    └── SKILL.md
```

### 目标目录（Cursor全局）
```
~/.cursor/skills-cursor/
├── debug-lcmhal-failure/
│   └── SKILL.md
├── run-lcmhal-demo/
│   └── SKILL.md
├── prompt-editing/
│   └── SKILL.md
└── [新的skill目录]/
    └── SKILL.md
```

## 同步检查清单

### 添加新Skill时
- [ ] 在 `.opencode/skills/` 创建目录和 `SKILL.md` 文件
- [ ] 确保 `SKILL.md` 包含正确的YAML头部（name和description）
- [ ] 将目录名从snake_case转换为kebab-case
- [ ] 复制到 `~/.cursor/skills-cursor/` 对应目录
- [ ] 提交git更改到.opencode目录

### 修改现有Skill时
- [ ] 优先在 `.opencode/skills/` 中修改源文件
- [ ] 同步更新 `~/.cursor/skills-cursor/` 中的对应文件
- [ ] 检查是否需要更新其他引用该skill的代码
- [ ] 记录修改原因和版本更新说明

### 删除Skill时
- [ ] 确认skill不再被使用
- [ ] 删除 `.opencode/skills/` 中的源文件
- [ ] 删除 `~/.cursor/skills-cursor/` 中的对应文件
- [ ] 更新相关文档和引用

## 自动化同步脚本

可以创建以下脚本来简化同步过程：

```bash
#!/bin/bash
# skill-sync.sh - Skills同步脚本

OPENCODE_DIR=".opencode/skills"
CURSOR_DIR="~/.cursor/skills-cursor"

echo "开始Skills同步..."

# 同步所有skills
for skill_dir in $(ls -d ${OPENCODE_DIR}/*/ 2>/dev/null); do
    if [ -d "$skill_dir" ]; then
        skill_name=$(basename "$skill_dir")
        # 转换命名规范：snake_case -> kebab-case
        cursor_skill_name=$(echo "$skill_name" | sed 's/_/-/g')
        
        echo "同步: $skill_name -> $cursor_skill_name"
        
        # 创建目标目录并复制文件
        mkdir -p "${CURSOR_DIR}/${cursor_skill_name}"
        cp "${skill_dir}/SKILL.md" "${CURSOR_DIR}/${cursor_skill_name}/"
    fi
done

# 处理单独的markdown文件
if [ -f "${OPENCODE_DIR}/prompt_editing.md" ]; then
    echo "同步: prompt_editing.md -> prompt-editing"
    mkdir -p "${CURSOR_DIR}/prompt-editing"
    # 转换为标准SKILL.md格式
    cat > "${CURSOR_DIR}/prompt-editing/SKILL.md" << 'EOF'
---
name: prompt_editing
description: Prompt编辑原则和最佳实践
---

EOF
    cat "${OPENCODE_DIR}/prompt_editing.md" >> "${CURSOR_DIR}/prompt-editing/SKILL.md"
fi

echo "同步完成！"
```

## 质量检查

每次同步后应检查：

1. **格式验证**：确保所有SKILL.md文件都包含正确的YAML头部
2. **内容完整性**：确认内容没有丢失或损坏
3. **链接有效性**：检查是否有其他文件引用这些skills
4. **命名一致性**：确保命名规范统一

## 常见问题处理

### 1. 命名冲突
- 检查是否有同名但不同命名规范的目录
- 优先使用kebab-case作为标准命名

### 2. 内容格式错误
- 验证YAML头部格式是否正确
- 确保description字段简洁明了

### 3. 同步遗漏
- 定期检查两个目录的结构是否一致
- 使用版本控制追踪所有修改

## 最佳实践

1. **源优先原则**：始终将 `.opencode/skills/` 作为主要的skill管理位置
2. **及时同步**：修改后立即同步，避免累积大量未同步的更改
3. **版本注释**：在git提交中清晰地描述skill的修改内容
4. **定期审查**：定期检查skills的有效性和相关性，删除过时的skills