#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 15:42
# @Author  : Tuhailong
# @Site    : 
# @File    : 4.py
# @Software: PyCharm Community Edition

"""
假设一个探险家被困在了地底的迷宫之中，要从当前位置开始找到一条通往迷宫出口的路径。迷宫可以用一个二维矩阵组成，有的部分是墙，有的
部分是路。迷宫之中有的路上还有门，每扇门都在迷宫的某个地方有与之匹配的钥匙，只有先拿到钥匙才能打开门，请设计一个算法，帮助探险家
找到脱困的最短路径。如前所述，迷宫是通过一个二维矩阵表示的，每个元素的值的含义如下 0-墙  1-路  2-探险家的起始位置，3-迷宫的出口，大
写字母-门，小写字母-对应大写字母所代表的门的钥匙。

输入
迷宫的地图，用二维矩阵表示。第一行表示矩阵的行数和列数M,N
后面的M行是矩阵的数据，中间没有空格

输出
路径长度

5 5
02111
01a0A
01003
01001
01111

"""
def run(res,num,key,map,x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or next_x > len(map[0]) or next_y < 0 or next_y > len(map):
            continue
        if map[next_x][next_y] == '0':
            continue
        if 'a'<= map[next_x][next_y] <= 'z':
            key.append(map[next_x][next_y])
        if 'A' <= map[next_x][next_y] <= 'Z' and map[next_x][next_y]-'A'+'a' not in key:
            continue
        if map[next_x][next_y] == '3':
            res.append(num)
            continue
        else:
            num += 1
            run(res,num,key,map,next_x,next_y)
    return res

if __name__=="__main__":
    m,n = [int(x) for x in input().split()]
    #print(m,n)
    map = []
    num = 0
    for i in range(m):
        row = [x for x in input()]
        map.append(row)
    #print(map)
    key = []
    res = []
    for i in range(m):
        for j in range(n):
            if map[i][j] == '2':
                result = run(res,num,key,map,i,j)
                print(min(result))
                break
        break