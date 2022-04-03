from collections import deque

XY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def new(y, x, dir):
    return (y * w + x) * 4 + dir

def bfs(sy, sx):
    for dir in range(4):
        i = new(sy, sx, dir)
        dist[i] = 0

    que = deque([])
    for dir, (dy, dx) in enumerate(XY):
        ny, nx = sy + dy, sx + dx
        if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
            continue
        ni = new(ny, nx, dir)
        dist[ni] = 0
        que.append((ny, nx, dir))

    while que:
        y, x, dir = que.popleft()
        i = new(y, x, dir)
        if (y, x) == (gy, gx):
            print(dist[i])
            exit()

        d = dist[i]
        for ndir, (dy, dx) in enumerate(XY):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < h and 0 <= nx < w) or S[ny][nx] == '#':
                continue

            ni = new(ny, nx, ndir)
            if dir == ndir:
                if dist[ni] <= d:
                    continue
                dist[ni] = d
                que.appendleft((ny, nx, ndir))
            else:
                if dist[ni] <= d + 1:
                    continue
                dist[ni] = d + 1
                que.append((ny, nx, ndir))


h, w = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(h)]

INF = float('inf')
hwd = h * w * 4
dist = [INF] * hwd
bfs(sy, sx)