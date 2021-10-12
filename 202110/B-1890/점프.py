import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

temp = [[-1] * n for _ in range(n)]

def check(x, y):
    print(x, y)
    size = matrix[x][y]
    temp[x][y] = 0
    if x+size < n:
        if x+size == n-1 and y == n-1:
            temp[x][y] += 1
        else:
            if temp[x+size][y] != -1:
                temp[x][y] += temp[x+size][y]
            else:
                temp[x][y] += check(x+size, y)
    if y+size < n:
        if y+size == n-1 and x == n-1:
            temp[x][y] += 1
        else:
            if temp[x][y+size] != -1:
                temp[x][y] += temp[x][y+size]
            else:
                temp[x][y] += check(x, y+size)
    return temp[x][y]


print(check(0, 0))
print(temp)