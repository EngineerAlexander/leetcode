# Given the root of a binary tree, 
# return the length of the diameter of the tree.
# The diameter of a binary tree is the length of 
# the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxLengthBelow(node):
            if not node:
                return 0

            nonlocal diam
            
            left_length = maxLengthBelow(node.left)
            right_length = maxLengthBelow(node.right)

            diam = max(left_length + right_length, diam)

            return max(left_length, right_length) + 1

        if not root:
            return 0

        diam = 0

        maxLengthBelow(root)

        return diam
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack