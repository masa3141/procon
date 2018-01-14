# -*- coding: utf-8 -*-
import math

N = int(input())
As = list(map(int, input().split()))

if As[-1] != 2:
    print(-1)
    exit()
if N == 1:
    print(2, 3)
    exit()

p_min = As[-1]
p_max = As[-1] + 1

for i in range(N-2,-1,-1):
    p_min = As[i] * math.ceil(p_min/As[i])
    p_max = As[i] * math.floor(p_max/As[i])
    if p_min > p_max:
        print(-1)
        exit()

    p_max = p_max + As[i] - 1


print(p_min, p_max)