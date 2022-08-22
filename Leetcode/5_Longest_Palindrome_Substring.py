'''
5. Longest Palindromic Substring
Given a string "s", return the longest palindromic substring in "s".

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''

s = 'babad'
# Use two pointer and expand around the center
# except 
def logestPalindrome(s):
    # 팰린드롬 판별 및 투 포인터 확장.
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left +1:right]
    
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key = len)
    return result

