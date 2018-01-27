# -*- coding: utf-8 -*-

N = int(input())
data = []
for i in range(N):
    x, y = map(int, input().split())
    data.append((x, y))
data.sort()


#上側の凸包を求める
def isClockwise(a, b):
    ax, ay = a
    bx, by = b
    cross = ax*by - ay*bx
    if cross <= 0:
        return True
    else:
        return False

ans1 = [data[0],data[1]]
for i in range(2,N):
    while True:
        ax, ay = ans1[-2]
        bx, by = ans1[-1]
        cx, cy = data[i]
        flg = isClockwise((bx-ax, by-ay), (cx-bx, cy-by))
        if flg:
            ans1.append(data[i])
            break
        else:
            ans1.pop()
            if len(ans1) == 1:
                ans1.append(data[i])
                break

ans2 = [data[-1],data[-2]]
for i in range(N-3,-1,-1):
    while True:
        ax, ay = ans2[-2]
        bx, by = ans2[-1]
        cx, cy = data[i]
        flg = isClockwise((bx-ax, by-ay), (cx-bx, cy-by))
        if flg:
            ans2.append(data[i])
            break
        else:
            ans2.pop()
            if len(ans2) == 1:
                ans2.append(data[i])
                break

ans2.reverse()
for i in range(len(ans1)-2,0,-1):
    ans2.append(ans1[i])

print(len(ans2))
for xy in ans2:
    x, y = xy
    print(x, y)