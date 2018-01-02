# -*- coding: utf-8 -*-
from collections import Counter

N = int(input())

As = list(map(int, input().split()))

V = []
for a in As:
    V.append(a)
    V.append(a+1)
    V.append(a-1)

cnter = Counter(V)

#print(cnter.most_common(1))
key, ans = cnter.most_common(1)[0]

print(ans)
