#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 16:08
# @Author  : Tuhailong
# @Site    : 
# @File    : 153stack_price.py
# @Software: PyCharm Community Edition

"""
描述
小Hi最近在分析一支股票的价格走势，他需要一个程序来辅助分析。这个程序会接收3种消息（指令）：

价格信息，格式是P timestamp price：表示这支股票在 timestamp 时刻价格是 price。

删除价格指令，格式是R timestamp：随着时间推移，小Hi会积累越来越多的价格数据。一些老旧的数据会变得不重要。这个指定会删除 timestamp 以前（包括 timestamp 时刻）的价格数据。

价格查询指令，格式是Q：小Hi希望程序返回这只股票最高、最低和最近的价格。注意已经被删除的价格不应该被统计。

给定一个包含以上3种信息（指令）的序列，你能否帮助小Hi完成这个程序呢？

输入
第1行包含一个整数 N (1 ≤ N ≤ 500000)，表示消息（指令）序列的长度。

第2 - N+1行，每行包含一条消息或指令。

输入保证价格信息是按照 timestamp 升序排列的，并且出现的 timestamp 和价格小于100000000。

输出
对于输入中每一条价格查询指令，输出当时最高、最低和最近的价格。
"""
def save_price_info(price_info, timestamp, price):
    price_info.append((timestamp, price))
    return price_info

def del_price_info(price_info, timestamp):
    for i in range(len(price_info))[::-1]:
        if price_info[i][0] <= timestamp:
            break
    return price_info[i+1:]

def get_price_info(price_info):
    maxi = max([item[1] for item in price_info])
    mini = min([item[1] for item in price_info])
    print(maxi, mini, price_info[-1][1])

if __name__ == "__main__":
    num = int(input())
    price_info = []
    for i in range(num):
        operate = input().split()
        if len(operate) == 3:
            price_info = save_price_info(price_info, int(operate[1]),int(operate[2]))

        if len(operate) == 2:
            price_info = del_price_info(price_info, int(operate[1]))

        if len(operate) == 1:
            get_price_info(price_info)


"""
10
P 1 77
P 2 73
P 5 70
P 7 74
Q
R 4
Q
P 8 78
R 5
Q
"""

"""
77 70 74
74 70 74
78 74 78
"""