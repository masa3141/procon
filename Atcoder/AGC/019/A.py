# -*- coding: utf-8 -*-
import math
Q, H, S, D = map(int, input().split())
N = int(input())

one = min([Q*4, H*2, S])
two = D

cost1 = N * one
cost2 = N//2 * two + (N % 2) * one
#print(one, two, cost1, cost2)
# data = [Q*4, H*2, S, D/2]
# nums = [0.25, 0.5, 1, 2]
# price = [Q, H, S, D]
# data_index = sorted(range(len(data)), key=lambda k: data[k])
# #print(data,data_index)
# ans = 0
# for i in range(4):
#     ans += N//nums[data_index[i]] * price[data_index[i]]
#     N -= N//nums[data_index[i]] * nums[data_index[i]]
print(min(cost1, cost2))