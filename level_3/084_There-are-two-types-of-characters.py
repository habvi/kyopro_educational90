from itertools import groupby
n = int(input())
s = input()
ans = n * (n - 1) // 2

for k, g in groupby(s):
    m = len(list(g))
    ans -= m * (m - 1) // 2
print(ans)