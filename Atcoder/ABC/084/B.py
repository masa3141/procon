# -*- coding: utf-8 -*-
A, B = map(int, input().split())
S = input()

data = S.split('-')

if len(data) != 2:
    print('No')
else:
    if len(data[0]) == A and len(data[1]) == B:
        if data[0].isdigit() and  data[1].isdigit():
            print('Yes')
        else:
            print('No')
    else:
        print('No')
