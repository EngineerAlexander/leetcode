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
        def longestPathBelow(node):
            if not node:
                return 0

            nonlocal max_diam

            left_path = longestPathBelow(node.left)
            right_path = longestPathBelow(node.right)

            max_diam = max(max_diam, left_path + right_path, max_diam)

            return max(left_path, right_path) + 1

        if not root:
            return 0

        max_diam = 0
        longestPathBelow(root)

        return max_diam
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the stack