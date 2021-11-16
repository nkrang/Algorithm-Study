import sys
input = sys.stdin.readline

N = int(input())
words = []
longest = 0
for _ in range(N):
    w = input().strip('\n')
    longest = max(len(w), longest)
    words.append(w)

matrix = [[0] * longest for _ in range(N)]
for i in range(N):
    zero = longest - len(words[i])
    for z in range(zero):
        matrix[i][z] = '0'
    for j in range(len(words[i])):
        matrix[i][zero + j] = words[i][j]

dic = dict()
count = 9

for i in range(longest):
    for j in range(N):
        if matrix[j][i] != '0':
            if matrix[j][i] in dic:
                matrix[j][i] = str(dic[matrix[j][i]])
            else:
                dic[matrix[j][i]] = count
                matrix[j][i] = str(count)
                count -= 1


answer = 0
for i in range(N):
    num = int(''.join(matrix[i]))
    answer += num

print(answer)
