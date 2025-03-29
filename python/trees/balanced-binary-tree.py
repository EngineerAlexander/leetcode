# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the 
# depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            if (left_height < 0) or (right_height < 0) or (abs(left_height - right_height) > 1):
                return -1
            else:
                return max(left_height, right_height) + 1
        
        if not root:
            return True

        if height(root) >= 0:
            return True
        else:
            return False
        
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack