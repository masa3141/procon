# -*- coding: utf-8 -*-

X, Y = map(int, input().split())
cnt = 0
num = X
while num <= Y:
    cnt += 1
    num = num*2

print(cnt)
