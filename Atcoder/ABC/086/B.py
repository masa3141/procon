# -*- coding: utf-8 -*-
import math

a, b = input().split()
c = int(a+b)
#print(c, math.sqrt(c))

c_sqrt = math.floor(math.sqrt(c))
if c == c_sqrt*c_sqrt:
    print('Yes')
else:
    print('No')
