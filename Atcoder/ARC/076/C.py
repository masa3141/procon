# -*- coding: utf-8 -*-

N, M = map(int, input().split())

min_num = min(N, M)
max_num = max(N, M)
diff = abs(N-M)
K = 10**9 + 7

if diff >= 2:
    print(0)
    exit()

ans = 0
if diff == 1:
    ans = 1
else:
    ans = 2

for i in range(N):
    ans = ((i+1)*ans) % K

for i in range(M):
    ans = ((i+1)*ans) % K

print(ans)