#!/bin/bash
#
# HappyCapy Office UI - 一键安装脚本
# 用法: bash install.sh
#
# 此脚本会:
#   1. 启动 Office UI 服务器
#   2. 导出预览端口
#   3. 初始化状态
#   4. 输出使用说明
#

set -e

echo ""
echo "╔════════════════════════════════════════════╗"
echo "║  HappyCapy Office UI - 一键安装            ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR/backend"
STATE_FILE="$SCRIPT_DIR/state.json"
PORT=18791

# 函数：更新状态
update_status() {
    cat > "$STATE_FILE" << EOF
{
  "state": "$1",
  "detail": "$2",
  "action": "",
  "progress": ${3:-0},
  "updated_at": "$(date -Iseconds)",
  "ttl_seconds": ${4:-30}
}
EOF
}

# 步骤 1: 检查并启动服务器
echo "[1/4] 检查服务器..."
if lsof -i :$PORT >/dev/null 2>&1; then
    echo "  ✓ 服务器已在运行 (端口 $PORT)"
else
    echo "  → 启动服务器..."
    cd "$BACKEND_DIR"
    python app.py > /tmp/capy_office.log 2>&1 &
    sleep 3
    
    if lsof -i :$PORT >/dev/null 2>&1; then
        echo "  ✓ 服务器启动成功"
    else
        echo "  ✗ 服务器启动失败"
        echo "  查看日志: cat /tmp/capy_office.log"
        exit 1
    fi
fi

# 步骤 2: 导出端口
echo ""
echo "[2/4] 导出预览端口..."
if [ -f "/app/export-port.sh" ]; then
    PREVIEW_URL=$(/app/export-port.sh $PORT 2>&1 | grep -o 'https://[^ ]*' | head -1)
    if [ -n "$PREVIEW_URL" ]; then
        echo "  ✓ 预览地址: $PREVIEW_URL"
    else
        echo "  → 端口已导出"
        PREVIEW_URL="https://$PORT-*-preview.happycapy.ai"
    fi
else
    echo "  → 跳过端口导出 (非沙盒环境)"
    PREVIEW_URL="http://localhost:$PORT"
fi

# 步骤 3: 初始化状态
echo ""
echo "[3/4] 初始化状态..."
update_status "idle" "Office UI 已启动！" 0 60
echo "  ✓ 状态已初始化"

# 步骤 4: 创建快捷命令
echo ""
echo "[4/4] 创建快捷命令..."
cat > /tmp/capy_commands.sh << 'CMDS'
# HappyCapy Office 快捷命令
CAPY_STATE_FILE="/home/node/a0/workspace/94c5d81a-d2d5-4673-afd3-7ae21cd608cb/workspace/happycapy-office-ui/state.json"

capy() {
    local state="${1:-idle}"
    local detail="${2:-等待中...}"
    local progress="${3:-0}"
    cat > "$CAPY_STATE_FILE" << EOF
{
  "state": "$state",
  "detail": "$detail",
  "action": "",
  "progress": $progress,
  "updated_at": "$(date -Iseconds)",
  "ttl_seconds": 30
}
EOF
}

# 快捷别名
alias capy.think='capy thinking'
alias capy.read='capy reading'
alias capy.search='capy searching'
alias capy.write='capy writing'
alias capy.code='capy coding'
alias capy.debug='capy debugging'
alias capy.run='capy executing'
alias capy.test='capy testing'
alias capy.meet='capy meeting'
alias capy.rest='capy idle'
CMDS
echo "  ✓ 快捷命令已创建"

# 完成
echo ""
echo "╔════════════════════════════════════════════╗"
echo "║  安装完成！                                 ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo "预览地址: $PREVIEW_URL"
echo ""
echo "使用方法:"
echo "  source /tmp/capy_commands.sh   # 加载快捷命令"
echo ""
echo "  capy writing \"编写代码...\"    # 更新状态"
echo "  capy reading \"阅读文档...\"    # 更新状态"
echo "  capy executing \"运行测试...\""
echo "  capy idle \"完成\""
echo ""
echo "或直接使用更新脚本:"
echo "  $SCRIPT_DIR/update_status.sh <state> <detail>"
echo ""
