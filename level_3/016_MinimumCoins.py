n = int(input())
a, b, c = map(int, input().split())
ans = float('inf')
for i in range(10000):
    for j in range(10000 - i):
        d = a*i + b*j
        if n - d < 0: continue
        if (n - d) % c == 0:
            ans = min(ans, i + j + (n - d)//c)
print(ans)