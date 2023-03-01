'''
Given the `head` of singly linked list, reverse the list, and return the reversed list.
'''

# solution 1 

def reverseList(head):
    node, prev = head, None
    while node:
        next, node.next = node.next, prev 
        prev, node = node, next 
    return prev 
         