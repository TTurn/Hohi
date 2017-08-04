#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 17:02
# @Author  : Tuhailong
# @Site    : 
# @File    : 148_Font_size.py
# @Software: PyCharm Community Edition

def run(N, P, W, H, count_para):
    #N：段落数  P：页数 W：屏幕宽 H：屏幕高 count_para：段落的字数
    result = min(W,H)
    for font_size in range(1,min(W,H)+1):
        lines = 0
        line_count = int(W/font_size)
        lines_num = int(H/font_size)
        all_lines = lines_num * P
        for i in range(N):
            if count_para[i] % line_count == 0:
                lines += int(count_para[i]/line_count)
            else:
                lines += int(count_para[i]/line_count)+1
        if lines > all_lines:
            result = font_size - 1
            break
    if result == 0:
        return False
    else:
        return result

if __name__ == "__main__":
    test_num = int(input())
    results = []
    for i in range(test_num):
        N, P, W, H = [int(x) for x in input().split()]
        count_para = [int(x) for x in input().split()]
        result = run(N, P, W, H, count_para)
        results.append(result)
    for result in results:
        print(result)