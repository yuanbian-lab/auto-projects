# -*- coding=utf-8 -*-
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设定窗口大小
width, height = 1863//3, 2490//3
screen = pygame.display.set_mode((width, height))
image = pygame.image.load("start.png")
image = pygame.transform.scale(image, (width, height))
screen.blit(image, (0, 0))
pygame.display.flip()
# 定义烟花的颜色，这里使用随机颜色
colors = [(255, 255, 255), (255, 255, 0), (255, 255, 255),
          (255, 0, 0), (255, 255, 255), (255, 255, 0),
          (0, 255, 255), (255, 0, 255)
          ]



# 定义烟花粒子的类
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 2
        self.vel_x = random.randint(-5, 5)/1.5
        # if self.vel_x == 0:
        #     self.vel_x = random.randint(-5, 5) / 1.5
        self.vel_y = random.randint(-15, -5)/1.5
        self.gravity = random.randint(1, 3)/30
        self.alpha = random.randint(180, 255)

    def update(self):
        self.vel_y += self.gravity
        self.x += self.vel_x + random.randint(-1, 1) /10
        self.y += self.vel_y
        self.alpha -= 3

    def draw(self):
        try:
            pygame.draw.circle(screen, self.color ,
                               (int(self.x), int(self.y)),
                               self.radius)
        except:
            print(self.color, self.alpha)



def start_play():
    # 创建烟花粒子并添加到列表中
    for _ in range(100):
        particle = Particle(300, 600, random.choice(colors))
        particles.append(particle)
    for particle in particles:
        particle.update()
        particle.draw()
        if particle.alpha <= 0:
            particles.remove(particle)


def draw_text():
    # 设置文字字体和大小
    font = pygame.font.Font(None, 72)
    # 设置文字内容和颜色
    text = font.render("Happy New Year To You", True, (255, 255, 255))
    # 获取文字的矩形对象
    text_rect = text.get_rect()
    # 设置文字的位置
    text_rect.center = (width // 2, 700)
    # 在窗口上绘制文字
    screen.blit(text, text_rect)

def draw_bg():
    image = pygame.image.load("baozhu.png")
    image = pygame.transform.scale(image, (600, 1080))
    screen.blit(image, (0, 0))
# 存储烟花粒子的列表
particles = []

# 游戏主循环
running = True
start = False
while running:
    # screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0, 0, 0))

            start = True
    if start:
        screen.fill((0, 0, 0))
        draw_bg()
        draw_text()
        start_play()
    pygame.display.flip()

# 退出程序
pygame.quit()