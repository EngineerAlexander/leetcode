# Serialization is the process of converting a data structure or 
# object into a sequence of bits so that it can be stored in a 
# file or memory buffer, or transmitted across a network connection 
# link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization 
# algorithm should work. You just need to ensure that a binary tree 
# can be serialized to a string and this string can be deserialized 
# to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode 
# serializes a binary tree. You do not necessarily need to follow this 
# format, so please be creative and come up with different approaches yourself.

# Constraints:
#The number of nodes in the tree is in the range [0, 104].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        nodeValues = data.split(',')
        self.i = 0

        def construct():
            nodeVal = nodeValues[self.i]
            self.i += 1
            if nodeVal == 'N':
                return None
            node = TreeNode(int(nodeVal))
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()
    
# Time complexity: O(n) to visit every node
# Space complexity: O(n) for the callstack (n = every node)