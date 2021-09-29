import sys
input = sys.stdin.readline

n, L = map(int, input().split())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

result = 0
for i in range(n):
    pre = matrix[i][0]
    cnt = 1
    for j in range(1, n):
        if matrix[i][j] == pre:
            cnt += 1
            pre = matrix[i][j]
        elif matrix[i][j] == pre + 1 and cnt >= 0:
            if cnt >= L:
                cnt = 1
                pre = matrix[i][j]
            else:
                break
        elif matrix[i][j] == pre - 1 and cnt >= 0:
            cnt = -L + 1
            pre = matrix[i][j]
        else:
            break
    else:
        if cnt >= 0:
            result += 1

for i in range(n):
    pre = matrix[0][i]
    cnt = 1
    for j in range(1, n):
        if matrix[j][i] == pre:
            cnt += 1
            pre = matrix[j][i]
        elif matrix[j][i] == pre + 1 and cnt >= 0:
            if cnt >= L:
                cnt += 1
                pre = matrix[j][i]
            else:
                break
        elif matrix[j][i] == pre - 1 and cnt >= 0:
            cnt = -L + 1
            pre = matrix[j][i]
        else:
            break
    else:
        if cnt >= 0:
            result += 1

print(result)