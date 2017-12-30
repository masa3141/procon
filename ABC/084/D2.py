# -*- coding: utf-8 -*-
import math
Q = int(input())

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    return True



ls = []
rs = []
for n in range(Q):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)
    num = 0
    for i in range(l, r+1, 2):
        #print(i, isPrime(i), isPrime((i+1)/2), isPrime((i+1)/2))
        if ((i+1)/2)%2 == 0 and (i+1)/2 != 2:
            continue
        else:
            if isPrime(i) and isPrime((i+1)/2):
                num += 1
    print(num)

