def solution(brown, yellow):
    answer = []
    x, y = 1, 1
    
    while True:
        if 2 * x + 2 * (y - 2) == brown and (x-2) * (y-2) == yellow:
            break
        if x == y:
            x += 1
            y = 1
        else:
            y += 1
    answer = [x, y]
    return answer