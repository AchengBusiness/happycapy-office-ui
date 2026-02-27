#!/bin/bash
# HappyCapy Office UI - 自动状态更新 Hooks
# 在 settings.json 中配置 hooks 调用此脚本

OFFICE_DIR="${OFFICE_DIR:-$(dirname "$(dirname "$(realpath "$0")")")}"
UPDATE_SCRIPT="$OFFICE_DIR/update_status.sh"

# 检查服务器是否运行
office_running() {
    lsof -i :18791 >/dev/null 2>&1
}

# 更新状态（仅当服务器运行时）
update_status() {
    if office_running && [ -x "$UPDATE_SCRIPT" ]; then
        "$UPDATE_SCRIPT" "$@" 2>/dev/null &
    fi
}

# 根据参数执行对应的状态更新
case "$1" in
    read|Read)
        update_status reading "阅读文件中..." 0 30
        ;;
    write|Write)
        update_status writing "编写文件中..." 0 30
        ;;
    edit|Edit)
        update_status editing "编辑代码中..." 0 30
        ;;
    bash|Bash)
        update_status executing "执行命令中..." 0 30
        ;;
    grep|Grep)
        update_status searching "搜索代码中..." 0 30
        ;;
    glob|Glob)
        update_status searching "查找文件中..." 0 30
        ;;
    task|Task)
        update_status thinking "思考中..." 0 60
        ;;
    idle)
        update_status idle "待命中..." 0 30
        ;;
    responding)
        update_status responding "回复用户中..." 0 30
        ;;
    *)
        # 默认：思考中
        update_status thinking "处理中..." 0 30
        ;;
esac
