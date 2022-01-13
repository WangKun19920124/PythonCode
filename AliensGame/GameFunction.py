# 游戏的主要工作都由这里负责
import sys

import pygame

import Bullet

import Alien

def checkEvents(ship, setting, screen, bullets):
    """按键事件响应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 必须先判断事件类型，再判断按键，因为有的事件没有按键
        if event.type == pygame.KEYDOWN:
            keyDownEvents(event, ship, setting, screen, bullets)
            if(event.key == pygame.K_q):    # q键退出
                sys.exit()
        if event.type == pygame.KEYUP:
            keyUpEvents(event, ship)


# 按键按下响应事件
def keyDownEvents(event, ship, setting, screen, bullets):
    if event.key == pygame.K_d:
        ship.movingRight = True
    if event.key == pygame.K_a:
        ship.movingLeft = True

    if(event.key == pygame.K_SPACE):
        createBullets(bullets, setting, screen, ship)


# 按键弹起响应事件
def keyUpEvents(event, ship):
    if event.key == pygame.K_d:
        ship.movingRight = False
    if event.key == pygame.K_a:
        ship.movingLeft = False


# 刷新屏幕
def refreshScreen(settings, screen, ship, bullets, aliens):
    # 填充背景色
    screen.fill(settings.backColor)
    # 绘制子弹
    for b in bullets:
        b.drawBullet()
    # 绘制飞船
    ship.drawShip()
    # 绘制外星人
    for a in aliens:
        a.drawAlien()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 子弹创建
def createBullets(bullets, setting, screen, ship):
    if (len(bullets) < setting.bulletMaxCount):
        newBullet = Bullet.Bullet(setting, screen, ship)
        # bullets.add(newBullet)
        bullets.add(newBullet)


# 子弹刷新、销毁
def refreshBullets(bullets, aliens):
    # 刷新子弹位置、销毁屏幕外的子弹
    # bullets.refreshBulletLocation()
    for b in bullets:
        b.refreshBulletLocation(aliens, bullets)
    for b in bullets.copy():
        if(b.rect.bottom <= 0):
            bullets.remove(b)


# 创建外星人编队
def createAlienSheet(aliens, screen, setting, ship):
    alien = Alien.Alien(screen, setting)
    alienWidth = alien.rect.width
    rowNumOfAliens = calcRowNumOfAliens(screen, setting, alienWidth)
    totalRows = calcAlienRow(setting, alien, ship)
    for rowIndex in range(totalRows):
        for indexAlien in range(rowNumOfAliens):
            createAlien(screen, setting, aliens, rowIndex, indexAlien, alienWidth)


# 创建一个敌人
def createAlien(screen, setting, aliens, rowIndex, alienIndex, alienWidth):
    alien = Alien.Alien(screen, setting)
    alien.rect.x = alienWidth + 2 * alienWidth * alienIndex
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowIndex
    aliens.add(alien)


# 计算一行敌人数量
def calcRowNumOfAliens(screen, setting, alienWidth):
    numOfOneRowAliens = int((setting.screenWidth - alienWidth * 2) / (alienWidth * 2))
    return numOfOneRowAliens


# 计算敌人总行数
def calcAlienRow(setting, alien, ship):
    if(setting.AlienSheetBeginningDistance > 0):
        distance = setting.AlienSheetBeginningDistance - 1
    else:
        distance = setting.AlienSheetBeginningDistance
    return int((setting.screenHeight - distance*alien.rect.height - alien.rect.height - ship.rect.height)/(2*alien.rect.height))


# 刷新敌人群体位置
def refreshAlienSheet(setting, aliens):
    checkFleetEdges(setting, aliens)
    for a in aliens:
        a.refreshAlienLocation(setting)

# 判断是否碰撞到屏幕边缘，改变敌人群体的移动方向
def checkFleetEdges(setting, aliens):
    for a in aliens:
        if a.checkEdge():
            for al in aliens:
                al.rect.y += setting.alienMoveSpeedVertical
            setting.direction = setting.direction * (-1)
            break
