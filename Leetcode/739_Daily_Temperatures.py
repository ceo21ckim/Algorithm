'''
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the 
number of days you have to wait after the `1-th` day to get a warmer temperature. If there is no future day for which this is possible, 
keep `answer[i] == 0` instead.

Input: T = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
'''

# Run Time error
T = [73, 74, 75, 71, 69, 72, 76, 73]

results = []
for i, t in enumerate(T[:-1]):
    ans = list(map(lambda x: x - t,T[(i+1):]))
    ans = [True if a > 0 else False for a in ans]
    try:
        idx = ans.index(True)
        results.append(idx+1)
    except:
        results.append(0)
results.append(0)

results


# Stack 
answer = [0] * len(T)
stack = []
for i, cur in enumerate(T):
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last 
    stack.append(i)

'''
1) stack = [0]
2) cur = 74, stack == True, while 문 실행
   - last = 73 
   - answer[last] = 1 - last (1)
   - stack = [1]

'''
