## 🏢 HappyCapy Office - CAD 平面图版本

### ✨ 新版特性

全新的 **CAD 风格办公室平面图**，参考建筑设计图纸打造！

---

## 🎨 CAD 版本 vs 原版对比

### 原版（等距投影）
- ❌ 视角：斜视 45° 等距投影
- ❌ 风格：像素艺术、游戏风格
- ❌ 尺寸：800 × 600
- ❌ 细节：较少，装饰性强

### CAD 版本（平面图）✅
- ✅ 视角：**正俯视图**，像建筑设计图
- ✅ 风格：**专业 CAD 平面图**
- ✅ 尺寸：**1200 × 800**（更大更清晰）
- ✅ 细节：**精确标注、图例、网格、坐标系**

---

## 🏗️ CAD 风格特点

### 1. **建筑级网格**
- 40×40 像素标准网格
- 辅助定位和测量
- 专业CAD软件风格

### 2. **墙体系统**
- 20px 厚度标准墙体
- 深灰色墙体 `#2c3e50`
- 清晰的房间分隔

### 3. **门窗标识**
- 🚪 **门**: 红色 `#e74c3c`，带门把手
- 🪟 **窗户**: 蓝色 `#3498db`，带窗格

### 4. **家具俯视图**
- 💼 **办公桌**: 紫色 `#8e44ad`，带WORK/CODE标签
- 🪑 **椅子**: 圆形灰色，精确布局
- 🛋️ **沙发**: 橙色，带靠垫细节
- 🖥️ **服务器**: 深灰机柜，绿色 LED

### 5. **专业标注**
- 区域名称标注（WORK AREA, DEV ZONE等）
- 右下角完整图例
- 左下角坐标系（X/Y轴）
- 顶部标题和比例尺 (1:50)

---

## 📐 房间布局

```
┌──────────────────────────────────────────────────┐
│  HAPPYCAPY OFFICE - FLOOR PLAN  |  Scale: 1:50   │
├──────────────┬───────────────────┬────────────────┤
│              │                   │  SERVER ROOM   │
│  WORK AREA   │   MEETING ROOM    │  🖥️ 🖥️         │
│  💼 🪑       │   🪑 🪑 🪑       │                │
│              │   🍽️             │  🔌 Network    │
│  DEV ZONE    │   🪑 🪑 🪑       ├────────────────┤
│  💻 🪑       │                   │                │
├──────────────┤                   │   LIBRARY      │
│   LOUNGE     │                   │   📚 📚        │
│   🛋️ 🛋️    │                   │   🪴           │
│   🍽️         │                   │                │
└──────────────┴───────────────────┴────────────────┘
```

### 区域说明

1. **WORK AREA** (左上) - 主办公桌区
   - 坐标: (210, 230)
   - 用途: 日常工作、文档编写

2. **DEV ZONE** (左中) - 开发区
   - 坐标: (210, 480)
   - 用途: 编程、代码开发

3. **LOUNGE** (左下) - 休息区
   - 坐标: (225, 600)
   - 用途: 休息、待命

4. **MEETING ROOM** (中央) - 会议室
   - 坐标: (550, 500)
   - 用途: 团队讨论、头脑风暴

5. **SERVER ROOM** (右上) - 服务器机房
   - 坐标: (950, 225)
   - 用途: 执行任务、系统操作

6. **LIBRARY** (右下) - 图书区
   - 坐标: (1060, 525)
   - 用途: 研究、学习、同步

---

## 🚀 快速开始

### 方法 1: 生成 CAD 平面图

```bash
# 生成 CAD 风格平面图
python create_cad_office.py
```

生成文件：`frontend/office_cad.png` (1200 × 800)

### 方法 2: 使用 CAD 版本前端

```bash
# 复制 CAD 版本为主页面（可选）
cp frontend/index_cad.html frontend/index.html

# 启动服务器
cd backend
python app.py
```

访问：http://localhost:18791

### 方法 3: 同时运行两个版本

**原版（等距投影）**
```bash
# 保持 index.html 不变
# 访问: http://localhost:18791/
```

**CAD 版本**
```bash
# 访问: http://localhost:18791/index_cad.html
```

---

