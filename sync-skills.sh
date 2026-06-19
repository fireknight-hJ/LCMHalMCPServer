#!/bin/bash
# Skills同步脚本 - 在.opencode和Cursor全局skills之间同步

set -e  # 遇到错误时退出

# 定义目录
OPENCODE_DIR=".opencode/skills"
CURSOR_DIR="$HOME/.cursor/skills-cursor"

# 颜色输出
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Skills同步脚本 ===${NC}"
echo "源目录: $OPENCODE_DIR"
echo "目标目录: $CURSOR_DIR"
echo

# 检查源目录是否存在
if [ ! -d "$OPENCODE_DIR" ]; then
    echo -e "${RED}错误: 源目录 $OPENCODE_DIR 不存在${NC}"
    exit 1
fi

# 创建目标目录（如果不存在）
mkdir -p "$CURSOR_DIR"

echo -e "${GREEN}开始同步...${NC}"

# 同步所有skill目录
synced_count=0
for skill_dir in $(find "$OPENCODE_DIR" -maxdepth 1 -type d ! -path "$OPENCODE_DIR"); do
    skill_name=$(basename "$skill_dir")
    
    # 跳过非skill目录（如node_modules）
    if [[ "$skill_name" == "node_modules" ]] || [[ "$skill_name" == ".*" ]]; then
        continue
    fi
    
    # 转换命名规范：snake_case -> kebab-case
    cursor_skill_name=$(echo "$skill_name" | sed 's/_/-/g')
    
    echo -e "${BLUE}同步: $skill_name -> $cursor_skill_name${NC}"
    
    if [ -f "$skill_dir/SKILL.md" ]; then
        # 创建目标目录并复制文件
        mkdir -p "$CURSOR_DIR/$cursor_skill_name"
        cp "$skill_dir/SKILL.md" "$CURSOR_DIR/$cursor_skill_name/"
        ((synced_count++))
        echo -e "  ${GREEN}✓${NC} 已同步: $skill_name"
    else
        echo -e "  ${RED}✗${NC} 跳过: $skill_name (缺少SKILL.md文件)"
    fi
done

# 处理单独的markdown文件（以.md结尾的文件）
for md_file in $(find "$OPENCODE_DIR" -maxdepth 1 -name "*.md" -type f); do
    filename=$(basename "$md_file" .md)
    
    # 跳过已经处理过的文件
    if [[ -d "$OPENCODE_DIR/$filename" ]]; then
        continue
    fi
    
    # 转换命名规范
    cursor_skill_name=$(echo "$filename" | sed 's/_/-/g')
    
    echo -e "${BLUE}同步: $filename.md -> $cursor_skill_name${NC}"
    
    # 创建目标目录并转换格式
    mkdir -p "$CURSOR_DIR/$cursor_skill_name"
    
    # 创建标准的SKILL.md格式
    cat > "$CURSOR_DIR/$cursor_skill_name/SKILL.md" << EOF
---
name: $filename
description: $(head -n 5 "$md_file" | grep -v '^#' | head -n 1 | sed 's/^ *//;s/ *$//')
---

EOF
    
    # 追加原文件内容（跳过标题行）
    tail -n +2 "$md_file" >> "$CURSOR_DIR/$cursor_skill_name/SKILL.md"
    ((synced_count++))
    echo -e "  ${GREEN}✓${NC} 已同步: $filename.md"
done

echo
echo -e "${GREEN}=== 同步完成！===${NC}"
echo "同步了 $synced_count 个skills"
echo

# 显示同步后的skills列表
echo -e "${BLUE}当前skills列表:${NC}"
ls -1 "$CURSOR_DIR" | grep -v "^d" | sed 's/^/  - /'

echo
echo -e "${BLUE}提示:${NC}"
echo "- 可以运行 'git status' 查看.opencode目录的更改"
echo "- 记得提交.opencode目录的更改到版本控制"
echo "- 如果需要反向同步（Cursor -> .opencode），请手动复制"