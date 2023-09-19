# https://www.acmicpc.net/problem/2864

A, B = input().split()

def func(a, src='5', dst='6'):
    return int(a.replace(src, dst))

_max = func(A) + func(B)
_min = func(A, '6', '5') + func(B, '6', '5')

print(_min, _max)