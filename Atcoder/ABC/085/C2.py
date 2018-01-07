# -*- coding: utf-8 -*-

N, Y = map(int, input().split())

moneys = [10000, 5000, 1000]

man = 0
gosen = 0
sen = 0
'''
方針：とりあえず、できるかの計算
その後は、１万円札から５０００円に両替
その次に５０００円札を１００００円に両替していく
'''

max_man = Y//10000
max_gosen = Y//5000

for m in range(max_man, -1, -1):
    for g in range(max_gosen, -1, -1):
        s = N - m - g
        if s < 0:
            continue
        if 10000*m + 5000*g + 1000*s == Y:
            print(m,g,s)
            exit()
print(-1,-1,-1)