import sys
input = sys.stdin.readline

def check(nation):
    for i in range(6):
        for j in range(3):
            print(nation)
            temp = j + 2
            if temp > 2:
                temp %= 2
            k = 0
            while nation[i][j] > 0 and k < 6:
                if i != k and nation[k][temp] > 0:
                    nation[i][j] -= 1
                    nation[k][temp] -= 1
                    k += 1
                else:
                    k += 1
            if nation[i][j] > 0:
                print(i, j, nation)
                return False
        
    else:
        return True

for _ in range(4):
    line = list(map(int, input().split()))
    nation = []
    for i in range(0, 18, 3):
        nation.append(line[i:i+3])
    if check(nation):
        print(1, end=" ")
    else:
        print(0, end=" ")

 
                
                