'''
344. Reverse String 
Write a function that reverses a string. The input given as an array of characters "s".
You must do this by modifying the input array in-place with "O(1)" extra memory.

Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
'''
# solution 1
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1

# solution 2
def reverseString(s):
    s.reverse()

# solution 3 
def reverseString(s):
    s[:] = s[::-1]

