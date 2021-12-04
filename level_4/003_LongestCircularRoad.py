import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p, d, dst):
    dst[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d + 1, dst)
    return dst

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x : int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

dist1 = [-1] * n
dist1 = dfs(0, -1, 1, dist1)

dist2 = [-1] * n
dist2 = dfs(dist1.index(max(dist1)), -1, 1, dist2)
print(max(dist2))