import math

def solution(w,h):
    temp = 0
    g = math.gcd(w, h)
    temp = w//g + h//g - 1
    return w * h - temp * g

print(solution(8, 12))