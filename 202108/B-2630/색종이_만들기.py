import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0

def devision(x, y, n):
    global white, blue
    check = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                #4등분
                devision(x, y, n//2)
                devision(x+n//2, y, n//2)
                devision(x, y+n//2, n//2)
                devision(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        #흰색
        white += 1
        return
    else:
        blue += 1
        return

devision(0, 0, n)
print(white)
print(blue)