import sys
input = sys.stdin.readline

n = int(input())
numbers = []
dic = dict()
max_value = -1
max_num = []
for _ in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

    if max_value < dic[x]:
        max_value = dic[x]
        max_num = [x]
    elif max_value == dic[x]:
        max_num.append(x)
    numbers.append(x)

a = sum(numbers)
if a > 0:
    print(int(a / n + 0.5))
elif a < 0:
    print(int(a / n - 0.5))
else:
    print(0)


numbers.sort()
print(numbers[n//2])
max_num.sort()
if len(max_num) > 1:
    print(max_num[1])
else:
    print(max_num[0])
print(numbers[-1] - numbers[0])