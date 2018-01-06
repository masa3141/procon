# -*- coding: utf-8 -*-

N, M = map(int, input().split())

from1 = []
gotoN = []

for m in range(M):
    a, b = list(map(int, input().split()))
    if a==1:
        from1.append(b)
    if b==N:
        gotoN.append(a)

can = set(from1) & set(gotoN)

if len(can) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
