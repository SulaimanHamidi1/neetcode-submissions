# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        dummy = ListNode(0, head)

        tmp = head
        length = 0

        while tmp:
            length += 1
            tmp = tmp.next
        
        curr = dummy
        for i in range(length - n):
            curr = curr.next
        
        curr.next = curr.next.next
        return dummy.next