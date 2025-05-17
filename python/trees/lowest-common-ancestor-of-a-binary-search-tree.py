# Given a binary search tree (BST), find the lowest common 
# ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two 
# nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root.val
        p_val = p.val
        q_val = q.val

        if (cur > p_val) and (cur > q_val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (cur < p_val) and (cur < q_val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
# Time complexity: O(N) for the worst case where we have to traverse the entire tree
# Space complexity: O(N) This is because the maximum amount of space utilized by the 
# recursion stack would be N since the height of a skewed BST could be N.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        p_val = p.val
        q_val = q.val

        while cur:
            parent_val = cur.val
            if (parent_val < p_val) and (parent_val < q_val):
                cur = cur.right
            elif (parent_val > p_val) and (parent_val > q_val):
                cur = cur.left
            else:
                return cur
            
# Time complexity: O(N) for the worst case where we have to traverse the entire tree
# Space complexity: O(1) for the iterative solution