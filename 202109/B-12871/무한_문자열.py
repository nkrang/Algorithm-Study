import sys
input = sys.stdin.readline

one = input().strip('\n')
two = input().strip('\n')

if len(one) > len(two):
    temp = one
    one = two
    two = temp

plus = one

while len(one) <= len(two):
    print(one)
    if one == two:
        print(1)
        break
    one += plus
    
else:
    print(0)
