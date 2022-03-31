def stoi(s):
    return ord(s) - ord('a')

def itos(i):
    return chr(i + ord('a'))

def right_leftmost_idx(S):
    n = len(S)
    idx = [[n] * 26 for _ in range(n + 1)]
    for i in reversed(range(n)):
        for alph in range(26):
            if stoi(S[i]) == alph:
                idx[i][alph] = i
            else:
                idx[i][alph] = idx[i + 1][alph]
    return idx


n, K = map(int, input().split())
S = input()

idx = right_leftmost_idx(S)

ans = []
now = -1
for times in range(K):
    for alph in range(26):
        nxt = idx[now + 1][alph]
        if n - nxt >= K - times:
            ans.append(itos(alph))
            now = nxt
            break
print(''.join(ans))