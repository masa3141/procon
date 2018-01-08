# -*- coding: utf-8 -*-
import math
Q, H, S, D = map(int, input().split())
N = int(input())

data = [Q*4, H*2, S, D/2]
nums = [0.25, 0.5, 1, 2]
price = [Q, H, S, D]
data_index = sorted(range(len(data)), key=lambda k: data[k])
print(data,data_index)
ans = 0
for i in range(4):
    print(i,data_index[i], N//nums[data_index[i]], N//nums[data_index[i]] * price[data_index[i]])
    ans += N//nums[data_index[i]] * price[data_index[i]]
    N -= N//nums[data_index[i]]
print(N, ans)