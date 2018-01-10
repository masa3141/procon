# -*- coding: utf-8 -*-

H, W = map(int, input().split())


if H%3==0 or W%3==0:
    print(0)
    exit()

if H%3==1 and W%3==1:
    print(0)
    exit()

if (H%3==1 and W%3==2) or (H%3==2 and W%3==1):
    print(0)
    exit()

if H%3==2 and W%3==2:
    print(0)
    exit()