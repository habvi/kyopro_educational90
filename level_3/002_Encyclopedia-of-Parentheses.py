n = int(input())
for i in range(1 << n):
    s = ''
    cnt = 0
    for j in reversed(range(n)):
        if cnt < 0:
            break
        if i & (1<<j) == 0:
            s += '('
            cnt += 1
        else:
            s += ')'
            cnt -= 1
    else:
        if cnt == 0:
            print(s)