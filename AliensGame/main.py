import sys

import pygame

import Setting

import Ship

import GameFunction

def run_game():
    # 创建设置对象
    settings = Setting.Setting()
    # 初始化游戏
    pygame.init()
    # 创建一个窗口对象surface，并设置窗口大小
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    # 设置窗口标题
    pygame.display.set_caption("Alien Invasion")

    # 创建一个ship对象
    ship = Ship.Ship(screen, settings)
    # 开始游戏的主循环
    while True:
        # 每次循环监视事件
        GameFunction.checkEvents(ship)

        # 刷新飞船位置
        ship.refreshShipLocation()

        # 重绘飞船
        ship.blitme()

        # 重绘屏幕
        GameFunction.refreshScreen(settings, screen, ship)


run_game()

