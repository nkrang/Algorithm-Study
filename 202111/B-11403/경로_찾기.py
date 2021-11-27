import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

#경유지, 출발지, 도착지 for 문 돌리기
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

#출력
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end= " ")
    print()

