# HappyCapy Office UI v2

3D 渲染风格虚拟办公室，实时可视化 AI 助手的工作状态。可爱的水豚角色会根据当前任务在不同区域移动。

![HappyCapy Office](frontend/office_bg.png)

## v2 新特性

相比 v1（像素风格），v2 完全重构：

| 特性 | v1 | v2 |
|------|----|----|
| 视觉风格 | 像素艺术 | 3D 渲染风格 |
| 区域数量 | 2 个 | 5 个功能区 |
| 状态数量 | 6 个 | 30+ 状态 |
| 行走动画 | 瞬间移动 | 3 秒平滑过渡 |
| 演示模式 | 无 | 一键演示 |
| 工作统计 | 无 | 实时统计面板 |
| 一键安装 | 无 | install.sh |

## 功能特性

- **3D 渲染风格办公室背景** - 精心绘制的等距视角办公室
- **5 个功能区域** - 办公桌、会议室、服务器机房、休息区、图书区
- **30+ 工作状态** - 细粒度的状态映射
- **平滑行走动画** - 3 秒过渡 + 走路动画效果
- **实时工作统计** - 各区域时间统计，数据持久化到 localStorage
- **演示模式** - 自动循环展示所有状态
- **幽默气泡文字** - 每个状态对应有趣的内心独白

## 状态区域映射

| 区域 | 状态列表 |
|------|----------|
| 休息区 (沙发) | idle, waiting, ready, error, stuck |
| 图书区 | thinking, analyzing, planning, researching, reading, learning, searching, confused |
| 办公桌 | writing, coding, editing, debugging, refactoring |
| 服务器机房 | executing, running, processing, building, testing, deploying |
| 会议室 | meeting, discussing, reviewing, collaborating, responding, explaining, presenting, chatting, answering |

## 快速开始

### 方式一：一键安装（推荐）

```bash
git clone https://github.com/AchengBusiness/happycapy-office-ui.git
cd happycapy-office-ui
./install.sh
```

安装脚本会：
1. 启动后端服务器
2. 导出预览端口
3. 配置状态更新命令

### 方式二：手动启动

```bash
# 1. 安装依赖
pip install flask

# 2. 启动后端
cd happycapy-office-ui/backend
python app.py

# 3. 访问 http://localhost:18791
```

## 状态更新

### 使用 update_status.sh

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

Office UI 可作为 Claude Code 技能使用：

```bash
# 安装技能
cp -r skill/* ~/.claude/skills/office-status-ui/

# 在 Claude 中启动
/office
```

## 目录结构

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

## API 端点

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

## 自动空闲机制

工作状态超过 TTL 时间未更新时，系统会自动将状态切换为 idle，水豚返回休息区。

## 自定义

### 修改区域位置

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

### 添加新状态

在 `STATE_CONFIG` 中添加：

```javascript
const STATE_CONFIG = {
    // ... 现有状态
    newstate: { area: 'desk', color: '#3498db', label: '新状态' },
};
```

### 修改气泡文字

编辑 `BUBBLE_TEXTS` 对象：

```javascript
const BUBBLE_TEXTS = {
    newstate: ['气泡文字1', '气泡文字2', '气泡文字3'],
};
```

## 历史版本

- **v1**: 像素风格办公室，2 个区域，6 个状态
- **v2**: 3D 渲染风格，5 个区域，30+ 状态，演示模式，工作统计

## License

MIT

---

**相关项目:**
- [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) - 原始灵感来源
- [Happycapy-skills](https://github.com/happycapy-ai/Happycapy-skills) - 更多 Claude 技能

**仓库:** https://github.com/AchengBusiness/happycapy-office-ui
