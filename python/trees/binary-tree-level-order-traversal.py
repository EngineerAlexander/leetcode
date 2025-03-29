# Given the root of a binary tree, return the level 
# order traversal of its nodes' values. (i.e., from 
# left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level):
            if not node:
                return

            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        if not root:
            return []

        levels = []
        dfs(root, 0)

        return levels
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack