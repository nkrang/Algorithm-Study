import sys
input = sys.stdin.readline

def main():

    string = str(input().strip('\n'))
    bomb = str(input().strip('\n'))

    stack = []
    last = bomb[-1] 


    for char in string:
        stack.append(char)
        if char == last and ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    answer = ''.join(stack)
    if answer:
        print(answer)
    else:
        print('FRULA')

if __name__ == '__main__':
    main()