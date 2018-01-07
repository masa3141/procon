# -*- coding: utf-8 -*-
import heapq

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
    d[0] = 0
    heapq.heappush(q, (0, 0)) #(d[id], id)
    S = set()

    while len(S) != n:
        print(q)
        dist, node_id = heapq.heappop(q)
        S.add(node_id)
        for u, c in adj[node_id].items(): #隣接ノード
            if c + d[node_id] < d[u]:
                d[u] = c + d[node_id]
                heapq.heappush(q, (d[u], u))
    return d

if __name__ == '__main__':
    n = 10
    adj = []
    for i in range(n):
        adj.append(dict())
    for i in range(n):
        for j in range(2):
            adj[i][j] = i+j
            adj[j][i] = i+j
    print(adj)
    d = dijkstra(adj)
    print(d)