# -*- coding: utf-8 -*-


N, K = map(int, input().split())

As = list(map(int, input().split()))

cnt = {}

for a in As:
    cnt.setdefault(a, 0)
    cnt[a] += 1

c = len(cnt)
ans = 0

for k, v in sorted(cnt.items(), key=lambda x:x[1]):
    if c <= K:
        break
    c -= 1
    ans += v

print(ans)


# # -*- coding: utf-8 -*-
# from collections import Counter
# def inpl(): return tuple(map(int, input().split()))

# N, K = inpl()
# A = inpl()
# C = Counter(A)

# print(sum(sorted(C.values(), reverse=True)[K:]))
