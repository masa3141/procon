# -*- coding: utf-8 -*-
import math
from collections import Counter
N = int(input())
As = list(map(int, input().split()))
M = 10**9 + 7
cnt = Counter(As)
ans = 1
if N%2 == 0:
    for i in range(0,N//2):
        if cnt[i*2+1] != 2:
            print(0)
            exit()

else:
    for i in range(1,N//2):
        if cnt[i*2] != 2:
            print(0)
            exit()
    if cnt[0] != 1:
        print(0)
        exit()

p = N//2
for i in range(p):
    ans = (ans*2) % M

print(ans)