# Given the head of a linked list, remove the nth 
# node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prehead = ListNode(-1)
        prehead.next = head

        slow = prehead
        fast = prehead
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # slow at node before one to remove
        slow.next = slow.next.next

        return prehead.next
    
# Time complexity: O(n)
# Space complexity: O(1)