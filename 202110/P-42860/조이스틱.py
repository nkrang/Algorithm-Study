def solution(name):
    answer = 0
    change = []
    for i in name:
        x = min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
        answer += x
        change.append(x)
    
    idx = 0
    change[0] = 0
    while sum(change) > 0:
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        if left < right:
            answer += left
            idx -= left
            
        else:
            answer += right
            idx += right
        
        change[idx] = 0
        
    return answer