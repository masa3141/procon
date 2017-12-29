# -*- coding: utf-8 -*-
'''
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A&lang=jp
動的計画法
最大長方形
正方形の時の解法は使えない。ヒストグラムで解いていく。
'''

H, W = map(int, input().split())
C = list()
maxArea = 0

for h in range(H):
    C.append(list(map(int, input().split())))

#buf = [[-1 for w in range(W)] for h in range(H)]
T = [[float('inf') for w in range(W)] for h in range(H)]
for h in range(H):
    for w in range(W):
        if C[h][w] == 1:
            T[h][w] = 0
        else:
            if h==0:
                T[h][w] = 1
                continue
            T[h][w] = T[h-1][w] + 1

class Rectangle():
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos

def getLargestRectangle(size, buff):
    S = list()
    maxv = 0
    buff.append(0)
    for w in range(size+1):
        rect = Rectangle(buff[w], w)
        if len(S) ==0:
            S.append(rect)
            #print("len(S)=0,w=",w)
        else:
            if S[-1].height < rect.height:
                S.append(rect)
                #print("S[-1].height < rect.height,w=",w)
            elif S[-1].height > rect.height:
                target = w
                while len(S) > 0 and S[-1].height >= rect.height:
                    #print("S[-1].height > rect.height,w=",w,",target=",target)
                    pre = S.pop()
                    area = pre.height * (w - pre.pos)
                    maxv = max(maxv, area)
                    target = pre.pos
                rect.pos = target
                S.append(rect)
    return maxv

#print(T)

ans = 0
for h in range(H):
    ans = max(ans, getLargestRectangle(W, T[h]))


print(ans)



