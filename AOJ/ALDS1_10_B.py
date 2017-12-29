# -*- coding: utf-8 -*-

'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=jp
動的計画法
連鎖行列積
'''

n = int(input())
p = []
m = dict()
for _ in range(n):
    r, c = map(int, input().split())
    p.append(r)
    if _ == n-1:
        p.append(c)

for i in range(n+1):
    m[(i,i)] = 0

for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        m[(i, j)] = float('inf')
        #print(l,i,j)
        for k in range(i, j):
            value = m[(i, k)] + m[(k+1, j)] + p[i-1]*p[k]*p[j]
            m[(i, j)] = min(m[(i, j)], value)

print(m[(1, n)])

