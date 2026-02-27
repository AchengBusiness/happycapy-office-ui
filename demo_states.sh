#!/bin/bash
# 演示不同状态的脚本

echo "🎬 HappyCapy 办公室状态演示"
echo "=============================="
echo ""

echo "1️⃣ 待命状态 - 在豪华休息区"
python set_state.py idle "在L型沙发上放松，享受咖啡~"
sleep 5

echo ""
echo "2️⃣ 工作状态 - 在办公桌"
python set_state.py writing "在豪华办公桌前整理重要文档..."
sleep 5

echo ""
echo "3️⃣ 研究状态 - 专注工作"
python set_state.py researching "查阅服务器机柜的运行日志..."
sleep 5

echo ""
echo "4️⃣ 执行任务 - 高效运转"
python set_state.py executing "处理多个任务，效率全开！"
sleep 5

echo ""
echo "5️⃣ 同步备份 - 数据安全"
python set_state.py syncing "正在将数据同步到云端服务器..."
sleep 5

echo ""
echo "6️⃣ 返回待命 - 任务完成"
python set_state.py idle "工作告一段落，回到休息区喝茶~"

echo ""
echo "✅ 演示完成！"
