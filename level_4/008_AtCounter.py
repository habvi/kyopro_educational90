from collections import defaultdict

n = int(input())
S = input()
MOD = 10**9 + 7

target = 'Xatcoder'

num = defaultdict(int)
num['X'] += 1
for s in S:
    i = target.find(s)
    if i == -1:
        continue
    num[s] += num[target[i - 1]]
    num[s] %= MOD

print(num['r'])