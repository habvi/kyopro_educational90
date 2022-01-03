k = int(input())
MOD = 10**9 + 7
if k % 9 != 0:
    print(0)
    exit()

dp = [0] * (k + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, k + 1):
    if i - 1 >= 0:
        dp[i] += dp[i - 1] * 2
    if i - 10 >= 0:
        dp[i] -= dp[i - 10]
    dp[i] %= MOD
print(dp[k])