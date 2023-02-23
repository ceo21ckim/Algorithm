'''
238. Product of Array Except Self 
Given an integer array "nums", return an array "answer" 
such taht "answer[i]" is equal to the product of all the elements of "nums" except "nums[i]".
The product of any prefix or suffix of "nums" is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in "O(n)" time and without using the division operation.

Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
'''

## solution 1
nums = [1, 2, 3, 4]
p = 1
out = []
for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]

p = 1 
for i in range(len(nums)-1, -1, -1):
    out[i] = out[i] * p 
    p = p * nums[i]

out

## solution 2
import numpy as np 
nums = [1, 2, 3, 4]
results = [np.prod(nums)//x for x in nums]
results


## solution 3
from itertools import accumulate
nums = [1, 2, 3, 4]
results = list(accumulate(nums, lambda x, y : x*y))
print(results[::-1])

