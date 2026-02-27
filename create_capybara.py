#!/usr/bin/env python3
"""创建更清晰的水豚角色"""

from PIL import Image, ImageDraw

# 创建64x64的水豚图片（更大更清晰）
size = 64
img_open = Image.new('RGBA', (size, size), (0, 0, 0, 0))
img_closed = Image.new('RGBA', (size, size), (0, 0, 0, 0))

draw_open = ImageDraw.Draw(img_open)
draw_closed = ImageDraw.Draw(img_closed)

# 颜色方案 - 更深更饱和
body_main = '#8B6914'      # 深棕黄色身体
body_dark = '#6B4F0A'      # 阴影
body_light = '#A6822A'     # 高光
nose_color = '#4A3A2A'     # 深棕色鼻子
eye_color = '#1A1A1A'      # 黑色眼睛
outline = '#3D2D1D'        # 深色轮廓

def draw_capybara(draw, eyes_open=True):
    # 轮廓（增加可见度）
    draw.ellipse([4, 18, 60, 60], fill=outline)

    # 身体（椭圆形）
    draw.ellipse([6, 20, 58, 58], fill=body_main)

    # 身体阴影
    draw.ellipse([6, 40, 58, 58], fill=body_dark)

    # 身体高光
    draw.ellipse([12, 22, 52, 45], fill=body_light)

    # 头部轮廓
    draw.ellipse([10, 4, 54, 42], fill=outline)

    # 头部
    draw.ellipse([12, 6, 52, 40], fill=body_main)

    # 头部高光
    draw.ellipse([16, 8, 48, 30], fill=body_light)

    # 耳朵（左）
    draw.ellipse([8, 8, 20, 18], fill=outline)
    draw.ellipse([10, 10, 18, 16], fill=body_main)

    # 耳朵（右）
    draw.ellipse([44, 8, 56, 18], fill=outline)
    draw.ellipse([46, 10, 54, 16], fill=body_main)

    # 鼻子/口鼻部（突出）
    draw.ellipse([20, 24, 44, 40], fill=body_light)
    draw.ellipse([24, 32, 40, 42], fill='#C4A262')  # 浅色嘴部

    # 鼻子
    draw.ellipse([28, 26, 36, 33], fill=nose_color)
    draw.ellipse([29, 27, 35, 31], fill='#2A2016')  # 鼻孔

    # 眼睛
    if eyes_open:
        # 眼白
        draw.ellipse([16, 16, 26, 26], fill='#FFFFFF')
        draw.ellipse([38, 16, 48, 26], fill='#FFFFFF')
        # 眼珠
        draw.ellipse([18, 18, 25, 25], fill=eye_color)
        draw.ellipse([40, 18, 47, 25], fill=eye_color)
        # 眼睛高光
        draw.ellipse([19, 19, 22, 22], fill='#FFFFFF')
        draw.ellipse([41, 19, 44, 22], fill='#FFFFFF')
    else:
        # 闭眼 - 弧线
        draw.arc([16, 18, 26, 26], 0, 180, fill=eye_color, width=2)
        draw.arc([38, 18, 48, 26], 0, 180, fill=eye_color, width=2)

    # 腿（前）
    draw.ellipse([14, 50, 24, 62], fill=outline)
    draw.ellipse([15, 51, 23, 61], fill=body_dark)
    draw.ellipse([40, 50, 50, 62], fill=outline)
    draw.ellipse([41, 51, 49, 61], fill=body_dark)

# 绘制睁眼版本
draw_capybara(draw_open, eyes_open=True)

# 绘制闭眼版本
draw_capybara(draw_closed, eyes_open=False)

# 保存
output_dir = '/home/node/a0/workspace/94c5d81a-d2d5-4673-afd3-7ae21cd608cb/workspace/happycapy-office-ui/frontend'
img_open.save(f'{output_dir}/capybara_open.png')
img_closed.save(f'{output_dir}/capybara_closed.png')

print("✓ 水豚图片已更新（64x64，颜色更深）")
print(f"  - {output_dir}/capybara_open.png")
print(f"  - {output_dir}/capybara_closed.png")
