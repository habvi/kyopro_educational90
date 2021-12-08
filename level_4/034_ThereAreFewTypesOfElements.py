from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
r = 0
d = defaultdict(int)
ans = 0
for l in range(n):
    while r < n and len(d) <= k:
        if len(d) == k and a[r] not in d:
            break
        d[a[r]] += 1
        r += 1
    
    ans = max(ans, r - l)
    if r == l:
        r += 1
    else:
        if d[a[l]] == 1:
            d.pop(a[l])
        else:
            d[a[l]] -= 1
print(ans)