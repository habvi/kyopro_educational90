from collections import defaultdict
n, Q = map(int, input().split())
coords = defaultdict()
max_x, min_x = -float('inf'), float('inf')
max_y, min_y = -float('inf'), float('inf')
for i in range(n):
    x, y = map(int, input().split())
    mx, my = x - y, x + y
    coords[i + 1] = (mx, my)
    max_x = max(max_x, mx)
    min_x = min(min_x, mx)
    max_y = max(max_y, my)
    min_y = min(min_y, my)

for _ in range(Q):
    q = int(input())
    mx, my = coords[q]
    print(max(max_x - mx, mx - min_x, max_y - my, my - min_y))