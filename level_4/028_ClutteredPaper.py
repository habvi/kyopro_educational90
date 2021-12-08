n = int(input())
m = 1001
g = [[0] * m for _ in range(m)]
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    g[y1][x1] += 1
    g[y1][x2] -= 1
    g[y2][x1] -= 1
    g[y2][x2] += 1

for i in range(m):
    for j in range(m - 1):
        g[i][j+1] += g[i][j]

for i in range(m - 1):
    for j in range(m):
        g[i+1][j] += g[i][j]

ans = [0] * n
for i in range(m):
    for j in range(m):
        if g[i][j] != 0:
            ans[g[i][j] - 1] += 1
print(*ans)