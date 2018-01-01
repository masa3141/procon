# -*- coding: utf-8 -*-

S = input()
n = len(S)
T = []

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        t = max(i+1, n-i-1)
        T.append(t)
if len(T) == 0:
    print(n)
else:
    print(min(T))
