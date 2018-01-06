# -*- coding: utf-8 -*-
from collections import Counter
import math
N = int(input())
S1 = input()
S2 = input()

i = 0
ans = 1
before = -1 #0:直前が縦、1:直前が横
while i < N :
    if S1[i] == S2[i]:#縦に置かれている
        if before == 1:#直前が横
            ans *= 1
        elif before == 0:#直前が縦
            ans *=2
        else:#最初
            ans *= 3
        ans = ans % 1000000007
        i += 1
        before = 0
    else:#横に置かれている
        if before == 1:#直前が横
            ans *= 3
        elif before == 0:#直前が縦
            ans *= 2
        else:#最初
            ans *= 6
        ans = ans % 1000000007
        i += 2
        before = 1

print(ans)


