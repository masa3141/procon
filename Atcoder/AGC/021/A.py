# -*- coding: utf-8 -*-
import math

# -*- coding: utf-8 -*-
N = input()
Nint = int(N)
Nlist = list(map(int,list(N)))
l = len(N)
ans = 0
for i in range(l-1, 0, -1):
    Nint -= ((int(N[i]) + 1) % 10) * 10**(l-i-1)
    N = str(Nint)


ans = sum(list(map(int,list(N))))
print(ans)
