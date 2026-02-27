#!/usr/bin/env python3
"""创建完整的全身水豚角色精灵图"""

from PIL import Image, ImageDraw
import os

def create_capybara_sprite(filename, eyes_open=True):
    """创建一个水豚精灵图"""
    # 创建 48x48 的图像（更大以容纳完整身体）
    img = Image.new('RGBA', (48, 48), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 颜色定义
    body_brown = (160, 130, 109)      # 主体棕色
    dark_brown = (139, 111, 71)       # 深棕色（耳朵、腿）
    light_brown = (180, 150, 120)     # 浅棕色（肚子）
    nose_brown = (106, 70, 43)        # 鼻子
    eye_white = (255, 255, 255)       # 眼白
    eye_black = (0, 0, 0)             # 瞳孔

    # === 身体（椭圆形）===
    # 主体
    draw.ellipse([10, 18, 38, 40], fill=body_brown, outline=dark_brown, width=1)

    # 肚子（浅色）
    draw.ellipse([14, 22, 34, 38], fill=light_brown)

    # === 头部 ===
    # 头部椭圆
    draw.ellipse([12, 8, 36, 24], fill=body_brown, outline=dark_brown, width=1)

    # 耳朵（左右两个小半圆）
    draw.ellipse([10, 10, 16, 16], fill=dark_brown)
    draw.ellipse([32, 10, 38, 16], fill=dark_brown)

    # === 脸部特征 ===
    if eyes_open:
        # 眼睛 - 睁开
        # 左眼
        draw.ellipse([16, 14, 20, 18], fill=eye_white)
        draw.ellipse([17, 15, 19, 17], fill=eye_black)
        # 右眼
        draw.ellipse([28, 14, 32, 18], fill=eye_white)
        draw.ellipse([29, 15, 31, 17], fill=eye_black)
    else:
        # 眼睛 - 闭合
        draw.line([16, 16, 20, 16], fill=eye_black, width=1)
        draw.line([28, 16, 32, 16], fill=eye_black, width=1)

    # 鼻子（小椭圆）
    draw.ellipse([22, 19, 26, 22], fill=nose_brown)

    # 嘴巴（微笑的弧线）
    draw.arc([20, 19, 28, 24], 0, 180, fill=dark_brown, width=1)

    # === 四肢 ===
    # 前腿（左）
    draw.ellipse([12, 34, 18, 42], fill=dark_brown)
    # 前腿（右）
    draw.ellipse([30, 34, 36, 42], fill=dark_brown)
    # 后腿（左，部分可见）
    draw.ellipse([10, 36, 15, 42], fill=dark_brown)
    # 后腿（右，部分可见）
    draw.ellipse([33, 36, 38, 42], fill=dark_brown)

    # 脚掌（小爪子）
    # 左前脚
    draw.ellipse([13, 40, 17, 43], fill=(80, 60, 40))
    # 右前脚
    draw.ellipse([31, 40, 35, 43], fill=(80, 60, 40))

    # === 尾巴（小小的）===
    draw.ellipse([36, 32, 40, 36], fill=dark_brown)

    # 添加高光（让角色更立体）
    # 头部高光
    draw.ellipse([20, 10, 24, 13], fill=(200, 170, 140, 100))
    # 身体高光
    draw.ellipse([18, 20, 28, 26], fill=(200, 170, 140, 80))

    return img

def create_capybara_walking_frames():
    """创建水豚行走动画帧"""
    frames = []

    # 基础帧 - 站立
    base = create_capybara_sprite("base", eyes_open=True)
    frames.append(base)

    # 行走帧1 - 左腿前
    walk1 = create_capybara_sprite("walk1", eyes_open=True)
    frames.append(walk1)

    # 行走帧2 - 右腿前
    walk2 = create_capybara_sprite("walk2", eyes_open=True)
    frames.append(walk2)

    # 眨眼帧
    blink = create_capybara_sprite("blink", eyes_open=False)
    frames.append(blink)

    return frames

# 保存精灵图
output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
os.makedirs(output_dir, exist_ok=True)

# 创建睁眼版本
capy_open = create_capybara_sprite("open", eyes_open=True)
capy_open.save(os.path.join(output_dir, 'capybara_open.png'))
print(f"✓ 睁眼水豚已创建: {output_dir}/capybara_open.png")

# 创建闭眼版本
capy_closed = create_capybara_sprite("closed", eyes_open=False)
capy_closed.save(os.path.join(output_dir, 'capybara_closed.png'))
print(f"✓ 闭眼水豚已创建: {output_dir}/capybara_closed.png")

print("✓ 完整全身水豚角色创建完成！")
print("特点: 完整身体、四肢、耳朵、尾巴、表情")
