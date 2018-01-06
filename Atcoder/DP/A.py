# -*- coding: utf-8 -*-

N = int(input())
Ps = list(map(int, input().split()))

# i番目までの問題を解いて、得られる得点を格納しておく
dp = dict()
dp[0] = True
for p in Ps:
    tmp = dp.copy()
    for k, v in dp.items():
        tmp[k+p] = True
    dp = tmp
print(len(dp))