import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
math = list(map(int, input().split()))

maxi = -1000000000
mini = 1000000000

def cal(num, i, add, minus, mul, div):
    global maxi, mini, numbers
    if i == n:
        maxi = max(maxi, num)
        mini = min(mini, num)
        return
    else:
        if add:
            cal(num + numbers[i], i+1, add-1, minus, mul, div)
        if minus:
            cal(num - numbers[i], i+1, add, minus-1, mul, div)
        if mul:
            cal(num * numbers[i], i+1, add, minus, mul-1, div)
        if div:
            cal(int(num / numbers[i]), i+1, add, minus, mul, div-1)

cal(numbers[0], 1, math[0], math[1], math[2], math[3])
print(maxi)
print(mini)

