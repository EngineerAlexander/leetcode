# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the 
# same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a 
# node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if (not p) and (not q):
                return True
            elif (not p) or (not q):
                return False
            
            return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        stack = [root]
        while stack:
            cur = stack.pop()

            if isSameTree(cur, subRoot):
                return True

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return False

# Time complexity: O(PQ) because We iterate over every node of the root tree (P), 
# then at each node check if it's identical to subRoot (Q) checks
# Space complexity: O(P+Q) for the worst case stack is full of nodes and callstack is Q deep checking if equal

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "N"
            return f"({node.val},{serialize(node.left)},{serialize(node.right)})"
        
        rootSerialized = serialize(root)
        subRootSerialized = serialize(subRoot)
        return subRootSerialized in rootSerialized
    
# Time complexity: O(P+Q) for the serialization of both trees
# Space complexity: O(P+Q) for the serialized strings of both trees