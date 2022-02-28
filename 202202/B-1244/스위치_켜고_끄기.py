import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

def boy(value):
    first = value
    value -= 1
    while True:
        switch[value] = (switch[value] + 1) % 2
        value += first
        if value >= n:
            break

def girl(value):
    value -= 1
    switch[value] = (switch[value] +1) % 2
    left, right = value-1, value+1

    while True:
        if left < 0 or right >= n:
            break
        elif switch[left] != switch[right]:
            break
        else:
            new = (switch[left] + 1) % 2
            switch[left] = new
            switch[right] = new

            left -= 1
            right += 1


t = int(input())
for _ in range(t):
    gender, number = map(int, input().split())
    if gender == 1:
        boy(number)
    else:
        girl(number)

for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end=" ")