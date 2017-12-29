# -*- coding: utf-8 -*-

n, m = map(int, input().split())
cs = list(map(int, input().split()))

f = dict() #k円で支払う時の、最小のコイン使用枚数
f[0] = 0
for k in range(1,n+1):
    f[k] = float('inf')
    for c in cs:
        if k - c < 0:
            continue
        f[k] = min(f[k], f[k - c] + 1)

print(f[n])
