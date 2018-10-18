from functools import reduce

import numpy as np


class Vtool:
    def tovector(a, b):
        """transform two 3-corrdinate to a vector"""
        v = []
        for i in 3:
            v[i] = b[i] - a[i]
        return v

    def distance(a, b):
        """
        distance between two points
        distance =√[(x1 - x2) ^ 2 + (y1 - y2) ^ 2 + (z1 - z2) ^ 2]
        """
        # a1 = np.array(a)
        # b1 = np.array(b)
        # cc = [(a1 + b1) ** 2]
        # print(cc)
        # c = reduce(lambda x, y: x + y, cc)
        return reduce(lambda x, y: x + y, ((np.array(a) - np.array(b))**2).tolist())**0.5

    def distan_op(point, plane):
        """
        calculate the distance of a point between a plane,
        d = |Ax+By+Cz+D|/(√(A^2+B^2+C^2))
        get two lists
        """
        A = plane[0]
        B = plane[1]
        C = plane[2]
        D = (plane+[0])[3]  # to avoid the size of list named 'plane' only have three elements
        return (A*point[0] + B*point[1] + C*point[2] + D) / (A**2 + B**2 + C**2)**0.5

    def corss_product(a, b):
        """ c is the cross product of a and b : c = a x b """
        a1 = np.array(a)
        b1 = np.array(b)
        c = np.cross(a1, b1)
        return c

    def parallel(a, b):
        """
        a,b are all the  vector
        if the cross product(x) is equal with zero
        """
        c = Vtool.corss_product(a, b)
        if c == np.array([0, 0, 0]):
            return True
        else:
            return False

    def vertical(a, b):
        """
        a,b are all the  vector
        if the inner product(*) is equal with zero
        """
        a1 = np.mat([a])
        b1 = np.mat([b])
        c = a1 * b1.T
        if c == 0:
            return True  # a is perpendicular to b
        else:
            return False

    # def cal_line1(x, y, z):
    #     """three axis and one direction vector"""
    #     l = len(x)  # it should be 8
    #     length = []
    #     for i in range(l):
    #         a = [x[i], y[i], z[i]]
    #         for j in range(i+1, l):
    #             b = [x[j], y[j], z[j]]
    #             dis = Vtool.distance(a, b)
    #             # save the distance into dict, a < b
    #             length.append([dis, [a, b]])
    #     # sort as first element of the list which is in the list named 'length'
    #     length.sort(key=lambda ll: ll[0])
    #     return [i[1] for i in length[:12]]

    def cal_line(x, y, z, x1=[], y1=[], z1=[]):
        """three axis and one direction vector"""
        l = len(x)  # it should be 8
        if len(x1) ==0:
            x1, y1, z1 = [[0 for i in range(l)] for i in range(3)]
        length = []
        for i in range(l):
            a = [x[i], y[i], z[i]]
            a1 = [x1[i], y1[i], z1[i]]
            for j in range(i+1, l):
                b = [x[j], y[j], z[j]]
                b1 = [x1[j], y1[j], z1[j]]
                dis = Vtool.distance(a, b)
                # save the distance into dict, a < b
                length.append([dis, [a, b], [a1, b1]])
        # sort as first element of the list which is in the list named 'length'
        length.sort(key=lambda ll: ll[0])
        index = 0
        for i in length:
            print(index," ",end="")
            index += 1
            print(float('%.2f'%i[0]))
        ll = length[8][0]**2
        if (ll - 1e-5) <= (length[0][0]**2 + length[4][0]**2) <= (11 + 1e-5):
            result = length[:8] + length[12:16]
        else:
            result = length[:12]
        # result = [(i[1], i[2]) for i in length[:12]]

        return [(i[1], i[2]) for i in result]

    # def cal_dot_line(x, y, z, length, point):
    #     l = len(x)
    #     for i in range(l):


    def ic_lp(xyz, v):
        """
        the intersection point of a line and a plane
        (x - x0)/v[0] = (y-y0)/v[1] = (z-z0)/v[2]
        # 直线的参数方程
        # x = x0 + v[0]*t
        # y = y0 + v[1]*t
        # z = z0 + v[2]*t
        the equation of plane which throw the point (0,0,0)
        # v[0]*x + v[1]*y + v[2]*z = 0
        """
        x0, y0, z0 = xyz
        t = (-v[0] * x0 - v[1] * y0 - v[2] * z0) / (v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        x1 = x0 + v[0] * t
        y1 = y0 + v[1] * t
        z1 = z0 + v[2] * t
        return x1, y1, z1



class Draw:
    def surface(A, B, C, D=0, size=2):
        """
        the standard equation of plane is " Ax+By+Cz+D=0 "
        so transform the equation as " z=(-D-Ax-By)/C
        """
        x, y = np.mgrid[-size:size:3j, -size:size:3j]
        z = ((-D) - A * x - B * y) / C
        return x, y, z

if __name__ == '__main__':
    Vtool.cal