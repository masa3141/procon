# -*- coding: utf-8 -*-
import math
Q = int(input())

ls = []
rs = []
for n in range(Q):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)
    num = 0

max_r = max(rs)

def eratos(n):
    if n == 1:
        return set()
    primes = [1 for i in range(n+1)]
    primes[0] = 0
    primes[1] = 0
    for i in range(2,math.floor(math.sqrt(n))+1):
        if primes[i] == 1:
            j = i + i
            while j <= n:
                primes[j] = 0
                j = j + i
    return primes


def count_similar(era, n):
    count_similar = [0 for i in range(n+1)]
    for i in range(1,n+1):
        count_similar[i] = count_similar[i-1]
        if era[i] == 1 and era[int((i+1)/2)] == 1:
            count_similar[i] += 1
    return count_similar


era = eratos(max_r)
cnt = count_similar(era, max_r)

for l, r in zip(ls, rs):
    print(cnt[r] - cnt[l-1])

# is_prime = [True for _ in range(N)]
# is_prime[1] = False
# for i in range(2,N) :
#     if not is_prime[i] :
#         continue
#     j = i*2
#     while j<N :
#         is_prime[j] = False
#         j += i
