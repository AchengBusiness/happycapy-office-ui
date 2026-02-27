#!/usr/bin/env python3
"""创建 CAD 风格的办公室平面图"""

from PIL import Image, ImageDraw, ImageFont
import math

# 创建 1200x800 的图像（更大更清晰）
width, height = 1200, 800
img = Image.new('RGB', (width, height), color='#ffffff')
draw = ImageDraw.Draw(img)

# === CAD 风格配色 ===
wall_color = '#2c3e50'          # 深灰色墙体
wall_fill = '#ecf0f1'           # 浅灰填充
floor_color = '#f8f9fa'         # 地板白色
door_color = '#e74c3c'          # 门红色
window_color = '#3498db'        # 窗户蓝色
furniture_color = '#95a5a6'     # 家具灰色
desk_color = '#8e44ad'          # 办公桌紫色
grid_color = '#dee2e6'          # 网格浅灰
text_color = '#2c3e50'          # 文字深灰

# === 绘制网格（CAD 背景）===
grid_size = 40
for x in range(0, width, grid_size):
    draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
for y in range(0, height, grid_size):
    draw.line([(0, y), (width, y)], fill=grid_color, width=1)

# === 外墙 ===
wall_thickness = 20

# 外墙矩形
outer_walls = [
    # 上墙
    (100, 100, width-100, 100+wall_thickness),
    # 下墙
    (100, height-100-wall_thickness, width-100, height-100),
    # 左墙
    (100, 100, 100+wall_thickness, height-100),
    # 右墙
    (width-100-wall_thickness, 100, width-100, height-100)
]

for wall in outer_walls:
    draw.rectangle(wall, fill=wall_color, outline=wall_color)

# === 内部房间分隔 ===
# 工作区分隔墙（左侧）
draw.rectangle([400, 100, 420, 400], fill=wall_color)

# 会议室分隔墙（上方）
draw.rectangle([100, 350, 700, 370], fill=wall_color)

# 服务器机房分隔（右上）
draw.rectangle([width-400, 100, width-380, 350], fill=wall_color)

