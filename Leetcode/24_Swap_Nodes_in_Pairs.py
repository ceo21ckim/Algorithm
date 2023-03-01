'''
Given a linked list, swap every two adjacent nodes and return its head. You must be solve the problem without modifying the values in the list`s nodes
(i.e., only nodes themselves may be changed.)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

# solution 1
def swapPairs(head):
    node = head  
    i = 0 
    while node:
        if i // 2 == 0 :
            node.val, node.next.val = node.next.val, node.val 
    return head 


# solution 2
def swapPairs(head):
    root = prev = ListNode(None)
    prev.next = head 
    
    while head and head.next :
        b = head.next 
        head.next = b.next 
        b.next = head 
        
        prev.next = b 
        
        head = head.next 
        prev = prev.next.next 
    
    return root.next 


# solution 3 
def swapPairs(head):
    if head and head.next:
        p = head.next 
        
        head.next = swapPairs(p.next)
        p.next = head 
        return p 

    return head 

