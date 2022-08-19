'''
125. Valid Palindrome 
A phrase is a "Palindrome" if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''
# solution 1 O(n^2)
def isPalindrome(s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        strs.pop(0) != strs.pop()
        return False
     
    return True 

# solution 2 
# Use Deque O(n)
from collections import deque
def isPalindrome(s:str) -> bool:
    strs = deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False 
    return True

# solution 3 Deque보다 2배 가량 빠름.
import re 
def isPalindrome(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1]


