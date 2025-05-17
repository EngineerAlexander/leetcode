# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values 
# of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #find smallest and backup k times

        def dfs(node):
            if not node:
                return []

            return dfs(node.left) + [node.val] + dfs(node.right)


        return dfs(root)[k-1]
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack (n = every node)