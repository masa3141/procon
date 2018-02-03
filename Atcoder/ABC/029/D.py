# -*- coding: utf-8 -*-
N = input()

n = len(N)
dp = [[[0 for i in range(2)] for j in range(2)] for k in range(n+1)]
print(dp[1])
print(dp[1][0])
dp[0][0][0] = 1
for i in range(n):
    for j in range(2):
        lim = 9 if j else int(N[i])
        for k in range(2):
            for d in range(lim+1):
                flg1 = int(j or lim<d)
                flg2 = int(k or d==1)
                print(i,j,k)
                dp[i+1][flg1][flg2] += dp[i][j][k]

ans = 0

for i in range(n):
    for j in range(2):
        for k in range(2):
            ans += dp[i][j][k]

print(dp)
print(ans)