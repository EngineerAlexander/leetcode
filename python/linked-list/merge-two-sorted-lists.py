# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made 
# by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        prehead = ListNode(-1)
        cur = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # link leftover list as-is
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return prehead.next
    
# Time complexity: O(min(N, M)) where N and M are the number of nodes in list1 and list2 respectively.
# Space complexity: O(1)