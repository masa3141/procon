# -*- coding: utf-8 -*-

N, W = map(int, input().split())

ws = []
vs = []

for i in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [{} for i in range(N)]
dp[0][ws[0]] = vs[0]
dp[0][0] = 0

for i in range(1,N):
    tmp = dp[i-1].copy()
    for key, value in tmp.items():
        dp[i].setdefault(ws[i]+key, 0)
        dp[i].setdefault(key, 0)
        #print(i, key, value, value+vs[i], dp[i][ws[i]+key])
        dp[i][ws[i]+key] = max(value+vs[i], dp[i][ws[i]+key])
        dp[i][key] = max(value,dp[i][key])

max_value = 0
for i in range(N):
    tmp = []
    for key, value in dp[i].items():
        if key <= W:
            tmp.append(value)
    if len(tmp)!=0:
        max_value = max(max_value, max(tmp))

#print(dp)
print(max_value)