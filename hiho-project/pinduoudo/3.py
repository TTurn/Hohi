#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 15:41
# @Author  : Tuhailong
# @Site    : 
# @File    : 3.py
# @Software: PyCharm Community Edition


#3      分糖果
student_num = int(input())
h_list = [int(x) for x in input().split()]
candy_num = int(input())
w_list = [int(x) for x in input().split()]
sort_h_list = sorted(h_list)
sort_w_list = sorted(w_list)
j = 0
num = 0
for i in range(candy_num):
    if j >= student_num:
       break
    elif sort_w_list[i] < sort_h_list[j]:
        continue
    else:
        j += 1
        num += 1
        continue
print(num)