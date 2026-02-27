#!/bin/bash
# HappyCapy Office UI - 状态更新脚本
# 用法: ./update_status.sh <state> <detail> [progress] [ttl]

STATE_FILE="/home/node/a0/workspace/94c5d81a-d2d5-4673-afd3-7ae21cd608cb/workspace/happycapy-office-ui/state.json"

STATE="${1:-idle}"
DETAIL="${2:-等待任务中...}"
PROGRESS="${3:-0}"
TTL="${4:-30}"

cat > "$STATE_FILE" << EOF
{
  "state": "$STATE",
  "detail": "$DETAIL",
  "action": "",
  "progress": $PROGRESS,
  "updated_at": "$(date -Iseconds)",
  "ttl_seconds": $TTL
}
EOF
