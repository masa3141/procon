# -*- coding: utf-8 -*-
import math
N, K = map(int, input().split())

ans = (N-K)*(N-K+1)//2

for i in range(1,N):
    if N%i >= K:
        ans += 1

print(ans)
