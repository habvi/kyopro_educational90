from itertools import permutations
from collections import defaultdict
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
d = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    d[x].append(y)
    d[y].append(x)

if n == 1:
    print(a[0][0])
    exit()

ans = float('inf')
for pr in permutations((i for i in range(n))):
    t = 0
    ok = True
    for i in range(n - 1):
        if pr[i] in d[pr[i + 1]]:
            ok = False
            break
        t += a[pr[i]][i]
    else:
        t += a[pr[-1]][i + 1]

    if ok:
        ans = min(ans, t)
print(ans if ans != float('inf') else -1)