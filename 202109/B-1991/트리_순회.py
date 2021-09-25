import sys
input = sys.stdin.readline

tree = dict()
n = int(input())
for _ in range(n):
    x, y, z = map(str, input().split())
    tree[x] = [y, z]

#전위
def first(nod, temp, res):
    res += nod
    child = tree[nod]
    if child[1] != ".":
        temp.append(child[1])
    if child[0] != ".":
        first(child[0], temp, res)
    else:
        if temp:
            first(temp.pop(0), temp, res)
        else:
            print(res)


#중위
def mid(nod, temp, res):
    child = tree[nod]
    f = child[0] + nod + child[1]
    res = res.replace(nod, f)
    res = res.replace('.' , '')
    
    if child[1] != ".":
        temp.append(child[1])
    if child[0] != ".":
        mid(child[0], temp, res)
    else:
        if temp:
            mid(temp.pop(0), temp, res)
        else:
            print(res)

#후위
def last(nod, temp, res):
    child = tree[nod]
    f = child[0] + child[1] + nod
    res = res.replace(nod, f)
    res = res.replace('.' , '')
    
    if child[1] != ".":
        temp.append(child[1])
    if child[0] != ".":
        last(child[0], temp, res)
    else:
        if temp:
            last(temp.pop(0), temp, res)
        else:
            print(res)

first('A', [], '')
mid('A', [], 'A')
last('A', [], 'A')