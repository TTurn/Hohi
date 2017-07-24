#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 18:25
# @Author  : Tuhailong
# @Site    : 
# @File    : 152region-perimeter.py
# @Software: PyCharm Community Edition
"""
描述
给定一个包含 N × M 个单位正方形的矩阵，矩阵中每个正方形上都写有一个数字。
对于两个单位正方形 a 和 b ，如果 a 和 b 有一条共同的边，并且它们的数字相等，那么 a 和 b 是相连的。
相连还具有传递性，如果 a 和 b 相连，b 和 c 相连，那么 a 和 c 也相连。
给定一个单位正方形 s，s 和与 s 相连的所有单位正方形会组成一个区域 R 。小Hi想知道 R 的周长是多少？
输入
第一行包含4个整数 N , M ，x 和 y ， N 和 M 是矩阵的大小， x 和 y 是给定的单位正方形 s 的坐标。(1 ≤ N , M ≤ 100, 0 ≤ x < N , 0 ≤ y < M )
以下是一个 N × M 的矩阵 A，Aij 表示相应的正方形上的数字。(0 ≤ Aij ≤ 100)
输出
输出一个整数表示 R 的周长。
"""

"""
解题思路：找到所有相邻的点，根据坐标判断相交的边界。
"""
def run(map, x, y, rows, colomns, already_walk, num):    #找到区域，返回区域面积和构成区域的点的坐标
    already_walk.append((x,y))
    #print(x,y,rows,colomns,already_walk,num)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        #print("i:{0}".format(i))
        afterx = x + dx[i]
        aftery = y + dy[i]
        #print((afterx, aftery))
        if (afterx,aftery) in already_walk:
            continue
        if 0<=afterx<rows and 0<=aftery<colomns:
            if map[afterx][aftery] == map[x][y]:
                num += 1
                num, already_walk = run(map, afterx, aftery, rows, colomns, already_walk, num)
    return num, already_walk


if __name__ == "__main__":
    input_str = input().split()
    rows = int(input_str[0])
    colomns = int(input_str[1])
    x = int(input_str[2])
    y = int(input_str[3])
    map = []
    for i in range(rows):
        map.append(input().split())
    """
6 5 2 1
0 0 1 2 2
3 1 1 3 7
4 3 1 3 7
4 3 0 3 2
4 3 3 0 1
4 5 5 5 5
    """
    result = 0
    already_walk = []
    num = 1
    result, already_walk = run(map, x, y, rows, colomns, already_walk, num)
    boundry_num = 0

    #根据区域中点的坐标判断点之间的相交边界
    for i in range(len(already_walk)):
        for j in range(i+1,len(already_walk)):
            if (already_walk[i][0] == already_walk[j][0] and abs(already_walk[i][1] - already_walk[j][1])== 1) or (already_walk[i][1] == already_walk[j][1] and abs(already_walk[i][0] - already_walk[j][0])== 1):
                 boundry_num += 1

    print(result*4 - boundry_num*2)