#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 15:41
# @Author  : Tuhailong
# @Site    : 
# @File    : 2.py
# @Software: PyCharm Community Edition

#2          大数相乘  输入输出都为字符串
def list2str(li):
    while li[0] == 0:
        del li[0]
    res = ''
    for i in li:
        res += str(i)
    return res

def multi(stra, strb):
    aa = list(stra)
    bb = list(strb)
    lena = len(stra)
    lenb = len(strb)
    result = [0 for i in range(lena + lenb)]
    for i in range(lena):
        for j in range(lenb):
            result[lena - i - 1 + lenb - j - 1] += int(aa[i]) * int(bb[j])
    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10
    return list2str(result[::-1])

if __name__ == '__main__':
    a, b = input().split()
    res = multi(a, b)
    print(res)