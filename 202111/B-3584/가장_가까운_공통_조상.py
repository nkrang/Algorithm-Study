import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        x, y = map(int, input().split())
        parent[y] = x
    A, B = map(int, input().split())

    pA, pB = [A], [B]

    while A != 0:
        pA.append(parent[A])
        A = parent[A]
    
    while B != 0:
        pB.append(parent[B])
        B = parent[B]

    b = False
    for x in pA:
        if b:
            break
        for y in pB:
            if x == y:
                print(x)
                b = True
                break
