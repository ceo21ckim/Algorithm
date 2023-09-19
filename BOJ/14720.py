# https://www.acmicpc.net/problem/14720

N = int(input())

c = 0
for n in list(map(int, input().split())):
    if c % 3 == n :
        c += 1
print(c)