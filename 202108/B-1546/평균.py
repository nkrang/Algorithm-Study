import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

maxi = max(score)
avg = sum(score)/n
print(avg/maxi * 100)
