'''
You are given the heads of two sorted linked `list1` and `list2`.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first tow lists.
Return the head of the merged linked list.

Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
    
def mergeTwoLists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1 
    
    if l1:
        l1.next = mergeTwoLists(l2.next, l2)
        
    return l1 