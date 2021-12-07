import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    score = []
    for _ in range(n):
        x, y = map(int, input().split())
        score.append([x, y])
    score.sort()

    maxi = score[0][1]
    answer = 1
    for i in range(1, n):
        if score[i][1] < maxi:
            answer += 1
            maxi = score[i][1]

    print(answer)