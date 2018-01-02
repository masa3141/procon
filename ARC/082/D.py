# -*- coding: utf-8 -*-
from collections import Counter
import math
N = int(input())

Ps = list(map(int, input().split()))

V = [[]]
k = 0
tmp = 0

for i,p in enumerate(Ps):
    if i+1 == p:
        #print(tmp, i, p, V)
        if tmp == i:
            V[k].append(p)
            tmp = i+1
        else:
            V.append([])
            k += 1
            V[k].append(p)
            tmp = i+1
ans = 0
for v in V:
    ans += math.ceil(len(v)/2)

print(ans)
