import time

import matplotlib.pyplot
from mpl_toolkits.mplot3d import axes3d
import numpy
from whichline import Vtool, Draw

print("let us run")
start_time1 = time.clock()
start_time2 = time.time()
# x = [ [0 for i in range(3)] for i in range(8)]
# print(x)

# 输入的原始点

x = [0 for i in range(8)]
y = [0 for i in range(8)]
z = [0 for i in range(8)]

# 投影到空间平面上的点
x1 = [0 for i in range(8)]
y1 = [0 for i in range(8)]
z1 = [0 for i in range(8)]
x1_x = {}
y1_y = {}
z1_z = {}

# new coordinate of new coordinate system
x2 = [0 for i in range(8)]
y2 = [0 for i in range(8)]
z2 = [0 for i in range(8)]

point1 = numpy.loadtxt("test.txt")
x = point1[0:8,0]
y = point1[0:8,1]
z = point1[0:8,2]

print(x,y,z)

# for i in range(8):
#     x[i] = int(input())
#     y[i] = int(input())
#     z[i] = int(input())
    # for j in range(3):
    #     x[i][j] = int(input())

# 面 垂直于方向向量 设定过原点
# Ax+By+Cz+D=0 
# v[0]*x + v[1]*y + v[2]*z = 0

v = [] # 方向向量
v = point1[8,0:3]

print(v)
# for i in range(3):
#     v[i] = int(input())

# 方向向量与各个点形成的直线的点向式方程
# (x - x[i])/v[0]=(y-y[i])/v[1] = (z-z[i])/v[2]

# 直线的参数方程
# / x = x[i] + v[0]*t
# | y = y[i] + v[1]*t
# \ z = z[i] + v[2]*t
# v[0]*x + v[1]*y + v[2]*z = 0

# 合并,得关于t的一元一次方程
# v[0]*(x[i]+v[0]*t) + v[1]*(y[i]+v[1]*t) + v[2]*(z[i]+v[2]*t) = 0

# 化简,解方程组,得直线与平面的交点
# t*(v[0]**+v[1]**+v[2]**) + v[0]*x[i] + v[1]*y[i] + v[2]*z[i] = 0
for i in range(8):
    # t = (-v[0]*x[i] - v[1]*y[i] - v[2]*z[i]) / (v[0]**2 + v[1]**2 + v[2]**2)
    # x1[i] = x[i] + v[0]*t
    # y1[i] = y[i] + v[1]*t
    # z1[i] = z[i] + v[2]*t
    xyz = [x[i], y[i], z[i]]
    x1[i], y1[i], z1[i] = Vtool.ic_lp(xyz, v)
    # 做一下映射 以便日后连线
    x1_x[x[i]] = x1[i]
    y1_y[y[i]] = y1[i]
    z1_z[z[i]] = z1[i]

print(x1,y1,z1)

# https://www.cnblogs.com/leexiaoming/p/6641162.html
fig = matplotlib.pyplot.figure(figsize=(10, 10))

# proj_type='ortho' for 正交投影(a perspective orthogonal plot)
ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
matplotlib.pyplot.axis('square')
# matplotlib.pyplot.tick_params(axis='both',which='major',labelsize=14)
# ax = fig.gca(projection='3d')
# to avoid the chinese font to become the chaos code
fontname1 = "FZZHYJW.TTF"
fontname2 = "A-OTF-TakaHandStd-DeBold.otf"
font1 = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/'+fontname1, size=20)
ax.set_title("我的立方体",fontproperties=font1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
# draw lines
# figure = ax.plot(x, y, z, color="red", markerfacecolor='blue',marker='o')
# only draw point
figure = ax.scatter(x, y, z, color='blue',marker='o')

for a, b, c in zip(x, y, z):
    ax.text(a, b, c, (a, b, c), ha='center', va='bottom', fontsize=10)

figure = ax.scatter(x1, y1, z1, color='#4a86e8',marker='o')
for a, b, c in zip(x1, y1, z1):
    print(a,b,c)
    abc = tuple([float('%.2f'%i) for i in (a, b, c)])
    print(abc)
    # ax.text(a, b, c, abc, ha='center', va='bottom', fontsize=10)

lines = Vtool.cal_line(x, y, z, x1, y1, z1)
print(lines)
for l, l1 in lines:
    # for j in range(3):
    l = numpy.array(l).T
    a = l[0, :]
    b = l[1, :]
    c = l[2, :]
    # b = numpy.array(b)
    ax.plot(a, b, c, color="red")

    # plot the shadow
    l1 = numpy.array(l1).T
    aa = l1[0, :]
    bb = l1[1, :]
    cc = l1[2, :]
    ax.plot(aa, bb, cc, color="#ff00ff")

ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="green")


