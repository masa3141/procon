# -*- coding: utf-8 -*-
import math
from collections import Counter
N = int(input())


def f(n):
    temp = n
    c = Counter()
    for i in range(2, n):
        if temp == 1:
            break
        while temp%i == 0:
            temp = temp//i
            c.update([i])
    else:
        c.update([temp])
    return c

c = Counter()
for i in range(2, N+1):
    c.update(f(i))

ans = 1
for _, x in c.items():
    ans = ans*(x+1) % 1000000007

print(ans)