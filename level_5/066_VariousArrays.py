n = int(input())
L, R = [], []
for _ in range(n):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for l in range(L[i], R[i] + 1):
            if R[j] < l:
                inv = R[j] - L[j] + 1
            else:
                inv = max(0, l - L[j])

            dnmnt = (R[i] - L[i] + 1) * (R[j] - L[j] + 1)
            ans += inv / dnmnt
print(ans)