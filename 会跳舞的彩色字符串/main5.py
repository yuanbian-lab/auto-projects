# -*- coding=utf-8 -*-
# from rich.console import Console
import os
import sys
import time
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

text = "Hello, World! 欢迎来到猿变实验室"
colors = [31, 33, 32, 36, 34, 35]  # 红黄绿青蓝紫（循环使用）
amplitude = 4                     # 波浪幅度
speed = 0.2                       # 波动速度
width = 20                        # 起始列位置
# console = Console()
try:
    t = 0
    for i in range(100000):
        clear()
        # console.clear()
        for i, char in enumerate(text):
            y = int(10 + math.sin(t + i * 0.5) * amplitude)  # 波浪效果
            x = width + i
            color = colors[i % len(colors)]
            # 输出字符到指定位置并加颜色
            sys.stdout.write(f"\033[{y};{x}H\033[{color}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
        t += 0.3
except KeyboardInterrupt:
    print("\033[0m\n退出动画")
