# Given the root of a binary tree, imagine yourself 
# standing on the right side of it, return the values 
# of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):

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

        res = []
        for layer in levels:
            res.append(layer[-1])

        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node):
            from collections import deque

            if not node:
                return

            queue = deque()
            queue.append((root, 0))
            max_level = 0
            res = [root.val]
            while queue:
                cur, cur_level = queue.popleft()

                if cur_level > max_level:
                    res.append(cur.val)
                    max_level += 1

                if cur.right:
                    queue.append((cur.right, max_level + 1))
                if cur.left:
                    queue.append((cur.left, max_level + 1))

            return res
        
        if not root:
            return []
        return bfs(root)

# First Solution Complexity
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack (n = every node)

# Second Solution Complexity
# Time complexity: O(n) to visit every node
# Space complexity: O(n) because of the queue