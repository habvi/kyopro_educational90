from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs(v, p):
    sub[v] = 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        sub[v] += sub[nv]

n = int(input())
ab = []
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    ab.append((a, b))
    g[a].append(b)
    g[b].append(a)

sub = [0] * n
dfs(0, -1)

ans = 0
for i in range(n - 1):
    a, b = ab[i]
    mn = min(sub[a], sub[b])
    ans += mn * (n - mn)
print(ans)