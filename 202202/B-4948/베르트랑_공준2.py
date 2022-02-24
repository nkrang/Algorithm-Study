import sys
input = sys.stdin.readline

check = [0] * 2 + [1] * 246912

#첫 소수만 1로 남기고
#소수의 배수들은 소수가 아니므로 0으로 초기화
for i in range(2, 246913):
    if check[i]:
        for j in range(i * 2, 246913, i):
            check[j] = 0

while True:
    x = int(input())
    if x == 0:
        break
    print(sum(check[x+1:x*2+1]))