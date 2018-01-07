# -*- coding: utf-8 -*-
import random
import math


'''
参考サイト
https://qiita.com/lethe2211/items/6f78ae202e96e52a8cb9
'''

import itertools

l = range(1, 6) # [1, 2, 3, 4, 5]

# lから要素を2つ選んで並べる
# 重複は考慮しない
# 順序は考慮する(順列)
for elem in itertools.permutations(l, 2):
    print(elem) # elemには並べた要素のタプルが代入される

# lから要素を3つ選んで並べる
# 重複は考慮しない
# 順序は考慮しない(組合せ)
for elem in itertools.combinations(l, 3):
    print(elem)


# lの各要素を取り出したものの2つ組を並べる
# 重複は考慮する
# 順序は考慮しない
for elem in itertools.product(l, repeat=2):
    print(elem)


# default dict
from collections import defaultdict
l = ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']

dd = defaultdict(int) # すべてのキーが0で初期化される
for e in l:
    dd[e] += 1 # 初期化の必要がない
print(dd) # defaultdict(<type 'int'>, {'be': 2, 'that': 1, 'is': 1, 'question': 1, 'to': 2, 'not': 1, 'the': 1, 'or': 1})
print(dd['be']) # 2

dd2 = defaultdict(list) # すべてのキーが[]で初期化される
dd2['a'].append(1)
print(dd2) # defaultdict(<type 'list'>, {'a': [1]})


# Counter
from collections import Counter
l = ['to', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question']

# リストなどを引数に渡すと，自動的にカウントされる
c = Counter(l)
print(c) # Counter({'be': 2, 'is': 1, 'not': 1, 'or': 1, 'question': 1, 'that': 1, 'the': 1, 'to': 2})

# カウンタの値の降順にソート
print(c.most_common()) # [('be', 2), ('to', 2), ('that', 1), ('is', 1), ('question', 1), ('not', 1), ('the', 1), ('or', 1)]

# カウンタの値が最大のものから順に3つを出力
print(c.most_common(3)) # [('be', 2), ('to', 2), ('that', 1)]

# 上手く動いていない？
def nCr(n, r):
    # 10C7 = 10C3
    r = min(r, n-r)
    # Calculate the numerator.
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i
    for i in range(r, 1, -1):
        numerator //= i
    return numerator
    # Calculate the denominator. Should use math.factorial?
    # denominator = 1
    # for i in range(r, 1, -1):
    #     denominator *= i
    # return numerator // denominator

# Combinationの計算

# http://nemupm.hatenablog.com/entry/2015/01/03/234840
def modc(a,b,m):
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1,m) % m
    return c

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m