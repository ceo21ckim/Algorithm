'''
1. Two Sum 
Given an array of integers "nums" and an integer "target", return indices of the two numbers such taht they add up to "target".
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
# solution 1, Brute-Force 
from re import L


nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]

# solution 2
'''
Without comparing all combinations. Specifically, exploring whether a value exists by subtracting the first value from the target.
'''
def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n 
        
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# solution 3
'''
Use dictionary ,Instead of comparison and exploring method.
'''
def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i 
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        # target -num in nums_map == key 값 조회
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# solution 4 
'''
improve search structure 
'''
def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# solution 5
'''
Using two pointer
해당 문제는 투 포인터로 푸는 것이 불가능하다. 기본적으로, sorting되지 않았기 때문이다.
sort를 해도 상관없으나, 그렇게 하면 index가 엉망이 되어서 문제가 된다. 
index가 아니라 값을 찾는 문제라면 투 포인터를 사용해도 무방하다.
'''

def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1 
        
        else:
            return [left, right]

