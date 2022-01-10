# 游戏的主要工作都由这里负责
import sys

import pygame


def checkEvents(ship):
    """按键事件响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 必须先判断事件类型，再判断按键，因为有的事件没有按键
        if event.type == pygame.KEYDOWN:
            keyDownEvents(event, ship)
        if event.type == pygame.KEYUP:
            keyUpEvents(event, ship)

# 按键按下响应事件
def keyDownEvents(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    if event.key == pygame.K_LEFT:
        ship.movingLeft = True

# 按键弹起响应事件
def keyUpEvents(event, ship):
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

