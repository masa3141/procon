# -*- coding: utf-8 -*-

S = input()
ans = ''
for i, s in enumerate(S):
    if i!= 3:
        ans += s
    else:
        ans += '8'
print(ans)