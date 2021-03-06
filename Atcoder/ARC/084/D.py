# -*- coding: utf-8 -*-
import heapq

'''
方針：mod Kで考える。すべての数字は、１を足すor10倍するの操作を繰り返せば作ることができる。
1を足す場合は、fは1増える。10倍しても、fは増加しない。
'''

K = int(input())
adj = [dict() for i in range(K)]
for i in range(1,K):
    adj[i] = dict()
    adj[i][(i+1)%K] = 1
    adj[i][(i*10)%K] = 0

# print(adj)
# １から０への最短経路を見つける
# ダイクストラ法
def dijkstra(adj):
    '''
    :param adj: adj[i][j] distance between i and j
    adj = list(dict()) #隣接リスト形式
    :return: d[u]
    '''
    q = []  # プライオリティキュー
    d = dict()  # 始点からvまでの最短コスト
    p = dict()  # 親ノードを保存
    n = len(adj)  # ノードの数

    for i in range(n):
        d[i] = float('inf')
    # 初期化
    start_id = 1
    d[start_id] = 0
    heapq.heappush(q, (0,start_id)) #(d[id], id)
    S = set()

    while len(S) != n:
        # print(q)
        dist, node_id = heapq.heappop(q)
        S.add(node_id)
        for u, c in adj[node_id].items(): #隣接ノード
            # print(u,c)
            if c + d[node_id] < d[u]:
                d[u] = c + d[node_id]
                heapq.heappush(q, (d[u], u))
    return d



d = dijkstra(adj)
print(d[0]+1)
