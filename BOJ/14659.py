input()

l = list(map(int, input().split()))

high = 0
count = 0 
answer = 0


for i in l:
    if i>high:
        high = i 
        count = 0 
    else:
        count += 1
    
    answer = max(answer, count)
print(answer)