import pygame

import Setting

from pygame.sprite import Sprite

from pygame.sprite import Group

import Ship

import GameFunction

import GameState

import time

def run_game():
    # 创建设置对象
    settings = Setting.Setting()
    # 初始化游戏
    pygame.init()
    # 创建一个窗口对象surface，并设置窗口大小
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    # 设置窗口标题
    pygame.display.set_caption("Alien Invasion")
    # 创建游戏存储实例
    state = GameState.GameState(settings)
    # 创建一个ship对象
    ship = Ship.Ship(screen, settings)
    # 存储所有子弹
    bullets = Group()
    # bullets = []
    # 创建外星人编队
    aliens = Group()
    GameFunction.createAlienSheet(aliens, screen, settings, ship)
    i = 0
    # 游戏主循环
    while True:
        # 每次循环监视事件
        GameFunction.checkEvents(ship, settings, screen, bullets)
        i = i + 1
        print(i)
        if(state.gameActive):
            # 刷新飞船位置
            ship.refreshShipLocation()
            # 刷新子弹位置
            GameFunction.refreshBullets(bullets, aliens)
            # 刷新敌人位置
            GameFunction.refreshAlienSheet(settings, aliens, ship, state, bullets, screen)
            # 重新绘制屏幕、飞船、子弹、敌人
            GameFunction.refreshScreen(settings, screen, ship, bullets, aliens)
            # time.sleep(1 / 60)
        else:
            time.sleep(1)
            state.gameNotActive(state, aliens, bullets, ship, screen)


run_game()

