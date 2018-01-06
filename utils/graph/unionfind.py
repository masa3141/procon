# -*- coding: utf-8 -*-
import random
import math

'''
参考サイト
http://www.geocities.jp/m_hiroi/light/pyalgo61.html
'''

class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    # 部分集合とその要素数を返す
    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

size = 10
uf = UnionFind(size)
print(uf.table)
data = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(size)]
for x, y in data:
    uf.union(x, y)
print(uf.table)
for i in range(size):
    print(uf.find(i))
print(uf.subsetall())