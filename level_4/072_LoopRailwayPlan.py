import sys
sys.setrecursionlimit(10 ** 7)
def dfs(y, x, d):
    for dy, dx in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < h and 0 <= nx < w): continue
        if g[ny][nx] == "#": continue
        if dist[ny][nx] != -1: continue
        if (ny, nx) == (i, j):
            max_d[0] = max(max_d[0], d)
        dist[ny][nx] = d + 1
        dfs(ny, nx, d + 1)
        dist[ny][nx] = -1
    
h, w = map(int, input().split())
g = [input() for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == "#":
            continue
        dist = [[-1] * w for _ in range(h)]
        max_d = [0]
        dfs(i, j, 1)
        ans = max(ans, max_d[0])
print(ans if ans > 2 else -1)
