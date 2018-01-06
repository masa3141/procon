# -*- coding: utf-8 -*-

N = int(input())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

As.sort()
Bs.sort()
Cs.sort()

ans = 0
for a in As:
    for b in Bs:
        if a >= b:
            continue
        for c in Cs:
            if b >= c:
                continue
            #print(a,b,c)
            ans += 1

print(ans)

Bcnt = []

for b in Bs:
    i = 0
    while i < N and b < Cs[i]:


