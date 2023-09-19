# https://www.acmicpc.net/problem/11034

while True:
    try:
        a, b, c = map(int, input().split())
        answer = max(b-a, c-b) -1 
        print(answer)
    except:
        break