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

# # ## plot sin(x)、cos(x)
# x = np.linspace(-10, 10, 100)
# siny = np.sin(x)
# cosy = np.cos(x)
#
# plt.figure(figsize = (12, 6), dpi = 100, facecolor = 'white')
# plt.title('sinx/cosx')
# plt.xlabel('x')
# plt.ylabel('y')
# # plt.xlim(-2*np.pi, 2*np.pi)
# plt.axis([-10, 10, -2, 2])
# plt.plot(x, siny, ls = '-', lw = 2, c = 'blue', label = r'$sin(x)$')
# plt.plot(x, cosy, ls = '-', lw = 2, c = 'green', label = r'$cos(x)$')
# plt.legend(loc = 'upper right')
# plt.grid(False, axis = 'both',ls = ':', c = 'y')
# plt.axhline(y = 1.0, ls = '--', lw = 2, c = 'r')
# plt.axhline(y = -1.0, ls = '--', lw = 2, c = 'r')
# plt.axvspan(xmin = 0.0, xmax = np.pi/2, color = 'grey', alpha = 0.4)
# plt.text(1.3, 0.3, s= 'cos(x)', weight = 'bold', color = 'green')
# plt.text(2.8, 0.3, s= 'sin(x)', weight = 'bold', color = 'blue')
# plt.annotate(text ="(0,1)", xy = (0,1), xytext = (1,1.5), weight = 'bold', color = 'red', arrowprops = dict(arrowstyle = '-|>', color = 'black',\
#                                                                                                             connectionstyle = 'arc3, rad = 0.5'))
# plt.show()

# ## 嵌套饼图
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(12,8), facecolor = 'cornsilk')
# mpl.rcParams["font.sans-serif"]=["SimHei"]
# mpl.rcParams["axes.unicode_minus"]=False
# labels1 = "A难度水平","B难度水平","C难度水平","D难度水平"
# labels2 = ['A', 'B', 'C', 'D']
#
# students1 = [0.35,0.15,0.20,0.30]
# colors1 = ['orange', 'limegreen', 'blue', 'violet']
# explode = (0,0,0,0)
#
# # 绘制外层饼图
# wedges1, texts1, autotexts1 = plt.pie(students1,explode=explode,
# labels=labels1,
# autopct="%3.1f%%",
# startangle=45,
# shadow=False,
# colors=colors1,pctdistance = 0.85, labeldistance = 1.1,radius = 0.7, wedgeprops= {'lw':1, 'edgecolor':'w'})
#
# # 绘制内层饼图
# students2 = [0.3, 0.2, 0.25, 0.25]
# colors2 = ['orange', 'limegreen', 'blue', 'violet']
# wedges2, texts2, autotexts2 = plt.pie(students2, explode=explode,labels=labels2,autopct="%3.1f%%",startangle=45,shadow=False,\
#                                       colors=colors2, pctdistance = 0.85, labeldistance = 1.1, radius = 0.5, wedgeprops= {'lw':1, 'edgecolor':'w'})
#
# # 绘制中心空白饼图
# plt.pie(x=[1], colors = 'w', radius = 0.3)
#
# plt.legend(wedges1, labels1, loc = 'upper right', title = '外环', edgecolor = 'red', facecolor = 'pink', fontsize =10, ncol = 2)
# # plt.legend(wedges2, labels2, loc = 'lower right', title = '内环', edgecolor = 'red', facecolor = 'pink', fontsize =10)
#
# plt.title("title", style = 'oblique', size = 'xx-large', color = 'c', family="Comic Sans MS")
#
# plt.table([students1, students2], cellLoc='left', colWidths=[0.4, 0.4, 0.4, 0.4], colLabels=labels1, colColours=colors1, rowLabels=['外环数据', '内环数据'], rowColours=['orange', 'limegreen'], rowLoc='right', loc = 'bottom')
#
# plt.show()

# ## 横向箱线图
# import matplotlib as mpl
# mpl.rcParams["font.sans-serif"]=["FangSong"]
# mpl.rcParams["axes.unicode_minus"]=False
# testA = np.random.randn(5000)
# testB = np.random.randn(5000)
# testList = [testA,testB]
# labels = ["随机数生成器AlphaRM","随机数生成器BetaRM"]
# colors = ["#1b9e77","#d95f02"]
# whis = 1.6
# width = 0.35
# bplot = plt.boxplot(testList, whis=whis, widths=width, sym="+", patch_artist=True,vert = False, showfliers = True)
# for patch,color in zip(bplot["boxes"],colors):
#     patch.set_facecolor(color)
# plt.xlabel("随机数值")
# plt.yticks(ticks= [1, 2], labels= labels, rotation = 90)
# plt.title("生成器抗干扰能力的稳定性比较")
# plt.grid(axis="y",ls=":",lw=1,color="gray",alpha=0.4)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 5 * np.pi, 1000)
#
# y1 = np.sin(x)
# y2 = np.sin(2 * x)
#
# plt.fill(x, y1, color = 'darkorange', alpha = 0.4, label="$ y = sin(x) $")
# plt.fill(x, y2, color = 'violet', alpha = 0.4, label="$ y = sin(2 * x) $")
# plt.legend(loc='best')
#
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.arange(0.0, 2, 0.01)
# x1 = np.sin(2 * np.pi * y)
# x2 = 1.2 * np.sin(4 * np.pi * y)
#
# fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=True)
#
# ax1.fill_betweenx(y, 0, x1)
# ax1.set_ylabel('(x1, 0)')
#
# ax2.fill_betweenx(y, x1, 1)
# ax2.set_ylabel('(x1, 1)')
#
# ax3.fill_betweenx(y, x1, x2)
# ax3.set_ylabel('(x1, x2)')
# ax3.set_xlabel('x')
#
# plt.show()

# x = np.linspace(-2*np.pi, 2*np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot((x.min(), x.max()), (0, 0))
# plt.plot(x, y1, color = 'blue', label = '$sin(x)$')
# plt.plot(x ,y2, color = 'red', label = '$cos(x)$')
# # plt.fill_between(x, y2, y1, where = (x>0)&(x<np.pi/2), color = 'darkorange', alpha = 0.4)
# # plt.fill_between(x, y1, y2, where = (y1<y2), color = 'violet', alpha = 0.4)
# plt.fill_between(x, y1, 0.5, where = (y1>0.5)&(x>0)&(x<np.pi), color = 'violet', alpha = 0.5)
# plt.legend(loc = 'best')
# plt.show()

# a = np.ones((2,3,2))
# b = np.ones((1,3,1))
a = np.asarray([[[1, 1], [1, 1], [1, 1]]])
b = np.asarray([[[1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1]]])
print(a)
print(b)
print(a*b)