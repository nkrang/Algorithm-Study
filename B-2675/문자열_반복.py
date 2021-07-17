import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    re, string = map(str, input().split())
    for x in string:
        for _ in range(int(re)):
            print(x, end = "")
    print()
