#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 14:46
# @Author  : Tuhailong
# @Site    : 
# @File    : 157island.py.py
# @Software: PyCharm Community Edition

"""
本题是一道非常经典的2D地图上的搜索问题，类似的问题还包括走迷宫、求房间数目等。

这道题需要我们求出三个数值，一是海岛数目，二是面积不同的海岛数目，三是形状不同的海岛数目。

第一个小问题是最基本的搜索问题。

一般我们可以从上到下、从左到右扫描，直到发现一个没有处理过的'#'。然后从这个'#'开始沿着4个方向扩展，把连在一起的'#'都找出来。这些连在一起的'#'就组成一个岛屿。
"""
"""
def get_map():
    map = [[0, 0, 0, '#', 0],
           ['#', '#', 0, '#', 0],
           [0, 0, '#', 0,'#'],
           [0, '#', '#', 0, '#']]
    return map


def gone(island_shape, island_area, map, x, y, has_gone_list, rows, colomns):      #在这个岛屿上游走开发
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        move_x = x + dx[i]
        move_y = y + dy[i]
        if 0 <= move_x < rows and 0 <= move_y < colomns:
            if map[move_x][move_y] == '#' and (move_x, move_y) not in has_gone_list:
                has_gone_list.append((move_x, move_y))
                island_shape.append([dx[i],dy[i]])
                island_area += 1
                island_shape, island_area, has_gone_list = gone(island_shape, island_area, map, move_x, move_y,has_gone_list, rows, colomns)

    return island_shape, island_area, has_gone_list


def get_island_information(map):
    island_num = 0
    island_area_list = []
    island_shape_list = []
    rows = len(map)
    colomns = len(map[0])
    has_gone_list = []
    for i in range(rows):
        for j in range(colomns):
            if map[i][j] == '#' and (i,j) not in has_gone_list:   #是岛屿并且没有被开发
                island_num += 1
                has_gone_list.append((i,j))
                island_area = 1
                island_shape = []
                island_shape, island_area, has_gone_list = gone(island_shape, island_area, map, i, j, has_gone_list, rows, colomns)  #在这个岛屿上进行开发游走
                island_area_list.append(island_area)
                island_shape_list.append(island_shape)

    return island_num, island_area_list, island_shape_list


if __name__ == "__main__":
    map = get_map()
    island_num, island_area_list, island_shape_list = get_island_information(map)
    print("一共有{0}个岛屿".format(island_num))
    #print("面积分别为：{0}".format(island_area_list))
    print("面积不同的岛屿数目：{0}".format(len(set(island_area_list))))
    island_shape_list_tmp = []
    shape_uni_num = 0
    for item in island_shape_list:
        if item not in island_shape_list_tmp:
            shape_uni_num += 1
            island_shape_list_tmp.append(item)
    print("不同形状岛屿的数目：{0}".format(shape_uni_num))
"""

###提交版本
"""
5 7
.####..  
.....#.  
####.#.  
.....#.  
..##.#. 
"""
def gone(island_shape, island_area, map, x, y, has_gone_list, rows, colomns):      #在这个岛屿上游走开发
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        move_x = x + dx[i]
        move_y = y + dy[i]
        if 0 <= move_x < rows and 0 <= move_y < colomns:
            if map[move_x][move_y] == '#' and (move_x, move_y) not in has_gone_list:
                has_gone_list.append((move_x, move_y))
                island_shape.append([dx[i],dy[i]])
                island_area += 1
                island_shape, island_area, has_gone_list = gone(island_shape, island_area, map, move_x, move_y,has_gone_list, rows, colomns)

    return island_shape, island_area, has_gone_list


def get_island_information(map):
    island_num = 0
    island_area_list = []
    island_shape_list = []
    rows = len(map)
    colomns = len(map[0])
    has_gone_list = []
    for i in range(rows):
        for j in range(colomns):
            if map[i][j] == '#' and (i,j) not in has_gone_list:   #是岛屿并且没有被开发
                island_num += 1
                has_gone_list.append((i,j))
                island_area = 1
                island_shape = []
                island_shape, island_area, has_gone_list = gone(island_shape, island_area, map, i, j, has_gone_list, rows, colomns)  #在这个岛屿上进行开发游走
                island_area_list.append(island_area)
                island_shape_list.append(island_shape)

    return island_num, island_area_list, island_shape_list

if __name__ == "__main__":
    one_row = input().split()
    N = int(one_row[0])
    M = int(one_row[1])
    map = []
    for i in range(N):
        row = []
        sign = input()
        for j in range(M):
            row.append(sign[j])
        map.append(row)
    island_num, island_area_list, island_shape_list = get_island_information(map)
    #print("一共有{0}个岛屿".format(island_num))
    #print("面积分别为：{0}".format(island_area_list))
    #print("面积不同的岛屿数目：{0}".format(len(set(island_area_list))))
    island_shape_list_tmp = []
    shape_uni_num = 0
    for item in island_shape_list:
        if item not in island_shape_list_tmp:
            shape_uni_num += 1
            island_shape_list_tmp.append(item)
    #print("不同形状岛屿的数目：{0}".format(shape_uni_num))
    print(island_num,len(set(island_area_list)),shape_uni_num)




