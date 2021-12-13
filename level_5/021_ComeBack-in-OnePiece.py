from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)
def dfs1(v):
    seen.add(v)
    for nv in gf[v]:
        if nv in seen:
            continue
        dfs1(nv)
    route.append(v)

def dfs2(v):
    seen.add(v)
    cnt[0] += 1
    for nv in gb[v]:
        if nv in seen:
            continue
        dfs2(nv)

n, m = map(int, input().split())
gf = defaultdict(list)
gb = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    gf[a].append(b)
    gb[b].append(a)

seen = set()
route = []
for i in range(n):
    if i in seen:
        continue
    dfs1(i)

seen = set()
ans = 0
for i in reversed(route):
    if i in seen:
        continue
    cnt = [0]
    dfs2(i)
    ans += cnt[0] * (cnt[0] - 1) // 2
print(ans)




'''
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3
'''