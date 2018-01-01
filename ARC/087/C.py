# -*- coding: utf-8 -*-

N = int(input())

As = list(map(int, input().split()))

cnt = {}

for a in As:
    cnt.setdefault(a, 0)
    cnt[a] += 1

ans = 0
for k, v in cnt.items():
    #print(k, v)
    if v - k < 0:
        ans += v
    else:
        ans += v - k

print(ans)
