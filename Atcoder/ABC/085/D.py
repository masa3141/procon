# -*- coding: utf-8 -*-

N, H = map(int, input().split())
A = []
B = []
AB = []

for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append((a,b))

#A.sort()
#B.sort()
amax = max(A)
bmax = max(B)

amax_b = float('inf')
amax_index = 0
for i in range(N):
    a, b =AB[i]
    if amax == a and b < amax_b:
        amax_b = b
        amax_index = i
#B[amax_index] = 0
B.sort(reverse=True)
i = 1
cnt = 1
print(amax, amax_b, amax_index)
H -= bmax

flg = True
while H > 0:
    #print(i, B[i], N, H)
    if i < N and B[i] > amax:
        cnt += 1
        H -= B[i]
        i += 1
    elif i < N and B[i] == amax_b and flg:
        cnt += 1
        H -= B[i]
        i += 1
        #flg = False
    else:
        cnt += H//amax
        H -= (H//amax + 1) * amax
        #print(H,cnt)

print(cnt)
