#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: quickhull.py
@time: 2021/11/27
@desc:
'''


import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon


def split(u, v, points):
    # return points on left side of UV
    return [p for p in points if np.cross(p - u, v - u) < 0]


def extend(u, v, points):
    if not points:
        return []
    # find furthest point W, and split search to WV, UW
    w = min(points, key=lambda p: np.cross(p - u, v - u))
    p1, p2 = split(w, v, points), split(u, w, points)
    return extend(w, v, p1) + [w] + extend(u, w, p2)


def convex_hull(points):
    # find two hull points, U, V, and split to left and right search
    u = min(points, key=lambda p: p[0])
    v = max(points, key=lambda p: p[0])
    left, right = split(u, v, points), split(v, u, points)

    # find convex hull on each side
    return [v] + extend(u, v, left) + \
           [u] + extend(v, u, right) + [v]

points = np.random.rand(100, 2)
point_list = convex_hull(points)

# xx = np.random.randint(100, 500, 100)
# yy = np.random.randint(50, 100, 100)
# points = []
# for i in range(100):
#     points.append([xx[i], yy[i]])
# point_list = convex_hull(points)
# print(point_list)
# print(points)
# plt.plot(point_list)
# plt.plot(points,".")
polygon1 =Polygon(point_list)
plt.plot(*polygon1.exterior.xy)
plt.show()