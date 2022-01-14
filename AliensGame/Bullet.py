# 子弹类
import pygame

from pygame.sprite import Sprite

import GameFunction


class Bullet(Sprite):
    """子弹"""
    def __init__(self, setting, screen, ship):
        super().__init__()
        self.rect = pygame.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)    # 创建子弹矩形
        self.rect.centerx = ship.rect.centerx   # 子弹初始位置
        self.rect.bottom = ship.rect.top
        self.floatY = float(self.rect.y)
        self.setting = setting
        self.ship = ship

        # 子弹颜色
        self.color = setting.bulletBackColor
        self.speed = setting.bulletSpeed

        # 窗口
        self.screen = screen

    # 绘制子弹
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    # 刷新子弹位置
    def refreshBulletLocation(self, aliens, bullets):
        self.floatY -= self.speed
        self.rect.y = self.floatY
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if len(aliens) == 0:
            bullets.empty()
            GameFunction.createAlienSheet(aliens, self.screen, self.setting, self.ship)



