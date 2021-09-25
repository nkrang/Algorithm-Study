import sys 
input = sys.stdin.readline

tree = dict()
n = int(input())
for _ in range(n):
    x, y, z = map(str, input().split())
    tree[x] = [y, z]

def first(node):
    if node != ".":
        print(node, end= "")
        first(tree[node][0])
        first(tree[node][1])

def mid(node):
    if node != ".":
        mid(tree[node][0])
        print(node, end= "")
        mid(tree[node][1])

def last(node):
    if node != ".":
        last(tree[node][0])
        last(tree[node][1])
        print(node, end= "")

first('A')
print()
mid('A')
print()
last('A')
