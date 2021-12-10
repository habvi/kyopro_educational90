from itertools import product
from collections import defaultdict
h, w = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(h)]

ans = 0
for i in range(1, 1 << h):
    check = []
    for j in range(h):
        if i & (1<<j):
            check.append(p[j])

    cnt1 = bin(i).count('1')
    d = defaultdict(int)
    for nums in zip(*check):
        if len(set(nums)) == 1:
            d[nums[0]] += cnt1
    if d:
        ans = max(ans, max(d.values()))
print(ans)

'''
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3
'''