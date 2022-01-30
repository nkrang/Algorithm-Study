answer = 0
def solution(info, edges):

    dic = dict()
    parent = [-1] * len(info)
    for x, y in edges:
        if x in dic:
            dic[x].append(y)
        else:
            dic[x] = [y]
        parent[y] = x
        

    def find(root, sheep, wolf, info):
        global answer
        temp = info[:]
        if root in dic:
        for x in dic[root]:
            if info[x] == 0:
                temp[x] = 2
                find(x, sheep+1, wolf, info)
                temp[x] = 0
            elif info[x] == 1:
                temp[x] = 2
                if wolf+1 >= sheep:
                    find(x, 0, wolf+1, info)
                else:
                    find(x, sheep, wolf+1, info)
                temp[x] = 1
            else:
                find(x, sheep, wolf, info)
    
    find(0, 0, 0, info)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))