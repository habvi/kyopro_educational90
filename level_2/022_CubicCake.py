from math import gcd
a, b, c = map(int, input().split())
g = gcd(a, gcd(b, c))
print(a//g - 1 + b//g - 1 + c//g - 1)