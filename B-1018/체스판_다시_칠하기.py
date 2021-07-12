m, n = map(int, input().split())


board = []
for _ in range(m):
    cross = list(input())
    board.append(cross)

def solution(first):
    res = 9999999
    color = first
    for i in range(m-7):
        for j in range(n-7):
            #한 단계
            cnt = 0
            for c in range(i, i+8):
                #c: 세로번호
                for v in range(j, j+8):
                    #v: 가로번호
                    if color == board[c][v]:
                        cnt += 1
                        color = "B" if color == "W" else "W"
                    else:
                        color = board[c][v]
                else:
                    color = "B" if color == "W" else "W"
                
            if cnt < res:
                res = cnt
    return res

W = solution("W")
B = solution("B")

print(min(W, B))
            
            