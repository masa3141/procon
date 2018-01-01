# -*- coding: utf-8 -*-
import math

N, M = map(int, input().split())

p = int(math.pow(2, M))

ans = (100*(N-M) + 1900*M)*p

print(ans)
