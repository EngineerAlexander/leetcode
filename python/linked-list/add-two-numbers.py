# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse 
# order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading 
# zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2
        carry = 0
        prehead = ListNode(-1)
        ans = prehead
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            cur_sum = carry + val1 + val2
            cur_sum_contribution = cur_sum % 10
            carry = cur_sum // 10
            ans.next = ListNode(cur_sum_contribution)

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            ans = ans.next

        if carry != 0:
            ans.next = ListNode(carry)

        return prehead.next