# for l in lines:
#     # for j in range(3):
#     l = numpy.array(l).T
#     a = l[0, :]
#     b = l[1, :]
#     c = l[2, :]
#     # b = numpy.array(b)
#     ax.plot(a, b, c, color="#ff00ff")


# ====================================
# make the new coordinate system
# new XOY plane
# v[0]*x + v[1]*y + v[2]*z = 0
nx, ny, nz = Draw.surface(v[0], v[1], v[2])
ax.plot_surface(nx, ny, nz, color="#f8ff00", alpha=0.27)  # alpha设置透明度
# (!false)----new XOZ plane is original X, original point and the direction vector
# 我们让new X axial 平行于 original XOY, so we can make a temp plane which is parallel to original XOY
# the intersecting line of the two planes is our new X axial
# ori-XOY : z = 0 ; temp : z = D
# so [!new X axial]: v[0]*x + v[1]*y + v[2]*D = 0 ==> x/v[1] = y/(-v[0]) - (v[2]*D) / (v[0]*v[1])
# so new Y is perpendicular to X and the direction vector (Z)
new_x = [v[1], -v[0], 0]
new_z = v
new_y = Vtool.corss_product(new_x, new_z)
# 现在先把新坐标系的原点定在原来的原点
new_origin = [0, 0, 0]
# print(new_y)
ax.plot([new_x[0], 0], [new_x[1], 0], [new_x[2], 0], color="green")
ax.plot([new_y[0], 0], [new_y[1], 0], [new_y[2], 0], color="green")
# [YOZ] : new_x[0]*x + new_x[1]*y + new_x[2]*z = 0
# [XOZ] : new_y[0]*x + new_y[1]*y + new_y[2]*z = 0
# [XOY] : new_z[0]*x + new_z[1]*y + new_z[2]*z = 0

# now, 始まる our battle
xyz = (x2, y2, z2)
new_xyz = (new_x, new_y, new_z)
for i in range(8):
    point = [x[i], y[i], z[i]]
    for j in range(3):  # order by YOZ, XOZ, XOY
        plane = [new_xyz[j][0], new_xyz[j][1], new_xyz[j][2], 0]
        xyz[j][i] = Vtool.distan_op(point, plane)

print(x2, y2, z2)
# =====================================
fig2 = matplotlib.pyplot.figure()
matplotlib.pyplot.axis('equal')

ax2 = fig2.add_subplot(111)
# ax = fig.add_subplot(122)
lines2d = Vtool.cal_line(x2, y2, z2)
ax2.scatter(x2, y2, z2, color="red")
for a, b in zip(x2, y2):
    ax2.text(a, b, (float('%.2f' % a), float('%.2f' % b)), ha='center', va='bottom', fontsize=10)

for l in lines2d:
    l = numpy.array(l).T
    a = l[0, :]
    b = l[1, :]
    # c = l[2, :]
    # b = numpy.array(b)
    ax2.plot(a, b, color="red")







# matplotlib.pyplot.legend()

print("programming time: "+str(time.time() - start_time2))
print("CPU:time_cousuming : "+str(time.clock() - start_time1))


matplotlib.pyplot.show()
