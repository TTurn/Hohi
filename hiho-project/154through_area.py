#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 13:49
# @Author  : Tuhailong
# @Site    : 
# @File    : 154through_area.py
# @Software: PyCharm Community Edition
"""
描述
作为H国的精英特工，你接到了一项任务，驾驶一辆吉普穿越布满监测雷达的禁区。为了简化题目，我们可以把禁区想象为一个左下角是(0, 0)右上角是( W, H )的长方形区域。区域中一共有 N 座雷达，其中第 i 座的坐标是(Xi, Yi )，监测范围是半径为 Ri 的圆形区域。所有在圆内和圆上的运载工具都会被监测到。

你的目标是从左到右穿越禁区。你可以选择线段(0, 0)-(0, H)上任意一点作为起点，线段(W, 0)-(W, H)上任意一点作为终点。在禁区内你可以沿任意路线行驶，只要保持始终在禁区内并且没有被雷达监测到。

给出禁区内的雷达部署方案，你需要判断是否存在满足条件的行驶路线。

输入
输入包含多组数据。

第1行是一个整数 T，表示以下有 T 组数据 (1 ≤ T ≤ 10)。

每组数据的第1行：三个整数 W, H, N (0 ≤ W, H ≤ 1000000, 1 ≤ N ≤ 1000)。

每组数据的第2-N+1行：每行三个整数Xi, Yi, Ri (0 ≤ Xi ≤ W, 0 ≤ Yi ≤ H, 1 ≤ Ri ≤ 1000000)。

输出
对于每组数据输出"YES"或者"NO"表示是否有满足条件的行驶路线。
"""
import math

def inter_compute(radar1, radar2):
    x1 = radar1[0]
    y1 = radar1[1]
    r1 = radar1[2]
    x2 = radar2[0]
    y2 = radar2[1]
    r2 = radar2[2]
    dictence = math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))
    if dictence > r1 + r2:
        sign = False
    else:
        sign = True
    return sign

def get_cluster(inter_info):
    cluster = []
    cluster.append([inter_info[0][0],inter_info[0][1]])
    for i in range(1,len(inter_info)):
        for item in cluster:
            if inter_info[i][0] in item or inter_info[i][1] in item:
                item.append(inter_info[i][0])
                item.append(inter_info[i][1])
            else:
                cluster.append([inter_info[i][0],inter_info[i][1]])
    return cluster

def through_area(cluster, radar_info):
    result = []
    for item in cluster:
        maxi = 0
        mini = 0
        for circle in item:
            maxi = max(radar_info[circle][1] + radar_info[circle][2],maxi)
            mini = min(radar_info[circle][1] - radar_info[circle][2],mini)
        result.append([maxi, mini])
    return result

def run(high, radar_info):
    radar_num = len(radar_info)
    inter_info = []
    for i in range(radar_num):
        for j in range(i+1,radar_num):
            sign = inter_compute(radar_info[i], radar_info[j])    #判断两两点之间是否相交
            if sign == True:
                inter_info.append((i,j))

    if len(inter_info) != 0:
        cluster = get_cluster(inter_info)            #相交是有传递性的，将相交的放在一起，为同一块区域
        result = through_area(cluster,radar_info)    #判断各个区域是否截断地图
        for item in result:
            if item[0] >= high and item[1] <= 0:
                return "NO"

    not_inter = [i for i in range(radar_num)]     #找到没有相交的单独点
    inter_list = []
    for item in inter_info:
        inter_list.append(item[0])
        inter_list.append(item[1])
    inter_set = set(inter_list)
    for item in inter_set:
        not_inter.remove(item)

    for index in not_inter:                       #单独点各自判断
        if radar_info[index][1] + radar_info[index][2] >= high and radar_info[index][1] - radar_info[index][2] <= 0:
            return "NO"
    return "YES"

if __name__ == "__main__":
    map_num = int(input())    #图的个数
    result_list = []
    for i in range(map_num):
        map_data = input().split()
        wide = int(map_data[0])
        high = int(map_data[1])
        radar_num = int(map_data[2])
        radar_info = []
        for i in range(radar_num):
            radar = input().split()
            radar_x = int(radar[0])
            radar_y = int(radar[1])
            radar_r = int(radar[2])
            radar_info.append((radar_x, radar_y, radar_r))

        result = run(high, radar_info)
        result_list.append(result)

    for result in result_list:
        print(result)
