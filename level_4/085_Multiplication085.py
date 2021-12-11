def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0: continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div

K = int(input())
d = div_lis(K)
n = len(d)
ans = 0
for i in range(n):
    for j in range(i, n):
        a, b = d[i], d[j]
        ab = a * b
        if K % ab != 0:
            continue
        c = K // ab
        if b <= c:
            ans += 1
print(ans)