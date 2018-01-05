# -*- coding: utf-8 -*-

N = int(input())
As = list(map(int, input().split()))

dp = 1
cnt = dict()

for a in As:
    if a in cnt:
        dp = 2*(dp-cnt[a]) + 1
    else:
        cnt[a] = dp
        dp = 2*dp + 1
print(dp)