# -*- coding: utf-8 -*-

N = int(input())
S = []

for i in range(N):
    S.append(int(input()))

if sum(S)%10 != 0:
    print(sum(S))
    exit()

sumv = sum(S)
S.sort()

for s in S:
    if s % 10 != 0:
        sumv -= s
        print(sumv)
        exit()
print(0)