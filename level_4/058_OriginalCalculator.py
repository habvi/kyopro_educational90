n, k = map(int, input().split())
MOD = 10 ** 5
dis = []
seen = set()
x = n
for i in range(MOD):
    x += sum(map(int, str(x)))
    x %= MOD
    if x in seen:
        break
    dis.append(x)
    seen.add(x)
    
cy = dis.index(x)
k -= 1
if k <= cy:
    print(dis[k])
else:
    k -= cy
    k %= len(dis) - cy
    print(dis[cy + k])