#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 15:13
# @Author  : Tuhailong
# @Site    : 
# @File    : 161_tree_struct.py
# @Software: PyCharm Community Edition

"""
描述
给定一个包含 N 个顶点 M 条边的无向图 G ，判断 G 是不是一棵树。

输入
第一个是一个整数 T ，代表测试数据的组数。 (1 ≤ T ≤ 10)

每组测试数据第一行包含两个整数 N 和 M 。(2 ≤ N ≤ 500, 1 ≤ M ≤ 100000)

以下 M 行每行包含两个整数 a 和 b ，表示顶点 a 和顶点 b 之间有一条边。(1 ≤ a, b ≤ N)

输出
对于每组数据，输出YES或者NO表示 G 是否是一棵树。

样例输入
2
3 2
3 1
3 2
5 5
3 1
3 2
4 5
1 2
4 1
样例输出
YES
NO
"""

def run(data_list):
    if data_list[0] != data_list[1] + 1:
        return "NO"
    data = []
    data.append(data_list[2][0][0])
    data.append(data_list[2][0][1])
    for i in range(1,data_list[1]):
        if data_list[2][i][0] not in data:
            data.append(data_list[2][i][0])
        if data_list[2][i][1] not in data:
            data.append(data_list[2][i][1])
    if len(set(data)) == data_list[0]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    num = int(input())
    indata_list = []
    for i in range(num):
        indata = []
        n,m = [int(x) for x in input().split()]
        indata.append(n)
        indata.append(m)
        line_list = []
        for j in range(m):
            line = [int(x) for x in input().split()]
            line_list.append(line)
        indata.append(line_list)
        indata_list.append(indata)

    for i in range(num):
        result = run(indata_list[i])
        print(result)