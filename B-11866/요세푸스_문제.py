from collections import deque

n, k = map(int, input().split())

numbers = list(range(1, n+1))
numbers = deque(numbers)

res =[]

while numbers:
    for _ in range(k-1):
        x = numbers.popleft()
        numbers.append(x)
    res.append(numbers.popleft())

print("<", end="")
for x in res:
    if x == res[-1]:
        print(x, end=">")
    else:
        print(x, end=", ")
    