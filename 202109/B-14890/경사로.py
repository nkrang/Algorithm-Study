import sys
input = sys.stdin.readline

n, L = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

res = 0
for i in range(n):
    row = 0
    col = 0
    while row < n-1:
        #print(i, row)
        b = False
        if matrix[i][row] == matrix[i][row+1]:
            row += 1
        elif row + L < n and matrix[i][row] == matrix[i][row+1] + 1:
            for j in range(1, L):
                if matrix[i][row + j] != matrix[i][row + j + 1]:
                    b = True
                    break
            else:
                row += L
        elif row - L >= -1 and matrix[i][row] + 1 == matrix[i][row+1]:
            if row - L == -1:
                for j in range(0, L-1):
                    if matrix[i][j] == matrix[i][j+1]:
                        row += 1
            else:
                #print("b", i)
                for j in range(0, L-1):
                    print(j)
                    if matrix[i][row - j] != matrix[i][row - j - 1]:
                        b = True
                        break
                else:
                    for j in range(0, 2*L):
                        if row-j >=0 and matrix[i][row-j] > matrix[i][row]:
                            b = True
                            break
                    else:
                        row += 1
        else:
            break
    
        if b:
            break
    else:
        # print("res", i)
        res += 1
    
    while col < n-1:
        #print(i, col)
        b = False
        if matrix[col][i] == matrix[col+1][i]:
            col += 1
        elif col + L < n and matrix[col][i] == matrix[col+1][i] + 1:
            for j in range(1, L):
                if matrix[col + j][i] != matrix[col + j + 1][i]:
                    b = True
                    break
            else:
                col += L
        elif col - L >= -1 and matrix[col][i] + 1 == matrix[col+1][i]:
            if col - L == -1:
                for j in range(0, L-1):
                    if matrix[j][i] != matrix[j+1][i]:
                        b = True
                        break
                else:
                    col += 1
            else:
                for j in range(0, L-1):
                    if matrix[col - j][i] != matrix[col - j - 1][i]:
                        b = True
                        break
                else:
                    for j in range(0, 2*L):
                        if col - j >= 0 and matrix[col-j][i] > matrix[col][i]:
                            b = True
                            break
                    else:
                        col += 1
        else:
            break
        if b:
            break
    else:
        #print("res", i)
        res += 1

print(res)