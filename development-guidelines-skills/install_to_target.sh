#!/usr/bin/env bash
set -e

TARGET="/Users/cyan/个人工作/AI-skillS汇总/开发相关"
SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$TARGET"
rsync -av --exclude="install_to_target.sh" "$SOURCE_DIR/" "$TARGET/"

echo "已复制到：$TARGET"
echo "Skill 数量：$(find "$TARGET" -name 'SKILL.md' | wc -l | tr -d ' ')"