## 🔄 实时状态集成

### 原理

CAD 版本支持**实时显示工作状态**：

```
Claude 执行操作 → realtime_bridge.py
→ state.json 更新
→ 前端轮询 /status
→ 水豚移动到对应区域
```

### 状态映射

| 状态 | 区域 | 说明 |
|------|------|------|
| `writing` | WORK AREA | 正在写文档/代码 |
| `researching` | DEV ZONE | 研究/搜索信息 |
| `executing` | SERVER ROOM | 执行命令/任务 |
| `syncing` | LIBRARY | 同步/学习 |
| `error` | LOUNGE | 错误/等待 |
| `idle` | LOUNGE | 空闲/待命 |

### 实时状态示例

```python
from realtime_bridge import bridge

# 开始编写代码
bridge.update_activity('writing', '正在创建 CAD 平面图...')
# → 水豚移动到 WORK AREA

# 执行测试
bridge.update_activity('running', '正在执行 Python 脚本...')
# → 水豚移动到 SERVER ROOM

# 完成任务
bridge.update_activity('thinking', '任务完成，待命中...')
# → 水豚返回 LOUNGE
```

---

## 🎯 UI 增强功能

### 信息面板

新版 UI 包含 4 个实时信息卡片：

1. **📍 Current Location** - 当前位置
2. **⚡ Current Activity** - 当前活动详情
3. **🕐 Last Update** - 最后更新时间
4. **📊 Status** - 状态（带emoji）

### 视觉改进

- ✅ 现代化渐变背景
- ✅ 圆角卡片设计
- ✅ 实时脉冲动画
- ✅ 平滑移动过渡
- ✅ 专业信息展示

---

## 🛠️ 自定义 CAD 平面图

### 修改颜色

编辑 `create_cad_office.py`：

```python
# 修改配色方案
wall_color = '#2c3e50'       # 墙体颜色
door_color = '#e74c3c'       # 门颜色
window_color = '#3498db'     # 窗户颜色
desk_color = '#8e44ad'       # 办公桌颜色
```

### 调整布局

```python
# 修改房间位置
draw.rectangle([400, 100, 420, 400], fill=wall_color)  # 分隔墙

# 添加新家具
draw_desk(x, y, width, height, label='NEW')
draw_chair(x, y)
draw_plant(x, y)
```

### 更改尺寸

```python
# 修改画布尺寸
width, height = 1600, 1000  # 改成更大的尺寸
```

**注意：** 修改尺寸后需要同步更新 `frontend/index_cad.html` 中的 canvas 配置。

---

## 📊 对比总结

| 特性 | 原版 | CAD 版本 |
|------|------|----------|
| 视角 | 等距 45° | 正俯视 90° |
| 尺寸 | 800×600 | 1200×800 |
| 风格 | 游戏/像素 | 建筑/CAD |
| 网格 | 无 | 40px 标准网格 |
| 标注 | 无 | 区域标注 + 图例 |
| 图例 | 无 | 完整图例 |
| 坐标系 | 无 | X/Y 轴坐标系 |
| 专业度 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🎓 CAD 平面图知识

### 什么是 CAD 平面图？

**CAD (Computer-Aided Design)** 是计算机辅助设计：

- 建筑师用来设计房屋的工具
- 正俯视 90° 视角
- 精确的尺寸和比例
- 标准符号和图例
- 网格辅助对齐

### 为什么使用 CAD 风格？

1. **更专业** - 像真实的建筑设计图
2. **更清晰** - 俯视图一目了然
3. **更精确** - 网格和标注便于定位
4. **更实用** - 符合用户对"房间型"的期望

---

## 🔗 相关文件

- `create_cad_office.py` - CAD 平面图生成器
- `frontend/index_cad.html` - CAD 版本前端
- `realtime_bridge.py` - 实时状态桥接
- `frontend/office_cad.png` - 生成的平面图

---

## 💡 使用建议

1. **日常使用** - 使用 CAD 版本，更专业清晰
2. **展示演示** - CAD 版本更适合对外展示
3. **像素爱好者** - 可以继续使用原版
4. **并行运行** - 两个版本可以同时存在

---

**享受你的专业级办公室平面图！** 🏢✨
