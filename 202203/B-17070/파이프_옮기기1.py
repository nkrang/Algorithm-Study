import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)

#[행][열][가로, 대각선, 세로] = 경우의 수
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

#0행 1열은 0,0 에서 가로로 오는 경우 1가지 밖에 없음
dp[0][1][0] = 1
#0행은 2열부터 벽이 존재하지 않을 때까지만 가로로 오는 경우 1가지 밖에 없음
for i in range(2, N):
    if matrix[0][i] == 0:
        dp[0][i][0] = 1
    else:
        #벽이 있으면 그 뒤로 다 못 감
        break

#나머지 행들도 0열, 1열은 못 감
for i in range(1, N):
    for j in range(2, N):
        #대각선이 갈 수 있는 (현재, 현재 위 칸, 현재 왼쪽 칸) 3칸이 다 비어있을 경우 
        if matrix[i][j] == 0 and matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
            #대각선은 세 방향에서 모두 다 갈 수 있으므로 전 칸에서 세가지 경우 다 갈 수 있음
            dp[i][j][1] = sum(dp[i-1][j-1])
        #그 칸만 딱 비어 있다 치면 가로, 세로로 오는 경우 가능
        if matrix[i][j] == 0:
            #가로 일때는 전 칸에서 가로, 대각선인 경우 가능
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            #세로 일 때는 전 칸에서 세로, 대각선인 경우 가능
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

#마지막 칸의 세가지 경우를 다 합해서 출력
print(sum(dp[N-1][N-1]))