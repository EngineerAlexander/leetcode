# Given a binary tree, find the lowest common ancestor 
# (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes 
# p and q as the lowest node in T that has both p and q as 
# descendants (where we allow a node to be a descendant of 
# itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        def recurse_tree(current_node):
            if not current_node:
                return False

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                ans[0] = current_node

            return mid or left or right

        recurse_tree(root)
        return ans[0]
    
# Time complexity: O(N) for the worst case where we have to traverse the entire tree
# Space complexity: O(N) for the recursion stack