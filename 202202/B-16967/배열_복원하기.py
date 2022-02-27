import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
matrix = []
for _ in range(H+X):
    line = list(map(int, input().split()))
    matrix.append(line)

result = [[0] * W for _ in range(H)]
for i in range(0, H):
    for j in range(0, W):
        if X <= i < H and Y <= j < W:
            temp = matrix[i][j] - result[i-X][j-Y]
            result[i][j] = temp
            print(temp, end=" ")
        else:
            result[i][j] = matrix[i][j]
            print(matrix[i][j], end=" ")
    print()


print(result)
    
# 3 3 1 1
# 1 2 3 0
# 4 6 8 3
# 7 12 14 6
# 0 7 8 9