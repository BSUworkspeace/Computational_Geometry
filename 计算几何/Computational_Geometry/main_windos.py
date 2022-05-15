#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: main_windos.py
@time: 2021/11/17
@desc:
'''

import tkinter as tk  # 使用Tkinter前需要先导入
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from jarvis import convexHull
from jarvis import Point
import PIL
from tkinter import *
from PIL import ImageTk
import time

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x1000')  # 这里的乘是小x

var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()
rad=tk.IntVar()
def show():
    # 获取var的值
    m.config(text="model: "+dict[rad.get()])

dict = {0: "jarvis", 1: "intersection", 2: "bentiey-ottmann",3:"in_poly"}

m = tk.Label(window, text="please choose model", bg="lightyellow", width=30)
m.pack()

var.set('input number of random plots')
# 第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show=None)  # 显示成明文形式
e.pack()



for x, y in dict.items():
    tk.Radiobutton(window, text=y, variable=rad, value=x, command=show).pack()

def jarvis_model(n):
    # print(n)
    xx = np.random.randint(100, 500, n)
    yy = np.random.randint(50, 100, n)
    points = []
    for i in range(n):
        points.append(Point(xx[i], yy[i]))

    point_list = convexHull(points, len(points))
    # plt.plot([xx[i], yy[i]],".")
    polygon1 = Polygon(point_list)
    plt.plot(*polygon1.exterior.xy)
    plt.savefig("./plot_point.png")
    print("success for jarvis")
    time.sleep(5)

def intersection_model(n):
    import skgeom as sg
    from skgeom.draw import draw
    from random import random as r
    import itertools

    segments = []
    for i in range(n):
        segments.append(sg.Segment2(sg.Point2(r(), r()),
                                    sg.Point2(r(), r())))
    intersections = []
    for s1, s2 in itertools.permutations(segments, 2):
        isect = sg.intersection(s1, s2)
        if isect:
            intersections.append(isect)

    for s in segments:
        draw(s)
    for i in intersections:
        draw(i)

    plt.savefig("./plot_point.png")
    print("success for intersection")
    time.sleep(5)

def BO_model(n):
    from lsi import intersection
    import random
    S = []
    for i in range(n):
        p1 = (random.randint(0, 1000), random.randint(0, 1000))
        p2 = (random.randint(0, 1000), random.randint(0, 1000))
        s = (p1, p2)
        S.append(s)
        print(s)

    i = intersection(S)
    print(i)


    for point, line in i.items():
        plt.plot(line[0], line[1], color="#1f77b4")
        plt.plot(point[0], point[1] + 20, ".")

    plt.savefig("./plot_point.png")
    print("success for BO")

def in_poly_model(point, poly):
    from task3_is_in_poly import is_in_poly
    plt.plot(point[0],point[1],".")
    polygon1 = Polygon(poly)
    plt.plot(*polygon1.exterior.xy)
    plt.savefig("./plot_point.png")

    return is_in_poly(point, poly)


def run(n,model):
    if model == 0:
        number =int(n)
        jarvis_model(number)
    elif model == 1:
        number = int(n)
        intersection_model(number)
    elif model == 2:
        number = int(n)
        BO_model(number)
    else:
        point=[int(n.split(":")[0].split(",")[0]),int(n.split(":")[0].split(",")[1])]
        poly=[[int(i.split(",")[0]),int(i.split(",")[1])] for i in n.split(":")[1:]]
        print(point,poly)
        #3,3:0,0:7,3:8,8:5,5
        print(in_poly_model(point,poly))





# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point():  # 在鼠标焦点处插入输入内容
    var = e.get()
    model=rad.get()
    n = var
    run(n,model)


image = None
im = None


def insert_end():  # 在文本框内容最后接着插入输入内容
    global im, image
    var = e.get()
    im = PIL.Image.open("./plot_point.png")
    # State the image location and import the image to the canvas
    #     # image_file = tk.PhotoImage(im)
    # Image location (relative path, same folder as .py file, can also use absolute path,
    # eed to give image specific absolute path)
    image = ImageTk.PhotoImage(im)
    label_img = tk.Label(window, image=image)
    label_img.pack()


# In step 6, create and place two buttons to trigger each of the two scenarios
b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()




# Step 8, the main window cycle display
window.mainloop()
