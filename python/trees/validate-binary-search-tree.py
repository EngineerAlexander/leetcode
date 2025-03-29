# Given the root of a binary tree, determine 
# if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only 
# nodes with keys less than the node's key.
# The right subtree of a node contains only 
# nodes with keys greater than the node's key.
# Both the left and right subtrees must also be 
# binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)


        return validate(root, float("-inf"), float("inf"))
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack