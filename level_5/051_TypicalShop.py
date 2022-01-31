from collections import defaultdict
from bisect import bisect

n, K, P = map(int, input().split())
A = list(map(int, input().split()))

mid = n // 2
B = A[:mid]
C = A[mid:]
lb, lc = len(B), len(C)

def culc(lis, m):
    case = defaultdict(list)
    for i in range(1 << m):
        ct = 0
        price = 0
        for j in range(m):
            if i >> j & 1:
                ct += 1
                price += lis[j]
        case[ct].append(price)
    return case

p1 = culc(B, lb)
p2 = culc(C, lc)
for k, v in p2.items():
    v.sort()

ans = 0
for k, vs in p1.items():
    just = K - k
    if just not in p2:
        if k == K:
            ans += 1
        continue
    
    for v in vs:
        lt = P - v
        ans += bisect(p2[just], lt)
print(ans)