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

def kselect(A,l,r, k):
    mid = pertition(A,l,r)
    if mid == k:
        return A[mid]
    elif mid > k:
        return kselect(A,l,mid-1,k)
    else:
        return kselect(A,mid+1,r,k)

B = [6,3,2,5,4]
print(kselect(B,0,len(B)-1,4))
print(B)