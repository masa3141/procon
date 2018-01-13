# -*- coding: utf-8 -*-

N = int(input())
As = list(map(int, input().split()))

'''
方針
N/3から2N/3まで動かして、その時の差分の最大値を返す
前半では、要素を追加して、最小値を取り出す
後半では、要素を
'''


import heapq
q = [] # プライオリティキュー minヒープ
heapq.heappush(q, 1) # 1をpush
#q
#[1]
heapq.heappush(q, 2) # 2をpush
#q
#[1, 2] # 1より2の方が優先度が低いので先頭以外に追加される
heapq.heappush(q, 0) # 0をpush

q1 = []
sum_q1 = 0
sum_q1s = []

for i in range(0,N,1):
    heapq.heappush(q1, As[i])
    sum_q1 += As[i]
sum_q1s.append(sum_q1)
for i in range(N,2*N,1):
    heapq.heappush(q1, As[i])
    pop_q1 = heapq.heappop(q1)
    sum_q1 = sum_q1 - pop_q1 + As[i]
    sum_q1s.append(sum_q1)

q2 = []
sum_q2 = 0
sum_q2s = []

for i in range(2*N,3*N,1):
    heapq.heappush(q2, -As[i])
    sum_q2 += -As[i]
sum_q2s.append(sum_q2)
for i in range(2*N-1,N-1,-1):
    heapq.heappush(q2, -As[i])
    pop_q2 = heapq.heappop(q2)
    sum_q2 = sum_q2 - pop_q2 - As[i]
    sum_q2s.append(sum_q2)

max_value = -float('inf')
for i in range(0,N+1,1):
    max_value = max(max_value, sum_q1s[i] + sum_q2s[N-i])

print(max_value)