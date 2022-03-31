from heapq import heappop, heappush

n, K = map(int, input().split())
S = input()

hq = []
for i in range(n - K):
    heappush(hq, (S[i], i))

ans = []
idx = [-1]
for i in range(n - K, n):
    heappush(hq, (S[i], i))
    while hq and hq[0][1] <= idx[-1]:
        heappop(hq)

    alph, j = heappop(hq)
    ans.append(alph)
    idx.append(j)

print(''.join(ans))