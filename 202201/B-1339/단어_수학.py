import sys
input = sys.stdin.readline

n = int(input())


dic = dict()

def makeDictonary(line):
    value = 1
    while line:
        x = line.pop()
        if x in dic:
            dic[x] += value
        else:
            dic[x] = value
        value *= 10

for _ in range(n):
    line = list(map(str, input().strip('\n')))
    makeDictonary(line)
    
sortedDic = sorted(dic.items(), key= lambda item:item[1], reverse= True)

answer = 0
num = 9
for x in sortedDic:
    answer += x[1] * num
    num -= 1

print(answer)