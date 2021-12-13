def is_ok(x):
    tot = 0
    i = 0
    cnt = K
    while cnt > 0:
        while i < n + 1:
            if tot >= x:
                break
            tot += d[i]
            i += 1
        if i == n + 1:
            return cnt == 0 and tot >= x
        tot = 0
        cnt -= 1
    return sum(d[i:]) >= x

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, L = map(int, input().split())
K = int(input())
a = [0] + list(map(int, input().split())) + [L]
d = []
for i in range(n + 1):
    d.append(a[i + 1] - a[i])

ans = bisect(L + 1, 0)
print(ans)