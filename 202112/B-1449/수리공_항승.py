import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = arr[0]
end = arr[0] + L

tape = 1

for i in range(N):
    if start <= arr[i] < end:
        continue
    else:
        start = arr[i]
        end = start + L
        tape += 1

print(tape)