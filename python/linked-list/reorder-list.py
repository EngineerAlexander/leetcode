# You are given the head of a singly linked-list. 
# The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. 
# Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev = None
        cur = slow
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp

        # merge lists
        l1 = head
        l2 = prev
        while l2.next:
            l1_next = l1.next
            l1.next = l2
            l1 = l1_next

            l2_next = l2.next
            l2.next = l1
            l2 = l2_next

        return head