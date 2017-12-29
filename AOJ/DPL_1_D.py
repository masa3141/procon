# -*- coding: utf-8 -*-
'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=jp
動的計画法
最長増加部分列
http://prdc.hatenablog.com/entry/2017/09/02/125842
'''
import bisect

n = int(input())
L = []

for i in range(n):
    a = int(input())
    z = bisect.bisect_left(L, a)
    if z >= len(L):
        L.append(a)
    else:
        L[z] = a

print(len(L))
