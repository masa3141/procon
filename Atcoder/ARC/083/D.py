# -*- coding: utf-8 -*-

N = int(input())

adj = []

for i in range(N):
    adj.append(dict(zip(range(N), list(map(int, input().split())))))
    del adj[i][i]
print(adj)

import heapq

# ダイクストラ法
def dijkstra(adj, start_id):
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
    d[start_id] = 0
    heapq.heappush(q, (0, start_id)) #(d[id], id)
    S = set()

    while len(S) != n:
        dist, node_id = heapq.heappop(q)
        S.add(node_id)
        for u, c in adj[node_id].items(): #隣接ノード
            if c + d[node_id] < d[u]:
                d[u] = c + d[node_id]
                heapq.heappush(q, (d[u], u))
    return d

for i in range(N):
    d = dijkstra(adj, i)
    del d[i]
    if d != adj[i]:
        print(-1)
        exit()


class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    # 部分集合とその要素数を返す
    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

S = set([0])
q = []
uf = UnionFind(N)
cost = 0
visited = []
for i in range(1,N):
    heapq.heappush(q, (adj[0][i], 0, i))
while len(S) != N:
    d, s_id, t_id = heapq.heappop(q)
    visited.append((s_id, t_id))
    print(d, s_id, t_id)
    if uf.find(s_id) != uf.find(t_id):
        uf.union(s_id, t_id)
        S.add(t_id)
        cost += d
    for k, v in adj[t_id].items():
        if (t_id, k) in visited:
            heapq.heappush(q, (v, t_id, k))

print(d)