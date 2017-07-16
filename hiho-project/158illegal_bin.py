#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 14:49
# @Author  : Tuhailong
# @Site    : 
# @File    : 158illegal_bin.py
# @Software: PyCharm Community Edition
"""
如果一个二进制数包含连续的两个1，我们就称这个二进制数是非法的。
小Hi想知道在所有n位二进制数（一共有2n个）中，非法二进制数有多少个。
例如对于 n = 3,有 011, 110, 111 三个非法二进制数。
由于结果可能很大，你只需要输出模109+7的余数。
"""

"""
解题思路1：
f[i] 表示i位数字，非法的个数
如果第i位为0 -> f[i] = f[i-1]
如果第i位为1 -> f[i-1] + 前i-2位数字是合法的，i-1位是1
用g[i]表示 第i-1位是1，前i-2位数字是合法的
用h[i]表示 第i位是0，前i-1位数字是合法的
f[i] = f[i-1] * 2 + g[i-1]
g[i] = h[i-1]
h[i] = 2^i - f[i] - g[i]
边界条件(需要思考一下)：
f[1] = 0, g[1] = 1, h[1] = 1
"""
"""
def get_f(n):
    if n > 0:
        f = get_f(n-1) * 2 + get_g(n-1)
    else:
        f = 0
    return f

def get_g(n):
    if n > 1:
        g = get_h(n-1)
    elif n == 1:
        g = 1
    else:
        g = 0
    return g

def get_h(n):
    if n > 1:
        h = pow(2, n) - get_f(n) - get_g(n)
    else:
        h = 1
    return h

if __name__ == "__main__":
    print("输入二进制位数：",end='')
    n = int(input())
    result = get_f(n)
    x = pow(10,9) + 7
    print("非法二进制数个数有{0}个".format(result%x))
"""



"""
考虑合法二进制的个数
f(1) = 2 
f(2) = 3
f(3) = 5
"""
#1.通过，列表的形式递推
def fibo(num):
    numList = [2,3]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList
if __name__ == "__main__":
    num = int(input())
    if num == 1:
        result = 0
    else:
        result = fibo(num)
        result = pow(2,num)-result[-1]
    print(result%(pow(10,9)+7))


#2.超时，递归的方法
"""
def get_f(n):
    if n == 0:
        f = 1
    elif n == 1:
        f = 2
    else:
        f = get_f(n-1) + get_f(n-2)
    return f
if __name__ == "__main__":
    n = int(input())
    result = get_f(n)
    result = pow(2,n)-result
    print(result%(pow(10,9)+7))
"""




