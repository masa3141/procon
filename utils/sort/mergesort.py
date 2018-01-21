# -*- coding: utf-8 -*-

def merge(A, l, mid, r):
    Ls = A[l:mid].copy()
    Rs = A[mid:r].copy()
    Ls.append(float('inf')) #番兵
    Rs.append(float('inf')) #番兵
    i = 0
    j = 0
    for k in range(l, r):
        if Ls[i] <= Rs[j]:
            A[k] = Ls[i]
            i += 1
        else:
            A[k] = Rs[j]
            j += 1


def mergeSort(A, l, r):
    if l+1 < r:
        mid = (l+r)//2
        mergeSort(A, l, mid)
        mergeSort(A, mid, r)
        merge(A, l, mid, r)

B = [3,6,2,4]

print(mergeSort(B,0,4))
print(B)