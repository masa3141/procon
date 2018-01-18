# -*- coding: utf-8 -*-

def partition(A, p, r):
    '''

    :param A: List
    :param p: start index
    :param r: end index
    :return: index of partition
    '''
    x = A[r] # value at end index
    i = p - 1 # index where the value is under than partition
    for j in range(p, r, 1):
        if A[j] <= x: # パーティションの値より小さかったら
            i = i+1
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1

B = [4,7,3,6,5]

print(partition(B,0,4))

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

print(B)
quickSort(B,0,4)
print(B)
