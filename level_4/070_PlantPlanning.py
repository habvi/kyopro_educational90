import statistics
n = int(input())
xs = []
ys = []
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    xy.append((x, y))

mx = int(statistics.median(xs))
my = int(statistics.median(ys))

ans = 0
for x, y in xy:
    ans += abs(mx - x) + abs(my - y)
print(ans)