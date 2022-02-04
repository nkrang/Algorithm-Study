import sys
input = sys.stdin.readline

matrix = []
for _ in range(19):
    line = list(map(int, input().split()))
    matrix.append(line)

dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

for i in range(19):
    for j in range(19):
        color = 0
        if matrix[i][j] != 0:
            color = matrix[i][j]
            #네방향 검사
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                #진행방향 반대에도 같은 숫자가 있으면 안됨
                if 0 <= i-dx[d] < 19 and 0 <= j-dy[d] < 19 and matrix[i-dx[d]][j-dy[d]] == color:
                    continue
                cnt = 1
                #진행방향으로 반복하면서 개수 세기
                while True:
                    if 0 <= nx < 19 and 0 <= ny < 19 and matrix[nx][ny] == color:
                        cnt += 1
                        nx += dx[d]
                        ny += dy[d]
                    else:
                        break
                #5개이면 정답
                if cnt == 5:
                    print(color)
                    print(i+1, j+1)
                    sys.exit(0)
else:
    print(0)