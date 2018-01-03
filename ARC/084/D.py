# -*- coding: utf-8 -*-

K = int(input())

min_v = 100
for i in range(1,100000):
    tmp = K*i
    v = sum([int(c) for c in str(tmp)])
    min_v = min(min_v, v)
print(min_v)
