# -*- coding: utf-8 -*-

N = int(input())
mochi = []
for n in range(N):
    mochi.append(int(input()))

print(len(set(mochi)))