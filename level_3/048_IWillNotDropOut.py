n, k = map(int, input().split())
t = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(b)
    t.append(a - b)
print(sum(sorted(t, reverse=True)[:k]))