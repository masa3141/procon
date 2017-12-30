# -*- coding: utf-8 -*-
import math
N = int(input())
Cs = []
Ss = []
Fs = []
for n in range(N-1):
    C, S, F = map(int, input().split())
    Cs.append(C)
    Ss.append(S)
    Fs.append(F)

for n in range(N-1):
    current_time = 0
    for i in range(n,N-1,1):
        if Ss[i] - current_time <= 0:
            tmp = (current_time + Ss[i]) % Fs[i]
            wait_time = (Fs[i] - tmp) % Fs[i]
            #print('after first train')
            #print(n, i, wait_time)
        else:
            wait_time = (Ss[i] - current_time)
            #print('before first train')
            #print(n, i, wait_time)
        current_time += wait_time
        current_time += Cs[i]
        #print("current_time", current_time)
    print(current_time)
print(0)
