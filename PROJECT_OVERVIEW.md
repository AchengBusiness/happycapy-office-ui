# HappyCapy Office UI - 项目概览

## 🎯 项目简介

这是一个基于 Phaser 游戏引擎和 Flask 后端的实时状态展示系统。通过可爱的像素风格水豚角色在豪华办公室中的移动，直观展示 AI 助手的工作状态。

## 🏗️ 技术架构

### 前端
- **游戏引擎**: Phaser 3.80.1
- **渲染方式**: Canvas 2D（像素艺术风格）
- **动画系统**:
  - 眨眼动画（2.5秒间隔）
  - 对话气泡（8秒间隔随机显示）
  - 打字机效果（50ms/字符）
  - 平滑移动（带摇摆效果）

### 后端
- **框架**: Flask（Python）
- **API端点**:
  - `GET /` - 主页面
  - `GET /status` - 状态查询（JSON）
  - `GET /health` - 健康检查

### 数据存储
- **格式**: JSON文件（`state.json`）
- **字段**:
  - `state`: 当前状态（idle/writing/researching/executing/syncing/error）
  - `detail`: 状态详细描述
  - `progress`: 进度（0-100）
  - `updated_at`: 最后更新时间
  - `ttl_seconds`: 自动空闲超时（默认25秒）

## 📐 办公室布局设计

### 区域坐标（800x600画布）

```javascript
areas = {
    workdesk: { x: 285, y: 350 },    // 左下 - 豪华办公桌
    breakroom: { x: 705, y: 495 },   // 右下 - L型休息沙发
    meeting: { x: 450, y: 220 },      // 中上 - 会议桌
    server: { x: 720, y: 230 },       // 右上 - 服务器机柜
}
```

### 视觉元素

#### 地面层
- 木地板纹理（3种棕色交替）
- 装饰地毯（椭圆形红色）

#### 家具层
1. **工作区**
   - 实木办公桌 (180-380, 280-420)
   - 显示器 + 键盘 + 鼠标
   - 咖啡杯
   - 豪华办公椅

2. **会议区**
   - 椭圆形会议桌 (350-550, 180-260)
   - 4把会议椅

3. **休息区**
   - L型沙发 (630-780, 460-570)
   - 玻璃茶几

4. **服务器区**
   - 2个专业机柜
   - LED状态指示灯（绿/橙/蓝）

#### 装饰层
- 3个大型落地窗（顶部）
- 玻璃隔断（左右两侧）
- 书架 + 彩色书籍
- 白板（带内容示意）
- 绿植：龙血树、小盆栽、吊兰
- 墙面时钟
- 文件柜

## 🔄 状态流转

```
┌─────────┐
│  idle   │ ◄──── 默认状态/超时后
└────┬────┘
     │
     ├──► writing ──────► breakroom区域
     ├──► researching ──► workdesk区域
     ├──► executing ────► workdesk区域
     ├──► syncing ──────► breakroom区域
     └──► error ────────► breakroom区域
```

## 🎨 角色设计

### 水豚（Capybara）
- **颜色**: 棕色（#A0826D）身体
- **尺寸**: 24x24 像素（缩放2倍）
- **特性**:
  - 两种纹理：睁眼/闭眼
  - 圆润的椭圆身体
  - 小黑眼睛（带瞳孔）
  - 棕色鼻子

### 动画行为
- **移动速度**: 1.0 像素/帧
- **摇摆效果**: sin(time/200) * 0.6
- **区域漫游**: 目标点周围 ±40 像素随机
- **触发频率**: 0.5% 每帧

## 📊 性能参数

- **轮询间隔**: 2000ms（状态检查）
- **眨眼间隔**: 2500ms
- **气泡间隔**: 8000ms
- **打字速度**: 50ms/字符
- **自动空闲**: 25秒无更新
- **帧率**: 60 FPS（Phaser默认）

## 🔧 配置文件

### backend/app.py
- 端口: 18791
- 主机: 0.0.0.0（监听所有接口）
- 调试模式: False

### state.json 示例
```json
{
  "state": "writing",
  "detail": "正在编写文档...",
  "progress": 60,
  "updated_at": "2026-02-27T13:00:00",
  "ttl_seconds": 25
}
```

## 🚀 部署建议

### 本地开发
```bash
python backend/app.py
```

### 生产环境
推荐使用 WSGI 服务器：
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:18791 backend.app:app
```

### 反向代理（Nginx）
```nginx
location / {
    proxy_pass http://127.0.0.1:18791;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## 📝 API 使用示例

### 查询状态
```bash
curl http://localhost:18791/status
```

### 更新状态（使用工具脚本）
```bash
python set_state.py writing "处理重要文档"
```

### 健康检查
```bash
curl http://localhost:18791/health
```

## 🎬 使用场景

1. **开发环境监控**: 显示 AI 助手当前工作状态
2. **演示展示**: 直观展示系统运行情况
3. **团队看板**: 多人协作时的状态同步
4. **趣味装饰**: 给工作环境增添活力

## 📦 文件清单

```
happycapy-office-ui/
├── README.md                    # 用户文档
├── PROJECT_OVERVIEW.md          # 技术文档（本文件）
├── requirements.txt             # Python依赖
├── .gitignore                   # Git忽略规则
├── state.sample.json            # 状态文件示例
├── set_state.py                 # 状态更新工具
├── demo_states.sh               # 演示脚本
├── create_background.py         # 简易背景生成器
├── create_luxury_background.py  # 豪华背景生成器
├── backend/
│   └── app.py                   # Flask后端服务
└── frontend/
    ├── index.html               # 前端页面
    └── office_bg.png            # 办公室背景图
```

## 🔮 未来扩展

- [ ] 添加音效（打字声、移动声）
- [ ] 支持多角色（不同AI助手）
- [ ] 添加更多区域（咖啡间、打印区等）
- [ ] 实时进度条显示
- [ ] WebSocket实时推送（替代轮询）
- [ ] 历史状态记录
- [ ] 数据统计面板
- [ ] 自定义主题系统

---

**创建于**: 2026-02-27
**基于**: Star-Office-UI
**许可证**: MIT
