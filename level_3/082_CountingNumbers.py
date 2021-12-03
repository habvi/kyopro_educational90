l, r = map(int, input().split())
MOD = 10**9 + 7
ans = 0
lenl, lenr = len(str(l)), len(str(r))

ans = 0
for i in range(lenl, lenr + 1):
    lo = max(l - 1, 10**(i - 1) - 1)
    hi = min(r, 10**i - 1)

    tot = hi * (hi + 1) // 2 - lo * (lo + 1) // 2 
    ans += i * tot
    ans %= MOD
print(ans)