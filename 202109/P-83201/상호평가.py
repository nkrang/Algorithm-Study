def solution(scores):
    answer = []
    for i in range(len(scores)):
        me = scores[i][i]
        myscore = []
        for j in range(len(scores)):
            myscore.append(scores[j][i])
        
        if max(myscore) == me or min(myscore) == me:
            if myscore.count(me) == 1:
                answer.append(score((sum(myscore) - me) / (len(scores) - 1)))
            else:
                answer.append(score(sum(myscore) / len(scores)))
        else:
            answer.append(score(sum(myscore) / len(scores)))
                
                
    return ''.join(answer)

def score(s):
    if s >= 90:
        return 'A'
    elif 80 <= s < 90:
        return 'B'
    elif 70 <= s < 80:
        return 'C'
    elif 50 <= s < 70:
        return 'D'
    else:
        return 'F'