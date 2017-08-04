#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 15:40
# @Author  : Tuhailong
# @Site    : 
# @File    : 1.py
# @Software: PyCharm Community Edition

#1         无序数组找三个数 使得乘积最大
num = int(input())
num_list = [int(item) for item in input().split()]

sort_num_list = sorted(num_list)
if sort_num_list[-3] >= 0:
    print(max(sort_num_list[-1]*sort_num_list[-2]*sort_num_list[-3],sort_num_list[-1]*sort_num_list[0]*sort_num_list[1]))
elif sort_num_list[-2] >= 0:
    print(sort_num_list[-1]*sort_num_list[-3]*sort_num_list[-4])
elif sort_num_list[-1] >= 0:
    print(sort_num_list[0]*sort_num_list[1]*sort_num_list[-1])
else:
    print(sort_num_list[-1] * sort_num_list[-2] * sort_num_list[-3])