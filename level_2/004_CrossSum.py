h, w = map(int, input().split())
row, col = [], []
A = []
for _ in range(h):
    a = tuple(map(int, input().split()))
    row.append(sum(a))
    A.append(a)

for z in zip(*A):
    col.append(sum(z))

for i in range(h):
    ans = []
    ans_append = ans.append
    for j in range(w):
        ans_append(row[i] + col[j] - A[i][j])
    print(*ans)