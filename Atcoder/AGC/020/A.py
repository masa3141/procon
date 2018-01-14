# -*- coding: utf-8 -*-

N, A, B = map(int, input().split())

if (B-A-1) % 2 == 1:
    print("Alice")
else:
    print("Borys")