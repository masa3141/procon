# -*- coding: utf-8 -*-
import math
H,W,D = map(int, input().split())

# Ah = np.array([0]*(H*W))
# Aw = np.array([0]*(H*W))
A = [0]*(H*W)
for h in range(H):
    As = list(map(int, input().split()))
    for w in range(W):
        A[As[w]-1] = (h,w)
    # Aw[As-1] = np.arange(W)
    # Ah[As-1] = h


Q = int(input())

# def solve(l, r):
#     ans = 0
#     # ah = Ah[l-1:r][::D]
#     # ans += np.sum(np.abs(ah[1:] - ah[0:-1]))
#     # aw = Aw[l-1:r][::D]
#     # ans += np.sum(np.abs(aw[1:] - aw[0:-1]))
#     ans = sum(Ah[l-1:l+D][::D])
#     while l != r:
#         x,y = A[l-1]
#         x2,y2 = A[l+D-1]
#         ans += abs(x-x2) + abs(y-y2)
#         l += D
#     return ans

Ans = [0]*(H*W)
aa = (H*W) // D
bb = (H*W) % D
for dth in range(1,aa+1):
    for d in range(D):
        if dth*D+d >=H*W:
            break
        x,y = A[(dth-1)*D+d]
        x2,y2 = A[dth*D+d]
        ans = abs(x-x2) + abs(y-y2)
        Ans[dth*D+d] = Ans[(dth-1)*D+d] + ans



lrs = []
for q in range(Q):
    L, R = map(int, input().split())
    print(Ans[R-1] - Ans[L-1])
    #lrs.append((L,R))

# for info in lrs:
#     L,R = info
#     print(solve(L, R))

