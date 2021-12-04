def is_ok(x):
    l = 0
    cnt = k
    for r in range(n):
        if a[r] - l >= x and L - a[r] >= x:
            cnt -= 1
            l = a[r]
    return cnt <= 0

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) //2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, L = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
print(bisect(L + 1, -1))