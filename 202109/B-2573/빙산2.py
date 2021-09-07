import sys
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
matrix = []
for i in range(n):
    data = list(map(int, input().split()))
    matrix.append(data)
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = [(x, y)]
    check[x][y] = 1 
    queue = deque(queue)
    while queue:
        print(queue)
        x,y = queue.popleft()
        for i in range(4):
            nx = x-dx[i]
            ny = y-dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if matrix[nx][ny]!=0 and not check[nx][ny]:
                check[nx][ny] =1
                queue.append((nx,ny))
                
            if matrix[nx][ny] ==0:
                if temp[i][j] == 0:
                    continue
                temp[i][j] -= 1

year=0
while True:
    flag = 0
    for i in matrix:
        flag += i.count(0)
    if flag == n*m:
        print(0)
        sys.exit()
        
    temp = matrix
    
    check = [[0] * (m+1) for _ in range(n+1)]
    count=0
    for i in range(1,n-1):
        for j in range(1, m-1):
            if matrix[i][j] > 0 and not check[i][j]:
                bfs(i,j)
                count+=1
                if count >=2:
                    print(year)
                    sys.exit()
    matrix = temp
                
    year += 1