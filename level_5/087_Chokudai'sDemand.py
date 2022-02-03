def calc(x):
    dst = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dst[i][j] = A[i][j] if A[i][j] != -1 else x

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dst[i][j] = min(dst[i][j], dst[i][k] + dst[k][j])

    inc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if dst[i][j] <= P:
                inc += 1
    return inc

def is_ok2(x):
    return calc(x) <= K

def bisect2(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok2(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok(x):
    return calc(x) < K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, P, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]

mx = 10 ** 9
high = bisect(0, mx)
low = bisect2(0, mx)

if low == mx:
    print(0)
elif high == mx:
    print('Infinity')
else:
    print(high - low)