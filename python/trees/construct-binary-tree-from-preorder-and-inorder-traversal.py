# Given two integer arrays preorder and inorder where preorder 
# is the preorder traversal of a binary tree and inorder is the 
# inorder traversal of the same tree, construct and return the binary tree.

# Constraints:
# preorder and inorder consist of unique values. (IMPORTANT)

# The first value of preorder is the root of the tree.
# In inorder, the values to the left of the root are in the left subtree,
# and the values to the right of the root are in the right subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack