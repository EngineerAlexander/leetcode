# Adjacency List Representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Adjacency Matrix Representation
graph = [
    [0, 1, 1],  # A → B, C
    [0, 0, 1],  # B → C
    [0, 0, 0]   # C → none
]

# Edge List Representation
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D')
]

# Depth First Search
# 1. Explores as far as possible along each branch before backtracking.
# 2. Implemented using a stack, in recursive the callstack serves this function.
# 3. USES: Detecting cycles, topological sorting, pathfinding.
# 4. Generally uses less memory, stores only the nodes along the current path

# Iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node.val)
            visited.add(node.val)

            # Reversed to keep the order of traversal because stack is LIFO
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Recursive
def dfs_recursive(graph, node, visited = None):
    if not visited:
        visited = set()

    if node in visited:
        return

    print(node.val)
    visited.add(node)

    for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Breadth First Search
# 1. Explores all neighbors of a node before moving to the next level.
# 2. Implemented using a queue to maintain the order of nodes to be explored.
# 3. USES: Finding the shortest path, level-order traversal in trees, network broadcasting.
# 4. Can consume more memory, as it stores all nodes at the current level.

# Iterative
from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Recursive
# Not worth it. Need to manually carry a queue between recursive calls.