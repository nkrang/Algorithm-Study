import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = 1e9
mini = 1e9

def search(up, down):
    global mini
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        floor = mid * up - (n - mid) * down
        if floor <= 0:
            left = mid + 1
        else:
            if floor < mini:
                mini = floor
                right = mid - 1
    
    return mini

for _ in range(m):
    x, y = map(int, input().split())
    mini = 1e9
    answer = min(search(x, y), answer)
    
print(answer)
