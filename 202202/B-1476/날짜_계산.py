import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

x, y, z = 1, 1, 1
year = 1

while True:
    if x == E and y == S and z == M:
        print(year)
        break

    year += 1

    x += 1
    y += 1
    z += 1

    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1