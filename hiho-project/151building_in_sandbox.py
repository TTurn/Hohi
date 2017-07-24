#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 18:55
# @Author  : Tuhailong
# @Site    : 
# @File    : 151building_in_sandbox.py
# @Software: PyCharm Community Edition

#https://www.zhihu.com/question/42406890
"""
在 各个坐标是1到100的地图中放置块，放置的块要与之前的块连接，并且可达到。判断 输入的放置块的坐标是否符合标准。
"""
"""
思路：
判断块是否能放置 ：floodfill 方法从当前的块出发能够到达地图外。
"""
import math
def distance(x,y):
    return math.sqrt(pow(x[0]-y[0],2) + pow(x[1]-y[1],2) + pow(x[2]-y[2],2))

def walk(already_region, coordinate):
    if coordinate[0] == 10 or coordinate[1] == 10 or coordinate[2] == 10:                #当前点就是地图的边缘点
        return 1
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    for i in range(6):
        end = [coordinate[0]+dx[i], coordinate[1]+dy[i], coordinate[2]+dz[i]]        #游走之后的点
        if end[0] == 0 or end[1] == 0 or end[2] == 0:                                   #不能是下边界
            continue
        if end in already_region:                                                      #已经游走到过的点
            continue
        if end[0] == 10 or end[1] == 10 or end[2] == 10:                             #到达上边界
            return 1
        else:
            already_region.append(coordinate)
            #print(already_region)
            result = walk(already_region, end)
            if result == 1:
                return 1
    return 0

def run(coordinate_list):
    for i in range(1,len(coordinate_list)):
        if coordinate_list[i][2] != 1:
            sign = 0
            for j in range(i):
                if distance(coordinate_list[i],coordinate_list[j]) == 1:               #判断两个快是否相邻
                    sign = 1
                    break
            if sign == 0:
                return "No"
        sign = walk(coordinate_list[:i], coordinate_list[i])                           #游走能不能到达地图外
        if sign == 0:
            return "No"
    if sign == 0:
        return "No"
    else:
        return "Yes"

if __name__ == "__main__":
    example_num = int(input())
    result = []
    for i in range(example_num):
        cube_num = int(input())
        coordinate_list = []
        for i in range(cube_num):
            coordinate = input().split()
            coordinate = [int(x) for x in coordinate]
            coordinate_list.append(coordinate)
        sign = run(coordinate_list)
        result.append(sign)
    for sign in result:
        print(sign)