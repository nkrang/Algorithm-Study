import sys
input = sys.stdin.readline

string = str(input().strip('\n'))
bomb = str(input().strip('\n'))

while bomb in string:
    string = string.replace(bomb, '')

if string:
    print(string)
else:
    print("FRULA")