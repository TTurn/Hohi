#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 17:05
# @Author  : Tuhailong
# @Site    : 
# @File    : 155task_assign.py
# @Software: PyCharm Community Edition
"""
描述
给定 N 项任务的起至时间( S1, E1 ), ( S2, E2 ), ..., ( SN, EN )， 计算最少需要多少台机器才能按时完成所有任务。
同一时间一台机器上最多进行一项任务，并且一项任务必须从头到尾保持在一台机器上进行。任务切换不需要时间。
输入
第一行一个整数 N，(1 ≤ N ≤ 100000)，表示任务的数目。 以下 N 行每行两个整数 Si, Ei，(0 ≤ Si < Ei ≤ 1000000000)，表示任务的起至时间。
输出
输出一个整数，表示最少的机器数目。
"""
"""
解题思路：
建立字典 起点的值为 1， 终点的值为 -1 
        对时间进行排序后遍历
        
    利用值的相加 求 机器数目
    
比如说 一直遇到的是 起点，那么 机器的数量就是加的，
      遇到 终点，那么 机器的数量是不变的
      一个点 既是起点又是终点 这个点可以拼接，直接去掉
"""

def run(pro_lines):
    points_dict = {}
    for lines in pro_lines:
        start_point = int(lines[0])
        points_dict.setdefault(start_point,0)
        end_point = int(lines[1])
        points_dict.setdefault(end_point,0)
        points_dict[start_point] += 1
        points_dict[end_point] -= 1
    print(points_dict)
    s = 0
    result = -1

    for point in sorted((points_dict.keys())):
        s += points_dict[point]
        result = max(result, s)
    return result

if __name__ == "__main__":
    num = int(input())
    pro_lines = []
    for i in range(num):
        lines = input().split()
        pro_lines.append(lines)
    result = run(pro_lines)
    print(result)










