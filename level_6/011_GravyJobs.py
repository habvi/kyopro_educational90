# n <= 5000
def solve2():
    day = 5000
    dp = [0] * (day + 1)

    for d, c, s in A:
        ndp = [0] * (day + 1)
        for i in range(day + 1):
            ndp[i] = max(ndp[i], dp[i])
            if i + c <= min(d, day):
                ndp[i + c] = max(ndp[i + c], dp[i] + s)
        dp = ndp
    print(max(dp))


# N <= 20
def solve1():
    ans = 0
    for bit in range(1 << n):
        total = 0
        now = 0
        for i in range(n):
            if bit >> i & 1 == 0:
                continue
            d, c, s = A[i]
            if d - c + 1 > now:
                total += s
                now += c
        ans = max(ans, total)
    print(ans)


n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]
A.sort(key=lambda x: x[0])

if n <= 20:
    solve1()
else:
    solve2()