#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 21:49
# @Author  : Tuhailong
# @Site    : 
# @File    : jsut.py
# @Software: PyCharm Community Edition
num = int(input())
price_info = []
for i in range(num):
    operate = input().split()
    if len(operate) == 3:
        price_info.append((int(operate[1]), int(operate[2])))

    if len(operate) == 2:
        for i in range(len(price_info))[::-1]:
            if price_info[i][0] <= int(operate[1]):
                break
        price_info = price_info[i+1:]

    if len(operate) == 1:
        maxi = max([item[1] for item in price_info])
        mini = min([item[1] for item in price_info])
        print(maxi, mini, price_info[-1][1])