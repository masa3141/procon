# -*- coding: utf-8 -*-

'''
戦略
すべてのパターンをfor文で回す
'''

A, B, C, D, E, F = map(int, input().split())

V = []
max_water = 0
max_sato = 0
max_ratio = -1

maxA = F//(100*A)
maxB = F//(100*B)

waters = set()

for i in range(0, maxA+1):
    for j in range(0, maxB+1):
        water = 100*A*i + 100*B*j
        waters.add(water)

maxC = F // C
maxD = F // D
satos = set()
for k in range(0, maxC+1):
    for l in range(0, maxD+1):
        sato = C*k + D*l
        satos.add(sato)

for water in waters:
    for sato in satos:
        if water+sato > F or water+sato == 0:
            continue
        if sato > water/100 * E:
            continue
        #print(water, sato)
        ratio = sato/(water+sato)*100
        if ratio > max_ratio:
            max_water = water+sato
            max_sato = sato
            max_ratio = ratio
print(max_water, max_sato)
