import pygame
import sys
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1600, 900))

# Регестрация цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # Список всех зарегестрированных цветов


def new_ball():
    """Рисуем новый шарик"""
    global x, y, r, i, j, color, x1, y1, circ
    x = 600    #randint(100, 1400)
    y = 300    #randint(100, 500)
    r = randint(30, 50)
    x1 = 50
    y1 = 50
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    circle(screen, color, (x, y), r).move_ip(500, 0)


def click():
    circle(screen, color, (x1, y1), r).move_ip(0, 300)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
s = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Событие поднятия левой клавиши мыши

            #(circle(screen, color, (x, y), r)).move(500, 0)
            #click()

            if event.button == 1:
                i, j = event.pos
                # print("Координаты тычка мышкой:", i, j)
                if ((i - x) ** 2 + (j - y) ** 2) <= r ** 2:  # Проверка на попадание
                    print("Попал")
                    s += 1
                    print("Количество попаданий:", s)

                else:
                    print("Мимо")

new_ball()
print("Координаты шарика", x, y)
    # screen.fill((0, 0, 0))
    # pygame.draw.circle(screen, color, (x, y), r)
pygame.display.update()
screen.fill(BLACK)

pygame.quit()
sys.exit()
