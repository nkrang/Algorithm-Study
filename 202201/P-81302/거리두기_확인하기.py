from collections import deque

def bfs(places, sx, sy):
    dq = deque([(sx, sy)])

    visited = [[0] * 5 for _ in range(5)]
    #네방향으로 가면서 X일때는 안가도록 해서 P를 만나면 False
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[sx][sy] = 1

    while dq:
        print(dq)
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (abs(nx-sx) + abs(ny-sy) <= 2) and visited[nx][ny] == 0:
                if places[nx][ny] == 'P':
                    print(nx, ny)
                    return False
                if places[nx][ny] == "O":
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
    else:
        return True 


def solution(places):
    answer = [1] * 5
    for t in range(5):
        B = False
        for i in range(5):
            for j in range(5):
                if places[t][i][j] == 'P':
                    if bfs(places[t], i, j) == False:
                        B = True
                        answer[t] = 0
                        break

    print(answer)
    return answer


#solution(["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"])
# solution(["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"])
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])