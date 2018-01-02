# -*- coding: utf-8 -*-

N, Z, W = map(int, input().split())

As = list(map(int, input().split()))

if len(As)==1:
    print(abs(W-As[-1]))
    exit()

print(max(abs(W-As[-1]), abs(As[-1]-As[-2])))
