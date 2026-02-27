# HappyCapy Office UI - 快速开始指南

## ⚡ 5分钟快速启动

### 1. 安装依赖
```bash
pip install flask
```

### 2. 启动服务器
```bash
cd happycapy-office-ui/backend
python app.py
```
访问: http://127.0.0.1:18791

### 3. 更新状态
```bash
# 在项目根目录
python set_state.py writing "正在工作中..."
```

## 🎮 常用命令

### 状态切换
```bash
# 待命（休息区）
python set_state.py idle "摸鱼中~"

# 工作中（办公桌）
python set_state.py writing "整理文档..."
python set_state.py researching "搜索资料..."
python set_state.py executing "执行任务..."

# 其他
python set_state.py syncing "同步数据..."
python set_state.py error "出错了..."
```

### 观看演示
```bash
./demo_states.sh
```

## 🎨 自定义背景

修改后重新生成：
```bash
python create_luxury_background.py
```

## 🌐 公开访问

使用 Cloudflare Tunnel:
```bash
cloudflared tunnel --url http://127.0.0.1:18791
```

## 📍 区域位置参考

- **办公桌**: 左下角 - 适合工作状态
- **休息区**: 右下角 - 适合待命状态
- **会议桌**: 中上方 - 可扩展使用
- **服务器**: 右上角 - 技术氛围

## 🔧 故障排查

### 服务器无法启动
```bash
# 检查端口是否被占用
lsof -i :18791

# 更改端口（编辑 backend/app.py）
app.run(host="0.0.0.0", port=8080)
```

### 状态不更新
```bash
# 检查状态文件
cat state.json

# 手动重置
python set_state.py idle "重新开始"
```

### 背景图不显示
```bash
# 确认文件存在
ls frontend/office_bg.png

# 重新生成
python create_luxury_background.py
```

## 💡 小贴士

- 状态会在25秒后自动返回idle
- 水豚会在区域内随机移动
- 对话气泡每8秒随机显示
- 支持移动端访问

## 📚 更多文档

- `README.md` - 完整功能说明
- `PROJECT_OVERVIEW.md` - 技术架构文档
- `demo_states.sh` - 状态演示脚本

---
有问题？查看完整 README.md 或技术文档！
