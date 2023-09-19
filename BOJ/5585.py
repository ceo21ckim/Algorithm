# https://www.acmicpc.net/problem/5585

money = 1000 - int(input())

answer = 0 
for m in [500, 100, 50, 10, 5, 1]:
    v = money // m 
    answer += v
    money -= v * m
print(answer)