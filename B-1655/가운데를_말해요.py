import sys
input = sys.stdin.readline

n = int(input().strip('\n'))

numbers = []
res = []

for i in range(n):
    num = int(input().strip('\n'))
    numbers.append(num)
    numbers.sort()
    index = len(numbers) // 2 + len(numbers) % 2
    res.append(numbers[index-1])

for x in res:
    print(x)
