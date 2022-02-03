from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v, p):
    p1, p2 = 1, 1
    for nv in g[v]:
        if nv == p:
            continue
        dfs(nv, v)
        
        if C[v] == 'a':
            p1 *= dp[nv][0] + dp[nv][2]
        else:
            p1 *= dp[nv][1] + dp[nv][2]
        p1 %= MOD
        p2 *= dp[nv][0] + dp[nv][1] + dp[nv][2] * 2
        p2 %= MOD
    
    if C[v] == 'a':
        dp[v][0] = p1
    else:
        dp[v][1] = p1
    dp[v][2] = (p2 - p1 + MOD) % MOD


n = int(input())
C = input().split()
MOD = 10**9 + 7

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0] * 3 for _ in range(n)]
dfs(0, -1)

print(dp[0][2])