# 游戏状态类
import GameFunction


class GameState:
    def __init__(self, setting):
        self.setting = setting
        self.shipLeft = self.setting.leftShips
        self.gameActive = True  # main中有些逻辑只在gameActive==True时才执行，有些逻辑是一直执行

    # # 重启游戏时重置剩余飞船数
    # def restart(self):
    #     self.shipLeft = self.setting.leftShips
    #     self.gameActive = True

    def gameNotActive(self, state, aliens, bullets, ship, screen):
        aliens.empty()          # 清空敌人
        bullets.empty()         # 清空子弹
        ship.centerShip()       # 飞船回到起始中间位置
        GameFunction.createAlienSheet(aliens, screen, state.setting, ship)
        GameFunction.refreshScreen(self.setting, screen, ship, bullets, aliens)