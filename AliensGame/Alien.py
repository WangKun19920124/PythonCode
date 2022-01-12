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
        self.x = float(self.rect.x)

    # 绘制外星人
    def drawAlien(self):
        self.screen.blit(self.image, self.rect)
