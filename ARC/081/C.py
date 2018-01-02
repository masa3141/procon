# -*- coding: utf-8 -*-
from collections import Counter
import math
N = int(input())

As = list(map(int, input().split()))

cnter = Counter(As)
V = dict()
select = 0

for k, v in cnter.most_common():
    if v>=2:
        V[k] = math.floor(v/2)
#print(V)
tmp = 0
h = 0

if len(V) < 2:
    print(0)
    exit()

for k, v in sorted(V.items(), key=lambda x:-x[0]):
    if v >= 2 and tmp == 0:
        print(int(k*k))
        exit()
    else:
        if(tmp==1):
            print(int(h*k))
            exit()
        tmp += 1
        h = k


