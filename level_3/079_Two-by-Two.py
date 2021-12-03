h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        if a[i][j] == b[i][j]:
            continue
        d = b[i][j] - a[i][j]
        ans += abs(d)
        for dy, dx in zip((0, 1, 0, 1), (0, 0, 1, 1)):
            a[i + dy][j + dx] += d

if a == b:
    print('Yes')
    print(ans)
else:
    print('No')