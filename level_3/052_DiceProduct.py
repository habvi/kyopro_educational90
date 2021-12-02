n = int(input())
MOD = 10**9 + 7
ans = 1
for _ in range(n):
    a = sum(map(int, input().split()))
    ans *= a
    ans %= MOD
print(ans)