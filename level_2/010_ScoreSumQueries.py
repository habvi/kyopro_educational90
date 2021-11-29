from itertools import accumulate
n = int(input())
c1 = [0] * (n + 1)
c2 = [0] * (n + 1)
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        c1[i] += p
    else:
        c2[i] += p

ac1 = [0] + list(accumulate(c1))
ac2 = [0] + list(accumulate(c2))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    print(ac1[r] - ac1[l], ac2[r] - ac2[l])