import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

def root(x):
    if rank[x] < 0:
       return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return False
    if rank[x] > rank[y]:
        x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    return True
def is_same(x, y):
    return root(x) == root(y)
def size(x):
    return -rank[root(x)]


n = int(input())
rank = [-1] * n
Q = []
edge = defaultdict(int)
ng = set()
i = 0
for _ in range(int(input())):
    t, x, y, v = map(int, input().split())
    x, y = x - 1, y - 1
    if t == 0:
        unite(x, y)
        edge[(x, y)] = v
    else:
        Q.append((x, y, v))
        if not is_same(x, y):
            ng.add(i)
        i += 1

num = [0] * n
for i in range(1, n):
    num[i] = edge[(i - 1, i)] - num[i - 1]

for i, (x, y, v) in enumerate(Q):
    if i in ng:
        print('Ambiguous')
        continue

    if (y - x) % 2:
        print(num[x] - v + num[y])
    else:
        print(v - num[x] + num[y])