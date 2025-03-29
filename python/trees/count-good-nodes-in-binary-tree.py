# Given a binary tree root, a node X in the tree is named 
# good if in the path from root to X there are no nodes 
# with a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS where we keep track of the max on the current path
        def dfs(node, max_seen):
            if not node:
                return

            nonlocal good_nodes

            if max_seen <= node.val:
                good_nodes += 1
            
            if node.left:
                dfs(node.left, max(max_seen, node.val))
            if node.right:
                dfs(node.right, max(max_seen, node.val))

        if not root:
            return 0
        good_nodes = 0
        dfs(root, root.val)
        return good_nodes
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack (n = every node)