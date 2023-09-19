# https://www.acmicpc.net/problem/2720

N = int(input())

for _ in range(N):
    money = int(input())
    answer = []
    for m in [25, 10, 5, 1]:
        t = money // m 
        money = money - (t * m)
        answer.append(str(t))
    print(' '.join(answer))