#!/bin/bash
# HappyCapy Office - Auto Status Updater
# Usage: ./update_status.sh <tool_name> <description>

STATE_FILE="/home/node/a0/workspace/94c5d81a-d2d5-4673-afd3-7ae21cd608cb/workspace/happycapy-office-ui/state.json"
TOOL_NAME="${1:-unknown}"
DESCRIPTION="${2:-工作中...}"
TIMESTAMP=$(date -Iseconds)

# Map tool to state
case "$TOOL_NAME" in
    Read|Glob|Grep|WebFetch)
        STATE="researching"
        DETAIL="正在查阅: ${DESCRIPTION}"
        ;;
    Write|Edit|NotebookEdit)
        STATE="writing"
        DETAIL="正在编写: ${DESCRIPTION}"
        ;;
    Bash|Task)
        STATE="executing"
        DETAIL="正在执行: ${DESCRIPTION}"
        ;;
    *)
        STATE="writing"
        DETAIL="${DESCRIPTION}"
        ;;
esac

# Write state file
cat > "$STATE_FILE" << EOF
{
  "state": "${STATE}",
  "detail": "${DETAIL}",
  "action": "${TOOL_NAME}",
  "progress": 50,
  "updated_at": "${TIMESTAMP}",
  "ttl_seconds": 25
}
EOF

echo "Status updated: ${STATE} - ${DETAIL}"
