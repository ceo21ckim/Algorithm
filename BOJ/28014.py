# https://www.acmicpc.net/problem/28014

N = int(input())
l = list(map(int, input().split()))
answer = 1

for i in range(N-1):
    if l[i] <= l[i+1]:
        answer += 1
        
print(answer)