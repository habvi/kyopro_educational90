from collections import deque, defaultdict

n, K = map(int, input().split())
A = list(map(int, input().split()))

q = deque([])
ans = 0
count_ = defaultdict(int)
for a in A:
    q.append(a)
    count_[a] += 1

    while q and len(count_) > K:
        rm = q.popleft()
        count_[rm] -= 1
        if not count_[rm]:
            del count_[rm]

    ans = max(ans, len(q))

print(ans)