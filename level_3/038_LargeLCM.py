from math import gcd
a, b = map(int, input().split())
ng = 10**18
lcm = a * b // gcd(a, b)
print('Large' if lcm > ng else lcm)