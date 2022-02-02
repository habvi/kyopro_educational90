from bisect import bisect, bisect_left

n = int(input())
A = list(map(int, input().split()))

lis_l = [0]
left = []
for a in A:
    if a > lis_l[-1]:
        lis_l.append(a)
        left.append(len(lis_l) - 1)
    else:
        bi = bisect_left(lis_l, a)
        lis_l[bi] = a
        left.append(bi)

lis_r = [0]
right = []
for a in reversed(A):
    if a > lis_r[-1]:
        lis_r.append(a)
        right.append(len(lis_r) - 1)
    else:
        bi = bisect_left(lis_r, a)
        lis_r[bi] = a
        right.append(bi)
right = right[::-1]

ans = 0
for l, r in zip(left, right):
    ans = max(ans, l + r - 1)
print(ans)