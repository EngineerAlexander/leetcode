# You are given an array of k linked-lists lists, 
# each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted 
# linked-list and return it.

# Constraints:
# lists[i] is sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
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

        if not l1:
            cur.next = l2
        else:
            cur.next = l1

        return prehead.next

# Time complexity: O(N log k) where N is the total number of nodes and k is the number of linked lists.
# Space complexity: O(1) since we are reusing existing nodes to merge lists.