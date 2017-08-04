#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 22:06
# @Author  : Tuhailong
# @Site    : 
# @File    : 160code_com.py
# @Software: PyCharm Community Edition
"""
描述
小Hi希望压缩一个只包含大写字母'A'-'Z'的字符串。他使用的方法是：
如果某个子串 S 连续出现了 X 次，就用'X(S)'来表示。例如AAAAAAAAAABABABCCD可以用10(A)2(BA)B2(C)D表示。
此外，这种压缩方法是可以嵌套的，例如HIHOHIHOCODERHIHOHIHOCODER可以表示成2(2(HIHO)CODER)。
对于一个字符串 S ，合法的压缩表示可能有很多种。例如AAAAAAAAAABABABCCD还可以表示成9(A)3(AB)CCD。
小Hi希望知道其中最短的表示方法长度是多少。
输入
第一行一个正整数 T (1 ≤ T ≤ 10)，表示测试数据的组数。
以下 T 行每行一个字符串 S ，长度不超过100。
输出
对于每组数据，输出最短的表示方法的长度。
样例输入
3
ABC
AAAAAAAAAABABABCCD
HIHOHIHOCODERHIHOHIHOCODER
样例输出
3
12
15
"""
