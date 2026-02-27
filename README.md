# HappyCapy Office UI - 豪华版

一个精致的像素风格办公室状态 UI，用于展示 AI 助手的工作状态。

## ✨ 特点

- 🏢 **豪华办公套间**：精心设计的像素风格办公室（俯视视角）
- 🦫 **可爱水豚角色**：根据状态在不同区域移动
- 💬 **动态交互**：对话气泡和打字机效果
- 📱 **移动端友好**：响应式设计
- 🎨 **丰富细节**：
  - 玻璃隔断分区
  - 服务器机柜（带闪烁指示灯）
  - 豪华办公桌配电脑显示器
  - 会议桌区域
  - L型休息沙发
  - 多个绿植装饰
  - 书架、白板、时钟
  - 地毯和文件柜

## 状态映射

- `idle / syncing / error` → 休息区
- `writing / researching / executing` → 工作桌

UI 会定期轮询 `/status` 端点并相应地渲染水豚角色。

## 目录结构

```
happycapy-office-ui/
  backend/        # Flask 后端（提供首页和状态接口）
  frontend/       # Phaser 前端 + office_bg.png
  state.json      # 运行时状态文件
  set_state.py    # 状态更新工具
```

## 环境要求

- Python 3.9+
- Flask

## 快速开始

### 1) 安装依赖

```bash
pip install flask
```

### 2) 放置背景图片

在以下路径放置 **800×600 PNG** 图片：

```
happycapy-office-ui/frontend/office_bg.png
```

你可以创建自己的像素风格办公室背景，或使用任何 800x600 的图片。

### 3) 启动后端

```bash
cd happycapy-office-ui/backend
python app.py
```

然后打开浏览器访问：

- http://127.0.0.1:18791

### 4) 更新状态

从项目根目录运行：

```bash
python set_state.py writing "正在编写文档..."
python set_state.py idle "待命中"
python set_state.py researching "搜索资料中..."
python set_state.py executing "执行任务中..."
```

### 5) 观看状态演示

运行自动演示脚本查看各种状态切换：

```bash
./demo_states.sh
```

演示脚本会自动循环展示所有状态，让水豚在不同区域移动。

## 可用状态

- `idle` - 待命（休息区）
- `writing` - 整理文档（工作桌）
- `researching` - 搜索信息（工作桌）
- `executing` - 执行任务（工作桌）
- `syncing` - 同步备份（休息区）
- `error` - 出错了（休息区）

## 自动空闲机制

如果状态超过 25 秒未更新，且当前处于工作状态（writing/researching/executing），系统会自动将状态切换为 idle，水豚会返回休息区。

## 公开访问（Cloudflare Tunnel）

如果想要公开访问，可以使用 `cloudflared`：

```bash
cloudflared tunnel --url http://127.0.0.1:18791
```

你会得到一个 `https://xxx.trycloudflare.com` 网址。

## 安全注意事项

- 任何拥有 tunnel URL 的人都可以读取 `/status`
- 不要在 `detail` 中放置敏感信息
- 如需要，可以为 `/status` 添加 token 验证

## 豪华版特性

### 办公区域划分

- **豪华办公桌区** (左下): 配备显示器、键盘、鼠标、咖啡杯
- **休息沙发区** (右下): L型豪华沙发配茶几
- **会议桌区** (中上): 椭圆形会议桌配椅子
- **服务器机柜区** (右上): 专业机柜带状态指示灯

### 装饰元素

- 🪴 **绿植**: 大型龙血树、小盆栽、吊兰
- 📚 **书架**: 装满彩色书籍的木质书架
- 📋 **白板**: 用于会议讨论和头脑风暴
- 🕐 **时钟**: 墙面装饰时钟
- 🪟 **窗户**: 三个大型落地窗配红色窗帘
- 🔲 **玻璃隔断**: 现代办公风格的透明分区
- 🔴 **地毯**: 椭圆形装饰地毯

## 自定义

### 修改角色外观

编辑 `frontend/index.html` 中的角色创建部分，可以自定义水豚的颜色和形状。

### 修改区域位置

在 `frontend/index.html` 中修改 `areas` 对象的坐标：

```javascript
areas = {
    workdesk: { x: 285, y: 350 },    // 豪华办公桌区域
    breakroom: { x: 705, y: 495 },   // 休息沙发区
    meeting: { x: 450, y: 220 },      // 会议桌区域
    server: { x: 720, y: 230 },       // 服务器机柜区
    alert: { x: 620, y: 490 }
};
```

### 修改对话文本

编辑 `BUBBLE_TEXTS` 对象来自定义不同状态下的对话内容。

### 重新生成背景

如果想要修改办公室布局，编辑 `create_luxury_background.py` 然后运行：

```bash
python create_luxury_background.py
```

## License

MIT

---

基于 [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) 修改
