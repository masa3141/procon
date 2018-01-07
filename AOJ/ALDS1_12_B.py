# -*- coding: utf-8 -*-

# ダイクストラ法

import heapq
q = [] # プライオリティキュー


n = int(input())
V = dict() #隣接行列
d = dict() #始点からvまでの最短コスト
p = dict() #親ノードを保存
for i in range(n):
    data = list(map(int, input().split()))
    V[data[0]] = data[2:]
    d[data[0]] = float('inf')

d[0] = 0
heapq.heappush(q, (0, 0)) #(d[id], id)
S = set()

while len(S) != len(V):
    dist, node_id = heapq.heappop(q)
    S.add(node_id)
    for u, c in zip(V[node_id][0::2], V[node_id][1::2]): #隣接ノード
        if c + d[node_id] < d[u]:
            d[u] = c + d[node_id]
            heapq.heappush(q, (d[u], u))
            #print("Update:", u, d[u])
for i in range(n):
    print(i, d[i])