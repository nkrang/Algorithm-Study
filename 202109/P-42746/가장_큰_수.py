answer = '0'

def solution(numbers):
    global answer
    used = [0] * len(numbers)
    seq([], used, numbers)
        
    return answer

def seq(arr, used, numbers):
    global answer
    if len(arr) == len(numbers):
        #크기 비교
        int_arr = ''.join(str(_) for _ in arr)
        if int(int_arr) > int(answer):
            answer = int_arr
    else:
        for i in range(len(numbers)):
            if not used[i]:
                arr.append(numbers[i])
                used[i] = 1
                seq(arr, used, numbers)
                used[i] = 0
                arr.pop()

print(solution([121, 55, 20000000]))