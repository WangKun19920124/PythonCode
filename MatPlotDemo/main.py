import matplotlib.pyplot as plt
import numpy as np
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

# import numpy
# # data = numpy.random.randn(10000)
# data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# plt.hist(data, bins=40, density=True, facecolor='blue', edgecolor='black', alpha=0.7)
# plt.xlabel("gauss distribution", fontsize=20)
# plt.ylabel("value", fontsize=20)
# plt.show()

# ##饼图
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False
# size = [40, 40, 20]
# explode = [0.1, 0, 0]
# color = ["red", "green", "blue"]
# label = ["part1", "part2", "part3"]
#
# plt.pie(size, explode=explode, colors=color, labels=label, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
# plt.axis("equal")
# plt.legend()
# plt.show()

# #条形图
# labels = ["2019", "2020", "2021", "2022"]
# num1 = [50, 100, 150, 200]
# num2 = [10, 100, 200, 300]
# a = [0, 1, 2, 3]
# ##绘制
# rects1 = plt.bar(a, height=num1, width=0.4, alpha=0.8, color="red", label="department1")
# rects2 = plt.bar([i+0.4 for i in a], height=num2, width=0.4, alpha=0.8, color="blue", label="department2")
# ##设置坐标轴
# plt.title("company")
# plt.xlabel("year")
# plt.xticks([index + 0.2 for index in a], labels)
# plt.ylabel("total count")
# plt.ylim(0, 400)
# plt.legend(loc="upper left")
# ##条形图上文本
# # for rect in rects1:
# #     height = rect.get_height()
# #     plt.text(rect.get_x(), rect.get_width()/2, height + 1, str(height), ha="center", va="bottom")
#
# plt.show()

# # 读CSV
# import csv
# from datetime import datetime
# filename = 'C:\\Users\\eivision\\Desktop\\222.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, colIndex in enumerate(header_row):
#         print(index, colIndex)
#
#     date = []
#     temperature = []
#     for row in reader:
#         # curDate = datetime.strptime(row[0], "%Y/%m/%d")
#         # date.append(curDate)
#         date.append(row[0])
#         temperature.append(int(row[1]))
#     fig = plt.figure(dpi=128, figsize=(10, 6))
#     plt.plot(date, temperature, c="green")
#     plt.title("csv graph", fontsize=24)
#     plt.xlabel("date", fontsize=10)
#     plt.ylabel("temperature ℃", fontsize=10)
#     plt.ylim(0, 40)
#     plt.tick_params(axis="both", which="major", labelsize=16)
#     fig.autofmt_xdate()
#     plt.show()
#     print(temperature)
#     print(date)

# ## 绘制心形1
# t = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# X=16*(np.sin(t))**3
# Y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
#
# plt.subplot(121)
# plt.plot(X,Y)
#
# x=y=np.arange(-3.0, 3.0, 0.02)
# X, Y=np.meshgrid(x, y)
# Z= (X**2 + Y**2 - 1)**3 -X**2 *  Y**3
# plt.subplot(122)
# plt.contour(X, Y, Z)
# plt.colorbar()
#
# plt.show()

# # 绘制心形2
# import turtle
# turtle.color('red', 'pink')
# turtle.pensize(2)
# turtle.pendown()
# turtle.setheading(150)
# turtle.begin_fill()
# turtle.fd(50)
# turtle.circle(50 * -3.745, 45)
# turtle.circle(50 * -1.431, 165)
# turtle.left(120)
# turtle.circle(50 * -1.431, 165)
# turtle.circle(50 * -3.745, 45)
# turtle.fd(50)
# turtle.end_fill()

## plot
x = np.linspace(-10, 10, 100)
siny = np.sin(x)
cosy = np.cos(x)

plt.figure(figsize = (12, 6), dpi = 100, facecolor = 'white')
plt.title('sinx/cosx')
plt.xlabel('x')
plt.ylabel('y')
# plt.xlim(-2*np.pi, 2*np.pi)
plt.axis([-10, 10, -2, 2])
plt.plot(x, siny, ls = '-', lw = 2, c = 'blue', label = 'sin(x)')
plt.plot(x, cosy, ls = '-', lw = 2, c = 'green', label = 'cos(x)')
plt.legend(loc = 'upper right')
plt.grid(False, axis = 'both',ls = ':', c = 'y')
plt.axhline(y = 1.0, ls = '--', lw = 2, c = 'r')
plt.axhline(y = -1.0, ls = '--', lw = 2, c = 'r')
plt.axvspan(xmin = 0.0, xmax = np.pi/2, color = 'grey', alpha = 0.4)
plt.text(1.3, 0.3, s= 'cos(x)', weight = 'bold', color = 'green')
plt.text(2.8, 0.3, s= 'sin(x)', weight = 'bold', color = 'blue')
plt.annotate(text ="(0,1)", xy = (0,1), xytext = (1,1.5), weight = 'bold', color = 'red', arrowprops = dict(arrowstyle = '-|>', color = 'black',\
                                                                                                            connectionstyle = 'arc3, rad = 0.5'))
plt.show()









