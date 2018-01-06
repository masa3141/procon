# -*- coding: utf-8 -*-
import math

def eratos(N):
    '''
    input: N
    return: list[N+1]
    エラトステネスの篩
    0からNまでの素数の真偽値を格納したリストを返す
    整数nが素数なら、list[n]がTrue
    計算量：O(N log log N)
    メモリ領域：O(N)
    '''
    is_prime = [True for _ in range(N+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,N+1) :
        if not is_prime[i] :
            continue
        j = i*2
        while j<N :
            is_prime[j] = False
            j += i
    return is_prime

print(eratos(15))

def isPrime(n):
    '''
    input: n
    return: True or False
    整数nが素数なら、Trueを返す
    '''
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n))+1, 1):
        if n % i == 0:
            return False
    return True

for i in range(1,10,1):
    print(i," is prime?:",isPrime(i))



'''
リストをスタックやキューとして使う
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])


# 2進数
b = format(10, 'b') # '1010'

# 8進数
o = format(10, 'o') # '12'

# 16進数(小文字)
x = format(10, 'x') # 'a'

# 16進数(大文字)
X = format(10, 'X') # 'A'

d1 = int('1010', 2) # 10
d2 = int('12', 8) # 10
d3 = int('a', 16) # 10
d4 = int('A', 16) # 10


# 文字列の逆順
s = 'abc'
reverse = s[::-1] # 'cba'

# どちらも0が100個続くリスト([0, 0, ..., 0])を変数lに代入する
l = [0 for i in range(100)] # リスト内包表記を用いた初期化
l = [0] * 100 # *を用いた初期化

l = [[0 for j in range(10)] for i in range(10)]

l = [5, 1, 3, 4, 2]

print(sorted(l)) # [1, 2, 3, 4, 5]
print(l) # [5, 1, 3, 4, 2]
print(l.sort()) # None
print(l) # [1, 2, 3, 4, 5]

l.sort(reverse=True)
print(l) # [5, 4, 3, 2, 1]


l2 = [('hoge', 1), ('fuga', 3), ('piyo', 2), ('fuga', 1)]

# l2について，下記の2つは等価
print(sorted(l2)) # [('fuga', 1), ('fuga', 3), ('hoge', 1), ('piyo', 2)]
print(sorted(l2, key=lambda x: (x[0], x[1]))) # [('fuga', 1), ('fuga', 3), ('hoge', 1), ('piyo', 2)]

# 第2要素について降順ソートし，同じ値だったものについては第1要素について昇順ソートする
print(sorted(l2, key=lambda x: (-x[1], x[0]))) # [('fuga', 3), ('piyo', 2), ('fuga', 1), ('hoge', 1)]

l = [0, 1, 2, 3]

# push/enque
l.append(4)
print(l) # [0, 1, 2, 3, 4]

# pop
x = l.pop() # 4
print(l) # [0, 1, 2, 3]

# deque
y = l.pop(0) # 0
print(l) # [1, 2, 3]


from collections import deque

l = [0, 1, 2, 3]
q = deque(l)

# push/enque
q.append(4)
print(q) # deque([0, 1, 2, 3, 4])

# pop
x = q.pop() # 4
print(q) # deque([0, 1, 2, 3])

# deque
y = q.popleft() # 0
print(q) # deque([1, 2, 3])

# 優先度付きキュー
# http://lethe2211.hatenablog.com/entry/2014/12/30/011030

import heapq
q = [] # プライオリティキュー
heapq.heappush(q, 1) # 1をpush
#q
#[1]
heapq.heappush(q, 2) # 2をpush
#q
#[1, 2] # 1より2の方が優先度が低いので先頭以外に追加される
heapq.heappush(q, 0) # 0をpush
#q
#[0, 2, 1] # 0の優先度が最も高いので先頭に追加される
#heapq.heappop(q)
#0
#q
#[1, 2]
