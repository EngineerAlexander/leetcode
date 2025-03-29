# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfsDepth(node, cur_depth):
            if not node:
                return cur_depth

            left_depth = dfsDepth(node.left, cur_depth + 1)
            right_depth = dfsDepth(node.right, cur_depth + 1)

            return max(left_depth, right_depth)

        return dfsDepth(root, 0)
    
# Time complexity: O(n)
# Space complexity: O(n) for the recursive call stack