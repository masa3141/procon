# -*- coding: utf-8 -*-
import math
N, H = map(int, input().split())
A = []
B = []
AB = []

for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append((a,b))

#A.sort()
#B.sort()
amax = max(A)
bmax = max(B)

B.sort(reverse=True)
i = 1
cnt = 1
H -= bmax

while H > 0:
    #print(i, B[i], N, H)
    if i < N and B[i] > amax:
        cnt += 1
        H -= B[i]
        i += 1
    else:
        cnt += math.ceil(H/amax)
        #print(H,amax, math.ceil(H/amax), math.ceil(H/amax) * amax)
        H -= math.ceil(H/amax) * amax
        #print(H)

print(cnt)
