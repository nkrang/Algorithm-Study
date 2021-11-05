def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero += 1
        else:
            if lottos[i] in win_nums:
                correct += 1
    
    
    worst = 6 - correct - zero + 1
    if worst >= 6:
        answer.append(6)
    else:
        answer.append(worst)
    
    best = 6 - correct + 1
    if best >= 6:
        answer.append(6)
    else:
        answer.append(best)
        
    
    
    
        
    return answer