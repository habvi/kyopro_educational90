def update(k, x):
    k += N0 - 1
    data[k] = x
    while k:
        k = (k - 1) // 2
        data[k] = max(data[2*k + 1], data[2*k + 2])
def query(l, r):
    L = l + N0; R = r + N0
    s = ng
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R - 1])
        if L & 1:
            s = max(s, data[L - 1])
            L += 1
        L >>= 1; R >>= 1
    return s

w, n = map(int, input().split())
lrv = [list(map(int, input().split())) for _ in range(n)]

N0 = 2**(w - 1).bit_length()
ng = -1
data = [ng] * (2 * N0)
update(0, 0)
for l, r, v in lrv:
    for i in range(w, -1, -1):
        L = max(0, i - r)
        R = i - l + 1
        if R < 0:
            break
        mw = query(L, R)
        if mw == ng:
            continue
        tw = query(i, i + 1)
        if mw + v > tw:
            update(i, mw + v)
ans = query(w, w + 1)
print(ans)