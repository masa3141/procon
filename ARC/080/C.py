# -*- coding: utf-8 -*-
from collections import Counter
import math
N = int(input())

As = list(map(int, input().split()))

li2 = []
li4 = []
liother = []

for a in As:
    if a%4 == 0:
        li4.append(a)
    elif a%2 == 0:
        li2.append(a)
    else:
        liother.append(a)

if len(li4) >= len(liother):
    print('Yes')
elif len(li4) == len(liother)-1 and len(li2) == 0:
    print('Yes')
else:
    print('No')
