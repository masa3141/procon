# -*- coding: utf-8 -*-

def pertition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] <= pivot:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    i += 1
    tmp = A[i]
    A[i] = A[r]
    A[r] = tmp
    return i

def kselect(A, k):
    r = len(A)-1
    ind = pertition(A, 0, r)
    while ind != k-1:
        if ind < k-1:
            ind = pertition(A, ind, r)
        else:
            ind = pertition(A, 0, ind)
    return A[ind]

B = [6,3,2,5,4]
print(kselect(B,2))
print(B)