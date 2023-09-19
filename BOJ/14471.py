# https://www.acmicpc.net/problem/14471

N, M = map(int, input().split())

answer = [0] * M
for i in range(M):
    A, B = map(int, input().split())
    if A < B:
        answer[i] = (B-A)//2
answer = sorted(answer)
print(sum(answer[:(M-1)]))