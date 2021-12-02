def pfact(x):
    res = []
    for i in range(2, int(x**0.5)+1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x >= 2: res.append(x)
    return res

n = int(input())
m = len(pfact(n))
ans = 0
while m > 1:
    m += 1
    m //= 2
    ans += 1
print(ans)