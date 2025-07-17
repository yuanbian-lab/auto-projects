# -*- coding=utf-8 -*-
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设定窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# 定义烟花的颜色，这里使用随机颜色
firework_colors = [
    (255, 255, 255),  # 白色
    (255, 0, 0),  # 红色
    (0, 255, 0),  # 绿色
    (0, 0, 255),  # 蓝色
    (255, 255, 0),  # 黄色
    (255, 0, 255),  # 紫色
    (0, 255, 255)  # 青色
]

# 定义烟花的粒子数量
num_particles = 100

# 定义烟花粒子的最大速度和加速度
max_speed = 2
max_acceleration = 0.1


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.uniform(-max_speed, max_speed)
        self.speed_y = random.uniform(-max_speed, max_speed)
        self.acceleration_x = random.uniform(-max_acceleration, max_acceleration)
        self.acceleration_y = random.uniform(-max_acceleration, max_acceleration)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x += self.acceleration_x
        self.speed_y += self.acceleration_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 2)


# 创建烟花粒子列表
particles = []

# 主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 更新和绘制烟花粒子
    for particle in particles:
        particle.update()
        particle.draw()

    # 创建新的烟花
    if len(particles) == 0 or random.random() < 0.01:
        x = random.randint(0, width)
        y = random.randint(int(height * 0.75), height)
        color = random.choice(firework_colors)
        particles.extend([Particle(x, y, color) for _ in range(num_particles)])

    # 更新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()