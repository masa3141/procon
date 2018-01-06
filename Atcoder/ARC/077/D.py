# -*- coding: utf-8 -*-
from collections import Counter

# 参考サイト
# http://arc058.contest.atcoder.jp/data/arc/058/editorial.pdf

N = int(input())
As = list(map(int, input().split()))
cnt = Counter(As)
dup, _ = cnt.most_common(1)[0]
# print(cnt.most_common(1)[0])
a = As.index(dup) #重複数字の最初の場所
As[a] = -1
b = As.index(dup) #重複数字の次の場所

MOD = 1000000007
inv = [0 if i > 2 else 1 for i in range(N + 2)]
pinv = [0 if i > 2 else 1 for i in range(N + 2)]
perm = [0 if i > 2 else 1 for i in range(N + 2)]
for i in range(2, N + 2):
    inv[i] = -int(MOD / i) * inv[MOD % i] + MOD
    pinv[i] = pinv[i - 1] * inv[i] % MOD
    perm[i] = perm[i - 1] * i % MOD
def C(n, m):
    return (perm[m] * pinv[n] % MOD) * pinv[m - n] % MOD if n <= m else 0


if N == 1:
    print(1)
    print(1)
    exit()


def nCr(n, r):
    # 10C7 = 10C3
    r = min(r, n-r)
    # Calculate the numerator.
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i
    for i in range(r, 1, -1):
        numerator //= i
    return numerator


# print(a,b)
print(N) #文字列1
for k in range(2, N):
    #tmp1 = nCr(N+1, k)
    #tmp2 = nCr(N-1+a-b, k-1)
    tmp1 = C(N+1, k)
    tmp2 = C(N-1+a-b, k-1)
    # print(tmp1, tmp2)
    print(tmp1-tmp2)
print(N+1) #文字列N
print(1) #文字列N+1

