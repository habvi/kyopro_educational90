n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
tot = 0
for i in range(n):
    tot += abs(a[i] - b[i])
print('Yes' if tot <= k and tot % 2 == k % 2 else 'No')