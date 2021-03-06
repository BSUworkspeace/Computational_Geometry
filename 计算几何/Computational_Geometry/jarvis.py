#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: jarvis.py
@time: 2021/11/17
@desc:
'''
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon


# point class with x, y as point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Left_index(points):
    '''
    Finding the left most point
    '''
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):
    '''
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convexHull(points, n):
    '''
    # There must be at least 3 points
    '''
    
    if n < 3:
        return

    # Find the leftmost point
    l = Left_index(points)

    hull = []

    # '''
    # Start from leftmost point, keep moving counterclockwise
    # until reach the start point again. This loop runs O(h)
    # times where h is number of points in result or output.
    # '''
    p = l
    q = 0
    while 1:

        # Add current point to result
        hull.append(p)

        # '''
        # Search for a point 'q' such that orientation(p, q,
        # x) is counterclockwise for all points 'x'. The idea
        # is to keep track of last visited most counterclock-
        # wise point in q. If any point 'i' is more counterclock-
        # wise than q, then update q.
        # '''
        q = (p + 1) % n

        for i in range(n):

            # If i is more counterclockwise
            # than current q, then update q
            if (orientation(points[p],
                            points[i], points[q]) == 2):
                q = i

        # '''
        # Now q is the most counterclockwise with respect to p
        # Set p as q for next iteration, so that q is added to
        # result 'hull'
        # '''
        p = q

        # While we don't come to first point
        if (p == l):
            break
    point_list=[]
    # Print Result
    for each in hull:
        print(points[each].x, points[each].y)
        point_list.append((points[each].x, points[each].y))
    return(point_list)

# xx = np.random.randint(100, 500, n)
# yy = np.random.randint(50, 100, n)
# points = []
# for i in range(n):
#     points.append(Point(xx[i], yy[i]))

# point_list = convexHull(points, len(points))
# plt.plot([xx[i], yy[i]],".")
# polygon1 = Polygon(point_list)
# plt.plot(*polygon1.exterior.xy)
# plt.savefig("./plot_point.png")
#
# points = np.random.rand(100, 2)
# point_list = convexHull(points, len(points))
n=1111111
xx = np.random.randint(100, 500, n)
yy = np.random.randint(50, 100, n)
points = []
point=[]
for i in range(n):
    point.append([xx[i], yy[i]])
    points.append(Point(xx[i], yy[i]))

print(point)
point_list = convexHull(points, len(points))
# print(point_list)
# print(points)
# plt.plot(point_list)
plt.plot(xx,yy,".")
polygon1 =Polygon(point_list)
plt.plot(*polygon1.exterior.xy)
plt.show()