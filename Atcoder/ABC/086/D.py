# -*- coding: utf-8 -*-

N, K = map(int, input().split())

xs = [{'ok':0,'ng':0} for i in range(K)]
ys = [{'ok':0,'ng':0} for i in range(K)]
zs = [[{'ok':0,'ng':0} for i in range(K)] for j in range(K)]
ok = 0
for i in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    x_bit = (x//K) % 2
    y_bit = (y//K) % 2
    x_mod = x%K
    y_mod = y%K
    color = ''
    flg = ''
    if (x_bit+y_bit) % 2 == 0:
        if c == 'W':
            ok += 1
            xs[x_mod]['ok'] += 1
            ys[y_mod]['ok'] += 1
            color = 'W'
            flg = 'ok'
        else:
            xs[x_mod]['ng'] += 1
            ys[y_mod]['ng'] += 1
            color = 'W'
            flg = 'ng'
    else:
        if c == 'B':
            ok += 1
            xs[x_mod]['ok'] += 1
            ys[y_mod]['ok'] += 1
            color = 'B'
            flg = 'ok'
        else:
            xs[x_mod]['ng'] += 1
            ys[y_mod]['ng'] += 1
            color = 'B'
            flg = 'ng'
    zs[y_mod][x_mod][flg] += 1


ans = [[0 for i in range(K)] for j in range(K)]

tmp = ok
for i in range(1,K):
    ans[0][i] = tmp - xs[i-1]['ok'] + xs[i-1]['ng']


# for j in range(1,K):
#     for i in range(1,K):
#         ans[j][i] = ans[j-1][i] - ys[j]['ok'] + xs[j]['ng']


tmp = ok
for j in range(1,K):
    ans[j][0] = tmp - ys[j-1]['ok'] + ys[j-1]['ng']

for i in range(1,K):
    for j in range(1,K):
        ans[i][j] = ans[i-1][j-1] - xs[i-1]['ok'] + xs[i-1]['ng']- ys[j-1]['ok'] + ys[j-1]['ng'] - (-zs[j-1][i-1]['ok']+zs[j-1][i-1]['ng'])


print(max(max(ans)))