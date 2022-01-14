# 飞船类
import pygame


class Ship:
    """初始化飞船并设置初始位置"""
    def __init__(self, screen, setting):
        self.screen = screen

        self.image = pygame.image.load('D:\\WorkSpace\\PythonCode\\AliensGame\\resources\\ship.bmp')
        self.rect = self.image.get_rect()

        self.screenRect = screen.get_rect()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        self.movingRight = False
        self.movingLeft = False

        self.setting = setting

    # 绘制飞船
    def drawShip(self):
        self.screen.blit(self.image, self.rect)

    # 刷新飞船位置
    def refreshShipLocation(self):
        if self.movingLeft == True:
            if(self.rect.x > 0):
                self.rect.x -= self.setting.shipSpeed
            else:
                self.rect.x = 0
        if self.movingRight == True:
            if(self.rect.x < self.screenRect.width - self.rect.width):
                self.rect.x += self.setting.shipSpeed
            else:
                self.rect.x = (self.screenRect.width - self.rect.width)

    # 飞船位置重新在屏幕中心
    def centerShip(self):
        self.rect.centerx = self.screenRect.centerx




