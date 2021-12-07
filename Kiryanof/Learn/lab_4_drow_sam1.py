import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400)) # Размер монтажной области

rect(screen, (192, 192, 192), (0 , 0, 400, 400))
#Заливка лица и контур
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 2)
#Левый глаз
circle(screen, (255, 0, 0), (120, 120), 30)
circle(screen, (0, 0, 0), (120, 120), 30, 5)
circle(screen, (0, 0, 0), (120, 120), 7)

#Правый глаз

circle(screen, (255, 0, 0), (280, 120), 20)
circle(screen, (0, 0, 0), (280, 120), 20, 3)
circle(screen, (0, 0, 0), (280, 120), 5)

#Брови

polygon(screen, (0, 0, 0), [(70,70), (85,85),
                               (160,100), (160,80)])

polygon(screen, (0, 0, 0), [(330,70), (315,85),
                               (240,115), (240,100)])

polygon(screen, (0, 0, 0), [(150,230), (280,230),
                               (280,250), (150,250)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()