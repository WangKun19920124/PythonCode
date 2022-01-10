import pygame


class Ship:
    """初始化飞船并设置初始位置"""
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('D:\\WorkSpace\\PythonCode\\AliensGame\\resources\\ship.bmp')
        self.rect = self.image.get_rect()

        self.screenRect = screen.get_rect()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        self.movingRight = False
        self.movingLeft = False

    # 刷新飞船位置
    def refreshShipLocation(self):
        if self.movingLeft == True:
            if(self.rect.x > 0):
                self.rect.x -= 1
            else:
                self.rect.x = 0
        if self.movingRight == True:
            if(self.rect.x < self.screenRect.width - self.rect.width):
                self.rect.x += 1
            else:
                self.rect.x = (self.screenRect.width - self.rect.width)

    # 绘制飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)




