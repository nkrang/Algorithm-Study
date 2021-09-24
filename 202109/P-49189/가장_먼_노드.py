from collections import deque

def solution(n, edge):
    answer = 0
    matrix = [[0]*(n+1) for _ in range(n+1)]

    for x, y in edge:
        matrix[x][y] = 1
        matrix[y][x] = 1
    
    dq = [(1, 0)]
    dq = deque(dq)
    passed = [i for i in range(2, n+1)]
    print(passed)
    maxi = 0
    while dq:
        print(dq)
        x, l = dq.popleft()
        for i in passed:
            if matrix[x][i] == 1:
                print(x, i)
                dq.append((i, l+1))
                print(maxi)
                if maxi == l:
                    answer += 1
                elif maxi < l:
                    maxi = l
                    answer = 1
                passed.remove(i)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))