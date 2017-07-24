#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 10:38
# @Author  : Tuhailong
# @Site    : 
# @File    : 150Demo_day.py
# @Software: PyCharm Community Edition
#动态规划
"""
地图中有障碍物
从左上开始走，要走到右下，每次走动只能是向下或向右，并且只有碰到障碍物时才能改变方向

求要到达终点 最少改变多少次 地图中的状态（障碍物或没有障碍物）
"""

def fun(i, j, direct, map):
    if i < 0 or j < 0:
        return len(map) * len(map[0])
    if i == 0 and j == 0:
        return 0
    if direct == 0:               #每个点可以由前两个点得到 四种情况
        num1 = fun(i, j - 1, 0, map) + int(map[i][j] == 'b')
        num2 = fun(i, j - 1, 1, map) + int(map[i+1][j-1] != 'b') + int(map[i][j] == 'b')
        num3 = fun(i - 1, j, 1, map) + int(map[i][j] == 'b') + int(map[i+1][j] != 'b')
        num4 = fun(i - 1, j, 0, map) + int(map[i-1][j+1] != 'b') + int(map[i+1][j] != 'b') + int(map[i][j] == 'b')
        result = min(num1, num2, num3, num4)
        return result
    if direct == 1:
        num1 = fun(i, j-1, 0, map) + int(map[i][j+1] != 'b') + int(map[i][j] == 'b')
        num2 = fun(i, j-1, 1, map) + int(map[i+1][j-1] != 'b') + int(map[i][j] == 'b') + int(map[i][j+1] != 'b')
        num3 = fun(i-1, j, 0, map) + int(map[i-1][j+1] != 'b') + int(map[i][j] == 'b')
        num4 = fun(i-1, j, 1, map) + int(map[i][j] == 'b')
        result = min(num1, num2, num3, num4)
        return result

def run(map, i, j):        #因为 只能向下或者向右 所以终点只能由两个点得到
    result = min(fun(i-2, j-1, 1, map) + int(map[i-1][j-1] == 'b'), fun(i-1, j-2, 0, map) + int(map[i-1][j-1] == 'b'))
    return result


if __name__ == "__main__":
    row_1 = input().split()
    N = int(row_1[0])
    M = int(row_1[1])
    map = []
    for i in range(N):
        row_str = input()
        row_list = []
        for j in range(M):
            row_list.append(row_str[j])
        map.append(row_list)

    result = run(map, N-1, M-1)
    print(result)
"""
    4 8
    ....bb..
    ........
    .....b..
    ...bb...
"""