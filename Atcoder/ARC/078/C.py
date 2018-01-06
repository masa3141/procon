# -*- coding: utf-8 -*-


N = int(input())
As = list(map(int, input().split()))

sum1 = 0
sum2 = sum(As)

min_diff = float('inf')

for a in As[0:len(As)-1]:
    sum1 += a
    sum2 -= a
    #print(abs(sum1 - sum2))
    min_diff = min(min_diff, abs(sum1 - sum2))
print(min_diff)