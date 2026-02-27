#!/usr/bin/env python3
"""创建豪华版像素风格办公室背景图"""

from PIL import Image, ImageDraw
import os

# 创建 800x600 的图像
width, height = 800, 600
img = Image.new('RGB', (width, height), color='#f5f0e8')
draw = ImageDraw.Draw(img)

# === 地板 - 木地板效果 ===
wood_colors = ['#c19a6b', '#d4a574', '#b8926a']
plank_height = 40
for y in range(0, height, plank_height):
    for x in range(0, width, 80):
        color = wood_colors[(x // 80 + y // plank_height) % 3]
        draw.rectangle([x, y, x + 80, y + plank_height], fill=color, outline='#8B7355', width=1)

# === 墙面装饰线条 ===
draw.rectangle([0, 0, width, 150], fill='#e8dcc8')  # 上墙
draw.line([0, 150, width, 150], fill='#8B7355', width=3)  # 墙面分界线

# === 窗户区域（豪华落地窗）===
# 左侧大窗
draw.rectangle([30, 20, 200, 130], fill='#87CEEB', outline='#2c3e50', width=4)
draw.line([115, 20, 115, 130], fill='#2c3e50', width=3)
draw.line([30, 75, 200, 75], fill='#2c3e50', width=3)
# 窗帘
draw.polygon([(30, 20), (50, 20), (40, 50)], fill='#c0392b')
draw.polygon([(180, 20), (200, 20), (190, 50)], fill='#c0392b')

# 中间窗
draw.rectangle([280, 20, 430, 130], fill='#87CEEB', outline='#2c3e50', width=4)
draw.line([355, 20, 355, 130], fill='#2c3e50', width=3)
draw.line([280, 75, 430, 75], fill='#2c3e50', width=3)
# 窗帘
draw.polygon([(280, 20), (300, 20), (290, 50)], fill='#c0392b')
draw.polygon([(410, 20), (430, 20), (420, 50)], fill='#c0392b')

# 右侧窗
draw.rectangle([530, 20, 680, 130], fill='#87CEEB', outline='#2c3e50', width=4)
draw.line([605, 20, 605, 130], fill='#2c3e50', width=3)
draw.line([530, 75, 680, 75], fill='#2c3e50', width=3)

# === 玻璃隔断（现代办公风格）===
# 左侧隔断
draw.rectangle([10, 150, 15, 600], fill='#34495e')  # 边框
draw.rectangle([15, 150, 180, 600], fill='#ecf0f1', outline='#34495e', width=2)  # 玻璃
for y in range(200, 600, 100):
    draw.line([15, y, 180, y], fill='#bdc3c7', width=2)

# 右后隔断
draw.rectangle([680, 150, 685, 450], fill='#34495e')
draw.rectangle([685, 150, 790, 450], fill='#ecf0f1', outline='#34495e', width=2)
for y in range(200, 450, 80):
    draw.line([685, y, 790, y], fill='#bdc3c7', width=2)

# === 服务器机柜区（右上角）===
# 机柜1
draw.rectangle([690, 160, 750, 300], fill='#2c3e50', outline='#000000', width=2)
for i in range(6):
    y = 170 + i * 20
    draw.rectangle([695, y, 745, y + 15], fill='#34495e')
    draw.circle((705, y + 7), 2, fill='#27ae60')  # 绿色指示灯
    draw.circle((715, y + 7), 2, fill='#27ae60')
    draw.circle((735, y + 7), 2, fill='#f39c12')  # 橙色指示灯

# 机柜2
draw.rectangle([690, 310, 750, 440], fill='#2c3e50', outline='#000000', width=2)
for i in range(5):
    y = 320 + i * 23
    draw.rectangle([695, y, 745, y + 18], fill='#34495e')
    draw.circle((705, y + 9), 2, fill='#27ae60')
    draw.circle((725, y + 9), 2, fill='#3498db')  # 蓝色指示灯

# === 豪华办公桌区（左下）===
# 主办公桌
draw.rectangle([190, 280, 380, 420], fill='#5d4037', outline='#3e2723', width=3)
draw.rectangle([195, 285, 375, 415], fill='#6d4c41')  # 桌面
# 桌面装饰
draw.rectangle([205, 295, 245, 335], fill='#2c3e50')  # 显示器
draw.rectangle([210, 300, 240, 325], fill='#3498db')  # 屏幕
draw.rectangle([220, 335, 230, 345], fill='#34495e')  # 支架
# 键盘
draw.rectangle([255, 320, 315, 340], fill='#ecf0f1', outline='#95a5a6', width=1)
# 鼠标
draw.ellipse([325, 325, 340, 340], fill='#34495e')
# 咖啡杯
draw.ellipse([350, 305, 365, 320], fill='#8B4513')
draw.arc([350, 305, 365, 320], 0, 180, fill='#fff', width=1)

# 办公椅（豪华版）
draw.ellipse([255, 430, 315, 470], fill='#2c3e50')  # 座位
draw.rectangle([280, 400, 290, 430], fill='#34495e')  # 靠背支撑
draw.rectangle([270, 380, 300, 420], fill='#2c3e50')  # 靠背
draw.line([260, 470, 270, 485], fill='#7f8c8d', width=3)  # 椅脚
draw.line([300, 470, 310, 485], fill='#7f8c8d', width=3)

# === 会议桌区（中上）===
draw.ellipse([350, 180, 550, 260], fill='#8B4513', outline='#654321', width=3)
draw.ellipse([355, 185, 545, 255], fill='#A0522D')
# 会议椅子
for x in [370, 430, 490, 530]:
    draw.rectangle([x, 165, x + 20, 180], fill='#c0392b')
    draw.rectangle([x, 265, x + 20, 280], fill='#c0392b')

# === 休息区（右边中部）===
# L型沙发
draw.rectangle([690, 460, 780, 530], fill='#2980b9', outline='#1a5276', width=3)
draw.rectangle([630, 500, 690, 570], fill='#2980b9', outline='#1a5276', width=3)
# 沙发细节
for x in range(700, 770, 20):
    draw.line([x, 470, x, 520], fill='#3498db', width=2)
for x in range(640, 680, 20):
    draw.line([x, 510, x, 560], fill='#3498db', width=2)

# 茶几
draw.rectangle([620, 450, 680, 490], fill='#34495e', outline='#2c3e50', width=2)
draw.rectangle([625, 445, 675, 450], fill='#ecf0f1')  # 玻璃台面

# === 大型地毯 ===
draw.ellipse([320, 300, 600, 500], fill='#8B0000', outline='#660000', width=4)
# 地毯花纹
for i in range(3):
    r = 40 + i * 20
    draw.ellipse([460 - r, 400 - r // 2, 460 + r, 400 + r // 2], outline='#B22222', width=2)

# === 绿植装饰 ===
# 大型龙血树（左前）
draw.rectangle([40, 420, 80, 480], fill='#8B4513')  # 花盆
draw.rectangle([45, 425, 75, 475], fill='#A0522D')
draw.ellipse([35, 340, 85, 420], fill='#228B22')  # 树冠
draw.ellipse([40, 360, 80, 410], fill='#32CD32')
draw.line([60, 420, 60, 380], fill='#654321', width=5)  # 树干

# 小盆栽（工作桌角）
draw.ellipse([185, 390, 205, 410], fill='#8B4513')
draw.ellipse([188, 375, 202, 395], fill='#228B22')

# 吊兰（右侧）
draw.rectangle([755, 520, 780, 550], fill='#D2691E')
draw.ellipse([750, 500, 785, 530], fill='#228B22')
for i in range(3):
    draw.line([765 + i * 5, 530, 760 + i * 5, 545], fill='#32CD32', width=2)

# === 书架（左侧墙边）===
draw.rectangle([20, 200, 150, 380], fill='#654321', outline='#3e2723', width=3)
# 书架层板
for y in [230, 270, 310, 350]:
    draw.line([25, y, 145, y], fill='#8B4513', width=4)
# 书籍
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
for shelf_y in [210, 250, 290, 330]:
    x_pos = 30
    for i in range(8):
        book_color = colors[i % 5]
        book_width = 12 + (i % 3) * 3
        draw.rectangle([x_pos, shelf_y, x_pos + book_width, shelf_y + 35],
                      fill=book_color, outline='#000', width=1)
        x_pos += book_width + 2

# === 白板（中间墙上）===
draw.rectangle([240, 160, 470, 240], fill='#ffffff', outline='#2c3e50', width=4)
# 白板内容（示意）
draw.line([250, 175, 320, 175], fill='#3498db', width=2)
draw.line([250, 190, 380, 190], fill='#e74c3c', width=2)
draw.rectangle([250, 205, 270, 225], outline='#27ae60', width=2)
draw.ellipse([285, 205, 305, 225], outline='#f39c12', width=2)

# === 文件柜（右下角）===
draw.rectangle([620, 580, 680, 600], fill='#95a5a6', outline='#7f8c8d', width=2)
for y in [585, 593]:
    draw.rectangle([625, y, 675, y + 5], fill='#7f8c8d')
    draw.circle((650, y + 2), 2, fill='#000')

# === 时钟（墙上）===
draw.circle((720, 60), 25, fill='#ecf0f1', outline='#2c3e50', width=3)
draw.line([720, 60, 720, 45], fill='#2c3e50', width=2)  # 时针
draw.line([720, 60, 730, 65], fill='#e74c3c', width=1)  # 分针

# === 天花板灯光效果 ===
for x in [250, 450, 650]:
    draw.ellipse([x - 15, 155, x + 15, 165], fill='#f39c12', outline='#d68910', width=2)
    # 光晕效果
    draw.ellipse([x - 25, 150, x + 25, 170], outline='#fef5e7', width=1)

# 保存图像
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'office_bg.png')
img.save(output_path)
print(f"✓ 豪华办公室背景已创建: {output_path}")
print("✓ 包含: 玻璃隔断、服务器机柜、豪华办公桌、会议桌、休息沙发区")
print("✓ 装饰: 多个绿植、书架、白板、时钟、地毯、文件柜")
