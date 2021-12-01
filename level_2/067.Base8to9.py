def eight_to_ten(x):
    ten = 0
    sx = str(x)
    n = len(sx)
    for i in range(n):
        ten += int(sx[n - i - 1]) * (8**i)
    return str(ten)
def ten_to_nine(ten):
    nine = ''
    while ten >= 1:
        nine += str(ten % 9)
        ten //= 9
    return nine[::-1]
def nine_to_eight(nine):
    eight = ''
    for c in str(nine):
        if c == '8': eight += '5'
        else: eight += c
    return eight

n, k = map(int, input().split())
if n == 0:
    print(0)
    exit()

eight = n
for _ in range(k):
    ten = eight_to_ten(eight)
    nine = ten_to_nine(int(ten))
    eight = nine_to_eight(int(nine))
print(eight)
