# -*- coding: utf-8 -*-


def lcs(X, Y):
    memo = dict()
    for i in range(len(X)+1):
        memo[(i, 0)] = 0
    for j in range(len(Y)+1):
        memo[(0, j)] = 0
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                memo[(i+1,j+1)] = memo[i, j] + 1
            else:
                memo[(i+1,j+1)] = max(memo[i, j+1], memo[i+1, j])
    return memo[(len(X), len(Y))]


q = int(input())
for i in range(q):
    X = input()
    Y = input()
    n = lcs(X, Y)
    print(n)

