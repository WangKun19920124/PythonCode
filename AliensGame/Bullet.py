import pygame


from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super().__init__()
        self.rect = pygame.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)    # 创建子弹矩形
        self.rect.centerx = ship.rect.centerx   # 子弹初始位置
        self.rect.bottom = ship.rect.top
        self.floatY = float(self.rect.y)

        # 子弹颜色
        self.color = setting.bulletBackColor
        self.speed = setting.bulletSpeed

        # 窗口
        self.screen = screen
    def refreshBulletLocation(self):
        self.floatY -= self.speed
        self.rect.y = self.floatY

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

