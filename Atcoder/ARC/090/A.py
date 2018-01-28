# -*- coding: utf-8 -*-
N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

for i in range(1,N):
    A1[i] = A1[i] + A1[i-1]

ans = A2.copy()
ans[0] += A1[0]

for i in range(1,N):
    ans[i] = max(A1[i]+A2[i], ans[i-1]+A2[i])

print(ans[N-1])