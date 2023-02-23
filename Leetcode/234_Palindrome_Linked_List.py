'''
Given the `head` of a singly linked list, return `ture` if it is `palindrome` or `false` otherwise.

Input: head = [1, 2, 2, 1]
Output: true
'''
# solution 1
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        deq = deque()

        node = head
        while node is not None:
            deq.append(node.val)
            node = node.next

        if not deq:
            return True 
        
        while len(deq) > 1:
            if deq.popleft() != deq.pop():
                return False
        
        return True

# solution 2
def isPalindrome(head):
    q = []
    
    if not head : 
        return True 
    
    node = head 
    while node is not None:
        q.append(node.val)
        node = node.next 
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False 
            
    return True 

# solution 3 
def isPalindrome(head):
    rev = None
    slow = fast = head 
    
    while fast and fast.next:
        fast = fast.next.next 
        
        rev, rev.next, slow = slow, rev, slow.next 
        
    if fast:
        slow = slow.next 
        
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next 
    
    return not rev 