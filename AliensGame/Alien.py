# 敌人类
import pygame


from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, setting):
        super(Alien, self).__init__()
        self.screen = screen
        self.setting = setting

        # 加载图片
        self.image = pygame.image.load('D:\\WorkSpace\\PythonCode\\AliensGame\\resources\\alien.bmp')
        self.rect = self.image.get_rect()

        # 位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 精确位置
        self.x = float(self.rect.x)     # self.x是float类型与int型的self.rect.x相加可有小数点后数据

        # 移动速度
        self.speed = setting.alienMoveSpeedHorizontal

    # 绘制外星人
    def drawAlien(self):
        self.screen.blit(self.image, self.rect)

    # 刷新单个外星人位置
    def refreshAlienLocation(self, setting):
        self.x = float(self.rect.x)
        self.x += self.speed * setting.direction
        self.rect.x = self.x

    def checkEdge(self):
        if((self.rect.x + self.rect.width) >= self.setting.screenWidth):
            return True
        elif(self.rect.x <= 0):
            return True
        else:
            return False
