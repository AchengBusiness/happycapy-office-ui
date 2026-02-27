<div align="center">

# HappyCapy Office UI v2

**[English](#english) | [中文](#中文)**

<img src="frontend/office_bg.png" alt="HappyCapy Office" width="600">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)

</div>

---

<a name="english"></a>
## English

A 3D-style virtual office that visualizes AI assistant working status in real-time. A cute capybara character moves between different areas based on the current task.

### What's New in v2

| Feature | v1 | v2 |
|---------|----|----|
| Visual Style | Pixel Art | 3D Rendered |
| Areas | 2 | 5 functional zones |
| States | 6 | 30+ states |
| Animation | Instant teleport | 3s smooth transition |
| Demo Mode | No | One-click demo |
| Statistics | No | Real-time stats panel |
| Installation | Manual | One-click install |
| Auto Status | No | Hooks integration |

### Features

- **3D Rendered Office** - Beautiful isometric office background
- **5 Functional Areas** - Desk, Meeting Room, Server Room, Lounge, Library
- **30+ Work States** - Fine-grained status mapping
- **Smooth Walking Animation** - 3-second transition with walking effect
- **Real-time Statistics** - Track time in each area, persisted to localStorage
- **Demo Mode** - Auto-cycle through all states
- **Humorous Bubbles** - Fun inner monologues for each state

### Area Mapping

| Area | States |
|------|--------|
| Lounge (Sofa) | idle, waiting, ready, error, stuck |
| Library | thinking, analyzing, planning, researching, reading, learning, searching, confused |
| Desk | writing, coding, editing, debugging, refactoring |
| Server Room | executing, running, processing, building, testing, deploying |
| Meeting Room | meeting, discussing, reviewing, collaborating, responding, explaining, presenting, chatting, answering |

### Quick Start

#### Option 1: One-Click Install (Recommended)

```bash
git clone https://github.com/AchengBusiness/happycapy-office-ui.git
cd happycapy-office-ui
./install.sh
```

#### Option 2: Manual Setup

```bash
# 1. Install dependency
pip install flask

# 2. Start backend
cd happycapy-office-ui/backend
python app.py

# 3. Visit http://localhost:18791
```

### Update Status

```bash
./update_status.sh <state> <detail> [progress] [ttl]

# Examples
./update_status.sh reading "Reading code..." 20 30
./update_status.sh writing "Writing feature..." 50 60
./update_status.sh executing "Running tests..." 80 120
./update_status.sh idle "Done" 100 30
```

Parameters:
- `state`: State name (see mapping table)
- `detail`: Status description
- `progress`: Progress percentage (0-100)
- `ttl`: Timeout in seconds, auto-returns to idle

### Claude Code Integration

```bash
# Install as skill
cp -r skill/* ~/.claude/skills/office-status-ui/

# Launch in Claude
/office
```

### Auto Status Hooks (Optional)

Enable automatic status updates based on Claude's tool usage:

```bash
./install_hooks.sh
```

This maps Claude's tools to office areas:
| Tool | Status | Area |
|------|--------|------|
| Read | reading | Library |
| Grep/Glob | searching | Library |
| Write/Edit | writing/editing | Desk |
| Bash | executing | Server Room |
| Task | thinking | Library |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main UI |
| `/cad` | GET | CAD-style UI |
| `/status` | GET | Current status JSON |
| `/health` | GET | Health check |

### Project Structure

```
happycapy-office-ui/
├── backend/
│   └── app.py           # Flask backend
├── frontend/
│   ├── index.html       # Main UI (v2)
│   ├── index_cad.html   # CAD-style UI
│   └── office_bg.png    # 3D background
├── hooks/
│   └── status_hooks.sh  # Auto status update hooks
├── skill/               # Claude Code skill
├── update_status.sh     # Status update script
├── install.sh           # One-click installer
├── install_hooks.sh     # Hooks installer
└── state.json           # Runtime state
```

---

<a name="中文"></a>
## 中文

3D 渲染风格虚拟办公室，实时可视化 AI 助手的工作状态。可爱的水豚角色会根据当前任务在不同区域移动。

### v2 新特性

| 特性 | v1 | v2 |
|------|----|----|
| 视觉风格 | 像素艺术 | 3D 渲染风格 |
| 区域数量 | 2 个 | 5 个功能区 |
| 状态数量 | 6 个 | 30+ 状态 |
| 行走动画 | 瞬间移动 | 3 秒平滑过渡 |
| 演示模式 | 无 | 一键演示 |
| 工作统计 | 无 | 实时统计面板 |
| 一键安装 | 无 | install.sh |
| 自动状态 | 无 | Hooks 集成 |

### 功能特性