# === 门 ===
def draw_door(x, y, width, height, orientation='horizontal'):
    """绘制门"""
    if orientation == 'horizontal':
        # 门框
        draw.rectangle([x, y, x+width, y+height], fill=door_color, outline=wall_color, width=2)
        # 门把手
        handle_x = x + width - 10
        draw.circle((handle_x, y+height//2), 3, fill=wall_color)
    else:
        # 竖向门
        draw.rectangle([x, y, x+width, y+height], fill=door_color, outline=wall_color, width=2)
        handle_y = y + height - 10
        draw.circle((x+width//2, handle_y), 3, fill=wall_color)

# 入口门
draw_door(500, 100, 80, wall_thickness, 'horizontal')

# 会议室门
draw_door(400, 350, wall_thickness, 60, 'vertical')

# 机房门
draw_door(width-400, 200, wall_thickness, 60, 'vertical')

# === 窗户 ===
def draw_window(x, y, width, height):
    """绘制窗户"""
    draw.rectangle([x, y, x+width, y+height], fill=window_color, outline=wall_color, width=3)
    # 窗格
    draw.line([x+width//2, y, x+width//2, y+height], fill='#ffffff', width=2)
    draw.line([x, y+height//2, x+width, y+height//2], fill='#ffffff', width=2)

# 左侧窗户
draw_window(100, 200, wall_thickness, 120)
draw_window(100, 400, wall_thickness, 120)

# 上方窗户
draw_window(250, 100, 120, wall_thickness)
draw_window(700, 100, 120, wall_thickness)

# === 家具（俯视图）===
def draw_desk(x, y, w, h, label=''):
    """绘制办公桌"""
    # 桌面
    draw.rectangle([x, y, x+w, y+h], fill=desk_color, outline=wall_color, width=2)
    # 抽屉线条
    draw.line([x+10, y+h//2, x+w-10, y+h//2], fill=wall_color, width=1)
    # 标签
    if label:
        try:
            draw.text((x+w//2-20, y+h//2-5), label, fill='#ffffff')
        except:
            pass

def draw_chair(x, y, size=30):
    """绘制椅子"""
    draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2], fill=furniture_color, outline=wall_color, width=2)

def draw_table(x, y, w, h):
    """绘制桌子"""
    draw.rectangle([x, y, x+w, y+h], fill=furniture_color, outline=wall_color, width=2)

def draw_sofa(x, y, w, h):
    """绘制沙发"""
    draw.rectangle([x, y, x+w, y+h], fill='#e67e22', outline=wall_color, width=2)
    # 靠垫
    cushion_w = w // 3
    for i in range(3):
        cx = x + cushion_w * i + cushion_w // 2
        cy = y + h // 2
        draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill='#d35400')

def draw_plant(x, y, size=25):
    """绘制植物"""
    # 花盆
    draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2], fill='#27ae60', outline='#229954', width=2)
    # 中心
    draw.ellipse([x-5, y-5, x+5, y+5], fill='#229954')

def draw_server_rack(x, y, w, h):
    """绘制服务器机柜"""
    draw.rectangle([x, y, x+w, y+h], fill='#34495e', outline=wall_color, width=2)
    # 服务器层
    for i in range(6):
        sy = y + 10 + i * (h-20) // 6
        draw.rectangle([x+5, sy, x+w-5, sy+8], fill='#2c3e50', outline='#1a252f', width=1)
        # LED
        draw.circle((x+w-15, sy+4), 3, fill='#27ae60')

# === 工作区（左侧）===
# 主办公桌
draw_desk(150, 200, 120, 60, 'WORK')
draw_chair(210, 170)

# 副办公桌
draw_desk(150, 450, 120, 60, 'CODE')
draw_chair(210, 420)

# === 休息区（左下）===
# L型沙发
draw_sofa(150, 550, 150, 60)
draw_sofa(300, 570, 60, 100)

# 茶几
draw_table(220, 620, 70, 50)

# === 会议区（中央）===
# 会议桌（椭圆形）
draw.ellipse([450, 420, 650, 580], fill=furniture_color, outline=wall_color, width=3)

# 会议椅
chair_positions = [
    (500, 400), (550, 395), (600, 400),  # 上方
    (500, 600), (550, 605), (600, 600),  # 下方
    (430, 500), (670, 500)                # 左右
]
for cx, cy in chair_positions:
    draw_chair(cx, cy, 25)

# === 服务器机房（右上）===
# 服务器机柜
draw_server_rack(width-350, 150, 80, 150)
draw_server_rack(width-250, 150, 80, 150)

# 网络设备
draw_table(width-350, 320, 180, 40)

# === 休闲区（右侧）===
# 书架
draw.rectangle([width-180, 400, width-140, 650], fill='#8B4513', outline=wall_color, width=2)
for y in [420, 480, 540, 600]:
    draw.line([width-175, y, width-145, y], fill=wall_color, width=2)

# 装饰植物
plant_positions = [(180, 320), (350, 280), (width-200, 550), (480, 380)]
for px, py in plant_positions:
    draw_plant(px, py)

# === 标注（CAD 风格）===
def draw_label(x, y, text, size=12):
    """绘制标注"""
    try:
        bbox = draw.textbbox((0, 0), text)
        text_width = bbox[2] - bbox[0]
        # 背景
        draw.rectangle([x-5, y-15, x+text_width+5, y+5], fill='#ffffff', outline=text_color, width=1)
        # 文字
        draw.text((x, y-12), text, fill=text_color)
    except:
        pass

# 区域标注
draw_label(210, 160, 'WORK AREA', 14)
draw_label(210, 420, 'DEV ZONE', 14)
draw_label(220, 530, 'LOUNGE', 14)
draw_label(540, 390, 'MEETING', 14)
draw_label(width-300, 120, 'SERVER ROOM', 14)
draw_label(width-180, 370, 'LIBRARY', 14)

# === 图例（右下角）===
legend_x = width - 250
legend_y = height - 180

draw.rectangle([legend_x-10, legend_y-10, legend_x+230, legend_y+160],
               fill='#ffffff', outline=wall_color, width=2)

try:
    draw.text((legend_x, legend_y), 'LEGEND', fill=text_color)

    # 墙体
    draw.rectangle([legend_x, legend_y+20, legend_x+30, legend_y+35], fill=wall_color)
    draw.text((legend_x+40, legend_y+20), 'Wall', fill=text_color)

    # 门
    draw.rectangle([legend_x, legend_y+45, legend_x+30, legend_y+60], fill=door_color)
    draw.text((legend_x+40, legend_y+45), 'Door', fill=text_color)

    # 窗户
    draw.rectangle([legend_x, legend_y+70, legend_x+30, legend_y+85], fill=window_color)
    draw.text((legend_x+40, legend_y+70), 'Window', fill=text_color)

    # 办公桌
    draw.rectangle([legend_x, legend_y+95, legend_x+30, legend_y+110], fill=desk_color)
    draw.text((legend_x+40, legend_y+95), 'Desk', fill=text_color)

    # 家具
    draw.rectangle([legend_x, legend_y+120, legend_x+30, legend_y+135], fill=furniture_color)
    draw.text((legend_x+40, legend_y+120), 'Furniture', fill=text_color)
except:
    pass

# === 标题 ===
try:
    draw.text((width//2-150, 30), 'HAPPYCAPY OFFICE - FLOOR PLAN', fill=text_color)
    draw.text((width//2-100, 55), 'Scale: 1:50  |  CAD View', fill=grid_color)
except:
    pass

# === 坐标系（左下角）===
arrow_x, arrow_y = 50, height - 50
# X轴
draw.line([(arrow_x, arrow_y), (arrow_x+50, arrow_y)], fill=text_color, width=2)
draw.polygon([(arrow_x+50, arrow_y), (arrow_x+45, arrow_y-3), (arrow_x+45, arrow_y+3)], fill=text_color)
try:
    draw.text((arrow_x+55, arrow_y-5), 'X', fill=text_color)
except:
    pass

# Y轴
draw.line([(arrow_x, arrow_y), (arrow_x, arrow_y-50)], fill=text_color, width=2)
draw.polygon([(arrow_x, arrow_y-50), (arrow_x-3, arrow_y-45), (arrow_x+3, arrow_y-45)], fill=text_color)
try:
    draw.text((arrow_x-5, arrow_y-60), 'Y', fill=text_color)
except:
    pass

# 保存
import os
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'office_cad.png')
img.save(output_path)

print(f"✓ CAD 风格办公室平面图已创建: {output_path}")
print(f"✓ 尺寸: {width} × {height} 像素")
print(f"✓ 风格: 建筑平面图 / CAD 俯视图")
print(f"✓ 包含: 工作区、会议室、服务器机房、休息区、图书区")
print(f"✓ 特点: 网格背景、图例、标注、精确布局")
