#!/usr/bin/env python3
"""
HappyCapy Office UI - 交互式办公室设计工具
"""

from PIL import Image, ImageDraw
import os

def show_menu():
    print("\n" + "="*60)
    print("🎨 HappyCapy Office UI - 办公室设计工具")
    print("="*60)
    print("\n请选择设计风格：")
    print("1. 现代简约风 (Modern Minimalist)")
    print("2. 科技未来风 (Tech Futuristic)")
    print("3. 温馨舒适风 (Cozy Comfortable)")
    print("4. 豪华商务风 (Luxury Business)")
    print("5. 自定义颜色 (Custom Colors)")
    print("0. 退出")
    print("="*60)

def get_color_scheme(choice):
    """获取配色方案"""
    schemes = {
        '1': {  # 现代简约
            'name': '现代简约风',
            'floor_base': '#e8e8e8',
            'floor_alt': '#f5f5f5',
            'wall_color': '#ffffff',
            'desk_wood': '#d4d4d4',
            'tech_blue': '#4a90e2',
            'plant_green': '#6fcf97',
            'chair_red': '#eb5757',
            'sofa_blue': '#56ccf2'
        },
        '2': {  # 科技未来
            'name': '科技未来风',
            'floor_base': '#1a1a2e',
            'floor_alt': '#16213e',
            'wall_color': '#0f3460',
            'desk_wood': '#533483',
            'tech_blue': '#00d4ff',
            'plant_green': '#00ff88',
            'chair_red': '#ff0080',
            'sofa_blue': '#7000ff'
        },
        '3': {  # 温馨舒适
            'name': '温馨舒适风',
            'floor_base': '#ffeaa7',
            'floor_alt': '#fdcb6e',
            'wall_color': '#fab1a0',
            'desk_wood': '#e17055',
            'tech_blue': '#74b9ff',
            'plant_green': '#55efc4',
            'chair_red': '#ff7675',
            'sofa_blue': '#a29bfe'
        },
        '4': {  # 豪华商务（默认）
            'name': '豪华商务风',
            'floor_base': '#3a3a52',
            'floor_alt': '#45455e',
            'wall_color': '#252538',
            'desk_wood': '#8B6F47',
            'tech_blue': '#4a9eff',
            'plant_green': '#4a9e5f',
            'chair_red': '#c44569',
            'sofa_blue': '#3867d6'
        }
    }
    return schemes.get(choice, schemes['4'])

def custom_colors():
    """自定义颜色"""
    print("\n请输入自定义颜色（十六进制格式，如 #3a3a52）")
    print("按回车使用默认值")

    colors = {}
    defaults = get_color_scheme('4')

    color_names = [
        ('floor_base', '地板主色'),
        ('floor_alt', '地板次色'),
        ('wall_color', '墙壁颜色'),
        ('desk_wood', '桌子颜色'),
        ('tech_blue', '科技蓝色'),
        ('plant_green', '植物绿色'),
        ('chair_red', '椅子红色'),
        ('sofa_blue', '沙发蓝色')
    ]

    for key, name in color_names:
        default = defaults[key]
        value = input(f"{name} (默认: {default}): ").strip()
        colors[key] = value if value else default

    colors['name'] = '自定义风格'
    return colors

