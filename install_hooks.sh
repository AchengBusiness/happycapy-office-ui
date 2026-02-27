#!/bin/bash
# HappyCapy Office UI - 自动状态更新 Hooks 安装脚本
# 运行此脚本后，Claude 的操作会自动映射到 Office UI 状态

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOKS_SCRIPT="$SCRIPT_DIR/hooks/status_hooks.sh"
SETTINGS_FILE="$HOME/.claude/settings.json"

echo "========================================"
echo "  HappyCapy Office UI - Hooks 安装"
echo "========================================"

# 确保 hooks 脚本存在且可执行
if [ ! -f "$HOOKS_SCRIPT" ]; then
    echo "[!] hooks/status_hooks.sh 不存在"
    exit 1
fi
chmod +x "$HOOKS_SCRIPT"

# 创建 settings.json 目录
mkdir -p "$(dirname "$SETTINGS_FILE")"

# 生成 hooks 配置
HOOKS_CONFIG=$(cat << EOF
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Read", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT read"}]},
      {"matcher": "Write", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT write"}]},
      {"matcher": "Edit", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT edit"}]},
      {"matcher": "Bash", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT bash"}]},
      {"matcher": "Grep", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT grep"}]},
      {"matcher": "Glob", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT glob"}]},
      {"matcher": "Task", "hooks": [{"type": "command", "command": "$HOOKS_SCRIPT task"}]}
    ]
  }
}
EOF
)

# 写入配置
echo "$HOOKS_CONFIG" > "$SETTINGS_FILE"

echo "[✓] Hooks 配置已写入: $SETTINGS_FILE"
echo ""
echo "状态映射:"
echo "  Read/Grep/Glob → 阅读/搜索 (图书区)"
echo "  Write/Edit     → 编写/编辑 (办公桌)"
echo "  Bash           → 执行命令 (服务器机房)"
echo "  Task           → 思考中   (图书区)"
echo ""
echo "现在 Claude 的操作会自动更新 Office UI 状态！"
echo ""
echo "提示: 先运行 ./install.sh 启动 Office UI"
echo "========================================"
