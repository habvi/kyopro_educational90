from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
tot = sum(a)
a2 = a * 2
ac = [0] + list(accumulate(a2))

m = 2 * n
r = 0
for l in range(m):
    while r < m and (ac[r] - ac[l]) <= tot / 10:
        if (ac[r] - ac[l]) == tot / 10:
            print('Yes')
            exit()
        r += 1

    if r == l:
        l += 1
print('No')