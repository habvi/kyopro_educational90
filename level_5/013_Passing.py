from collections import defaultdict
import heapq
def dijkstra(st):
    dst = [float('inf')]*n
    dst[st] = 0
    hq = [(0, st)]
    while hq:
        c, v = heapq.heappop(hq)
        if c > dst[v]: continue
        for nc, nv in g[v]:
            if c + nc >= dst[nv]: continue
            dst[nv] = c + nc
            heapq.heappush(hq, (c + nc, nv))
    return dst

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    g[a].append((c, b))
    g[b].append((c, a))

left = dijkstra(0)
right = dijkstra(n - 1)
for l, r in zip(left, right):
    print(l + r)