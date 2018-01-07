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

if N == 1:
    print(1)
    print(1)
    exit()


# def nCr(n, r):
#     # 10C7 = 10C3
#     r = min(r, n-r)
#     # Calculate the numerator.
#     numerator = 1
#     for i in range(n, n-r, -1):
#         numerator *= i
#     for i in range(r, 1, -1):
#         numerator //= i
#     return numerator
def modc(a,b,m):
    b = min(b, a-b)
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1,m) % m
    return c

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

#print(a,b)
print(N) #文字列1
for k in range(2, N):
    #tmp1 = nCr(N+1, k)
    #tmp2 = nCr(N-1+a-b, k-1)
    #tmp1 = C(N+1, k)
    #tmp2 = C(N-1+a-b, k-1)
    tmp1 = modc(N+1, k, MOD)
    tmp2 = modc(N-1+a-b, k-1, MOD)
    #print(tmp1, tmp2)
    print(tmp1-tmp2)
print(N+1) #文字列N
print(1) #文字列N+1

