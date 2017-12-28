# -*- coding: utf-8 -*-


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_memo(n, memo):
    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

memo = [-1 for i in range(45)]

n = int(input())
print(fib_memo(n, memo))
