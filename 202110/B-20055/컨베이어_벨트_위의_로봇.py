N, K = map(int, input().split())
#내구도
S = list(map(int, input().split()))
belt = []
f1 = [x for x in range(0, N)]
belt.append(f1)
f2 = [x for x in range(2*N-1, N-1, -1)]
belt.append(f2)


def beltmove():
    new = [[0] * (N) for _ in range(2)]
    new[0][1:N] = belt[0][0:N-1]
    new[0][0] = belt[1][0]
    new[1][0:N-1] = belt[1][1:N]
    new[1][N-1] = belt[0][N-1]

    for i in range(N-2, -1, -1):
        if robot[i] == 1:
            robot[i] = 0
            if i+1 != N-1:
                robot[i+1] = 1
    return new

robot = [0] * N
def robotmove():
    for i in range(N-2, -1, -1):
        if robot[i] == 1:
            next = belt[0][i+1]
            if robot[i+1] == 0 and S[next] > 0:
                if i+1 != N-1:
                    robot[i+1] = 1
                S[next] -= 1
                robot[i] = 0
    if S[belt[0][0]] > 0:
        robot[0] = 1
        S[belt[0][0]] -= 1
    if S.count(0) >= K:
        return False
    return True

answer = 0
while True:
    answer += 1
    belt = beltmove()
    if robotmove() == False:
        break
print(answer)