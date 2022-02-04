from math import degrees, atan2
from bisect import bisect

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]


def check(x):
    return  x if x <= 180 else 360 - x


ans = 0
for i, (x1, y1) in enumerate(xy):
    dgrs = set()
    for j, (x2, y2) in enumerate(xy):
        if i == j:
            continue

        dgr = degrees(atan2(y2 - y1, x2 - x1))
        dgrs.add(dgr if dgr >= 0 else dgr + 360)

    sd = sorted(dgrs)
    m = len(sd)

    for j, dgr in enumerate(sd):
        opposite = (dgr + 180) % 360
        close = bisect(sd, opposite)

        l = close % m
        if l == j:
            l = (l + 1) % m

        r = close - 1
        if r == j:
            r -= 1

        ans = max(ans, check(abs(dgr - sd[l])))
        ans = max(ans, check(abs(dgr - sd[r])))
print(ans)