# https://www.acmicpc.net/problem/10162

T = int(input())
answer = []
for t in [300, 60, 10]:
    v = T//t
    T -= v * t 
    answer.append(str(v))
if T:
    print(-1)
else:
    print(' '.join(answer))