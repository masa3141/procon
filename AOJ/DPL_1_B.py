# -*- coding: utf-8 -*-
'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp
動的計画法
ナップザック問題
'''
N, W = map(int, input().split())

class Item():
    def __init__(self, v, w):
        self.v = v
        self.w = w

items = []

for _ in range(N):
    v, w = map(int, input().split())
    item = Item(v, w)
    items.append(item)

C = dict()
for n in range(N+1):
    C[(n, 0)] = 0

for w in range(W+1):
    C[(0, w)] = 0

for n in range(1, N+1):
    for w in range(1, W+1):
        if w-items[n-1].w < 0:
            C[(n, w)] = C[(n-1, w)]
            continue
        C[(n, w)] = max(C[(n-1, w)], C[(n-1, w-items[n-1].w)] + items[n-1].v)

print(C[(n, w)])

