# https://www.acmicpc.net/problem/22864

A, B, C, M = map(int, input().split())

stack = 0
answer = 0 
for _ in range(24):
    if A > M:
        break 
    if stack + A <= M:
        answer += B 
        stack += A
    else:
        stack -= C 
        if stack < 0:
            stack = 0
print(answer)
