# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        prev = None
        
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        return prev
    
# Time complexity: O(n)
# Space complexity: O(1)