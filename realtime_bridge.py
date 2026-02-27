#!/usr/bin/env python3
"""
实时状态桥接系统
连接 Claude 的实际工作状态到 UI
"""

import json
import time
from datetime import datetime
from pathlib import Path

class RealtimeStateBridge:
    def __init__(self, state_file='state.json'):
        self.state_file = Path(__file__).parent / state_file
        self.activity_log = []

    def update_activity(self, action, detail, state='working'):
        """更新当前活动"""
        timestamp = datetime.now().isoformat()

        # 状态映射
        state_map = {
            'reading': 'researching',
            'writing': 'writing',
            'running': 'executing',
            'thinking': 'idle',
            'searching': 'researching',
            'editing': 'writing',
            'creating': 'writing',
            'testing': 'executing',
            'debugging': 'executing',
            'analyzing': 'researching'
        }

        mapped_state = state_map.get(action.lower(), 'idle')

        # 更新状态文件
        state_data = {
            'state': mapped_state,
            'detail': detail,
            'action': action,
            'progress': 0,
            'updated_at': timestamp
        }

        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(state_data, f, indent=2, ensure_ascii=False)

        # 记录活动日志
        self.activity_log.append({
            'timestamp': timestamp,
            'action': action,
            'detail': detail
        })

        print(f"✓ 状态更新: [{mapped_state}] {action} - {detail}")

    def get_current_state(self):
        """获取当前状态"""
        if not self.state_file.exists():
            return None

        with open(self.state_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def log_tool_use(self, tool_name, description):
        """记录工具使用"""
        action_map = {
            'Read': 'reading',
            'Write': 'writing',
            'Edit': 'editing',
            'Bash': 'running',
            'Grep': 'searching',
            'Glob': 'searching',
            'Task': 'thinking'
        }

        action = action_map.get(tool_name, 'working')
        self.update_activity(action, f"{tool_name}: {description}")

# 全局实例
bridge = RealtimeStateBridge()

# === 工具钩子（示例）===
def on_tool_use(tool_name, params):
    """工具使用钩子"""
    descriptions = {
        'Read': f"正在读取文件...",
        'Write': f"正在创建文件...",
        'Edit': f"正在编辑代码...",
        'Bash': f"正在执行命令...",
        'Grep': f"正在搜索内容...",
        'Glob': f"正在查找文件...",
    }

    desc = descriptions.get(tool_name, f"正在使用 {tool_name}...")
    bridge.log_tool_use(tool_name, desc)

# === 使用示例 ===
if __name__ == '__main__':
    # 模拟工作流程
    print("\n🔄 实时状态桥接系统测试\n")

    bridge.update_activity('reading', '正在阅读项目文档...')
    time.sleep(2)

    bridge.update_activity('writing', '正在编写代码...')
    time.sleep(2)

    bridge.update_activity('running', '正在执行测试...')
    time.sleep(2)

    bridge.update_activity('thinking', '任务完成，待命中...')

    print("\n✓ 测试完成")
    print(f"✓ 活动日志: {len(bridge.activity_log)} 条记录")
