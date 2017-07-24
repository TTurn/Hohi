#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 21:16
# @Author  : Tuhailong
# @Site    : 
# @File    : 149_forbidden.py
# @Software: PyCharm Community Edition

#https://hihocoder.com/contest/hiho149/problem/1
#匹配第一个


class TrieNode(object):
    def __init__(self):
        self.child = [None, None]
        self.value = None

class Trie(object):
    def __init__(self):
        self.nodes = [TrieNode()]

    def insert(self, binstr, index, allowed):   #插入节点
        pos = 0
        if len(binstr) == 0:
            self.nodes[0].value = (index, allowed)        
        for item in binstr:
            if self.nodes[pos].child[int(item)]:
                pos = self.nodes[pos].child[int(item)]
            else:
                self.nodes.append(TrieNode())
                self.nodes[pos].child[int(item)] = len(self.nodes) - 1
                pos = len(self.nodes) - 1
        if not self.nodes[pos].value:
            self.nodes[pos].value = (index, allowed)

    def find(self, binstr):        #查询节点
        pos = 0
        result = [self.nodes[pos].value]
        for item in binstr:
            if self.nodes[pos].child[int(item)]:
                pos = self.nodes[pos].child[int(item)]
                result.append(self.nodes[pos].value)
            else:
                break
        #print("result:{0}".format(result))
        mini = 1001
        access = "allow"
        for item in result:
            if item:
                if item[0] < mini:
                    mini = item[0]
                    access = item[1]
        return access

def binary(ip, mask = 32):         #转换为二进制
    s = ip.split('.')
    x = ''
    for i in range(4):
        x += str(bin(int(s[i]))[2:].rjust(8,'0'))    #bin生成的二进制数0b开头。所以取[2:]
    return x[:mask]


if __name__ == "__main__":
    n, m = map(int, input().split())
    trie = Trie()

    for i in range(n):
        sign, ip_mask = input().split()
        if '/' in ip_mask:
            ip, mask = ip_mask.split('/')
            mask = int(mask)
        else:
            ip = ip_mask
            mask = 32
        ip_binary = binary(ip, mask)

        trie.insert(ip_binary, i+1, sign)

    results = []
    for i in range(m):
        ip = input()
        ip_binary = binary(ip)
        #print(ip_binary)
        result = trie.find(ip_binary)
        if result == "allow":
            results.append("YES")
        else:
            results.append("NO")
    for result in results:
        print(result)



"""
5 5
allow 1.2.3.4/30
deny 1.1.1.1
allow 127.0.0.1
allow 123.234.12.23/3
deny 0.0.0.0/0
1.2.3.4
1.2.3.5
1.1.1.1
100.100.100.100
219.142.53.100
"""