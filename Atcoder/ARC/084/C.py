# -*- coding: utf-8 -*-
import bisect
N = int(input())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

As.sort()
Bs.sort()
Cs.sort()

ans = 0
# for a in As:
#     for b in Bs:
#         if a >= b:
#             continue
#         for c in Cs:
#             if b >= c:
#                 continue
#             #print(a,b,c)
#             ans += 1
#
# print(ans)

Bcnt = [0 for i in range(N)]
i = 0
for b in Bs:
    cnt = N - bisect.bisect_right(Cs, b)
    # print(b, cnt)
    Bcnt[i] = cnt
    i += 1

Bsum = [0 for i in range(N)]
Bsum[N-1] = Bcnt[N-1]
for i in range(N-2, -1, -1):
    Bsum[i] = Bsum[i+1] + Bcnt[i]
    # print(i, Bsum)

for a in As:
    cnt = bisect.bisect_right(Bs, a)
    if cnt == N:
        ans += 0
    else:
        ans += Bsum[cnt]

# print(Bcnt)
# print(Bsum)
print(ans)