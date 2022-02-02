from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

lis_l = [0]
left = []
inc = 0
for a in A:
    if a > lis_l[-1]:
        lis_l.append(a)
        inc += 1
    else:
        lis_l[bisect_left(lis_l, a)] = a
    left.append(inc)

lis_r = [0]
right = []
inc = 0
for a in reversed(A):
    if a > lis_r[-1]:
        lis_r.append(a)
        inc += 1
    else:
        lis_r[bisect_left(lis_r, a)] = a
    right.append(inc)
right = right[::-1]

ans = 0
for l, r in zip(left, right):
    ans = max(ans, l + r - 1)
print(ans)