def draw_iso_tile(draw, x, y, w, h, color1, color2):
    """绘制等距瓷砖"""
    top = (x, y)
    right = (x + w//2, y + h//2)
    bottom = (x, y + h)
    left = (x - w//2, y + h//2)
    draw.polygon([top, right, bottom, left], fill=color1, outline=color2, width=1)

def draw_iso_box(draw, x, y, w, h, d, top_color, side_color):
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

def create_office(colors, layout='standard'):
    """创建办公室"""
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color=colors['wall_color'])
    draw = ImageDraw.Draw(img)

    print(f"\n🎨 正在生成 {colors['name']}...")

    # 地板
    print("  ✓ 绘制地板...")
    tile_w, tile_h = 60, 30
    for row in range(-2, 15):
        for col in range(-2, 20):
            x = 400 + (col - row) * (tile_w // 2)
            y = 100 + (col + row) * (tile_h // 2)
            if 0 <= x <= 850 and 0 <= y <= 650:
                color = colors['floor_base'] if (row + col) % 2 == 0 else colors['floor_alt']
                draw_iso_tile(draw, x, y, tile_w, tile_h, color, colors['wall_color'])

    # 后墙
    draw.rectangle([0, 0, width, 160], fill=colors['wall_color'])

    # 窗户
    print("  ✓ 添加窗户...")
    for x_pos in [50, 340, 630]:
        draw.rectangle([x_pos, 30, x_pos+120, 130], fill='#1a1a2e', outline='#0f0f1e', width=3)
        draw.rectangle([x_pos+5, 35, x_pos+115, 125], fill='#4a7c9e', outline='#2c5f9a', width=2)
        draw.line([x_pos+60, 35, x_pos+60, 125], fill='#1a1a2e', width=2)
        draw.line([x_pos+5, 80, x_pos+115, 80], fill='#1a1a2e', width=2)

    # 家具
    print("  ✓ 摆放家具...")
    # 办公桌
    draw_iso_box(draw, 180, 360, 100, 40, 60, colors['desk_wood'], colors['desk_wood'])
    # 显示器
    draw_iso_box(draw, 200, 310, 50, 35, 8, colors['tech_blue'], '#1a1a2e')
    draw.rectangle([205, 315, 245, 340], fill=colors['tech_blue'])

    # 沙发
    draw_iso_box(draw, 650, 500, 80, 35, 60, colors['sofa_blue'], colors['sofa_blue'])

    # 会议桌
    draw.ellipse([360, 200, 540, 270], fill=colors['desk_wood'], outline='#4a3d2f', width=3)

    # 植物
    print("  ✓ 添加装饰...")
    for px, py, size in [(40, 440, 35), (170, 420, 20), (760, 540, 25)]:
        draw_iso_box(draw, px, py, size, size, size//2, '#8B4513', '#654321')
        for i in range(3):
            offset_x = -10 + i * 10
            offset_y = -20 - i * 8
            draw.ellipse([px+size//2-8+offset_x, py+offset_y,
                         px+size//2+8+offset_x, py+offset_y+16],
                        fill=colors['plant_green'], outline='#2d5f3a', width=1)

    # 服务器机柜
    draw_iso_box(draw, 690, 190, 45, 90, 25, '#2c3e50', '#1a252f')
    for i in range(5):
        y = 200 + i * 16
        draw.rectangle([695, y, 725, y+12], fill='#34495e', outline='#000', width=1)
        draw.ellipse([700, y+4, 704, y+8], fill='#27ae60')
        draw.ellipse([707, y+4, 711, y+8], fill=colors['tech_blue'])

    # 地毯
    draw.ellipse([200, 380, 350, 450], fill='#8B4B3D', outline='#6d3a2f', width=2)
    draw.ellipse([580, 480, 720, 560], fill='#5a4a6a', outline='#4a3a5a', width=2)

    # 照明
    for x in [250, 500, 700]:
        draw.ellipse([x-12, 155, x+12, 170], fill='#ffd700', outline='#d4af37', width=2)

    return img

def main():
    while True:
        show_menu()
        choice = input("\n请选择 (0-5): ").strip()

        if choice == '0':
            print("\n👋 感谢使用！再见！")
            break

        if choice == '5':
            colors = custom_colors()
        elif choice in ['1', '2', '3', '4']:
            colors = get_color_scheme(choice)
        else:
            print("\n❌ 无效选择，请重试！")
            continue

        # 创建办公室
        img = create_office(colors)

        # 保存
        output_dir = os.path.join(os.path.dirname(__file__), 'frontend')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'office_bg.png')
        img.save(output_path)

        print(f"\n✅ 完成！")
        print(f"📁 保存位置: {output_path}")
        print(f"🎨 风格: {colors['name']}")
        print(f"📏 尺寸: 800 × 600 像素")

        # 显示颜色配置
        print("\n🎨 使用的颜色配置：")
        for key, value in colors.items():
            if key != 'name':
                print(f"  {key}: {value}")

        # 询问是否继续
        continue_choice = input("\n是否继续设计？(y/n): ").strip().lower()
        if continue_choice != 'y':
            print("\n👋 感谢使用！")
            break

if __name__ == "__main__":
    print("\n🎨 欢迎使用 HappyCapy Office UI 设计工具！")
    print("="*60)
    main()
