import matplotlib.pyplot as plt

## 绘制曲线
# x = [1, 3, 9, 16, 25, 36]
# plt.plot(range(1, 7), x, linewidth=3)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("X", fontsize=10)
# plt.ylabel("Y", fontsize=10)
# plt.tick_params(axis="both", labelsize=10)
# plt.show()

## 绘制离散点
# x = range(0, 101)
# for i in x:
#     plt.scatter(i, i*i, s=50)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("X", fontsize=10)
# plt.ylabel("Y", fontsize=10)
# plt.tick_params(axis="both", labelsize=10)
# plt.show()

# ## 绘制颜色映射
# x = range(0, 101)
# y = [i**2 for i in x]
# plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolors='none', s=50)
# plt.axis([0, 100, 0, 11000])
# plt.savefig("scatterDemo.png", bbox_inches='tight')
# plt.show()

# ## 随机漫步
# from random import choice
# class RandomWalk:
#     def __init__(self, totalPoints):
#         self.x_values = [0]
#         self.y_values = [0]
#         self.totalPoints = totalPoints
#
#     def fillWalk(self):
#         while len(self.x_values) < self.totalPoints:
#             xDir = choice([-1, 1])
#             xStepTemp = choice([0, 1, 2, 3, 4])
#             yDir = choice([-1, 1])
#             yStepTemp = choice([0, 1, 2, 3, 4])
#
#             xStep = xDir * xStepTemp
#             yStep = yDir * yStepTemp
#             if xStep == 0 and yStep == 0:
#                 continue
#             xNext = self.x_values[-1] + xStep
#             yNext = self.y_values[-1] + yStep
#             self.x_values.append(xNext)
#             self.y_values.append(yNext)
#
# while True:
#     rw = RandomWalk(50000)
#     rw.fillWalk()
#     plt.figure(dpi = 128, figsize=(10, 6), facecolor='red', edgecolor='yellow')
#     plt.scatter(0, 0, c="green", edgecolors="none", s=100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
#     plt.scatter(rw.x_values, rw.y_values, c=list(range(0, rw.totalPoints)), cmap=plt.cm.Blues, edgecolors='none', s=1)
#     # plt.axes().get_xaxis().set_visible(False)
#     # plt.axes().get_yaxis().set_visible(False)
#     plt.show()
#     flag = input("want another walk?(y/n)")
#     if flag == "n":
#         print("walk over..")
#         break

import numpy
# data = numpy.random.randn(10000)
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=40, density=True, facecolor='blue', edgecolor='black', alpha=0.7)
plt.xlabel("gauss distribution", fontsize=20)
plt.ylabel("value", fontsize=20)
plt.show()