n, q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(q)]
MOD = 10**9 + 7
K = 60

ans = 1
for k in range(K):
    mul = 0
    for bit in range(1 << n):
        ok = True
        for x, y, z, w in A:
            x, y, z = x - 1, y - 1, z - 1
            if (bit >> x & 1) | (bit >> y & 1) | (bit >> z & 1) != (w >> k & 1):
                ok = False
                break
        if ok:
            mul += 1
    ans *= mul
    ans %= MOD

print(ans)