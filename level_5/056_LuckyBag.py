n, s = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[''] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 'S'

for i, (a, b) in enumerate(ab):
    for j in range(s + 1):
        if j - a >= 0 and dp[i][j - a]:
            dp[i + 1][j] = 'A'
        if j - b >= 0 and dp[i][j - b]:
            dp[i + 1][j] = 'B'

if not dp[-1][-1]:
    print('Impossible')
    exit()

ans = []
j = s
for i in reversed(range(1, n + 1)):
    c = dp[i][j]
    ans.append(c)
    j -= ab[i - 1]['AB'.index(c)]
    
print(''.join(ans[::-1]))