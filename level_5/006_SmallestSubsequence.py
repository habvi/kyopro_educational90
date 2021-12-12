n, k = map(int, input().split())
s = input()
idx = [[n] * 26 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for al in range(26):
        if al == ord(s[i]) - ord('a'):
            idx[i][al] = i
        else:
            idx[i][al] = idx[i + 1][al]

ans = ""
now = 0
for cnt in range(k):
    for al in range(26):
        if k - cnt <= n - idx[now][al]:
            ans += chr(al + ord('a'))
            now = idx[now][al] + 1
            break
print(ans)