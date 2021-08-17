import sys
input = sys.stdin.readline

n, repeat = map(int, input().split())

first = []
for _ in range(n):
    line = list(map(int, input().split()))
    first.append(line)

def multiple(a, b):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * b[k][j]
            temp[i][j] = num % 1000
        
    return temp

# for _ in range(repeat-1):
#     multiple()
binary = list(str(bin(repeat)))
binary = binary[2:]

#단위 행렬(곱했을 때 자기 자신이 나올 수 있는 행렬)
result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
#result = 0
#주어진 횟수만큼 반복하면 시간초과
#제곱의 제곱으로 해결할 수 있는 것들을 그렇게 함으로써 반복 횟수를 줄임
# ex) 10 = 1010(2) 8제곱 * 2제곱
for i in range(len(binary)):
    temp = first.copy()
    if binary[-i-1] == "1":
        for _ in range(i):
            temp = multiple(temp, temp)
        result = multiple(result, temp)
#출력
for i in range(n):
    for j in range(n):
        print(result[i][j], end = " ")
    print()
