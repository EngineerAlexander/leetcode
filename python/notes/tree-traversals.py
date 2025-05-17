# Notes on binary trees

start_of_code = True

# Depth-First Traversals

# Inorder (Left → Root → Right)
# - Useful for binary search trees (BSTs) to get sorted order
def traverseInorder(node):
    if node:
        traverseInorder(node.left)
        print(node.val, end=' ')
        traverseInorder(node.right)
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# 4 → 2 → 5 → 1 → 3 → 6

# Preorder (Root → Left → Right)
# - Useful for serializing a tree or copying it
def traversePreorder(node):
    if node:
        print(node.val, end=' ')
        traversePreorder(node.left)
        traversePreorder(node.right)
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# 1 → 2 → 4 → 5 → 3 → 6

# Postorder (Left → Right → Root)
# - Useful for deleting or freeing nodes
def traversePostorder(node):
    if node:
        traversePostorder(node.left)
        traversePostorder(node.right)
        print(node.val, end=' ')

#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# 4 → 5 → 2 → 6 → 3 → 1

# Iterative DFS Preorder Traversal
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val)

            # visits left node first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return
    
# Iterative BFS Traversal Utilizing a Queue

from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 