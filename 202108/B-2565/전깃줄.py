import sys
input = sys.stdin.readline

n = int(input())
line = []

for _ in range(n):
    x, y = map(int, input().split())
    line.append((x, y))

#첫번째 점에 대해 오름차순으로 정렬
#두번째 점의 크기를 비교해서 가장 긴 오름차순 수열을 찾는다
#가장 긴 오름차순 수열에 해당하는 선만 있으면 선들이 만날 일이 없다는 뜻
#고로 전체 선 개수에서 가장 긴 오름차순 수열의 길이를 빼면 지울 선의 개수가 된다.

line.sort()
dp = [1] * n
for i in range(n):
    for j in range(i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))