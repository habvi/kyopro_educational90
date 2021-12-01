n = int(input())
s = set()
day = 1
for i in range(n):
    t = input()
    if t not in s:
        print(day)
        s.add(t)
    day += 1