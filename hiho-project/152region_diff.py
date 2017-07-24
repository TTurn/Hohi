#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 12:30
# @Author  : Tuhailong
# @Site    : 
# @File    : 152region_diff.py
# @Software: PyCharm Community Edition
"""
描述
给定两个区间集合 A 和 B，其中集合 A 包含 N 个区间[ A1, A2 ], [ A3, A4 ], ..., [ A2N-1, A2N ]，集合 B 包含 M 个区间[ B1, B2 ], [ B3, B4 ], ..., [ B2M-1, B2M ]。求 A - B 的长度。

例如对于 A = {[2, 5], [4, 10], [14, 18]}, B = {[1, 3], [8, 15]}, A - B = {(3, 8), (15, 18]}，长度为8。

输入
第一行：包含两个整数 N 和 M (1 ≤ N, M ≤ 100000)。

第二行：包含 2N 个整数 A1, A2, ..., A2N (1 ≤ Ai ≤ 100000000)。

第三行：包含 2M 个整数 B1, B2, ..., B2M (1 ≤= Bi ≤ 100000000)。

输出
一个整数，代表 A - B 的长度。
"""

def get_region(a_list, b_list):
    # 得到a区间
    a_dict = {}
    for point in a_list:
        start_point = point[0]
        a_dict[start_point] = 1
        end_point = point[1]
        a_dict[end_point] = -1
    sort_a_dict = sorted(a_dict.items(),key= lambda a_dict : a_dict[0])
    sign = 0
    A_list = []
    start_sign = 1
    for point in sort_a_dict:
        if start_sign == 1:
            start = point[0]
            start_sign = 0
        sign += point[1]
        if sign == 0:
            end = point[0]
            A_list.append((start,end))
            start_sign = 1
    #得到b区间
    b_dict = {}
    for point in b_list:
        start_point = point[0]
        b_dict[start_point] = 1
        end_point = point[1]
        b_dict[end_point] = -1
    sort_b_dict = sorted(b_dict.items(), key=lambda b_dict: b_dict[0])
    sign = 0
    B_list = []
    start_sign = 1
    for point in sort_b_dict:
        if start_sign == 1:
            start = point[0]
            start_sign = 0
        sign += point[1]
        if sign == 0:
            end = point[0]
            B_list.append((start, end))
            start_sign = 1
    return A_list, B_list



def run(A_list,B_list):
    all_dict = {}
    for item in A_list:
        start_point = item[0]
        all_dict[start_point] = 1
        end_point = item[1]
        all_dict[end_point] = -1
    for item in B_list:
        start_point = item[0]
        if start_point in all_dict.keys():
            all_dict[start_point] = 3
        else:
            all_dict[start_point] = 2
        end_point = item[1]
        if end_point in all_dict.keys():
            all_dict[end_point] = -3
        else:
            all_dict[end_point] = -2
    sort_dict = sorted(all_dict.items(), key=lambda all_dict: all_dict[0])

    a_result_list = []
    b_result_list = []
    #print(sort_dict)
    if sort_dict[0][1] == 1:
        a_result_list.append(1)
        b_result_list.append(0)
    if sort_dict[0][1] == 2:
        a_result_list.append(0)
        b_result_list.append(1)
    if sort_dict[0][1] == 3:
        a_result_list.append(1)
        b_result_list.append(1)

    for i in range(1,len(sort_dict)-1):
        if sort_dict[i][1] == 1:
            a_result_list.append(a_result_list[-1] + 1)
            b_result_list.append(b_result_list[-1])
        if sort_dict[i][1] == 2:
            a_result_list.append(a_result_list[-1])
            b_result_list.append(b_result_list[-1] + 1)
        if sort_dict[i][1] == 3:
            a_result_list.append(a_result_list[-1] + 1)
            b_result_list.append(b_result_list[-1] + 1)
        if sort_dict[i][1] == -1:
            a_result_list.append(a_result_list[-1] - 1)
            b_result_list.append(b_result_list[-1])
        if sort_dict[i][1] == -2:
            a_result_list.append(a_result_list[-1])
            b_result_list.append(b_result_list[-1] - 1)
        if sort_dict[i][1] == -3:
            a_result_list.append(a_result_list[-1] - 1)
            b_result_list.append(b_result_list[-1] - 1)
    region_list = []
    for i in range(1,len(sort_dict)):
        region_list.append(sort_dict[i][0]-sort_dict[i-1][0])
    return a_result_list, b_result_list,region_list


if __name__ == "__main__":

    row_1 = input().split()
    N = int(row_1[0])
    M = int(row_1[1])
    rows_2 = input().split()
    A_list = []
    for i in range(N):
        A_list.append((int(rows_2[2*i]),int(rows_2[2*i+1])))

    rows_3 = input().split()
    B_list = []
    for i in range(M):
        B_list.append((int(rows_3[2*i]),int(rows_3[2*i+1])))

    #A_list = [(2,5),(4,10),(14,18)]
    #B_list = [(1,3),(8,15)]
    #A_result, B_result = get_region(A_list, B_list)   #得到区间
    #print(A_result, B_result)
    a_result, b_result, region_result = run(A_list, B_list)
    result = 0
    for i in range(len(a_result)):
        if a_result[i] != 0 and b_result[i] == 0:
            result += region_result[i]
    print(result)

    """
3 2
2 5 4 10 14 18
1 3 8 15
    """





