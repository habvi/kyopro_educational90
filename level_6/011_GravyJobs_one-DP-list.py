n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]

A.sort()
mx = 5000
INF = float('inf')
dp = [-INF] * (mx + 1)
dp[0] = 0

for d, c, s in A:
    for i in reversed(range(mx + 1)):
        if i + c <= min(d, mx):
            dp[i + c] = max(dp[i + c], dp[i] + s)

print(max(dp))