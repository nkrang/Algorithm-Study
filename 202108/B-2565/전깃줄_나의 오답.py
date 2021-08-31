import sys
input = sys.stdin.readline

n = int(input())
line = []
cross = [[] for _ in range(n)]

for j in range(n):
    x, y = map(int, input().split())
    line.append((x, y))
    for i in range(len(line) - 1):
        temp = line[i]
        if temp[0] < x and temp[1] > y or temp[0] > x and temp[1] < y:
            cross[j].append(i)
            cross[i].append(j)

def deleteMax():
    global deleted
    maxi = 0
    index = 0
    for i in range(n):
        if len(cross[i]) > maxi:
            maxi = len(cross[i])
            index = i
    if maxi == 0:
        print(deleted)
        return
    else:
        #지우기
        cross[index] = []
        for i in range(n):
            if index in cross[i]:
                cross[i].remove(index)
        deleted += 1
        deleteMax()

deleted = 0
deleteMax()


#열심히 풀어보려고 노력은 해봤으나... 가장 많이 겹치는 선이 여러개일 때 지워지는 순서를 고려하지 않음..
#LIS 열심히 공부해놓고 활용 못하는 나,,,,,, ㅠㅠ