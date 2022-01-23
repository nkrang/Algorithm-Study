def solution(board, skill):
    answer = 0
    imos = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for row in skill:
        if row[0] == 1:
            imos[row[1]][row[2]] += -row[5]
            imos[row[3] + 1][row[2]] += row[5]
            imos[row[1]][row[4] + 1] += row[5]
            imos[row[3] + 1][row[4] + 1] += -row[5]
        else:
            imos[row[1]][row[2]] += row[5]
            imos[row[3] + 1][row[2]] += -row[5]
            imos[row[1]][row[4] + 1] += -row[5]
            imos[row[3] + 1][row[4] + 1] += row[5]
            
    for i in range(len(imos)):
        now = 0
        for j in range(len(imos[0])):
            now += imos[i][j]
            imos[i][j] = now

    for i in range(len(imos[0])):
        now = 0
        for j in range(len(imos)):
            now += imos[j][i]
            imos[j][i] = now

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))