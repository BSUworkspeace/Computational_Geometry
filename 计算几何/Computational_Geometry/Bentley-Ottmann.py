#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: Bentley-Ottmann.py
@time: 2021/11/12
@desc:
'''
from lsi import intersection
import numpy as np
import random
from skgeom.draw import draw
import matplotlib.pyplot as plt
S =[]
for i in range(1000):
    p1 = (random.randint(0, 1000), random.randint(0, 1000))
    p2 = (random.randint(0, 1000), random.randint(0, 1000))
    s = (p1, p2)
    S.append(s)

i = intersection(S)

segments=i.values()
intersections=i.keys()


for point , line in i.items():
    print(point,line)
    plt.plot(line[0], line[1], color="#1f77b4")
    plt.plot(point[0], point[1]+20, ".")

plt.show()