- **3D 渲染风格办公室背景** - 精心绘制的等距视角办公室
- **5 个功能区域** - 办公桌、会议室、服务器机房、休息区、图书区
- **30+ 工作状态** - 细粒度的状态映射
- **平滑行走动画** - 3 秒过渡 + 走路动画效果
- **实时工作统计** - 各区域时间统计，数据持久化到 localStorage
- **演示模式** - 自动循环展示所有状态
- **幽默气泡文字** - 每个状态对应有趣的内心独白

### 状态区域映射

| 区域 | 状态列表 |
|------|----------|
| 休息区 (沙发) | idle, waiting, ready, error, stuck |
| 图书区 | thinking, analyzing, planning, researching, reading, learning, searching, confused |
| 办公桌 | writing, coding, editing, debugging, refactoring |
| 服务器机房 | executing, running, processing, building, testing, deploying |
| 会议室 | meeting, discussing, reviewing, collaborating, responding, explaining, presenting, chatting, answering |

### 快速开始

#### 方式一：一键安装（推荐）

```bash
git clone https://github.com/AchengBusiness/happycapy-office-ui.git
cd happycapy-office-ui
./install.sh
```

安装脚本会：
1. 启动后端服务器
2. 导出预览端口
3. 配置状态更新命令

#### 方式二：手动启动

```bash
# 1. 安装依赖
pip install flask

# 2. 启动后端
cd happycapy-office-ui/backend
python app.py

# 3. 访问 http://localhost:18791
```

### 状态更新

```bash
./update_status.sh <state> <detail> [progress] [ttl]

# 示例
./update_status.sh reading "阅读代码..." 20 30
./update_status.sh writing "编写功能..." 50 60
./update_status.sh responding "回复用户..." 0 30
./update_status.sh executing "运行测试..." 80 120
./update_status.sh idle "完成" 100 30
```

参数说明：
- `state`: 状态名称（见上方映射表）
- `detail`: 状态描述文字
- `progress`: 进度百分比 (0-100)
- `ttl`: 超时秒数，超时后自动回到 idle

### Claude Code 集成

```bash
# 安装技能
cp -r skill/* ~/.claude/skills/office-status-ui/

# 在 Claude 中启动
/office
```

### API 端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | 主界面 |
| `/cad` | GET | CAD 风格界面 |
| `/status` | GET | 获取当前状态 JSON |
| `/health` | GET | 健康检查 |

### 状态 JSON 格式

```json
{
  "state": "writing",
  "detail": "编写功能代码...",
  "progress": 50,
  "updated_at": "2026-02-27T10:30:00+08:00",
  "ttl_seconds": 60
}
```

### 自动空闲机制

工作状态超过 TTL 时间未更新时，系统会自动将状态切换为 idle，水豚返回休息区。

### 自定义配置

<details>
<summary>修改区域位置</summary>

编辑 `frontend/index.html` 中的 `AREAS` 对象：

```javascript
const AREAS = {
    lounge:  { x: 72,  y: 68, name: '休息区' },
    library: { x: 24,  y: 32, name: '图书区' },
    desk:    { x: 25,  y: 75, name: '办公桌' },
    server:  { x: 75,  y: 28, name: '服务器' },
    meeting: { x: 60,  y: 60, name: '会议室' }
};
```
</details>

<details>
<summary>添加新状态</summary>

在 `STATE_CONFIG` 中添加：

```javascript
const STATE_CONFIG = {
    // ... 现有状态
    newstate: { area: 'desk', color: '#3498db', label: '新状态' },
};
```
</details>

<details>
<summary>修改气泡文字</summary>

编辑 `BUBBLE_TEXTS` 对象：

```javascript
const BUBBLE_TEXTS = {
    newstate: ['气泡文字1', '气泡文字2', '气泡文字3'],
};
```
</details>

### 目录结构

```
happycapy-office-ui/
├── backend/
│   └── app.py           # Flask 后端服务
├── frontend/
│   ├── index.html       # 主界面（v2）
│   ├── index_cad.html   # CAD 风格界面
│   └── office_bg.png    # 3D 渲染背景
├── skill/               # Claude Code 技能文件
├── update_status.sh     # 状态更新脚本
├── install.sh           # 一键安装脚本
└── state.json           # 运行时状态文件
```

---

## Version History

| Version | Description |
|---------|-------------|
| **v2** | 3D rendered style, 5 areas, 30+ states, demo mode, statistics |
| **v1** | Pixel art style, 2 areas, 6 states |

## License

MIT

---

<div align="center">

**Related Projects / 相关项目**

[Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) - Original Inspiration

[Happycapy-skills](https://github.com/happycapy-ai/Happycapy-skills) - More Claude Skills

---

**Repository:** https://github.com/AchengBusiness/happycapy-office-ui

Made with love by [AchengBusiness](https://github.com/AchengBusiness)

</div>
