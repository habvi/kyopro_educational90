h, w = map(int, input().split())
if h == 1 or w == 1:
    print(h * w)
    exit()

r = (h + 2 - 1) // 2
c = (w + 2 - 1) // 2
print(r * c)