n, q = map(int, input().split())
a = list(map(int, input().split()))
higher = [a[0]]
tot = 0
for i in range(n - 1):
    higher.append(a[i + 1] - a[i])
    tot += abs(a[i + 1] - a[i])
higher.append(-a[-1])

for _ in range(q):
    l, r, v = map(int, input().split())
    if l >= 2:
        tot -= abs(higher[l - 1])
        higher[l - 1] += v
        tot += abs(higher[l - 1])
    if r < n:
        tot -= abs(higher[r])
        higher[r] -= v
        tot += abs(higher[r])
    print(tot)