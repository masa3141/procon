# -*- coding: utf-8 -*-
import math
from collections import Counter
N = int(input())

S = []
for n in range(N):
    S.append(input()[0])

S_cnt = Counter(S)

cond = [['M','A','R'],
        ['M','A','C'],
        ['M','A','H'],
        ['M','R','C'],
        ['M','R','H'],
        ['M','C','H'],
        ['A','R','C'],
        ['A','R','H'],
        ['A','C','H'],
        ['R','C','H']]

ans = 0
for li in cond:
    ans += S_cnt[li[0]] * S_cnt[li[1]] * S_cnt[li[2]]
print(ans)
