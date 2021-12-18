k = int(input())
MOD = 10**9 + 7
if k % 9 != 0:
    print(0)
    exit()

dp = [0] * (k + 1)
dp[0] = 1
for i in range(k):
    for j in range(1, 10):
        if i + j <= k:
            dp[i + j] += dp[i]
            dp[i + j] %= MOD
print(dp[k])