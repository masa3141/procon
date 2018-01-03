# -*- coding: utf-8 -*-
from collections import Counter
import math
A = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
Acnt = Counter(A)

ans = ''
flg = 1
while flg == 1:
    for c in alpha:
        print (c,Acnt[c])
        if Acnt[c] == 0:
            ans += c
            flg = 0
            break
        Acnt[c] -= 1
    if flg == 0:
        break
    else:
        ans += 'a'
print(ans)

