# -*- coding: utf-8 -*-

N = int(input())

tc = 0
xc = 0
yc = 0
ok_flg = 1
for n in range(N):
    t, x, y = map(int, input().split())
    t_diff = tc - t
    x_diff = abs(x - xc)
    y_diff = abs(y - yc)
    xy_diff = x_diff + y_diff
    if t%2 == 0:
        if xy_diff <= t and xy_diff%2 ==0:
            continue
        else:
            ok_flg = 0
    else:
        if xy_diff <= t and xy_diff%2 ==1:
            continue
        else:
            ok_flg = 0
if ok_flg == 1:
    print('Yes')
else:
    print('No')