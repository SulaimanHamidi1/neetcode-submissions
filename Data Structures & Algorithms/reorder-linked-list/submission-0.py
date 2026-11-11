# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        second = self.reverseList(slow.next)    
        slow.next = None

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        
        
    
    def reverseList(self, head):
        before = None
        
        while head is not None:
            after = head.next
            head.next = before
            before = head
            head = after
        
        return before
