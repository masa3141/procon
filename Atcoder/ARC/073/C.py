# -*- coding: utf-8 -*-

N, T = map(int, input().split())

ts = list(map(int, input().split()))

ts.append(10**10)

ans = 0
for i in range(N):
    ans += min(ts[i+1]-ts[i], T)

print(ans)