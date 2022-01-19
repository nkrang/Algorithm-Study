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
        if depth < 0:
            if arrow > n:
                return
            peach, lion = cal(score)
            if lion - peach > diff:
                diff = lion - peach
                answer = score[:]
                if arrow < n:
                    answer[10] += n - arrow
            return
        
        score[depth] = info[depth] + 1
        dfs(score,  arrow + info[depth] + 1, depth - 1)
        score[depth] = 0
        dfs(score, arrow, depth-1)
        
    dfs([0] * 11, 0, 10)
    print(answer)
    return answer