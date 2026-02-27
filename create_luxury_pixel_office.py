#!/usr/bin/env python3
"""
创建豪华像素风格办公室 - 游戏风格 + CAD 平面图布局
"""

from PIL import Image, ImageDraw
import os

# 画布尺寸
width, height = 800, 600
img = Image.new('RGB', (width, height), color='#1a1a2e')
draw = ImageDraw.Draw(img)

# === 豪华配色方案 ===
# 地板
floor_main = '#2d2d44'
floor_accent = '#3d3d5c'
floor_highlight = '#4a4a6a'

# 墙壁
wall_main = '#1a1a2e'
wall_accent = '#252542'

# 木材（豪华深木色）
wood_dark = '#4a3728'
wood_main = '#6b4c3a'
wood_light = '#8b6b4c'

# 金属/科技
metal_dark = '#2c3e50'
metal_main = '#34495e'
tech_blue = '#3498db'
tech_green = '#2ecc71'

# 软装
fabric_navy = '#2c3e6e'
fabric_gold = '#d4a853'
leather_brown = '#8b5a2b'

# 装饰
plant_green = '#27ae60'
light_warm = '#f4d03f'
glass_blue = '#5dade2'

# === 绘制豪华木地板 ===
# 人字形木地板图案
plank_w, plank_h = 40, 15
for row in range(height // plank_h + 1):
    for col in range(width // plank_w + 1):
        x = col * plank_w
        y = row * plank_h
        # 交替方向
        if (row + col) % 2 == 0:
            color = wood_main if (col % 3 != 0) else wood_light
        else:
            color = wood_dark if (col % 3 != 0) else wood_main
        draw.rectangle([x, y, x+plank_w-1, y+plank_h-1], fill=color)
        # 木纹线条
        draw.line([x+2, y+plank_h//2, x+plank_w-3, y+plank_h//2], fill=wood_dark, width=1)

# === 墙壁（上方深色区域）===
wall_height = 100
draw.rectangle([0, 0, width, wall_height], fill=wall_main)
# 墙裙
draw.rectangle([0, wall_height-15, width, wall_height], fill=wall_accent)

# === 豪华大窗户 ===
def draw_luxury_window(x, y, w, h):
    """绘制豪华落地窗"""
    # 窗框（金色）
    draw.rectangle([x-3, y-3, x+w+3, y+h+3], fill=fabric_gold)
    # 玻璃
    draw.rectangle([x, y, x+w, y+h], fill=glass_blue)
    # 窗格（十字形）
    draw.line([x+w//2, y, x+w//2, y+h], fill=fabric_gold, width=3)
    draw.line([x, y+h//2, x+w, y+h//2], fill=fabric_gold, width=3)
    # 反光效果
    draw.line([x+5, y+5, x+15, y+5], fill='#ffffff', width=2)
    draw.line([x+5, y+5, x+5, y+15], fill='#ffffff', width=2)

# 三个大窗户
draw_luxury_window(80, 15, 100, 70)
draw_luxury_window(350, 15, 100, 70)
draw_luxury_window(620, 15, 100, 70)

# === 房间分区线（地面标记）===
def draw_area_border(x1, y1, x2, y2, color='#d4a853'):
    """绘制区域边界"""
    # 虚线边框
    dash_len = 8
    for i in range(0, x2-x1, dash_len*2):
        draw.line([x1+i, y1, min(x1+i+dash_len, x2), y1], fill=color, width=2)
        draw.line([x1+i, y2, min(x1+i+dash_len, x2), y2], fill=color, width=2)
    for i in range(0, y2-y1, dash_len*2):
        draw.line([x1, y1+i, x1, min(y1+i+dash_len, y2)], fill=color, width=2)
        draw.line([x2, y1+i, x2, min(y1+i+dash_len, y2)], fill=color, width=2)

# 工作区边界
draw_area_border(30, 130, 280, 350)
# 休息区边界
draw_area_border(30, 380, 280, 570)
# 会议区边界
draw_area_border(310, 200, 550, 450)
# 服务器区边界
draw_area_border(580, 130, 770, 320)
# 图书区边界
draw_area_border(580, 350, 770, 570)

# === 豪华 CEO 办公桌（左上）===
def draw_executive_desk(x, y):
    """绘制行政级办公桌"""
    # 大桌面（深木色，L型）
    draw.rectangle([x, y, x+150, y+70], fill=wood_dark, outline=wood_light, width=2)
    draw.rectangle([x+120, y+50, x+150, y+120], fill=wood_dark, outline=wood_light, width=2)
    # 桌面装饰线
    draw.rectangle([x+5, y+5, x+145, y+65], fill=wood_main)
    # 显示器
    draw.rectangle([x+20, y+15, x+80, y+50], fill=metal_dark, outline=metal_main, width=2)
    draw.rectangle([x+25, y+20, x+75, y+45], fill=tech_blue)
    # 显示器支架
    draw.rectangle([x+45, y+50, x+55, y+60], fill=metal_main)
    # 键盘
    draw.rectangle([x+85, y+35, x+130, y+55], fill='#cccccc', outline=metal_main, width=1)
    # 鼠标
    draw.ellipse([x+135, y+40, x+145, y+52], fill='#333333')
    # 台灯（金色）
    draw.rectangle([x+10, y+52, x+18, y+65], fill=fabric_gold)
    draw.ellipse([x+5, y+45, x+23, y+55], fill=light_warm)
    # 皮质办公椅
    draw.ellipse([x+70, y+75, x+110, y+115], fill=leather_brown, outline=wood_dark, width=2)

draw_executive_desk(50, 160)

# === 豪华休息区（左下）===
def draw_lounge_area(x, y):
    """绘制豪华休息区"""
    # 真皮沙发（深棕色，三人座）
    draw.rectangle([x, y, x+160, y+50], fill=leather_brown, outline=wood_dark, width=2)
    # 沙发靠背
    draw.rectangle([x, y-15, x+160, y], fill=wood_dark)
    # 沙发坐垫分隔
    draw.line([x+53, y, x+53, y+50], fill=wood_dark, width=2)
    draw.line([x+107, y, x+107, y+50], fill=wood_dark, width=2)
    # 扶手
    draw.rectangle([x-10, y-15, x, y+50], fill=wood_dark)
    draw.rectangle([x+160, y-15, x+170, y+50], fill=wood_dark)

    # 大理石茶几
    draw.rectangle([x+30, y+70, x+130, y+110], fill='#ecf0f1', outline='#bdc3c7', width=2)
    # 茶几装饰
    draw.ellipse([x+70, y+80, x+90, y+100], fill=fabric_gold)  # 装饰品

    # 单人沙发椅
    draw.ellipse([x+180, y+10, x+230, y+60], fill=fabric_navy, outline=wood_dark, width=2)

draw_lounge_area(40, 440)

# === 会议室（中央）===
def draw_meeting_room(x, y):
    """绘制豪华会议室"""
    # 椭圆形会议桌（深木色）
    draw.ellipse([x, y, x+180, y+120], fill=wood_dark, outline=fabric_gold, width=3)
    draw.ellipse([x+10, y+10, x+170, y+110], fill=wood_main)

    # 会议椅（围绕桌子）
    chair_positions = [
        (x+90, y-20),    # 上方中间
        (x+40, y-10),    # 左上
        (x+140, y-10),   # 右上
        (x+90, y+140),   # 下方中间
        (x+40, y+130),   # 左下
        (x+140, y+130),  # 右下
        (x-25, y+60),    # 左侧
        (x+205, y+60),   # 右侧
    ]
    for cx, cy in chair_positions:
        draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=leather_brown, outline=wood_dark, width=2)

    # 投影仪
    draw.rectangle([x+80, y+50, x+100, y+70], fill=metal_main)
    draw.ellipse([x+85, y+55, x+95, y+65], fill=tech_blue)

draw_meeting_room(320, 240)

# === 服务器机房（右上）===
def draw_server_room(x, y):
    """绘制服务器机房"""
    # 机柜1
    draw.rectangle([x, y, x+60, y+130], fill=metal_dark, outline=metal_main, width=2)
    # 服务器层
    for i in range(7):
        sy = y + 10 + i * 17
        draw.rectangle([x+5, sy, x+55, sy+12], fill=metal_main)
        # LED指示灯
        draw.ellipse([x+8, sy+3, x+14, sy+9], fill=tech_green)
        draw.ellipse([x+18, sy+3, x+24, sy+9], fill=tech_green)
        draw.ellipse([x+28, sy+3, x+34, sy+9], fill=tech_blue)

    # 机柜2
    draw.rectangle([x+80, y, x+140, y+130], fill=metal_dark, outline=metal_main, width=2)
    for i in range(7):
        sy = y + 10 + i * 17
        draw.rectangle([x+85, sy, x+135, sy+12], fill=metal_main)
        draw.ellipse([x+88, sy+3, x+94, sy+9], fill=tech_green)
        draw.ellipse([x+98, sy+3, x+104, sy+9], fill=tech_blue)

    # 网络设备架
    draw.rectangle([x+20, y+145, x+120, y+170], fill=metal_main, outline=metal_dark, width=2)
    # 闪烁的网络灯
    for i in range(8):
        draw.ellipse([x+30+i*10, y+152, x+36+i*10, y+158], fill=tech_green if i%2==0 else tech_blue)

draw_server_room(595, 145)

# === 图书区（右下）===
def draw_library_area(x, y):
    """绘制图书区"""
    # 书架（三层）
    draw.rectangle([x, y, x+150, y+140], fill=wood_dark, outline=wood_light, width=2)
    # 层板
    for i in range(3):
        shelf_y = y + 15 + i * 45
        draw.line([x+5, shelf_y, x+145, shelf_y], fill=wood_light, width=3)
        # 书籍
        book_colors = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f', '#9b59b6', '#e67e22', '#1abc9c']
        book_x = x + 10
        for j, color in enumerate(book_colors):
            book_w = 12 + (j % 3) * 3
            draw.rectangle([book_x, shelf_y-35, book_x+book_w, shelf_y-2], fill=color, outline='#2c3e50', width=1)
            book_x += book_w + 2

    # 阅读椅
    draw.ellipse([x+30, y+160, x+80, y+210], fill=fabric_navy, outline=wood_dark, width=2)

    # 阅读灯
    draw.rectangle([x+130, y+150, x+138, y+180], fill=metal_main)
    draw.ellipse([x+120, y+140, x+148, y+155], fill=light_warm)

draw_library_area(595, 365)

# === 装饰植物 ===
def draw_plant(x, y, size='medium'):
    """绘制装饰植物"""
    if size == 'large':
        # 大型龙血树
        draw.rectangle([x-8, y+20, x+8, y+40], fill=wood_dark)  # 花盆
        for i in range(-3, 4):
            draw.ellipse([x-20+i*5, y-20+abs(i)*3, x+20+i*5, y+10-abs(i)*5],
                        fill=plant_green, outline='#229954', width=1)
    else:
        # 小盆栽
        draw.rectangle([x-5, y+10, x+5, y+20], fill=wood_dark)
        draw.ellipse([x-12, y-10, x+12, y+10], fill=plant_green, outline='#229954', width=1)

# 放置植物
draw_plant(280, 150, 'large')
draw_plant(570, 130, 'medium')
draw_plant(300, 520, 'medium')
draw_plant(560, 540, 'large')

# === 地毯（豪华波斯风格）===
def draw_rug(x, y, w, h):
    """绘制豪华地毯"""
    # 地毯主体（深红色）
    draw.rectangle([x, y, x+w, y+h], fill='#8B0000', outline=fabric_gold, width=3)
    # 花纹边框
    draw.rectangle([x+5, y+5, x+w-5, y+h-5], outline='#d4a853', width=2)
    draw.rectangle([x+10, y+10, x+w-10, y+h-10], outline='#b8860b', width=1)
    # 中心图案
    cx, cy = x + w//2, y + h//2
    draw.ellipse([cx-20, cy-15, cx+20, cy+15], fill='#d4a853', outline='#b8860b', width=1)

# 办公区地毯
draw_rug(45, 240, 180, 80)
# 休息区地毯
draw_rug(45, 480, 200, 60)

# === 吊灯 ===
def draw_chandelier(x, y):
    """绘制水晶吊灯"""
    # 灯座
    draw.rectangle([x-5, y-10, x+5, y], fill=fabric_gold)
    # 灯罩
    draw.polygon([(x-20, y), (x+20, y), (x+15, y+15), (x-15, y+15)], fill=light_warm, outline=fabric_gold, width=1)
    # 光晕
    draw.ellipse([x-30, y-5, x+30, y+25], outline='#fff9e6', width=1)

draw_chandelier(150, 105)
draw_chandelier(420, 105)
draw_chandelier(680, 105)

# === 区域标签 ===
# 使用简单的矩形标签代替文字
def draw_label_box(x, y, w, h, color):
    """绘制区域标签"""
    draw.rectangle([x, y, x+w, y+h], fill=color, outline='#ffffff', width=1)

# 工作区标签
draw_label_box(35, 135, 60, 15, '#8e44ad')
# 休息区标签
draw_label_box(35, 385, 60, 15, '#e67e22')
# 会议区标签
draw_label_box(315, 205, 60, 15, '#27ae60')
# 服务器标签
draw_label_box(585, 135, 60, 15, '#3498db')
# 图书区标签
draw_label_box(585, 355, 60, 15, '#9b59b6')

# 保存
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'office_bg.png')
img.save(output_path)

print(f"✓ 豪华像素办公室已创建: {output_path}")
print(f"✓ 尺寸: {width} × {height} 像素")
print(f"✓ 风格: 游戏像素 + CAD平面图布局")
print(f"✓ 特点: 豪华CEO办公桌、真皮沙发、会议室、服务器机房、图书区")
print(f"✓ 配色: 深木色调、金色点缀、专业科技感")
