# -*- coding: utf-8 -*-

N = int(input())
As = list(map(int, input().split()))

results = []

ans = 0
sum_a = 0
flg = 1

for a in As:
    if flg == 1:
        if 1 <= sum_a + a:
            sum_a += a
        else:
            a_ = 1 - sum_a
            ans += 1 - sum_a - a
            sum_a = 1
        #print(a,sum_a,ans)
    else:
        if sum_a + a <= -1:
            sum_a += a
        else:
            a_ = -1 - sum_a
            ans += +1 + sum_a + a
            sum_a = -1
        #print(a,sum_a,ans)
    flg *= -1

results.append(ans)

ans = 0
sum_a = 0
flg = -1

for a in As:
    if flg == 1:
        if 1 <= sum_a + a:
            sum_a += a
        else:
            a_ = 1 - sum_a
            ans += 1 - sum_a - a
            sum_a = 1
        #print(a,sum_a,ans)
    else:
        if sum_a + a <= -1:
            sum_a += a
        else:
            a_ = -1 - sum_a
            ans += +1 + sum_a + a
            sum_a = -1
        #print(a,sum_a,ans)
    flg *= -1

results.append(ans)

print(min(results))