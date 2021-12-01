from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    d[a].add(b)

print(sum(1 for v in d.values() if len(v) == 1))