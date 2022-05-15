#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: Intersection.py
@time: 2021/11/26
@desc:
'''
import skgeom as sg
from skgeom.draw import draw
from random import random as r
import itertools
import matplotlib.pyplot as plt
segments = []
for i in range(100000):
    segments.append(sg.Segment2(sg.Point2(r(), r()),
                                sg.Point2(r(), r())))

intersections = []
for s1, s2 in itertools.permutations(segments, 2):
    isect = sg.intersection(s1, s2)
    if isect:
        intersections.append(isect)

# for s in segments:
#     print(s)
#     draw(s)
# for i in intersections:
#     draw(i)
# plt.show()