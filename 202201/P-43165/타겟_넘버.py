answer = 0
def solution(numbers, target):
    global answer
    
    def dfs(num, depth):
        global answer
        if depth == len(numbers):
            if num == target:
                answer += 1
            return
        
        dfs(num + numbers[depth], depth+1)
        dfs(num - numbers[depth], depth+1)
    
    dfs(0, 0)
    
    return answer