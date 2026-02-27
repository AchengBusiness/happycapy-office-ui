#!/usr/bin/env python3
"""创建简单的像素风格办公室背景图"""

from PIL import Image, ImageDraw, ImageFont
import os

# 创建 800x600 的图像
width, height = 800, 600
img = Image.new('RGB', (width, height), color='#e8dcc8')
draw = ImageDraw.Draw(img)

# 绘制地板瓷砖
tile_size = 40
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        if (x // tile_size + y // tile_size) % 2 == 0:
            draw.rectangle([x, y, x + tile_size, y + tile_size], fill='#d4c4a8')

# 绘制工作区（左下）
# 工作桌
draw.rectangle([180, 280, 340, 400], fill='#8B4513')
draw.rectangle([185, 285, 335, 395], fill='#A0522D')
# 椅子
draw.rectangle([240, 410, 280, 440], fill='#4a4a4a')

# 绘制休息区（右上）
# 沙发
draw.rectangle([580, 140, 720, 200], fill='#3498db')
draw.rectangle([585, 145, 715, 195], fill='#5dade2')
# 茶几
draw.rectangle([620, 220, 680, 260], fill='#8B4513')
draw.rectangle([625, 225, 675, 255], fill='#A0522D')

# 绘制植物（装饰）
draw.ellipse([100, 150, 140, 200], fill='#228B22')
draw.rectangle([115, 200, 125, 240], fill='#8B4513')

draw.ellipse([720, 400, 760, 450], fill='#228B22')
draw.rectangle([735, 450, 745, 490], fill='#8B4513')

# 绘制书架（右下）
draw.rectangle([600, 450, 720, 550], fill='#654321')
for i in range(3):
    y = 470 + i * 30
    draw.line([605, y, 715, y], fill='#8B4513', width=3)

# 绘制电脑（工作桌上）
draw.rectangle([220, 300, 280, 340], fill='#2c3e50')
draw.rectangle([225, 305, 275, 330], fill='#3498db')

# 绘制窗户（上方）
draw.rectangle([50, 30, 180, 120], fill='#87CEEB')
draw.rectangle([250, 30, 380, 120], fill='#87CEEB')
draw.rectangle([450, 30, 580, 120], fill='#87CEEB')
# 窗框
for x in [50, 250, 450]:
    draw.rectangle([x, 30, x + 130, 120], outline='#4a4a4a', width=3)
    draw.line([x + 65, 30, x + 65, 120], fill='#4a4a4a', width=2)
    draw.line([x, 75, x + 130, 75], fill='#4a4a4a', width=2)

# 绘制地毯（中央）
draw.ellipse([300, 250, 500, 400], fill='#c0392b', outline='#922b21', width=3)

# 保存图像
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'office_bg.png')
img.save(output_path)
print(f"✓ 背景图已创建: {output_path}")
