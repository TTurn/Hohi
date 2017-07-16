#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/7 9:49
# @Author  : Tuhailong
# @Site    : 
# @File    : 157bin-dec.py
# @Software: PyCharm Community Edition

#小数部分二进制和十进制之间的转换：乘2取整数部分。
#小数部分的最简分数形式 的分母 如果是 2 的 n 次 那么可以转成二进制小数

def split_figure(figure):
    integer = int(str(figure).split('.')[0])
    decimal = float("0." + str(figure).split('.')[1])
    return integer, decimal

def int2bin(integer):
    int2bin_list = []
    flag = True
    while flag:
        bin = integer % 2
        integer = integer // 2
        flag = integer
        int2bin_list.insert(0,bin)
    result = 0
    for item in int2bin_list:
        result = result * 10 + item
    return(result)

def dec2bin(decimal):
    length = len(str(decimal))
    dec2bin_list = []
    flag = True
    num = 1
    while(flag):
        if num == length:
            return "no"
        if decimal * 2 == 1:
            flag = False
        bin = int(str(decimal * 2).split('.')[0])
        dec2bin_list.insert(0,bin)
        decimal = float("0." + str(decimal * 2).split('.')[1])
        num += 1
    result = 0
    for item in dec2bin_list:
        result = result * 0.1 + item
    print(result)
    print(result * 0.10)
    return(result * 0.1)
if __name__ == "__main__":
    figure_list = [0.3,0.75,1.725]
    for i in range(len(figure_list)):
        integer, decimal = split_figure(figure_list[i])
        bin_int = int2bin(integer)
        bin_dec = dec2bin(decimal)
        if bin_dec == "no":
            print(bin_dec)
        else:
            print(bin_int+bin_dec)







