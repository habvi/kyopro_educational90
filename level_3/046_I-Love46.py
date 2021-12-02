from collections import defaultdict
n = int(input())
K = 46
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

sa = defaultdict(int)
sb = defaultdict(int)
sc = defaultdict(int)
for i in range(n):
    sa[A[i] % K] += 1
    sb[B[i] % K] += 1
    sc[C[i] % K] += 1

ans = 0
for a, c1 in sa.items():
    for b, c2 in sb.items():
        for c, c3 in sc.items():
            abc = a + b + c
            if abc % K == 0:
                ans += (c1 * c2 * c3)
print(ans)