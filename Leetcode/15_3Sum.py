'''
15. 3Sum 
Given an integer array nums, return all the triplets "[nums[i], nums[j], nums[k]]" 
such that "i != j", "i != k", and "j != k", and "nums[i] + nums[j] + nums[k] == 0 

Input: nums [-1, 0, 1, 2, -1, 4]
Output: [[-1, -1, 2], [-1, 0, 1]]
'''


nums = [-1, 0, 1, 2, -1, -4]
# solution 1 - 브루트 포스 (Time out)
nums.sort()
results = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            value = nums[i] + nums[j] + nums[k] 
            if value == 0 and [nums[i], nums[j], nums[k]] not in results :
                
                results.append([nums[i], nums[j], nums[k]])
                
results 

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()

nums
# solution 2 - two pointer
results = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    left, right = i+1, len(nums) - 1
    sums = nums[left] + nums[i] + nums[right]
    while left < right:
        if sums < 0:
            left += 1
        
        elif sums > 0:
            right -= 1
            
        else:
            results.append([nums[i], nums[left], nums[right]])
            left += 1 
            right -= 1
results