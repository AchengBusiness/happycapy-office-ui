# HappyCapy Office Status - Claude Skill

实时显示 Claude AI 工作状态的虚拟办公室可视化。

## 安装

将此 skill 复制到 `~/.claude/skills/office-status/`

```bash
cp -r /path/to/happycapy-office-ui/skill ~/.claude/skills/office-status
```

## 使用

在 Claude 会话中使用 `/office` 命令启动。

## 状态更新

在工作过程中，使用以下命令更新状态：

```bash
# 基础命令
./update_status.sh <state> <detail> [progress] [ttl]

# 快捷命令（需要 source setup_claude_office.sh）
capy_writing "编写代码..."
capy_reading "阅读文档..."
capy_executing "运行测试..."
capy_idle "休息中"
```

## 状态类型

| 状态 | Capy位置 | 用途 |
|------|---------|------|
| idle, waiting | 休息区(沙发) | 空闲等待 |
| thinking, analyzing | 图书区 | 思考分析 |
| reading, searching | 图书区 | 阅读搜索 |
| writing, coding | 办公桌 | 编写代码 |
| debugging | 办公桌 | 调试修复 |
| executing, testing | 服务器 | 执行测试 |
| meeting | 会议室 | 开会讨论 |

## 自动集成

在 CLAUDE.md 中添加以下内容，让 Claude 自动更新状态：

```markdown
## 状态更新提醒

工作时请更新 HappyCapy Office 状态：
- 读取文件前: capy_reading "阅读 xxx..."
- 编写代码前: capy_writing "编写 xxx..."
- 执行命令前: capy_executing "运行 xxx..."
- 完成任务后: capy_idle "完成"
```
