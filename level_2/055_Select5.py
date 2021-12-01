from itertools import combinations
n, p, q = map(int, input().split())
A = tuple(map(lambda x : int(x) % p, input().split()))

ans = 0
for (c0, c1, c2, c3, c4) in combinations((i for i in range(n)), 5):
    k = 1
    for c in (c0, c1, c2, c3, c4):
        k *= A[c]
        k %= p
    if k == q:
        ans += 1
print(ans)