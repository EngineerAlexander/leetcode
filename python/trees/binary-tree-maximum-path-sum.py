# A path in a binary tree is a sequence of nodes where each pair of 
# adjacent nodes in the sequence has an edge connecting them. A node 
# can only appear in the sequence at most once. Note that the path 
# does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any 
# non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # At every node, the maxPathSum is max(leftMaxPathSum, leftMaxPathSum + node + rightMaxPathSum, rightMaxPathSum)
        def maxPathSumHelper(node):
            if not node:
                return 0

            nonlocal max_path_sum

            # If subtree contributes a negative sum, ignore it
            left_max_path = max(0, maxPathSumHelper(node.left))
            right_max_path = max(0, maxPathSumHelper(node.right))
            max_path_sum = max(max_path_sum, node.val + left_max_path + right_max_path)

            return node.val + max(left_max_path, right_max_path)

        max_path_sum = float('-inf')
        maxPathSumHelper(root)
        return max_path_sum

# Time complexity: O(n) to visit every node in dfs manner
# Space complexity: O(h) → Call stack depth in recursion (height of the tree).
# In a balanced tree, O(log n); in a skewed tree, O(n).