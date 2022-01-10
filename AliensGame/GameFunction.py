import sys

import pygame


def checkEvents(ship):
    """按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            if event.key == pygame.K_LEFT:
                ship.movingLeft = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            if event.key == pygame.K_LEFT:
                ship.movingLeft = False

def refreshScreen(settings, screen, ship):
    # 填充背景色
    screen.fill(settings.backColor)
    # 刷新飞船
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

