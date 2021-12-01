from bisect import bisect
n = int(input())
A = list(set(map(int, input().split())))
A.sort()

q = int(input())
for _ in range(q):
    ans = float('inf')
    b = int(input())
    bi = bisect(A, b)
    if bi == 0:
        ans = A[bi] - b
    elif bi == len(A):
        ans = b - A[bi - 1]
    else:
        ans = min(A[bi] - b, b - A[bi - 1])
    print(ans)