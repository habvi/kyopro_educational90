from math import degrees, atan2
from bisect import bisect

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]


def check(x):
    return  x if x <= 180 else 360 - x


ans = 0
for i, (x1, y1) in enumerate(xy):
    angles = set()
    for j, (x2, y2) in enumerate(xy):
        if i == j:
            continue

        angle = degrees(atan2(y2 - y1, x2 - x1))
        angles.add(angle if angle >= 0 else angle + 360)

    sa = sorted(angles)
    m = len(sa)

    for j, angle in enumerate(sa):
        opposite = (angle + 180) % 360
        close = bisect(sa, opposite)

        l = close % m
        if l == j:
            l = (l + 1) % m

        r = close - 1
        if r == j:
            r -= 1

        ans = max(ans, check(abs(angle - sa[l])))
        ans = max(ans, check(abs(angle - sa[r])))
print(ans)