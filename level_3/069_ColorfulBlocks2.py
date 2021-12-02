n, k = map(int, input().split())
MOD = 10**9 + 7
if n == 1:
    print(k)
    exit()
if n == 2 and k < 2:
    print(0)
    exit()

print(k * (k - 1) * pow(k - 2, n - 2, MOD) % MOD)
