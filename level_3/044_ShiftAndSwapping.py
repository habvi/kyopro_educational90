n, q = map(int, input().split())
A = list(map(int, input().split()))
sft = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x = (x - 1 + sft) % n
    y = (y - 1 + sft) % n
    if t == 1:
        A[x], A[y] = A[y], A[x]
    elif t == 2:
        sft -= 1
    else:
        print(A[x])