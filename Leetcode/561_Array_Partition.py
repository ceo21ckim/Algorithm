'''
561. Array Partition
Given an integer array "nums" of "2n" integers, group these intergers into "n" pairs "(a1, b1), (a2_b2), ..., (an, bn)"
such that the sum of "min(ai, bi)" for all "i" is maximized. Return the maximized sum.

Input: nums = [1, 4, 3, 2]
Output: 4
'''

# solution 1
nums = [1, 4, 3, 2]
nums.sort()

output = 0

for i in range(0, len(nums), 2):
    output += min(nums[i],nums[i+1])

# solution 2
nums = [1, 4, 3, 2]
total = 0 
pair = []
nums.sort()

for n in nums:
    pair.append(n)
    if len(pair) == 2:
        total += min(pair)
        pair = []
total 


# solution 3
results = 0 
nums.sort()

for i, in enumerate(nums):
    if i % 2 == 0 :
        results += n 
        
