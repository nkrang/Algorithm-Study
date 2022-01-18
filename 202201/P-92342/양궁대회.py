
answer = [-1]
diff = 0

def solution(n, info):
    global answer, diff

    def cal(score):
        peach, lion = 0, 0
        for i in range(11):
            if score[i] > info[i]:
                lion += 10 - i
            elif info[i] != 0:
                peach += 10 - i
        return peach, lion

    def dfs(score, arrow, depth):
        global answer, diff
        peach, lion = cal(score)
        if lion - peach >= diff:
            diff = lion - peach
            answer = score[:]
            if arrow < n:
                answer[10] += n - arrow


        if depth == 11:
            return
        if arrow + info[depth] + 1 <= n:
            score[depth] = info[depth] + 1
            dfs(score,  arrow + info[depth] + 1, depth + 1)
            score[depth] = 0
            dfs(score, arrow, depth+1)
        else:
            dfs(score, arrow, depth+1)
        
    dfs([0] * 11, 0, 0)
    print(answer)
    return answer

# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1])
# print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
print(solution(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))