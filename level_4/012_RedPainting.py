import sys
sys.setrecursionlimit(10**7)

def root(x):
    if rank[x] < 0: return x
    rank[x] = root(rank[x])
    return rank[x]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y: return False
    if rank[x] > rank[y]: x, y = y, x
    rank[x] += rank[y]
    rank[y] = x
    return True
def is_same(x, y): return root(x) == root(y)
def size(x): return -rank[root(x)]

def hw(i, j):
    return i * w + j

def q1(a):
    r, c = a
    r -= 1; c -= 1
    G[r][c] = 1
    for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        ny, nx = r + dy, c + dx
        if not (0 <= ny < h and 0 <= nx < w): continue
        if G[ny][nx] == 0: continue
        if not is_same(hw(r, c), hw(ny, nx)):
            unite(hw(r, c), hw(ny, nx))

def q2(a):
    ra, rc, rb, cb = a
    ra -= 1; rc -= 1; rb -= 1; cb -= 1
    if G[ra][rc] == G[rb][cb] == 1 and is_same(hw(ra, rc), hw(rb, cb)):
        print('Yes')
    else:
        print('No')

h, w = map(int, input().split())
G = [[0] * w for _ in range(h)]
rank = [-1] * (h * w)
q = int(input())
for _ in range(q):
    num, *a = map(int, input().split())
    if num == 1:
        q1(a)
    else:
        q2(a)