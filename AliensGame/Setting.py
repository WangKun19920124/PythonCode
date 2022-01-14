class Setting:
    """游戏设置参数"""

    def __init__(self):
        # 窗口设置
        self.screenWidth = 1080     # 窗口宽度
        self.screenHeight = 800     # 窗口高度
        self.backColor = (230, 230, 230)        # 背景颜色

        # 飞船设置
        self.shipSpeed = 10                      # 飞船速度
        self.leftShips = 2                      # 剩余飞船数量

        # 子弹设置
        self.bulletWidth = 5        # 子弹宽度
        self.bulletHeight = 15      # 子弹高度
        self.bulletBackColor = 255, 0, 0     # 子弹颜色
        self.bulletSpeed = 10        # 子弹速度
        self.bulletMaxCount = 5     # 允许同屏子弹数量最大值

        # 敌人设置
        self.AlienSheetBeginningDistance = 2    # 敌人初始距离（alien.rect.height的整数倍）
        self.direction = 1           # 移动方向（1为向右，-1为向左）
        self.alienMoveSpeedHorizontal = 8  # 外星人移动速度(必须>1)
        self.alienMoveSpeedVertical = 50        # 向下速度