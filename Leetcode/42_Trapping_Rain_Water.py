'''
42. Trapping Rain Water 
Given "n" non-negative integers representing an elevation map where the width of each bar is "1", 
compute how much water it can trap after raining.

Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
'''

# solution 1 - two point **
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
results = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left <= right:
    left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
    
    if left_max <= right_max :
        results += left_max - height[left]
        left += 1 
    
    else:
        results += right_max - height[right]
        right -= 1


# solution 2 - Stack ***
stack = []
volume = 0 

for i in range(len(height)):
    # 변곡점을 만나는 경우 
    while stack and height[i] > height[stack[-1]]:
        # 스택에서 꺼낸다.
        top = stack.pop()
        
        if not len(stack):
            break 
        
        # 이전과의 차이만큼 물 높이 처리
        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]
        volume += distance * waters 
    
    stack.append(i)
    

## array 
def trap(height):
    n = len(height)
    if n == 0 :
        return 0 
    
    lmax = [0] * n 
    rmax = [0] * n 
    lmax[0] = height[0]
    rmax[n-1] = height[n-1]
    for i in range(1, n):
        lmax[i] = max(lmax[i-1], height[i])
    
    for i in range(n-1, -1, -1):
        rmax[i] = max(rmax[i], height[i-1])
        
    ans = 0 
    for i in range(n):
        ans += min(lmax[i], rmax[i]) - height[i]
    return ans 


height = [1, 0, 2, 1, 0, 1, 2, 3, 1]
n = len(height)
lmax = [0] * n 
rmax = [0] * n 

lmax[0] = height[0]
rmax[n-1] = height[n-1]

for i in range(1, n):
    lmax[i] = max(lmax[i-1], height[i])

for i in range(n-2, -1, -1):
    rmax[i] = max(rmax[i+1], height[i])

volume = 0 
for i in range(n):
    volume += min(lmax[i], rmax[i]) - height[i]
    print(min(lmax[i], rmax[i]) - height[i])