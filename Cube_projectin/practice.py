# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from functools import reduce
from random import random
from time import sleep

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

# %matplotlib inline

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']


def plot_opaque_cube(x=10, y=20, z=30, dx=40, dy=50, dz=60):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')


    xx = np.linspace(x, x+dx, 2)
    yy = np.linspace(y, y+dy, 2)
    zz = np.linspace(z, z+dz, 2)

    xx, yy = np.meshgrid(xx, yy)

    ax.plot_surface(xx, yy, z)
    ax.plot_surface(xx, yy, z+dz)

    yy, zz = np.meshgrid(yy, zz)
    ax.plot_surface(x, yy, zz)
    ax.plot_surface(x+dx, yy, zz)

    xx, zz = np.meshgrid(xx, zz)
    ax.plot_surface(xx, y, zz)
    ax.plot_surface(xx, y+dy, zz)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    # ax.set_xlim3d(-dx, dx*2, 20)
    plt.title("Cube")
    plt.show()



def plot_linear_cube(x, y, z, dx, dy, dz, color='red'):
    fig = plt.figure()
    ax = Axes3D(fig)
    xx = [x, x, x+dx, x+dx, x]
    yy = [y, y+dy, y+dy, y, y]
    kwargs = {'alpha': 1, 'color': color}
    ax.plot3D(xx, yy, [z]*5, **kwargs)
    ax.plot3D(xx, yy, [z+dz]*5, **kwargs)
    ax.plot3D([x, x], [y, y], [z, z+dz], **kwargs)
    ax.plot3D([x, x], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], **kwargs)
    ax.plot3D([x+dx, x+dx], [y, y], [z, z+dz], **kwargs)
    plt.title('Cube')
    plt.show()



def fun1():
    # import necessary module
    # from mpl_toolkits.mplot3d import axes3d
    # import matplotlib.pyplot as plt
    # import numpy as np

    # load data from file
    # you replace this using with open
    data1 = np.array([[random()*10 for i in range(13)]for i in range(22)])
    first_2000 = data1[:, 3]
    second_2000 = data1[:, 7]
    third_2000 = data1[:, 11]

    data2 = data1-1
    first_1000 = data2[:, 3]
    second_1000 = data2[:, 7]
    third_1000 = data2[:, 11]

    # new a figure and set it into 3d
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # set figure information
    ax.set_title("3D_Curve")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # draw the figure, the color is r = read
    ax.plot(first_2000, second_2000, third_2000, c='r')
    sleep(1)
    plt.show()
    ax.plot(first_1000, second_1000, third_1000, c='b')
    sleep(1)
    plt.show()

def fun2():
    import numpy
    from mpl_toolkits.mplot3d import proj3d
    def orthogonal_proj(zfront, zback):
        a = (zfront + zback) / (zfront - zback)
        b = -2 * (zfront * zback) / (zfront - zback)
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, a, b],
                            [0, 0, 0, zback]])

    proj3d.persp_transformation = orthogonal_proj

def fun3():
    fig = plt.figure(5)
    ax = fig.add_subplot(1, 1, 1, projection='3d')  # 绘制三维图

    # x, y = np.mgrid[-2:2:20j, -2:2:20j]  # 获取x轴数据，y轴数据
    # z = x #x * np.exp(-x ** 2 - y ** 2)  # 获取z轴数据
    x, y = np.mgrid[0:1:10j, 0:1:10j]
    z = np.array([[1 for i in range(10)] for i in range(10)])
    ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.coolwarm, alpha=0.8)  # 绘制三维图表面
    # ax.set_xlabel('x-name')  # x轴名称
    # ax.set_ylabel('y-name')  # y轴名称
    # ax.set_zlabel('z-name')  # z轴名称

    plt.show()

def fun4():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter

    fig = plt.figure(figsize=(16, 12))
    ax = fig.gca(projection="3d")

    # 准备数据
    x = np.arange(-5, 5, 0.25)  # 生成[-5，5] 间隔0.25的数列，间隔越小，曲面越平滑
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)  # 格点矩阵，原来的x行向量向下复制len(y)此形成
    # len(y)*len(x)的矩阵，即为新的x矩阵；原来的y列向量向右复制len(x)次，形成
    # len(y)*len(x)的矩阵，即为新的y矩阵；新的x矩阵和新的y矩阵shape相同
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)

    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  # cmap指color map

    # 自定义z轴
    ax.set_zlim(-1, 1)
    ax.zaxis.set_major_locator(LinearLocator(20))  # z轴网格线的疏密，刻度的疏密，20表示刻度的个数
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 将z的value子符串转为float，保留2位小数

    # 设置坐标轴的label和标题
    ax.set_xlabel('x', size=15)
    ax.set_ylabel('y', size=15)
    ax.set_zlabel('z', size=15)
    ax.set_title("Surface plot", weight='bold', size=20)

    # 添加右侧的色卡条
    fig.colorbar(surf, shrink=0.6, aspect=8)  # shrink表示整体收缩比例，aspect仅对bar的宽度有影响，
    # aspect值越大，bar越窄

    plt.show()

if __name__ == "__main__":
    # fun2()
    # plot_linear_cube(0, 0, 0, 100, 120, 130)
    # plot_opaque_cube()
    # fun3()
    #
    # a = [
    #     [1,'a'],
    #     [33, 'aaa'],
    #     [23, 'aw'],
    #     [2,'b'],
    #      ]
    # a.sort()
    # print(a)
    # b =  0
    # a  = np.mgrid[0:1:3j, 0:1:3j]
    # print(a,"----\n",b)
    # a  = [1, 2,3]
    # b1,b2 = a
    # # b[0][1]=11
    # print(b1,b2)
    # a = np.loadtxt('test.txt')
    # a -= 1
    # print(a)
    # np.savetxt('test.txt', a, fmt='%d %d %d')
    a = 2
    if 1 < a < 3:
        print(1e10)
