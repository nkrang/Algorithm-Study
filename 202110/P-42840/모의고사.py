def solution(answers):
    answer = []
    score = [0] * 3
    ans_a = [1, 2, 3, 4, 5]
    ans_b = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if ans_a[i % len(ans_a)] == answers[i]:
            score[0] += 1
        if ans_b[i % len(ans_b)] == answers[i]:
            score[1] += 1
        if ans_c[i % len(ans_c)] == answers[i]:
            score[2] += 1
    
    maxi = max(score)
    for i in range(3):
        if score[i] == maxi:
            answer.append(i+1)
    
    
    return answer
