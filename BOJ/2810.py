# https://www.acmicpc.net/problem/2810

input()

a = input()
if a.count('LL') <= 1:
    print(len(a))
else:
    print(a.count('LL') + a.count('S') + 1)