# -*- coding: utf-8 -*-

H, W = map(int, input().split())
N = int(input())
As = list(map(int, input().split()))

status = 0 #0:下方向、1:右方向、2:上方向、3:左方向
x = 0
y = 0
switch = 0

ans = [[0 for i in range(H)] for j in range(W)]

for i in range(N):
    tmp = As[i]
    while tmp > 0:
        if status == 0:
            ans[x][y] = i+1
            if y == H-1-switch:
                x += 1
                status = 1
            else:
                y += 1
        elif status == 1:
            #print(x,y)
            ans[x][y] = i+1
            if x == W-1-switch:
                y -= 1
                status = 2
            else:
                x += 1
        elif status == 2:
            ans[x][y] = i+1
            if y == switch:
                x -= 1
                status = 3
                switch += 1
            else:
                y -= 1
        else:
            ans[x][y] = i+1
            if x == switch:
                y += 1
                status = 0
            else:
                x -= 1
        tmp -= 1

for h in range(H):
    for w in range(W):
        print(ans[w][h],end=' ')
        # if w != W-1:
        #     print(' ')
    print()



# 蛇腹で変えていく方法
# H, W = map(int, input().split())
# N = int(input())
# A = [int(x) for x in input().split()]
# board = [[0] * W for _ in range(H)]
# colors = [i + 1 for i in range(N) for _ in range(A[i])]

# for i in range(H):
#     if i % 2 == 0:
#         for j in range(W):
#             board[i][j] = colors[i * W + j]
#     else:
#         for j in range(W):
#             board[i][W-j-1] = colors[i * W + j]
# for row in board:
#     print(*row)

