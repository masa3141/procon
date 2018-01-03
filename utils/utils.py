# -*- coding: utf-8 -*-
import math

def eratos(N):
    '''
    input: N
    return: list[N+1]
    エラトステネスの篩
    0からNまでの素数の真偽値を格納したリストを返す
    整数nが素数なら、list[n]がTrue
    計算量：O(N log log N)
    メモリ領域：O(N)
    '''
    is_prime = [True for _ in range(N+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,N+1) :
        if not is_prime[i] :
            continue
        j = i*2
        while j<N :
            is_prime[j] = False
            j += i
    return is_prime

print(eratos(15))

def isPrime(n):
    '''
    input: n
    return: True or False
    整数nが素数なら、Trueを返す
    '''
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    return True

for i in range(1,10,1):
    print(i," is prime?:",isPrime(i))



'''
リストをスタックやキューとして使う
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])


