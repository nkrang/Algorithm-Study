import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    line = list(map(str, input().strip('\n')))
    matrix.append(line)


def division(x, y, n):
    check = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != check:
                print('(', end="")
                division(x, y, n//2)
                division(x, y+n//2, n//2)
                division(x+n//2, y, n//2)
                division(x+n//2, y+n//2, n//2)
                print(')', end="")
                return
    else:
        print(check, end="")

division(0, 0, N)