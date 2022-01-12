class Setting:
    """游戏设置参数"""

    def __init__(self):
        # 窗口设置
        self.screenWidth = 1200     # 窗口宽度
        self.screenHeight = 800     # 窗口高度
        self.backColor = (230, 230, 230)        # 背景颜色
        self.shipSpeed = 2                      # 飞船速度

        # 子弹设置
        self.bulletWidth = 3        # 子弹宽度
        self.bulletHeight = 15      # 子弹高度
        self.bulletBackColor = 60, 0, 0     # 子弹颜色
        self.bulletSpeed = 1        # 子弹速度
        self.bulletMaxCount = 3
