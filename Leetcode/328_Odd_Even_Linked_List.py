'''
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

Input: head = [1, 2, 3, 4, 5]
Output: [1, 3, 5, 2, 4]
'''

def oddEvenList(head):
    if head is None:
        return None
    
    # head, head.next 
    odd = head 
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next

    # odd: 1-> 3 -> 5
    # even: 2 -> 4 -> None (break)

    odd.next = even_head 
    # odd: 5, even_head: 2
    # 1 -> 3 -> 5 -> /  2 -> 4 -> None 
    return head 