def comb(n, r, MOD):
    if n < r or n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    nmrt = fact[n]
    dnmnt = invfact[n - r] * invfact[r] % MOD
    return nmrt * dnmnt % MOD


n = int(input())
MOD = 10**9 + 7

lenc = n + 10
fact, invfact = [1] * lenc, [1] * lenc
for i in range(1, lenc):
    fact[i] = fact[i - 1] * i % MOD

invfact[lenc - 1] = pow(fact[lenc - 1], MOD - 2, MOD)
for i in range(lenc - 1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

for diff in range(1, n + 1):
    ans = 0
    for i in range(1, n // diff + 2):
        ans += comb(n - (diff - 1)*(i - 1), i, MOD)
        ans %= MOD
    print(ans)