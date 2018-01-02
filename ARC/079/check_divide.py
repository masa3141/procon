# -*- coding: utf-8 -*-
import math
N = int(input())

for i in range(N):
    for j in range(1,N):
        if i//j != math.floor(i/j):
            print(i,j)
