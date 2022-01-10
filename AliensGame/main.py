import sys

import pygame

import Setting

import Ship

import GameFunction

def run_game():
    # 创建设置对象
    settings = Setting.Setting()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个ship对象
    ship = Ship.Ship(screen)
    # 开始游戏的主循环
    while True:
        # 每次循环监视事件
        GameFunction.checkEvents(ship)

        ship.refreshShipLocation()

        ship.blitme()

        GameFunction.refreshScreen(settings, screen, ship)


run_game()

