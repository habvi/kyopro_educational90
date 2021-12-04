import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p, m):
    if m: one.append(v + 1)
    else: zero.append(v + 1)
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, 1 - m)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
zero, one = [], []
dfs(0, -1, 0)

if len(zero) >= n // 2:
    print(*zero[:n // 2])
else:
    print(*one[:n // 2])