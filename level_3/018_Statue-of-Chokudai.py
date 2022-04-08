from math import radians, degrees, sin, cos, atan2

T = int(input())
L, X, Y = map(int, input().split())

r = L / 2

Q = int(input())
for _ in range(Q):
    E = int(input())

    angle = 360 - 360 * (E / T) - 90
    sy = r * cos(radians(angle))
    sz = r + r * sin(radians(angle))

    y = Y - sy
    a = (X**2 + y**2) ** 0.5
    print(degrees(atan2(sz, a)))