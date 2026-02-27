#!/usr/bin/env python3
"""创建更加豪华的等距投影风格办公室 - 参考Pixel Agents风格"""

from PIL import Image, ImageDraw
import math
import os

# 创建 800x600 的图像
width, height = 800, 600
img = Image.new('RGB', (width, height), color='#2d2d44')
draw = ImageDraw.Draw(img)

# === 颜色方案 ===
floor_base = '#3a3a52'
floor_alt = '#45455e'
wall_color = '#252538'
desk_wood = '#8B6F47'
desk_light = '#A0826D'
tech_blue = '#4a9eff'
tech_dark = '#2c5f9a'
plant_green = '#4a9e5f'
chair_red = '#c44569'
sofa_blue = '#3867d6'

# === 地板（菱形瓷砖 - 等距风格）===
def draw_iso_tile(x, y, w, h, color1, color2):
    """绘制等距投影瓷砖"""
    # 菱形的四个点
    top = (x, y)
    right = (x + w//2, y + h//2)
    bottom = (x, y + h)
    left = (x - w//2, y + h//2)

    # 绘制主面（顶面）
    draw.polygon([top, right, bottom, left], fill=color1, outline=color2, width=1)

# 绘制地板网格
tile_w, tile_h = 60, 30
for row in range(-2, 15):
    for col in range(-2, 20):
        x = 400 + (col - row) * (tile_w // 2)
        y = 100 + (col + row) * (tile_h // 2)
        if 0 <= x <= 850 and 0 <= y <= 650:
            color = floor_base if (row + col) % 2 == 0 else floor_alt
            draw_iso_tile(x, y, tile_w, tile_h, color, '#2a2a3f')

# === 后墙 ===
draw.rectangle([0, 0, width, 160], fill=wall_color)

# === 窗户（等距风格）===
def draw_iso_window(x, y, w, h):
    """绘制等距窗户"""
    # 窗框
    draw.rectangle([x, y, x+w, y+h], fill='#1a1a2e', outline='#0f0f1e', width=3)
    # 玻璃（渐变效果模拟）
    draw.rectangle([x+5, y+5, x+w-5, y+h-5], fill='#4a7c9e', outline='#2c5f9a', width=2)
    # 窗格
    draw.line([x+w//2, y+5, x+w//2, y+h-5], fill='#1a1a2e', width=2)
    draw.line([x+5, y+h//2, x+w-5, y+h//2], fill='#1a1a2e', width=2)

# 三个现代窗户
draw_iso_window(50, 30, 120, 100)
draw_iso_window(340, 30, 120, 100)
draw_iso_window(630, 30, 120, 100)

# === 豪华办公桌（左下，等距风格）===
def draw_iso_box(x, y, w, h, d, top_color, side_color):
    """绘制等距立方体"""
    # 顶面
    top_points = [
        (x, y),
        (x + w, y - w//2),
        (x + w + d, y - w//2 + d//2),
        (x + d, y + d//2)
    ]
    draw.polygon(top_points, fill=top_color, outline='#000', width=1)

    # 右侧面
    if d > 0:
        right_points = [
            (x + w, y - w//2),
            (x + w + d, y - w//2 + d//2),
            (x + w + d, y - w//2 + d//2 + h),
            (x + w, y - w//2 + h)
        ]
        draw.polygon(right_points, fill=side_color, outline='#000', width=1)

    # 前面
    front_points = [
        (x, y),
        (x + w, y - w//2),
        (x + w, y - w//2 + h),
        (x, y + h)
    ]
    draw.polygon(front_points, fill=side_color, outline='#000', width=1)

# 主办公桌
draw_iso_box(180, 360, 100, 40, 60, desk_light, desk_wood)

# 显示器（在桌上）
draw_iso_box(200, 310, 50, 35, 8, tech_dark, '#1a1a2e')
# 屏幕
draw.rectangle([205, 315, 245, 340], fill=tech_blue)

# 键盘
draw_iso_box(260, 340, 40, 8, 20, '#d4d4dc', '#a0a0a8')

# === 豪华沙发区（右下）===
# L型沙发主体
draw_iso_box(650, 500, 80, 35, 60, sofa_blue, '#2d4a8f')
# L型延伸
draw_iso_box(590, 530, 60, 35, 40, sofa_blue, '#2d4a8f')

# 沙发靠垫
for offset in [10, 30, 50]:
    draw.ellipse([660+offset, 500, 675+offset, 515], fill='#5a7ec6')

# 茶几
draw_iso_box(610, 480, 50, 20, 40, '#6a5d4f', '#4a3d2f')

# === 会议桌（中上）===
# 椭圆形会议桌（等距模拟）
draw.ellipse([360, 200, 540, 270], fill='#6d4c41', outline='#4a3d2f', width=3)
draw.ellipse([365, 205, 535, 265], fill='#8B6F47')

# 会议椅
chair_positions = [(380, 190), (450, 185), (500, 190), (390, 275), (480, 275)]
for cx, cy in chair_positions:
    draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill=chair_red, outline='#8e2a45', width=1)

# === 服务器机柜区（右上）===
# 机柜1
draw_iso_box(690, 190, 45, 90, 25, '#2c3e50', '#1a252f')
# 服务器层
for i in range(5):
    y = 200 + i * 16
    draw.rectangle([695, y, 725, y+12], fill='#34495e', outline='#000', width=1)
    # LED灯
    draw.circle((703, y+6), 2, fill='#27ae60')
    draw.circle((710, y+6), 2, fill='#27ae60')
    draw.circle((717, y+6), 2, fill='#f39c12')

# 机柜2
draw_iso_box(745, 200, 40, 80, 20, '#2c3e50', '#1a252f')
for i in range(4):
    y = 210 + i * 18
    draw.rectangle([750, y, 775, y+14], fill='#34495e', outline='#000', width=1)
    draw.circle((758, y+7), 2, fill='#3498db')
    draw.circle((767, y+7), 2, fill='#27ae60')

# === 装饰元素 ===

# 大型绿植（左前）
def draw_plant(x, y, pot_w, pot_h):
    """绘制等距植物"""
    # 花盆
    draw_iso_box(x, y, pot_w, pot_h, pot_w//2, '#8B4513', '#654321')
    # 植物叶子
    for i in range(3):
        offset_x = -15 + i * 15
        offset_y = -30 - i * 10
        draw.ellipse([x+pot_w//2-10+offset_x, y+offset_y,
                     x+pot_w//2+10+offset_x, y+offset_y+20],
                    fill=plant_green, outline='#2d5f3a', width=1)

draw_plant(40, 440, 35, 30)

# 小盆栽（多个位置）
draw_plant(170, 420, 20, 15)
draw_plant(760, 540, 25, 20)

# === 书架（左侧）===
draw_iso_box(25, 220, 80, 130, 30, '#654321', '#4a3021')
# 书架层板
for y in [240, 280, 320]:
    draw.line([30, y, 105, y], fill='#8B6F47', width=3)
# 书籍
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
for shelf in [225, 265, 305]:
    x_pos = 35
    for i, color in enumerate(colors):
        w = 8 + i % 3 * 2
        draw.rectangle([x_pos, shelf, x_pos+w, shelf+30], fill=color, outline='#000', width=1)
        x_pos += w + 2

# === 照明效果 ===
# 吊灯
for x in [250, 500, 700]:
    # 灯具
    draw.ellipse([x-12, 155, x+12, 170], fill='#ffd700', outline='#d4af37', width=2)
    # 光晕
    draw.ellipse([x-25, 150, x+25, 175], outline='#fff9e6', width=1)
    draw.ellipse([x-35, 145, x+35, 180], outline='#fff9e6', width=1)

# === 地毯（装饰）===
# 办公桌前的小地毯
draw.ellipse([200, 380, 350, 450], fill='#8B4B3D', outline='#6d3a2f', width=2)
# 花纹
for r in [15, 25, 35]:
    draw.ellipse([275-r, 415-r//2, 275+r, 415+r//2], outline='#a0564a', width=1)

# 沙发区的地毯
draw.ellipse([580, 480, 720, 560], fill='#5a4a6a', outline='#4a3a5a', width=2)
for r in [12, 22]:
    draw.ellipse([650-r, 520-r//2, 650+r, 520+r//2], outline='#7a6a8a', width=1)

# === 墙面装饰 ===
# 公司logo/标识牌
draw.rectangle([200, 145, 600, 155], fill='#ffd700', outline='#d4af37', width=2)
# 文字区域（占位）
draw.rectangle([250, 148, 550, 152], fill='#000')

# === 玻璃隔断（现代风格）===
# 左侧隔断
for y in range(160, 400, 60):
    draw.line([15, y, 15, y+50], fill='#a0b0c0', width=3)
    draw.rectangle([18, y, 140, y+50], fill=(236, 240, 244, 100))

# 右侧隔断
for y in range(160, 350, 50):
    draw.line([785, y, 785, y+40], fill='#a0b0c0', width=3)

# === 细节增强 ===
# 电源插座
draw.rectangle([765, 540, 775, 550], fill='#2c2c2c', outline='#000', width=1)

# 垃圾桶
draw_iso_box(600, 575, 20, 25, 15, '#4a4a4a', '#2a2a2a')

# 文件柜
draw_iso_box(120, 480, 35, 50, 25, '#7f8c8d', '#5f6c6d')

# 保存图像
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'office_bg.png')
img.save(output_path)
print(f"✓ 等距豪华办公室背景已创建: {output_path}")
print("✓ 风格: Pixel Agents inspired - 等距投影、现代科技风")
print("✓ 包含: 等距地板、立体家具、服务器机柜、照明效果、装饰元素")
