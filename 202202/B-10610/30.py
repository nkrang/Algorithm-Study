import sys
input = sys.stdin.readline

N = list(map(int, input().strip('\n')))
N.sort(reverse= True)

num = int("".join(map(str, N)))
if num % 30 == 0:
    print(num)
else:
    print(-1)