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

# Using a stack to implement DFS preorder traversal
def traverseDFS(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            print(node.val, end=' ')
            stack.append(node.right)
            stack.append(node.left)