# https://www.acmicpc.net/problem/4796

i = 1
while True:
    L, P, V = map(int, input().split())
    if [L, P, V] == [0, 0, 0]:
        break
    
    remain = V%P if V%P < L else L 
    answer = L * (V//P) + remain
    print(f'Case {i}: {answer}')
    i += 1